## ctensor

<!-- category: Tensors -->
<!-- keywords: bdvac -->
<!-- signatures: bdvac(f) -->
### Function: bdvac (f)

Gera as componentes covariantes das equações de campo de vácuo da
teoria de gravitação de Brans-Dicke. O campo escalar é especificado
através do argumento *f*, que pode ser um nome de função (com apóstrofo)
com dependências funcionais, e.g., `'p(x)`.


As componentes de segunda categoria do tensor campo covariante são as componentes de segunda categoria
representadas pelo array `bd`.

<!-- category: Tensors -->
<!-- keywords: bimetric -->
<!-- signatures: bimetric() -->
### Function: bimetric ()

*** NOT YET IMPLEMENTED ***


Gera as euauações de campo da teoria bimétrica de Rosen. As equações
de campo são as componentes de um array chamado `rosen`.

<!-- category: Tensors -->
<!-- keywords: cdisplay -->
<!-- signatures: cdisplay(ten) -->
### Function: cdisplay (ten)

Mostra todos os elementos do tensor *ten*, como representados por
um array multidimensional. Tensores de categoria 0 e 1, assim como outros tipos de
variáveis, são mostrados com `ldisplay`. Tensores de categoria 2 são
mostrados como matrizes bidimensionais, enquanto tensores de alta categoria são mostrados
como uma lista de matrizes bidimensionais. Por exemplo, o tensor de Riemann da
métrica de Schwarzschild pode ser visto como:



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

Faz com que cálculos sejam executados relativamente a uma moldura móvel em oposição a
uma métrica holonômica. A moldura é definida através do array da moldura inversa `fri`
e da métrica da moldura `lfg`. Para cálculos usando uma moldura Cartesiana,
`lfg` pode ser a matriz unitária de dimensão apropriada; para
cálculos em uma moldura de Lorentz, `lfg` pode ter a assinatura
apropriada.

<!-- category: Tensors -->
<!-- keywords: cgeodesic -->
<!-- signatures: cgeodesic(dis) -->
### Function: cgeodesic (dis)

Uma função no pacote `ctensor`.
`cgeodesic` calcula as equações geodésicas de
movimento para uma dada métrica.  Elas são armazenadas no array `geod[i]`.  Se
o argumento *dis* for `true` então essas equações são mostradas.

<!-- category: Tensors -->
<!-- keywords: checkdiv -->
<!-- signatures: checkdiv() -->
### Function: checkdiv ()

Calcula a divergência covariante do tensor de segunda categoria misto
(cujo primeiro índice deve ser covariante) imprimindo as
correspondentes n componentes do campo do vetor (a divergência) onde
n = `dim`. Se o argumento para a função for `g` então a
divergência do tensor de Einstein será formada e pode ser zero.
Adicionalmente, a divergência (vetor) é dada no array chamado `div`.

<!-- category: Tensors -->
<!-- keywords: christof -->
<!-- signatures: christof(dis) -->
### Function: christof (dis)

Uma função no pacote `ctensor`.
Essa função calcula os símbolos de Christoffel de ambos
os tipos.  O argumento *dis* determina quais resultados são para serem imediatamente
mostrados.  Os símbolos de Christoffel de primeiro e de segundo tipo são
armazenados nos arrays `lcs[i,j,k]` e `mcs[i,j,k]` respectivamente e
definidos para serem simétricos nos primeiros dois índices. Se o argumento para
`christof` for `lcs` ou for `mcs` então o único valor não nulo de `lcs[i,j,k]`
ou de `mcs[i,j,k]`, respectivamente, será mostrado. Se o argumento for `all`
então o único valor não nulo de `lcs[i,j,k]` e o único valor não nulo de  `mcs[i,j,k]` serão
mostrados.  Se o argumento for `false` então a exibição dos elementos
não acontecerá. Os elementos do array `mcs[i,j,k]` são definidos de uma tal
maneira que o índice final é contravariante.

<!-- category: Tensors -->
<!-- keywords: cmetric -->
<!-- signatures: cmetric(dis), cmetric() -->
### Function: cmetric (dis)

É uma função no pacote `ctensor`
que calcula o inverso da métrica e prepara o pacote para
cálculos adiante.


