## Pacote atensor

<!-- category: Tensors -->
<!-- keywords: abasep -->
<!-- signatures: abasep(v) -->
### Function: abasep (v)

Verifica se esse argumento é uma base vectorial `atensor` .  


E será, se ele for
um símbolo indexado, com o símbolo sendo o mesmo que o valor de
`asymbol`, e o índice tiver o mesmo valor numérico entre 1
e `adim`.

<!-- category: Tensors -->
<!-- keywords: adim -->
<!-- signatures: adim -->
### Variable: adim

A dimensionalidade da álgebra.  `atensor` usa o valor de `adim`
para determinar se um objecto indexado é uma base vectorial válida. Veja `abasep`.

<!-- category: Tensors -->
<!-- keywords: af -->
<!-- signatures: af(u, v) -->
### Function: af (u, v)

É uma função escalar antisimétrica que é usada em relações comutativas.
A implementação padrão verifica se ambos os argumentos são bases vectoriais
usando `abasep` e se esse for o caso, substitui o
valor correspondente da matriz `aform`.

<!-- category: Tensors -->
<!-- keywords: aform -->
<!-- signatures: aform -->
### Variable: aform

Valor por omissão para as formas bilineares `sf`, `af`, e
`av`.  O padrão é a matriz identidade `ident(3)`.

<!-- category: Tensors -->
<!-- keywords: alg_type -->
<!-- signatures: alg_type -->
### Function: alg_type

O tipo de álgebra.  Valores válidos sáo `universal`, `grassmann`,
`clifford`, `symmetric`, `symplectic` e `lie_envelop`.

<!-- category: Tensors -->
<!-- keywords: asymbol -->
<!-- signatures: asymbol -->
### Variable: asymbol

O símbolo para bases vectoriais.

<!-- category: Tensors -->
<!-- keywords: atensimp -->
<!-- signatures: atensimp(expr) -->
### Function: atensimp (expr)

Simplifica a expressão algébrica de tensores *expr* conforme as
regras configuradas por uma chamada a `init_atensor`.
Simplificações incluem aplicação
recursiva de relações comutativas e
resoluções de chamadas a `sf`, `af`, e
`av` onde for aplicável.  Uma salvaguarda é usada para garantir
que a função sempre termine, mesmo para expressões
complexas.

<!-- category: Tensors -->
<!-- keywords: av -->
<!-- signatures: av(u, v) -->
### Function: av (u, v)

É uma função antisimétrica que é usada em relações comutativas.
A implementação padrão verifica se ambos os argumentos são bases vectoriais
usando `abasep` e se esse for o caso, substitui o
valor correspondente da matriz `aform`.


Por exemplo:



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

Inicializa o pacote `atensor` com o tipo especificado de álgebra.  *alg_type*
pode ser um dos seguintes:


`universal`: A álgebra universal tendo regras não comutativas.


`grassmann`: A álgebra de Grassman é definida pela relação de 
comutação `u.v+v.u=0`.


`clifford`: A álgebra de Clifford é definida pela relação
de comutação `u.v+v.u=-2*sf(u,v)` onde `sf` é a função
valor-escalar simétrico.  Para essa álgebra, *opt_dims* pode ser acima de três 
inteiros não negativos, representando o número de dimensões positivas,
dimensões degeneradas, e dimensões negativas da álgebra, respectivamente.  Se
quaisquer valores *opt_dims* são fornecidos, `atensor` irá configurar os
valores de `adim` e `aform` apropriadamente.  Caso contrário,
`adim` irá por padrão para 0 e `aform` não será definida.


`symmetric`: A álgebra simétrica é definida pela relação de 
comutação `u.v-v.u=0`.


`symplectic`: A álgebra simplética é definida pela relação de 
comutação `u.v-v.u=2*af(u,v)` onde `af` é uma função valor-escalar 
antisimétrica.  Para a álgebra simplética, *opt_dims* pode
mais de dois inteiros não negativos, representando a dimensão não degenerada e
e a dimensão degenerada, respectivamente.  Se quaisquer valores *opt_dims* são
fornecidos, `atensor` irá configurar os valores de `adim` e `aform`
apropriadamente.  Caso contrário, `adim` irá por padrão para 0 e `aform`
não será definida.


`lie_envelop`: O invólucro da álgebra de Lie é definido pela 
relação de comutação `u.v-v.u=2*av(u,v)` onde `av` é
uma função antisimétrica.


A função `init_atensor` também reconhece muitos tipos pré-definidos de 
álgebra:


`complex` implementa a álgebra de números complexos como a
álgebra de Clifford Cl(0,1).  A chamada `init_atensor(complex)` é
equivalente a `init_atensor(clifford,0,0,1)`.


`quaternion` implementa a álgebra de quaterniões.  A chamada
`init_atensor(quaternion)` é equivalente a 
`init_atensor(clifford,0,0,2)`.


`pauli` implementa a álgebra de spinores de Pauli como a
álgebra de Clifford Cl(3,0).  Uma chamada a `init_atensor(pauli)`
é equivalente a `init_atensor(clifford,3)`.


`dirac` implementa a álgebra de spinores de Dirac como a
álgebra de Clifford Cl(3,1).  Uma chamada a `init_atensor(dirac)`
é equivalente a `init_atensor(clifford,3,0,1)`.

<!-- category: Tensors -->
<!-- keywords: sf -->
<!-- signatures: sf(u, v) -->
### Function: sf (u, v)

É uma função escalar simétrica que é usada em
relações comutativas.  A implementação
padrão verifica se ambos os argumentos são bases vectoriais usando
`abasep` e se esse for o caso, substitui o valor correspondente da
matriz `aform`.

