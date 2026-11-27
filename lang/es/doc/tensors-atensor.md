## atensor

<!-- category: Tensors -->
<!-- keywords: abasep -->
<!-- signatures: abasep(v) -->
### Function: abasep (v)

Analiza si su argumento es un vector base en `atensor`. Esto es, si se trata de un símbolo indexado, siendo el símbolo el mismo que el valor de `asymbol` y si el índice tiene un valor numérico entre 1 y `adim`.

<!-- category: Tensors -->
<!-- keywords: adim -->
<!-- signatures: adim -->
### Variable: adim

Valor por defecto: 0


La dimensión del álgebra. El paquete `atensor` utiliza el valor de `adim` para determinar si un objeto indexado es un vector válido para la base. Véase `abasep`.

<!-- category: Tensors -->
<!-- keywords: af -->
<!-- signatures: af(u, v) -->
### Function: af (u, v)

Una función escalar antisimétrica que se utiliza en relaciones de conmutación. La implementación por defecto analiza si los dos argumentos son vectores base mediante  `abasep` y en tal caso sustituye el valor correspondiente de la matriz  `aform`.

<!-- category: Tensors -->
<!-- keywords: aform -->
<!-- signatures: aform -->
### Variable: aform

Valor por defecto: `ident(3)`


Valores por defecto para las formas bilineales  `sf`, `af` y `av`. El valor por defecto es la matriz identidad `ident(3)`.

<!-- category: Tensors -->
<!-- keywords: alg_type -->
<!-- signatures: alg_type -->
### Function: alg_type

Tipo de álgebra. Valores válidos son `universal`, `grassmann`,
`clifford`, `symmetric`, `symplectic` y `lie_envelop`.

<!-- category: Tensors -->
<!-- keywords: asymbol -->
<!-- signatures: asymbol -->
### Variable: asymbol

Valor por defecto: `v`


Símbolo para los vectores base.

<!-- category: Tensors -->
<!-- keywords: atensimp -->
<!-- signatures: atensimp(expr) -->
### Function: atensimp (expr)

Simplifica la expresión algebraica de un tensor  *expr* de acuerdo con las reglas configuradas mediante una llamada a  `init_atensor`. La simplificación incluye la aplicación recursiva de las reglas de conmutación y llamadas a `sf`, `af` y `av` siempre que sea posible. Se utiliza un algoritmo que asegure que la función termina siempre, incluso en el caso de expresiones complejas.

<!-- category: Tensors -->
<!-- keywords: av -->
<!-- signatures: av(u, v) -->
### Function: av (u, v)

Una función antisimétrica que se utiliza en relaciones de conmutación. La implementación por defecto analiza si los dos argumentos son vectores base mediante  `abasep` y en tal caso sustituye el valor correspondiente de la matriz  `aform`.


Ejemplo:



```maxima
(%i1) load("atensor");
(%o1)       /share/tensor/atensor.mac
(%i2) adim:3;
(%o2)                                  3
(%i3) aform:matrix([0,3,-2],[-3,0,1],[2,-1,0]);
                               [  0    3   - 2 ]
                               [               ]
(%o3)                          [ - 3   0    1  ]
                               [               ]
                               [  2   - 1   0  ]
(%i4) asymbol:x;
(%o4)                                  x
(%i5) av(x[1],x[2]);
(%o5)                                 x
                                       3
```

<!-- category: Tensors -->
<!-- keywords: init_atensor -->
<!-- signatures: init_atensor(alg_type, opt_dims), init_atensor(alg_type) -->
### Function: init_atensor (alg_type, opt_dims)

Inicializa el paquete `atensor` con el tipo de álgebra especificado, *alg_type*, que puede ser una de las siguientes:


`universal`: El álgebra universal no tiene reglas de conmutación.


`grassmann`: El álgebra de Grassman se define mediante la relación de conmutación `u.v+v.u=0`.


`clifford`: El álgebra de Clifford se define mediante la regla de conmutación  `u.v+v.u=-2*sf(u,v)` donde  `sf` es una función escalar simétrica. Para esta álgebra,  *opt_dims* puede contener hasta tres enteros no negativos, que representan el número de dimensiones positivas, degeneradas y negativas, respectivamente, de esta álgebra. Si se suministran los valores de *opt_dims*, `atensor` configurará los valores de `adim` y `aform` de forma apropiada. En otro caso, `adim` tomará por defecto el valor 0 y `aform` no se definirá.


`symmetric`: El álgebra simétrica se define mediante la regla de conmutación `u.v-v.u=0`.


`symplectic`: El álgebra simpléctica se define mediante la regla de conmutación `u.v-v.u=2*af(u,v)`, donde `af` es una función escalar antisimétrica. Para el álgebra simpléctica, *opt_dims* puede contener hasta dos enteros no negativos, que representan las dimensiones no degeneradas y degeneradas, respectivamente. Si se suministran los valores de *opt_dims*, `atensor` configurará los valores de `adim` y `aform` de forma apropiada. En otro caso, `adim` tomará por defecto el valor 0 y `aform` no se definirá.


`lie_envelop`: El álgebra de la envolvente de Lie se define mediante la regla de conmutación `u.v-v.u=2*av(u,v)`, donde `av` es una función antisimétrica.


La función `init_atensor` también reconoce algunos tipos de álgebras predefinidas:


`complex` implementa el álgebra de números complejos como un álgebra de Clifford Cl(0,1). La llamada  `init_atensor(complex)` equivale a `init_atensor(clifford,0,0,1)`.


`quaternion` implementa el álgebra de cuaterniones. La llamada `init_atensor(quaternion)` equivale a
`init_atensor(clifford,0,0,2)`.


`pauli` implementa el álgebra de Pauli como un álgebra de Clifford Cl(3,0). La llamada `init_atensor(pauli)` equivale a `init_atensor(clifford,3)`.


`dirac` implementa el álgebra de Dirac como un álgebra de Clifford Cl(3,1). La llamada `init_atensor(dirac)` equivale a `init_atensor(clifford,3,0,1)`.

<!-- category: Tensors -->
<!-- keywords: sf -->
<!-- signatures: sf(u, v) -->
### Function: sf (u, v)

Una función escalar simétrica que se utiliza en relaciones de conmutación. La implementación por defecto analiza si los dos argumentos son vectores base mediante  `abasep` y en tal caso sustituye el valor correspondiente de la matriz  `aform`.

