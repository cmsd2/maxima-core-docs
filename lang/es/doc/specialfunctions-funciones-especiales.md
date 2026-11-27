## Funciones Especiales

<!-- category: SpecialFunctions -->
<!-- keywords: %s -->
<!-- signatures: %s[u, v](z) -->
### Function: %s ([u, v](z))

Función s[u,v](z) de Lommel.
Gradshteyn & Ryzhik 8.570.1.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_ai -->
<!-- signatures: airy_ai(x) -->
### Function: airy_ai (x)

Función de Airy Ai(x).  (A&S 10.4.2)


La derivada `diff (airy_ai(x), x)` es `airy_dai(x)`.


Véanse `airy_bi`, `airy_dai` y `airy_dbi`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_bi -->
<!-- signatures: airy_bi(x) -->
### Function: airy_bi (x)

Es la función Bi de Airy, tal como la definen Abramowitz y Stegun,
*Handbook of Mathematical Functions*, Sección 10.4. Se trata de la segunda solución de la ecuación de Airy `diff (y(x), x, 2) - x y(x) = 0`.


Si el argumento `x` es un número decimal real o complejo, se devolverá el valor numérico de `airy_bi` siempre que sea posible. En los otros casos, se devuelve la expresión sin evaluar.


La derivada `diff (airy_bi(x), x)` es `airy_dbi(x)`.


Véanse `airy_ai` y `airy_dbi`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dai -->
<!-- signatures: airy_dai(x) -->
### Function: airy_dai (x)

Es la derivada de la función Ai de Airy, `airy_ai(x)`. 


Véase `airy_ai`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dbi -->
<!-- signatures: airy_dbi(x) -->
### Function: airy_dbi (x)

Es la derivada de la función Bi de Airy, `airy_bi(x)`.


Véanse `airy_ai` y `airy_bi`.

<!-- category: SpecialFunctions -->
<!-- keywords: algepsilon -->
<!-- signatures: algepsilon -->
### Variable: algepsilon

Valor por defecto: 10^8


El valor de `algepsilon` es usado por `algsys`.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_i -->
<!-- signatures: bessel_i(v, z) -->
### Function: bessel_i (v, z)

Función modificada de Bessel de primera especie de orden $v$ y argumento $z$.


La función `bessel_i` se define como



```maxima
inf
                    ====   - v - 2 k  v + 2 k
                    \     2          z
                     >    -------------------
                    /     k! gamma(v + k + 1)
                    ====
                    k = 0
```



$$
\sum_{k=0}^{\infty } {{1\over{k!\,\Gamma
 \left(v+k+1\right)}} {\left(z\over 2\right)^{v+2\,k}}}
$$


aunque la serie infinita no se utiliza en los cálculos.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_j -->
<!-- signatures: bessel_j(v, z) -->
### Function: bessel_j (v, z)

Función de Bessel de primera especie de orden $v$ y argumento $z$.


La función `bessel_j` se define como



```maxima
inf
                ====       k  - v - 2 k  v + 2 k
                \     (- 1)  2          z
                 >    --------------------------
                /        k! gamma(v + k + 1)
                ====
                k = 0
```



$$
\sum_{k=0}^{\infty }{{{\left(-1\right)^{k}\,\left(z\over 2\right)^{v+2\,k}
 }\over{k!\,\Gamma\left(v+k+1\right)}}}
$$


aunque la serie infinita no se utiliza en los cálculos.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_k -->
<!-- signatures: bessel_k(v, z) -->
### Function: bessel_k (v, z)

Función modificada de Bessel de segunda especie de orden $v$ y argumento $z$.


La función `bessel_k` se define como



```maxima
%pi csc(%pi v) (bessel_i(-v, z) - bessel_i(v, z))
           -------------------------------------------------
                                  2
```



$$
{{\pi\,\csc \left(\pi\,v\right)\,\left(I_{-v}(z)-I_{v}(z)\right)}\over{2}}
$$


si $v$ no es un entero.  Si $v$ es igual al entero $n$, entonces se calcula el límite cuando $v$ tiende a $n$.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_y -->
<!-- signatures: bessel_y(v, z) -->
### Function: bessel_y (v, z)

Función de Bessel de segunda especie de orden $v$ y argumento $z$.


La función `bessel_y` se define como



```maxima
cos(%pi v) bessel_j(v, z) - bessel_j(-v, z)
              -------------------------------------------
                             sin(%pi v)
```



$$
{{\cos \left(\pi\,v\right)\,J_{v}(z)-J_{-v}(z)}\over{
 \sin \left(\pi\,v\right)}}
$$


si $v$ no es un entero.  En caso de que  $v$ sea un entero $n$, se calcula el límite cuando $v$ se aproxima a $n$.

<!-- category: SpecialFunctions -->
<!-- keywords: besselexpand -->
<!-- signatures: besselexpand -->
### Variable: besselexpand

Valor por defecto: `false`


Controla la expansión de las funciones de Bessel cuando el orden es la mitad de un entero impar. En tal caso, las funciones de Bessel se pueden expandir en términos de otras funciones elementales.  Si `besselexpand` vale `true`, se expande la función de Bessel.



