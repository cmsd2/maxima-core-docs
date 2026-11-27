## ctensor

<!-- category: Tensors -->
<!-- keywords: bdvac -->
<!-- signatures: bdvac(f) -->
### Function: bdvac (f)

Genera las componentes covariantes de las ecuaciones del campo vacío de la teoría gravitacional de Brans- Dicke gravitational. El campo escalar se especifica con el argumento  *f*, el cual debe ser el nombre de una función no evaluada (precedida de apóstrofo) con dependencias funcionales, por ejemplo,  `'p(x)`.


Las componentes del tensor covariante (second rank covariant field tensor) se almacenan en el arreglo `bd`.

<!-- category: Tensors -->
<!-- keywords: cdisplay -->
<!-- signatures: cdisplay(ten) -->
### Function: cdisplay (ten)

Muestra todos los elementos del tensor *ten* como arreglo multidimensional. Tensors de rango 0 y 1, así como otros tipos de variables, se muestran como en `ldisplay`. Tensors de rango 2 se muestran como matrices bidimensionales, mientras que tensores de mayor rango se muestran como listas de matrices bidimensionales. Por ejemplo, el tensor de Riemann de la métrica de Schwarzschild se puede ver como:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) riemann(false);
(%o4)                                done
(%i5) cdisplay(riem);
               [ 0               0                    0            0      ]
               [                                                          ]
               [                              2                           ]
               [      3 m (r - 2 m)   m    2 m                            ]
               [ 0  - ------------- + -- - ----       0            0      ]
               [            4          3     4                            ]
               [           r          r     r                             ]
               [                                                          ]
    riem     = [                                 m (r - 2 m)              ]
        1, 1   [ 0               0               -----------       0      ]
               [                                      4                   ]
               [                                     r                    ]
               [                                                          ]
               [                                              m (r - 2 m) ]
               [ 0               0                    0       ----------- ]
               [                                                   4      ]
               [                                                  r       ]

                                [    2 m (r - 2 m)       ]
                                [ 0  -------------  0  0 ]
                                [          4             ]
                                [         r              ]
                     riem     = [                        ]
                         1, 2   [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]

                                [         m (r - 2 m)    ]
                                [ 0  0  - -----------  0 ]
                                [              4         ]
                                [             r          ]
                     riem     = [                        ]
                         1, 3   [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]

                                [            m (r - 2 m) ]
                                [ 0  0  0  - ----------- ]
                                [                 4      ]
                                [                r       ]
                     riem     = [                        ]
                         1, 4   [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]

                               [       0         0  0  0 ]
                               [                         ]
                               [       2 m               ]
                               [ - ------------  0  0  0 ]
                    riem     = [    2                    ]
                        2, 1   [   r  (r - 2 m)          ]
                               [                         ]
                               [       0         0  0  0 ]
                               [                         ]
                               [       0         0  0  0 ]

                   [     2 m                                         ]
                   [ ------------  0        0               0        ]
                   [  2                                              ]
                   [ r  (r - 2 m)                                    ]
                   [                                                 ]
                   [      0        0        0               0        ]
                   [                                                 ]
        riem     = [                         m                       ]
            2, 2   [      0        0  - ------------        0        ]
                   [                     2                           ]
                   [                    r  (r - 2 m)                 ]
                   [                                                 ]
                   [                                         m       ]
                   [      0        0        0         - ------------ ]
                   [                                     2           ]
                   [                                    r  (r - 2 m) ]

                                [ 0  0       0        0 ]
                                [                       ]
                                [            m          ]
                                [ 0  0  ------------  0 ]
                     riem     = [        2              ]
                         2, 3   [       r  (r - 2 m)    ]
                                [                       ]
                                [ 0  0       0        0 ]
                                [                       ]
                                [ 0  0       0        0 ]

                                [ 0  0  0       0       ]
                                [                       ]
                                [               m       ]
                                [ 0  0  0  ------------ ]
                     riem     = [           2           ]
                         2, 4   [          r  (r - 2 m) ]
                                [                       ]
                                [ 0  0  0       0       ]
                                [                       ]
                                [ 0  0  0       0       ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [ m          ]
                               3, 1   [ -  0  0  0 ]
                                      [ r          ]
                                      [            ]
                                      [ 0  0  0  0 ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [    m       ]
                               3, 2   [ 0  -  0  0 ]
                                      [    r       ]
                                      [            ]
                                      [ 0  0  0  0 ]

                               [   m                      ]
                               [ - -   0   0       0      ]
                               [   r                      ]
                               [                          ]
                               [        m                 ]
                               [  0   - -  0       0      ]
                    riem     = [        r                 ]
                        3, 3   [                          ]
                               [  0    0   0       0      ]
                               [                          ]
                               [              2 m - r     ]
                               [  0    0   0  ------- + 1 ]
                               [                 r        ]

                                    [ 0  0  0    0   ]
                                    [                ]
                                    [ 0  0  0    0   ]
                                    [                ]
                         riem     = [            2 m ]
                             3, 4   [ 0  0  0  - --- ]
                                    [             r  ]
                                    [                ]
                                    [ 0  0  0    0   ]

                                [       0        0  0  0 ]
                                [                        ]
                                [       0        0  0  0 ]
                                [                        ]
                     riem     = [       0        0  0  0 ]
                         4, 1   [                        ]
                                [      2                 ]
                                [ m sin (theta)          ]
                                [ -------------  0  0  0 ]
                                [       r                ]

                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                     riem     = [ 0        0        0  0 ]
                         4, 2   [                        ]
                                [         2              ]
                                [    m sin (theta)       ]
                                [ 0  -------------  0  0 ]
                                [          r             ]

                              [ 0  0          0          0 ]
                              [                            ]
                              [ 0  0          0          0 ]
                              [                            ]
                   riem     = [ 0  0          0          0 ]
                       4, 3   [                            ]
                              [                2           ]
                              [         2 m sin (theta)    ]
                              [ 0  0  - ---------------  0 ]
                              [                r           ]

                 [        2                                             ]
                 [   m sin (theta)                                      ]
                 [ - -------------         0                0         0 ]
                 [         r                                            ]
                 [                                                      ]
                 [                         2                            ]
                 [                    m sin (theta)                     ]
      riem     = [        0         - -------------         0         0 ]
          4, 4   [                          r                           ]
                 [                                                      ]
                 [                                          2           ]
                 [                                   2 m sin (theta)    ]
                 [        0                0         ---------------  0 ]
                 [                                          r           ]
                 [                                                      ]
                 [        0                0                0         0 ]

(%o5)                                done
```

<!-- category: Tensors -->
<!-- keywords: cframe_flag -->
<!-- signatures: cframe_flag -->
### Variable: cframe_flag

Provoca que los cálculos se realicen respecto de un sistema de referencia móvil.

<!-- category: Tensors -->
<!-- keywords: cgeodesic -->
<!-- signatures: cgeodesic(dis) -->
### Function: cgeodesic (dis)

Es una función del paquete `ctensor` que calcula las ecuaciones geodésicas del movimiento para una métrica dada, las cuales se almacenan en el arreglo `geod[i]`. Si el argumento  *dis* vale `true` entonces se muestran estas ecuaciones.

<!-- category: Tensors -->
<!-- keywords: checkdiv -->
<!-- signatures: checkdiv() -->
### Function: checkdiv ()

Calcula la divergencia covariante del tensor de segundo rango (mixed second rank tensor), cuyo primer índice debe ser covariante, devolviendo las `n` componentes correspondientes del campo vectorial (la divergencia), siendo `n = dim`.

<!-- category: Tensors -->
<!-- keywords: christof -->
<!-- signatures: christof(dis) -->
### Function: christof (dis)

Es una función del paquete `ctensor`. Calcula los símbolos de Christoffel de ambos tipos. El argumento *dis* determina qué resultados se mostrarán de forma inmediata. Los símbolos de Christoffel de primer y segundo tipo se almacenan en los arreglos  `lcs[i,j,k]` y `mcs[i,j,k]`, respectivamente, y se definen simétricos en sus dos primeros índices. Si el argumento de `christof` es `lcs` o `mcs` entonces serán mostrados únicamente los valores no nulos de `lcs[i,j,k]` o `mcs[i,j,k]`, respectivamente. Si el argumento es `all` entonces se mostrarán los valores no nulos de `lcs[i,j,k]` y `mcs[i,j,k]`.  Si el argumento vale `false` entonces no se mostrarán los elementos. El arreglo `mcs[i,j,k]` está definido de tal modo que el último índice es contravariante.

<!-- category: Tensors -->
<!-- keywords: cmetric -->
<!-- signatures: cmetric(dis), cmetric() -->
### Function: cmetric (dis)

Es la función del paquete `ctensor` que calcula la métrica inversa y prepara el paquete para cálculos ulteriores.


Si `cframe_flag` vale `false`, la función calcula la métrica inversa `ug` a partir de la matriz `lg` definida por el usuario. Se calcula también la métrica determinante y se almacena en la variable `gdet`. Además, el paquete determina si la métrica es diagonal y ajusta el valor de `diagmetric` de la forma apropiada. Si el argumento opcional *dis* está presente y no es igual a `false`, el usuario podrá ver la métrica inversa.


Si `cframe_flag` vale `true`, la función espera que los valores de `fri` (la matriz del sistema de referencia inverso) y `lfg` (la matriz del sistema de referencia) estén definidos. A partir de ellos, se calculan la matriz del sistema de referencia `fr` y su métrica `ufg`.

<!-- category: Tensors -->
<!-- keywords: cnonmet_flag -->
<!-- signatures: cnonmet_flag -->
### Variable: cnonmet_flag

Obliga a que se calculen también los coeficientes de no metricidad junto con los coeficientes de conexión. Los coeficientes de no metricidad se calculan con la función `nonmetricity` a partir del vector de no metricidad`nm` suministrado por el usuario.

<!-- category: Tensors -->
<!-- keywords: cograd -->
<!-- signatures: cograd() -->
### Function: cograd ()

Calcula el gradiente covariante de una función escalar permitiendo al usuario
elegir el nombre del vector correspondiente, tal como ilustra el ejemplo que acompaña
a la definición de la función `contragrad`.

<!-- category: Tensors -->
<!-- keywords: contortion -->
<!-- signatures: contortion(tr) -->
### Function: contortion (tr)

Calcula los coeficientes (2,1) de contorsión del tensor de torsión *tr*.

<!-- category: Tensors -->
<!-- keywords: contragrad -->
<!-- signatures: contragrad() -->
### Function: contragrad ()

Calcula el gradiente contravariante de una función escalar permitiendo al usuario elegir el nombre del vector correspondiente, tal como muestra el siguiente ejemplo para la métrica de Schwarzschild:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(f,r);
(%o4)                               [f(r)]
(%i5) cograd(f,g1);
(%o5)                                done
(%i6) listarray(g1);
(%o6)                            [0, f , 0, 0]
                                      r
(%i7) contragrad(f,g2);
(%o7)                                done
(%i8) listarray(g2);
                               f  r - 2 f  m
                                r        r
(%o8)                      [0, -------------, 0, 0]
                                     r
```

<!-- category: Tensors -->
<!-- keywords: csetup -->
<!-- signatures: csetup() -->
### Function: csetup ()

Es la función del paquete `ctensor` que inicializa el paquete y permite al usuario introducir una métrica de forma interactiva. Véase `ctensor` para más detalles.

<!-- category: Tensors -->
<!-- keywords: ct_coords -->
<!-- signatures: ct_coords -->
### Variable: ct_coords

Valor por defecto: `[]`


La variable `ct_coords` contiene una lista de coordenadas. Aunque se define normalmente cuando se llama a la función `csetup`, también se pueden redefinir las coordenadas con la asignación `ct_coords: [j1, j2, ..., jn]` donde  `j` es el nuevo nombre de las coordenadas. Véase también `csetup`.

<!-- category: Tensors -->
<!-- keywords: ct_coordsys -->
<!-- signatures: ct_coordsys(sistema_coordenadas, extra_arg), ct_coordsys(sistema_coordenadas) -->
### Function: ct_coordsys (sistema_coordenadas, extra_arg)

Prepara un sistema de coordenadas predefinido y una métrica. El argumento *sistema_coordenadas* puede ser cualquiera de los siguientes símbolos:



```maxima
Símbolo              Dim Coordenadas       Descripción/comentarios
  --------------------------------------------------------------------------------
  cartesian2d           2  [x,y]             Sistema de coordenadas cartesianas en 2D
  polar                 2  [r,phi]           Sistema de coordenadas polares
  elliptic              2  [u,v]             Sistema de coordenadas elípticas
  confocalelliptic      2  [u,v]             Coordenadas elípticas confocales
  bipolar               2  [u,v]             Sistema de coordenas bipolares
  parabolic             2  [u,v]             Sistema de coordenadas parabólicas
  cartesian3d           3  [x,y,z]           Sistema de coordenadas cartesianas en 3D
  polarcylindrical      3  [r,theta,z]       Polares en 2D con cilíndrica z
  ellipticcylindrical   3  [u,v,z]           Elípticas en 2D con cilíndrica z
  confocalellipsoidal   3  [u,v,w]           Elipsoidales confocales
  bipolarcylindrical    3  [u,v,z]           Bipolares en 2D con cilíndrica z
  paraboliccylindrical  3  [u,v,z]           Parabólicas en 2D con cilíndrica z
  paraboloidal          3  [u,v,phi]         Coordenadas paraboloidales
  conical               3  [u,v,w]           Coordenadas cónicas
  toroidal              3  [u,v,phi]         Coordenadas toroidales
  spherical             3  [r,theta,phi]     Sistema de coordenadas esféricas
  oblatespheroidal      3  [u,v,phi]         Coordenadas esferoidales obleadas
  oblatespheroidalsqrt  3  [u,v,phi]
  prolatespheroidal     3  [u,v,phi]         Coordenadas esferoidales prolatas
  prolatespheroidalsqrt 3  [u,v,phi]
  ellipsoidal           3  [r,theta,phi]     Coordenadas elipsoidales
  cartesian4d           4  [x,y,z,t]         Sistema de coordenadas cartesianas en 4D
  spherical4d           4  [r,theta,eta,phi] Sistema de coordenadas esféricas en 4D
  exteriorschwarzschild 4  [t,r,theta,phi]   Métrica de Schwarzschild
  interiorschwarzschild 4  [t,z,u,v]         Métrica interior de Schwarzschild
  kerr_newman           4  [t,r,theta,phi]   Métrica simétrica con carga axial
```


El argumento `sistema_coordenadas` puede ser también una lista de funciones de transformación, seguida de una lista que contenga los nombres de las coordenadas. Por ejemplo, se puede especificar una métrica esférica como se indica a continuación:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o2)                                done
(%i3) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o3)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
(%i4) ct_coords;
(%o4)                           [r, theta, phi]
(%i5) dim;
(%o5)                                  3
```


Las funciones de transformación se pueden utilizar también si `cframe_flag` vale `true`:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) cframe_flag:true;
(%o2)                                true
(%i3) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o3)                                done
(%i4) fri;
      [ cos(phi) cos(theta)  - cos(phi) r sin(theta)  - sin(phi) r cos(theta) ]
      [                                                                       ]
(%o4) [ sin(phi) cos(theta)  - sin(phi) r sin(theta)   cos(phi) r cos(theta)  ]
      [                                                                       ]
      [     sin(theta)            r cos(theta)                   0            ]
(%i5) cmetric();
(%o5)                                false
(%i6) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o6)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
```


