## Funciones Especiales

<!-- category: Other -->
<!-- keywords: %f -->
<!-- signatures: %f[p, q]([a],[b],z) -->
### Function: %f ([p, q]([a],[b],z))

Es la función hipergeométrica pFq(a1,a2,..ap;b1,b2,..bq;z),
donde `a` es una lista de longitud `p` y 
`b` otra lista de longitud `q`.

<!-- category: Other -->
<!-- keywords: %m -->
<!-- signatures: %m[k, u](z) -->
### Function: %m ([k, u](z))

Función M de Whittaker
`M[k,u](z) = exp(-z/2)*z^(1/2+u)*M(1/2+u-k,1+2*u,z)`.  
(A&S 13.1.32)

<!-- category: Other -->
<!-- keywords: %w -->
<!-- signatures: %w[k, u](z) -->
### Function: %w ([k, u](z))

Función W de Whittaker.  (A&S 13.1.33)

<!-- category: Other -->
<!-- keywords: erf -->
<!-- signatures: erf(z) -->
### Function: erf (z)

Función de error erf(z) (A&S 7.1.1)


Véase también `erfflag`.

<!-- category: Other -->
<!-- keywords: erf_generalized -->
<!-- signatures: erf_generalized(z1, z2) -->
### Function: erf_generalized (z1, z2)

Función de error generalizada Erf(z1,z2)

<!-- category: Other -->
<!-- keywords: erf_representation -->
<!-- signatures: erf_representation -->
### Variable: erf_representation

Valor por defecto: false


Cuando valga `true` erfc, erfi, erf_generalized, fresnel_s 
y fresnel_c se transforman a erf.

<!-- category: Other -->
<!-- keywords: erfc -->
<!-- signatures: erfc(z) -->
### Function: erfc (z)

Complemento de la función de error erfc(z) (A&S 7.1.2)


`erfc(z) = 1-erf(z)`

<!-- category: Other -->
<!-- keywords: erfi -->
<!-- signatures: erfi(z) -->
### Function: erfi (z)

Función de error imaginaria. 


`erfi(z) = -%i*erf(%i*z)`

<!-- category: Other -->
<!-- keywords: fresnel_c -->
<!-- signatures: fresnel_c(z) -->
### Function: fresnel_c (z)

Integral de Fresnel `C(z) = integrate(cos((%pi/2)*t^2),t,0,z)`. (A&S 7.3.1)


La simplificación `fresnel_c(-x) = -fresnel_c(x)` se aplica cuando
la variable global `trigsign` vale `true`.


La simplificación `fresnel_s(%i*x) = -%i*fresnel_s(x)` se aplica cuando
la variable global `%iargs` vale `true`.


Véanse también `erf_representation` y
`hypergeometric_representation`.

<!-- category: Other -->
<!-- keywords: fresnel_s -->
<!-- signatures: fresnel_s(z) -->
### Function: fresnel_s (z)

Integral de Fresnel S(z) = integrate(sin((%pi/2)*t^2),t,0,z). (A&S 7.3.2)


La simplificación fresnel_s(-x) = -fresnel_s(x) se aplica cuando
la variable global `trigsign` vale `true`.


La simplificación fresnel_s(%i*x) =  %i*fresnel_s(x) se aplica cuando
la variable global `%iargs` vale `true`.


Véanse también `erf_representation` y
`hypergeometric_representation`.

<!-- category: Other -->
<!-- keywords: generalized_lambert_w -->
<!-- signatures: generalized_lambert_w(k, z) -->
### Function: generalized_lambert_w (k, z)

*k*-ésima rama de la función W de Lambert’s, W(z), solución de
`z = W(z) * exp(W(z))`. (DLMF 4.13)


La rama principal, representada por Wp(z) en DLMF, es `lambert_w(z) = generalized_lambert_w(0,z)`.


La otra rama con valores reales, representada por Wm(z) en DLMF, es `generalized_lambert_w(-1,z)`.

<!-- category: Other -->
<!-- keywords: hgfred -->
<!-- signatures: hgfred(a, b, t) -->
### Function: hgfred (a, b, t)

Simplifica la función hipergeométrica generalizada en términos
de otras funciones más sencillas. *a* es una lista de parámetros
del numerador y *b* lo es de parámetros del denominador.


En caso de que `hgfred` no pueda simplificar la función hipergeométrica
devolverá una expresión de la forma `%f[p,q]([a], [b], x)`, siendo *p*
el número de elementos de *a* y *q* el de *b*. Esta es la 
función hipergeométrica generalizada `pFq`.



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


Tal como muestra el siguiente ejemplo, puede ser de utilidad cargar
también el paquete `orthopoly`. Nótese que *L* es el
polinomio generalizado de Laguerre.



```maxima
(%i5) load("orthopoly")$
(%i6) hgfred([-2],[a],z);

                                    (a - 1)
                                 2 L       (z)
                                    2
(%o6)                            -------------
                                   a (a + 1)
(%i7) ev(%);

                                  2
                                 z        2 z
(%o7)                         --------- - --- + 1
                              a (a + 1)    a
```

