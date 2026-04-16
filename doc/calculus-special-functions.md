## Special Functions

### Function: expintegral_chi (z)

The Exponential Integral Chi(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.4]()
and [https://dlmf.nist.gov/6.2#E16DLMF 6.2#E16]()) defined as



$${\rm Chi}(z) = \gamma + \log z + \int_0^z {{\cosh t - 1} \over t} dt$$


$${\rm Chi}(z) = \gamma + \log z + \int_0^z {{\cosh t - 1} \over t} dt$$



with 
$|\arg z| < \pi.$


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_ci (z)

The Exponential Integral Ci(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.2]()
and [https://dlmf.nist.gov/6.2#E13DLMF 6.2#E13]()) defined as



$${\rm Ci}(z) = \gamma + \log z + \int_0^z {{\cos t - 1} \over t} dt$$


$${\rm Ci}(z) = \gamma + \log z + \int_0^z {{\cos t - 1} \over t} dt$$



with 
$|\arg z| < \pi.$


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_e (n, z)

The Exponential Integral En(z) ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.4]()) defined as



$$E_n(z) = \int_1^\infty {e^{-zt} \over t^n} dt$$


$$E_n(z) = \int_1^\infty {e^{-zt} \over t^n} dt$$


with 
${\rm Re}(z) > 1$
and $n$ a
non-negative integer.


For half-integral orders, this can be written in terms of `erfc`
or `erf`.  `expintexpand` for examples.

See also: `erfc`, `erf`, `expintexpand`.

### Function: expintegral_e1 (z)

The Exponential Integral E1(z) defined as



$$E_1(z) = \int_z^\infty {e^{-t} \over t} dt$$


$$E_1(z) = \int_z^\infty {e^{-t} \over t} dt$$



