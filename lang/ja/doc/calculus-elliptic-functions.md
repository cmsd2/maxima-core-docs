## Elliptic Functions

<!-- category: Calculus -->
<!-- keywords: elliptic_e -->
<!-- signatures: elliptic_e(phi, m) -->
### Function: elliptic_e (phi, m)

以下のように定義された第二種不完全楕円積分



$$
\int_0^\phi \sqrt{1 - m\sin^2\theta} d\theta
$$


`elliptic_e`と`elliptic_ec`も参照してください。

See also: `elliptic_e`, `elliptic_ec`.

<!-- category: Calculus -->
<!-- keywords: elliptic_ec -->
<!-- signatures: elliptic_ec(m) -->
### Function: elliptic_ec (m)

以下のように定義された第二種完全楕円積分




$$
\int_0^{{\pi}\over{2}} \sqrt{1 - m\sin^2\theta} d\theta
$$

$m$のある値に関して
積分の値は$Gamma$関数で表されることが知られています。
それらを評価するには`makegamma`を使ってください。

<!-- category: Calculus -->
<!-- keywords: elliptic_eu -->
<!-- signatures: elliptic_eu(u, m) -->
### Function: elliptic_eu (u, m)

以下のように定義された第二種不完全楕円積分



$$
$$\int_0^u {\rm dn}(v, m) dv  = \int_0^\tau \sqrt{{1-m t^2}\over{1-t^2}} dt$$

where $\tau = {\rm sn}(u, m)$.
$$


これは、



$$
$$E(u,m) = E(\phi, m)$$

where $\phi = \sin^{-1} {\rm sn}(u, m)$.
$$

によって$elliptic_e$と関連付けられます。


`elliptic_e`も参照してください。

See also: `elliptic_e`.

<!-- category: Calculus -->
<!-- keywords: elliptic_f -->
<!-- signatures: elliptic_f(phi, m) -->
### Function: elliptic_f (phi, m)

以下のように定義された第一種不完全楕円積分




$$
\int_0^\phi {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$


`elliptic_e`と`elliptic_kc`も参照してください。

See also: `elliptic_e`, `elliptic_kc`.

<!-- category: Calculus -->
<!-- keywords: elliptic_kc -->
<!-- signatures: elliptic_kc(m) -->
### Function: elliptic_kc (m)

以下のように定義された第一種完全楕円積分




$$
\int_0^{{\pi}\over{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$

$m$のある値に関して
積分の値は$Gamma$関数で表されることが知られています。
それらを評価するには`makegamma`を使ってください。

<!-- category: Calculus -->
<!-- keywords: elliptic_pi -->
<!-- signatures: elliptic_pi(n, phi, m) -->
### Function: elliptic_pi (n, phi, m)

以下のように定義された第三種不完全楕円積分



$$
\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$


Maximaが知っている$phi$に関する唯一の導関数

