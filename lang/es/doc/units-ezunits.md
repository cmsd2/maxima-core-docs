## ezunits

<!-- category: Units -->
<!-- keywords: ` -->
<!-- signatures: ` -->
### Function: `

Operador de magnitud dimensional. 
Una expresión tal como $a ` b$ representa una magnitud dimensional, siendo
`a` una magnitud adimensional y `b` las unidades.
Se puede utilizar un símbolo como unidad, sin necesidad
de declararlo como tal ni de que deba cumplir propiedades especiales.
Tanto la magnitud como la unidad de una expresión de la forma $a ` b$
pueden extraerse invocando las funciones `qty` y `units`,
respectivamente.


Las operaciones aritméticas con magnitudes dimensionales se realizan
de la forma convencional.



- * 
`(x ` a) * (y ` b)` es igual a $(x * y) ` (a * b)$.
- * 
`(x ` a) + (y ` a)` es igual a $(x + y) ` a$.
- * 
`(x ` a)^y` es igual a $x^y ` a^y$ si `y` es adimensional.


`ezunits` no necesita que las unidades en una suma tengan las mismas 
dimensiones; estos términos serán sumados sin emitirse mensaje de error.


Para utilizar este operador ejecútese primero `load("ezunits")`.


Ejemplos:


Unidades del Sistema Internacional.










```maxima
(%i1) load ("ezunits")$
(%i2) foo : 10 ` m;
(%o2)                        10 ` m
(%i3) qty (foo);
(%o3)                          10
(%i4) units (foo);
(%o4)                           m
(%i5) dimensions (foo);
(%o5)                        length
```



Unidades definidas por el usuario.









```maxima
(%i1) load ("ezunits")$
(%i2) bar : x ` acre;
(%o2)                       x ` acre
(%i3) dimensions (bar);
                                   2
(%o3)                        length
(%i4) fundamental_units (bar);
                                2
(%o4)                          m
```


Unidades ad hoc.










```maxima
(%i1) load ("ezunits")$
(%i2) baz : 3 ` sheep + 8 ` goat + 1 ` horse;
(%o2)           8 ` goat + 3 ` sheep + 1 ` horse
(%i3) subst ([sheep = 3*goat, horse = 10*goat], baz);
(%o3)                       27 ` goat
(%i4) baz2 : 1000`gallon/fortnight;
                                gallon
(%o4)                   1000 ` ---------
                               fortnight
(%i5) subst (fortnight = 14*day, baz2);
                          500   gallon
(%o5)                     --- ` ------
                           7     day
```



Operaciones aritméticas y magnitudes dimensionales.











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` kg + 200 ` kg;
(%o2)                       300 ` kg
(%i3) 100 ` m^3 - 100 ` m^3;
                                  3
(%o3)                        0 ` m
(%i4) (10 ` kg) * (17 ` m/s^2);
                                 kg m