El argumento opcional *extra_arg* puede ser cualquiera de los siguientes:


`cylindrical` indica a `ct_coordsys` que añada una coordenada cilíndrica más.


`minkowski` indica a  `ct_coordsys` que añada una coordenada más con signatura métrica negativa.


`all` indica a  `ct_coordsys` que llame a  `cmetric` y a `christof(false)` tras activar la métrica.


Si la variable global `verbose` vale `true`, `ct_coordsys` muestra los valores de `dim`, `ct_coords`, junto con `lg` o `lfg` y `fri`, dependiendo del valor de `cframe_flag`.

<!-- category: Tensors -->
<!-- keywords: ctaylor -->
<!-- signatures: ctaylor() -->
### Function: ctaylor ()

La función `ctaylor` trunca su argumento convirtiéndolo en un desarrollo de Taylor por medio de la función `taylor` e invocando después a `ratdisrep`. Esto tiene el efecto de eliminar términos de orden alto en la variable de expansión `ctayvar`. El orden de los términos que deben ser eliminados se define `ctaypov`; el punto alrededor del cual se desarrolla la serie se especifica en `ctaypt`.


Como ejemplo, considérese una sencilla métrica que es una perturbación de la de Minkowski. Sin añadir restricciones, incluso una métrica diagonal produce expansiones del tensor de Einstein que pueden llegar a ser muy complejas:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) derivabbrev:true;
(%o3)                                true
(%i4) ct_coords:[t,r,theta,phi];
(%o4)                         [t, r, theta, phi]
(%i5) lg:matrix([-1,0,0,0],[0,1,0,0],[0,0,r^2,0],[0,0,0,r^2*sin(theta)^2]);
                        [ - 1  0  0         0        ]
                        [                            ]
                        [  0   1  0         0        ]
                        [                            ]