<!-- category: Other -->
<!-- keywords: hypergeometric -->
<!-- signatures: hypergeometric([a1, ..., ap], [b1, ..., bq], x) -->
### Function: hypergeometric ([a1, ..., ap], [b1, ..., bq], x)

Es la función hipergeométrica. A diferencia de la función
hipergeométrica `%f` de Maxima, la función `hypergeometric`
es simplificadora; además, `hypergeometric` soporta la evaluación
en doble (float) y gran (bigfloat) precisión. La evaluación 
numérica fuera del círculo unidad no está en general
soportada, pero sí en el caso de la función
hipergeométrica de Gauss, cuando $p = 2$ y $q = 1$.


Si la variable opcional `expand_hypergeometric` vale `true`,
(el valor por defecto es `false`) y uno de los argumentos entr `a1`
y `ap` es entero negativo (caso polinomial), entonces `hypergeometric`
devuelve un polinomio expandido.


Ejemplos:


```maxima
(%i1)  hypergeometric([],[],x);
(%o1) %e^x
```


Los polinomios se expanden automáticamente cuando `expand_hypergeometric`
vale `true`.



```maxima
(%i2) hypergeometric([-3],[7],x);
(%o2) hypergeometric([-3],[7],x)

(%i3) hypergeometric([-3],[7],x), expand_hypergeometric : true;
(%o3) -x^3/504+3*x^2/56-3*x/7+1
```


Se soporta la evaluación en doble (float) y gran (bigfloat) precisión:



```maxima
(%i4) hypergeometric([5.1],[7.1 + %i],0.42);
(%o4)       1.346250786375334 - 0.0559061414208204 %i
(%i5) hypergeometric([5,6],[8], 5.7 - %i);
(%o5)     .007375824009774946 - .001049813688578674 %i
(%i6) hypergeometric([5,6],[8], 5.7b0 - %i), fpprec : 30;
(%o6) 7.37582400977494674506442010824b-3
                          - 1.04981368857867315858055393376b-3 %i
```

<!-- category: Other -->
<!-- keywords: hypergeometric_representation -->
<!-- signatures: hypergeometric_representation -->
### Variable: hypergeometric_representation

Valor por defecto: false


Permite obtener la representación hipergeométrica
de las funciones fresnel_s y fresnel_c.

<!-- category: Other -->
<!-- keywords: lambert_w -->
<!-- signatures: lambert_w(z) -->
### Function: lambert_w (z)

Rama principal de la función W de Lambert, solución de
la ecuación `z = W(z) * exp(W(z))`.  (DLMF 4.13)

<!-- category: Other -->
<!-- keywords: nzeta -->
<!-- signatures: nzeta(z) -->
### Function: nzeta (z)

Función de dispersión del plasma.
`nzeta(z) = %i*sqrt(%pi)*exp(-z^2)*(1-erf(-%i*z))`

<!-- category: Other -->
<!-- keywords: nzetai -->
<!-- signatures: nzetai(z) -->
### Function: nzetai (z)

Devuelve `imagpart(nzeta(z))`.

<!-- category: Other -->
<!-- keywords: nzetar -->
<!-- signatures: nzetar(z) -->
### Function: nzetar (z)

Devuelve `realpart(nzeta(z))`.

<!-- category: Other -->
<!-- keywords: parabolic_cylinder_d -->
<!-- signatures: parabolic_cylinder_d(v, z) -->
### Function: parabolic_cylinder_d (v, z)

Función de cilindro parabólico `parabolic_cylinder_d(v,z)`. (A&s 19.3.1)

<!-- category: Other -->
<!-- keywords: specint -->
<!-- signatures: specint(exp(-s*t)*expr, t) -->
### Function: specint (exp(-s*t)*expr, t)

Calcula la transformada de Laplace de *expr* respecto de
la variable *t*. El integrando *expr* puede contener
funciones especiales.


La función `specint` admite las funciones especiales siguientes:
la gamma incompleta, las funciones de error (pero no `erfi`, siendo
sencillo transformar `erfi` en la función de error `erf`),
integrales exponenciales, funciones de Bessel (incluidos productos de
funciones de Bessel), funciones de Hankel, de Hermite y los polinomios de
Laguerre.


Además, `specint` también admite la función hipergeométrica
`%f[p,q]([],[],z)`, la función de Whittaker de primera especie
`%m[u,k](z)` y la de segunda especie `%w[u,k](z)`.


El resultado puede darse en términos de funciones especiales y es
posible que incluya también funciones hipergeométricas sin
simplificar.


Cuando `laplace` es incapaz de calcular la transformada de Laplace,
entonces llama a la función `specint`. Puesto que `laplace`
tiene programadas más reglas para calcular transformadas de Laplace,
es preferible utilizar `laplace` en lugar de `specint`.


La ejecución de `demo(hypgeo)` muestra algunos ejemplos de
transformadas de Laplace calculadas con `specint`.


Ejemplos:









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


Ejemplos para integrales exponenciales:



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


Resultados cuando se utiliza la expansión de `gamma_incomplete`
y se cambia la representación de `expintegral_e1`:



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

