## Spezielle Funktionen

<!-- category: Other -->
<!-- keywords: %f -->
<!-- signatures: %f[p, q]([a], [b], z) -->
### Function: %f ([p, q]([a], [b], z))

Ist die hypergeometrische Funktion
`F[p,q](a_1, ..., a_p; b_1,..., b_q; z)`.  Das Argument *a* ist eine
Liste mit den *p*-Elementen *a_i* und das Argument *b* die Liste
mit den *q*-Elementen *b_i*.

<!-- category: Other -->
<!-- keywords: %m -->
<!-- signatures: %m[k, u](z) -->
### Function: %m ([k, u](z))

Ist die Whittaker M Funktion
`M[k,u](z) = exp(-z/2) * z^(1/2+u) * M(1/2+u-k, 1+2*u, z)`.
Siehe A & S 13.1.32 fur die Definition.

<!-- category: Other -->
<!-- keywords: %s -->
<!-- signatures: %s[u, v](z) -->
### Function: %s ([u, v](z))

Lommels kleine Funktion `s[u,v](z)`.  Siehe Gradshteyn & Ryzhik 8.570.1.

<!-- category: Other -->
<!-- keywords: %w -->
<!-- signatures: %w[k, u](z) -->
### Function: %w ([k, u](z))

Ist die Whittaker W Funktion.  Siehe A & S 13.1.33 fur die Definition.

<!-- category: Other -->
<!-- keywords: erf -->
<!-- signatures: erf(z) -->
### Function: erf (z)

Die Fehlerfunktion `erf(z)` (A&S 7.1.1).


Siehe auch die Optionsvariable `erfflag`.

See also: `erfflag`.

<!-- category: Other -->
<!-- keywords: erf_generalized -->
<!-- signatures: erf_generalized(z1, z2) -->
### Function: erf_generalized (z1, z2)

Die verallgemeinerte Fehlerfunktion $Erf(z1, z2)$.

<!-- category: Other -->
<!-- keywords: erf_representation -->
<!-- signatures: erf_representation -->
### Variable: erf_representation

Standarwert: `false`


Hat die Optionsvariable `erf_representation` den Wert `true`, werden
die Funktionen `erfc`, `erfi`,
`erf_generalized`, `fresnel_s` und `fresnel_c` in eine
Darstellung mit der Funktion `erf` transformiert.

See also: `erfc`, `erfi`, `erf_generalized`, `fresnel_s`, `fresnel_c`, `erf`.

<!-- category: Other -->
<!-- keywords: erfc -->
<!-- signatures: erfc(z) -->
### Function: erfc (z)

Die komplementare Fehlerfunktion `erfc(z) = 1 - erf(z)` (A & S 7.1.2).

<!-- category: Other -->
<!-- keywords: erfi -->
<!-- signatures: erfi(z) -->
### Function: erfi (z)

Die imaginare Fehlerfunktion `erfi(z) = -%i*erf(%i*z)`.

<!-- category: Other -->
<!-- keywords: fresnel_c -->
<!-- signatures: fresnel_c(z) -->
### Function: fresnel_c (z)

Das Fresnel-Integral, das definiert ist als (A & S 7.3.1):



```maxima
z
          /           2
          [      %pi t
   C(z) = I  cos(------) dt
          ]        2
          /
           0
```


Hat die Optionsvariable `trigsign` den Wert `true`, vereinfacht
Maxima `fresnel_c(-x)` zu `-fresnel_c(x)`.


Hat die Optionsvariable `%iargs` den Wert `true`, vereinfacht 
Maxima `fresnel_c(%i*x)` zu `%i*fresnel_c(x)`.


Siehe auch die Optionsvariable `hypergeometric_representation`, um
die Fresnelfunktion in eine hypergeometrische Darstellung zu transformieren,
und die Optionsvariable `erf_representation` fur eine Darstellung als
Fehlerfunktion.

See also: `trigsign`, `%iargs`, `hypergeometric_representation`, `erf_representation`.

<!-- category: Other -->
<!-- keywords: fresnel_s -->
<!-- signatures: fresnel_s(z) -->
### Function: fresnel_s (z)

Das Fresnel-Integral, das definiert ist als (A & S 7.3.2):



```maxima
z
          /           2
          [      %pi t
   S(z) = I  sin(------) dt
          ]        2
          /
           0
```


Hat die Optionsvariable `trigsign` den Wert `true`, vereinfacht
Maxima `fresnel_s(-x)` zu `-fresnel_s(x)`.


Hat die Optionsvariable `%iargs` den Wert `true`, vereinfacht 
Maxima `fresnel_s(%i*x)` zu `%i*fresnel_s(x)`.