(%o5)                   [          2                 ]
                        [  0   0  r         0        ]
                        [                            ]
                        [              2    2        ]
                        [  0   0  0   r  sin (theta) ]
(%i6) h:matrix([h11,0,0,0],[0,h22,0,0],[0,0,h33,0],[0,0,0,h44]);
                            [ h11   0    0    0  ]
                            [                    ]
                            [  0   h22   0    0  ]
(%o6)                       [                    ]
                            [  0    0   h33   0  ]
                            [                    ]
                            [  0    0    0   h44 ]
(%i7) depends(l,r);
(%o7)                               [l(r)]
(%i8) lg:lg+l*h;
         [ h11 l - 1      0          0                 0            ]
         [                                                          ]
         [     0      h22 l + 1      0                 0            ]
         [                                                          ]
(%o8)    [                        2                                 ]
         [     0          0      r  + h33 l            0            ]
         [                                                          ]
         [                                    2    2                ]
         [     0          0          0       r  sin (theta) + h44 l ]
(%i9) cmetric(false);
(%o9)                                done
(%i10) einstein(false);
(%o10)                               done
(%i11) ntermst(ein);
[[1, 1], 62] 
[[1, 2], 0] 
[[1, 3], 0] 
[[1, 4], 0] 
[[2, 1], 0] 
[[2, 2], 24] 
[[2, 3], 0] 
[[2, 4], 0] 
[[3, 1], 0] 
[[3, 2], 0] 
[[3, 3], 46] 
[[3, 4], 0] 
[[4, 1], 0] 
[[4, 2], 0] 
[[4, 3], 0] 
[[4, 4], 46] 
(%o12)                               done
```


Sin embargo, si se recalcula este ejemplo como una aproximación lineal en la variable `l`, se obtienen expresiones más sencillas:



```maxima
(%i14) ctayswitch:true;
(%o14)                               true
(%i15) ctayvar:l;
(%o15)                                 l
(%i16) ctaypov:1;
(%o16)                                 1
(%i17) ctaypt:0;
(%o17)                                 0
(%i18) christof(false);
(%o18)                               done
(%i19) ricci(false);
(%o19)                               done
(%i20) einstein(false);
(%o20)                               done
(%i21) ntermst(ein);
[[1, 1], 6] 
[[1, 2], 0] 
[[1, 3], 0] 
[[1, 4], 0] 
[[2, 1], 0] 
[[2, 2], 13] 
[[2, 3], 2] 
[[2, 4], 0] 
[[3, 1], 0] 
[[3, 2], 2] 
[[3, 3], 9] 
[[3, 4], 0] 
[[4, 1], 0] 
[[4, 2], 0] 
[[4, 3], 0] 
[[4, 4], 9] 
(%o21)                               done
(%i22) ratsimp(ein[1,1]);
                         2      2  4               2     2
