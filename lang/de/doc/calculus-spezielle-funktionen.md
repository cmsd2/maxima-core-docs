## Spezielle Funktionen

<!-- category: Calculus -->
<!-- keywords: elliptic_e -->
<!-- signatures: elliptic_e(phi, m) -->
### Function: elliptic_e (phi, m)

Das unvollstandige elliptische Integral der zweiten Art, das definiert ist als



$$
\int_0^\phi \sqrt{1 - m\sin^2\theta} d\theta
$$


Siehe auch `elliptic_e` und `elliptic_ec`.

See also: `elliptic_e`, `elliptic_ec`.

<!-- category: Calculus -->
<!-- keywords: elliptic_ec -->
<!-- signatures: elliptic_ec(m) -->
### Function: elliptic_ec (m)

Das vollstandige elliptische Integral der zweiten Art, das definiert ist als




$$
\int_0^{{\pi}\over{2}} \sqrt{1 - m\sin^2\theta} d\theta
$$


Fur einige spezielle Argumente *m* kennt Maxima Werte mit der
Gammafunktion `gamma`.  Die Werte konnen mit der Funktion
`makegamma` berechnet werden.

See also: `gamma`, `makegamma`.

<!-- category: Calculus -->
<!-- keywords: elliptic_eu -->
<!-- signatures: elliptic_eu(u, m) -->
### Function: elliptic_eu (u, m)

Das unvollstandige elliptische Integral der zweiten Art, das definiert ist als



$$
$$\int_0^u {\rm dn}(v, m) dv  = \int_0^\tau \sqrt{{1-m t^2}\over{1-t^2}} dt$$

mit $\tau = {\rm sn}(u, m)$.
$$


Dieses Integral steht in Beziehung zum elliptischen Integral `elliptiec_e`



$$
$$E(u,m) = E(\phi, m)$$

mit $\phi = \sin^{-1} {\rm sn}(u, m)$.
$$


Siehe auch `elliptic_e`.

See also: `elliptic_e`.

<!-- category: Calculus -->
<!-- keywords: elliptic_f -->
<!-- signatures: elliptic_f(phi, m) -->
### Function: elliptic_f (phi, m)

Das unvollstandige elliptische Integral der ersten Art, das definiert ist als