Se `cframe_flag` for `false`, a função calcula a métrica inversa
`ug` a partir da matriz `lg` (definida pelo usuário). O determinante da métrica é
também calculado e armazenado na variável `gdet`. Mais adiante, o
pacote determina se a métrica é diagonal e escolhe o valor
de `diagmetric` conforme a determinação. Se o argumento opcional *dis*
estiver presente e não for `false`, a saída é mostrada ao usuário pela linha de comando para que ele possa ver
o inverso da métrica.


Se `cframe_flag` for `true`, a função espera que o valor de
`fri` (a matriz moldura inversa) e `lfg` (a métrica da moldura) sejam
definidas. A partir dessas, a matriz da moldura `fr` e a métrica da moldura
inversa `ufg` são calculadas.

<!-- category: Tensors -->
<!-- keywords: cnonmet_flag -->
<!-- signatures: cnonmet_flag -->
### Variable: cnonmet_flag

Faz com que os coeficientes de não metricidade sejam incluídos no cálculo dos
coeficientes de conecção. Os coeficientes de não metricidade são calculados
a partir do vetor de não metricidade `nm` fornecido pelo usuário através da função
`nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: cograd -->
<!-- signatures: cograd() -->
### Function: cograd ()

Calcula o gradiente covariante de uma função escalar permitindo ao
usuário escolher o nome do vetor correspondente como o exemplo sob
`contragrad` ilustra.

<!-- category: Tensors -->
<!-- keywords: contortion -->
<!-- signatures: contortion(tr) -->
### Function: contortion (tr)

Calcula os coeficientes de contorsão de categoria (2,1) a partir do tensor de torsão *tr*.

<!-- category: Tensors -->
<!-- keywords: contragrad -->
<!-- signatures: contragrad() -->
### Function: contragrad ()

Calcula o gradiente contravariante de uma função escalar permitindo

ao usuário escolher o nome do vetor correspondente como o exemplo
abaixo como ilustra a métrica de Schwarzschild:



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

É uma função no pacote `ctensor` (component tensor)
que inicializa o pacote e permite ao usuário inserir uma métrica
interativamente. Veja `ctensor` para mais detalhes.

<!-- category: Tensors -->
<!-- keywords: ct_coords -->
<!-- signatures: ct_coords -->
### Variable: ct_coords

Valor padrão: `[]`


Uma opção no pacote `ctensor`.
`ct_coords` contém uma lista de coordenadas.
Enquanto normalmente definida quando a função `csetup` for chamada,
se pode redefinir as coordenadas com a atribuição
`ct_coords: [j1, j2, ..., jn]` onde os j’s são os novos nomes de coordenadas.
Veja também `csetup`.

<!-- category: Tensors -->
<!-- keywords: ct_coordsys -->
<!-- signatures: ct_coordsys(sistema_de_coordenadas, extra_arg), ct_coordsys(sistema_de_coordenadas) -->
### Function: ct_coordsys (sistema_de_coordenadas, extra_arg)

Escolhe um sistema de coordenadas predefinido e uma métrica. O argumento
*sistema_de_coordenadas* pode ser um dos seguintes símbolos:



```maxima
SYMBOL               Dim Coordenadas       Descrição/comentários
  --------------------------------------------------------------------------
  cartesian2d           2  [x,y]             Sist. de coord. cartesianas 2D
  polar                 2  [r,phi]           Sist. de coord. Polare
  elliptic              2  [u,v]
  confocalelliptic      2  [u,v]
  bipolar               2  [u,v]
  parabolic             2  [u,v]
  cartesian3d           3  [x,y,z]           Sist. de coord. cartesianas 3D
  polarcylindrical      3  [r,theta,z]
  ellipticcylindrical   3  [u,v,z]           Elíptica 2D com Z cilíndrico
  confocalellipsoidal   3  [u,v,w]
  bipolarcylindrical    3  [u,v,z]           Bipolar 2D com Z cilíndrico
  paraboliccylindrical  3  [u,v,z]           Parabólico 2D com Z cilíndrico
  paraboloidal          3  [u,v,phi]
  conical               3  [u,v,w]
  toroidal              3  [u,v,phi]
  spherical             3  [r,theta,phi]     Sist. de coord. Esféricas
  oblatespheroidal      3  [u,v,phi]
  oblatespheroidalsqrt  3  [u,v,phi]
  prolatespheroidal     3  [u,v,phi]
  prolatespheroidalsqrt 3  [u,v,phi]
  ellipsoidal           3  [r,theta,phi]
  cartesian4d           4  [x,y,z,t]         Sist. de coord. 4D
  spherical4d           4  [r,theta,eta,phi]
  exteriorschwarzschild 4  [t,r,theta,phi]   Métrica de Schwarzschild
  interiorschwarzschild 4  [t,z,u,v]        Métrica de Schwarzschild Interior
  kerr_newman           4  [t,r,theta,phi]   Métrica simétrica axialmente alterada
