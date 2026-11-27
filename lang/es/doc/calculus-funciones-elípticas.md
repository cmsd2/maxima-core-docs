## Funciones elípticas

<!-- category: Calculus -->
<!-- keywords: elliptic_e -->
<!-- signatures: elliptic_e(phi, m) -->
### Function: elliptic_e (phi, m)

Integral elíptica incompleta de segunda especie, definida como



$$
\int_0^\phi \sqrt{1 - m\sin^2\theta} d\theta
$$


Véanse también `elliptic_e` y `elliptic_ec`.

<!-- category: Calculus -->
<!-- keywords: elliptic_ec -->
<!-- signatures: elliptic_ec(m) -->
### Function: elliptic_ec (m)

Integral elíptica completa de segunda especie, definida como




$$
\int_0^{{\pi}\over{2}} \sqrt{1 - m\sin^2\theta} d\theta
$$

Para algunos valores de $m$, se conoce el valor de la integral en términos de la función $Gamma$. Hágase uso de `makegamma` para realizar su cálculo.

<!-- category: Calculus -->
<!-- keywords: elliptic_eu -->
<!-- signatures: elliptic_eu(u, m) -->
### Function: elliptic_eu (u, m)

Integral elíptica incompleta de segunda especie, definida como



$$
$$\int_0^u {\rm dn}(v, m)^2 dv  = \int_0^\tau \sqrt{{1-m t^2}\over{1-t^2}} dt$$

donde $\tau = {\rm sn}(u, m)$.
$$


Esto se relaciona con `elliptic_e` mediante



$$
$$E(u,m) = E(\phi, m)$$

donde $\phi = \sin^{-1} {\rm sn}(u, m)$.
$$


Véase también `elliptic_e`.

<!-- category: Calculus -->
<!-- keywords: elliptic_f -->
<!-- signatures: elliptic_f(phi, m) -->
### Function: elliptic_f (phi, m)

Integral elíptica incompleta de primera especie, definida como




$$
\int_0^\phi {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


Véanse también `elliptic_e` y `elliptic_kc`.

<!-- category: Calculus -->
<!-- keywords: elliptic_kc -->
<!-- signatures: elliptic_kc(m) -->
### Function: elliptic_kc (m)

Integral elíptica completa de primera especie, definida como




$$
\int_0^{{\pi}\over{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


Para algunos valores de $m$, se conoce el valor de la integral en términos de la función $Gamma$. Hágase uso de `makegamma` para realizar su cálculo.

<!-- category: Calculus -->
<!-- keywords: elliptic_pi -->
<!-- signatures: elliptic_pi(n, phi, m) -->
### Function: elliptic_pi (n, phi, m)

Integral elíptica incompleta de tercera especie, definida como



$$
\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$


Maxima sólo conoce la derivada respecto de $phi$.

