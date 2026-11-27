## unit

<!-- category: Units -->
<!-- keywords: %unitexpand -->
<!-- signatures: %unitexpand -->
### Variable: %unitexpand

Valor por defecto: `2`


Es el valor suministrado a `metricexpandall` durante la carga del
paquete `unit`.

<!-- category: Units -->
<!-- keywords: convert -->
<!-- signatures: convert(expr, list) -->
### Function: convert (expr, list)

La función `convert` permite conversiones de una sola vez sin
alterar el entorno global de ejecución. Acepta tanto un único argumento
como una lista de unidades a utilizar en las conversiones. Cuando se realiza
una llamada a `convert` se ignora el sistema global de evaluación, con 
el fin de evitar que el resultado deseado sea nuevamente transformado.
Como consecuencia de esto, en los cálculos con decimales, los avisos de
tipo `rat` se harán visibles si la variable global `ratprint`
vale `true`. Otra propiedad de `convert` es que permite al
usuario hacer conversiones al sistema fundamental de dimensiones incluso
cuando el entorno ha sido ajustado para simplificar a una dimensión
derivada.


```maxima
(%i2) kg*m/s^2;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) convert(kg*m/s^2,[g,km,s]);
                                     g km
(%o3)                                ----
                                       2
                                      s


(%i4) convert(kg*m/s^2,[g,inch,minute]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                              18000000000   %in g
(%o4)                        (-----------) (-----)
                                  127           2
                                            %min


(%i5) convert(kg*m/s^2,[N]);
(%o5)                                  N


(%i6) convert(kg*m^2/s^2,[N]);
(%o6)                                 m N


(%i7) setunits([N,J]);
(%o7)                                done


(%i8) convert(kg*m^2/s^2,[N]);
(%o8)                                 m N


(%i9) convert(kg*m^2/s^2,[N,inch]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                 5000
(%o9)                           (----) (%in N)
                                 127


(%i10) convert(kg*m^2/s^2,[J]);
(%o10)                                 J


(%i11) kg*m^2/s^2;
(%o11)                                 J


(%i12) setunits([g,inch,s]);
(%o12)                               done


(%i13) kg*m/s^2;
(%o13)                                 N


(%i14) uforget(N);
(%o14)                               false


(%i15) kg*m/s^2;
                                5000000   %in g
(%o15)                         (-------) (-----)
                                  127       2
                                           s


(%i16) convert(kg*m/s^2,[g,inch,s]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                5000000   %in g
(%o16)                         (-------) (-----)
                                  127       2
                                           s
```


Véanse también `setunits` y `uforget`.
Para hacer uso de esta función ejecútese `load("unit")`.

<!-- category: Units -->
<!-- keywords: metricexpandall -->
<!-- signatures: metricexpandall(x) -->
### Function: metricexpandall (x)

Reconstruye automáticamente las listas globales de unidades creando todas
los múltiplos y submúltiplos métricos necesarios. El argumento numérico 
*x* se utiliza para especificar cuántos prefijos numéricos quiere 
utilizar el usuario. Los argumentos son los siguientes:


```maxima
0 - none. Only base units
               1 - kilo, centi, milli
(por defecto)  2 - giga, mega, kilo, hecto, deka, deci, centi,
                   milli, micro, nano
               3 - peta, tera, giga, mega, kilo, hecto, deka,
                   deci, centi, milli, micro, nano, pico, 
                   femto
               4 - todos
```


Normalmente, Maxima no definirá el juego completo de múltiplos y 
submúltiplos, lo que implica un número muy grande de unidades, pero
`metricexpandall` puede utilizarse para reconstruir la lista. La
variable fundamental del paquete `unit` es `%unitexpand`.

<!-- category: Units -->
<!-- keywords: setunits -->
<!-- signatures: setunits(list) -->
### Function: setunits (list)

El paquete `unit` no utiliza por defecto dimensiones derivadas, pero convierte
todas las unidades a las siete fundamentales en unidades MKS.



```maxima
(%i2) N;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) dyn;
                                   1      kg m
(%o3)                           (------) (----)
                                 100000     2
                                           s


(%i4) g;
                                    1
(%o4)                             (----) (kg)
                                   1000


(%i5) centigram*inch/minutes^2;
                                  127        kg m
(%o5)                       (-------------) (----)
                             1800000000000     2
                                              s
```


Este es el comportamiento que se desea en ciertos casos. Si
el usuario necesita utilizar otras unidades, habrá de utilizar la
instrucción `setunits`:


```maxima
(%i6) setunits([centigram,inch,minute]);
(%o6)                                done


(%i7) N;
                            1800000000000   %in cg
(%o7)                      (-------------) (------)
                                 127            2
                                            %min


(%i8) dyn;
                               18000000   %in cg
(%o8)                         (--------) (------)
                                 127          2
                                          %min


(%i9) g;
(%o9)                             (100) (cg)


(%i10) centigram*inch/minutes^2;
                                    %in cg
(%o10)                              ------
                                        2
                                    %min
```