```maxima
(%i1) besselexpand: false$
(%i2) bessel_j (3/2, z);
                                    3
(%o2)                      bessel_j(-, z)
                                    2
(%i3) besselexpand: true$
(%i4) bessel_j (3/2, z);
                                        sin(z)   cos(z)
                       sqrt(2) sqrt(z) (------ - ------)
                                           2       z
                                          z
(%o4)                  ---------------------------------
                                   sqrt(%pi)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta -->
<!-- signatures: beta(a, b) -->
### Function: beta (a, b)

La función beta se define como `gamma(a) gamma(b)/gamma(a+b)`
(A&S 6.2.1).


Maxima simplifica la función beta para enteros positivos y números
racionales cuya suma sea entera. Si `beta_args_sum_to_integer`
vale `true`, Maxima también simplifica expresiones generales
cuya suma sea también entera.


Cuando *a* o *b* sean nulos, la función beta no está definida.


En general, la función beta no está definida para enteros negativos. 
La excepción es para *a=-n*, siendo *n* un entero positivo
y *b* otro entero positivo tal que *b<=n*, entonces es posible
definir una continuación analítica. En este caso Maxima
devuelve un resultado.


Si `beta_expand` vale `true`, expresiones como `beta(a+n,b)`,
`beta(a-n,b)`, `beta(a,b+n)` o `beta(a,b-n)`, siendo `n`
entero, se simplifican.


Maxima puede evaluar la función beta para valores reales y complejos, tanto
de tipo decimal flotante o big float. Para la evaluación numérica
Maxima utiliza `log_gamma`:



```maxima
- log_gamma(b + a) + log_gamma(b) + log_gamma(a)
         %e
```


Maxima reconoce la simetría de la función beta.


Maxima conoce las derivadas de la función beta, tanto respecto de *a*
como de *b*.


Para expresar la función beta como un cociente de funciones gamma,
véase `makegamma`.


Ejemplos:


Simplificación cuando uno de sus argumentos es entero:



```maxima
(%i1) [beta(2,3),beta(2,1/3),beta(2,a)];
                               1   9      1
(%o1)                         [--, -, ---------]
                               12  4  a (a + 1)
```


Simplificación para argumentos racionales que suman un entero:



```maxima
(%i2) [beta(1/2,5/2),beta(1/3,2/3),beta(1/4,3/4)];
                          3 %pi   2 %pi
(%o2)                    [-----, -------, sqrt(2) %pi]
                            8    sqrt(3)
```


Cuando se iguala `beta_args_sum_to_integer` a `true` se
simplifican expresiones más generales si la suma de los argumentos
se reduce a un entero:



```maxima
(%i3) beta_args_sum_to_integer:true$
(%i4) beta(a+1,-a+2);
                                %pi (a - 1) a
(%o4)                         ------------------
                              2 sin(%pi (2 - a))
```


Posibles valores cuando uno de los argumentos es entero negativo: 



```maxima
(%i5) [beta(-3,1),beta(-3,2),beta(-3,3)];
                                    1  1    1
(%o5)                            [- -, -, - -]
                                    3  6    3
```


`beta(a+n,b)` o `beta(a-n)` con `n` entero se simplifica
si `beta_expand` vale `true`:



```maxima
(%i6) beta_expand:true$
(%i7) [beta(a+1,b),beta(a-1,b),beta(a+1,b)/beta(a,b+1)];
                    a beta(a, b)  beta(a, b) (b + a - 1)  a
(%o7)              [------------, ----------------------, -]
                       b + a              a - 1           b
```


La función beta no está definida si uno de sus argumentos es cero:



```maxima
(%i7) beta(0,b);
beta: expected nonzero arguments; found 0, b
 -- an error.  To debug this try debugmode(true);
```


Evaluación numérica para argumentos reales y complejos de tipo
decimal flotante o big float:



```maxima
(%i8) beta(2.5,2.3);
(%o8) .08694748611299981

(%i9) beta(2.5,1.4+%i);
(%o9) 0.0640144950796695 - .1502078053286415 %i

(%i10) beta(2.5b0,2.3b0);
(%o10) 8.694748611299969b-2

(%i11) beta(2.5b0,1.4b0+%i);
(%o11) 6.401449507966944b-2 - 1.502078053286415b-1 %i
```


La función beta es simétrica con simetría especular:



```maxima
(%i14) beta(a,b)-beta(b,a);
(%o14)                                 0
(%i15) declare(a,complex,b,complex)$
(%i16) conjugate(beta(a,b));
(%o16)                 beta(conjugate(a), conjugate(b))
```


Derivada de la función beta respecto de `a`:



```maxima
(%i17) diff(beta(a,b),a);
(%o17)               - beta(a, b) (psi (b + a) - psi (a))
                                      0             0
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_args_sum_to_integer -->
<!-- signatures: beta_args_sum_to_integer -->
### Variable: beta_args_sum_to_integer

Valor por defecto: false


Si `beta_args_sum_to_integer` vale `true`, Maxima simplifica 
`beta(a,b)` cuando la suma de los argumentos *a* y *b* sea un entero.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_expand -->
<!-- signatures: beta_expand -->
### Variable: beta_expand

Valor por defecto: false


