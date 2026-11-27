## itensor

<!-- category: Tensors -->
<!-- keywords: allsym -->
<!-- signatures: allsym -->
### Variable: allsym

Valor por omissão: `false`. Se `true` então todos os objectos indexados
são assumidos simétricos em todos os seus índices covariantes e
contravariantes. Se `false` então nenhum simétrico de qualquer tipo é assumidos
nesses índices. Índices derivativos são sempre tomados para serem simétricos
a menos que `iframe_flag` seja escolhida para `true`.

<!-- category: Tensors -->
<!-- keywords: canform -->
<!-- signatures: canform(expr) -->
### Function: canform (expr)

Simplifica *expr* através de mudança de nome de índices
que ocorrem exactamente duas vezes e reordenação de todos os índices como ditados pelas condições de simetria
impostas sobre eles. Se `allsym` for `true` então todos os índices são assumidos
simétricos, de outra forma a informação de simetria fornecida pelas declarações
`decsym` irão ser usadas. Os índices que ocorrem exactamente duas vezes são renomeados da mesma
maneira que na função `rename`. Quando `canform` é aplicada a uma expressão
larga o cálculo pode tomar um considerável montante de tempo.
Esse tempo pode ser diminuído através do uso de `rename` sobre a expressão em primeiro lugar.
Também veja o exemplo sob `decsym`. Nota: `canform` pode não estar apta a
reduzir um expressão completamente para sua forma mais simples embora
retorne sempre um resultado matemáticamente correcto.

<!-- category: Tensors -->
<!-- keywords: canten -->
<!-- signatures: canten(expr) -->
### Function: canten (expr)

Simplifica *expr* por renomeação (veja `rename`)
e permutando índices que ocorrem exactamente duas vezes. `rename` é restrito a adições de produto
de tensores nos quais nenhum índice derivativo estiver presente. Como tal isso é limitado
e pode somente ser usado se `canform` não for capaz de realizar a
simplificação requerida.


A função `canten` retorna um resultado matematicamente correcto somente
se seu argumento for uma expressão que é completamente simétrica em seus índices.
Por essa razão, `canten` retorna um erro se `allsym` não for
posicionada em `true`.

<!-- category: Tensors -->
<!-- keywords: changename -->
<!-- signatures: changename(antigo, novo, expr) -->
### Function: changename (antigo, novo, expr)

Irá mudar o nome de todos os objectos indexados chamados *antigo* para *novo*
em *expr*. *antigo* pode ser ou um símbolo ou uma lista da forma
`[nome, m, n]` nesse caso somente esses objectos indexados chamados
*nome* com índice covariante *m* e índice contravariante *n* serão
renomeados para *novo*.

<!-- category: Tensors -->
<!-- keywords: components -->
<!-- signatures: components(tensor, expr) -->
### Function: components (tensor, expr)

Permite que se atribua um valor indicial a uma expressão
*expr* dando os valores das componentes do *tensor*. Esses
são automaticamente substituídos para o tensor mesmo que isso ocorra com
todos os seus índices. O tensor deve ser da forma `t([...],[...])`
onde qualquer lista pode ser vazia. *expr* pode ser qualquer expressão indexada
envolvendo outros objectos com os mesmos índices livres que *tensor*. Quando
usada para atribuir valores a um tensor métrico no qual as componentes
possuem índices que ocorrem exactamente duas vezes se deve ser cuidadoso para definir esses índices de forma a
evitar a geração de índices que ocorrem exactamente duas vezes e que são múltiplos. a remoção dessas
atribuições é dada para a função `remcomps`.


É importante ter em mente que `components` cuida somente da
valência de um tensor, e que ignora completamente qualquer ordenação particular de índices. Dessa forma
atribuindo componentes a, digamos, `x([i,-j],[])`, `x([-j,i],[])`, ou
`x([i],[j])` todas essas atribuições produzem o mesmo resultado, a saber componentes sendo
atribuidas a um tensor chamado `x` com valência `(1,1)`.


Componentes podem ser atribuidas a uma expressão indexada por quatro caminhos, dois
dos quais envolvem o uso do comando `components`:


1) Como uma expressão indexada. Por exemplo:



```maxima
(%i2) components(g([],[i,j]),e([],[i])*p([],[j]))$
(%i3) ishow(g([],[i,j]))$
                                      i  j
(%t3)                                e  p
```


2) Como uma matriz:



```maxima
(%i6) components(g([i,j],[]),lg);
(%o6)                                done
(%i7) ishow(g([i,j],[]))$
(%t7)                                g
                                      i j
(%i8) g([3,3],[]);
(%o8)                                  1
(%i9) g([4,4],[]);
(%o9)                                 - 1
```


3) Como uma função. Pode usar uma função Maxima para especificar as
componentes de um tensor baseado nesses índices. Por exemplo, os seguintes
códigos atribuem `kdelta` a `h` se `h` tiver o mesmo número de
índices covariantes e índices contravariantes e nenhum índice derivativo, e
atribui `kdelta` a `g` caso as condições anteriores não sejam atendidas:



```maxima
(%i4) h(l1,l2,[l3]):=if length(l1)=length(l2) and length(l3)=0
  then kdelta(l1,l2) else apply(g,append([l1,l2], l3))$
(%i5) ishow(h([i],[j]))$
                                          j
(%t5)                               kdelta
                                          i
(%i6) ishow(h([i,j],[k],l))$
                                     k
(%t6)                               g
                                     i j,l
```


4) Usando a compatibilidade dos modelos de coincidência do Maxima, especificamente os
comandos `defrule` e `applyb1`:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) matchdeclare(l1,listp);
(%o2)                                done
(%i3) defrule(r1,m(l1,[]),(i1:idummy(),
      g([l1[1],l1[2]],[])*q([i1],[])*e([],[i1])))$

(%i4) defrule(r2,m([],l1),(i1:idummy(),
      w([],[l1[1],l1[2]])*e([i1],[])*q([],[i1])))$

(%i5) ishow(m([i,n],[])*m([],[i,m]))$
                                    i m
(%t5)                              m    m
                                         i n
(%i6) ishow(rename(applyb1(%,r1,r2)))$
                           %1  %2  %3 m
(%t6)                     e   q   w     q   e   g
                                         %1  %2  %3 n
```

<!-- category: Tensors -->
<!-- keywords: concan -->
<!-- signatures: concan(expr) -->
### Function: concan (expr)

Similar a `canten` mas também executa contração de índices.

<!-- category: Tensors -->
<!-- keywords: conmetderiv -->
<!-- signatures: conmetderiv(expr, tensor) -->
### Function: conmetderiv (expr, tensor)

Simplifica expressões contendo derivadas comuns de
ambas as formas covariantes e contravariantes do tensor métrico (a
restrição corrente).  Por exemplo, `conmetderiv` pode relatar a
derivada do tensor contravariante métrico com símbolos de
Christoffel como visto adiante:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(g([],[a,b],c))$
                                      a b
(%t2)                                g
                                      ,c
(%i3) ishow(conmetderiv(%,g))$
                         %1 b      a       %1 a      b
(%t3)                 - g     ichr2     - g     ichr2
                                   %1 c              %1 c
```

<!-- category: Tensors -->
<!-- keywords: contract -->
<!-- signatures: contract(expr) -->
### Function: contract (expr)