$$
\int_0^\phi {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


Siehe auch `elliptic_e` und `elliptic_kc`.

See also: `elliptic_e`, `elliptic_kc`.

<!-- category: Calculus -->
<!-- keywords: elliptic_kc -->
<!-- signatures: elliptic_kc(m) -->
### Function: elliptic_kc (m)

Das vollstandige elliptische Integral der ersten Art, das definiert ist als




$$
\int_0^{{\pi}\over{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


Fur einige spezielle Argumente *m* kennt Maxima Werte mit der
Gammafunktion `gamma`.  Die Werte konnen mit der Funktion
`makegamma` berechnet werden.

See also: `gamma`, `makegamma`.

<!-- category: Calculus -->
<!-- keywords: elliptic_pi -->
<!-- signatures: elliptic_pi(n, phi, m) -->
### Function: elliptic_pi (n, phi, m)

Das unvollstandige elliptische Integral der dritten Art, das definiert ist als



$$
\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$


Maxima kennt nur die Ableitung nach der Variablen *phi*.

<!-- category: Calculus -->
<!-- keywords: expintegral_chi -->
<!-- signatures: expintegral_chi(z) -->
### Function: expintegral_chi (z)

Das Exponentielle Integral `Chi(z)` (A&S 5.2.4).

<!-- category: Calculus -->
<!-- keywords: expintegral_ci -->
<!-- signatures: expintegral_ci(z) -->
### Function: expintegral_ci (z)

Das Exponentielle Integral `Ci(z)` (A&S 5.2.2).

<!-- category: Calculus -->
<!-- keywords: expintegral_e -->
<!-- signatures: expintegral_e(n, z) -->
### Function: expintegral_e (n, z)

Das Exponentielle Integral `E[n](z)` (A&S 5.1.4).

<!-- category: Calculus -->
<!-- keywords: expintegral_e1 -->
<!-- signatures: expintegral_e1(z) -->
### Function: expintegral_e1 (z)

Das Exponentielle Integral `E1(z)` (A&S 5.1.1).

<!-- category: Calculus -->
<!-- keywords: expintegral_ei -->
<!-- signatures: expintegral_ei(z) -->
### Function: expintegral_ei (z)

Das Exponentielle Integral `Ei(z)` (A&S 5.1.2).

<!-- category: Calculus -->
<!-- keywords: expintegral_li -->
<!-- signatures: expintegral_li(n, z) -->
### Function: expintegral_li (n, z)

Das Exponentielle Integral `Li(z)` (A&S 5.1.3).

<!-- category: Calculus -->
<!-- keywords: expintegral_shi -->
<!-- signatures: expintegral_shi(z) -->
### Function: expintegral_shi (z)

Das Exponentielle Integral `Shi(z)` (A&S 5.2.3).

<!-- category: Calculus -->
<!-- keywords: expintegral_si -->
<!-- signatures: expintegral_si(z) -->
### Function: expintegral_si (z)

Das Exponentielle Integral `Si(z)` (A&S 5.2.1).

<!-- category: Calculus -->
<!-- keywords: expintexpand -->
<!-- signatures: expintexpand -->
### Variable: expintexpand

Standardwert: `false`


Expandiert das Exponentielle Integral `E[n](z)` fur halbzahlige, gerade
Ordnung *n* nach den Funktionen `erfc` und `erf`. sowie fur
positive ganze Zahlen nach der Funktion `expintegral_ei`.

See also: `erfc`, `erf`, `expintegral_ei`.

<!-- category: Calculus -->
<!-- keywords: expintrep -->
<!-- signatures: expintrep -->
### Variable: expintrep

Standardwert: `false`


Wechselt die Darstellung eines Exponentiellen Integrals in eine der anderen
Funktionen `gamma_incomplete`, `expintegral_e1`,
`expintegral_ei`, `expintegral_li`,
`expintegral_si`, `expintegral_ci`,
`expintegral_shi`, oder `expintegral_chi`.

See also: `gamma_incomplete`, `expintegral_e1`, `expintegral_ei`, `expintegral_li`, `expintegral_si`, `expintegral_ci`, `expintegral_shi`, `expintegral_chi`.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_cd -->
<!-- signatures: inverse_jacobi_cd(u, m) -->
### Function: inverse_jacobi_cd (u, m)

Die inverse Jacobische elliptische Funktion $cd(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_cn -->
<!-- signatures: inverse_jacobi_cn(u, m) -->
### Function: inverse_jacobi_cn (u, m)

Die inverse Jacobische elliptische Funktion $cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_cs -->
<!-- signatures: inverse_jacobi_cs(u, m) -->
### Function: inverse_jacobi_cs (u, m)

Die inverse Jacobische elliptische Funktion $cs(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_dc -->
<!-- signatures: inverse_jacobi_dc(u, m) -->
### Function: inverse_jacobi_dc (u, m)

Die inverse Jacobische elliptische Funktion $dc(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_dn -->
<!-- signatures: inverse_jacobi_dn(u, m) -->
### Function: inverse_jacobi_dn (u, m)

Die inverse Jacobische elliptische Funktion $dn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_ds -->
<!-- signatures: inverse_jacobi_ds(u, m) -->
### Function: inverse_jacobi_ds (u, m)

Die inverse Jacobische elliptische Funktion $ds(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_nc -->
<!-- signatures: inverse_jacobi_nc(u, m) -->
### Function: inverse_jacobi_nc (u, m)

Die inverse Jacobische elliptische Funktion $nc(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_nd -->
<!-- signatures: inverse_jacobi_nd(u, m) -->
### Function: inverse_jacobi_nd (u, m)

Die inverse Jacobische elliptische Funktion $nc(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_ns -->
<!-- signatures: inverse_jacobi_ns(u, m) -->
### Function: inverse_jacobi_ns (u, m)

Die inverse Jacobische elliptische Funktion $ns(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_sc -->
<!-- signatures: inverse_jacobi_sc(u, m) -->
### Function: inverse_jacobi_sc (u, m)

Die inverse Jacobische elliptische Funktion $sc(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_sd -->
<!-- signatures: inverse_jacobi_sd(u, m) -->
### Function: inverse_jacobi_sd (u, m)

Die inverse Jacobische elliptische Funktion $sd(u,m)$.

<!-- category: Calculus -->
<!-- keywords: inverse_jacobi_sn -->
<!-- signatures: inverse_jacobi_sn(u, m) -->
### Function: inverse_jacobi_sn (u, m)

Die inverse Jacobische elliptische Funktion $sn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_cd -->
<!-- signatures: jacobi_cd(u, m) -->
### Function: jacobi_cd (u, m)

Die Jacobische elliptische Funktion $cd(u,m) = cn(u,m)/dn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_cn -->
<!-- signatures: jacobi_cn(u, m) -->
### Function: jacobi_cn (u, m)

Die Jacobische elliptische Funktion $cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_cs -->
<!-- signatures: jacobi_cs(u, m) -->
### Function: jacobi_cs (u, m)

Die Jacobische elliptische Funktion $cs(u,m) = cn(u,m)/sn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_dc -->
<!-- signatures: jacobi_dc(u, m) -->
### Function: jacobi_dc (u, m)

Die Jacobische elliptische Funktion $dc(u,m) = dn(u,m)/cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_dn -->
<!-- signatures: jacobi_dn(u, m) -->
### Function: jacobi_dn (u, m)

Die Jacobische elliptische Funktion $dn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_ds -->
<!-- signatures: jacobi_ds(u, m) -->
### Function: jacobi_ds (u, m)

Die Jacobische elliptische Funktion $ds(u,m) = dn(u,m)/sn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_nc -->
<!-- signatures: jacobi_nc(u, m) -->
### Function: jacobi_nc (u, m)

Die Jacobische elliptische Funktion $nc(u,m) = 1/cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_nd -->
<!-- signatures: jacobi_nd(u, m) -->
### Function: jacobi_nd (u, m)

Die Jacobische elliptische Funktion $nc(u,m) = 1/cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_ns -->
<!-- signatures: jacobi_ns(u, m) -->
### Function: jacobi_ns (u, m)

Die Jacobische elliptische Funktion $ns(u,m) = 1/sn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_sc -->
<!-- signatures: jacobi_sc(u, m) -->
### Function: jacobi_sc (u, m)

Die Jacobische elliptische Funktion $sc(u,m) = sn(u,m)/cn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_sd -->
<!-- signatures: jacobi_sd(u, m) -->
### Function: jacobi_sd (u, m)

Die Jacobische elliptische Funktion $sd(u,m) = sn(u,m)/dn(u,m)$.

<!-- category: Calculus -->
<!-- keywords: jacobi_sn -->
<!-- signatures: jacobi_sn(u, m) -->
### Function: jacobi_sn (u, m)

Die Jacobische elliptische Funktion $sn(u,m)$.