Si `beta_expand` vale `true`, `beta(a,b)` y sus
funciones relacionadas se expanden para argumentos del tipo 
$a+n$ o $a-n$, siendo $n$ un número entero.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete -->
<!-- signatures: beta_incomplete(a, b, z) -->
### Function: beta_incomplete (a, b, z)

La definición básica de la función beta incompleta (A&S 6.6.1) es



```maxima
z
                      /
                      [         b - 1  a - 1
                      I  (1 - t)      t      dt
                      ]
                      /
                       0
```


Esta definición es posible para $realpart(a)>0$, $realpart(b)>0$
y $abs(z)<1$. Para otras situaciones, la función beta incompleta puede
definirse por medio de una función hipergeométrica generalizada:



```maxima
gamma(a) hypergeometric_generalized([a, 1 - b], [a + 1], z) z
```

(Véase Funcións.wolfram.com para una completa definición de la función beta 
incompleta.)


Para enteros negativos $a = -n$ y enteros positivos $b=m$ con 
$m<=n$ la función beta incompleta se define como



```maxima
m - 1           k
                            ====  (1 - m)  z
                      n - 1 \            k
                     z       >    -----------
                            /     k! (n - k)
                            ====
                            k = 0
```

Maxima utiliza esta definición para simplificar `beta_incomplete` 
cuando *a* es entero negativo.


Cuando *a* es entero positivo, `beta_incomplete` se simplifica
para cualesquiera argumentos *b* y *z*, y para *b* entero
positivo para cualesquiera argumentos *a* y *z*, con la 
excepción de cuando *a* sea entero negativo.


Para $z=0$ y $realpart(a)>0$, `beta_incomplete` se anula.
Para *z=1* y $realpart(b)>0$, `beta_incomplete` se reduce a
la función `beta(a,b)`.


Maxima evalúa `beta_incomplete` numéricamente para valores reales
y complejos en forma decimal y big float. La evaluación numérica se
realiza expandiendo la función beta incompleta en fracciones continuas.


Si `beta_expand` vale `true`, Maxima expande las expresiones
`beta_incomplete(a+n,b,z)` y `beta_incomplete(a-n,b,z)`,
siendo *n* entero positivo.


Maxima conoce las derivadas de `beta_incomplete` con respecto a
las variables *a*, *b* y *z*, así como la
integral respecto de la variable *z*.


Ejemplos:


Simplificación para *a* entero positivo:



```maxima
(%i1) beta_incomplete(2,b,z);
                                       b
                            1 - (1 - z)  (b z + 1)
(%o1)                       ----------------------
                                  b (b + 1)
```


Simplificación para *b* entero positivo:



```maxima
(%i2) beta_incomplete(a,2,z);
                                               a
                              (a (1 - z) + 1) z
(%o2)                         ------------------
                                  a (a + 1)
```


Simplificación para *a* y *b* enteros positivos:



```maxima
(%i3) beta_incomplete(3,2,z);
                                               3
                              (3 (1 - z) + 1) z
(%o3)                         ------------------
                                      12
```


Para *a* entero negativo y $b<=(-a)$:



```maxima
(%i4) beta_incomplete(-3,1,z);
                                       1
(%o4)                              - ----
                                        3
                                     3 z
```


Simplificación para los valores $z=0$ y $z=1$:



```maxima
(%i5) assume(a>0,b>0)$
(%i6) beta_incomplete(a,b,0);
(%o6)                                 0
(%i7) beta_incomplete(a,b,1);
(%o7)                            beta(a, b)
```


Evaluación numérica, tanto con float (precisión doble)
como big float (precisión arbitraria):



```maxima
(%i8) beta_incomplete(0.25,0.50,0.9);
(%o8)                          4.594959440269333
(%i9)  fpprec:25$
(%i10) beta_incomplete(0.25,0.50,0.9b0);
(%o10)                    4.594959440269324086971203b0
```


Para $abs(z)>1$, `beta_incomplete` devuelve un
resultado complejo:



```maxima
(%i11) beta_incomplete(0.25,0.50,1.7);
(%o11)              5.244115108584249 - 1.45518047787844 %i
```


Resultados para argumentos complejos más generales:



```maxima
(%i14) beta_incomplete(0.25+%i,1.0+%i,1.7+%i);
(%o14)             2.726960675662536 - .3831175704269199 %i
(%i15) beta_incomplete(1/2,5/4*%i,2.8+%i);
(%o15)             13.04649635168716 %i - 5.802067956270001
(%i16)
```


Expansión cuando `beta_expand` vale `true`:



```maxima
(%i23) beta_incomplete(a+1,b,z),beta_expand:true;
                                                       b  a
                   a beta_incomplete(a, b, z)   (1 - z)  z
(%o23)             -------------------------- - -----------
                             b + a                 b + a

(%i24) beta_incomplete(a-1,b,z),beta_expand:true;
                                                           b  a - 1
           beta_incomplete(a, b, z) (- b - a + 1)   (1 - z)  z
(%o24)     -------------------------------------- - ---------------
                           1 - a                         1 - a
```

 

Derivada e integral de `beta_incomplete`:



```maxima
(%i34) diff(beta_incomplete(a, b, z), z);
                              b - 1  a - 1
(%o34)                 (1 - z)      z
(%i35) integrate(beta_incomplete(a, b, z), z);
              b  a
       (1 - z)  z
(%o35) ----------- + beta_incomplete(a, b, z) z
          b + a
                                       a beta_incomplete(a, b, z)
                                     - --------------------------
                                                 b + a
(%i36) factor(diff(%, z));
(%o36)              beta_incomplete(a, b, z)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_generalized -->
<!-- signatures: beta_incomplete_generalized(a, b, z1, z2) -->
### Function: beta_incomplete_generalized (a, b, z1, z2)

La definición básica de la función beta incompleta generalizada es


The basic definition of the generalized incomplete beta function is



```maxima
z2
                     /
                     [          b - 1  a - 1
                     I   (1 - t)      t      dt
                     ]
                     /
                      z1
```


Maxima simplifica `beta_incomplete_regularized` para *a* y *b* 
enteros positivos.


Para $realpart(a)>0$ y $z1=0$ o $z2=0$, Maxima reduce
`beta_incomplete_generalized` a `beta_incomplete`. Para
$realpart(b)>0$ y $z1=1$ o *z2=1*, Maxima reduce a
una expresión con `beta` y `beta_incomplete`.


Maxima evalúa `beta_incomplete_generalized` numéricamente para valores reales
y complejos en forma decimal y big float.


Si `beta_expand` vale `true`, Maxima expande 
`beta_incomplete_generalized` para los argumentos $a+n$ y $a-n$,
siendo *n* entero positivo.


Maxima conoce las derivadas de `beta_incomplete_generalized` con respecto a
las variables *a*, *b*, *z1* y *z2*, así como la
integral respecto de las variables *z1* y *z2*.


Ejemplos:


Maxima simplifica `beta_incomplete_generalized` para *a* y *b*
enteros positivos:


```maxima
(%i1) beta_incomplete_generalized(2,b,z1,z2);
                          b                      b
                  (1 - z1)  (b z1 + 1) - (1 - z2)  (b z2 + 1)
(%o1)             -------------------------------------------
                                   b (b + 1)

(%i2) beta_incomplete_generalized(a,2,z1,z2);
                                     a                      a
                  (a (1 - z2) + 1) z2  - (a (1 - z1) + 1) z1
(%o2)             -------------------------------------------
                                   a (a + 1)

(%i3) beta_incomplete_generalized(3,2,z1,z2);
                  2      2                       2      2
          (1 - z1)  (3 z1  + 2 z1 + 1) - (1 - z2)  (3 z2  + 2 z2 + 1)
(%o3)     -----------------------------------------------------------
                                      12
```


Simplificación para los valores $z1=0$, $z2=0$, $z1=1$
o $z2=1$:


```maxima
(%i4) assume(a > 0, b > 0)$
(%i5) beta_incomplete_generalized(a,b,z1,0);
(%o5)                    - beta_incomplete(a, b, z1)

(%i6) beta_incomplete_generalized(a,b,0,z2);
(%o6)                    - beta_incomplete(a, b, z2)

(%i7) beta_incomplete_generalized(a,b,z1,1);
(%o7)              beta(a, b) - beta_incomplete(a, b, z1)

(%i8) beta_incomplete_generalized(a,b,1,z2);
(%o8)              beta_incomplete(a, b, z2) - beta(a, b)
```


Evaluación numérica para argumentos reales, tanto con float
(precisión doble) como big float (precisión arbitraria):


```maxima
(%i9) beta_incomplete_generalized(1/2,3/2,0.25,0.31);
(%o9)                        .09638178086368676

(%i10) fpprec:32$
(%i10) beta_incomplete_generalized(1/2,3/2,0.25,0.31b0);
(%o10)               9.6381780863686935309170054689964b-2
```


Evaluación numérica para argumentos complejos, tanto con float
(precisión doble) como big float (precisión arbitraria):


```maxima
(%i11) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31);
(%o11)           - .09625463003205376 %i - .003323847735353769
(%i12) fpprec:20$
(%i13) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31b0);
(%o13)     - 9.6254630032054178691b-2 %i - 3.3238477353543591914b-3
```


Expansión para $a+n$ o $a-n$, siendo *n* entero positivo
con `beta_expand` igual `true`:


```maxima
(%i14) beta_expand:true$
(%i15) beta_incomplete_generalized(a+1,b,z1,z2);
               b   a           b   a
       (1 - z1)  z1  - (1 - z2)  z2
(%o15) -----------------------------
                   b + a
                            a beta_incomplete_generalized(a, b, z1, z2)
                          + -------------------------------------------
                                               b + a

(%i16) beta_incomplete_generalized(a-1,b,z1,z2);
       beta_incomplete_generalized(a, b, z1, z2) (- b - a + 1)
(%o16) -------------------------------------------------------
                                1 - a
                                          b   a - 1           b   a - 1
                                  (1 - z2)  z2      - (1 - z1)  z1
                                - -------------------------------------
                                                  1 - a
```


Derivada respecto de la variable *z1* e integrales respecto de 
*z1* y *z2*:


```maxima
(%i17) diff(beta_incomplete_generalized(a,b,z1,z2),z1);
                                      b - 1   a - 1
(%o17)                      - (1 - z1)      z1

(%i18) integrate(beta_incomplete_generalized(a,b,z1,z2),z1);
(%o18) beta_incomplete_generalized(a, b, z1, z2) z1
                                        + beta_incomplete(a + 1, b, z1)