```


`sistema_de_coordenadas` pode também ser uma lista de funções de transformação,
seguida por uma lista contendo as varáveis coordenadas. Por exemplo,
você pode especificar uma métrica esférica como segue:



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


Funções de transformação podem também serem usadas quando `cframe_flag` for `true`:



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


O argumento opcional *extra_arg* pode ser qualquer um dos seguintes:



`cylindrical` diz a `ct_coordsys` para anexar uma coordenada adicional cilíndrica.


`minkowski` diz a `ct_coordsys` para anexar uma coordenada com assinatura métrica negativa.


`all` diz a `ct_coordsys` para chamar `cmetric` e `christof(false)` após escolher a métrica.



Se a variável global `verbose` for escolhida para `true`, `ct_coordsys` mostra os valores de `dim`, `ct_coords`, e ou `lg` ou `lfg` e `fri`, dependendo do valor de `cframe_flag`.

<!-- category: Tensors -->
<!-- keywords: ctaylor -->
<!-- signatures: ctaylor() -->
### Function: ctaylor ()

A função `ctaylor` trunca seus argumentos através da conversão
destes para uma série de Taylor usando `taylor`, e então chamando
`ratdisrep`. Isso tem efeito combinado de abandonar termos
de ordem mais alta na variável de expansão `ctayvar`. A ordem
dos termos que podem ser abandonados é definida através de `ctaypov`; o
ponto em torno do qual a expansão da série é realizada está especificado
em `ctaypt`.


Como um exemplo, considere uma métrica simples que é uma perturbação da
métrica de Minkowski. Sem restrições adicionais, mesmo uma métrica
diagonal produz expressões para o tensor de Einstein que são de longe muito
complexas:



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


Todavia, se nós recalcularmos esse exemplo como uma aproximação que é
linear na variável `l`, pegamos expressões muito simples:



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


Essa compatibilidade pode ser útil, por exemplo, quando trabalhamos no limite
do campo fraco longe de uma fonte gravitacional.

<!-- category: Tensors -->
<!-- keywords: ctaypov -->
<!-- signatures: ctaypov -->
### Variable: ctaypov

Maximo expoente usado em expansões de séries de Taylor quando `ctayswitch` for
escolhida para `true`.

<!-- category: Tensors -->
<!-- keywords: ctaypt -->
<!-- signatures: ctaypt -->
### Variable: ctaypt

Ponto em torno do qual expansões de séries de Taylor sao realizadas quando
`ctayswitch` for escolhida para `true`.

<!-- category: Tensors -->
<!-- keywords: ctayswitch -->
<!-- signatures: ctayswitch -->
### Variable: ctayswitch

Se escolhida para `true`, faz com que alguns cálculos de `ctensor` sejam realizados usando
expansões das séries de Taylor. atualmente, `christof`, `ricci`,
`uricci`, `einstein`, e `weyl` levam em conta essa
escolha.

<!-- category: Tensors -->
<!-- keywords: ctayvar -->
<!-- signatures: ctayvar -->
### Variable: ctayvar

Variável usada pela expansão de séries de Taylor se `ctayswitch` é escolhida para
`true`.

<!-- category: Tensors -->
<!-- keywords: ctorsion_flag -->
<!-- signatures: ctorsion_flag -->
### Variable: ctorsion_flag

Faz com que o tensor de contorsão seja incluído no cálculo dos
coeficientes de conecção. O tensor de contorsão por si mesmo é calculado através de
`contortion` a partir do tensor `tr` fornecido pelo usuário.

<!-- category: Tensors -->
<!-- keywords: ctransform -->
<!-- signatures: ctransform(M) -->
### Function: ctransform (M)

Uma função no pacote `ctensor`
que irá executar uma transformação de coordenadas
sobre uma matriz simétrica quadrada arbitrária *M*. O usuário deve informar as
funçãoes que definem a transformação.  (Formalmente chamada `transform`.)

<!-- category: Tensors -->
<!-- keywords: ctrgsimp -->
<!-- signatures: ctrgsimp -->
### Variable: ctrgsimp

Faz com que simplificações trigonométricas sejam usadas quando tensores forem calculados. Atualmente,
`ctrgsimp` afeta somente cálculos envolvendo uma moldura móvel.

<!-- category: Tensors -->
<!-- keywords: deleten -->
<!-- signatures: deleten(L, n) -->
### Function: deleten (L, n)

Retorna uma nova lista consistindo de *L* com o *n*’ésimo elemento
apagado.

<!-- category: Tensors -->
<!-- keywords: diagmatrixp -->
<!-- signatures: diagmatrixp(M) -->
### Function: diagmatrixp (M)

Retorna `true` se *M* for uma matriz diagonal ou um array (2D).

<!-- category: Tensors -->
<!-- keywords: diagmetric -->
<!-- signatures: diagmetric -->
### Variable: diagmetric

Valor padrão: `false`


Uma opção no pacote `ctensor`.
Se `diagmetric` for `true` rotinas especiais calculam
todos os objetos geométricos (que possuem o tensor métrico explicitamente)
levando em consideração a diagonalidade da métrica. Tempo de
execuçào reduzido irá, com certeza, resultar dessa escolha. Nota: essa opção é escolhida
automaticamente por `csetup` se uma métrica diagonal for especificada.

<!-- category: Tensors -->
<!-- keywords: dim -->
<!-- signatures: dim -->
### Variable: dim

Valor padrão: 4


Uma opção no pacote `ctensor`.
`dim` é a dimensão de multiplicação com o
padrão 4. O comando `dim: n` irá escolher a dimensão para qualquer outro
valor `n`.

<!-- category: Tensors -->
<!-- keywords: einstein -->
<!-- signatures: einstein(dis) -->
### Function: einstein (dis)

Uma função no pacote `ctensor`.
`einstein` calcula o tensor misto de Einstein
após os símbolos de Christoffel e o tensor de Ricci terem sido obtidos
(com as funções `christof` e `ricci`).  Se o argumento *dis* for
`true`, então os valores não nulos do tensor misto de Einstein `ein[i,j]`
serão mostrados quando `j` for o índice contravariante.
A variável `rateinstein` fará com que a simplificação racional ocorra sobre
esses componentes. Se `ratfac` for `true` então as componentes irão
também ser fatoradas.

<!-- category: Tensors -->
<!-- keywords: fb -->
<!-- signatures: fb -->
### Variable: fb

Coeficientes delimitadores da moldura, como calculado através de `frame_bracket`.

<!-- category: Tensors -->
<!-- keywords: findde -->
<!-- signatures: findde(A, n) -->
### Function: findde (A, n)

Retorna uma lista de equações diferenciais únicas (expressões)
correspondendo aos elementos do array quadrado *n* dimensional
*A*. Atualmente, *n* pode ser 2 ou 3. `deindex` é uma lista global
contendo os índices de *A* correspondendo a essas únicas
equações diferenciais. Para o tensor de Einstein (`ein`), que
é um array dimensional, se calculado para a métrica no exemplo
abaixo, `findde` fornece as seguintes equações diferenciais independentes:




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

O delimitador da moldura (`fb[]`).


Calcula o delimitador da moldura conforme a seguinte definição:



```maxima
c          c         c        d     e
ifb   = ( ifri    - ifri    ) ifr   ifr
   ab         d,e       e,d      a     b
