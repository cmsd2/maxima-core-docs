## Analysis

<!-- category: Calculus -->
<!-- keywords: antid -->
<!-- signatures: antid(expr, x, u(x)) -->
### Function: antid (expr, x, u(x))

Gibt eine Liste mit zwei Elementen zuruck aus denen die Stammfunktion des 
Ausdrucks *expr* mit der Variablen *x* konstruiert werden kann.  Der
Ausdruck *expr* kann eine unbekannte Funktion *u* und deren Ableitungen
enthalten.  Ist *L* das Ergebnis der Funktion `antid`, dann ist der 
Ausdruck `L[1]+ 'integrate(L[2], x)` die gesuchte 
Stammfunktion des Ausdrucks *expr* mit der Variablen *x*.


Kann `antid` die Stammfunktion vollstandig bestimmen, ist das zweite
Element der Liste Null.  Hat `antid` keinerlei Erfolg, ist das erste 
Element der Liste Null.  In anderen Fallen enthalt das erste Elemente den
integrierbaren Anteil des Ausdrucks *expr* und das zweite Element den nicht
integrierbaren Anteil des Ausdrucks.


Mit dem Kommando `load("antid")` wird die Funktion geladen.


`antid` steht in folgender Beziehung zur Funktion `antidiff`.  Ist
*L* die Liste mit den Ergebnissen der Funktion `antid`, dann hat die
Funktion `antidiff` das Ergebnis `L[1] + 'integrate(L[2], x)` mit *x* als der Variablen des Ausdrucks *expr*.


Beispiele:



```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

See also: `antidiff`.

<!-- category: Calculus -->
<!-- keywords: antidiff -->
<!-- signatures: antidiff(expr, x, u(x)) -->
### Function: antidiff (expr, x, u(x))

Gibt die Stammfunktion des Ausdrucks *expr* mit der Variablen *x* 
zuruck.  Der Ausdruck *expr* kann eine unbekannte Funktion *u* und 
deren Ableitungen enthalten.


Kann `antidiff` die Stammfunktion nicht oder nur teilweise bestimmen,
enthalt das Ergebnis das Integral des nicht bestimmbaren Anteils.


Mit dem Kommando `load("antid")` wird die Funktion geladen.


`antidiff` steht in folgender Beziehung zur Funktion `antid`.  Ist 
*L* die Liste mit den Ergebnissen der Funktion `antid`, dann hat die
Funktion `antidiff` das Ergebnis `L[1] + 'integrate(L[2], x)` mit *x* als der Variablen des Ausdrucks *expr*.


Fur Beispiele und weitere Ausfuhrungen siehe die Funktion `antid`.

See also: `antid`.

<!-- category: Calculus -->
<!-- keywords: at -->
<!-- signatures: at(expr, [eqn_1, ..., eqn_n]), at(expr, eqn) -->
### Function: at (expr, [eqn_1, ..., eqn_n])

Wertet den Ausdruck *expr* aus, wobei dessen Variablen die Werte annehmen, 
die in der Liste der Gleichungen `[eqn_1, ..., eqn_n]` 
oder in der einzelnen Gleichung *eqn* angegeben sind.


Wenn ein Teilausdruck von einer Variablen abhangt, fur die ein Wert 
angegeben ist, aber kein `atvalue`, und er auch sonst nicht ausgewertet 
werden kann, dann wird von `at` eine Substantivform zuruckgegeben.


`at` fuhrt mehrfache Ersetzungen parallel aus.


Siehe auch `atvalue`.  Fur andere Funktionen, die Ersetzungen 
ausfuhren, siehe weiterhin `subst` und `ev`.


Beispiele:



```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);
                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

See also: `atvalue`, `subst`, `ev`.

<!-- category: Calculus -->
<!-- keywords: atomgrad -->
<!-- signatures: atomgrad -->
### Variable: atomgrad

Wird fur ein Symbol eine Ableitung mit der Funktion `gradef` definiert,
dann erhalt das Symbol die Eigenschaft `atomgrad`.

See also: `gradef`.

<!-- category: Calculus -->
<!-- keywords: atvalue -->
<!-- signatures: atvalue(expr, [x_1=a_1, ..., x_m=a_m], c), atvalue(expr, x_1=a_1, c) -->
### Function: atvalue (expr, [x_1=a_1, ..., x_m=a_m], c)

Dem Ausdruck *expr* wird der Wert *c* am Punkt `x = a`
zugewiesen.  Typischerweise werden Randwerte mit der Funktion `atvalue`
definiert.


Der Ausdruck *expr* ist entweder eine Funktion `f(x_1, ..., x_m)` oder die Ableitung einer Funktion `diff(f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`.  Die Argumente
mussen explizit auftreten.  *n_i* ist die Ordnung der Ableitung 
bezuglich der Variablen *x_i*.


Die Randwerte werden durch die Liste `[x_1 = a_1, ..., x_m = a_m]` definiert.  Eine einzelne Gleichung muss nicht als Liste 
angegeben werden.


`printprops([f_1, f_2, ...], atvalue)` zeigt die Randwerte der
Funktionen `f_1, f_2, ...` wie sie mit der Funktion 
`atvalue` definiert wurden.  `printprops (f, atvalue)` zeigt
nur die Randwerte fur die Funktion *f*.  `printprops (all, atvalue)`
zeigt die Randwerte aller Funktionen.


Die Symbole `@1`, `@2`, ... reprasentieren die Variablen 
*x_1*, *x_2*, ..., wenn die Randwerte angezeigt werden.


`atvalue` wertet die Argumente aus.  `atvalue` gibt den Randwert
*c* zuruck.


Beispiele:



```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);

                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Calculus -->
<!-- keywords: bc2 -->
<!-- signatures: bc2(solution, xval1, yval1, xval2, yval2) -->
### Function: bc2 (solution, xval1, yval1, xval2, yval2)

Lost das Randwertproblem einer Differentialgleichung 2. Ordnung.  Das
Argument *solution* ist eine allgemeine Losung, wie sie von der Funktion
`ode2` zuruckgegeben wird.  *xval1* gibt den Wert der unabhangigen
Variablen im ersten Randpunkt an.  Der Randwert wird als ein Ausdruck
`x = x1` angegeben.  Das Argument *yval1* gibt den Wert
der abhangigen Variablen in diesem Punkt an.  Der Randwert wird als
`y = y1` angegeben.  Mit den Argumenten *xval2* und
*yval2* werden die entsprechenden Werte an einem zweiten Randpunkt
angegeben.


Siehe die Funktion `ode2` fur Beispiele.

See also: `ode2`.

<!-- category: Calculus -->
<!-- keywords: cartan -->
<!-- signatures: cartan -->
### Function: cartan

The exterior calculus of differential forms is a basic tool of differential 
geometry developed by Elie Cartan and has important applications in the theory 
of partial differential equations.  The `cartan` package implements the 
functions `ext_diff` and `lie_diff`, along with the operators 
`~` (wedge product) and `|` (contraction of a form with a vector.)
Type `demo (tensor)` to see a brief description of these commands along 
with examples.


`cartan` was implemented by F.B. Estabrook and H.D. Wahlquist.

<!-- category: Calculus -->
<!-- keywords: changevar -->
<!-- signatures: changevar(expr, f(x,y), y, x) -->
### Function: changevar (expr, f(x,y), y, x)

Fuhrt eine Substitution der Integrationsvariablen, die als *f(x,y)=0* 
angegeben wird, fur die Variable *x* in allen Integralen durch, die in 
*expr* enthalten sind.  Die neue Variable ist *y*.




```maxima
(%i1) assume(a > 0)$

(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     [    sqrt(a) sqrt(y)
(%o2)                I  %e                dy
                     ]
                     /
                      0


(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     [                abs(z)
                   2 I            z %e       dz
                     ]
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


Ein Ausdruck mit einem Integral in einer Substantivform `'integrate` wie
im obigen Beispiel kann mit der Funktion `ev` und dem Auswertungsschalter
`nouns` ausgewertet werden.  Das Beispiel von oben kann zum Beispiel mit
`ev(%o3, nouns)` ausgewertet werden.


Mit `changevar` konnen auch die Indizes einer Summe oder eines Produktes
substituiert werden.  Dabei muss beachtet werden, dass nur lineare 
Verschiebungen, wie zum Beispiel `i = j + ...`, eine korrekte Substitution 
fur Summen und Produkte sind.