(%i19) integrate(beta_incomplete_generalized(a,b,z1,z2),z2);
(%o19) beta_incomplete_generalized(a, b, z1, z2) z2
                                        - beta_incomplete(a + 1, b, z2)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_regularized -->
<!-- signatures: beta_incomplete_regularized(a, b, z) -->
### Function: beta_incomplete_regularized (a, b, z)

Función beta incompleta regularizada A&S 6.6.2,
definida como



```maxima
beta_incomplete_regularized(a, b, z) = 
                                      beta_incomplete(a, b, z)
                                      ------------------------
                                             beta(a, b)
```


Al igual que `beta_incomplete`, esta definición no es completa.
Véase Funcións.wolfram.com para una definición completa de 
`beta_incomplete_regularized`.


`beta_incomplete_regularized` se simplifica para *a* o *b* 
entero positivo.


Para $z=0$ y $realpart(a)>0$, `beta_incomplete_regularized` se anula.
Para *z=1* y $realpart(b)>0$, `beta_incomplete_regularized` se reduce a 1.


Maxima evalúa `beta_incomplete_regularized` numéricamente para valores reales
y complejos en forma decimal y big float.


Si `beta_expand` vale `true`, Maxima expande 
`beta_incomplete_regularized` para los argumentos $a+n$ o $a-n$,
siendo *n* entero.


Maxima conoce las derivadas de `beta_incomplete_regularized` con respecto a
las variables *a*, *b* y *z*, así como la
integral respecto de la variable *z*.


Ejemplos:


Simplificación para *a* o *b* enteros positivos:



```maxima
(%i1) beta_incomplete_regularized(2,b,z);
                                       b
(%o1)                       1 - (1 - z)  (b z + 1)

(%i2) beta_incomplete_regularized(a,2,z);
                                               a
(%o2)                         (a (1 - z) + 1) z

(%i3) beta_incomplete_regularized(3,2,z);
                                               3
(%o3)                         (3 (1 - z) + 1) z
```


Simplificación para los valores $z=0$ y $z=1$:



```maxima
(%i4) assume(a>0,b>0)$
(%i5) beta_incomplete_regularized(a,b,0);
(%o5)                                 0
(%i6) beta_incomplete_regularized(a,b,1);
(%o6)                                 1
```


Evaluación numérica, tanto con float (precisión doble)
como big float (precisión arbitraria):



```maxima
(%i7) beta_incomplete_regularized(0.12,0.43,0.9);
(%o7)                         .9114011367359802
(%i8) fpprec:32$
(%i9) beta_incomplete_regularized(0.12,0.43,0.9b0);
(%o9)               9.1140113673598075519946998779975b-1
(%i10) beta_incomplete_regularized(1+%i,3/3,1.5*%i);
(%o10)             .2865367499935403 %i - 0.122995963334684
(%i11) fpprec:20$
(%i12) beta_incomplete_regularized(1+%i,3/3,1.5b0*%i);
(%o12)      2.8653674999354036142b-1 %i - 1.2299596333468400163b-1
```


Expansión cuando `beta_expand` vale `true`:



```maxima
(%i13) beta_incomplete_regularized(a+1,b,z);
                                                     b  a
                                              (1 - z)  z
(%o13) beta_incomplete_regularized(a, b, z) - ------------
                                              a beta(a, b)
(%i14) beta_incomplete_regularized(a-1,b,z);
(%o14) beta_incomplete_regularized(a, b, z)
                                                     b  a - 1
                                              (1 - z)  z
                                         - ----------------------
                                           beta(a, b) (b + a - 1)
```


Derivada e integral respecto de *z*:



```maxima
(%i15) diff(beta_incomplete_regularized(a,b,z),z);
                              b - 1  a - 1
                       (1 - z)      z
(%o15)                 -------------------
                           beta(a, b)
(%i16) integrate(beta_incomplete_regularized(a,b,z),z);
(%o16) beta_incomplete_regularized(a, b, z) z
                                                           b  a
                                                    (1 - z)  z
          a (beta_incomplete_regularized(a, b, z) - ------------)
                                                    a beta(a, b)
        - -------------------------------------------------------
                                   b + a
```

<!-- category: SpecialFunctions -->
<!-- keywords: bffac -->
<!-- signatures: bffac(expr, n) -->
### Function: bffac (expr, n)

Versión para "bigfloat" de la función factorial (Gamma desplazada). El segundo argumento indica cuántos dígitos se conservan y devuelven, pudiendo utilizarse para obtener algunas cifras extra.

<!-- category: SpecialFunctions -->
<!-- keywords: bfpsi, bfpsi0 -->
<!-- signatures: bfpsi(n, z, fpprec), bfpsi0(z, fpprec) -->
### Function: bfpsi (n, z, fpprec)

La función `bfpsi` es la poligamma de argumento real *z* y de orden el entero *n*. La función `bfpsi0` es la digamma.  La llamada `bfpsi0 (z, fpprec)` equivale a `bfpsi (0, z, fpprec)`.


Estas funciones devuelven valores "bigfloat". La variable *fpprec* es la precisión "bigfloat" del valor de retorno.