```

<!-- category: Tensors -->
<!-- keywords: gdet -->
<!-- signatures: gdet -->
### Variable: gdet

O determinante do tensor métrico `lg`. Calculado através de `cmetric` quando
`cframe_flag` for escolhido para `false`.

<!-- category: Tensors -->
<!-- keywords: init_ctensor -->
<!-- signatures: init_ctensor() -->
### Function: init_ctensor ()

Inicializa o pacote `ctensor`.


A função `init_ctensor` reinicializa o pacote `ctensor`. Essa função remove todos os arrays e matrizes usados por `ctensor`, coloca todos os sinalizadores de volta a seus valores padrão, retorna `dim` para 4, e retorna a métrica da moldura para a métrica da moldura de Lorentz.

<!-- category: Tensors -->
<!-- keywords: invariant1 -->
<!-- signatures: invariant1() -->
### Function: invariant1 ()

Gera o tensor misto de Euler-Lagrange (equações de campo) para a
densidade invariante de R^2. As equações de campo são componentes de um
array chamado `inv1`.

<!-- category: Tensors -->
<!-- keywords: invariant2 -->
<!-- signatures: invariant2() -->
### Function: invariant2 ()

*** NOT YET IMPLEMENTED ***


Gera o tensor misto de Euler-Lagrange (equações de campo) para a
densidade invariante de `ric[i,j]*uriem[i,j]`. As equações de campo são as
componentes de um array chamado `inv2`.

<!-- category: Tensors -->
<!-- keywords: kinvariant -->
<!-- signatures: kinvariant -->
### Variable: kinvariant

O invariante de Kretchmann. Calculado através de `rinvariant`.

<!-- category: Tensors -->
<!-- keywords: kt -->
<!-- signatures: kt -->
### Variable: kt

O tensor de contorsão, calculado a partir de `tr` através de `contortion`.

<!-- category: Tensors -->
<!-- keywords: leinstein -->
<!-- signatures: leinstein(dis) -->
### Function: leinstein (dis)

Tensor covariante de Einstein. `leinstein` armazena o valor do tensor covariante de Einstein no array `lein`. O tensor covariante de Einstein é calculado a partir tensor misto de Einstein `ein` através da multiplicação desse pelo tensor métrico. Se o argumento *dis* for `true`, então os valores não nulos do tensor covariante de Einstein são mostrados.

<!-- category: Tensors -->
<!-- keywords: lfg -->
<!-- signatures: lfg -->
### Variable: lfg

A moldura métrica covariante. Por padrão, é inicializada para a moldura tetradimensional de Lorentz com assinatura (+,+,+,-). Usada quando `cframe_flag` for `true`.

<!-- category: Tensors -->
<!-- keywords: lg -->
<!-- signatures: lg -->
### Variable: lg

O tensor métrico. Esse tensor deve ser especificado (como uma `dim` através da matriz `dim`)
antes que outro cálculo possa ser executado.

<!-- category: Tensors -->
<!-- keywords: lriem -->
<!-- signatures: lriem -->
### Variable: lriem

O tensor covariante de Riemann. Calculado através de `lriemann`.

<!-- category: Tensors -->
<!-- keywords: lriemann -->
<!-- signatures: lriemann(dis) -->
### Function: lriemann (dis)

Tensor covariante de Riemann (`lriem[]`).


Calcula o tensor covariante de Riemann como o array `lriem`. Se o
argumento *dis* for `true`, únicos valores não nulos são mostrados.


Se a variável `cframe_flag` for `true`, o tensor covariante
de Riemann é calculado diretamente dos coeficientes de campo da moldura. De outra forma,
o tensor (3,1) de Riemann é calculado primeiro.


Para informação sobre a ordenação de índice, veja `riemann`.

<!-- category: Tensors -->
<!-- keywords: nm -->
<!-- signatures: nm -->
### Variable: nm

Vetor de não metrcidade fornecido pelo usuário. Usado por `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nmc -->
<!-- signatures: nmc -->
### Variable: nmc