(%o22) - (((h11 h22 - h11 ) (l )  r  - 2 h33 l    r ) sin (theta)
                              r               r r

                                2               2      4    2
                  - 2 h44 l    r  - h33 h44 (l ) )/(4 r  sin (theta))
                           r r                r
```


Esta capacidad del paquete `ctensor` puede ser muy útil; por ejemplo, cuando se trabaja en zonas del campo gravitatorio alejadas del origen de éste.

<!-- category: Tensors -->
<!-- keywords: ctaypov -->
<!-- signatures: ctaypov -->
### Variable: ctaypov

Máximo exponente utilizado en los desarrollos de Taylor cuando `ctayswitch` vale `true`.

<!-- category: Tensors -->
<!-- keywords: ctaypt -->
<!-- signatures: ctaypt -->
### Variable: ctaypt

Punto alrededor del cual se realiza un desarrollo de Taylor cuando `ctayswitch` vale `true`.

<!-- category: Tensors -->
<!-- keywords: ctayswitch -->
<!-- signatures: ctayswitch -->
### Variable: ctayswitch

Si vale `true`, obliga a que ciertos cálculos de `ctensor` se lleven a cabo utilizando desarrollos de series de 
Taylor. Estos cálculos hacen referencia a las funciones `christof`, `ricci`, `uricci`, `einstein` y `weyl`.

<!-- category: Tensors -->
<!-- keywords: ctayvar -->
<!-- signatures: ctayvar -->
### Variable: ctayvar

Variable utilizada para desarrollos de Taylor cuando la variable `ctayswitch` vale `true`.

<!-- category: Tensors -->
<!-- keywords: ctorsion_flag -->
<!-- signatures: ctorsion_flag -->
### Variable: ctorsion_flag

Obliga a que se calcule también el tensor de contorsión junto con los coeficientes de conexión. El propio tensor de contorsión se calcula con la función `contortion` a partir del tensor `tr` suministrado por el usuario.

<!-- category: Tensors -->
<!-- keywords: ctransform -->
<!-- signatures: ctransform(M) -->
### Function: ctransform (M)

Es una función del paquete `ctensor`.  Realiza una transformación de coordenadas a partir de una matriz cuadrada simétrica *M* arbitraria. El usuario debe introducir las funciones que definen la transformación.

<!-- category: Tensors -->
<!-- keywords: ctrgsimp -->
<!-- signatures: ctrgsimp -->
### Variable: ctrgsimp

Provoca que se realicen simplificaciones trigonométricas cuando se calculan tensores. La variable `ctrgsimp` afecta únicamente a aquellos cálculos que utilicen un sistema de referencia móvil.

<!-- category: Tensors -->
<!-- keywords: deleten -->
<!-- signatures: deleten(L, n) -->
### Function: deleten (L, n)

Devuelve una nueva lista consistente en *L* sin su *n*-ésimo elemento.

<!-- category: Tensors -->
<!-- keywords: diagmatrixp -->
<!-- signatures: diagmatrixp(M) -->
### Function: diagmatrixp (M)

Devuelve `true` si *M* es una matriz diagonal o un arreglo bidimensional.

<!-- category: Tensors -->
<!-- keywords: diagmetric -->
<!-- signatures: diagmetric -->
### Variable: diagmetric

Valor por defecto: `false`


Si `diagmetric` vale `true` se utilizarán rutinas especiales para calcular todos los objetos geométricos teniendo en cuenta la diagonalidad de la métrica, lo que redundará en una reducción del tiempo de cálculo. Esta opción se fija automáticamente por `csetup` si se especifica una métrica diagonal.

<!-- category: Tensors -->
<!-- keywords: dim -->
<!-- signatures: dim -->
### Variable: dim

Valor por defecto: 4


Es la dimensión de la variedad, que por defecto será 4. La instrucción `dim: n` establecerá la dimensión a cualquier otro valor `n`.

<!-- category: Tensors -->
<!-- keywords: dscalar -->
<!-- signatures: dscalar() -->
### Function: dscalar ()

Calcula el tensor de d’Alembertian de la función escalar una vez se han declarado las dependencias. Por ejemplo:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(p,r);
(%o4)                               [p(r)]
(%i5) factor(dscalar(p));
                          2
                    p    r  - 2 m p    r + 2 p  r - 2 m p
                     r r           r r        r          r
(%o5)               --------------------------------------
                                       2
                                      r
```