<!-- category: SpecialFunctions -->
<!-- keywords: cbffac -->
<!-- signatures: cbffac(z, fpprec) -->
### Function: cbffac (z, fpprec)

Calcula el factorial de números complejos de punto flotante grandes.


La instrucción `load ("bffac")` carga esta función.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma -->
<!-- signatures: gamma(x) -->
### Function: gamma (x)

La definición básica de la función gamma (A&S 6.1.1) es



```maxima
inf
                              /
                              [     z - 1   - t
                   gamma(z) = I    t      %e    dt
                              ]
                              /
                               0
```


$$
\Gamma\left(z\right)=\int_{0}^{\infty }{t^{z-1}\,e^ {- t }\;dt}
$$


Maxima simplifica `gamma` para enteros positivos y para fracciones positivas
o negativas. Para fracciones de denominador dos, el resultado es un número 
racional multiplicado por `sqrt(%pi)`. La simplificación para valores
enteros la controla `factlim`. Para enteros mayores que `factlim`
el resultado numérico de la función factorial, la cual se utiliza para
calcular `gamma`, producirá un desbordamiento. La simplificación
para números racionales la controla `gammalim` para evitar desbordamientos.
Véanse también `factlim` y `gammalim`.


Para enteros negativos, `gamma` no está definida.


Maxima puede evaluar `gamma` numéricamente para valores reales
y complejos, tanto en formato float (doble precisión) como big float 
(precisión arbitraria).


La función `gamma` tiene simetría especular.


Si `gamma_expand` vale `true`, Maxima expande `gamma`
para argumentos del tipo `z+n` y `z-n`, siendo `n`
un entero.


Maxima conoce la derivada de `gamma`.


Ejemplos:


Simplificación para enteros, fracciones de denominador dos
y números racionales:



```maxima
(%i1) map('gamma,[1,2,3,4,5,6,7,8,9]);
(%o1)               [1, 1, 2, 6, 24, 120, 720, 5040, 40320]

(%i2) map('gamma,[1/2,3/2,5/2,7/2]);
                           sqrt(%pi)  3 sqrt(%pi)  15 sqrt(%pi)
(%o2)          [sqrt(%pi), ---------, -----------, ------------]
                               2           4            8

(%i3) map('gamma,[2/3,5/3,7/3]);
                                        2           1
                                2 gamma(-)  4 gamma(-)
                            2           3           3
(%o3)                [gamma(-), ----------, ----------]
                            3       3           9
```


Evaluación numérica para valores reales y complejos:



```maxima
(%i4) map('gamma,[2.5,2.5b0]);
(%o4)             [1.329340388179137, 1.329340388179137b0]

(%i5) map('gamma,[1.0+%i,1.0b0+%i]);
(%o5) [.4980156681183558 - .1549498283018108 %i, 
                      4.980156681183561b-1 - 1.549498283018107b-1 %i]
```


Simetría especular:



```maxima
(%i6) declare(z,complex)$
(%i7) conjugate(gamma(z));
(%o7)                         gamma(conjugate(z))
```


Maxima expande `gamma(z+n)` y `gamma(z-n)` si 
`gamma_expand` vale `true`:



```maxima
(%i8) gamma_expand:true$
(%i9) [gamma(z+1),gamma(z-1),gamma(z+2)/gamma(z+1)];
                                      gamma(z)
(%o9)                    [z gamma(z), --------, z + 1]
                                       z - 1
```


Derivada de `gamma`:



```maxima
(%i10) diff(gamma(z),z);
(%o10)                         psi (z) gamma(z)
                                  0
```


Véase también `makegamma`.


La constante de Euler-Mascheroni es `%gamma`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_expand -->
<!-- signatures: gamma_expand -->
### Variable: gamma_expand

Valor por defecto: `false`


`gamma_expand` controla la expansión de `gamma_incomplete`.
Si `gamma_expand` vale `true`, `gamma_incomplete(v,z)`
se expande en términos de
`z`, `exp(z)` y `erfc(z)`, siempre que sea posible.



```maxima
(%i1) gamma_incomplete(2,z);
(%o1)                       gamma_incomplete(2, z)
(%i2) gamma_expand:true;
(%o2)                                true
(%i3) gamma_incomplete(2,z);
                                           - z
(%o3)                            (z + 1) %e

(%i4) gamma_incomplete(3/2,z);
                              - z   sqrt(%pi) erfc(sqrt(z))
(%o4)               sqrt(z) %e    + -----------------------
                                               2
```

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete -->
<!-- signatures: gamma_incomplete(a, z) -->
### Function: gamma_incomplete (a, z)

Función gamma incompleta superior, A&S 6.5.3:



```maxima
inf
                             /
                             [     a - 1   - t
    gamma_incomplete(a, z) = I    t      %e    dt
                             ]
                             /
                              z
```


$$
\Gamma\left(a , z\right)=\int_{z}^{\infty }{t^{a-1}\,e^ {- t }\;dt}
$$


Véanse también `gamma_expand` para controlar cómo se expresa
`gamma_incomplete` en términos de funciones elementales y de `erfc`.


Véanse también las funciones relacionadas `gamma_incomplete_regularized` y
`gamma_incomplete_generalized`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_generalized -->
<!-- signatures: gamma_incomplete_generalized(a, z1, z1) -->
### Function: gamma_incomplete_generalized (a, z1, z1)