```maxima
(%i4) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ====
                         \         i - 2
(%o4)                     >    a  x
                         /      i
                         ====
                         i = 0


(%i5) changevar (%, i-2-n, n, i);
                        inf
                        ====
                        \               n
(%o5)                    >      a      x
                        /        n + 2
                        ====
                        n = - 2
```

See also: `ev`, `nouns`.

<!-- category: Calculus -->
<!-- keywords: dblint -->
<!-- signatures: dblint(f, r, s, a, b) -->
### Function: dblint (f, r, s, a, b)

Eine Routine, um ein bestimmtes doppeltes Integral mit der Simpsonschen Regel 
numerisch zu berechnen.



$$
\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx.
$$


```maxima
b  s(x)
     /  /
     [  [
     I  I     f(x, y) dy dx
     ]  ]
     /  /
      a  r(x)
```


Die Funktion *f* muss eine Funktion von zwei Variablen sein.  *r* und 
*s* mussen Funktionen einer Variablen sein.  *a* und *b* sind 
Gleitkommazahlen.  Die Optionsvariablen `dblint_x` und `dblint_y` 
kontrollieren die Anzahl der Unterteilungen des Integrationsintervalls fur
den Simpsonschen Algorithmus.  Der Standardwert ist jeweils 10.


Das Kommando `demo(dblint)` zeigt ein Beispiel.


Die numerischen Funktionen des Pakets `QUADPACK` sind gegenuber 
`dblint` zu bevorzugen.

<!-- category: Calculus -->
<!-- keywords: defint -->
<!-- signatures: defint(expr, x, a, b) -->
### Function: defint (expr, x, a, b)

Sucht das bestimmte Integral eines Ausdrucks *expr* fur die 
Integrationsvariable *x* in den Grenzen *a* und *b*.  Diese Funktion
wird ausgefuhrt, wenn ein bestimmtes Integral mit der Funktion 
`integrate` gesucht wird.


`defint` gibt einen symbolischen Ausdruck als Ergebnis zuruck.  Ist das 
Integral divergent, generiert Maxima eine Fehlermeldung.  Kann `defint` 
keine Losung finden, wird eine Substantivform zuruckgegeben.

See also: `integrate`.

<!-- category: Calculus -->
<!-- keywords: del -->
<!-- signatures: del(x) -->
### Function: del (x)

`del(x)` reprasentiert das Differential der Variablen *x*.


`diff` gibt Ausdrucke zuruck, die Differentiale enthalten, wenn keine 
Variablen angegeben sind, nach denen abgeleitet werden soll.  In diesem Fall
gibt `diff` das totale Differential zuruck.


Beispiele:



```maxima
(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x
(%i2) diff (exp (x*y));
                     x y              x y
(%o2)            x %e    del(y) + y %e    del(x)
(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

<!-- category: Calculus -->
<!-- keywords: delta -->
<!-- signatures: delta(t) -->
### Function: delta (t)

Die Diracsche Delta-Funktion.


Maxima kennt die Delta-Funktion nur im Zusammenhang mit 
Laplace-Trans­for­ma­tio­nen.  Siehe `laplace`.


Beispiel:





```maxima
(%i1) laplace (delta (t - a) * sin(b*t), t, s);
Is  a  positive, negative, or zero?

p;
                                   - a s
(%o1)                   sin(a b) %e
```

See also: `laplace`.

<!-- category: Calculus -->
<!-- keywords: dependencies -->
<!-- signatures: dependencies -->
### Variable: dependencies

Standardwert: `[]`


`dependencies` ist eine Liste der Symbole, fur die eine Abhangigkeit 
mit den Funktionen `depends` oder `gradef` definiert wurde.  Siehe
`depends` und `gradef`.

See also: `depends`, `gradef`.

<!-- category: Calculus -->
<!-- keywords: depends -->
<!-- signatures: depends(f_1, x_1, ..., f_n, x_n) -->
### Function: depends (f_1, x_1, ..., f_n, x_n)

Definiert die Abhangigkeit einer Funktion *f* von einer Variablen *x*.
Ist keine Abhangigkeit definiert, dann hat die Ableitung `diff(f, x)` das 
Ergebnis Null.  Wird mit dem Kommando `depends(f, x)` definiert, dass die
Funktion *f* von der Variablen *x* abhangt, dann ist das Ergebnis der
Ableitung die Substantivform `'diff(f,x,1)`.


Jedes Argument *f_1*, *x_1*, ... kann der Name einer Variablen, 
eines Arrays oder eine Liste mit Namen sein.  Jedes Symbol *f_i* hangt ab 
von den Symbolen der Liste *x_i*.  Ist eines der Symbole *f_i* der Name
eines Arrays, dann hangen alle Elemente des Arrays von *x_i* ab.


`diff` erkennt indirekte Abhangigkeiten und wendet fur diesen Fall
die Kettenregel an.


`remove(f, dependency)` entfernt alle Abhangigkeiten, die fur
*f* definiert wurden.


`depends` gibt eine Liste der Abhangigkeiten zuruck.  Die 
Abhangigkeiten werden in die Informationsliste `dependencies` 
eingetragen.  `depends` wertet die Argumente aus.


Die Funktion `diff` ist die einzige Maxima-Funktion, die Abhangigkeiten
erkennt, die mit `depends` definiert wurden.  Andere Funktionen wie
`integrate` oder `laplace` erkennen keine Abhangigkeiten, die mit
der `depends` definiert wurden.  Fur diese Funktionen mussen die
Abhangigkeiten explizit angegeben werden, zum Beispiel als
`integrate(f(x), x)`.


Beispiele:



```maxima
(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]
(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]
(%i3) depends (u, t);
(%o3)                        [u(t)]
(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]
(%i5) diff (r.s, u);
                         dr           ds
(%o5)                    -- . s + r . --
                         du           du
```



```maxima
(%i6) diff (r.s, t);
                      dr du           ds du
(%o6)                 -- -- . s + r . -- --
                      du dt           du dt
```



```maxima
(%i7) remove (r, dependency);
(%o7)                         done
(%i8) diff (r.s, t);
                                ds du
(%o8)                       r . -- --
                                du dt
```

See also: `diff`, `integrate`, `laplace`.

<!-- category: Calculus -->
<!-- keywords: derivabbrev -->
<!-- signatures: derivabbrev -->
### Variable: derivabbrev

Standardwert: `false`


Hat `derivabbrev` den Wert `true`, werden symbolische Ableitungen
mit einem tiefgestellten Index angezeigt.  Ansonsten werden Ableitungen als
`dy/dx` angezeigt.


Beispiel:



```maxima
(%i1) derivabbrev:false$

(%i2) 'diff(y,x);
                               dy
(%o2)                          --
                               dx
(%i3) derivabbrev:true$

(%i4) 'diff(y,x);
(%o4)                          y
                                x
```

<!-- category: Calculus -->
<!-- keywords: derivdegree -->
<!-- signatures: derivdegree(expr, y, x) -->
### Function: derivdegree (expr, y, x)

Gibt die hochste Ableitung des Arguments *y* in Bezug auf die Variable
*x* zuruck, die in dem Ausdruck *expr* enthalten ist.


Beispiel:



```maxima
(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx
(%i2) derivdegree (%, y, x);
(%o2)                           2
```

<!-- category: Calculus -->
<!-- keywords: derivlist -->
<!-- signatures: derivlist(var_1, ..., var_k) -->
### Function: derivlist (var_1, ..., var_k)

`derivlist` ist ein Auswertungsschalter fur die Funktion `ev`.
`ev` fuhrt nur die Ableitungen in Bezug auf die angegebenen Variablen
*var_1*, ..., *var_k* aus.  Siehe auch `ev`.

See also: `ev`.

<!-- category: Calculus -->
<!-- keywords: derivsubst -->
<!-- signatures: derivsubst -->
### Variable: derivsubst

Standardwert: `false`


Hat `derivsubst` den Wert `true`, werden Substitutionen auch in 
Ausdrucke mit Ableitungen ausgefuhrt.  Zum Beispiel hat dann
`subst(x, 'diff(y, t), 'diff(y, t, 2))` das Ergebnis `'diff(x, t)`.

