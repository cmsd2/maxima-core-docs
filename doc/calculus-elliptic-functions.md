## Elliptic Functions

### Function: carlson_rc (x, y)

Carlson’s RC integral is defined by



$$R_C(x, y) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}(t+y)}\, dt$$


$$R_C(x, y) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}(t+y)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


This integral is related to many elementary functions in the following
way:



$$\eqalign{ \log x &= (x-1) R_C\left(\left({\frac{1+x}{2}}\right)^2, x\right), \quad x > 0 \cr \sin^{-1} x &= x R_C(1-x^2, 1), \quad |x| \le 1 \cr \cos^{-1} x &= \sqrt{1-x^2} R_C(x^2,1), \quad 0 \le x \le 1 \cr \tan^{-1} x &= x R_C(1,1+x^2) \cr \sinh^{-1} x &= x R_C(1+x^2,1) \cr \cosh^{-1} x &= \sqrt{x^2-1} R_C(x^2,1), \quad x \ge 1 \cr \tanh^{-1}(x) &= x R_C(1,1-x^2), \quad |x| \le 1 }$$


$$\eqalign{
\log x &= (x-1) R_C\left(\left({\frac{1+x}{2}}\right)^2, x\right), \quad x > 0 \cr
\sin^{-1} x &= x R_C(1-x^2, 1), \quad |x| \le 1 \cr
\cos^{-1} x &= \sqrt{1-x^2} R_C(x^2,1), \quad 0 \le x \le 1  \cr
\tan^{-1} x &= x  R_C(1,1+x^2)  \cr
\sinh^{-1} x &= x  R_C(1+x^2,1)  \cr
\cosh^{-1} x &= \sqrt{x^2-1}  R_C(x^2,1), \quad x \ge 1  \cr
\tanh^{-1}(x) &= x  R_C(1,1-x^2), \quad |x| \le 1
}
$$



Also, we have the relationship



$$R_C(x,y) = R_F(x,y,y)$$


$$R_C(x,y) = R_F(x,y,y)
$$



Some special values:

$$\eqalign{R_C(0, 1) &= \frac{\pi}{2} \cr R_C(0, 1/4) &= \pi \cr R_C(2,1) &= \log(\sqrt{2} + 1) \cr R_C(i,i+1) &= \frac{\pi}{4} + \frac{i}{2} \log(\sqrt{2}-1) \cr R_C(0,i) &= (1-i)\frac{\pi}{2\sqrt{2}} \cr }$$


$$\eqalign{R_C(0, 1) &= \frac{\pi}{2} \cr
R_C(0, 1/4) &= \pi \cr
R_C(2,1) &= \log(\sqrt{2} + 1) \cr
R_C(i,i+1) &= \frac{\pi}{4} + \frac{i}{2} \log(\sqrt{2}-1) \cr
R_C(0,i) &= (1-i)\frac{\pi}{2\sqrt{2}} \cr
}
$$

### Function: carlson_rd (x, y, z)

Carlson’s RD integral is defined by



$$R_D(x,y,z) = \frac{3}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+z)}\, dt$$


$$R_D(x,y,z) = \frac{3}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+z)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


We also have the special values



$$\eqalign{ R_D(x,x,x) &= x^{-\frac{3}{2}} \cr R_D(0,y,y) &= \frac{3}{4} \pi y^{-\frac{3}{2}} \cr R_D(0,2,1) &= 3 \sqrt{\pi} \frac{\Gamma(\frac{3}{4})}{\Gamma(\frac{1}{4})} }$$


$$\eqalign{
R_D(x,x,x) &= x^{-\frac{3}{2}} \cr
R_D(0,y,y) &= \frac{3}{4} \pi y^{-\frac{3}{2}} \cr
R_D(0,2,1) &= 3 \sqrt{\pi} \frac{\Gamma(\frac{3}{4})}{\Gamma(\frac{1}{4})}
}
$$




It is also related to the complete elliptic integral of the second
kind, $E$,
(`elliptic_ec`) as follows 



$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)$$


$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)
$$

See also: `elliptic_ec`.

### Function: carlson_rf (x, y, z)