<!-- category: Tensors -->
<!-- keywords: einstein -->
<!-- signatures: einstein(dis) -->
### Function: einstein (dis)

Es una función del paquete `ctensor`. La función  `einstein` calcula el tensor de Einstein después de que los símbolos de  Christoffel y el tensor de Ricci hayan sido calculados (con las funciones `christof` y `ricci`).  Si el argumento *dis* vale `true`, entonces se mostrarán los valores no nulos del tensor de Einstein `ein[i,j]`, donde `j` es el índice contravariante. La variable `rateinstein` causará la simplificación racional de estas componentes. Si `ratfac` vale `true` entonces las componentes también se factorizarán.

<!-- category: Tensors -->
<!-- keywords: fb -->
<!-- signatures: fb -->
### Variable: fb

Son los coeficientes del sistema de referencia soporte, tal como los calcula `frame_bracket`.

<!-- category: Tensors -->
<!-- keywords: findde -->
<!-- signatures: findde(A, n) -->
### Function: findde (A, n)

Devuelve la lista de las ecuaciones diferenciales que corresponden a los elementos del arreglo cuadrado *n*-dimensional. El argumento *n* puede ser 2 ó 3; `deindex` es una lista global que contiene los índices de *A* que corresponden a estas ecuaciones diferenciales. Para el tensor de Einstein (`ein`), que es un arreglo bidimensional, si se calcula para la métrica del ejemplo de más abajo, `findde` devuelve las siguientes ecuaciones diferenciales independientes:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) dim:4;
(%o3)                                  4
(%i4) lg:matrix([a,0,0,0],[0,x^2,0,0],[0,0,x^2*sin(y)^2,0],[0,0,0,-d]);
                          [ a  0       0        0  ]
                          [                        ]
                          [     2                  ]
                          [ 0  x       0        0  ]
(%o4)                     [                        ]
                          [         2    2         ]
                          [ 0  0   x  sin (y)   0  ]
                          [                        ]
                          [ 0  0       0       - d ]
(%i5) depends([a,d],x);
(%o5)                            [a(x), d(x)]
(%i6) ct_coords:[x,y,z,t];
(%o6)                            [x, y, z, t]
(%i7) cmetric();
(%o7)                                done
(%i8) einstein(false);
(%o8)                                done
(%i9) findde(ein,2);
                                            2
(%o9) [d  x - a d + d, 2 a d d    x - a (d )  x - a  d d  x + 2 a d d
        x                     x x         x        x    x            x

                                                        2          2
                                                - 2 a  d , a  x + a  - a]
                                                     x      x
