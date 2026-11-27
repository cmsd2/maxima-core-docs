## unit

<!-- category: Units -->
<!-- keywords: %unitexpand -->
<!-- signatures: %unitexpand -->
### Variable: %unitexpand

Valor por omissão: `2`


Ess é o valor fornecido a `metricexpandall` durante a inicialização
de *unit*.

<!-- category: Units -->
<!-- keywords: convert -->
<!-- signatures: convert(expr, list) -->
### Function: convert (expr, list)

Quando do restabelecimento dos valores padrão o ambiente global é destruído, existe o comando
`convert`, que permite conversões imediatas.  `convert` pode aceitar  um argumetno
simples ou uma lista de unidades a serem usadas na conversão.  Quando uma operação de conversão for
concluída, o sistema normal de avaliação global é contornado, com o objectivo de evitar que
o resultado desejado seja convertido novamente.  Como consequência, em cálculos aproximados
alertas de "rat" irão ser visíveis se o ambiente global que controla esse comportamento
(`ratprint`) for `true`.  `convert` também é útil para uma verificação pontual e imediata da
precisão de uma conversão global.  Outro recurso é que `convert` irá permitir a um
utilizador fazer um Base de Conversões Dimensionais mesmo se o ambiente global for escolhido para
simplificar par uma Dimensão Derivada.



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


Veja também `setunits` e `uforget`. Para usar essa função primeiramente escreva `load("unit")`.

<!-- category: Units -->
<!-- keywords: metricexpandall -->
<!-- signatures: metricexpandall(x) -->
### Function: metricexpandall (x)

Reconstrói listas de unidades globais automaticamente criando todas as unidades métricas desejadas.
*x* é um argumento numérico que é usado para especificar quantos prefixos
métricos o utilizador deseja que seja definido.  Os argumentos são os seguintes, com cada
maior número definindo todos os menores números de unidade:


```maxima
0 - none. Only base units
           1 - kilo, centi, milli
(default)  2 - giga, mega, kilo, hecto, deka, deci, centi, milli,
               micro, nano
           3 - peta, tera, giga, mega, kilo, hecto, deka, deci,
               centi, milli, micro, nano, pico, femto
           4 - all
```

Normalmente, Maxima não irá definir a expansão completa desses resultados em uma
grande número de unidades, mas `metricexpandall` pode ser usada para
reconstruir a lista em um estilo mais ou menos completo. A variável relevante
no ficheiro *unit.mac* é *%unitexpand*.

<!-- category: Units -->
<!-- keywords: setunits -->
<!-- signatures: setunits(list) -->
### Function: setunits (list)

Por padrão, o pacote *unit* não usa qualquer dimensões derivadas, mas irá
converter todas as unidades nas sete fundamentais do sistema MKS.


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


Em alguns casos esse é o comportamento desejado.  Se o utilizador desejar usar outras
unidades, isso é conseguido com o comando `setunits`:


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


A escolha de unidades é completamente flexível.  Por exemplo, se quisermos
voltar para quiilogramas, metros, e segundos como padrão para essas
dimensão nós podemos fazer:


```maxima
(%i11) setunits([kg,m,s]);
(%o11)                               done
(%i12) centigram*inch/minutes^2;
                                  127        kg m
(%o12)                      (-------------) (----)
                             1800000000000     2
                                              s
```


Unidade derivadas são também manuseáveis por meio desse comando:


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


Note que o pacote *unit* reconhece a combinação não MKS
de massa, comprimento, e tempo inverso elevado ao quadrado como uma força, e converte isso
para Newtons.  É dessa forma que Maxima trabalha geralmente.  Se, por exemplo, nós
preferirmos dinas em lugar de Newtons, simplesmente fazemos o seguinte:


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


Para descontinuar simplificando para qualquer unidade de força, usamos o comando `uforget`:


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

Isso pode trabalhar igualmente bem com `uforget(N)` ou
`uforget(%force)`.


Veja também `uforget`. Para usar essa função escreva primeiro `load("unit")`.

<!-- category: Units -->
<!-- keywords: uforget -->
<!-- signatures: uforget(list) -->
### Function: uforget (list)

Por padrão, o pacote *unit* converte todas as unidades para as
sete unidaes fundamentais do sitema MKS de unidades. Ess comportamento pode
ser mudado com o comando `setunits`. Após o qual, o
utilizador pode restabelecer o comportamento padrão para uma dimensão em particular
mediante o comando `uforget`:


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


`uforget` opera sobre dimensões,
não sobre unidades, de forma que qualquer unidade de uma dimensão em particular irá trabalhar.  A
própia dimensão é também um argumento legal.


Veja também `setunits`. To use this function write first `load("unit")`.

<!-- category: Units -->
<!-- keywords: usersetunits -->
<!-- signatures: usersetunits -->
### Variable: usersetunits

Valor por omissão: none


Se um utilizador desejar ter um comportamento padrão de unidade diferente daquele descrito,
ele pode fazer uso de *maxima-init.mac* e da variável
*usersetunits*.  O pacote *unit* irá verificar o ficheiro *maxima-init.mac* na inicialização para ver se a essa variável 
foi atribuído uma lista.  Se isso aconteceu, o pacote *unit* irá usar `setunits` sobre aquela lista e pegar 
as unidades lá colocadas para serem as padrões.  `uforget` irá reverter para o comportamento
definido por `usersetunits` sobrescrevendo seus próprios padrões.  Por exemplo, Se tivermos um ficheiro
*maxima-init.mac* contendo:


```maxima
usersetunits : [N,J];
```

nós poderemos ver o seguinte comportamento:


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
WARNING: DEFUN/DEFMACRO: redefining function TOPLEVEL-MACSYMA-EVAL ...
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

Sem `usersetunits`, as entradas iniciais poderiam ter sido convertidas
para o sistema de unidades MKS, e `uforget` poderia ter resultado em um retorno para as regras do MKS.  Em vez disso,
as preferências do utilizador foram respeitadas em ambos os casos.  Note que esse podem ainda
serem sobrescritos se for desejado.  Para eliminar completamente essa simplificação - i.e.
ter as preferências de utilizador escolhidas para os padrões de unidade do Maxima - o comando
`dontusedimension` pode ser usado.  `uforget` pode restabelecer as preferências de utilizador novamente, mas
somente se `usedimension` liberar isso para uso.  Alternativamente,
`kill(usersetunits)` irá remover completametne todo o conhecimento dessas escolhas de utilizador
da sessão actual.  Aqui está alguns exemplos de como esssas várias opções trabalham.


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
Done.  To have Maxima simplify to this dimension, use setunits([unit]) 
to select a unit. 
(%o20)                               true
(%i21) usedimension(J);
Done.  To have Maxima simplify to this dimension, use setunits([unit]) 
to select a unit. 
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

Desafortunadamente essa ampla variedade de opções é um pouco confus no início,
mas uma vez que o utilizador cultiva o uso delas o utilizador perceberá que elas permitem completo
controle sobre seu ambiente de trabalho.