Realiza contrações tensoriais em *expr* a qual pode ser qualquer
combinação de adições e produtos. Essa função usa a informação
dada para a função `defcon`. Para melhores resultados, `expr`
pode ser completamente expandida. `ratexpand` é o meio mais rápido para expandir
produtos e expoentes de adições se não existirem variáveis nos denominadores
dos termos. O comutador `gcd` pode ser `false` se cancelamentos de
máximo divisor comum forem desnecessários.

<!-- category: Tensors -->
<!-- keywords: coord -->
<!-- signatures: coord(tensor_1, tensor_2, ...) -->
### Function: coord (tensor_1, tensor_2, ...)

Dados os *tensor_i* a propriedade de diferenciação da coordenada que a
derivada do vector contravariante cujo nome é um dos
*tensor_i* retorna um delta de Kronecker. Por exemplo, se `coord(x)` tiver
sido concluída então `idiff(x([],[i]),j)` fornece `kdelta([i],[j])`.
`coord` que é uma lista de todos os objectos indexados tendo essa propriedade.

<!-- category: Tensors -->
<!-- keywords: covdiff -->
<!-- signatures: covdiff(expr, v_1, v_2, ...) -->
### Function: covdiff (expr, v_1, v_2, ...)

Retorna a derivada da covariante de *expr* com
relação às variáveis *v_i* em termos de símbolos de Christoffel de
segundo tipo (`ichr2`).  Com o objectivo de avaliar esses, se pode usar
`ev(expr,ichr2)`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the índices covariantes: [i,j];
Enter a list of the índices contravariantes: [k];
Enter a list of the derivative indices: [];
                                      k
(%t2)                                a
                                      i j
(%i3) ishow(covdiff(%,s))$
             k         %1     k         %1     k            k     %1
(%t3)     - a     ichr2    - a     ichr2    + a      + ichr2     a
             i %1      j s    %1 j      i s    i j,s        %1 s  i j
(%i4) imetric:g;
(%o4)            g
(%i5) ishow(ev(%th(2),ichr2))$
  %1 %4  k
 g      a     (g       - g       + g  )
  i %1   s %4,j  j s,%4    j %4,s
(%t5) - ------------------------------------------
       2
    %1 %3  k
   g   a     (g       - g    + g     )
    %1 j   s %3,i    i s,%3    i %3,s
 - ------------------------------------------
         2
    k %2  %1
   g     a    (g        - g    + g      )
   i j   s %2,%1    %1 s,%2    %1 %2,s   k
 + ------------------------------------------- + a
   2     i j,s
(%i6)
```

<!-- category: Tensors -->
<!-- keywords: decsym -->
<!-- signatures: decsym(tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...]) -->
### Function: decsym (tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...])

Declara propriedades de simetria para *tensor* de covariante *m* e
*n* índices contravariantes. As *cov_i* e *contr_i* são
pseudofunções expressando relações de simetrias em meio a índices covariante e
índices contravariantes respectivamente.  Esses são da forma
`symoper(index_1, index_2,...)` onde `symoper` é um entre
`sym`, `anti` ou `cyc` e os *index_i* são inteiros
indicando a posição do índice no *tensor*.  Isso irá
declarar *tensor* para ser simétrico, antisimétrico ou cíclico respectivamente
nos *index_i*. `symoper(all)` é também forma permitida que
indica todos os índices obedecem à condição de simetria. Por exemplo, dado um
objecto `b` com 5 índices covariantes,
`decsym(b,5,3,[sym(1,2),anti(3,4)],[cyc(all)])` declara `b`
simétrico no seu primeiro e no seu segundo índices e antisimétrico no seu terceiro e
quarto índices covariantes, e cíclico em todos de seus índices contravariantes.
Qualquer lista de declarações de simetria pode ser nula.  A função que
executa as simplificações é `canform` como o exemplo abaixo
ilustra.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:contract(expand(a([i1,j1,k1],[])*kdels([i,j,k],[i1,j1,k1])))$
(%i3) ishow(expr)$
(%t3)         a      + a      + a      + a      + a      + a
               k j i    k i j    j k i    j i k    i k j    i j k
(%i4) decsym(a,3,0,[sym(all)],[]);
(%o4)                                done
(%i5) ishow(canform(expr))$
(%t5)                              6 a
                                      i j k
(%i6) remsym(a,3,0);
(%o6)                                done
(%i7) decsym(a,3,0,[anti(all)],[]);
(%o7)                                done
(%i8) ishow(canform(expr))$
(%t8)                                  0
(%i9) remsym(a,3,0);
(%o9)                                done
(%i10) decsym(a,3,0,[cyc(all)],[]);
(%o10)                               done
(%i11) ishow(canform(expr))$
(%t11)                        3 a      + 3 a
                                 i k j      i j k
(%i12) dispsym(a,3,0);
(%o12)                     [[cyc, [[1, 2, 3]], []]]
```

<!-- category: Tensors -->
<!-- keywords: defcon -->
<!-- signatures: defcon(tensor_1), defcon(tensor_1, tensor_2, tensor_3) -->
### Function: defcon (tensor_1)

Dado *tensor_1* a propriedade que a
contração de um produto do *tensor_1* e do *tensor_2* resulta em *tensor_3*
com os índices apropriados.  Se somente um argumento, *tensor_1*, for
dado, então a contração do produto de *tensor_1* com qualquer objecto
indexado tendo os índices apropriados (digamos `my_tensor`) irá retornar como resultado um
objecto indexado com aquele nome, i.e. `my_tensor`, e com uma nova escolha de
índices refletindo as contrações executadas.
Por exemplo, se `imetric:g`, então `defcon(g)` irá implementar o
incremento e decremento de índices através da contração com o tensor
métrico.
Mais de uma `defcon` pode ser dada para o mesmo objecto indexado; o
último  fornecido que for aplicado a uma contração particular será
usado.
`contractions` é uma lista de objectos indexados que tenham fornecido
propriedades de contrações com `defcon`.

<!-- category: Tensors -->
<!-- keywords: entertensor -->
<!-- signatures: entertensor(nome) -->
### Function: entertensor (nome)

É uma função que, através da linha de comando, permite criar um objecto
indexado chamado *nome* com qualquer número de índices de tensores e
derivativos. Ou um índice simples ou uma lista de índices (às quais podem ser
nulas) são entradas aceitáveis (veja o exemplo sob `covdiff`).

<!-- category: Tensors -->
<!-- keywords: evundiff -->
<!-- signatures: evundiff(expr) -->
### Function: evundiff (expr)

Equivalente à execução de `undiff`, seguida por `ev` e
`rediff`.