Siehe auch die Optionsvariable `hypergeometric_representation`, um
die Fresnelfunktion in eine hypergeometrische Darstellung zu transformieren,
und die Optionsvariable `erf_representation` fur eine Darstellung als
Fehlerfunktion.

See also: `trigsign`, `%iargs`, `hypergeometric_representation`, `erf_representation`.

<!-- category: Other -->
<!-- keywords: hgfred -->
<!-- signatures: hgfred(a, b, z) -->
### Function: hgfred (a, b, z)

Vereinfacht die Hypergeometrische Funktion zu einfacheren Funktionen, wie
Polynome und spezielle Funktionen.  Die Hypergeometrische Funktion ist die
verallgemeinerte geometrische Reihe und ist wie folgt definiert:



```maxima
F    (a_1, ... a_p; b_1, ..., b_q; z) =
    p, q

             inf      p                    q                k
             ====   /===\ gamma(k + a )  /===\   gamma(b ) z
             \       ! !             i    ! !           j
           =  >      ! !  -------------   ! !  ----------------
             /       ! !    gamma(a )     ! !  k! gamma(k + b )
             ====   i = 1          i     j = 1               j
             k = 0
```


Die Argumente *a* und *b* sind Listen mit den Parametern der 
Hypergeometrischen Funktion `a_1`, ..., `a_p` sowie
`b_1`, ..., `b_p`.  Die Liste *a* enthalt die
`p`-Elemente *a_i* und die Liste *b* enthalt die
*q*-Elemente *b_i*.








Kann `hgfred` die Hypergeomentrische Funktion nicht vereinfachen, wird
eine Substantivform `%f[p,q]([a], [b], z)` zuruckgegeben.


Beispiele:



```maxima
(%i1) assume(not(equal(z,0)));
(%o1)                          [notequal(z, 0)]
(%i2) hgfred([v+1/2],[2*v+1],2*%i*z);

                     v/2                               %i z
                    4    bessel_j(v, z) gamma(v + 1) %e
(%o2)               ---------------------------------------
                                       v
                                      z
(%i3) hgfred([1,1],[2],z);

                                   log(1 - z)
(%o3)                            - ----------
                                       z
(%i4) hgfred([a,a+1/2],[3/2],z^2);


                               1 - 2 a          1 - 2 a
                        (z + 1)        - (1 - z)
(%o4)                   -------------------------------
                                 2 (1 - 2 a) z
```

<!-- category: Other -->
<!-- keywords: hypergeometric -->
<!-- signatures: hypergeometric([a_1, ..., a_p], [b_1, ..., b_q], z) -->
### Function: hypergeometric ([a_1, ..., a_p], [b_1, ..., b_q], z)

Ist die hypergeometrische Funktion.  Im Unterschied zu den Funktionen
`%f` und `hgfred`, ist die Funktion `hypergeometric` eine
vereinfachende Funktion.  `hypergeometric` unterstutzt die Berechnung
von numerischen Werten fur reelle und komplexe Gleitkommazahlen in doppelter
und mit beliebiger Genauigkeit.  Fur die Gaußsche hypergeometrische
Funktion ist $p = 2$ und $q = 1$.  In diesem Fall wird auch die
numerische Berechnung außerhalb des Einheitskreises unterstutzt.







Hat die Optionsvariable `expand_hypergeometric` den Wert `true`, das
ist der Standardwert, und eines der Argumente `a_1`, ..., `a_p`
ist eine negative ganze Zahl, gibt `hypergeometric` ein Polynom zuruck.


Beispiel:



```maxima
(%i1)  hypergeometric([],[],x);
 (%o1) %e^x
```





Expansion in ein Polynom fur eine negative ganze Zahl, wenn die
Optionsvariable `expand_hypergeometric` den Wert `true` hat.



```maxima
(%i2) hypergeometric([-3],[7],x);
 (%o2) hypergeometric([-3],[7],x)

 (%i3) hypergeometric([-3],[7],x), expand_hypergeometric : true;
 (%o3) -x^3/504+3*x^2/56-3*x/7+1
```




Numerische Berechnung in doppelter und beliebiger Gleitkommagenauigkeit.



```maxima
(%i4) hypergeometric([5.1],[7.1 + %i],0.42);
(%o4)       1.346250786375334 - 0.0559061414208204 %i
(%i5) hypergeometric([5,6],[8], 5.7 - %i);
(%o5)     .007375824009774946 - .001049813688578674 %i
(%i6) hypergeometric([5,6],[8], 5.7b0 - %i), fpprec : 30;
(%o6) 7.37582400977494674506442010824b-3
                          - 1.04981368857867315858055393376b-3 %i
```