<!-- category: Calculus -->
<!-- keywords: desolve -->
<!-- signatures: desolve(eqn, x), desolve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: desolve (eqn, x)

Die Funktion `desolve` lost lineare Systeme gewohnlicher
Differentialgleichungen mit Hilfe der Methode der Laplacetransformation.  Die
Argumente *eqn_i* sind die Differentialgleichungen mit den abhangigen
Variablen *x_1*, ..., *x_n*.  Die funktionale Abhangigkeit der
Variablen *x_1*, ..., *x_n* zum Beispiel von einer Variablen *x*
muss explizit fur die Variablen und ihrer Ableitungen angegeben werden.  Zum
Beispiel ist sind die folgenden zwei Gleichungen keine korrekte Definition: 



```maxima
eqn_1: 'diff(f,x,2) = sin(x) + 'diff(g,x);
eqn_2: 'diff(f,x) + x^2 - f = 2*'diff(g,x,2);
```




Eine korrekte Definition der zwei Gleichungen ist



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```




Die Funktion `desolve` wird dann folgendermaßen aufgerufen



```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```





Sind Anfangswerte fur `x=0` bekannt, konnen diese mit der Funktion
`atvalue` vor dem Aufruf der Funktion `desolve` angegeben werden.



```maxima
(%i1) 'diff(f(x),x)='diff(g(x),x)+sin(x);
                 d           d
(%o1)            -- (f(x)) = -- (g(x)) + sin(x)
                 dx          dx
(%i2) 'diff(g(x),x,2)='diff(f(x),x)-cos(x);

                  2
                 d            d
(%o2)            --- (g(x)) = -- (f(x)) - cos(x)
                   2          dx
                 dx