O ponto dessa operação é facilmente avaliar expressões que não possam
ser directamente avaliadas na forma derivada. Por exemplo, o seguinte
causa um erro:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) icurvature([i,j,k],[l],m);
Maxima encountered a Lisp error:

 Error in $ICURVATURE [or a callee]:
 $ICURVATURE [or a callee] requires less than three arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```


Todavia, se `icurvature` é informado em sua forma substantiva, pode ser avaliado
usando `evundiff`:



```maxima
(%i3) ishow('icurvature([i,j,k],[l],m))$
                                         l
(%t3)                          icurvature
                                         i j k,m
(%i4) ishow(evundiff(%))$
             l              l         %1           l           %1
(%t4) - ichr2        - ichr2     ichr2      - ichr2       ichr2
             i k,j m        %1 j      i k,m        %1 j,m      i k

                l              l         %1           l           %1
         + ichr2        + ichr2     ichr2      + ichr2       ichr2
                i j,k m        %1 k      i j,m        %1 k,m      i j
```


Nota: Em versões anteriores do Maxima, formas derivadas dos
símbolos de Christoffel também não podiam ser avaliadas. Isso foi corrigido actualmente,
de forma que `evundiff` não mais é necessária para expressões como essa:



```maxima
(%i5) imetric(g);
(%o5)                                done
(%i6) ishow(ichr2([i,j],[k],l))$
       k %3
      g     (g         - g         + g        )
              j %3,i l    i j,%3 l    i %3,j l
(%t6) -----------------------------------------
                          2

                         k %3
                        g     (g       - g       + g      )
                         ,l     j %3,i    i j,%3    i %3,j
                      + -----------------------------------
                                         2
```

<!-- category: Tensors -->
<!-- keywords: extdiff -->
<!-- signatures: extdiff(expr, i) -->
### Function: extdiff (expr, i)

Calcula a derivada externa de *expr* com relação ao índice
*i*. A derivada externa é formalmente definida como o produto
cunha do operador de derivada parcial e uma forma diferencial. Como
tal, essa operação é também controlada através da escolha de `igeowedge_flag`.
Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(extdiff(v([i]),j))$
                                  v    - v
                                   j,i    i,j
(%t2)                             -----------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(extdiff(a([i,j]),k))$
                           a      - a      + a
                            j k,i    i k,j    i j,k
(%t4)                      ------------------------
                                      3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(extdiff(v([i]),j))$
(%t6)                             v    - v
                                   j,i    i,j
(%i7) ishow(extdiff(a([i,j]),k))$
(%t7)                      a      - a      + a
                            j k,i    i k,j    i j,k
```

<!-- category: Tensors -->
<!-- keywords: flipflag -->
<!-- signatures: flipflag -->
### Variable: flipflag

Valor por omissão: `false`. Se `false` então os índices irão ser
renomeados conforme a ordem dos índices contravariantes,
de outra forma serão ordenados conforme a ordem dos índices covariantes.


Se `flipflag` for `false` então `rename` forma uma lista
de índices contravariantes na ordem em que forem encontrados da esquerda para a direita
(se `true` então de índices contravariantes). O primeiro índice
que ocorre exactamente duas vezes na lista é renomeado para `%1`, o seguinte para `%2`, etc.
Então a ordenação ocorre após a ocorrência do `rename` (veja o exemplo
sob `rename`).

<!-- category: Tensors -->
<!-- keywords: flush -->
<!-- signatures: flush(expr, tensor_1, tensor_2, ...) -->
### Function: flush (expr, tensor_1, tensor_2, ...)

Escolhe para zero, em
*expr*, todas as ocorrências de *tensor_i* que não tiverem índices derivativos.

<!-- category: Tensors -->
<!-- keywords: flush1deriv -->
<!-- signatures: flush1deriv(expr, tensor) -->
### Function: flush1deriv (expr, tensor)

Escolhe para zero, em `expr`, todas as ocorrências de `tensor` que possuem
exactamente um índice derivativo.

<!-- category: Tensors -->
<!-- keywords: flushd -->
<!-- signatures: flushd(expr, tensor_1, tensor_2, ...) -->
### Function: flushd (expr, tensor_1, tensor_2, ...)

Escolhe para zero, em
*expr*, todas as ocorrências de *tensor_i* que tiverem índices derivativos.

<!-- category: Tensors -->
<!-- keywords: flushnd -->
<!-- signatures: flushnd(expr, tensor, n) -->
### Function: flushnd (expr, tensor, n)

Escolhe para zero, em *expr*, todas as
ocorrências do objecto diferenciado *tensor* que tem *n* ou mais
índices derivativos como demonstra o seguinte exemplo.


```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i],[J,r],k,r)+a([i],[j,r,s],k,r,s))$
                                J r      j r s
(%t2)                          a      + a
                                i,k r    i,k r s
(%i3) ishow(flushnd(%,a,3))$
                                     J r
(%t3)                               a
                                     i,k r
```

<!-- category: Tensors -->
<!-- keywords: hodge -->
<!-- signatures: hodge(expr) -->
### Function: hodge (expr)

Calcula o Hodge dual de *expr*. Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                            done
(%i3) idim(4);
(%o3)                            done
(%i4) icounter:100;
(%o4)                             100
(%i5) decsym(A,3,0,[anti(all)],[])$

(%i6) ishow(A([i,j,k],[]))$
(%t6)                           A
                                 i j k
(%i7) ishow(canform(hodge(%)))$
                          %1 %2 %3 %4
               levi_civita            g        A
                                       %1 %102  %2 %3 %4
(%t7)          -----------------------------------------
                                   6
(%i8) ishow(canform(hodge(%)))$
                 %1 %2 %3 %8            %4 %5 %6 %7
(%t8) levi_civita            levi_civita            g        g
                                                     %1 %106  %2 %107
                                            g        g      A        /6
                                             %3 %108  %4 %8  %5 %6 %7
(%i9) lc2kdt(%)$

(%i10) %,kdelta$

(%i11) ishow(canform(contract(expand(%))))$
(%t11)                     - A
                              %106 %107 %108
```

<!-- category: Tensors -->
<!-- keywords: ic_convert -->
<!-- signatures: ic_convert(eqn) -->
### Function: ic_convert (eqn)

Converte a equação *eqn* na sintaxe `itensor` para uma declaração de atribuição `ctensor`.
Adições implícitas sobre índices que ocorrem exactamente duas vezes são tornadas explícitas enquanto objectos
indexados são transformados em arrays (os arrays subscritos estão na
ordem de covariância seguidos de índices contravariantes dos objectos
indexados). A derivada de um objecto indexado será substituída pela
forma substantiva de `diff` tomada com relação a `ct_coords` subscrita
pelo índice de derivação. Os símbolos de Christoffel `ichr1` e `ichr2`
irão ser traduzidos para `lcs` e `mcs`, respectivamente e se
`metricconvert` for `true` então todas as ocorrências da métrica
com dois índices covariantes (ou contravariantes) irão ser renomeadas para `lg`
(ou `ug`). Adicionalmente, ciclos `do` irão ser introduzidos adicionando sobre
todos os índices livres de forma que a
declaração de atribuição transformada pode ser avaliada através de apenas fazendo
`ev`. Os seguintes exemplos demonstam os recursos dessa
função.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) eqn:ishow(t([i,j],[k])=f([],[])*g([l,m],[])*a([],[m],j)*b([i],[l,k]))$
                             k        m   l k
(%t2)                       t    = f a   b    g
                             i j      ,j  i    l m
(%i3) ic_convert(eqn);
(%o3) for i thru dim do (for j thru dim 

do (for k thru dim do t        : f sum(sum(diff(a , ct_coords ) b
                       i, j, k                   m           j   i, l, k

 g    , l, 1, dim), m, 1, dim)))
  l, m
(%i4) imetric(g);
(%o4)                                done
(%i5) metricconvert:true;
(%o5)                                true
(%i6) ic_convert(eqn);
(%o6) for i thru dim do (for j thru dim 

do (for k thru dim do t        : f sum(sum(diff(a , ct_coords ) b
                       i, j, k                   m           j   i, l, k

 lg    , l, 1, dim), m, 1, dim)))
   l, m
```

<!-- category: Tensors -->
<!-- keywords: icc1 -->
<!-- signatures: icc1 -->
### Variable: icc1

Coeficientes de conecção de primeiro tipo. Em `itensor`, definido como



```maxima
icc1    = ichr1    - ikt1    - inmc1
    abc        abc       abc        abc
```


Nessa expressão, se `iframe_flag` for `true`, o símbolo de Christoffel
`ichr1` é substituído com o coeficiente de conecção do referencial `ifc1`.
Se `itorsion_flag` for `false`, `ikt1`
será omitido. `ikt1` é também omitido se uma base de referencial for usada, como a
torsão está já calculada como parte do suporte do referencial.
Ultimamente, como `inonmet_flag` é `false`,
`inmc1` não estará presente.

<!-- category: Tensors -->
<!-- keywords: icc2 -->
<!-- signatures: icc2 -->
### Variable: icc2

Coeficientes de conecção de segundo tipo. Em `itensor`, definido como



```maxima
c         c        c         c
icc2   = ichr2   - ikt2   - inmc2
    ab        ab       ab        ab
```


Nessa expressão, se `iframe_flag` for `true`, o símbolo de Christoffel
`ichr2` é substituído com o coeficiente de conecção `ifc2`.
Se `itorsion_flag` for `false`, `ikt2`
será omitido. `ikt2` também será omitido se uma base de referencial for usada, uma vez que a
torsão já está calculada como parte do suporte do referencial.
Ultimamente, como `inonmet_flag` é `false`,
`inmc2` não estará presente.

<!-- category: Tensors -->
<!-- keywords: ichr1 -->
<!-- signatures: ichr1([i, j, k]) -->
### Function: ichr1 ([i, j, k])

Retorna o símbolo de Christoffel de primeiro tipo via
definição


```maxima
(g      + g      - g     )/2 .
         ik,j     jk,i     ij,k
```


Para avaliar os símbolos de Christoffel para uma métrica particular, à
variável `imetric` deve ser atribuída um nome como no exemplo sob `chr2`.

<!-- category: Tensors -->
<!-- keywords: ichr2 -->
<!-- signatures: ichr2([i, j], [k]) -->
### Function: ichr2 ([i, j], [k])

Retorna o símbolo de Christoffel de segundo tipo
definido pela relação


```maxima
ks
   ichr2([i,j],[k]) = g    (g      + g      - g     )/2
                             is,j     js,i     ij,s
```

<!-- category: Tensors -->
<!-- keywords: icounter -->
<!-- signatures: icounter -->
### Variable: icounter

Valor por omissão: `1`


Determina o sufixo numérico a ser usado na
geração do próximo índice que ocorre exactamente duas vezes no pacote tensor.  O prefixo é
determinado através da opção `idummy` (padrão: `%`).

<!-- category: Tensors -->
<!-- keywords: icurvature -->
<!-- signatures: icurvature([i, j, k], [h]) -->
### Function: icurvature ([i, j, k], [h])

Retorna o tensor da curvatura de
Riemann em termos de símbolos de Christoffel de segundo
tipo (`ichr2`).  A seguinte notação é usada:


```maxima
h             h            h         %1         h
     icurvature     = - ichr2      - ichr2     ichr2    + ichr2
               i j k         i k,j        %1 j      i k        i j,k
                               h          %1
                        + ichr2      ichr2
                               %1 k       i j
```

<!-- category: Tensors -->
<!-- keywords: idiff -->
<!-- signatures: idiff(expr, v_1, [n_1, [v_2, n_2]...]) -->
### Function: idiff (expr, v_1, [n_1, [v_2, n_2]...])

Diferenciação indicial. A menos que `diff`, que diferencia
com relação a uma variável independente, `idiff` possa ser usada
para diferenciar com relação a uma coordenada. Para um objecto indexado,
isso equivale a anexar ao final os *v_i* como índices derivativos.
Subsequêntemente, índices derivativos irão ser ordenados, a menos que `iframe_flag`
seja escolhida para `true`.


`idiff` pode também ser o determinante de um tensor
métrico. Dessa forma, se `imetric` tiver sido associada a `G` então
`idiff(determinant(g),k)` irá retornar
`2*determinant(g)*ichr2([%i,k],[%i])` onde o índice que ocorre exactamente duas vezes `%i`
é escolhido apropriadamente.

<!-- category: Tensors -->
<!-- keywords: idim -->
<!-- signatures: idim(n) -->
### Function: idim (n)

Escolhe as dimensões da métrica. Também inicializa as propriedades de
antisimetria dos símbolos de Levi-Civita para as dimensões dadas.

<!-- category: Tensors -->
<!-- keywords: idummy -->
<!-- signatures: idummy() -->
### Function: idummy ()

Incrementos `icounter` e retorno como seu valor um índice da forma
`%n` onde n é um inteiro positivo.  Isso garante que índices que ocorrem exactamente duas vezes
e que são necessários na formação de expressões não irão conflitar com índices
que já estiverem sendo usados (veja o exemplo sob `indices`).

<!-- category: Tensors -->
<!-- keywords: idummyx -->
<!-- signatures: idummyx -->
### Variable: idummyx

Valor por omissão: `%`


É o prefixo para índices que ocorrem exactamente duas vezes (veja o exemplo sob índices `indices`).

<!-- category: Tensors -->
<!-- keywords: ifb -->
<!-- signatures: ifb -->
### Variable: ifb

O suporte do referencial. A contribuição da métrica do referencial para os coeficientes
de conecção é expressa usando o suporte do referencial:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                  2
```


O suporte do referencial por si mesmo é definido em termos de campo de
referencial e métrica do referencial. Dois métodos alternativos de
cálculo são usados dependendo do valor de
`frame_bracket_form`. Se `true` (o padrão) ou se o
sinalizador `itorsion_flag` for `true`:



```maxima
d      e                                      f
ifb =  ifr    ifr   (ifri      - ifri      - ifri    itr   )
   abc    b      c       a d,e       a e,d       a f    d e
```


Otherwise:



```maxima
e      d        d      e
ifb    = (ifr    ifr    - ifr    ifr   ) ifri
   abc       b      c,e      b,e    c        a d
```

<!-- category: Tensors -->
<!-- keywords: ifc1 -->
<!-- signatures: ifc1 -->
### Variable: ifc1

Coeficiente de referencial de primeiro tipo (também conhecido como coeficientes de
rotação de Ricci).  Esse tensor representa a contribuição
da métrica do referencial para o coeficiente de conecção de primeiro tipo. Definido
como:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                   2
```

<!-- category: Tensors -->
<!-- keywords: ifc2 -->
<!-- signatures: ifc2 -->
### Variable: ifc2

Coeficiente de referencial de primeiro tipo. Esse tensor representa a contribuição
da métrica do referencial para o coeficiente de conecção de primeiro tipo. Definido
como uma permutação de suporte de referencial (`ifb`) com os índices
apropriados incrementados e decrementados como necessário:



```maxima
c       cd
ifc2   = ifg   ifc1
    ab             abd
```

<!-- category: Tensors -->
<!-- keywords: ifg -->
<!-- signatures: ifg -->
### Variable: ifg

A métrica do referencial. O valor padrão é `kdelta`, mas pode ser mudada usando
`components`.

<!-- category: Tensors -->
<!-- keywords: ifgi -->
<!-- signatures: ifgi -->
### Variable: ifgi

O inverso da métrica do referencial. Contrai com a métrica do referencial (`ifg`)
para `kdelta`.

<!-- category: Tensors -->
<!-- keywords: ifr -->
<!-- signatures: ifr -->
### Variable: ifr

O campo do referencial. Contrai (`ifri`) para e com a forma do
campo inverso do referencial para formar a métrica do referencial
(`ifg`).

<!-- category: Tensors -->
<!-- keywords: iframe_bracket_form -->
<!-- signatures: iframe_bracket_form -->
### Variable: iframe_bracket_form

Valor por omissão: `true`


Especifica como o suporte do referencial (`ifb`) é calculado.

<!-- category: Tensors -->
<!-- keywords: iframes -->
<!-- signatures: iframes() -->
### Function: iframes ()

Uma vez que nessa versão do Maxima, identidades de contração para `ifr` e
`ifri` são sempre definidas, como é o suporte do referencial (`ifb`), essa
função não faz nada.

<!-- category: Tensors -->
<!-- keywords: ifri -->
<!-- signatures: ifri -->
### Variable: ifri

O campo inverso do referencial. Especifica a base do referencial (vectores base duais). Juntamente
com a métrica do referencial, forma a base de todos os cálculos baseados em
referenciais.

<!-- category: Tensors -->
<!-- keywords: igeodesic_coords -->
<!-- signatures: igeodesic_coords(expr, nome) -->
### Function: igeodesic_coords (expr, nome)

Faz com que símbolos de Christoffel não diferenciados e
a primeira derivada do tensor métrico tendam para zero em *expr*. O *nome*
na função `igeodesic_coords` refere-se à métrica *nome*
(se isso aparecer em *expr*) enquando os coeficientes de conecção devem ser
chamados com os nomes `ichr1` e/ou `ichr2`. O seguinte exemplo
demonstra a verificação da identidade cíclica satisfeita através do tensor da
curvatura de Riemann usando a função `igeodesic_coords`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(icurvature([r,s,t],[u]))$
             u            u         %1         u            u         %1
(%t2) - ichr2      - ichr2     ichr2    + ichr2      + ichr2     ichr2
             r t,s        %1 s      r t        r s,t        %1 t      r s
(%i3) ishow(igeodesic_coords(%,ichr2))$
                                 u            u
(%t3)                       ichr2      - ichr2
                                 r s,t        r t,s
(%i4) ishow(igeodesic_coords(icurvature([r,s,t],[u]),ichr2)+
            igeodesic_coords(icurvature([s,t,r],[u]),ichr2)+
            igeodesic_coords(icurvature([t,r,s],[u]),ichr2))$
             u            u            u            u            u
(%t4) - ichr2      + ichr2      + ichr2      - ichr2      - ichr2
             t s,r        t r,s        s t,r        s r,t        r t,s

                                                                  u
                                                           + ichr2
                                                                  r s,t
(%i5) canform(%);
(%o5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: igeowedge_flag -->
<!-- signatures: igeowedge_flag -->
### Variable: igeowedge_flag

Valor por omissão: `false`


Controla o comportamento de produto cunha e derivada externa. Quando
for esconhida para `false` (o padrão), a noção de formas diferenciais irá
corresponder àquela de um campo tensor covariante totalmente antisimétrico.
Quando escolhida para `true`, formas diferenciais irão concordar com a noção do
elemento volume.

<!-- category: Tensors -->
<!-- keywords: ikt1 -->
<!-- signatures: ikt1 -->
### Variable: ikt1

Permutação covariante do tensor de torsão (também conhecido como contorsão).
Definido como:



```maxima
d           d       d
          -g   itr  - g    itr   - itr   g
            ad    cb    bd    ca      ab  cd
ikt1    = ----------------------------------
    abc                   2
```


(Substitue `ifg` em lugar de `g` se um referencial métrico for usada.)

<!-- category: Tensors -->
<!-- keywords: ikt2 -->
<!-- signatures: ikt2 -->
### Variable: ikt2

Permutação contravariante do tensor de torsão (também conhecida como contorsão).
Definida como:



```maxima
c     cd
ikt2   = g   ikt1
    ab           abd
```


(Substitue `ifg` em lugar de `g` se um referencial métrico for usada.)

<!-- category: Tensors -->
<!-- keywords: imetric -->
<!-- signatures: imetric(g) -->
### Function: imetric (g)

Especifica a métrica através de atribuição à variável `imetric:g`
adicionalmente, as propriedades de contração da métrica *g* são escolhidas através da
execução dos comandos `defcon(g),defcon(g,g,kdelta)`.
A variável `imetric` (desassociada por padrão), é associada à métrica, atribuida pelo
comando `imetric(g)`.

<!-- category: Tensors -->
<!-- keywords: indexed_tensor -->
<!-- signatures: indexed_tensor(tensor) -->
### Function: indexed_tensor (tensor)

Deve ser executada antes de atribuir componentes para um *tensor* para o qual
um valor interno já existe como com `ichr1`, `ichr2`,
`icurvature`. Veja o exemplo sob `icurvature`.

<!-- category: Tensors -->
<!-- keywords: indices -->
<!-- signatures: indices(expr) -->
### Function: indices (expr)

Retorna uma lista de dois elementos.  O primeiro é uma lista de índices
livres em *expr* (aqueles que ocorrem somente uma vez). O segundo é uma
lista de indices que ocorrem exactamente duas vezes em *expr* (dummy)
como demonstra o seguinte exemplo.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i,j],[k,l],m,n)*b([k,o],[j,m,p],q,r))$
                                k l      j m p