Os coeficientes de não metricidade, calculados a partir de `nm` por `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nonmetricity -->
<!-- signatures: nonmetricity(nm) -->
### Function: nonmetricity (nm)

Calcula o coeficiente de não metricidade de categoria (2,1) a partir do vetor de
não metricidade *nm*.

<!-- category: Tensors -->
<!-- keywords: np -->
<!-- signatures: np -->
### Variable: np

Um tetrad nulo de Newman-Penrose. Calculado através de `nptetrad`.

<!-- category: Tensors -->
<!-- keywords: npi -->
<!-- signatures: npi -->
### Variable: npi

O índice ascendente do tetrad nulo de Newman-Penrose. Calculado através de `nptetrad`.
Definido como `ug.np`. O produto `np.transpose(npi)` é constante:



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

Calcula um tetrad nulo de Newman-Penrose (`np`) e seus índices ascendentes
em contrapartida (`npi`). Veja `petrov` para um exemplo.


O tetrad nulo é construído assumindo que uma moldura métrica ortonormal
tetradimensional com assinatura métrica (-,+,+,+) está sendo usada.
As componentes do tetrad nulo são relacionadas para a matriz moldura inversa
como segue:



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

Fornece ao usuário um rápido quadro do "tamanho" do tensor duplamente
subscrito (array) *f*.  Imprime uma lista de dois elementos onde o segundo
elemento corresponde a N-TERMOS de componentes especificadas através dos primeiros
elementos.  Nesse caminho, é possível rapidamente encontrar as expressões
não nulas e tentar simplificação.

<!-- category: Tensors -->
<!-- keywords: petrov -->
<!-- signatures: petrov() -->
### Function: petrov ()

Calcula a classificação de petrov da métrica caracterizada através de `psi[0]`...`psi[4]`.


Por exemplo, o seguinte demonstra como obter a classificação de Petrov
da métrica de Kerr:



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


A função de classificação Petrov é baseada no algorítmo publicado em
"Classifying geometries in general relativity: III Classification in practice"
por Pollney, Skea, e d’Inverno, Class. Quant. Grav. 17 2885-2902 (2000).
Exceto para alguns casos de teste simples, a implementação não está testada até
19 de Dezembro de 2004, e é provável que contenha erros.

<!-- category: Tensors -->
<!-- keywords: ratchristof -->
<!-- signatures: ratchristof -->
### Variable: ratchristof

Faz com que simplificações racionais sejam aplicadas através de `christof`.

<!-- category: Tensors -->
<!-- keywords: rateinstein -->
<!-- signatures: rateinstein -->
### Variable: rateinstein

Valor padrão: `true`


Se `true` simplificação racional será
executada sobre as componentes não nulas de tensores de Einstein; se
`ratfac` for `true` então as componentes irão também ser fatoradas.

<!-- category: Tensors -->
<!-- keywords: ratriemann -->
<!-- signatures: ratriemann -->
### Variable: ratriemann

Valor padrão: `true`


Um dos comutadores que controlam
simplificações dos tensores de Riemann; se `true`, então simplificações
racionais irão ser concluídas; se `ratfac` for `true` então cada uma das
componentes irá também ser fatorada.

<!-- category: Tensors -->
<!-- keywords: ratweyl -->
<!-- signatures: ratweyl -->
### Variable: ratweyl

Valor padrão: `true`


Se `true`, esse comutador faz com que a função de `weyl`
aplique simplificações racionais aos valores do tensor de Weyl. Se
`ratfac` for `true`, então as componentes irão também ser fatoradas.

<!-- category: Tensors -->
<!-- keywords: ric -->
<!-- signatures: ric -->
### Variable: ric

O tensor misto de Ricci. Calculado através de `ricci`.

<!-- category: Tensors -->
<!-- keywords: ricci -->
<!-- signatures: ricci(dis) -->
### Function: ricci (dis)

Uma função no pacote `ctensor`.
`ricci` calcula as componentes contravariantes
(simétricas) `ric[i,j]` do tensor de Ricci.  Se o argumento *dis* for `true`,
então as componentes não nulas são mostradas.

<!-- category: Tensors -->
<!-- keywords: riem -->
<!-- signatures: riem -->
### Variable: riem

O tensor de categoria (3,1) de Riemann. Calculado quando a função `riemann` é invocada. Para informação sobre ordenação de índices, veja a descrição de `riemann`.


Se `cframe_flag` for `true`, `riem` é calculado a partir do tensor covariante de Riemann `lriem`.

<!-- category: Tensors -->
<!-- keywords: riemann -->
<!-- signatures: riemann(dis) -->
### Function: riemann (dis)

Uma função no pacote `ctensor`.
`riemann` calcula o tensor de curvatura de Riemann
a partir da métrica dada e correspondendo aos símbolos de Christoffel. As seguintes
convenções de índice são usadas:



```maxima
l      _l       _l       _l   _m    _l   _m
 R[i,j,k,l] =  R    = |      - |      + |    |   - |    |
                ijk     ij,k     ik,j     mk   ij    mj   ik