(%o4)                      170 ` ----
                                   2
                                  s
(%i5) (x ` m) / (y ` s);
                              x   m
(%o5)                         - ` -
                              y   s
(%i6) (a ` m)^2;
                              2    2
(%o6)                        a  ` m
```

<!-- category: Units -->
<!-- keywords: `` -->
<!-- signatures: `` -->
### Function: ``

Operador de conversión de unidades.
Una expresión tal como $a ` b `` c$ convierte las unidades `b`
en `c`. El paquete `ezunits` contiene funciones conversoras para
unidades fundamentales del SI, unidades derivadas, así como
algunas otras unidades ajenas al SI.
Las conversiones entre unidades que no estén programadas en `ezunits`
podrán declararse a posteriori.
Las conversiones conocidas por `ezunits` están especificadas en la
variable global `known_unit_conversions`, incluyendo tanto las ya
declaradas por defecto como aquéllas introducidas por el usuario.
Las conversiones para los productos, cocientes y potencias de unidades
se derivan del conjunto de conversiones ya conocidas.


No hay un sistema de representación de unidades que se considere preferible,
razón por la cual las unidades no se convierten a otras a menos que se
indique de forma explícita. Del mismo modo, `ezunits`
no transforma prefijos (milli-, centi-, deci-, etc) a menos que se le
indique.


Para utilizar este operador ejecútese primero `load("ezunits")`.


Ejemplos:


Conjunto de conversiones conocidas.








```maxima
(%i1) load ("ezunits")$
(%i2) display2d : false$
(%i3) known_unit_conversions;
(%o3) {acre = 4840*yard^2,Btu = 1055*J,cfm = feet^3/minute,
       cm = m/100,day = 86400*s,feet = 381*m/1250,ft = feet,
       g = kg/1000,gallon = 757*l/200,GHz = 1000000000*Hz,
       GOhm = 1000000000*Ohm,GPa = 1000000000*Pa,
       GWb = 1000000000*Wb,Gg = 1000000*kg,Gm = 1000000000*m,
       Gmol = 1000000*mol,Gs = 1000000000*s,ha = hectare,
       hectare = 100*m^2,hour = 3600*s,Hz = 1/s,inch = feet/12,
       km = 1000*m,kmol = 1000*mol,ks = 1000*s,l = liter,
       lbf = pound_force,lbm = pound_mass,liter = m^3/1000,
       metric_ton = Mg,mg = kg/1000000,MHz = 1000000*Hz,
       microgram = kg/1000000000,micrometer = m/1000000,
       micron = micrometer,microsecond = s/1000000,
       mile = 5280*feet,minute = 60*s,mm = m/1000,
       mmol = mol/1000,month = 2629800*s,MOhm = 1000000*Ohm,
       MPa = 1000000*Pa,ms = s/1000,MWb = 1000000*Wb,
       Mg = 1000*kg,Mm = 1000000*m,Mmol = 1000000000*mol,
       Ms = 1000000*s,ns = s/1000000000,ounce = pound_mass/16,
       oz = ounce,Ohm = s*J/C^2,
       pound_force = 32*ft*pound_mass/s^2,
       pound_mass = 200*kg/441,psi = pound_force/inch^2,
       Pa = N/m^2,week = 604800*s,Wb = J/A,yard = 3*feet,
       year = 31557600*s,C = s*A,F = C^2/J,GA = 1000000000*A,
       GC = 1000000000*C,GF = 1000000000*F,GH = 1000000000*H,
       GJ = 1000000000*J,GK = 1000000000*K,GN = 1000000000*N,
       GS = 1000000000*S,GT = 1000000000*T,GV = 1000000000*V,
       GW = 1000000000*W,H = J/A^2,J = m*N,kA = 1000*A,
       kC = 1000*C,kF = 1000*F,kH = 1000*H,kHz = 1000*Hz,
       kJ = 1000*J,kK = 1000*K,kN = 1000*N,kOhm = 1000*Ohm,
       kPa = 1000*Pa,kS = 1000*S,kT = 1000*T,kV = 1000*V,
       kW = 1000*W,kWb = 1000*Wb,mA = A/1000,mC = C/1000,
       mF = F/1000,mH = H/1000,mHz = Hz/1000,mJ = J/1000,
       mK = K/1000,mN = N/1000,mOhm = Ohm/1000,mPa = Pa/1000,
       mS = S/1000,mT = T/1000,mV = V/1000,mW = W/1000,
       mWb = Wb/1000,MA = 1000000*A,MC = 1000000*C,
       MF = 1000000*F,MH = 1000000*H,MJ = 1000000*J,
       MK = 1000000*K,MN = 1000000*N,MS = 1000000*S,
       MT = 1000000*T,MV = 1000000*V,MW = 1000000*W,
       N = kg*m/s^2,R = 5*K/9,S = 1/Ohm,T = J/(m^2*A),V = J/C,
       W = J/s}
```



Converiones de unidades fundamentales.
















```maxima
(%i1) load ("ezunits")$
(%i2) 1 ` ft `` m;
Computing conversions to base units; may take a moment. 
                            381
(%o2)                       ---- ` m
                            1250
(%i3) %, numer;
(%o3)                      0.3048 ` m
(%i4) 1 ` kg `` lbm;
                            441
(%o4)                       --- ` lbm
                            200
(%i5) %, numer;
(%o5)                      2.205 ` lbm
(%i6) 1 ` W `` Btu/hour;
                           720   Btu
(%o6)                      --- ` ----
                           211   hour
(%i7) %, numer;
                                        Btu
(%o7)               3.412322274881517 ` ----
                                        hour
(%i8) 100 ` degC `` degF;
(%o8)                      212 ` degF
(%i9) -40 ` degF `` degC;
(%o9)                     (- 40) ` degC
(%i10) 1 ` acre*ft `` m^3;
                        60228605349    3
(%o10)                  ----------- ` m
                         48828125
(%i11) %, numer;
                                          3
(%o11)                1233.48183754752 ` m
```


Transformando pies a metros y viceversa.











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` m + 100 ` ft;
(%o2)                  100 ` m + 100 ` ft
(%i3) (100 ` m + 100 ` ft) `` ft;
                           163100
(%o3)                      ------ ` ft
                            381
(%i4) %, numer;
(%o4)                428.0839895013123 ` ft
(%i5) (100 ` m + 100 ` ft) `` m;
                            3262
(%o5)                       ---- ` m
                             25
(%i6) %, numer;
(%o6)                      130.48 ` m
```


Análisis dimensional para encontrar dimensiones y unidades fundamentales.











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 1 ` acre * ft;
(%o2)                      1 ` acre ft
(%i3) dimensions (foo);
                                   3
(%o3)                        length
(%i4) fundamental_units (foo);
                                3
(%o4)                          m
(%i5) foo `` m^3;
                        60228605349    3
(%o5)                   ----------- ` m
                         48828125
(%i6) %, numer;
                                          3
(%o6)                 1233.48183754752 ` m
```


Declaración de conversiones.











```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (MMBtu = 10^6*Btu, kW = 1000*W);
(%o2)                         done
(%i3) declare_unit_conversion (kWh = kW*hour, MWh = 1000*kWh,
                               bell = 1800*s);
(%o3)                         done
(%i4) 1 ` kW*s `` MWh;
Computing conversions to base units; may take a moment. 
                             1
(%o4)                     ------- ` MWh
                          3600000
(%i5) 1 ` kW/m^2 `` MMBtu/bell/ft^2;
                       1306449      MMBtu
(%o5)                 ---------- ` --------
                      8242187500          2
                                   bell ft
```

<!-- category: Units -->
<!-- keywords: constvalue, declare_constvalue, remove_constvalue -->
<!-- signatures: constvalue(x), declare_constvalue(a, x), remove_constvalue(a) -->
### Function: constvalue (x)

Devuelve la constante declarada para un símbolo.
Los valores constantes se declaran con `declare_constvalue`.


Los valores constantes reconocidos por `constvalue`
son distintos de los valores declarados por `numerval`
y reconocidos por `constantp`.


El paquete `physical_units` declara los valores constantes
de las constantes físicas.


`remove_constvalue` deshace la acción de `declare_constvalue`.


Para utilizar estas funciones ejecútese primero `load("ezunits")`.


Ejemplos:


Valor de una constante física.








```maxima
(%i1) load ("physical_constants")$
(%i2) constvalue (%G);
                                     3
                                    m
(%o2)                    6.67428 ` -----
                                       2
                                   kg s
(%i3) get ('%G, 'description);
(%o3)           Newtonian constant of gravitation
```


Declarando una nueva constante.









```maxima
(%i1) load ("ezunits")$
(%i2) declare_constvalue (FOO, 100 ` lbm / acre);
                                 lbm
(%o2)                      100 ` ----
                                 acre
(%i3) FOO * (50 ` acre);
(%o3)                     50 FOO ` acre
(%i4) constvalue (%);
(%o4)                      5000 ` lbm
```

<!-- category: Units -->
<!-- keywords: declare_dimensions, remove_dimensions -->
<!-- signatures: declare_dimensions(a_1, d_1, ..., a_n, d_n), remove_dimensions(a_1, ..., a_n) -->
### Function: declare_dimensions (a_1, d_1, ..., a_n, d_n)

`declare_dimensions` declara *a_1*, ..., *a_n*
con las dimensiones *d_1*, ..., *d_n*, respectivamente.


Cada *a_k* es un símbolo o lista de símbolos.
En caso de ser una lista, cada símbolo en *a_k* se
declara de dimensión *d_k*.


`remove_dimensions` invierte el efecto de `declare_dimensions`.


Ejecútese `load("ezunits")` para hacer uso de estas funciones.


Ejemplos:









```maxima
(%i1) load ("ezunits") $
(%i2) declare_dimensions ([x, y, z], length, [t, u], time);
(%o2)                         done
(%i3) dimensions (y^2/u);
                                   2
                             length
(%o3)                        -------
                              time
(%i4) fundamental_units (y^2/u);
0 errors, 0 warnings
                                2
                               m
(%o4)                          --
                               s
```

<!-- category: Units -->
<!-- keywords: declare_fundamental_dimensions, remove_fundamental_dimensions, fundamental_dimensions -->
<!-- signatures: declare_fundamental_dimensions(d_1, d_2, d_3, ...), remove_fundamental_dimensions(d_1, d_2, d_3, ...), fundamental_dimensions -->
### Function: declare_fundamental_dimensions (d_1, d_2, d_3, ...)

`declare_fundamental_dimensions` declara dimensiones fundamentales.
Los símbolos *d_1*, *d_2*, *d_3*, ... se añaden a la lista
de dimensiones fundamentales si no están ya presentes en la lista.


`remove_fundamental_dimensions` invierte el efecto de `declare_fundamental_dimensions`.


`fundamental_dimensions` es la lista de dimensiones fundamentales.
Por defecto, la lista comprende algunas dimensiones físicas.


Ejecútese `load("ezunits")` para hacer uso de estas funciones.


Ejemplos:











```maxima
(%i1) load ("ezunits") $
(%i2) fundamental_dimensions;
(%o2) [length, mass, time, current, temperature, quantity]
(%i3) declare_fundamental_dimensions (money, cattle, happiness);
(%o3)                         done
(%i4) fundamental_dimensions;
(%o4) [length, mass, time, current, temperature, quantity, 
                                        money, cattle, happiness]
(%i5) remove_fundamental_dimensions (cattle, happiness);
(%o5)                         done
(%i6) fundamental_dimensions;
(%o6) [length, mass, time, current, temperature, quantity, money]
```

<!-- category: Units -->
<!-- keywords: declare_fundamental_units, remove_fundamental_units -->
<!-- signatures: declare_fundamental_units(u_1, d_1, ..., u_n, d_n), remove_fundamental_units(u_1, ..., u_n) -->
### Function: declare_fundamental_units (u_1, d_1, ..., u_n, d_n)

`declare_fundamental_units` declara *u_1*, ..., *u_n*
de dimensiones *d_1*, ..., *d_n*, respectivamente.
Todos los argumentos deben símbolos.


Tras la llamada a `declare_fundamental_units`,
`dimensions(u_k)` devuelve *d_k* para cada argumento *u_1*, ..., *u_n*,
y `fundamental_units(d_k)` devuelve *u_k* para cada *d_1*, ..., *d_n*.


`remove_fundamental_units` invierte el efecto de `declare_fundamental_units`.


Ejecútese `load("ezunits")` para hacer uso de estas funciones.


Ejemplos:












```maxima
(%i1) load ("ezunits") $
(%i2) declare_fundamental_dimensions (money, cattle, happiness);
(%o2)                         done
(%i3) declare_fundamental_units (dollar, money, goat, cattle,
                                 smile, happiness);
(%o3)                 [dollar, goat, smile]
(%i4) dimensions (100 ` dollar/goat/km^2);
                             money
(%o4)                    --------------
                                      2
                         cattle length
(%i5) dimensions (x ` smile/kg);
                            happiness
(%o5)                       ---------
                              mass
(%i6) fundamental_units (money*cattle/happiness);
0 errors, 0 warnings
                           dollar goat
(%o6)                      -----------
                              smile
```

<!-- category: Units -->
<!-- keywords: declare_unit_conversion -->
<!-- signatures: declare_unit_conversion(u=v, ...) -->
### Function: declare_unit_conversion (u=v, ...)

Añade las ecuaciones *u* = *v*, ... a la lista de conversiones
de unidades conocidas por el operador de conversión $``$.
*u* y *v* son términos multiplicativos en las que las
variables son unidades o expresiones dimensionales literales.


De momento, es imperativo expresar las conversiones de forma
que el miembro izquierdo de cada ecuación sea una unidad simple
(en opsición a una expresión multiplicativa) o una expresión
dimensional literal con la cantidad igual a 1 y con unidad simple.
Está previsto eliminar esta restricción en versiones futuras.


`known_unit_conversions` es la lista de conversiones de unidades conocidas.


Para utilizar esta función ejecútese primero `load("ezunits")`.


Ejemplos:


Conversión de unidades expresadas por ecuaciones con términos multiplicativos.









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (nautical_mile = 1852 * m,
                               fortnight = 14 * day);
(%o2)                         done
(%i3) 100 ` nautical_mile / fortnight `` m/s;
Computing conversions to base units; may take a moment. 
                            463    m
(%o3)                       ---- ` -
                            3024   s
```


Conversión de unidades expresadas por ecuaciones con expresiones dimensionales
literales.









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (1 ` fluid_ounce = 2 ` tablespoon);
(%o2)                         done
(%i3) declare_unit_conversion (1 ` tablespoon = 3 ` teaspoon);
(%o3)                         done
(%i4) 15 ` fluid_ounce `` teaspoon;
Computing conversions to base units; may take a moment. 
(%o4)                     90 ` teaspoon
```

<!-- category: Units -->
<!-- keywords: dimensionless -->
<!-- signatures: dimensionless(L) -->
### Function: dimensionless (L)

Devuelve una expresión sin dimensiones que se puede formar
a partir de una lista *L* de cantidades dimensionales 


Para utilizar esta función ejecútese primero `load("ezunits")`.


Ejemplos:







```maxima
(%i1) load ("ezunits") $
(%i2) dimensionless ([x ` m, y ` m/s, z ` s]);
0 errors, 0 warnings
0 errors, 0 warnings
                               y z
(%o2)                         [---]
                                x
```


Cantidades adimensionales obtenidas a partir de cantidades físicas.
Nótese que el primer elemento de la lista es proporcional a la
constante de estructura fina.








```maxima
(%i1) load ("ezunits") $
(%i2) load ("physical_constants") $
(%i3) dimensionless([%h_bar, %m_e, %m_P, %%e, %c, %e_0]);
0 errors, 0 warnings
0 errors, 0 warnings
                              2
                           %%e        %m_e
(%o3)                [--------------, ----]
                      %c %e_0 %h_bar  %m_P
```

<!-- category: Units -->
<!-- keywords: fundamental_units -->
<!-- signatures: fundamental_units(x), fundamental_units() -->
### Function: fundamental_units (x)

`fundamental_units(x)` devuelve las unidades
asociadas a las dimensiones fundamentales de *x*,
tal como queda determinada por `dimensions(x)`.


*x* puede ser una expresión literal dimensional $a ` b$,
un símbolo con unidades declaradas a través de
`declare_units` o una expresión que contenga a ambos.


`fundamental_units()` devuelve una lista con las unidades
fundamentales conocidas, tal como fueron declaradas por `declare_fundamental_units`.


Para utilizar esta función ejecútese primero `load("ezunits")`.


Ejemplos:










```maxima
(%i1) load ("ezunits")$
(%i2) fundamental_units ();
(%o2)                 [m, kg, s, A, K, mol]
(%i3) fundamental_units (100 ` mile/hour);
                                m
(%o3)                           -
                                s
(%i4) declare_units (aa, g/foot^2);
                                g
(%o4)                         -----
                                  2
                              foot
(%i5) fundamental_units (aa);
                               kg
(%o5)                          --
                                2
                               m
```

<!-- category: Units -->
<!-- keywords: natural_unit -->
<!-- signatures: natural_unit(expr, [v_1, ..., v_n]) -->
### Function: natural_unit (expr, [v_1, ..., v_n])

Busca los exponentes *e_1*, ..., *e_n* tales que
`dimension(expr) = dimension(v_1^e_1 ... v_n^e_n)`.


Para utilizar esta función ejecútese primero `load("ezunits")`.

<!-- category: Units -->
<!-- keywords: qty, declare_qty -->
<!-- signatures: qty(x), declare_qty(a, x) -->
### Function: qty (x)

`qty` devuelve la parte adimensional de la magnitud dimensional *x*,
o *x*, si *x* es adimensional.
*x* puede ser una expresión literal dimensional $a ` b$,
un símbolo con unidades declaradas o una expresión 
que contenga cualquiera o ambos de los anteriores.


`declare_qty` declara que `qty(a)`
debe devolver *x*, siendo *x* una magnitud dimensional.


Para utilizar estas funciones ejecútese primero `load("ezunits")`.


Ejemplos:


`qty` aplicado a expresiones dimensionales literales.











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                       100 ` kg
(%i3) qty (foo);
(%o3)                          100
(%i4) bar : v ` m/s;
                                  m
(%o4)                         v ` -
                                  s
(%i5) foo * bar;
                                  kg m
(%o5)                     100 v ` ----
                                   s
(%i6) qty (foo * bar);
(%o6)                         100 v
```


`qty` aplicado a símbolos con unidades declaradas.











```maxima
(%i1) load ("ezunits")$
(%i2) declare_qty (aa, xx);
(%o2)                          xx
(%i3) qty (aa);
(%o3)                          xx
(%i4) qty (aa^2);
                                 2
(%o4)                          xx
(%i5) foo : 100 ` kg;
(%o5)                       100 ` kg
(%i6) qty (aa * foo);
(%o6)                        100 xx
```

<!-- category: Units -->
<!-- keywords: unitp -->
<!-- signatures: unitp(x) -->
### Function: unitp (x)

Devuelve `true` si *x* es una expresión dimensional
literal, un símbolo declarado como dimensional o
una expresión en la que su operador principal ha sido declarado
como dimensional. En cualquier otro caso, `unitp` devuelve
`false`.


Para utilizar esta función ejecútese primero `load("ezunits")`.


Ejemplos:


`unitp` aplicado a expresiones dimensionales literales.







```maxima
(%i1) load ("ezunits")$
(%i2) unitp (100 ` kg);
(%o2)                         true
```


`unitp` applied to a symbol declared dimensional.









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (foo);
(%o2)                         false
(%i3) declare (foo, dimensional);
(%o3)                         done
(%i4) unitp (foo);
(%o4)                         true
```


`unitp` aplicado a una expresión en la que el operador
principal se declara dimensional.









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (bar (x, y, z));
(%o2)                         false
(%i3) declare (bar, dimensional);
(%o3)                         done
(%i4) unitp (bar (x, y, z));
(%o4)                         true
```

<!-- category: Units -->
<!-- keywords: units, declare_units -->
<!-- signatures: units(x), declare_units(a, u) -->
### Function: units (x)

Devuelve las unidades de la magnitud dimensional *x*,
o 1 en caso de que *x* sea adimensional.


*x* puede ser una expresión literal dimensional $a ` b$,
un símbolo con unidades declaradas por
medio de `declare_units`, o una expresión 
que contenga cualquiera o ambos de los anteriores.


`declare_constvalue` declara que `units(a)`
debe devolver *u*, siendo *u* una expresión.


Para utilizar estas funciones ejecútese primero `load("ezunits")`.


Ejemplos:


`units` aplicado a expresiones dimensionales literales.













```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                              100 ` kg
(%i3) bar : x ` m/s;
                                         m
(%o3)                                x ` -
                                         s
(%i4) units (foo);
(%o4)                                 kg
(%i5) units (bar);
                                       m
(%o5)                                  -
                                       s
(%i6) units (foo * bar);
                                     kg m
(%o6)                                ----
                                      s
(%i7) units (foo / bar);
                                     kg s
(%o7)                                ----
                                      m
(%i8) units (foo^2);
                                        2
(%o8)                                 kg
```


`units` aplicado a símbolos con unidades declaradas.












```maxima
(%i1) load ("ezunits")$
(%i2) linenum:0;
(%o0)                                  0
(%i1) units (aa);
(%o1)                                  1
(%i2) declare_units (aa, J);
(%o2)                                  J
(%i3) units (aa);
(%o3)                                  J
(%i4) units (aa^2);
                                       2
(%o4)                                 J
(%i5) foo : 100 ` kg;
(%o5)                              100 ` kg
(%i6) units (aa * foo);
(%o6)                                kg J
```