(%t2)                          a        b
                                i j,m n  k o,q r
(%i3) indices(%);
(%o3)                 [[l, p, i, n, o, q, r], [k, j, m]]
```


Um produto de tensores contendo o mesmo índice mais que duas vezes é sintaticamente
ilegal. `indices` tenta lidar com essas expressões de uma
forma razoável; todavia, quando `indices` é chamada para operar sobre tal uma
expressão ilegal, seu comportamento pode ser considerado indefinido.

<!-- category: Tensors -->
<!-- keywords: inm -->
<!-- signatures: inm -->
### Variable: inm

O vector de não metricidade. Conforme a não metricidade está definida através da
derivada covariante do tensor métrico. Normalmente zero, o tensor da
métrica derivada covariante irá avaliar para o seguinte quando
`inonmet_flag` for escolhido para `true`:



```maxima
g     =- g  inm
 ij;k     ij  k
```

<!-- category: Tensors -->
<!-- keywords: inmc1 -->
<!-- signatures: inmc1 -->
### Variable: inmc1

Permutação covariante de componentes do vector de não metricidade. Definida como



```maxima
g   inm  - inm  g   - g   inm
            ab    c      a  bc    ac    b
inmc1    = ------------------------------
     abc                 2
```


(Substitue `ifg` em lugar de `g` se um referencial métrico for usada.)

<!-- category: Tensors -->
<!-- keywords: inmc2 -->
<!-- signatures: inmc2 -->
### Variable: inmc2

Permutação covariante de componentes do vector de não metricidade. Usada
nos coeficicientes de conecção se `inonmet_flag` for `true`. Definida
como:



```maxima
c         c         cd
          -inm  kdelta  - kdelta  inm  + g   inm  g
     c        a       b         a    b          d  ab