See also: `%f`, `hgfred`.

<!-- category: Other -->
<!-- keywords: hypergeometric_representation -->
<!-- signatures: hypergeometric_representation -->
### Variable: hypergeometric_representation

Standardwert: `false`


Hat die Optionsvariable `hypergeometric_representation` den Wert
`true`, werden die Funktionen `fresnel_s` und `fresnel_c` in
eine hypergeometrische Funktion transformiert.

See also: `fresnel_s`, `fresnel_c`.

<!-- category: Other -->
<!-- keywords: lambert_w -->
<!-- signatures: lambert_w(z) -->
### Function: lambert_w (z)

Der Hauptzweig der Lambert W Funktion, die Losung von
`z = W(z) * exp(W(z))`.

<!-- category: Other -->
<!-- keywords: li -->
<!-- signatures: li[s](z) -->
### Function: li ([s](z))

Ist der Polylogarithmus der Ordnung *s* mit dem Argument *z*.  Der
Polylogarithmus wird durch die folgende Reihe definiert werden:



$$
{\rm Li}_s \left(z\right) = \sum_{k=1}^\infty {z^k \over k^s}
$$


```maxima
inf
                                 ====   k
                                 \     z
                        Li (z) =  >    --
                          s      /      s
                                 ====  k
                                 k = 1
```





Fur *s=1* geht der Polylogarithmus in die gewohnliche
Logarithmusfunktion uber und man erhalt `-log(1-z)`.  Fur *s=2*
oder *s=3* spricht man vom Dilogarithmus oder Trilogarithmus.






Maxima vereinfacht fur *s=1* sofort zum gewohnlichen Logarithmus.
Fur negative ganze Zahlen *s* einschließlich der Null vereinfacht
Maxima den Polylogarithmus zu einer rationalen Funktion.






Ist *s=2* oder *s=3* und das Argument *z* eine Gleitkommazahl, 
vereinfacht Maxima den Di- oder Trilogarithmus zu einer Gleitkommazahl.


Beispiele:



```maxima
(%i1) assume (x > 0);
(%o1)                        [x > 0]
(%i2) integrate ((log (1 - t)) / t, t, 0, x);
(%o2)                       - li (x)
                                2
(%i3) li [2] (7);
(%o3)                        li (7)
                               2
(%i4) li [2] (7), numer;
(%o4)        1.24827317833392 - 6.113257021832577 %i
(%i5) li [3] (7);
(%o5)                        li (7)
                               3
(%i6) li [2] (7), numer;
(%o6)        1.24827317833392 - 6.113257021832577 %i
(%i7) L : makelist (i / 4.0, i, 0, 8);
(%o7)   [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
(%i8) map (lambda ([x], li [2] (x)), L);
(%o8) [0, .2676526384986274, .5822405249432515, 
.9784693966661848, 1.64493407, 2.190177004178597
 - .7010261407036192 %i, 2.374395264042415
 - 1.273806203464065 %i, 2.448686757245154
 - 1.758084846201883 %i, 2.467401098097648
 - 2.177586087815347 %i]
(%i9) map (lambda ([x], li [3] (x)), L);
(%o9) [0, .2584613953442624, 0.537213192678042, 
.8444258046482203, 1.2020569, 1.642866878950322
 - .07821473130035025 %i, 2.060877505514697
 - .2582419849982037 %i, 2.433418896388322
 - .4919260182322965 %i, 2.762071904015935
 - .7546938285978846 %i]
```

<!-- category: Other -->
<!-- keywords: nzeta -->
<!-- signatures: nzeta(z) -->
### Function: nzeta (z)

Die Plasma Dispersion Funktion
`nzeta(z) = %i*sqrt(%pi)*exp(-z^2)*(1-erf(-%i*z))`.

<!-- category: Other -->
<!-- keywords: nzetai -->
<!-- signatures: nzetai(z) -->
### Function: nzetai (z)

Gibt `imagpart(nzeta(z))` zuruck.

<!-- category: Other -->
<!-- keywords: nzetar -->
<!-- signatures: nzetar(z) -->
### Function: nzetar (z)

Gibt  `realpart(nzeta(z))` zuruck.

<!-- category: Other -->
<!-- keywords: parabolic_cylinder_d -->
<!-- signatures: parabolic_cylinder_d(v, z) -->
### Function: parabolic_cylinder_d (v, z)

Die parabolische Zylinderfunktion `parabolic_cylinder_d(v,z)`.