Carlson’s RF integral is defined by



$$R_F(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}}\, dt$$


$$R_F(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


We also have the special values



$$\eqalign{ R_F(0,1,2) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{2\pi}} \cr R_F(i,-i,0) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{\pi}} }$$


$$\eqalign{
R_F(0,1,2)  &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{2\pi}} \cr
R_F(i,-i,0) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{\pi}}
}
$$



It is also related to the complete elliptic integral of the second
kind, $E$,
(`elliptic_ec`) as follows 



$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)$$


$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)
$$

See also: `elliptic_ec`.

### Function: carlson_rj (x, y, z, p)

Carlson’s RJ integral is defined by



$$R_J(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+p)}\, dt$$


$$R_J(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+p)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


It is related to the elliptic integral of the third kind (`elliptic_pi`)
by



$$\int_0^\phi {1\over \left(1+n\sin^2\theta\right) \sqrt{1-m\sin^2\theta}} \, d\theta = R_F(c-1,c-m,c) - {n\over 3}R_j(c-1,c-m,c,c+n)$$


$$\int_0^\phi {1\over \left(1+n\sin^2\theta\right) \sqrt{1-m\sin^2\theta}}
\, d\theta = R_F(c-1,c-m,c) - {n\over 3}R_j(c-1,c-m,c,c+n)$$



where
$c = \csc\phi.$
Note that this differs in our definition of `elliptic_pi` by the
sign of the parameter $n$.

See also: `elliptic_pi`.

### Function: elliptic_e (phi, m)

The incomplete elliptic integral of the second kind, defined as



$$\int_0^\phi {\sqrt{1 - m\sin^2\theta}}\, d\theta$$


$$\int_0^\phi {\sqrt{1 - m\sin^2\theta}}\, d\theta
$$



See also `elliptic_005ff` and `elliptic_005fec`.

See also: `elliptic_f`, `elliptic_ec`.

### Function: elliptic_ec (m)

The complete elliptic integral of the second kind, defined as



$$\int_0^{\frac{\pi}{2}} \sqrt{1 - m\sin^2\theta}\, d\theta$$


$$\int_0^{\frac{\pi}{2}} \sqrt{1 - m\sin^2\theta}\, d\theta
$$



For certain values of $m$, the value of the integral is known in
terms of `gamma` functions.  Use `makegamma` to evaluate them.

See also: `gamma`, `makegamma`.

### Function: elliptic_eu (u, m)

The incomplete elliptic integral of the second kind, defined as



$$E(u, m) = \int_0^u {\rm dn}(v, m)\, dv = \int_0^\tau \sqrt{\frac{1-m t^2}{1-t^2}}\, dt$$


$$E(u, m) = \int_0^u {\rm dn}(v, m)\, dv  = \int_0^\tau \sqrt{\frac{1-m t^2}{1-t^2}}\, dt
$$



where 
$\tau = {\rm sn}(u,m) .$



This is related to `elliptic_e` by



$$E(u,m) = E(\sin^{-1} {\rm sn}(u, m), m)$$


$$E(u,m) = E(\sin^{-1} {\rm sn}(u, m), m)
$$



See also `elliptic_005fe`.

See also: `elliptic_e`.

### Function: elliptic_f (phi, m)

The incomplete elliptic integral of the first kind, defined as



$$\int_0^{\phi} {\frac{d\theta}{\sqrt{1-m\sin^2\theta}}}$$


$$\int_0^{\phi} {\frac{d\theta}{\sqrt{1-m\sin^2\theta}}}
$$



See also `elliptic_005fe` and `elliptic_005fkc`.

See also: `elliptic_e`, `elliptic_kc`.

### Function: elliptic_kc (m)

The complete elliptic integral of the first kind, defined as



$$\int_0^{\frac{\pi}{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}$$


$$\int_0^{\frac{\pi}{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$



For certain values of $m$, the value of the integral is known in
terms of `gamma` functions.  Use `makegamma` to evaluate them.

See also: `gamma`, `makegamma`.

### Function: elliptic_pi (n, phi, m)

The incomplete elliptic integral of the third kind, defined as



$$\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}$$


$$\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$