inmc2   = -------------------------------------------
     ab                        2
```


(Substitue `ifg` em lugar de `g` se um referencial métrico for usada.)

<!-- category: Tensors -->
<!-- keywords: ishow -->
<!-- signatures: ishow(expr) -->
### Function: ishow (expr)

Mostra *expr* com os objectos indexados tendo seus
índices covariantes como subscritos e índices contravariantes como
sobrescritos.  Os índices derivativos são mostrados como subscritos,
separados dos índices covariantes por uma vírgula (veja os exemplos
através desse documento).

<!-- category: Tensors -->
<!-- keywords: itr -->
<!-- signatures: itr -->
### Variable: itr

O tensor de torsão. Para uma métrica com torsão, diferenciação covariante
repetida sobre uma funçào escalar não irá comutar,como demonstrado
através do seguinte exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric:g;
(%o2)                                  g
(%i3) covdiff(covdiff(f([],[]),i),j)-covdiff(covdiff(f([],[]),j),i)$
(%i4) ishow(%)$
                                   %4              %2
(%t4)                    f    ichr2    - f    ichr2
                          ,%4      j i    ,%2      i j
(%i5) canform(%);
(%o5)                                  0
(%i6) itorsion_flag:true;
(%o6)                                true
(%i7) covdiff(covdiff(f([],[]),i),j)-covdiff(covdiff(f([],[]),j),i)$
(%i8) ishow(%)$
                           %8             %6
(%t8)             f    icc2    - f    icc2    - f     + f
                   ,%8     j i    ,%6     i j    ,j i    ,i j
(%i9) ishow(canform(%))$
                                   %1             %1
(%t9)                     f    icc2    - f    icc2
                           ,%1     j i    ,%1     i j
(%i10) ishow(canform(ev(%,icc2)))$
                                   %1             %1
(%t10)                    f    ikt2    - f    ikt2
                           ,%1     i j    ,%1     j i
(%i11) ishow(canform(ev(%,ikt2)))$
                      %2 %1                    %2 %1
(%t11)          f    g      ikt1       - f    g      ikt1
                 ,%2            i j %1    ,%2            j i %1
(%i12) ishow(factor(canform(rename(expand(ev(%,ikt1))))))$
                           %3 %2            %1       %1
                     f    g      g      (itr    - itr   )
                      ,%3         %2 %1     j i      i j
(%t12)               ------------------------------------
                                      2
(%i13) decsym(itr,2,1,[anti(all)],[]);
(%o13)                               done
(%i14) defcon(g,g,kdelta);
(%o14)                               done
(%i15) subst(g,nounify(g),%th(3))$
(%i16) ishow(canform(contract(%)))$
                                           %1
(%t16)                           - f    itr
                                    ,%1    i j
```