Función gamma incompleta generalizada.  



```maxima
gamma_incomplete_generalized(a, z1, z2) = 
                                               z2
                                              /
                                              [    a - 1   - t
                                              I   t      %e    dt
                                              ]
                                              /
                                               z1
```


$$
\Gamma\left(a , z_{1}, z_{2}\right)=\int_{z_{1}}^{z_{2}}{t^{a-1}\,e^ {- t }\;dt}
$$


Véanse también `gamma_incomplete` y `gamma_incomplete_regularized`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_lower -->
<!-- signatures: gamma_incomplete_lower(a, z) -->
### Function: gamma_incomplete_lower (a, z)

Función gamma incompleta inferior (A&S 6.5.2):



```maxima
z
                                   /
                                   [  a - 1   - t
    gamma_incomplete_lower(a, z) = I t      %e    dt
                                   ]
                                   /
                                    0
```


$$
\gamma\left(a , z\right)=\int_{0}^{z}{t^{a-1}\,e^ {- t }\;dt}
$$


Véase también `gamma_incomplete` (función gamma incompleta superior).

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_regularized -->
<!-- signatures: gamma_incomplete_regularized(a, z) -->
### Function: gamma_incomplete_regularized (a, z)

Función gamma incompleta superior regularizada, A&S 6.5.1.



```maxima
gamma_incomplete_regularized(a, z) = 
                                        gamma_incomplete(a, z)
                                        ----------------------
                                               gamma(a)
```


$$
{\it Q}\left(a , z\right)={{\Gamma\left(a , z\right)}\over{\Gamma\left(a\right)}}
$$


Véanse también `gamma_expand` para controlar cómo se expresa
`gamma_incomplete` en términos de funciones elementales y de `erfc`.


Véase también `gamma_incomplete`.

<!-- category: SpecialFunctions -->
<!-- keywords: gammalim -->
<!-- signatures: gammalim -->
### Variable: gammalim

Valor por defecto: 10000


La variable `gammalim` controla la simplificación de la función gamma con argumentos enteros o racionales. Si el valor absoluto del argumento no es mayor que `gammalim`, entonces se realizará la simplificación. Nótese que la variable `factlim` también controla la simplificación del resultado de `gamma` con argumento entero.

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_1 -->
<!-- signatures: hankel_1(v, z) -->
### Function: hankel_1 (v, z)

Función de Hankel de primera especie de orden $v$ y argumento $z$
(A&S 9.1.3). La función `hankel_1` se define como



```maxima
bessel_j(v,z) + %i * bessel_y(v,z)
```


Maxima evalúa `hankel_1` numéricamente para el orden real $v$
y el argumento complejo $z$ en doble precisión (float). La evaluación
numérica en gran precisión (bigfloat) y para órdenes complejos no está
implementada.


Si `besselexpand` vale `true`, `hankel_1` se expande en 
términos de funciones elementales cuando el orden $v$ es la mitad
de un entero impar. Véase al respecto `besselexpand`.


Maxima reconoce la derivada de `hankel_1` con respecto del argumento $z$.


Ejemplos:


Evaluación numérica:







```maxima
(%i1) hankel_1(1,0.5);
(%o1)              .2422684576748738 - 1.471472392670243 %i
(%i2) hankel_1(1,0.5+%i);
(%o2)             - .2558287994862166 %i - 0.239575601883016
```


No se soportan órdenes complejos. Maxima devuelve una forma nominal:






```maxima
(%i3) hankel_1(%i,0.5+%i);
(%o3)                       hankel_1(%i, %i + 0.5)
```


Expansión de `hankel_1` cuando `besselexpand` vale `true`:






```maxima
(%i4) hankel_1(1/2,z),besselexpand:true;
                      sqrt(2) sin(z) - sqrt(2) %i cos(z)
(%o4)                 ----------------------------------
                              sqrt(%pi) sqrt(z)
```


Derivada de `hankel_1` respecto del argumento $z$. No está
soportada la derivada respecto del orden $v$. Maxima devuelve una forma nominal:







```maxima
(%i5) diff(hankel_1(v,z),z);
                    hankel_1(v - 1, z) - hankel_1(v + 1, z)
(%o5)               ---------------------------------------
                                       2
(%i6) diff(hankel_1(v,z),v);
                             d
(%o6)                        -- (hankel_1(v, z))
                             dv
```

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_2 -->
<!-- signatures: hankel_2(v, z) -->
### Function: hankel_2 (v, z)

Función de Hankel de segunda especie de orden $v$ y argumento $z$
(A&S 9.1.4). La función `hankel_2` se define como



```maxima
bessel_j(v,z) - %i * bessel_y(v,z)
```


Maxima evalúa `hankel_2` numéricamente para el orden real $v$
y el argumento complejo $z$ en doble precisión (float). La evaluación
numérica en gran precisión (bigfloat) y para órdenes complejos no está
implementada.


Si `besselexpand` vale `true`, `hankel_2` se expande en 
términos de funciones elementales cuando el orden $v$ es la mitad
de un entero impar. Véase al respecto `besselexpand`.


Maxima reconoce la derivada de `hankel_2` con respecto del argumento $z$.