(%i10) deindex;
(%o10)                     [[1, 1], [2, 2], [4, 4]]
```

<!-- category: Tensors -->
<!-- keywords: frame_bracket -->
<!-- signatures: frame_bracket(fr, fri, diagframe) -->
### Function: frame_bracket (fr, fri, diagframe)

Es el sistema de referencia soporte (`fb[]`).


Calcula el soporte del sistema de referencia de acuerdo con la siguiente definición:



```maxima
c          c         c        d     e
ifb   = ( ifri    - ifri    ) ifr   ifr
   ab         d,e       e,d      a     b
```

<!-- category: Tensors -->
<!-- keywords: gdet -->
<!-- signatures: gdet -->
### Variable: gdet

Es el determinante del tensor métrico `lg`, calculado por  `cmetric` cuando `cframe_flag` vale `false`.

<!-- category: Tensors -->
<!-- keywords: init_ctensor -->
<!-- signatures: init_ctensor() -->
### Function: init_ctensor ()

Inicializa el paquete `ctensor`.


La función `init_ctensor` reinicializa el paquete `ctensor`. Borra todos los arreglos ("arrays") y matrices utilizados por `ctensor` y reinicializa todas las variables, asignando a `dim` el valor 4 y la métrica del sistema de referencia a la de Lorentz.

<!-- category: Tensors -->
<!-- keywords: invariant1 -->
<!-- signatures: invariant1() -->
### Function: invariant1 ()

Genera el tensor de Euler-Lagrange (ecuaciones de campo) para la densidad invariante de  R^2. Las ecuaciones de campo son las componentes del arreglo `inv1`.

<!-- category: Tensors -->
<!-- keywords: kinvariant -->
<!-- signatures: kinvariant -->
### Variable: kinvariant

Es la invariante de Kretchmann, tal como la calcula la función `rinvariant`.

<!-- category: Tensors -->
<!-- keywords: kt -->
<!-- signatures: kt -->
### Variable: kt

Es el tensor de contorsión, calculado a partir de `tr` por la función `contortion`.

<!-- category: Tensors -->
<!-- keywords: leinstein -->
<!-- signatures: leinstein(dis) -->
### Function: leinstein (dis)

Es el tensor covariante de Einstein. La función `leinstein` almacena los valores del tensor covariante de Einstein en el arreglo `lein`. El tensor covariante de Einstein se calcula a partir del tensor de Einstein `ein` multiplicándolo por el tensor métrico. Si el argumento  *dis* vale `true`, entonces se mostrarán los valores no nulos del tensor covariante de Einstein.

<!-- category: Tensors -->
<!-- keywords: lfg -->
<!-- signatures: lfg -->
### Variable: lfg

Es la covariante de la métrica del sistema de referencia. Por defecto, está inicializada al sistema de referencia tetradimensional de Lorentz con signatura  (+,+,+,-). Se utiliza cuando `cframe_flag` vale `true`.

<!-- category: Tensors -->
<!-- keywords: lg -->
<!-- signatures: lg -->
### Variable: lg

Es el tensor métrico. Este tensor se debe especificar (como matriz cuadrada de orden `dim`) antes de que se hagan otros cálculos.

<!-- category: Tensors -->
<!-- keywords: lriem -->
<!-- signatures: lriem -->
### Variable: lriem

Es el tensor covariante de Riemann. Lo calcula la función `lriemann`.

<!-- category: Tensors -->
<!-- keywords: lriemann -->
<!-- signatures: lriemann(dis) -->
### Function: lriemann (dis)

Es el tensor covariante de Riemann (`lriem[]`).


Calcula el tensor covariante de Riemann como un arreglo `lriem`. Si el argumento *dis* vale `true`, sólo se muestran los valores no nulos.


Si la variable `cframe_flag` vale `true`, el tensor covariante de Riemann se calcula directamente de los coeficientes del campo. En otro caso, el tensor de Riemann (3,1) se calcula en primer lugar.


Para más información sobre la ordenación de los índices, véase `riemann`.

<!-- category: Tensors -->
<!-- keywords: nm -->
<!-- signatures: nm -->
### Variable: nm

Vector de no metricidad suministrado por el usuario. Lo utiliza la función `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nmc -->
<!-- signatures: nmc -->
### Variable: nmc

Son los coeficientes de no metricidad, calculados a partir de `nm` por la función `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nonmetricity -->
<!-- signatures: nonmetricity(nm) -->
### Function: nonmetricity (nm)

Calcula los coeficientes (2,1) de no metricidad del vector de no metricidad *nm*.

<!-- category: Tensors -->
<!-- keywords: np -->
<!-- signatures: np -->
### Variable: np

Es la cuaterna nula de Newman-Penrose, tal como la calcula la función `nptetrad`.

<!-- category: Tensors -->
<!-- keywords: npi -->
<!-- signatures: npi -->
### Variable: npi

Es la cuaterna nula "raised-index Newman-Penrose". Lo calcula la función `nptetrad`.
Se define como `ug.np`. El producto `np.transpose(npi)` es constante:



```maxima
(%i39) trigsimp(np.transpose(npi));
                              [  0   - 1  0  0 ]
                              [                ]
                              [ - 1   0   0  0 ]
(%o39)                        [                ]
                              [  0    0   0  1 ]
                              [                ]
                              [  0    0   1  0 ]