with 
$\left| \arg z \right| < \pi.$
([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.1]()) and ([https://dlmf.nist.gov/6.2E2DLMF 6.2E2]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_ei (x)

The Exponential Integral Ei(x) defined as



$$Ei(x) = - -\kern-10.5pt\int_{-x}^\infty {e^{-t} \over t} dt = -\kern-10.5pt\int_{-\infty}^x {e^{t} \over t} dt$$


$$Ei(x)
  = - -\kern-10.5pt\int_{-x}^\infty {e^{-t} \over t} dt
  = -\kern-10.5pt\int_{-\infty}^x {e^{t} \over t} dt  $$



with $x$ real and $x > 0$. ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.2]()) and ([https://dlmf.nist.gov/6.2E5DLMF 6.2E5]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_li (x)

The Exponential Integral li(x) defined as



$$li(x) = -\kern-10.5pt\int_0^x {dt \over \ln t}$$


$$li(x) = -\kern-10.5pt\int_0^x {dt \over \ln t}$$



with $x$ real and $x > 1$. ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.3]()) and ([https://dlmf.nist.gov/6.2E8DLMF 6.2E8]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_shi (z)

The Exponential Integral Shi(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.3]()
and [https://dlmf.nist.gov/6.2#E15DLMF 6.2#E15]()) defined as



$${\rm Shi}(z) = \int_0^z {\sinh t \over t} dt$$


$${\rm Shi}(z) = \int_0^z {\sinh t \over t} dt$$



This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_si (z)

The Exponential Integral Si(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.1]()
and [https://dlmf.nist.gov/6.2#E9DLMF 6.2#E9]()) defined as



$${\rm Si}(z) = \int_0^z {\sin t \over t} dt$$


$${\rm Si}(z) = \int_0^z {\sin t \over t} dt$$



This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Variable: expintexpand

Default value: false


Expand `expintegral_005fe` for half
integral values in terms of `erfc` or `erf` and
for positive integers in terms of `expintegral_ei`.










```maxima
maxima

(%i1) expintegral_e(1/2,z);
                                     1
(%o1)                  expintegral_e(-, z)
                                     2


(%i2) expintegral_e(1,z);
(%o2)                  expintegral_e(1, z)


(%i3) expintexpand:true;
(%o3)                         true


(%i4) expintegral_e(1/2,z);
                     sqrt(%pi) erfc(sqrt(z))
(%o4)                -----------------------
                             sqrt(z)


(%i5) expintegral_e(1,z);
                       1
                 log(- -) - log(- z)
                       z
(%o5) - log(z) - ------------------- - expintegral_ei(- z)
                          2
```

See also: `expintegral_e`, `erfc`, `erf`, `expintegral_ei`.

### Variable: expintrep

Default value: `false`


Change the representation of one of the exponential integrals,
`expintegral_005fe`,
`expintegral_005fe1`, or
`expintegral_005fei` to an equivalent form if possible.






















The possible values for `expintrep` are:


**false** — The representation is not changed.
**gamma_incomplete** — The representation uses `gamma_incomplete`.
**expintegral_e1** — The representation uses `expintegral_e1`.
**expintegral_ei** — The representation uses `expintegral_ei`.
**expintegral_li** — The representation uses `expintegral_li`.
**expintegral_trig** — The representation uses `expintegral_si` or `expintegral_ci`.
**expintegral_hyp** — The representation uses `expintegral_shi` or `expintegral_chi`.


Here are some examples for `expintrep` set to
`expintrep_002dgamma_002dincomplete`:













```maxima
maxima

(%i1) expintrep:'gamma_incomplete;
(%o1)                   gamma_incomplete


(%i2) expintegral_e1(z);
(%o2)                gamma_incomplete(0, z)


(%i3) expintegral_ei(z);
(%o3)     log(z) - log(- z) - gamma_incomplete(0, - z)


(%i4) expintegral_li(z);
(%o4) log(log(z)) - log(- log(z)) - gamma_incomplete(0, - log(z))


(%i5) expintegral_e(n,z);
                                            n - 1
(%o5)           gamma_incomplete(1 - n, z) z


(%i6) expintegral_si(z);
(%o6) (%i (- log(%i z) + log(- %i z) - gamma_incomplete(0, %i z)
                                + gamma_incomplete(0, - %i z)))/2


(%i7) expintegral_ci(z);
(%o7) log(z) - (log(%i z) + log(- %i z)
     + gamma_incomplete(0, %i z) + gamma_incomplete(0, - %i z))/2


(%i8) expintegral_shi(z);
(%o8) (log(z) - log(- z) + gamma_incomplete(0, z)
                                    - gamma_incomplete(0, - z))/2


(%i9) expintegral_chi(z);
(%o9) - (- log(z) + log(- z) + gamma_incomplete(0, z)
                                    + gamma_incomplete(0, - z))/2
```


For `expintrep` set to `expintrep_002dexpintegral_002de1`:













```maxima
maxima

(%i1) expintrep:'expintegral_e1;
(%o1)                    expintegral_e1


(%i2) expintegral_ei(z);
(%o2)        log(z) - log(- z) - expintegral_e1(- z)


(%i3) expintegral_li(z);
(%o3) log(log(z)) - log(- log(z)) - expintegral_e1(- log(z))


(%i4) expintegral_e(n,z);
(%o4)                  expintegral_e(n, z)


(%i5) expintegral_si(z);
(%o5) (%i (- log(%i z) - expintegral_e1(%i z) + log(- %i z)
                                     + expintegral_e1(- %i z)))/2


(%i6) expintegral_ci(z);
(%o6) log(z) - (log(- %i z) (expintegral_e1(%i z)
                           + expintegral_e1(- %i z)) log(%i z))/2


(%i7) expintegral_shi(z);
      log(z) + expintegral_e1(z) - log(- z) - expintegral_e1(- z)
(%o7) -----------------------------------------------------------
                                   2


(%i8) expintegral_chi(z);
(%o8) 
    - log(z) + expintegral_e1(z) + log(- z) + expintegral_e1(- z)
  - -------------------------------------------------------------
                                  2
```


For `expintrep` set to `expintrep_002dexpintegral_002dei`:














```maxima
maxima

(%i1) expintrep:'expintegral_ei;
(%o1)                    expintegral_ei


(%i2) expintegral_e1(z);
                                  1
                 log(- z) - log(- -)
                                  z
(%o2) - log(z) + ------------------- - expintegral_ei(- z)
                          2


(%i3) expintegral_ei(z);
(%o3)                   expintegral_ei(z)


(%i4) expintegral_li(z);
(%o4)                expintegral_ei(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6) (%i (log(%i z) + 2 (expintegral_ei(- %i z)
                                              %i          %i
  - expintegral_ei(%i z)) - log(- %i z) + log(--) - log(- --)))/4
                                              z           z


(%i7) expintegral_ci(z);
(%o7) (- log(%i z) + 2 (expintegral_ei(%i z)
                                               %i          %i
 + expintegral_ei(- %i z)) - log(- %i z) + log(--) + log(- --))/4
                                               z           z
 + log(z)


(%i8) expintegral_shi(z);
(%o8) (- 2 log(z) + 2 (expintegral_ei(z) - expintegral_ei(- z))
                                                            1
                                         + log(- z) - log(- -))/4
                                                            z


(%i9) expintegral_chi(z);
(%o9) (2 log(z) + 2 (expintegral_ei(z) + expintegral_ei(- z))
                                                            1
                                         - log(- z) + log(- -))/4
                                                            z
```


For `expintrep` set to `expintrep_002dexpintegral_002dli`:














```maxima
maxima

(%i1) expintrep:'expintegral_li;
(%o1)                    expintegral_li


(%i2) expintegral_e1(z);
                                                          1
                                         log(- z) - log(- -)
                         - z                              z
(%o2) - expintegral_li(%e   ) - log(z) + -------------------
                                                  2


(%i3) expintegral_ei(z);
                                        z
(%o3)                  expintegral_li(%e )


(%i4) expintegral_li(z);
(%o4)                   expintegral_li(z)


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
                              %i z                     - %e z
(%o6) - (%i (expintegral_li(%e    ) - expintegral_li(%e      )
                                                %pi signum(z)
                                              - -------------))/2
                                                      2


(%i7) expintegral_ci(z);
                       %i z                     - %i z
      expintegral_li(%e    ) + expintegral_li(%e      )
(%o7) -------------------------------------------------
                              2
                                                  - signum(z) + 1


(%i8) expintegral_shi(z);
                            z                     - z
           expintegral_li(%e ) - expintegral_li(%e   )
(%o8)      -------------------------------------------
                                2


(%i9) expintegral_chi(z);
                            z                     - z
           expintegral_li(%e ) + expintegral_li(%e   )
(%o9)      -------------------------------------------
                                2
```


For `expintrep` set to `expintrep_002dexpintegral_002dtrig`:














```maxima
maxima

(%i1) expintrep:'expintegral_trig;
(%o1)                   expintegral_trig


(%i2) expintegral_e1(z);
(%o2) log(%i z) - %i expintegral_si(%i z) - expintegral_ci(%i z)
                                                         - log(z)


(%i3) expintegral_ei(z);
(%o3) - log(%i z) - %i expintegral_si(%i z)
                                  + expintegral_ci(%i z) + log(z)


(%i4) expintegral_li(z);
(%o4) - log(%i log(z)) - %i expintegral_si(%i log(z))
                        + expintegral_ci(%i log(z)) + log(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6)                   expintegral_si(z)


(%i7) expintegral_ci(z);
(%o7)                   expintegral_ci(z)


(%i8) expintegral_shi(z);
(%o8)               - %i expintegral_si(%i z)


(%i9) expintegral_chi(z);
(%o9)      - log(%i z) + expintegral_ci(%i z) + log(z)
```


For `expintrep` set to `expintrep_002dexpintegral_002dhyp`:














```maxima
maxima

(%i1) expintrep:'expintegral_hyp;
(%o1)                    expintegral_hyp


(%i2) expintegral_e1(z);
(%o2)        expintegral_shi(z) - expintegral_chi(z)


(%i3) expintegral_ei(z);
(%o3)        expintegral_shi(z) + expintegral_chi(z)


(%i4) expintegral_li(z);
(%o4)   expintegral_shi(log(z)) + expintegral_chi(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6)              - %i expintegral_shi(%i z)


(%i7) expintegral_ci(z);
(%o7)     - log(%i z) + expintegral_chi(%i z) + log(z)


(%i8) expintegral_shi(z);
(%o8)                  expintegral_shi(z)


(%i9) expintegral_chi(z);
(%o9)                  expintegral_chi(z)
```

See also: `false`, `expintegral_e`, `expintegral_e1`, `expintegral_ei`, `expintrep`, `gamma_incomplete`, `expintegral_li`, `expintegral_si`, `expintegral_ci`, `expintegral_shi`, `expintegral_chi`, `expintrep-gamma-incomplete`, `expintrep-expintegral-e1`, `expintrep-expintegral-ei`, `expintrep-expintegral-li`, `expintrep-expintegral-trig`, `expintrep-expintegral-hyp`.