<!-- category: Tensors -->
<!-- keywords: kdels -->
<!-- signatures: kdels(L1, L2) -->
### Function: kdels (L1, L2)

Delta de Kronecker simetrizado, usado em alguns cálculos. Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) kdelta([1,2],[2,1]);
(%o2)                                 - 1
(%i3) kdels([1,2],[2,1]);
(%o3)                                  1
(%i4) ishow(kdelta([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  - kdelta  kdelta
                             a       b         a       b
(%i4) ishow(kdels([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  + kdelta  kdelta
                             a       b         a       b
```

<!-- category: Tensors -->
<!-- keywords: kdelta -->
<!-- signatures: kdelta(L1, L2) -->
### Function: kdelta (L1, L2)

é a função delta generalizada de Kronecker definida no
pacote `itensor` com *L1* a lista de índices covariantes e *L2*
a lista de índices contravariantes.  `kdelta([i],[j])` retorna o delta de
Kronecker comum.  O comando `ev(expr,kdelta)` faz com que a avaliação de
uma expressão contendo `kdelta([],[])` se dê para a dimensão de
multiplicação.


No que conduzir a um abuso dessa notação, `itensor` também permite
`kdelta` ter 2 covariantes e nenhum contravariante, ou 2 contravariantes
e nenhum índice covariante, com efeito fornecendo uma compatibilidade para "matriz unitária" covariante ou
contravariante. Isso é estritamente considerado um recurso de programação e não significa
implicar que `kdelta([i,j],[])` seja um objecto tensorial válido.

<!-- category: Tensors -->
<!-- keywords: lc2kdt -->
<!-- signatures: lc2kdt(expr) -->
### Function: lc2kdt (expr)

Simplifica expressões contendo os símbolos de Levi-Civita, convertendo esses
para expressões delta de Kronecker quando possível. A principal diferença entre
essa função e simplesmente avaliar os simbolos de Levi-Civita é que a avaliação
directa muitas vezes resulta em expressões Kronecker contendo índices
numéricos. Isso é muitas vezes indesejável como na prevenção de simplificação adicional.
A função `lc2kdt` evita esse problema, retornando expressões que
são mais facilmente simplificadas com `rename` ou `contract`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:ishow('levi_civita([],[i,j])*'levi_civita([k,l],[])*a([j],[k]))$
                                  i j  k
(%t2)                  levi_civita    a  levi_civita
                                       j            k l
(%i3) ishow(ev(expr,levi_civita))$
                                  i j  k       1 2
(%t3)                       kdelta    a  kdelta
                                  1 2  j       k l
(%i4) ishow(ev(%,kdelta))$
             i       j         j       i   k
(%t4) (kdelta  kdelta  - kdelta  kdelta ) a
             1       2         1       2   j

                               1       2         2       1
                        (kdelta  kdelta  - kdelta  kdelta )
                               k       l         k       l
(%i5) ishow(lc2kdt(expr))$
                     k       i       j    k       j       i
(%t5)               a  kdelta  kdelta  - a  kdelta  kdelta
                     j       k       l    j       k       l
(%i6) ishow(contract(expand(%)))$
                                 i           i
(%t6)                           a  - a kdelta
                                 l           l
```


A função `lc2kdt` algumas vezes faz uso de tensores métricos.
Se o tensor métrico não tiver sido definido previamente com `imetric`,
isso resulta em um erro.



```maxima
(%i7) expr:ishow('levi_civita([],[i,j])*'levi_civita([],[k,l])*a([j,k],[]))$
                                 i j            k l
(%t7)                 levi_civita    levi_civita    a
                                                     j k
(%i8) ishow(lc2kdt(expr))$
Maxima encountered a Lisp error:

 Error in $IMETRIC [or a callee]:
 $IMETRIC [or a callee] requires less than two arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i9) imetric(g);
(%o9)                                done
(%i10) ishow(lc2kdt(expr))$
         %3 i       k   %4 j       l     %3 i       l   %4 j       k
(%t10) (g     kdelta   g     kdelta   - g     kdelta   g     kdelta  ) a
                    %3             %4               %3             %4   j k
(%i11) ishow(contract(expand(%)))$
                                  l i      l i
(%t11)                           a    - a g
```

<!-- category: Tensors -->
<!-- keywords: lc_l -->
<!-- signatures: lc_l -->
### Function: lc_l

Regra de simplificação usada para expressões contendo símbolos não avaliados de
Levi-Civita (`levi_civita`). Juntamente com `lc_u`, pode ser usada para simplificar
muitas expressões mais eficientemente que a avaliação de `levi_civita`.
Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2)  el1:ishow('levi_civita([i,j,k],[])*a([],[i])*a([],[j]))$
                             i  j
(%t2)                       a  a  levi_civita
                                             i j k
(%i3) el2:ishow('levi_civita([],[i,j,k])*a([i])*a([j]))$
                                       i j k
(%t3)                       levi_civita      a  a
                                              i  j
(%i4) ishow(canform(contract(expand(applyb1(el1,lc_l,lc_u)))))$
(%t4)                                  0
(%i5) ishow(canform(contract(expand(applyb1(el2,lc_l,lc_u)))))$
(%t5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: lc_u -->
<!-- signatures: lc_u -->
### Function: lc_u

Regra de simplificação usada para expressões contendo símbolos não avaliados de
Levi-Civita (`levi_civita`). Juntamente com `lc_u`, pode ser usada para simplificar
muitas expressões mais eficientemente que a avaliação de `levi_civita`.
Para detalhes, veja `lc_l`.

<!-- category: Tensors -->
<!-- keywords: levi_civita -->
<!-- signatures: levi_civita(L) -->
### Function: levi_civita (L)

é o tensor de permutação (ou de Levi-Civita) que retorna 1 se
a lista *L* consistir de uma permutação par de inteiros, -1 se isso
consistir de uma permutação ímpar, e 0 se alguns índices em *L* forem
repetidos.

<!-- category: Tensors -->
<!-- keywords: liediff -->
<!-- signatures: liediff(v, ten) -->
### Function: liediff (v, ten)

Calcula a derivada de Lie da expressão tensorial *ten* com
relação ao campo vectorial *v*. *ten* pode ser qualquer expressão tensorial
indexada; *v* pode ser o nome (sem índices) de um campo
vectorial. Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(liediff(v,a([i,j],[])*b([],[k],l)))$
       k    %2            %2          %2
(%t2) b   (v   a       + v   a     + v   a    )
       ,l       i j,%2    ,j  i %2    ,i  %2 j

                                %1  k        %1  k      %1  k
                            + (v   b      - b   v    + v   b   ) a
                                    ,%1 l    ,l  ,%1    ,l  ,%1   i j
```

<!-- category: Tensors -->
<!-- keywords: listoftens -->
<!-- signatures: listoftens -->
### Function: listoftens

Lista todos os tensores em uma expressão tensorial, incluindo seus índices. E.g.,



```maxima
(%i6) ishow(a([i,j],[k])*b([u],[],v)+c([x,y],[])*d([],[])*e)$
                                         k
(%t6)                        d e c    + a    b
                                  x y    i j  u,v
(%i7) ishow(listoftens(%))$
                               k
(%t7)                        [a   , b   , c   , d]
                               i j   u,v   x y
```

<!-- category: Tensors -->
<!-- keywords: lorentz_gauge -->
<!-- signatures: lorentz_gauge(expr) -->
### Function: lorentz_gauge (expr)

Impõe a condição de Lorentz através da substituição de 0 para todos os
objectos indexados em *expr* que possui um índice de derivada idêntico ao
índice contravariante.

<!-- category: Tensors -->
<!-- keywords: makebox -->
<!-- signatures: makebox(expr) -->
### Function: makebox (expr)

Mostra *expr* da mesma maneira que `show`; todavia,
qualquer tensor d’Alembertiano ocorrendo em *expr* será indicado usando o
símbolo `[]`.  Por exemplo, `[]p([m],[n])` representa
`g([],[i,j])*p([m],[n],i,j)`.

<!-- category: Tensors -->
<!-- keywords: rediff -->
<!-- signatures: rediff(ten) -->
### Function: rediff (ten)

Avalia todas as ocorrências do comando `idiff` na expressão
tensorial *ten*.

<!-- category: Tensors -->
<!-- keywords: remcomps -->
<!-- signatures: remcomps(tensor) -->
### Function: remcomps (tensor)

Desassocia todos os valores de *tensor* que foram atribuídos com a
função `components`.

<!-- category: Tensors -->
<!-- keywords: remcon -->
<!-- signatures: remcon(tensor_1, ..., tensor_n), remcon(all) -->
### Function: remcon (tensor_1, ..., tensor_n)

Remove todas as propriedades de contração
de *tensor_1*, ..., *tensor_n*). `remcon(all)` remove todas as propriedades de
contração de todos os objectos indexados.

<!-- category: Tensors -->
<!-- keywords: remcoord -->
<!-- signatures: remcoord(tensor_1, tensor_2, ...), remcoord(all) -->
### Function: remcoord (tensor_1, tensor_2, ...)

Remove a propriedade de coordenada de diferenciação dos `tensor_i`
que foram estabelecidos através da função `coord`.  `remcoord(all)`
remove essa propriedade de todos os objectos indexados.

<!-- category: Tensors -->
<!-- keywords: remsym -->
<!-- signatures: remsym(tensor, m, n) -->
### Function: remsym (tensor, m, n)

Remove todas as propriedades de simetria de *tensor* que tem *m*
índices covariantes e *n* índices contravariantes.

<!-- category: Tensors -->
<!-- keywords: rename -->
<!-- signatures: rename(expr), rename(expr, contador) -->
### Function: rename (expr)

Retorna uma expressão equivalente para *expr* mas com índices que ocorrem exactamente duas vezes
em cada termo alterado do conjunto `[%1, %2,...]`, se o segundo argumento
opcional for omitido. De outra forma, os índices que ocorrem exactamente duas vezes são indexados
começando no valor de *contador*.  Cada índice que ocorre exactamente duas vezes em um produto
será diferente. Para uma adição, `rename` irá operar sobre cada termo na
a adição zerando o contador com cada termo. Nesse caminho `rename` pode
servir como um simplificador tensorial. Adicionalmente, os índices serão
ordenados alfanumericamente (se `allsym` for `true`) com relação a
índices covariantes ou contravariantes dependendo do valor de `flipflag`.
Se `flipflag` for `false` então os índices serão renomeados conforme
a ordem dos índices contravariantes. Se `flipflag` for `true`
a renomeação ocorrerá conforme a ordem dos índices
covariantes. Isso muitas vezes ajuda que o efeito combinado dos dois restantes sejam
reduzidos a uma expressão de valor um ou mais que um por si mesma.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) allsym:true;
(%o2)                                true
(%i3) g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%4],[%3])*
ichr2([%2,%3],[u])*ichr2([%5,%6],[%1])*ichr2([%7,r],[%2])-
g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%2],[u])*
ichr2([%3,%5],[%1])*ichr2([%4,%6],[%3])*ichr2([%7,r],[%2]),noeval$
(%i4) expr:ishow(%)$

       %4 %5  %6 %7      %3         u          %1         %2
(%t4) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %4      %2 %3      %5 %6      %7 r

              %4 %5  %6 %7      u          %1         %3         %2
           - g      g      ichr2      ichr2      ichr2      ichr2
                                %1 %2      %3 %5      %4 %6      %7 r
(%i5) flipflag:true;
(%o5)                                true
(%i6) ishow(rename(expr))$
       %2 %5  %6 %7      %4         u          %1         %3
(%t6) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %2      %3 %4      %5 %6      %7 r

              %4 %5  %6 %7      u          %1         %3         %2
           - g      g      ichr2      ichr2      ichr2      ichr2
                                %1 %2      %3 %4      %5 %6      %7 r
(%i7) flipflag:false;
(%o7)                                false
(%i8) rename(%th(2));
(%o8)                                  0
(%i9) ishow(rename(expr))$
       %1 %2  %3 %4      %5         %6         %7        u
(%t9) g      g      ichr2      ichr2      ichr2     ichr2
                         %1 %6      %2 %3      %4 r      %5 %7

              %1 %2  %3 %4      %6         %5         %7        u
           - g      g      ichr2      ichr2      ichr2     ichr2
                                %1 %3      %2 %6      %4 r      %5 %7
```

<!-- category: Tensors -->
<!-- keywords: showcomps -->
<!-- signatures: showcomps(tensor) -->
### Function: showcomps (tensor)

Mostra atribuições de componentes de um tensor, feitas usando o comando
`components`. Essa função pode ser particularmente útil quando uma matriz é atribuída
a um tensor indicial usando `components`, como demonstrado através do
seguinte exemplo:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) load("itensor");
(%o2)      /share/tensor/itensor.lisp
(%i3) lg:matrix([sqrt(r/(r-2*m)),0,0,0],[0,r,0,0],
                [0,0,sin(theta)*r,0],[0,0,0,sqrt((r-2*m)/r)]);
               [         r                                     ]
               [ sqrt(-------)  0       0              0       ]
               [      r - 2 m                                  ]
               [                                               ]
               [       0        r       0              0       ]
(%o3)          [                                               ]
               [       0        0  r sin(theta)        0       ]
               [                                               ]
               [                                      r - 2 m  ]
               [       0        0       0        sqrt(-------) ]
               [                                         r     ]
(%i4) components(g([i,j],[]),lg);
(%o4)                                done
(%i5) showcomps(g([i,j],[]));
                  [         r                                     ]
                  [ sqrt(-------)  0       0              0       ]
                  [      r - 2 m                                  ]
                  [                                               ]
                  [       0        r       0              0       ]
(%t5)      g    = [                                               ]
            i j   [       0        0  r sin(theta)        0       ]
                  [                                               ]
                  [                                      r - 2 m  ]
                  [       0        0       0        sqrt(-------) ]
                  [                                         r     ]
(%o5)                                false
```


O comando `showcomps` pode também mostrar componentes de um tensor de
categoria maior que 2.

<!-- category: Tensors -->
<!-- keywords: simpmetderiv -->
<!-- signatures: simpmetderiv(expr), simpmetderiv(expr[, stop]) -->
### Function: simpmetderiv (expr)

Simplifica expressões contendo produtos de derivadas de
tensores métricos. Especificamente, `simpmetderiv` reconhece duas identidades:



```maxima
ab        ab           ab                 a
  g   g   + g   g     = (g   g  )   = (kdelta )   = 0
   ,d  bc        bc,d         bc ,d          c ,d
```


consequêntemente



```maxima
ab          ab
  g   g   = - g   g
   ,d  bc          bc,d
```


e



```maxima
ab          ab
 g   g     = g   g
  ,j  ab,i    ,i  ab,j
```


que seguem de simetrias de símbolos de Christoffel.


A função `simpmetderiv` toma um parâmetro opcional que, quando
presente, faz com que a função pare após a primeira substituição feita com
sucesso em uma expressão produto. A função `simpmetderiv`
também faz uso da variável global *flipflag* que determina
como aplicar uma ordenação “canonica” para os índices de produto.


Colocados juntos, essas compatibilidades podem ser usadas poderosamente para encontrar
simplificações que são difíceis ou impossíveis de realizar de outra forma.
Isso é demonstrado através do seguinte exemplo que explicitamente usa o 
recurso de simplificação parcial de `simpmetderiv` para obter uma
expressão contractível:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                                done
(%i3) ishow(g([],[a,b])*g([],[b,c])*g([a,b],[],d)*g([b,c],[],e))$
                             a b  b c
(%t3)                       g    g    g      g
                                       a b,d  b c,e
(%i4) ishow(canform(%))$

errexp1 has improper indices
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) ishow(simpmetderiv(%))$
                             a b  b c
(%t5)                       g    g    g      g
                                       a b,d  b c,e
(%i6) flipflag:not flipflag;
(%o6)                                true
(%i7) ishow(simpmetderiv(%th(2)))$
                               a b  b c
(%t7)                         g    g    g    g
                               ,d   ,e   a b  b c
(%i8) flipflag:not flipflag;
(%o8)                                false
(%i9) ishow(simpmetderiv(%th(2),stop))$
                               a b  b c
(%t9)                       - g    g    g      g
                                    ,e   a b,d  b c
(%i10) ishow(contract(%))$
                                    b c
(%t10)                           - g    g
                                    ,e   c b,d
```


Veja também `weyl.dem` para um exemplo que usa `simpmetderiv`
e `conmetderiv` juntos para simplificar contrações do tensor de Weyl.

<!-- category: Tensors -->
<!-- keywords: tentex -->
<!-- signatures: tentex(expr) -->
### Function: tentex (expr)

Para usar a função `tentex`, deve primeiro chamar `tentex`,
como no seguinte exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) load("tentex");
(%o2)       /share/tensor/tentex.lisp
(%i3) idummyx:m;
(%o3)                                  m
(%i4) ishow(icurvature([j,k,l],[i]))$
            m1       i           m1       i           i            i
(%t4)  ichr2    ichr2     - ichr2    ichr2     - ichr2      + ichr2
            j k      m1 l        j l      m1 k        j l,k        j k,l
(%i5) tentex(%)$
$$\Gamma_{j\,k}^{m_1}\,\Gamma_{l\,m_1}^{i}-\Gamma_{j\,l}^{m_1}\,
 \Gamma_{k\,m_1}^{i}-\Gamma_{j\,l,k}^{i}+\Gamma_{j\,k,l}^{i}$$
```


Note o uso da declaração `idummyx`, para evitar o aparecimento
do sinal de porcentagem na expressão TeX, o qual pode induzir a erros de compilação.


Note Bem: Essa vesão da função `tentex` é um tanto quanto experimental.

<!-- category: Tensors -->
<!-- keywords: undiff -->
<!-- signatures: undiff(expr) -->
### Function: undiff (expr)

Retorna uma expressão equivalente a *expr* mas com todas as derivadas
de objectos indexados substituídas pela forma substantiva da função `idiff`. Seu
argumento pode retornar aquele objecto indexado se a diferenciação for
concluída.  Isso é útil quando for desejado substituir um
objecto indexado que sofreu diferenciação com alguma definição de função resultando
em *expr* e então concluir a diferenciação através de digamos
`ev(expr, idiff)`.

<!-- category: Tensors -->
<!-- keywords: | -->
<!-- signatures: | -->
### Variable: |

A barra vertical `|` denota a operação binária
"contração com um vector". Quando um tensor covariante totalmente antisimétrico é contraído
com um vector contravariante, o resultado é o mesmo independente de qual índice
foi usado para a contração. Dessa forma, é possível definir a
operação de contração de uma forma livre de índices.


No pacote `itensor`, contração com um vector é sempre realizada
com relação ao primeiro índice na ordem literal de ordenação. Isso garante
uma melhor simplificação de expressões envolvendo o operador `|`. Por exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) decsym(a,2,0,[anti(all)],[]);
(%o2)                                done
(%i3) ishow(a([i,j],[])|v)$
                                    %1
(%t3)                              v   a
                                        %1 j
(%i4) ishow(a([j,i],[])|v)$
                                     %1
(%t4)                             - v   a
                                         %1 j
```


Note que isso é essencial que os tensores usado como o operador `|` seja
declarado totalmente antisimétrico em seus índices covariantes. De outra forma,
os resultados serão incorrectos.

<!-- category: Tensors -->
<!-- keywords: ~ -->
<!-- signatures: ~ -->
### Variable: ~

O operador do produto cunha é definido como sendo o acento til `~`. O til é
um operador binário. Seus argumentos podem ser expressões envolvendo escalares,
tensores covariantes de categoria 1, ou tensores covariantes de categoria `l` que
tiverem sido declarados antisimétricos em todos os índices covariantes.


O comportamento do operador do produto cunha é controlado através do
sinalizador `igeowedge_flag`, como no seguinte exemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i])~b([j]))$
                                 a  b  - b  a
                                  i  j    i  j
(%t2)                            -------------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(a([i,j])~b([k]))$
                          a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
(%t4)                     ---------------------------
                                       3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(a([i])~b([j]))$
(%t6)                            a  b  - b  a
                                  i  j    i  j
(%i7) ishow(a([i,j])~b([k]))$
(%t7)                     a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
```

