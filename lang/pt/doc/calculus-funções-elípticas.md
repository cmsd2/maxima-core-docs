## Funções Elípticas

<!-- category: Calculus -->
<!-- keywords: elliptic_e -->
<!-- signatures: elliptic_e(phi, m) -->
### Function: elliptic_e (phi, m)

A integral elíptica incompleta de segundo tipo, definida como



$$
\int_0^\phi \sqrt{1 - m\sin^2\theta} d\theta
$$

Veja também *elliptic_e* e *elliptic_ec*.

<!-- category: Calculus -->
<!-- keywords: elliptic_ec -->
<!-- signatures: elliptic_ec(m) -->
### Function: elliptic_ec (m)

A integral elíptica completa de segundo tipo, definida como




$$
\int_0^{{\pi}\over{2}} \sqrt{1 - m\sin^2\theta} d\theta
$$

Para certos valores de $m$, o valor da integral é conhecido em
termos de funções $Gama$.  Use `makegamma` para avaliar esse valor.

<!-- category: Calculus -->
<!-- keywords: elliptic_eu -->
<!-- signatures: elliptic_eu(u, m) -->
### Function: elliptic_eu (u, m)

A integral elíptica incompleta de segundo tipo, definida como

$$
$\int_0^u {\rm dn}(v, m) dv  = \int_0^\tau \sqrt{{1-m t^2}\over{1-t^2}} dt$$

onde $\tau = {\rm sn}(u, m)
$$




Isso é relacionado a $elliptic_e$ através de

$$
$E(u,m) = E(\phi, m)$$

onde $\phi = \sin^{-1} {\rm sn}(u, m)
$$

Veja também *elliptic_e*.

<!-- category: Calculus -->
<!-- keywords: elliptic_f -->
<!-- signatures: elliptic_f(phi, m) -->
### Function: elliptic_f (phi, m)

A integral elíptica incompleta de primeiro tipo, definida como




$$
\int_0^\phi {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


Veja também *elliptic_e* e *elliptic_kc*.

<!-- category: Calculus -->
<!-- keywords: elliptic_kc -->
<!-- signatures: elliptic_kc(m) -->
### Function: elliptic_kc (m)

A integral elíptica completa de primeiro tipo, definida como




$$
\int_0^{{\pi}\over{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$

Para certos valores de $m$, o valor da integral é conhecido em
termos de funções $Gama$.  Use `makegamma` para avaliar esse valor.

<!-- category: Calculus -->
<!-- keywords: elliptic_pi -->
<!-- signatures: elliptic_pi(n, phi, m) -->
### Function: elliptic_pi (n, phi, m)

A integral elíptica incompleta de terceiro tipo, definida como



$$
\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$


Somente a derivada em relação a $phi$ é conhecida pelo Maxima.