Véanse ejemplos en `hankel_1`.

<!-- category: SpecialFunctions -->
<!-- keywords: log_gamma -->
<!-- signatures: log_gamma(z) -->
### Function: log_gamma (z)

Logaritmo natural de la función gamma.

<!-- category: SpecialFunctions -->
<!-- keywords: makefact -->
<!-- signatures: makefact(expr) -->
### Function: makefact (expr)

Transforma las funciones `binomial`, `gamma` y `beta` que aparecen en *expr* en su notación factorial.


Véase también `makegamma`.

<!-- category: SpecialFunctions -->
<!-- keywords: makegamma -->
<!-- signatures: makegamma(expr) -->
### Function: makegamma (expr)

Transforma las funciones `binomial`, `factorial` y `beta` que aparecen en *expr* en funciones `gamma`.


Véase también `makefact`.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracdenom -->
<!-- signatures: maxpsifracdenom -->
### Variable: maxpsifracdenom

Valor por defecto: 6


Sea *x* un número racional menor que la unidad de la forma `p/q`.
Si `q` es mayor que `maxpsifracnum`, entonces
`psi[n](x)` no devolverá una respuesta simplificada.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracnum -->
<!-- signatures: maxpsifracnum -->
### Variable: maxpsifracnum

Valor por defecto: 6


Sea *x* un número racional menor que la unidad de la forma `p/q`.
Si `p` es mayor que `maxpsifracnum`, entonces
`psi[n](x)` no devolverá una respuesta simplificada.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsinegint -->
<!-- signatures: maxpsinegint -->
### Variable: maxpsinegint

Valor por defecto: -10


La variable `maxpsinegint` guarda el menor valor negativo para el
que `psi[n](x)` intentará calcular un valor exacto. Si
*x* es menor que `maxnegint`, `psi[n](x)` no devolverá
una respuesta simplificada, aunque supiese cómo hacerlo.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsiposint -->
<!-- signatures: maxpsiposint -->
### Variable: maxpsiposint

Valor por defecto: 20


La variable `maxpsiposint` guarda el mayor valor positivo para el 
que `psi[n](x)` intentará calcular un valor exacto.

<!-- category: SpecialFunctions -->
<!-- keywords: numfactor -->
<!-- signatures: numfactor(expr) -->
### Function: numfactor (expr)

Devuelve el factor numérico que multiplica a la expresión *expr*, la cual debe tener un único término. 



```maxima
(%i1) gamma (7/2);
                          15 sqrt(%pi)
(%o1)                     ------------
                               8
(%i2) numfactor (%);
                               15
(%o2)                          --
                               8
```

<!-- category: SpecialFunctions -->
<!-- keywords: psi -->
<!-- signatures: psi[n](x) -->
### Function: psi ([n](x))

Es la derivada de `log (gamma (x))` de orden `n+1`,
de tal manera que `psi[0](x)` es la primera derivada, 
`psi[1](x)` la segunda derivada y así 
sucesivamente.


En general, Maxima no sabe cómo calcular valores numéricos de 
`psi`, pero sí conoce el valor exacto para
algunos argumentos racionales.
Existen algunas variables globales para controlar en qué rangos
racionales debe devolver `psi` resultados exactos, si ello es posible.
Véanse las descripciones de `maxpsiposint`, `maxpsinegint`,
`maxpsifracnum` y `maxpsifracdenom`.
En resumen, *x* debe alcanzar un valor entre `maxpsinegint` y
`maxpsiposint`. Si el valor absoluto de la parte fraccional de
*x* es racional y tiene un numerador menor que `maxpsifracnum`
y un denominador menor que `maxpsifracdenom`, la función `psi`
devolverá un valor exacto.


La función `bfpsi` del paquete `bffac` puede calcular
valores numéricos.

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i -->
<!-- signatures: scaled_bessel_i(v, z) -->
### Function: scaled_bessel_i (v, z)

Es la función de Bessel modificada de primera especie de
orden $v$ y argumento $z$, es decir
$scaled_bessel_i(v,z) = exp(-abs(z))*bessel_i(v, z)$.
Esta función es especialmente útil para calcular $bessel_i$
cuando $z$ es grande. Sin embargo, Maxima no sabe mucho más 
sobre esta función. En cálculos simbólicos, quizás sea
preferible trabajar directamente con la expresión 
`exp(-abs(z))*bessel_i(v, z)`.

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i0 -->
<!-- signatures: scaled_bessel_i0(z) -->
### Function: scaled_bessel_i0 (z)

Idéntica a `scaled_bessel_i(0,z)`.

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i1 -->
<!-- signatures: scaled_bessel_i1(z) -->
### Function: scaled_bessel_i1 (z)

Idéntica a `scaled_bessel_i(1,z)`.

<!-- category: SpecialFunctions -->
<!-- keywords: struve_h -->
<!-- signatures: struve_h(v, z) -->
### Function: struve_h (v, z)

Función H de Struve de orden *v* y argumento *z*, (A&S 12.1.1).

<!-- category: SpecialFunctions -->
<!-- keywords: struve_l -->
<!-- signatures: struve_l(v, z) -->
### Function: struve_l (v, z)

Función L modificada de Struve de orden *v* y argumento *z*, (A&S 12.2.1).