```


Essa notação é consistente com a notação usada por no pacote
`itensor` e sua função `icurvature`.
Se o argumento opcional *dis* for `true`,
as componentes não nulas `riem[i,j,k,l]` serão mostradas.
Como com o tensor de Einstein, vários comutadores escolhidos pelo usuário
controlam a simplificação de componentes do tensor de Riemann.
Se `ratriemann` for `true`, então
simplificação racional será feita. Se `ratfac`
for `true` então
cada uma das componentes irá também ser fatorada.


Se a variável `cframe_flag` for `false`, o tensor de Riemann é
calculado diretamente dos símbolos de Christoffel. Se `cframe_flag` for
`true`, o tensor covariante de Riemann é calculado primeiro dos
coeficientes de campo da moldura.

<!-- category: Tensors -->
<!-- keywords: rinvariant -->
<!-- signatures: rinvariant() -->
### Function: rinvariant ()

Compõe o invariante de Kretchmann (`kinvariant`) obtido através da
contração dos tensores



```maxima
lriem[i,j,k,l]*uriem[i,j,k,l].
```


Esse objeto não é automaticamente simplificado devido ao fato de poder ser muito largo.

<!-- category: Tensors -->
<!-- keywords: scurvature -->
<!-- signatures: scurvature() -->
### Function: scurvature ()

Retorna a curvatura escalar (obtida através da contração
do tensor de Ricci) do Riemaniano multiplicado com a métrica dada.

<!-- category: Tensors -->
<!-- keywords: symmetricp -->
<!-- signatures: symmetricp(M) -->
### Function: symmetricp (M)

Retorna `true` se *M* for uma matriz simétrica ou um array (2D).

<!-- category: Tensors -->
<!-- keywords: tensorkill -->
<!-- signatures: tensorkill -->
### Variable: tensorkill

Variável indicando se o pacote tensor foi inicializado. Escolhida e usada por
`csetup`, retornada ao seu valor original através de `init_ctensor`.

<!-- category: Tensors -->
<!-- keywords: tr -->
<!-- signatures: tr -->
### Variable: tr

Tensor de categoria 3 fornecido pelo usuário representando torsão. Usado por `contortion`.

<!-- category: Tensors -->
<!-- keywords: ufg -->
<!-- signatures: ufg -->
### Variable: ufg

A métrica da moldura inversa. Calculada de `lfg` quando `cmetric` for chamada enquanto `cframe_flag` for escolhida para `true`.

<!-- category: Tensors -->
<!-- keywords: ug -->
<!-- signatures: ug -->
### Variable: ug

O inverso do tensor métrico. Calculado através de `cmetric`.

<!-- category: Tensors -->
<!-- keywords: uric -->
<!-- signatures: uric -->
### Variable: uric

O tensor contravariante de Ricci. Calculado através de `uricci`.

<!-- category: Tensors -->
<!-- keywords: uricci -->
<!-- signatures: uricci(dis) -->
### Function: uricci (dis)

Essa função primeiro calcula as
componentes contravariantes `ric[i,j]` do tensor de Ricci.
Então o tensor misto de Ricci é calculado usando o
tensor métrico contravariante.  Se o valor do argumento *dis*
for `true`, então essas componentes mistas, `uric[i,j]` (o índice "i" é
covariante e o índice "j" é contravariante), serão mostradas
diretamente.  De outra forma, `ricci(false)` irá simplesmente calcular as entradas
do array `uric[i,j]` sem mostrar os resultados.

<!-- category: Tensors -->
<!-- keywords: uriem -->
<!-- signatures: uriem -->
### Variable: uriem

O tensor contravariante de Riemann. Calculado através de `uriemann`.

<!-- category: Tensors -->
<!-- keywords: uriemann -->
<!-- signatures: uriemann(dis) -->
### Function: uriemann (dis)

Calcula as componentes contravariantes do tensor de curvatura
 de Riemann como elementos do array `uriem[i,j,k,l]`.  Esses são mostrados
se *dis* for `true`.

<!-- category: Tensors -->
<!-- keywords: weyl -->
<!-- signatures: weyl(dis) -->
### Function: weyl (dis)

Calcula o tensor conformal de Weyl.  Se o argumento *dis* for
`true`, as componentes não nulas `weyl[i,j,k,l]` irão ser mostradas para o
usuário.  De outra forma, essas componentes irão simplesmente serem calculadas e armazenadas.
Se o comutador `ratweyl` é escolhido para `true`, então as componentes irão ser
racionalmente simplificadas; se `ratfac` for `true` então os resultados irão ser
fatorados também.