Die parabolischen Zylinderfunktionen sind in Abramowitz and Stegun,
*Handbook of Mathematical Functions*, Kapitel 19 definiert.





Die parabolischen Zylinderfunktionen konnen als Ergebnis der Funktion
`hgfred` auftreten.  Maxima kennt keine weiteren Eigenschaften.

See also: `hgfred`.

<!-- category: Other -->
<!-- keywords: specint -->
<!-- signatures: specint(exp(-s*t)*expr, t) -->
### Function: specint (exp(-s*t)*expr, t)

Berechnet die Laplace-Transformation des Ausdrucks *expr* fur die
Integrationsvariable *t*.  *s* ist der Parameter der
Laplace-Transformation.  Der Integrand *expr* kann spezielle
Funktionen der Mathematik enthalten.











Die folgenden speziellen Funktionen konnen als Integrand auftreten: die
un­voll­stan­di­ge Gammafunkion `gamma_incomplete`, die
Fehlerfunktionen `erf` und `erfc`, nicht jedoch die Funktion
`erfi`, die jedoch in eine andere Fehlerfunktion transformiert werden
kann, die Exponentiellen Integrale wie zum Beispiel `expintegral_e1`,
die Bessel-Funktionen wie zum Beispiel `bessel_j`, einschließlich
der Produkte von Bessel-Funktionen, Hankel-Funktionen wie zum Beispiel
`hankel_1`, Hermite `hermite` und Laguerre Polynome
`laguerre`.  Weiterhin kann `specint` Integranden mit der
Hypergeometrische Funktion `%f[p,q]([],[],z)`, die Whittaker Funktion der
ersten Art `%m[u,k](z)` und die der zweiten Art `%w[u,k](z)`
integrieren.





Das Ergebnis kann spezielle Funktionen und die Hypergeometrische Funktion
enthalten.






Kann die Funktion `laplace` keine Laplace-Transformation finden, wird
`specint` aufgerufen.  Da die Funktion `laplace` einige allgemeine
Regeln kennt, um die Laplace-Transformation zu finden, ist es von Vorteil
die Laplace-Transformation mit der Funktion `laplace` zu berechnen.





`demo(hypgeo)` zeigt einige Beispiele fur Laplace-Transformationen mit
der Funktion `specint`.


Beispiele:



```maxima
(%i1) assume (p > 0, a > 0)$
(%i2) specint (t^(1/2) * exp(-a*t/4) * exp(-p*t), t);
                           sqrt(%pi)
(%o2)                     ------------
                                 a 3/2
                          2 (p + -)
                                 4

(%i3) specint (t^(1/2) * bessel_j(1, 2 * a^(1/2) * t^(1/2))
              * exp(-p*t), t);


                                   - a/p
                         sqrt(a) %e
(%o3)                    ---------------
                                2
                               p
```




Beispiel mit Exponentiellen Integralen.



```maxima
(%i4) assume(s>0,a>0,s-a>0)$
(%i5) ratsimp(specint(%e^(a*t)
                      *(log(a)+expintegral_e1(a*t))*%e^(-s*t),t));

                             log(s)
(%o5)                        ------
                             s - a

(%i6) logarc:true$
(%i7) gamma_expand:true$

radcan(specint((cos(t)*expintegral_si(t)
                     -sin(t)*expintegral_ci(t))*%e^(-s*t),t));
                             log(s)
(%o8)                        ------
                              2
                             s  + 1
ratsimp(specint((2*t*log(a)+2/a*sin(a*t)
                      -2*t*expintegral_ci(a*t))*%e^(-s*t),t));
                               2    2
                          log(s  + a )
(%o9)                     ------------
                                2
                               s
```





Entwicklung der unvollstandigen Gammafunktion und Wechsel in eine Darstellung
mit dem Exponentiellen Integral `expintegral_e1`.



```maxima
(%i10) assume(s>0)$
(%i11) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                                            1
                            gamma_incomplete(-, k s)
                                            2
(%o11)                      ------------------------
                               sqrt(%pi) sqrt(s)

(%i12) gamma_expand:true$
(%i13) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                              erfc(sqrt(k) sqrt(s))
(%o13)                        ---------------------
                                     sqrt(s)

(%i14) expintrep:expintegral_e1$
(%i15) ratsimp(specint(1/(t+a)^2*%e^(-s*t),t));
                              a s
                        a s %e    expintegral_e1(a s) - 1
(%o15)                - ---------------------------------
                                        a
```

See also: `gamma_incomplete`, `erf`, `erfc`, `erfi`, `expintegral_e1`, `bessel_j`, `hankel_1`, `hermite`, `laguerre`, `laplace`.