La especificación de las variables es relativamente flexible.
Por ejemplo, si se quiere volver a utilizar kilogramos, metros y
segundos como unidades por defecto, podemos hacer:


```maxima
(%i11) setunits([kg,m,s]);
(%o11)                               done


(%i12) centigram*inch/minutes^2;
                                  127        kg m
(%o12)                      (-------------) (----)
                             1800000000000     2
                                              s
```


Las unidades derivadas también se controlan con esta misma instrucción:


```maxima
(%i17) setunits(N);
(%o17)                               done


(%i18) N;
(%o18)                                 N


(%i19) dyn;
                                    1
(%o19)                           (------) (N)
                                  100000


(%i20) kg*m/s^2;
(%o20)                                 N


(%i21) centigram*inch/minutes^2;
                                    127
(%o21)                        (-------------) (N)
                               1800000000000
```


Téngase en cuenta que el paquete `unit` reconoce que la
combinación de masa, longitud e inversa del cuadrado del tiempo da
lugar a una fuerza, convirtiéndola a newtons. Esta es la forma
general en la que trabaja Maxima. Si el usuario prefiere dinas a newtons,
tan solo tendrá que hacer lo siguiente:


```maxima
(%i22) setunits(dyn);
(%o22)                               done


(%i23) kg*m/s^2;
(%o23)                          (100000) (dyn)


(%i24) centigram*inch/minutes^2;
                                  127
(%o24)                         (--------) (dyn)
                                18000000
```


Para desactivar una unidad se utiliza la instrucción `uforget`:


```maxima
(%i26) uforget(dyn);
(%o26)                               false


(%i27) kg*m/s^2;
                                     kg m
(%o27)                               ----
                                       2
                                      s


(%i28) centigram*inch/minutes^2;
                                  127        kg m
(%o28)                      (-------------) (----)
                             1800000000000     2
                                              s
```

Esto también hubiese funcionado con `uforget(N)` o
`uforget(%force)`. 



Véase también `uforget`. Para hacer uso de esta función ejecútese `load("unit")`.

<!-- category: Units -->
<!-- keywords: uforget -->
<!-- signatures: uforget(list) -->
### Function: uforget (list)

Por defecto, el paquete `unit` convierte todas las unidades a las
siete fundamentales del sistema MKS. Este comportamiento puede alterarse
mediante la instrucción `setunits`. Después, si el usuario quiere
restaurar el comportamiento por defecto podrá hacerlo para una dimensión
determinada haciendo uso de la instrucción `uforget`:


```maxima
(%i13) setunits([centigram,inch,minute]);
(%o13)                               done


(%i14) centigram*inch/minutes^2;
                                    %in cg
(%o14)                              ------
                                        2
                                    %min


(%i15) uforget([cg,%in,%min]);
(%o15)                      [false, false, false]


(%i16) centigram*inch/minutes^2;
                                  127        kg m
(%o16)                      (-------------) (----)
                             1800000000000     2
                                              s
```


La instrucción `uforget` opera
sobre dimensiones, no sobre unidades, de modo que valdrá para
cualquier unidad de una dimensión concreta. La propia dimensión
es una argumento válido para esta función.


Véase también `setunits`. Para hacer uso de esta función ejecútese `load("unit")`.

<!-- category: Units -->
<!-- keywords: usersetunits -->
<!-- signatures: usersetunits -->
### Variable: usersetunits

Valor por defecto: ninguno


En caso de que el usuario desee que el comportamiento por defecto del
paquete `unit` sea distinto del descrito, puede hacer uso del
fichero `maxima-init.mac` y de la variable global `usersetunits`.
El paquete `unit` comprobará al ser cargado si se le ha dado a esta
variable una lista de unidades; en caso afirmativo, aplicará `setunits`
a las unidades de esta lista y las utilizará por defecto. Una llamada a la
función `uforget` permitirá retornar al comportamiento establecido
por defecto por el usuario. Por ejemplo, si en el archivo `maxima-init.mac`
se tiene el siguiente código:


```maxima
usersetunits : [N,J];
```


observaríamos el siguiente comportamiento:


```maxima
(%i1) load("unit")$
*******************************************************************
*                       Units version 0.50                        *
*          Definitions based on the NIST Reference on             *
*              Constants, Units, and Uncertainty                  *
*       Conversion factors from various sources including         *
*                   NIST and the GNU units package                *
*******************************************************************

Redefining necessary functions...
WARNING: DEFUN/DEFMACRO: redefining function
 TOPLEVEL-MACSYMA-EVAL ...
WARNING: DEFUN/DEFMACRO: redefining function MSETCHK ...
WARNING: DEFUN/DEFMACRO: redefining function KILL1 ...
WARNING: DEFUN/DEFMACRO: redefining function NFORMAT ...
Initializing unit arrays...
Done.
User defaults found...
User defaults initialized.


(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) kg*m^3/s^2;
(%o4)                                 J m


(%i5) kg*m*km/s^2;
(%o5)                             (1000) (J)


(%i6) setunits([dyn,eV]);
(%o6)                                done


(%i7) kg*m/s^2;
(%o7)                           (100000) (dyn)


(%i8) kg*m^2/s^2;
(%o8)                     (6241509596477042688) (eV)


(%i9) kg*m^3/s^2;
(%o9)                    (6241509596477042688) (eV m)


(%i10) kg*m*km/s^2;
(%o10)                   (6241509596477042688000) (eV)


(%i11) uforget([dyn,eV]);
(%o11)                           [false, false]


(%i12) kg*m/s^2;
(%o12)                                 N


(%i13) kg*m^2/s^2;
(%o13)                                 J


(%i14) kg*m^3/s^2;
(%o14)                                J m


(%i15) kg*m*km/s^2;
(%o15)                            (1000) (J)
```


De no haber hecho uso de `usersetunits`, las entradas iniciales hubiesen
sido convertidas a unidades MKS y cualquier llamada a `uforget` hubiese
retornado también a MKS. Sin embargo, las preferencias establecidas por el
usuario se respetan en ambos casos. Para eliminar las preferencias del usuario
y volver a utilizar las establecidas por defecto por el paquete `unit`,
debe utilizarse la instrucción `dontusedimension`. La función
`uforget` puede restaurar nuevamente las preferencias del usuario, pero
sólo si `usedimension` mantiene su valor. Alternativamente, 
`kill(usersetunits)`  eliminará completamente cualquier vestigio de las
preferencias del usuario durante la sesión actual. Véanse a continuación
algunos ejemplos de aplicación de estas opciones:


```maxima
(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) setunits([dyn,eV]);
(%o4)                                done


(%i5) kg*m/s^2;
(%o5)                           (100000) (dyn)


(%i6) kg*m^2/s^2;
(%o6)                     (6241509596477042688) (eV)


(%i7) uforget([dyn,eV]);
(%o7)                          [false, false]


(%i8) kg*m/s^2;
(%o8)                                  N


(%i9) kg*m^2/s^2;
(%o9)                                  J


(%i10) dontusedimension(N);
(%o10)                             [%force]


(%i11) dontusedimension(J);
(%o11)                         [%energy, %force]


(%i12) kg*m/s^2;
                                     kg m
(%o12)                               ----
                                       2
                                      s


(%i13) kg*m^2/s^2;
                                         2
                                     kg m
(%o13)                               -----
                                       2
                                      s


(%i14) setunits([dyn,eV]);
(%o14)                               done


(%i15) kg*m/s^2;
                                     kg m
(%o15)                               ----
                                       2
                                      s


(%i16) kg*m^2/s^2;
                                         2
                                     kg m
(%o16)                               -----
                                       2
                                      s


(%i17) uforget([dyn,eV]);
(%o17)                         [false, false]


(%i18) kg*m/s^2;
                                     kg m
(%o18)                               ----
                                       2
                                      s


(%i19) kg*m^2/s^2;
                                         2
                                     kg m
(%o19)                               -----
                                       2
                                      s


(%i20) usedimension(N);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o20)                               true


(%i21) usedimension(J);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o21)                               true


(%i22) kg*m/s^2;
                                     kg m
(%o22)                               ----
                                       2
                                      s


(%i23) kg*m^2/s^2;
                                         2
                                     kg m
(%o23)                               -----
                                       2
                                      s


(%i24) setunits([dyn,eV]);
(%o24)                               done


(%i25) kg*m/s^2;
(%o25)                          (100000) (dyn)


(%i26) kg*m^2/s^2;
(%o26)                    (6241509596477042688) (eV)


(%i27) uforget([dyn,eV]);
(%o27)                           [false, false]


(%i28) kg*m/s^2;
(%o28)                                 N


(%i29) kg*m^2/s^2;
(%o29)                                 J


(%i30) kill(usersetunits);
(%o30)                               done


(%i31) uforget([dyn,eV]);
(%o31)                          [false, false]


(%i32) kg*m/s^2;
                                     kg m
(%o32)                               ----
                                       2
                                      s


(%i33) kg*m^2/s^2;
                                         2
                                     kg m
(%o33)                               -----
                                       2
                                      s
```


Desafortunadamente, esta amplia variedad de opciones puede resultar
confusa en un primer momento, pero una vez se practica un poco con
ellas, el usuario comprobará que tiene un control absoluto sobre
su entorno de trabajo.