```

<!-- category: Tensors -->
<!-- keywords: nptetrad -->
<!-- signatures: nptetrad() -->
### Function: nptetrad ()

Calcula la cuaterna nula de Newman-Penrose (`np`). Véase `petrov` para un ejemplo.


La cuaterna nula se construye bajo la suposición de que se está utilizando una métrica tetradimensional ortonormal con signatura métrica (-,+,+,+). Los componentes de la cuaterna nula se relacionan con la inversa de la matriz del sistema de referencia de la siguiente manera:



```maxima
np  = (fri  + fri ) / sqrt(2)
  1       1      2

np  = (fri  - fri ) / sqrt(2)
  2       1      2

np  = (fri  + %i fri ) / sqrt(2)
  3       3         4

np  = (fri  - %i fri ) / sqrt(2)
  4       3         4
```

<!-- category: Tensors -->
<!-- keywords: ntermst -->
<!-- signatures: ntermst(f) -->
### Function: ntermst (f)

Permite hacerse una idea del tamaño del tensor *f*.

<!-- category: Tensors -->
<!-- keywords: petrov -->
<!-- signatures: petrov() -->
### Function: petrov ()

Calcula la clasificación de  Petrov de la métrica caracterizada por `psi[0]`...`psi[4]`.


Por ejemplo, lo que sigue demuestra cómo obtener la clasificación de Petrov para la métrica de Kerr:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) (cframe_flag:true,gcd:spmod,ctrgsimp:true,ratfac:true);
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) ug:invert(lg)$
(%i5) weyl(false);
(%o5)                                done
(%i6) nptetrad(true);
(%t6) np = 

       [  sqrt(r - 2 m)           sqrt(r)                                     ]
       [ ---------------   ---------------------      0             0         ]
       [ sqrt(2) sqrt(r)   sqrt(2) sqrt(r - 2 m)                              ]
       [                                                                      ]
       [  sqrt(r - 2 m)            sqrt(r)                                    ]
       [ ---------------  - ---------------------     0             0         ]
       [ sqrt(2) sqrt(r)    sqrt(2) sqrt(r - 2 m)                             ]
       [                                                                      ]
       [                                              r      %i r sin(theta)  ]
       [        0                    0             -------   ---------------  ]
       [                                           sqrt(2)       sqrt(2)      ]
       [                                                                      ]
       [                                              r       %i r sin(theta) ]
       [        0                    0             -------  - --------------- ]
       [                                           sqrt(2)        sqrt(2)     ]

                             sqrt(r)          sqrt(r - 2 m)
(%t7) npi = matrix([- ---------------------, ---------------, 0, 0], 
                      sqrt(2) sqrt(r - 2 m)  sqrt(2) sqrt(r)

          sqrt(r)            sqrt(r - 2 m)
[- ---------------------, - ---------------, 0, 0], 
   sqrt(2) sqrt(r - 2 m)    sqrt(2) sqrt(r)

           1               %i
[0, 0, ---------, --------------------], 
       sqrt(2) r  sqrt(2) r sin(theta)

           1                 %i
[0, 0, ---------, - --------------------])
       sqrt(2) r    sqrt(2) r sin(theta)

(%o7)                                done
(%i7) psi(true);
(%t8)                              psi  = 0
                                      0

(%t9)                              psi  = 0
                                      1

                                          m
(%t10)                             psi  = --
                                      2    3
                                          r

(%t11)                             psi  = 0
                                      3

(%t12)                             psi  = 0
                                      4
(%o12)                               done
(%i12) petrov();
(%o12)                                 D
```


La función de clasificación de Petrov se basa en el algoritmo publicado en "Classifying geometries in general relativity: III Classification in practice" de Pollney, Skea, and d’Inverno, Class. Quant. Grav. 17 2885-2902 (2000).
Excepto para algunos ejemplos sencillos, esta implementación no ha sido exhaustivamente probada, por lo que puede contener errores.

<!-- category: Tensors -->
<!-- keywords: ratchristof -->
<!-- signatures: ratchristof -->
### Variable: ratchristof

Obliga a que la función `christof` aplique la simplificación racional.

<!-- category: Tensors -->
<!-- keywords: rateinstein -->
<!-- signatures: rateinstein -->
### Variable: rateinstein

Valor por defecto: `true`


Si vale `true` entonces se hará la simplificación racional en los componentes no nulos de los tensores de Einstein; si `ratfac` vale `true` entonces las componentes también serán factorizadas.

<!-- category: Tensors -->
<!-- keywords: ratriemann -->
<!-- signatures: ratriemann -->
### Variable: ratriemann

Valor por defecto: `true`


Es una de las variables que controlan la simplificación de los tensores de Riemann; si vale `true`, entonces se llevará a cabo la simplificación racional; si `ratfac` vale `true` entonces las componentes también serán factorizadas.

<!-- category: Tensors -->
<!-- keywords: ratweyl -->
<!-- signatures: ratweyl -->
### Variable: ratweyl

Valor por defecto: `true`


Si vale `true`, entonces la función `weyl` llevará a cabo la simplificación racional de los valores del tensor de Weyl. si `ratfac` vale `true` entonces las componentes también serán factorizadas.

<!-- category: Tensors -->
<!-- keywords: ric -->
<!-- signatures: ric -->
### Variable: ric

Es el tensor de Ricci. Lo calcula la función `ricci`.

<!-- category: Tensors -->
<!-- keywords: ricci -->
<!-- signatures: ricci(dis) -->
### Function: ricci (dis)

Es una función del paquete `ctensor`. La función `ricci` calcula las componentes covariantes (simétricas) 
`ric[i,j]` del tensor de Ricci. Si el argumento *dis* vale `true`, entonces se muestran las componentes no nulas.