(%i3) atvalue('diff(g(x),x),x=0,a);
(%o3)                           a
(%i4) atvalue(f(x),x=0,1);
(%o4)                           1
(%i5) desolve([%o1,%o2],[f(x),g(x)]);

                  x
(%o5) [f(x) = a %e  - a + 1, g(x) = 
                                                x
                                   cos(x) + a %e  - a + g(0) - 1]

(%i6) [%o1,%o2],%o5,diff;
             x       x      x                x
(%o6)   [a %e  = a %e , a %e  - cos(x) = a %e  - cos(x)]
```




Kann `desolve` keine Losung finden, ist die Ruckgabe `false`.

See also: `atvalue`.

<!-- category: Calculus -->
<!-- keywords: diff -->
<!-- signatures: diff(expr, x_1, n_1, ..., x_m, n_m), diff(expr, x, n), diff(expr, x), diff(expr) -->
### Function: diff (expr, x_1, n_1, ..., x_m, n_m)

Gibt die Ableitungen oder Differentiale des Ausdrucks *expr* in Bezug auf
alle oder einige der Variablen des Ausdrucks zuruck.


`diff(expr, x, n)` gibt die n-te Ableitung des Ausdrucks
*expr* in Bezug auf die Variable *x* zuruck.


`diff(expr, x_1, n_1, ..., x_m, n_m)` gibt
die partielle Ableitung des Ausdrucks *expr* in Bezug auf die Variablen
*x_1*, ..., *x_m* zuruck.  Dies ist aquivalent zu `diff(... (diff(expr, x_m, n_m) ...), x_1, n_1)`.


`diff(expr, x)` gibt die erste Ableitung des Ausdrucks 
*expr* in Bezug auf die Variable *x* zuruck.


`diff(expr)` gibt das totale Differential des Ausdrucks *expr*
zuruck.  Siehe auch `del`.


Wenn die Ableitungen nicht ausgefuhrt werden sollen, kann der
`'` `'` verwendet werden, um eine Substantivform der
Ableitung zu erhalten.


Hat `derivabbrev` den Wert `true`, werden symbolische Ableitungen
mit einem tiefgestelltem Index angezeigt.  Ansonsten werden Ableitungen als
`dy/dy` angezeigt.


`diff` ist auch ein Auswertungsschalter fur die Funktion `ev`.  Das 
Kommando `ev(expr), diff` bewirkt, dass alle Ableitungen ausgefuhrt 
werden, die im Ausdruck *expr* enthalten sind.  Siehe auch die Funktion 
`ev`.


`derivative` ist ein Alias-Name der Funktion `diff`.


Beispiele:



```maxima
(%i1) diff (exp (f(x)), x, 2);

                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx

(%i2) derivabbrev: true$
(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        [
(%o3)                   I     f(x, y) dy
                        ]
                        /
                         g(x)
(%i4) diff (%, x);
       h(x)
      /
      [
(%o4) I     f(x, y)  dy + f(x, h(x)) h(x)  - f(x, g(x)) g(x)
      ]            x                     x                  x
      /
       g(x)
```





For the tensor package, the following modifications have been incorporated:



1. The derivatives of any indexed objects in *expr* will have the 
variables *x_i* appended as additional arguments.  Then all the 
derivative indices will be sorted.
2. The *x_i* may be integers from 1 up to the value of the variable
`dimension` [default value: 4].  This will cause the differentiation to
be carried out with respect to the *x_i*’th member of the list 
`coordinates` which should be set to a list of the names of the 
coordinates, e.g., `[x, y, z, t]`.  If `coordinates` is bound to an 
atomic variable, then that variable subscripted by *x_i* will be used for
the variable of differentiation.  This permits an array of coordinate names 
or subscripted names like `X[1]`, `X[2]`, ... to be used.  If 
`coordinates` has not been assigned a value, then the variables will be 
treated as in (1) above.

See also: `del`, `'`, `derivabbrev`, `ev`.

<!-- category: Calculus -->
<!-- keywords: erfflag -->
<!-- signatures: erfflag -->
### Variable: erfflag

Standardwert: `true`


Hat `erfflag` den Wert `false`, wird von der Funktion `risch`
die Fehlerfunktion `erf` nicht in die Losung eingefuhrt.

See also: `risch`, `erf`.

<!-- category: Calculus -->
<!-- keywords: gradef -->
<!-- signatures: gradef(f(x_1, ..., x_n), g_1, ..., g_m), gradef(a, x, expr) -->
### Function: gradef (f(x_1, ..., x_n), g_1, ..., g_m)

Definiert eine partielle Ableitung der Funktion *f* oder Variablen *a*.


Das Kommando `gradef(f(x_1, ..., x_n), g_1, ..., g_m)` definiert die partielle Ableitung `df/dx_i` als
*g_i*.  *g_i* ist ein Ausdruck.  *g_i* kann ein Funktionsaufruf
sein, aber nicht der Name einer Funktion.  Die Anzahl der partiellen Ableitungen
*m* kann kleiner als die Anzahl der Argumente *n* sein.


`gradef(a, x, expr)` definiert die Ableitung der
Variablen *a* in Bezug auf die Variable *x* als *expr*.  Wie mit der
Funktion `depends` wird *a* als abhangig von *x* deklariert.  Die
Abhangigkeit wird in die Liste `dependencies` eingetragen.  Siehe auch
`depends`.


Bis auf das erste Argument werden die Argumente der Funktion `gradef` 
ausgewertet.  `gradef` gibt die Funktion oder Variable zuruck, fur die 
eine partielle Ableitung definiert wurde.


`gradef` kann die Ableitungen von vorhandenen Maxima-Funktionen neu 
definieren.  Zum Beispiel definiert `gradef(sin(x), sqrt (1 - sin(x)^2))`
eine neue Ableitung der Sinusfunktion.


`gradef` kann keine partiellen Ableitungen fur indizierte Funktionen
definieren.


`printprops([f_1, ..., f_n], gradef)` zeigt die mit 
`gradef` definierten partiellen Ableitungen der Funktionen *f_1*, 
..., *f_n* an und `printprops([a_n, ..., a_n], atomgrad)` zeigt die mit `gradef` definierten partiellen Ableitungen der 
Variablen *a_n*, ..., *a_n* an.  Siehe `printprops`.


`gradefs` ist eine Informationsliste, die die Funktionen enthalt, fur
die mit `gradef` eine Ableitung definierte wurde.  Die Liste enthalt 
keine Variablen, fur die Ableitungen definiert wurden.

See also: `depends`, `printprops`, `gradefs`.

<!-- category: Calculus -->
<!-- keywords: gradefs -->
<!-- signatures: gradefs -->
### Variable: gradefs

Standardwert: `[]`


`gradefs` ist eine Liste der Funktionen, fur die eine Ableitung mit der
Funktion `gradef` definiert wurde.

See also: `gradef`.

<!-- category: Calculus -->
<!-- keywords: ic1 -->
<!-- signatures: ic1(solution, xval, yval) -->
### Function: ic1 (solution, xval, yval)

Lost das Anfangswertproblem fur eine Differentialgleichung 1. Ordnung.
Das Argument *solution* ist eine allgemeine Losung der
Differentialgleichung, wie sie von der Funktion `ode2` zuruckgegeben
wird.  Mit dem Argument *xval* wird der Anfangswert der unabhangigen
Variablen in der Form `x = x0` angegeben.  Mit dem Argument
*yval* wird der Anfangswert der unabhangigen Variablen in der Form
`y = y0` angegeben.




Siehe die Funktion `ode2` fur ein Beispiel.

See also: `ode2`.

<!-- category: Calculus -->
<!-- keywords: ic2 -->
<!-- signatures: ic2(solution, xval, yval, dval) -->
### Function: ic2 (solution, xval, yval, dval)

Lost das Anfangswertproblem fur eine Differentialgleichung 2. Ordnung.
Das Argument *solution* ist eine allgemeine Losung der
Differentialgleichung, wie sie von der Funktion `ode2` zuruckgegeben
wird.  Mit dem Argument *xval* wird der Anfangswert der unabhangigen
Variablen in der Form `x = x0` angegeben.  Mit dem Argument
*yval* wird der Anfangswert der abhangigen Variablen in der Form
`y = y0` angegeben.  Mit dem Argument *dval* wird der
Anfangswert der ersten Ableitung der abhangigen Variablen nach der
unabhangigen Variablen in der Form `diff(y,x) = dy0`
angegeben.  Dem Symbol `diff` muss kein `'` `'`
vorangestellt werden.




Siehe auch `ode2` fur ein Beispiel.

See also: `'`, `ode2`.

<!-- category: Calculus -->
<!-- keywords: ilt -->
<!-- signatures: ilt(expr, s, t) -->
### Function: ilt (expr, s, t)

Berechnet die Inverse Laplace-Transformation des Ausdrucks *expr* fur die
Variable *s* und den Parameter *t*.  *expr* muss eine rationale
Funktion sein, in deren Nenner nur lineare und quadratische Faktoren auftreten.
Mit den Funktionen `laplace` und `ilt` sowie den Funktionen
`solve` oder `linsolve` konnen lineare Differentialgleichungen oder
Systeme von linearen Differentialgleichungen gelost werden.



```maxima
(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             [                                    2
(%o1)        I  f(t - x) sinh(a x) dx + b f(t) = t
             ]
             /
              0


(%i2) laplace (%, t, s);
                               a laplace(f(t), t, s)   2
(%o2)  b laplace(f(t), t, s) + --------------------- = --
                                       2    2           3
                                      s  - a           s


(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s


(%i4) ilt (rhs (first (%)), s, t);
Is  a b (a b - 1)  positive, negative, or zero?

pos;
               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a

                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a
```

See also: `laplace`, `solve`, `linsolve`.

<!-- category: Calculus -->
<!-- keywords: intanalysis -->
<!-- signatures: intanalysis -->
### Variable: intanalysis

Standardwert: `true`


Hat `intanalysis` den Wert `true`, sucht Maxima nach Polen in einem 
Integranden.  Existieren solche, wird der Cauchysche Hauptwert des Integrals
bestimmt.  Hat `intanalysis` den Wert `false`, wird die Integration
unter der Annahme ausgefuhrt, dass das Integral keine Pole im 
Integrationsbereich hat.


Siehe auch `ldefint`.


Beispiele:


Maxima kann das folgende Integral losen, wenn `intanalysis` den Wert
`false` hat.



```maxima
(%i1) integrate(1/(sqrt(x)+1),x,0,1);

                                1
                               /
                               [       1
(%o1)                          I  ----------- dx
                               ]  sqrt(x) + 1
                               /
                                0


(%i2) integrate(1/(sqrt(x)+1),x,0,1),intanalysis:false;
(%o2)                            2 - 2 log(2)

(%i3) integrate(cos(a)/sqrt((tan(a))^2 +1),a,-%pi/2,%pi/2);
The number 1 isn't in the domain of atanh
 -- an error. To debug this try: debugmode(true);

(%i4) intanalysis:false$
(%i5) integrate(cos(a)/sqrt((tan(a))^2+1),a,-%pi/2,%pi/2);
                                      %pi
(%o5)                                 ---
                                       2
```

See also: `ldefint`.

<!-- category: Calculus -->
<!-- keywords: integrate -->
<!-- signatures: integrate(expr, x), integrate(expr, x, a, b) -->
### Function: integrate (expr, x)

Sucht die symbolische Losung des Integrals fur den Ausdruck *expr* und
der Integrationsvariablen *x*.  `integrate(expr, x)` lost
das unbestimmte Integral.


`integrate(expr, x, a, b)` sucht die Losung des
bestimmten Integrals in den Integrationsgrenzen *a* und *b*.  Die
Integrationsgrenzen durfen die Integrationsvariable *x* nicht enthalten.
Fur die Integrationsgrenzen muss nicht gelten *a* < *b*.  Sind die
Integrationsgrenzen gleich, dann ist das Ergebnis der Integration Null.


Fur die numerische Losung von Integralen siehe die Funktion
`quad_qag` und verwandte Funktionen.  Residuen eines Integranden konnen
mit der Funktion `residue` berechnet werden.  Einen alternativen
Algorithmus fur das Losen von Integralen, die im Integranden eine unbekannte
Funktion und deren Ableitung enthalten, bieten die Funktionen `antid` und
`antidiff`.


Findet `integrate` keine Losung wird eine Substantivform oder ein
Ausdruck mit einer oder mehreren Substantivformen zuruckgegeben.


Soll das Integral nicht sofort berechnet werden, kann die Substantivform des
Integrals angegeben werden, zum Beispiel `'integrate(expr, x)`.
Die Berechnung des Integrals ist dann mit Funktion `ev` und dem
Auswertungsschalter `nouns` moglich.




































Die Abhangigkeit der Funktionen im Integranden von Variablen muss explizit zum
Beispiel mit `f(x)` angegeben werden.  `integrate` beachtet keine
Abhangigkeit die mit der Funktion `depends` definiert werden.


Benotigt `integrate` Informationen zu einem Parameter, die nicht aus dem
aktuellen Kontext abgeleitet werden konnen, wird der Nutzer nach den fehlenden
Informationen gefragt.


`integrate` ist standardmaßig nicht als linear deklariert.  Siehe
`declare` und `linear`.


Nur in einigen speziellen Fallen wendet `integrate` die Methode der
partiellen Integration an.


Beispiele:


Elementare unbestimmte und bestimme Integrale.



```maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3


(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )


(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5


(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```


Gebrauch von `assume` und interaktive Fragen.



```maxima
(%i1) assume (a > 1)$

(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
    2 a + 2
Is  -------  an integer?
       5

no;
Is  2 a - 3  positive, negative, or zero?

neg;
                                   3
(%o2)                  beta(a + 1, - - a)
                                   2
```


Substitution der Integrationsvariablen.  In diesem Beispiel werden zwei 
verschiedene Substitutionen vorgenommen.  Zuerst wird eine Ableitung der 
Funktion mit der Funktion `gradef` definiert.  Die andere nutzt die 
Ableitung `diff(r(x))` einer unbekannten Funktion `r(x)`.



```maxima
(%i3) gradef (q(x), sin(x^2));
(%o3)                         q(x)


(%i4) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o4)                ----------------------
                            q(r(x))


(%i5) integrate (%, x);
(%o5)                     log(q(r(x)))
```


Die Losung enthalt eine Substantivform fur das Integral einer rationalen 
Funktion.  Siehe auch `integrate_use_rootsof` fur Informationen zu
Integralen von rationalen Funktionen.



```maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4


(%i2) integrate (1/%, x);
                              /  2
                              [ x  + 4 x + 18
                              I ------------- dx
                              ]  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73
```


Definition einer Funktion als ein Integral.  Die rechte Seite einer
Funktionsdefinition wird nicht ausgewertet.  Daher enthalt die 
Funktionsdefinition das Integral in einer Substantivform.  Der
`''` `''` erzwingt die Auswertung der
Substantivform.



```maxima
(%i1) f_1(a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)


(%i2) ev(f_1 (7), nouns);
(%o2)                          600


(%i3) /* Note parentheses around integrate(...) here */
      f_2(a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4


(%i4) f_2(7);
(%o4)                          600
```

See also: `quad_qag`, `residue`, `antid`, `antidiff`, `ev`, `nouns`, `depends`, `declare`, `linear`, `integrate_use_rootsof`, `''`.

<!-- category: Calculus -->
<!-- keywords: integrate_use_rootsof -->
<!-- signatures: integrate_use_rootsof -->
### Variable: integrate_use_rootsof

Standardwert: `false`


Hat `integrate_use_rootsof` den Wert `true` und der Nenner einer
rationalen Funktion kann nicht faktorisiert werden, dann gibt
`integrate` ein Integral zuruck, das eine Summe uber die unbekannten
Wurzeln des Nenners enthalt.


Hat zum Beispiel `integrate_use_rootsof` den Wert `false`, gibt
`integrate` im Folgenden ein Losung zuruck, die eine Substantivform
enthalt.



```maxima
(%i1) integrate_use_rootsof: false$

(%i2) integrate (1/(1+x+x^5), x);
        /  2
        [ x  - 4 x + 5
        I ------------ dx                            2 x + 1
        ]  3    2                2            5 atan(-------)
        / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2)   ----------------- - --------------- + ---------------
                7                 14             7 sqrt(3)
```


Mit dem Wert `true` fur die Optionsvariable `integrate_use_rootsof`
wird das ungeloste Integral als eine Summe uber die Wurzeln des Nenners der
rationalen Funktion zuruckgegeben.



```maxima
(%i3) integrate_use_rootsof: true$

(%i4) integrate (1/(1+x+x^5), x);
      ====        2
      \       (%r4  - 4 %r4 + 5) log(x - %r4)
       >      -------------------------------
      /                    2
      ====            3 %r4  - 2 %r4
                      3    2
      %r4 in rootsof(x  - x  + 1)
(%o4) ----------------------------------------------------------
               7

                                                      2 x + 1
                                  2            5 atan(-------)
                             log(x  + x + 1)          sqrt(3)
                           - --------------- + ---------------
                                   14             7 sqrt(3)
```


Alternativ kann der Nutzer die Wurzeln des Nenners separat berechnen und den
Integranden mit Hilfe der Wurzeln ausdrucken.  Zum Beispiel als 
`1/((x - a)*(x - b)*(x - c))` oder `1/((x^2-(a+b)*x + a*b)*(x - c))`
fur ein kubisches Polynom mit drei Nullstellen im Nenner.  Auf diese Weise
kann Maxima in einigen Fallen eine Losung fur ein Integral finden.

See also: `integrate`.

<!-- category: Calculus -->
<!-- keywords: integration_constant -->
<!-- signatures: integration_constant -->
### Variable: integration_constant

Standardwert: `%c`


Wird eine symbolische Integrationskonstante fur die Losung eines Integrals
benotigt, erzeugt Maxima diese durch Verkettung des Symbols 
`integration_constant` mit einer laufenden Nummer, die der Wert der
Optionsvariablen `integration_constant_counter` ist.


Der Optionsvariablen `integration_constant` kann ein beliebiges Symbol
zugewiesen werden.


Beispiele:



```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integration_constant : 'k;
(%o2)                           k


(%i3) integrate (x^2 = 1, x);
                            3
                           x
(%o3)                      -- = x + k2
                           3
```

See also: `integration_constant_counter`.

<!-- category: Calculus -->
<!-- keywords: integration_constant_counter -->
<!-- signatures: integration_constant_counter -->
### Variable: integration_constant_counter

Standardwert: 0


Wird eine symbolische Integrationskonstante fur die Losung eines Integrals
benotigt, erzeugt Maxima diese durch Verkettung des Symbols 
`integration_constant` mit einer laufenden Nummer, die der Wert der
Optionsvariablen `integration_constant_counter` ist.


Der Wert der Systemvariablen `integration_constant_counter` wird vor der
Erzeugung der Integrationskonstanten erhoht.


Beispiele:



```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integrate (x^2 = 1, x);
                           3
                          x
(%o2)                     -- = x + %c2
                          3


(%i3) reset (integration_constant_counter);
(%o3)            [integration_constant_counter]


(%i4) integrate (x^2 = 1, x);
                           3
                          x
(%o4)                     -- = x + %c1
                          3
```

See also: `integration_constant`.

<!-- category: Calculus -->
<!-- keywords: laplace -->
<!-- signatures: laplace(expr, t, s) -->
### Function: laplace (expr, t, s)

Sucht die Laplace-Transformation des Ausdrucks *expr* fur die 
Integrationsvariable *x* und den Parameter *s*.


`laplace` findet die Laplace-Transformation fur Ausdrucke, die die
Funktionen `delta`, `exp`, `log`, `sin`,
`cos`, `sinh`, `cosh` und `erf` sowie Ausdrucke
mit `derivative`, `integrate`, `sum` und `ilt`
enthalten.


Kann `laplace` die Laplace-Transformation nicht finden, wird die Funktion
`specint` aufgerufen.  `specint` kann die Laplace-Transformation fur
eine Vielzahl von speziellen Funktionen im Integranden berechnen.  Findet auch
`specint` keine Losung ist das Ergebnis eine Substantivform.














`laplace` erkennt die Faltung von Funktionen der Form
`integrate (f(x) * g(t - x), x, 0, t)`.  Andere Faltungen werden nicht
erkannt.


Funktionale Abhangigkeiten von Variablen mussen explizit angegeben werden.
`laplace` erkennt keine Abhangigkeiten, die mit der Funktion 
`depends` definiert wurden.  Eine Funktion die von den Variablen *x* 
abhangt, muss als `f(x)` im Ausdruck *expr* auftreten.


Siehe auch `ilt` fur die Inverse Laplace-Transformation.


Beispiele:



```maxima
(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)                    ---------------
                           2           2
                         (s  - 4 s + 5)
(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)
(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt
(%i4) laplace (%, t, s);
                            !
               d            !         2
(%o4)        - -- (delta(t))!      + s  - delta(0) s
               dt           !
                            !t = 0
(%i5) assume(a>0)$
(%i6) laplace(gamma_incomplete(a,t),t,s),gamma_expand:true;
                                              - a - 1
                         gamma(a)   gamma(a) s
(%o6)                    -------- - -----------------
                            s            1     a
                                        (- + 1)
                                         s
(%i7) factor(laplace(gamma_incomplete(1/2,t),t,s));

                                              s + 1
                      sqrt(%pi) (sqrt(s) sqrt(-----) - 1)
                                                s
(%o7)                 -----------------------------------
                                3/2      s + 1
                               s    sqrt(-----)
                                           s

(%i8) assume(exp(%pi*s)>1)$
(%i9) laplace(sum((-1)^n*unit_step(t-n*%pi)*sin(t),n,0,inf),t,s)
        ,simpsum;

                         %i                         %i
              ------------------------ - ------------------------
                              - %pi s                    - %pi s
              (s + %i) (1 - %e       )   (s - %i) (1 - %e       )
(%o9)         ---------------------------------------------------
                                       2

(%i9) factor(%);
                                      %pi s
                                    %e
(%o9)                   -------------------------------
                                             %pi s
                        (s - %i) (s + %i) (%e      - 1)
```

See also: `delta`, `exp`, `log`, `sin`, `cos`, `sinh`, `cosh`, `erf`, `derivative`, `integrate`, `sum`, `ilt`, `specint`, `depends`.

<!-- category: Calculus -->
<!-- keywords: ldefint -->
<!-- signatures: ldefint(expr, x, a, b) -->
### Function: ldefint (expr, x, a, b)

Sucht die Losung des bestimmten Integrals fur den Integranden *expr*.
`ldefint` bestimmt die Stammfunktion und sucht die Grenzwerte mit der
Funktion `limit` an den Integrationsgrenzen *a* und *b*.  Kann ein
Grenzwert nicht ermittelt werden, enthalt das Ergebnis die Substantivform
des Grenzwertes.


`ldefint` wird nicht von der Funktion `integrate` aufgerufen.  Daher
kann `ldefint` ein von `integrate` verschiedenes Ergebnis haben.
`ldefint` verwendet immer denselben Algorithmus, um eine Losung zu
finden.  Dagegen wendet `integrate` verschiedene Algorithmen an, um nach
einer Losung zu suchen.

<!-- category: Calculus -->
<!-- keywords: ode2 -->
<!-- signatures: ode2(eqn, dvar, ivar) -->
### Function: ode2 (eqn, dvar, ivar)

Die Funktion `ode2` lost eine gewohnliche Differentialgleichung der
ersten oder zweiten Ordnung.  Die Funktion hat drei Argumente: die
Differentialgleichung *eqn*, die abhangige Variable `dvar` und die
unabhangige Variable `ivar`.  Ist die Funktion `ode2` erfolgreich
wird eine explizite oder implizite Losung fur die abhangige Variable
zuruckgegeben.  Im Fall einer Differentialgleichung 1. Ordnung wird die
Integrationskonstante mit `%c` bezeichnet.  Fur eine
Differentialgleichung 2. Ordnung werden die Integrationskonstanten mit
`%k1` und `%k2` bezeichnet.  Die Abhangigkeit der abhangigen
Variable von der unabhangigen Variablen muss nicht explizit, wie im Fall von
`desolve` angegeben werden.















Kann `ode2` keine Losung finden, ist die Ruckgabe `false`.
Gegebenenfalls wird eine Fehlermeldung ausgegeben.  Folgende Methoden werden
fur das Losen einer Differentialgleichung 1. Ordnung nacheinander
angewendet: linear, separierbar, exakt - wenn notwendig unter Zuhilfenahme
eines Integrationsfaktors, homogen, bernoullische Differentialgleichung und
eine Methode fur verallgemeinerte homogene Gleichungen.  Fur eine
Differentialgleichung 2. Ordnung kommen die folgenden Methoden zur Anwendung:
konstante Koeffizienten, exakt, linear homogen mit nicht-konstanten
Koeffizienten, die zu konstanten Koeffizienten transformiert werden konnen,
eulersche Differentialgleichung, Variation der Parameter, Reduktion auf eine
Differentialgleichung 1. Ordnung, wenn die Differentialgleichung entweder
frei von der unabhangigen oder der abhangigen Variablen ist.









Im Laufe des Losungsverfahrens werden zur Information des Nutzers globale
Variablen gesetzt: `method` bezeichnet die Methode, die von `ode2`
zum Auffinden der Losung verwendet wurde.  `intfactor` bezeichnet einen
verwendeten Integrationsfaktor.  `odeindex` bezeichnet den Index der
bernoullischen Gleichung oder der verallgemeinerte Methode fur eine homogene
Differentialgleichung.  `yp` bezeichnet eine partikulare Losung, wenn
die Variation der Parameter angewendet wird.







Fur das Losen von Anfangswertproblemen einer Differentialgleichung 1. oder
2. Ordnung konnen die Funktionen `ic1` und `ic2` verwendet werden.
Ein Randwertproblem fur eine Differentialgleichung 2. Ordnung kann mit der
Funktion `bc2` gelost werden.


Beispiele:



```maxima
(%i1) x^2*'diff(y,x) + 3*y*x = sin(x)/x;
                      2 dy           sin(x)
(%o1)                x  -- + 3 x y = ------
                        dx             x
(%i2) ode2(%,y,x);
                             %c - cos(x)
(%o2)                    y = -----------
                                  3
                                 x
(%i3) ic1(%o2,x=%pi,y=0);
                              cos(x) + 1
(%o3)                   y = - ----------
                                   3
                                  x
(%i4) 'diff(y,x,2) + y*'diff(y,x)^3 = 0;
                         2
                        d y      dy 3
(%o4)                   --- + y (--)  = 0
                          2      dx
                        dx
(%i5) ode2(%,y,x);
                      3
                     y  + 6 %k1 y
(%o5)                ------------ = x + %k2
                          6
(%i6) ratsimp(ic2(%o5,x=0,y=0,'diff(y,x)=2));
                             3
                          2 y  - 3 y
(%o6)                   - ---------- = x
                              6
(%i7) bc2(%o5,x=0,y=1,x=1,y=3);

                         3
                        y  - 10 y       3
(%o7)                   --------- = x - -
                            6           2
```

See also: `desolve`, `ic1`, `ic2`, `bc2`.

<!-- category: Calculus -->
<!-- keywords: quad_control -->
<!-- signatures: quad_control(parameter, [value]) -->
### Function: quad_control (parameter, [value])

Control error handling for quadpack.  The parameter should be one of
the following symbols:



**current_error** — The current error number
**control** — Controls if messages are printed or not.  If it is set to zero or
less, messages are suppressed.
**max_message** — The maximum number of times any message is to be printed.


If *value* is not given, then the current value of the
*parameter* is returned.  If *value* is given, the value of
*parameter* is set to the given value.

<!-- category: Calculus -->
<!-- keywords: quad_qag -->
<!-- signatures: quad_qag(f(x), x, a, b, key, [epsrel, epsabs, limit]), quad_qag(f, x, a, b, key, [epsrel, epsabs, limit]) -->
### Function: quad_qag (f(x), x, a, b, key, [epsrel, epsabs, limit])

Die Funktion `quad_qag` berechnet das folgende Integral uber ein
endliches Intervall.



           b
          /
          [
          I  f(x) dx
          ]
          /
           a


$$
\int_a^b {f(x) \, dx}
$$


`quad_qag` implementiert einen globalen adaptiven Integrator auf
Grundlage der Strategie von Aind (Piessens, 1973).  Es kann aus 6 verschiedenen 
Paaren von Gauß-Kronrad-Quadraturformeln ausgewahlt werden.  Die Formeln 
hoheren Grades sind fur stark oszillierende Integranden geeignet.


Die Funktion *f(x)* mit der abhangigen Variablen *x* wird im 
Integrationsintervall *a* und *b* integriert.  *key* wahlt den
Grad der Gauß-Kronrod-Quadraturformel aus und kann Werte von 1 bis 6
annehmen.  Ein großerer Grad ist geeignet fur stark oszillierende
Integranden.


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die numerische Integration wird adaptiv ausgefuhrt.  Der Integrationsbereich
wird solange geteilt, bis die gewunschte Genauigkeit erreicht wird.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.  Die
Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Approximation.  Der Standardwert ist 
`1.0e-8`.
**epsabs** — Gewunschter absoluter Fehler der Approximation.  Der Standardwert ist 
`0`.
**limit** — Die maximale Zahl an Teilintervallen des adaptiven Algorithmus.  Der
Standardwert ist `200`.


`quad_qag` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3, 'epsrel=5d-8);
(%o1)    [.4444444444492108, 3.1700968502883E-9, 961, 0]


(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

<!-- category: Calculus -->
<!-- keywords: quad_qagi -->
<!-- signatures: quad_qagi(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qagi(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qagi (f(x), x, a, b, [epsrel, epsabs, limit])

Die Funktion `quad_qagi` berechnet die folgenden Integrale uber ein
unendliches oder halb-unendliches Intervall.



           inf
          /
          [
          I    f(x) dx
          ]
          /
           a


$$
\int_a^\infty {f(x) \, dx}
$$



           a
          /
          [
          I     f(x) dx
          ]
          /
           minf


$$
\int_\infty^a {f(x) \, dx}
$$



           inf
          /
          [
          I     f(x) dx
          ]
          /
           minf


$$
\int_{-\infty}^\infty {f(x) \, dx}
$$


Das Intervall wird auf ein endliches Intervall transformiert.  Das
transformierte Integrationsproblem wird dann mit einem geringfugig
modifizierten Algorithmus wie in `quad_qags` gelost.


Die Funktion *f(x)* mit der abhangigen Variablen *x* wird uber einen
unendlichen Bereich integriert.


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Eine der Grenzen des Integrationsbereiches kann unendlich sein.  Ist dies nicht
der Fall gibt `quad_qagi` eine Substantivform zuruck.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.  Die
Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Approximation.  Der Standardwert ist 
`1.0e-8`.
**epsabs** — Gewunschter absoluter Fehler der Approximation.  Der Standardwert ist 
`0`.
**limit** — Die maximale Zahl an Teilintervallen des adaptiven Algorithmus.  Der
Standardwert ist `200`.


`quad_qag` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf, 'epsrel=1d-8);
(%o1)        [0.03125, 2.95916102995002E-11, 105, 0]


(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

See also: `quad_qags`.

<!-- category: Calculus -->
<!-- keywords: quad_qagp -->
<!-- signatures: quad_qagp(f(x), x, a, b, points, [epsrel, epsabs, limit]), quad_qagp(f, x, a, b, points, [epsrel, epsabs, limit]) -->
### Function: quad_qagp (f(x), x, a, b, points, [epsrel, epsabs, limit])

Integration of a general function over a finite interval.
`quad_qagp` implements globally adaptive interval subdivision with
extrapolation (de Doncker, 1978) by the Epsilon algorithm (Wynn, 1956).


`quad_qagp` computes the integral


$integrate (f(x), x, a, b)$

$$
\int_a^b {f(x) \, dx}
$$



The function to be integrated is *f(x)*, with
dependent variable *x*, and the function is to be integrated
between the limits *a* and *b*.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


To help the integrator, the user must supply a list of points where
the integrand is singular or discontinous.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qagp` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.





Examples:



```maxima
(%i1) quad_qagp(x^3*log(abs((x^2-1)*(x^2-2))),x,0,3,[1,sqrt(2)]);
(%o1)   [52.74074838347143, 2.6247632689546663e-7, 1029, 0]


(%i2) quad_qags(x^3*log(abs((x^2-1)*(x^2-2))), x, 0, 3);
(%o2)   [52.74074847951494, 4.088443219529836e-7, 1869, 0]
```


The integrand has singularities at 1 and sqrt(2) so we supply these
points to `quad_qagp`.  We also note that `quad_qagp` is
more accurate and more efficient that `quad_qags`.

<!-- category: Calculus -->
<!-- keywords: quad_qags -->
<!-- signatures: quad_qags(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qags(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qags (f(x), x, a, b, [epsrel, epsabs, limit])

Die Funktion `quad_qags` berechnet das folgende Integral uber ein
endliches Intervall.



           b
          /
          [
          I  f(x) dx
          ]
          /
           a


$$
\int_a^b {f(x) \, dx}
$$


`quad_qags` implementiert die Strategie einer globalen adaptiven 
Unterteilung des Integrationsintervalls mit Extrapolation (de Doncker, 1978).
Zusatzlich wird versucht, die Konvergenz der Integralapproximation mit Hilfe
des Epsilon-Algorithmus (Wynn, 1956) zu beschleunigen.  Dies fuhrt zum 
Beispiel bei Integranden mit Singularitaten, deren Lage und Typ unbekannt 
sind, zu einer Effizienzsteigerung.


Die Funktion *f(x)* mit der abhangigen Variablen *x* wird im 
Integrationsintervall *a* und *b* integriert.


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.  Die
Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Approximation.  Der Standardwert ist 
`1.0e-8`.
**epsabs** — Gewunschter absoluter Fehler der Approximation.  Der Standardwert ist 
`0`.
**limit** — Die maximale Zahl an Teilintervallen des adaptiven Algorithmus.  Der
Standardwert ist `200`.


`quad_qag` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:


`quad_qags` ist genauer und effizienter als `quad_qag` fur das
folgende Beispiel.



```maxima
(%i1) quad_qags (x^(1/2)*log(1/x), x, 0, 1, 'epsrel=1d-10);
(%o1)   [.4444444444444448, 1.11022302462516E-15, 315, 0]
```

See also: `quad_qag`.

<!-- category: Calculus -->
<!-- keywords: quad_qawc -->
<!-- signatures: quad_qawc(f(x), x, c, a, b, [epsrel, epsabs, limit]), quad_qawc(f, x, c, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qawc (f(x), x, c, a, b, [epsrel, epsabs, limit])

Die Funktion `quad_qawc` berechnet den Cauchyschen Hauptwert von
$f(x)(x - c)$ uber ein endliches Intervall $(a, b)$ und dem Wert
$c$.



           b
          /
          [  f(x)
          I  ----- dx
          ]  x - c
          /
           a


$$
\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}
$$


Es wird eine modifizierte Clenshaw-Curtis-Formel angewendet, wenn $c$ im
Teilbereich enthalten ist, andernfalls wird eine globale adaptive Strategie mit
einem Gauß-Kronrod-Formelpaar angewendet.


Die Funktion `f(x)/(x - c)`, die von der Variablen
*x* abhangt, wird in den Grenzen *a* und *b* integriert.


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.  Die
Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Approximation.  Der Standardwert ist 
`1.0e-8`.
**epsabs** — Gewunschter absoluter Fehler der Approximation.  Der Standardwert ist 
`0`.
**limit** — Die maximale Zahl an Teilintervallen des adaptiven Algorithmus.  Der
Standardwert ist `200`.


`quad_qag` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5,
                 'epsrel=1d-7);
(%o1)    [- 3.130120337415925, 1.306830140249558E-8, 495, 0]


(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1),
                 x, 0, 5);
Principal Value
                       alpha
        alpha       9 4                 9
       4      log(------------- + -------------)
                      alpha           alpha
                  64 4      + 4   64 4      + 4
(%o2) (-----------------------------------------
                        alpha
                     2 4      + 2

       3 alpha                       3 alpha
       -------                       -------
          2            alpha/2          2          alpha/2
    2 4        atan(4 4       )   2 4        atan(4       )   alpha
  - --------------------------- - -------------------------)/2
              alpha                        alpha
           2 4      + 2                 2 4      + 2


(%i3) ev (%, alpha=5, numer);
(%o3)                    - 3.130120337415917
```

<!-- category: Calculus -->
<!-- keywords: quad_qawf -->
<!-- signatures: quad_qawf(f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst]), quad_qawf(f, x, a, omega, trig, [epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawf (f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst])

Die Funktion `quad_qawf` berechnet die Sinus- oder
Kosinus-Fouriertransformation mit der Gewichtsfunktion $w$ uber ein
halb-unendliches Intervall.



           inf
          /
          [
          I    f(x) w(x) dx
          ]
          /
           a


$$
\int_a^\infty f(x) \, w(x) \, dx
$$


Zur Berechnung des Integrals wird die global adaptive Routine
`quad_qawo` sukzessive auf endliche Teilintervalle angewendet.  Zur
Konvergenzbeschleunigung der resultierenden alternierenden Reihe wird
der Epsilon-Algorithmus (Wynn, 1956) verwendet.


Die Gewichtsfunktion $w$ wird mit dem Schlusselwort *trig* 
ausgewahlt:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.
Die Schlusselwortargumente sind:



**epsabs** — Gewunschter absoluter Fehler der Naherung.  Der Standardwert ist 
`1.0e-10`.
**limit** — `(limit - limlst)/2` ist die maximale Zahl an Teilintervallen
des adaptiven Algorithmus.  Der Standardwert ist `200`.
**maxp1** — Die maximale Anzahl an Chebyshev-Gewichten.  Der Wert muss großer als 0 
sein.  Der Standardwert ist `100`.
**limlst** — Obere Grenze fur die Anzahl an Zyklen.  Der Wert muss großer oder gleich
3 sein.  Der Standardwert ist 10.


`quad_qawf` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos, 'epsabs=1d-9);
(%o1)   [.6901942235215714, 2.84846300257552E-11, 215, 0]


(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2


(%i3) ev (%, numer);
(%o3)                   .6901942235215714
```

See also: `quad_qawo`.

<!-- category: Calculus -->
<!-- keywords: quad_qawo -->
<!-- signatures: quad_qawo(f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]), quad_qawo(f, x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawo (f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst])

Die Funktion `quad_qawo` berechnet das folgende Integral mit den
trigonometrischen Gewichtsfunktionen $cos(omega x) f(x)$ oder
$sin(omega x) f(x)$ uber ein endliches Intervall, wobei $omega$
eine Konstante ist.



           b
          /
          [
          I  f(x) w(x) dx
          ]
          /
           a



$$
Die Funktion @code{quad_qawo} berechnet das folgende Integral mit den
trigonometrischen Gewichtsfunktionen
$\cos\left(\omega \, x\right) \, f\left(x\right)$ oder
$\sin\left(\omega \, x\right) \, f\left(x\right)$ @"uber ein endliches
Intervall, wobei $\omega$ eine Konstante ist.

$$\int_a^b f(x) \, w(x) \, dx$$
$$


Der Algorithmus basiert auf eine modifizierte Clenshaw-Curtis-Technik.
`quad_qawo` wendet eine adaptive Unterteilung des Integrationsintervalls
mit Extrapolation an, die vergleichbar mit dem Algorithmus von
`quad_qags` ist.  Zusatzlich wird versucht, die Konvergenz der
Integralapproximation mit Hilfe des Epsilon-Algorithmus zu beschleunigen.


Die Gewichtsfunktion $w$ wird mit dem Schlusselwort *trig* 
ausgewahlt:



**cos** — $w(x) = cos (omega x)$ $$
w\left(x\right) = \cos \left(\omega \, x\right)
$$
**sin** — $w(x) = sin (omega x)$ $$
w\left(x\right) = \sin \left(\omega \, x\right)
$$


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.
Die Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Naherung.  Der Standardwert ist
`1.0e-8`
**epsabs** — Gewunschter absoluter Fehler der Naherung.  Der Standardwert ist `0`.
**limit** — `limit/2` ist die maximale Zahl an Teilintervallen des adaptiven 
Algorithmus.  Der Standardwert ist `200`.
**maxp1** — Die maximale Anzahl an Chebyshev-Gewichten.  Der Wert muss großer als 0 
sein.  Der Standardwert ist `100`.
**limlst** — Obere Grenze fur die Anzahl an Zyklen.  Der Wert muss großer oder gleich
3 sein.  Der Standardwert ist 10.


`quad_qawo` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1)     [1.376043389877692, 4.72710759424899E-11, 765, 0]


(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x),
                x, 0, inf));
                   alpha/2 - 1/2            2 alpha
        sqrt(%pi) 2              sqrt(sqrt(2        + 1) + 1)
(%o2)   -----------------------------------------------------
                               2 alpha
                         sqrt(2        + 1)


(%i3) ev (%, alpha=2, numer);
(%o3)                     1.376043390090716
```

See also: `quad_qags`.

<!-- category: Calculus -->
<!-- keywords: quad_qaws -->
<!-- signatures: quad_qaws(f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]), quad_qaws(f, x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]) -->
### Function: quad_qaws (f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit])

Die Funktion `quad_qaws` berechnet das Integral von $w(x) f(x)$ uber
ein endliches Intervall $[a, b]$, wobei $w$ eine Funktion der Form
$(x - a)^alpha (b - x)^beta v(x)$ ist und $v(x)$ ist 1 oder
$log(x - a)$ oder $log(b - x)$ oder $log(x - a) log(b - x)$, und
$alpha > -1$ und $beta > -1$.



           b
          /
          [
          I  f(x) w(x) dx
          ]
          /
           a



$$
Die Funktion @code{quad_qaws} berechnet das Integral von von
$w\left(x\right) \, f\left(x\right)$ @"uber ein endliches Intervall
$\left[a, b\right]$, wobei $w$ eine Funktion der Form 
$\left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, v\left(x\right)$ ist
und $v\left(x\right)$ ist $1$ oder $\log\left(x - a\right)$ oder 
$\log\left(b - x\right)$ oder $\log\left(x - a\right) \, \log\left(b - 
x\right)$, und $\alpha > -1$ und $\beta > -1$.

$$\int_a^b f(x) \, w(x) \, dx$$
$$


`quad_qaws` ist speziell fur die effiziente Berechnung von Integralen
uber endliche Intervalle mit algebraischen oder algebraisch-logarithmischen
Endpunktsingularitat konzipiert.  Eine globale adaptive Strategie mit 
Unterteilung des Integrationsintervalls wird angewendet.  Auf Teilintervalle,
die keinen Endpunkt des Integrationsintervalls enthalten, kommt ein 
Gauß-Kronrod-Formelpaar und auf Randintervallen kommen modifizierte
Clenshaw-Curtis-Formeln zur Anwendung.


Die Gewichtsfunktion wird mit dem Schlusselwort *wfun* ausgewahlt:



**1** — $w(x) = (x - a)^alpha (b - x)^beta$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta
$$
**2** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, 
\log\left(x - a\right)
$$
**3** — $w(x) = (x - a)^alpha (b - x)^beta log(b - x)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, 
\log\left(b - x\right)
$$
**4** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a) log(b - x)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, 
\log\left(x - a\right) \, \log\left(b - x\right)
$$


Der Integrand kann eine Maxima-Funktion, eine Lisp-Funktion, ein Operator, ein
Maxima-Lambda-Ausdruck oder ein allgemeiner Maxima-Ausdruck sein.


Die Schlusselwortargumente sind optional und konnen in beliebiger
Reihenfolge angegeben werden.  Sie haben die Form `key=val`.
Die Schlusselwortargumente sind:



**epsrel** — Gewunschter relativer Fehler der Naherung.  Der Standardwert ist
`1.0e-8`
**epsabs** — Gewunschter absoluter Fehler der Naherung.  Der Standardwert ist `0`.
**limit** — Maximale Anzahl der Teilintervalle des adaptiven Algorithmus.  Der Standardwert
ist `200`.


`quad_qaws` gibt eine Liste mit vier Elementen zuruck:



- * 
eine numerische Naherung des Integrals,
- * 
geschatzer absoluter Fehler der Naherung,
- * 
Anzahl der Auswertungen des Integranden,
- * 
ein Fehlercode.


Der Fehlercode kann die folgenden Werte annehmen:



- * 
`0`,
wenn kein Fehler aufgetreten ist,
- * 
`1`,
wenn zu viele Teilintervalle notwendig wurden,
- * 
`2`,
wenn ubemaßiger Rundungsfehler aufgetreten sind,
- * 
`3`,
wenn ein extrem schlechtes Verhalten des Integranden vorliegt,
- * 
`6`,
wenn die Eingabe ungultig ist.


Beispiele:



```maxima
(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1,
                 'epsabs=1d-9);
(%o1)     [8.750097361672832, 1.24321522715422E-10, 170, 0]


(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
       alpha
Is  4 2      - 1  positive, negative, or zero?

pos;
                          alpha         alpha
                   2 %pi 2      sqrt(2 2      + 1)
(%o2)              -------------------------------
                               alpha
                            4 2      + 2


(%i3) ev (%, alpha=4, numer);
(%o3)                     8.750097361672829
```

<!-- category: Calculus -->
<!-- keywords: residue -->
<!-- signatures: residue(expr, z, z_0) -->
### Function: residue (expr, z, z_0)

Berechnet das Residuum fur den Ausdruck *expr*, wenn die Variable *z*
gegen den Wert *z_0* geht.


Beispiele:



```maxima
(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2


(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

<!-- category: Calculus -->
<!-- keywords: risch -->
<!-- signatures: risch(expr, x) -->
### Function: risch (expr, x)

Nutzt den transzendenten Risch-Algorithmus fur die Integration des
Ausdruck *expr* und der Integrationsvariable *x*.  Der algebraische
Risch-Algorithmus ist nicht implementiert.  Der transzendente Risch-Algorithmus
behandelt Integranden mit Exponential- und Logarithmusfunktionen.  Der
Risch-Algorithmus wird von `integrate` aufgerufen, wenn `integrate`
keine Stammfunktion finden kann.


Hat `erfflag` den Wert `false`, werden von der Funktion `risch`
keine Fehlerfunktionen `erf` in die Losung eingefuhrt.


Beispiele:



```maxima
(%i1) risch (x^2*erf(x), x);
                                                        2
             3                      2                - x
        %pi x  erf(x) + (sqrt(%pi) x  + sqrt(%pi)) %e
(%o1)   -------------------------------------------------
                              3 %pi


(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

See also: `integrate`, `erfflag`.

<!-- category: Calculus -->
<!-- keywords: tldefint -->
<!-- signatures: tldefint(expr, x, a, b) -->
### Function: tldefint (expr, x, a, b)

Entspricht der Funktion `ldefint` mit dem Wert `true` fur die 
Optionsvariable `tlimswitch`.