<!-- category: Tensors -->
<!-- keywords: riem -->
<!-- signatures: riem -->
### Variable: riem

Es el tensor (3,1) de Riemann. Se calcula cuando se invoca la función `riemann`. Para información sobre el indexado, véase la descripción de  `riemann`.


Si `cframe_flag` vale `true`, `riem` se calcula a partir del tensor covariante de Riemann `lriem`.

<!-- category: Tensors -->
<!-- keywords: riemann -->
<!-- signatures: riemann(dis) -->
### Function: riemann (dis)

Es una función del paquete `ctensor`. La función `riemann` calcula el tensor de curvatura de Riemann a partir de la métrica dada y de los símbolos de Christoffel correspondientes. Se utiliza el siguiente convenio sobre los índices:



```maxima
l      _l       _l       _l   _m    _l   _m
 R[i,j,k,l] =  R    = |      - |      + |    |   - |    |
                ijk     ij,k     ik,j     mk   ij    mj   ik
```


Esta notación es consistente con la notación utilizada por el paquete `itensor` y su función `icurvature`. Si el argumento opcional *dis* vale `true`, se muestran las componentes no nulas únicas de `riem[i,j,k,l]`. Como en el caso del tensor de Einstein, ciertas variables permiten controlar al usuario la simplificación de las componentes del tensor de Riemann. Si  `ratriemann` vale `true`, entonces se hará la simplificación racional. Si `ratfac` vale `true`, entonces se factorizarán todas las componentes.


Si la variable `cframe_flag` vale `false`, el tensor de Riemann se calcula directamente a partir de los símbolos de Christoffel. Si `cframe_flag` vale `true`, el tensor covariante de Riemann se calcula a partir de los coeficientes del campo.

<!-- category: Tensors -->
<!-- keywords: rinvariant -->
<!-- signatures: rinvariant() -->
### Function: rinvariant ()

Calcula la invariante de Kretchmann (`kinvariant`) obtenida por contracción de los tensores.



```maxima
lriem[i,j,k,l]*uriem[i,j,k,l].
```


Este objeto no se simplifica automáticamente al ser en ocasiones muy grande.

<!-- category: Tensors -->
<!-- keywords: scurvature -->
<!-- signatures: scurvature() -->
### Function: scurvature ()

Devuelve la curvatura escalar (obtenida por contracción del tensor de Ricci) de la variedad de Riemannian con la métrica dada.

<!-- category: Tensors -->
<!-- keywords: symmetricp -->
<!-- signatures: symmetricp(M) -->
### Function: symmetricp (M)

Devuelve `true` si *M* es una matriz simétrica o un arreglo bidimensional.

<!-- category: Tensors -->
<!-- keywords: tensorkill -->
<!-- signatures: tensorkill -->
### Variable: tensorkill

Variable que indica si el paquete de tensores se ha inicializado. Utilizada por `csetup` y reinicializada por `init_ctensor`.

<!-- category: Tensors -->
<!-- keywords: tr -->
<!-- signatures: tr -->
### Variable: tr

Tensor de rango 3 suministrado por el usuario y que representa una torsión. Lo utiliza la función `contortion`.

<!-- category: Tensors -->
<!-- keywords: ufg -->
<!-- signatures: ufg -->
### Variable: ufg

Es la métrica del sistema de referencia inverso. La calcula `lfg` cuando `cmetric` es invocada tomando  `cframe_flag` el valor  `true`.

<!-- category: Tensors -->
<!-- keywords: ug -->
<!-- signatures: ug -->
### Variable: ug

Es la inversa del tensor métrico. Lo calcula la función `cmetric`.

<!-- category: Tensors -->
<!-- keywords: uric -->
<!-- signatures: uric -->
### Variable: uric

Es el tensor contravariante de Ricci. Lo calcula la función `uricci`.

<!-- category: Tensors -->
<!-- keywords: uricci -->
<!-- signatures: uricci(dis) -->
### Function: uricci (dis)

Esta función calcula en primer lugar las componentes covariantes  `ric[i,j]` del tensor de Ricci. Después se calcula el tensor de Ricci utilizando la métrica contravariante. Si el valor del argumento *dis* vale `true`, entonces se mostrarán directamente las componentes `uric[i,j]` (el índice *i* es covariante y el *j* contravariante). En otro caso,  `ricci(false)` simplemente calculará las entradas del arreglo `uric[i,j]` sin mostrar los resultados.

<!-- category: Tensors -->
<!-- keywords: uriem -->
<!-- signatures: uriem -->
### Variable: uriem

Es el tensor contravariante de Riemann. Lo calcula la función `uriemann`.

<!-- category: Tensors -->
<!-- keywords: uriemann -->
<!-- signatures: uriemann(dis) -->
### Function: uriemann (dis)

Calcula las componentes contravariantes del tensor de curvatura de Riemann como un arreglo `uriem[i,j,k,l]`.  Éstos se muestran si *dis* vale `true`.

<!-- category: Tensors -->
<!-- keywords: weyl -->
<!-- signatures: weyl(dis) -->
### Function: weyl (dis)

Calcula el tensor conforme de Weyl. Si el argumento *dis* vale `true`, se le mostrarán al usuario las componentes no nulas `weyl[i,j,k,l]`. En otro caso, estas componentes serán únicamente calculadas y almacenadas. Si la variable `ratweyl` vale `true`, entonces las componentes se simplifican racionalmente; si `ratfac` vale `true` los resultados también se simplificarán.

