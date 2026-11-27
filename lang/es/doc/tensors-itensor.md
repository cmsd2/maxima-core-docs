## itensor

<!-- category: Tensors -->
<!-- keywords: allsym -->
<!-- signatures: allsym -->
### Variable: allsym

Valor por defecto: `false`


Si vale `true` entonces todos los objetos indexados se consideran simétricos respecto de todos sus índices covariantes y contravariantes. Si vale `false` entonces no se tienen en cuenta ningún tipo de simetría para estos índices. Los índices de derivadas se consideran siempre simétricos, a menos que la variable `iframe_flag` valga `true`.

<!-- category: Tensors -->
<!-- keywords: canform -->
<!-- signatures: canform(expr), canform(expr, rename) -->
### Function: canform (expr)

Simplifica *expr* renombrando índices mudos y reordenando todos los índices según las condiciones de simetría que se le hayan impuesto. Si `allsym` vale `true` entonces todos los índices se consideran simétricos, en otro caso se utilizará la información sobre simetrías suministrada por `decsym`. Los índices mudos se renombran de la misma manera que en la función `rename`. Cuando `canform` se aplica a una expresión grande el cálculo puede llevar mucho tiempo. Este tiempo se puede acortar llamando primero  a `rename`.
Véase también el ejemplo de la descripción de `decsym`. La función `canform` puede que no reduzca completamente una expresión a su forma más sencilla, pero en todo caso devolverá un resultado matemáticamente correcto.


Si al parámetro opcional *rename* se le asigna el valor `false`, no se renombrarán los índices mudos.

<!-- category: Tensors -->
<!-- keywords: canten -->
<!-- signatures: canten(expr) -->
### Function: canten (expr)

Simplifica *expr* renombrando (véase `rename`) y permutando índices mudos. La función `rename` se restringe a sumas de productos de tensores en los cuales no hay derivadas, por lo que está limitada y sólo debería utilizarse si `canform` no es capaz de de llevar a cabo la simplificación requerida.


La función `canten` devuelve un resultado matemáticamente correcto sólo si su argumento es una expresión completamente simétrica respecto de sus índices. Por esta razón, `canten` devuelve un error si `allsym` no vale `true`.

<!-- category: Tensors -->
<!-- keywords: changename -->
<!-- signatures: changename(anterior, nuevo, expr) -->
### Function: changename (anterior, nuevo, expr)

Cambia el nombre de todos los objetos indexados llamados *anterior* a *new* en *expr*. El argumento *anterior* puede ser un símbolo o una lista de la forma `[nombre, m, n]`, en cuyo caso sólo los objetos indexados de llamados *nombre* con *m* índices covariantes y *n* contravariantes se renombrarán como *nuevo*.

<!-- category: Tensors -->
<!-- keywords: components -->
<!-- signatures: components(tensor, expr) -->
### Function: components (tensor, expr)

Permite asignar un valor indexado a la expresión *expr* dando los valores de las componentes de *tensor*. El tensor debe ser de la forma `t([...],[...])`, donde cualquiera de las listas puede estar vacía. La expresión  *expr* puede ser cualquier objeto indexado que tenga otros objetos con los mismos índices libres que *tensor*. Cuando se utiliza para asignar valores al tensor métrico en el que las componentes contengan índices mudos, se debe tener cuidado en no generar índices mudos múltiples. Se pueden borrar estas asignaciones con la función  `remcomps`.


Es importante tener en cuenta que `components` controla la valencia del tensor, no el orden de los índices. Así, asignando componentes de la forma `x([i,-j],[])`, `x([-j,i],[])` o `x([i],[j])` todos ellos producen el mismo resultado, la asignación de componentes a un tensor de nombre `x` con valencia `(1,1)`.


Las componentes se pueden asignar a una expresión indexada de cuatro maneras, dos de las cuales implican el uso de la instrucción `components`:


1) Como una expresión indexada. Por ejemplo:



```maxima
(%i2) components(g([],[i,j]),e([],[i])*p([],[j]))$
(%i3) ishow(g([],[i,j]))$
                                      i  j
(%t3)                                e  p
```


2) Como una matriz:



```maxima
(%i5) lg:-ident(4)$lg[1,1]:1$lg;
                            [ 1   0    0    0  ]
                            [                  ]
                            [ 0  - 1   0    0  ]
(%o5)                       [                  ]
                            [ 0   0   - 1   0  ]
                            [                  ]
                            [ 0   0    0   - 1 ]

(%i6) components(g([i,j],[]),lg);
(%o6)                                done
(%i7) ishow(g([i,j],[]))$
(%t7)                                g
                                      i j
(%i8) g([1,1],[]);
(%o8)                                  1
(%i9) g([4,4],[]);
(%o9)                                 - 1
```


3) Como una función. Se puede utilizar una función de Maxima para especificar las componentes de un tensor en base a sus índices. Por ejemplo, el código siguiente asigna  `kdelta` a `h` si `h` tiene el mismo número de índices covariantes y contravariantes y no tiene índices de derivadas, asignándole `g` en otro caso:



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


4) Utilizando los patrones de Maxima, en particular las funciones `defrule` y `applyb1`:



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

Similar a `canten` pero también realiza la contracción de los índices.

<!-- category: Tensors -->
<!-- keywords: conmetderiv -->
<!-- signatures: conmetderiv(expr, tensor) -->
### Function: conmetderiv (expr, tensor)

Simplifica expresiones que contengan derivadas ordinarias tanto de las formas covariantes como contravariantes del tensor métrico. Por ejemplo,  `conmetderiv` puede relacionar la derivada del tensor métrico contravariante con los símbolos de Christoffel, como se ve en el ejemplo:



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

Lleva a cabo las contracciones tensoriales en *expr*, la cual puede ser cualquier combinación de sumas y productos. Esta función utiliza la información dada a la función `defcon`. Para obtener mejores resultados, `expr`
debería estar completamente expandida. La función `ratexpand` es la forma más rápida de expandir productos y potencias de sumas si no hay variables en los denominadores de los términos.

<!-- category: Tensors -->
<!-- keywords: coord -->
<!-- signatures: coord(tensor_1, tensor_2, ...) -->
### Function: coord (tensor_1, tensor_2, ...)

Le da a *tensor_i* la propiedad de diferenciación coordenada, que la derivada del vector contravariante cuyo nombre es uno de los *tensor_i* es igual a la delta de Kronecker.  Por ejemplo, si se ha hecho `coord(x)` entonces  `idiff(x([],[i]),j)` da `kdelta([i],[j])`. La llamada `coord` devuelve una lista de todos los objetos indexados con esta propiedad.

<!-- category: Tensors -->
<!-- keywords: covdiff -->
<!-- signatures: covdiff(expr, v_1, v_2, ...) -->
### Function: covdiff (expr, v_1, v_2, ...)

Devuelve la derivada covariante de *expr* respecto de las variables  *v_i* en términos de los símbolos de Christoffel de segunda especie (`ichr2`). Para evaluarlos debe hacerse `ev(expr,ichr2)`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the covariant indices: [i,j];
Enter a list of the contravariant indices: [k];
Enter a list of the derivative indices: [];
                                      k
(%t2)                                a
                                      i j
(%i3) ishow(covdiff(%,s))$
             k         %1     k         %1     k
(%t3)     - a     ichr2    - a     ichr2    + a
             i %1      j s    %1 j      i s    i j,s

             k     %1
      + ichr2     a
             %1 s  i j
(%i4) imetric:g;
(%o4)                                  g
(%i5) ishow(ev(%th(2),ichr2))$
         %1 %4  k
        g      a     (g       - g       + g      )
                i %1   s %4,j    j s,%4    j %4,s
(%t5) - ------------------------------------------
                            2
    %1 %3  k
   g      a     (g       - g       + g      )
           %1 j   s %3,i    i s,%3    i %3,s
 - ------------------------------------------
                       2
    k %2  %1
   g     a    (g        - g        + g       )
          i j   s %2,%1    %1 s,%2    %1 %2,s     k
 + ------------------------------------------- + a
                        2                         i j,s
```

<!-- category: Tensors -->
<!-- keywords: decsym -->
<!-- signatures: decsym(tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...]) -->
### Function: decsym (tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...])

Declara propiedades de simetría para el *tensor* de *m* índices covariantes y *n* contravariantes. Los *cov_i* y *contr_i* son seudofunciones que expresan relaciones de simetría entre los índices covariantes y contravariantes, respectivamente. Éstos son de la forma `symoper(index_1, index_2,...)` donde `symoper` es uno de `sym`, `anti` o `cyc` y los *index_i* son enteros que indican la posición del índice en el *tensor*.  Esto declarará a *tensor* simétrico, antisimétrico o cíclico respecto de *index_i*. La llamada `symoper(all)` indica que todos los índices cumplen la condición de simetría. Por ejemplo, dado un objeto `b` con 5 índices covariantes, `decsym(b,5,3,[sym(1,2),anti(3,4)],[cyc(all)])` declara `b` simétrico en el primer y segundo índices covariantes, antisimétrico en su tercer y cuarto índices también covariantes y cíclico en todos sus índices contravariantes. Cualquiera de las listas de declaración de simetrías puede ser nula. La función que realiza las simplificaciones es `canform`, como se ilustra en el siguiente ejemplo,



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:contract(expand(a([i1,j1,k1],[])
            *kdels([i,j,k],[i1,j1,k1])))$
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

Le asigna a gives *tensor_1* la propiedad de que la contracción de un producto de *tensor_1* por *tensor_2* da como resultado un *tensor_3* con los índices apropiados. Si sólo se aporta un argumento, *tensor_1*, entonces la contracción del producto de *tensor_1* por cualquier otro objeto indexado que tenga los índices apropiados, por ejemplo `my_tensor`, dará como resultado un objeto indexado con ese nombre, `my_tensor`, y con un nuevo conjunto de índices que reflejen las contracciones realizadas. Por ejemplo, si `imetric:g`, entonces `defcon(g)` implementará el aumento o disminución de los índices a través de la contracción con el tensor métrico. Se puede dar más de un `defcon` para el mismo objeto indexado, aplicándose el último. La variable 
`contractions` es una lista con aquellos objetos indexados a los que se le han dado propiedades de contracción con  `defcon`.

<!-- category: Tensors -->
<!-- keywords: dispcon -->
<!-- signatures: dispcon(tensor_1, tensor_2, ...), dispcon(all) -->
### Function: dispcon (tensor_1, tensor_2, ...)

Muestra las propiedades contractivas de sus argumentos tal como 
fueron asignadas por `defcon`. La llamada `dispcon (all)`
muestra todas propiedades contractivas que fueron definidas.

<!-- category: Tensors -->
<!-- keywords: entertensor -->
<!-- signatures: entertensor(nombre) -->
### Function: entertensor (nombre)

Permite crear un objeto indexado llamado *nombre*, con cualquier número de índices tensoriales y de derivadas. Se admiten desde un único índice hasta una lista de índices. Véase el ejemplo en la descripción de `covdiff`.

<!-- category: Tensors -->
<!-- keywords: evundiff -->
<!-- signatures: evundiff(expr) -->
### Function: evundiff (expr)

Equivale a `undiff` seguido de  `ev` y `rediff`.


La razón de esta operación es evaluar de forma sencilla expresiones que no pueden ser directamente evaluadas en su forma derivada. Por ejemplo, lo siguiente provoca un error:



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


Sin embargo, si `icurvature` se da en forma nominal, puede ser evaluada utilizando `evundiff`:



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


Nota: en versiones antiguas de Maxima, las formas derivadas de los símbolos de
Christoffel no se podían evaluar. Este fallo ha sido subsanado, de manera que
`evundiff` ya no se necesita en expresiones como esta:



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

Calcula la derivada exterior de *expr* con respecto del índice *i*. La derivada exterior se define formalmente como el producto exterior del operador de la derivada parcial y una forma diferencial. Por lo tanto, esta operación también se ve afectada por el valor que tome la variable `igeowedge_flag`. Ejemplo:



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
(%t7)                    - (a      - a      + a     )
                             k j,i    k i,j    j i,k
```

<!-- category: Tensors -->
<!-- keywords: flipflag -->
<!-- signatures: flipflag -->
### Variable: flipflag

Valor por defecto: `false`


Si vale `false` los índices se renombrarán de acuerdo con el orden de los índices covariantes, si `true` se renombrarán de acuerdo con el orden de los índices covariantes.


Si `flipflag` vale `false`, entonces `rename` construye una lista con los índices contravariantes según van apareciendo de izquierda a derecha; si vale `true`, entonces va formando la lista con los covariantes. Al primer índice mudo se le da el nombre `%1`, al siguiente `%2`, etc. Finalmente se hace la ordenación. Véase el ejemplo en la descripción de la función `rename`.

<!-- category: Tensors -->
<!-- keywords: flush -->
<!-- signatures: flush(expr, tensor_1, tensor_2, ...) -->
### Function: flush (expr, tensor_1, tensor_2, ...)

Iguala a cero en la expresión *expr* todas las apariciones de *tensor_i* que no tengan índices de derivadas.

<!-- category: Tensors -->
<!-- keywords: flush1deriv -->
<!-- signatures: flush1deriv(expr, tensor) -->
### Function: flush1deriv (expr, tensor)

Iguala a cero en `expr` todas las apariciones de `tensor` que tengan exactamente un índice derivado.

<!-- category: Tensors -->
<!-- keywords: flushd -->
<!-- signatures: flushd(expr, tensor_1, tensor_2, ...) -->
### Function: flushd (expr, tensor_1, tensor_2, ...)

Iguala a cero en la expresión *expr* todas las apariciones de *tensor_i* que tengan índices de derivadas

<!-- category: Tensors -->
<!-- keywords: flushnd -->
<!-- signatures: flushnd(expr, tensor, n) -->
### Function: flushnd (expr, tensor, n)

Iguala a cero en *expr* todas las apariciones del objeto diferenciado  *tensor* que tenga *n* o más
índices de derivadas, como demuestra el siguiente ejemplo:



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

Calcula el dual de Hodge  *expr*. Por ejemplo:



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
(%t8) levi_civita            levi_civita            g       
                                                     %1 %106
                             g        g        g      A         /6
                              %2 %107  %3 %108  %4 %8  %5 %6 %7
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

Convierte la ecuación *eqn* del entorno `itensor` a una sentencia de asignación de `ctensor`. Sumas implícitas sobre índices mudos se hacen explícitas mientras que objetos indexados se transforman en arreglos (los subíndices de los arreglos se ordenan poniendo primero los covariantes seguidos de los contravariantes. La derivada de un objeto indexado se reemplazará por por la forma nominal de `diff` tomada con respecto a `ct_coords` con el subíndice correspondiente al índice derivado. Los símbolos de Christoffel `ichr1`  `ichr2` se traducen a `lcs` y `mcs`, respectivamente. Además, se añaden bucles `do` para la sumación de todos los índices libres, de manera que la sentencia traducida pueda ser evaluada haciendo simplemente `ev`. Los siguientes ejemplos muestran las funcionalidades de esta función.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) eqn:ishow(t([i,j],[k])=f([],[])*g([l,m],[])*a([],[m],j)
      *b([i],[l,k]))$
                             k        m   l k
(%t2)                       t    = f a   b    g
                             i j      ,j  i    l m
(%i3) ic_convert(eqn);
(%o3) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 g    , l, 1, dim), m, 1, dim)))
  l, m
(%i4) imetric(g);
(%o4)                                done
(%i5) metricconvert:true;
(%o5)                                true
(%i6) ic_convert(eqn);
(%o6) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 lg    , l, 1, dim), m, 1, dim)))
   l, m
```

<!-- category: Tensors -->
<!-- keywords: icc1 -->
<!-- signatures: icc1 -->
### Variable: icc1

Coeficientes de conexión de primera especie. Se definen en `itensor` como



```maxima
icc1    = ichr1    - ikt1    - inmc1
    abc        abc       abc        abc
```


En esta expresión, si `iframe_flag` vale `true`, el símbolo de Christoffel `ichr1` se reemplaza por el coeficiente de conexión del sistema de referencia `ifc1`. Si `itorsion_flag` vale `false`, `ikt1` será omitido. También se omite si se utiliza una base, ya que la torsión ya está calculada como parte del sistema de referencia.

<!-- category: Tensors -->
<!-- keywords: icc2 -->
<!-- signatures: icc2 -->
### Variable: icc2

Coeficientes de conexión de segunda especie. Se definen en `itensor` como



```maxima
c         c        c         c
icc2   = ichr2   - ikt2   - inmc2
    ab        ab       ab        ab
```


En esta expresión, si la variable `iframe_flag` vale `true`, el símbolo de Christoffel `ichr2` se reemplaza por el coeficiente de conexión del sistema de referencia `ifc2`. Si `itorsion_flag` vale `false`, `ikt2` se omite. También se omite si se utiliza una base de referncia. Por último, si  `inonmet_flag` vale `false`, se omite `inmc2`.

<!-- category: Tensors -->
<!-- keywords: ichr1 -->
<!-- signatures: ichr1([i, j, k]) -->
### Function: ichr1 ([i, j, k])

Devuelve el símbolo de Christoffel de primera especie dado por la definición 


```maxima
(g      + g      - g     )/2 .
         ik,j     jk,i     ij,k
```


Para evaluar los símbolos de Christoffel de una métrica determinada, a la variable  `imetric` hay que asignarle un nombre como en el ejemplo de la descripción de `chr2`.

<!-- category: Tensors -->
<!-- keywords: ichr2 -->
<!-- signatures: ichr2([i, j], [k]) -->
### Function: ichr2 ([i, j], [k])

Devuelve el símbolo de Christoffel de segunda especie dado por la definición


```maxima
ks
   ichr2([i,j],[k]) = g    (g      + g      - g     )/2
                             is,j     js,i     ij,s
```

<!-- category: Tensors -->
<!-- keywords: icounter -->
<!-- signatures: icounter -->
### Variable: icounter

Valor por defecto: `1`


Determina el sufijo numérico a ser utilizado en la generación del siguiente índice mudo. El prefijo se determina con la opción `idummy` (por defecto: %).

<!-- category: Tensors -->
<!-- keywords: icurvature -->
<!-- signatures: icurvature([i, j, k], [h]) -->
### Function: icurvature ([i, j, k], [h])

Devuelve el tensor de curvatura de Riemann en términos de los símbolos de Christoffel de segunda especie (`ichr2`).  Se utiliza la siguiente notación:


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

Diferenciación inicial. Al contrario que `diff`, que deriva respecto de una variable independiente, `idiff` puede usarse para derivar respecto de una coordenada. 


La función `idiff` también puede derivar el determinante del tensor métrico. Así, si `imetric` toma el valor `G` entonces `idiff(determinant(g),k)` devolverá `2*determinant(g)*ichr2([%i,k],[%i])` donde la índice mudo `%i` se escoge de forma apropiada.

<!-- category: Tensors -->
<!-- keywords: idim -->
<!-- signatures: idim(n) -->
### Function: idim (n)

Establece las dimensiones de la métrica. También inicializa las propiedades de antisimetría de los símbolos de Levi-Civita para la dimensión dada.

<!-- category: Tensors -->
<!-- keywords: idummy -->
<!-- signatures: idummy() -->
### Function: idummy ()

Incrementa `icounter` y devuelve un índice de la forma `%n` siendo `n` un entero positivo.  Esto garantiza que índices mudos que sean necesarios para formar expresiones no entren en conflico con índices que ya están en uso. Véase el ejemplo de la descripción de `indices`.

<!-- category: Tensors -->
<!-- keywords: idummyx -->
<!-- signatures: idummyx -->
### Variable: idummyx

Valor por defecto: `%`


Es el prefijo de los índices mudos. Véase `indices`.

<!-- category: Tensors -->
<!-- keywords: ifb -->
<!-- signatures: ifb -->
### Variable: ifb

Es el sistema de referencia soporte. La contribución de la métrica del campo a los coeficientes de conexión se expresa utilizando:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                  2
```


El sistema de referencia soporte se define en términos del campo y la métrica del sistema de referencia. Se utilizan dos métodos alternativos dependiendo del valor de `frame_bracket_form`. Si vale `true` (que es el valor por defecto) o si `itorsion_flag` vale `true`:



```maxima
d      e                                      f
ifb =  ifr    ifr   (ifri      - ifri      - ifri    itr   )
   abc    b      c       a d,e       a e,d       a f    d e
```


En otro caso:



```maxima
e      d        d      e
ifb    = (ifr    ifr    - ifr    ifr   ) ifri
   abc       b      c,e      b,e    c        a d
```

<!-- category: Tensors -->
<!-- keywords: ifc1 -->
<!-- signatures: ifc1 -->
### Variable: ifc1

Coeficiente del sistema de referencia de primera especie, también conocido como coeficientes de rotación de Ricci. Este tensor represnta la contribución de la métrica del sistema de referencia al coeficiente de conexión de primera especie, definido como



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

Coeficiente del sistema de referencia de segunda especie. Este tensor representa
la contribución de la métrica del sistema de referencia al coeficiente 
de conexión de segunda especie, definido como



```maxima
c       cd
ifc2   = ifg   ifc1
    ab             abd
```

<!-- category: Tensors -->
<!-- keywords: ifg -->
<!-- signatures: ifg -->
### Variable: ifg

La métrica del sistema de referencia. Su valor por defecto es `kdelta`, pero puede cambiarse utilizando 
`components`.

<!-- category: Tensors -->
<!-- keywords: ifgi -->
<!-- signatures: ifgi -->
### Variable: ifgi

La métrica inversa del sistema de referencia. Se contrae con la métrica `ifg` para dar `kdelta`.

<!-- category: Tensors -->
<!-- keywords: ifr -->
<!-- signatures: ifr -->
### Variable: ifr

El campo del sistema de referencia. Se contrae con el campo inverso `ifri` para formar la métrica del sistema de referencia, `ifg`.

<!-- category: Tensors -->
<!-- keywords: iframe_bracket_form -->
<!-- signatures: iframe_bracket_form -->
### Variable: iframe_bracket_form

Valor por defecto: `true`


Especifica cómo se calcula `ifb`.

<!-- category: Tensors -->
<!-- keywords: ifri -->
<!-- signatures: ifri -->
### Variable: ifri

Campo inverso del sistema de referencia. Especifica la base del sistema de referencia (vectores de la base dual).

<!-- category: Tensors -->
<!-- keywords: igeodesic_coords -->
<!-- signatures: igeodesic_coords(expr, nombre) -->
### Function: igeodesic_coords (expr, nombre)

Elimina los símbolos no diferenciados de Christoffel y las primeras derivadas del tensor métrico de *expr*. El argumento *nombre* de la función `igeodesic_coords` se refiere a la métrica *nombre* si aparece en *expr*, mientras que los coeficientes de conexión deben tener los nombres  `ichr1` y/o `ichr2`. El siguiente ejemplo hace la verificación de la identidad cíclica satisfecha por el tensor de curvatura de Riemann haciendo uso de la función `igeodesic_coords`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(icurvature([r,s,t],[u]))$
             u            u         %1         u     
(%t2) - ichr2      - ichr2     ichr2    + ichr2      
             r t,s        %1 s      r t        r s,t 

                                              u         %1
                                       + ichr2     ichr2
                                              %1 t      r s
(%i3) ishow(igeodesic_coords(%,ichr2))$
                                 u            u
(%t3)                       ichr2      - ichr2
                                 r s,t        r t,s
(%i4) ishow(igeodesic_coords(icurvature([r,s,t],[u]),ichr2)+
            igeodesic_coords(icurvature([s,t,r],[u]),ichr2)+
            igeodesic_coords(icurvature([t,r,s],[u]),ichr2))$
             u            u            u            u
(%t4) - ichr2      + ichr2      + ichr2      - ichr2
             t s,r        t r,s        s t,r        s r,t

                                             u            u
                                      - ichr2      + ichr2
                                             r t,s        r s,t
(%i5) canform(%);
(%o5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: igeowedge_flag -->
<!-- signatures: igeowedge_flag -->
### Variable: igeowedge_flag

Valor por defecto: `false`


Controla el comportamiento del producto exterior y de la derivada exterior. Cuando vale `false`, la noción de formas diferenciales se corresponde con el de campo tensorial covariante totalmente antisimétrico. Cuando vale `true`, las formas diferenciales se corresponden con la idea de elemento de volumen.

<!-- category: Tensors -->
<!-- keywords: ikt1 -->
<!-- signatures: ikt1 -->
### Variable: ikt1

Permutación covariante del tensor de permutación, también conocido como contorsión. Se define como



```maxima
d           d       d
          -g   itr  - g    itr   - itr   g
            ad    cb    bd    ca      ab  cd
ikt1    = ----------------------------------
    abc                   2
```


(Sustitúyase `g` por `ifg` si se utiliza una métrica para el sistema de referencia.)

<!-- category: Tensors -->
<!-- keywords: ikt2 -->
<!-- signatures: ikt2 -->
### Variable: ikt2

Permutación contravariante del tensor de permutación, también conocido como contorsión. Se define como



```maxima
c     cd
ikt2   = g   ikt1
    ab           abd
```


(Sustitúyase `g` por `ifg` si se utiliza una métrica para el sistema de referencia.)

<!-- category: Tensors -->
<!-- keywords: imetric -->
<!-- signatures: imetric(g) -->
### Function: imetric (g)

Especifica la métrica haciendo la asignación de la variable `imetric:g`, además las propiedades de contracción de la métrica *g* se fijan ejecutando las instrucciones `defcon(g), defcon(g,g,kdelta)`. La variable `imetric`, a la que no se le asigna ningún valor por defecto, tiene el valor de la métrica que se le haya asignado con la instrucción `imetric(g)`.

<!-- category: Tensors -->
<!-- keywords: indexed_tensor -->
<!-- signatures: indexed_tensor(tensor) -->
### Function: indexed_tensor (tensor)

Debe ejecutarse antes de asignarle componentes a un *tensor* para el que ya existe un valor, como `ichr1`, `ichr2` o `icurvature`. Véase el ejemplo de la descripción de `icurvature`.

<!-- category: Tensors -->
<!-- keywords: indices -->
<!-- signatures: indices(expr) -->
### Function: indices (expr)

Devuelve una lista con dos elementos. El primer elemento es una lista con los índices libres, aquellos que aparecen una sola vez. El segundo elemento es una lista con los índices mudos en *expr*, aquellos que aparecen exactamente dos veces. Por ejemplo,



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


Un producto tensorial que contenga el mismo índice más de dos veces es sintácticamente incorrecto. La función `indices` intenta tratar estas expresiones de una forma razonable; sin embargo, cuando se la obliga a manipular una expresión incorrecta puede tener un comportamiento imprevisto.

<!-- category: Tensors -->
<!-- keywords: inm -->
<!-- signatures: inm -->
### Variable: inm

Vector de no metricidad. La no metricidad conforme se define a partir de la derivada covariante del tensor métrico. La derivada covariante del tensor métrico, que normalmente es nula, se calcula, cuando `inonmet_flag` vale `true`, como 



```maxima
g     =- g  inm
 ij;k     ij   k
```

<!-- category: Tensors -->
<!-- keywords: inmc1 -->
<!-- signatures: inmc1 -->
### Variable: inmc1

Permutación covariante de las componentes del vector de no metricidad. Se define como



```maxima
g   inm  - inm  g   - g   inm
            ab    c      a  bc    ac    b
inmc1    = ------------------------------
     abc                 2
```


(Sustitúyase `g` por `ifg` si se utiliza una métrica para el sistema de referencia.)

<!-- category: Tensors -->
<!-- keywords: inmc2 -->
<!-- signatures: inmc2 -->
### Variable: inmc2

Permutación contravariante de las componentes del vector de no metricidad. Se utiliza en los coeficientes de conexión si `inonmet_flag` vale `true`. Se define como



```maxima
c         c         cd
          -inm  kdelta  - kdelta  inm  + g   inm  g
     c        a       b         a    b          d  ab
inmc2   = -------------------------------------------
     ab                        2
```


(Sustitúyase `g` por `ifg` si se utiliza una métrica para el sistema de referencia.)

<!-- category: Tensors -->
<!-- keywords: ishow -->
<!-- signatures: ishow(expr) -->
### Function: ishow (expr)

Muestra *expr* con todos los objetos indexados que contiene, junto con los correspondientes índices covariantes (como subíndices) y contravariantes (como superíndices). Los índices de derivadas se muestran como subíndices, separados de los covariantes por una coma; véanse los múltiples ejemplos de este documento.

<!-- category: Tensors -->
<!-- keywords: itr -->
<!-- signatures: itr -->
### Variable: itr

Tensor de torsión. Para una métrica con torsión, la diferenciación covariante iterada de una función escalar no conmuta, tal como demuestra el siguiente ejemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric:g;
(%o2)                                  g
(%i3) covdiff(covdiff(f([],[]),i),j)
         -covdiff(covdiff(f([],[]),j),i)$
(%i4) ishow(%)$
                                   %4              %2
(%t4)                    f    ichr2    - f    ichr2
                          ,%4      j i    ,%2      i j
(%i5) canform(%);
(%o5)                                  0
(%i6) itorsion_flag:true;
(%o6)                                true
(%i7) covdiff(covdiff(f([],[]),i),j)
        -covdiff(covdiff(f([],[]),j),i)$
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

Función delta de Kronecker simetrizada, utilizada en algunos cálculos. Por ejemplo:



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

Es la función delta generalizada de Kronecker definida en el paquete `itensor` siendo *L1* la lista de índices covariantes y *L2* la lista de índices contravariantes. La función  `kdelta([i],[j])` devuelve el valor de la delta ordinaria de Kronecker. La instrucción `ev(expr,kdelta)` provoca la evaluación de una expresión que contenga `kdelta([],[])`.


En un abuso de la notación, `itensor` también permite a `kdelta` tener 2 índices covariantes y ninguno contravariante, o 2 contravariantes y ninguno covariante. Esto es una funcionalidad del paquete, loque no implica que  `kdelta([i,j],[])` sea un objeto tensorial de pleno derecho.

<!-- category: Tensors -->
<!-- keywords: lc2kdt -->
<!-- signatures: lc2kdt(expr) -->
### Function: lc2kdt (expr)

Simplifica expresiones que contengan el símbolo de Levi-Civita, convirtiéndolas en expresiones con la delta de Kronecker siempre que sea posible. La diferencia principal entre esta función y la simple evaluación del símbolo de Levi-Civita consiste en que de esta última forma se obtienen expresiones de Kronecker con índices numéricos, lo que impide simplificaciones ulteriores. La función `lc2kdt` evita este problema, dando resultados con son más fáciles de simplificar con `rename` o `contract`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([k,l],[])*a([j],[k]))$
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


La función `lc2kdt` en ocasiones hace uso del tensor métrico. Si el tensor métrico no fue previamente definido con `imetric`, se obtiene un mensaje de error.



```maxima
(%i7) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([],[k,l])*a([j,k],[]))$
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
         %3 i       k   %4 j       l     %3 i       l   %4 j
(%t10) (g     kdelta   g     kdelta   - g     kdelta   g    
                    %3             %4               %3
              k
        kdelta  ) a
              %4   j k
(%i11) ishow(contract(expand(%)))$
                                  l i    l i  j
(%t11)                           a    - g    a
                                              j
```

<!-- category: Tensors -->
<!-- keywords: lc_l -->
<!-- signatures: lc_l -->
### Function: lc_l

Regla de simplificación utilizada en expresiones que contienen el símbolo de `levi_civita` sin evaluar. Junto con  `lc_u`, puede utilizarse para simplificar muchas expresiones de forma más eficiente que la evaluación de `levi_civita`. Por ejemplo:



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
(%i4) canform(contract(expand(applyb1(el1,lc_l,lc_u))));
(%t4)                                  0
(%i5) canform(contract(expand(applyb1(el2,lc_l,lc_u))));
(%t5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: lc_u -->
<!-- signatures: lc_u -->
### Function: lc_u

Regla de simplificación utilizada en expresiones que contienen el símbolo de `levi_civita` sin evaluar. Junto con  `lc_l`, puede utilizarse para simplificar muchas expresiones de forma más eficiente que la evaluación de `levi_civita`. Véase `lc_l`.

<!-- category: Tensors -->
<!-- keywords: levi_civita -->
<!-- signatures: levi_civita(L) -->
### Function: levi_civita (L)

Es el tensor de permutación de Levi-Civita, el cual devuelve 1  si la lista *L* con una permutación par de enteros, -1 si es en una permutación impar y 0 si algunos de los índices de *L* están repetidos.

<!-- category: Tensors -->
<!-- keywords: liediff -->
<!-- signatures: liediff(v, ten) -->
### Function: liediff (v, ten)

Calcula la derivada de Lie de la expresión tensorial *ten* respecto de campo vectorial *v*. La expresión *ten* debe ser cualquier tensor indexado; *v* debe ser el nombre (sin índices) de un campo vectorial. Por ejemplo:



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

Hace un listado de todos los tensores y sus índices en una expresión tensorial. Por ejemplo,



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

Impone la condición de Lorentz sustituyendo por 0 todos los objetos indexados de *expr* que tengan un índice derivado idéntico a un índice contravariante.

<!-- category: Tensors -->
<!-- keywords: makebox -->
<!-- signatures: makebox(expr) -->
### Function: makebox (expr)

Muestra *expr* de la misma manera que lo hace `show`; sin embargo, cualquier tensor de d’Alembert que aparezca en  *expr* estará indicado por `[]`.  Por ejemplo, `[]p([m],[n])` representa `g([],[i,j])*p([m],[n],i,j)`.

<!-- category: Tensors -->
<!-- keywords: rediff -->
<!-- signatures: rediff(ten) -->
### Function: rediff (ten)

Calcula todas las instrucciones `idiff` que aparezcan en la expresión tensorial *ten*.

<!-- category: Tensors -->
<!-- keywords: remcomps -->
<!-- signatures: remcomps(tensor) -->
### Function: remcomps (tensor)

Borra todos los valores de *tensor* que han sido asignados con la función `components`.

<!-- category: Tensors -->
<!-- keywords: remcon -->
<!-- signatures: remcon(tensor_1, ..., tensor_n), remcon(all) -->
### Function: remcon (tensor_1, ..., tensor_n)

Borra todas las propiedades de contracción de *tensor_1*, ..., *tensor_n*). La llamada `remcon(all)` borra todas las propiedades de contracción de todos los objetos indexados.

<!-- category: Tensors -->
<!-- keywords: remcoord -->
<!-- signatures: remcoord(tensor_1, tensor_2, ...), remcoord(all) -->
### Function: remcoord (tensor_1, tensor_2, ...)

Borra todas las propiedades de diferenciación coordenada de `tensor_i` que hayan sido establecidas por la función `coord`. La llamada `remcoord(all)` borra esta propiedad de todos los objetos indexados.

<!-- category: Tensors -->
<!-- keywords: remsym -->
<!-- signatures: remsym(tensor, m, n) -->
### Function: remsym (tensor, m, n)

Borra todas las propiedades de simetría del *tensor* que tiene *m* índices covariantes y *n* contravariantes.

<!-- category: Tensors -->
<!-- keywords: rename -->
<!-- signatures: rename(expr), rename(expr, count) -->
### Function: rename (expr)

Devuelve una expresión equivalente a *expr* pero con los índices mudos de cada término elegidos del conjunto  `[%1, %2,...]` si el segundo argumento opcional se omite. En otro caso, los índices mudos son indexados empezando con el valor *count*. Cada índice mudo en un producto será diferente. En el caso de las sumas, la función `rename` operará sobre cada término de la suma reinicializando el contador con cada término. De esta manera `rename` puede servir como simplificador tensorial. Además, los índices se ordenarán alfanuméricamente, si la variable `allsym` vale `true`, respecto de los índices covariantes y contravariantes dependiendo del valor de `flipflag`. Si  `flipflag` vale `false`, entonces los índices se renombrarán de acuerdo con el orden de los índices contravariantes. Si `flipflag` vale `true`, entonces los índices se renombrarán de acuerdo con el orden de los índices covariantes. Suele acontecer que el efecto combinado de los dos cambios de nombre reduzcan la expresión más de lo que que pueda reducir cualquiera de ellas por separado.




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
<!-- keywords: show -->
<!-- signatures: show(expr) -->
### Function: show (expr)

Muestra `expr` con sus objetos indexados que tengan índices covariantes como subíndices y los contravariantes como superíndices.  Los índices derivados se muestran como subíndices, separados por una coma de los covariantes.

<!-- category: Tensors -->
<!-- keywords: showcomps -->
<!-- signatures: showcomps(tensor) -->
### Function: showcomps (tensor)

Muestra las componentes de un tensor definidas con la instrucción `components`. Por ejemplo:



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


La función `showcomps` también puede mostrar las componentes de tensores de rango mayor de 2.

<!-- category: Tensors -->
<!-- keywords: simpmetderiv -->
<!-- signatures: simpmetderiv(expr), simpmetderiv(expr[, stop]) -->
### Function: simpmetderiv (expr)

Simplifica expresiones que contienen productos de las derivadas del tensor métrico. La función `simpmetderiv` reconoce dos identidades:



```maxima
ab        ab           ab                 a
  g   g   + g   g     = (g   g  )   = (kdelta )   = 0
   ,d  bc        bc,d         bc ,d          c ,d
```


de donde 



```maxima
ab          ab
  g   g   = - g   g
   ,d  bc          bc,d
```


y



```maxima
ab          ab
 g   g     = g   g
  ,j  ab,i    ,i  ab,j
```


que se deduce de las simetrías de los símbolos de Christoffel.


La función `simpmetderiv` tiene un argumento opcional, el cual detiene la función después de la primera sustitución exitosa en un expresión producto. La función `simpmetderiv` también hace uso de la variable global *flipflag* que determina cómo aplicar una ordenación “canónica” a los índices de los productos.


Todo esto se puede utilizar para conseguir buenas simplificaciones que serían difíciles o imposibles de conseguir, lo que se demuestra en el siguiente ejemplo, que utiliza explícitamente las simplificaciones parciales de `simpmetderiv`:



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


Véase también `weyl.dem` para un ejemplo que utiliza `simpmetderiv` y `conmetderiv` para simplificar contracciones del tensor de Weyl.

<!-- category: Tensors -->
<!-- keywords: tentex -->
<!-- signatures: tentex(expr) -->
### Function: tentex (expr)

Para utilizar la función `tentex`, primero se debe cargar `tentex`, tal como muestra el siguiente ejemplo:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) load("tentex");
(%o2)       /share/tensor/tentex.lisp
(%i3) idummyx:m;
(%o3)                                  m
(%i4) ishow(icurvature([j,k,l],[i]))$
            m1       i           m1       i           i
(%t4)  ichr2    ichr2     - ichr2    ichr2     - ichr2
            j k      m1 l        j l      m1 k        j l,k

                                                      i
                                               + ichr2
                                                      j k,l
(%i5) tentex(%)$
$$\Gamma_{j\,k}^{m_1}\,\Gamma_{l\,m_1}^{i}-\Gamma_{j\,l}^{m_1}\,
 \Gamma_{k\,m_1}^{i}-\Gamma_{j\,l,k}^{i}+\Gamma_{j\,k,l}^{i}$$
```


Nótese la asignación de la variable `idummyx` para evitar la aparición del símbolo del porcentaje en la expresión en TeX, que puede dar errores de compilación.


Téngase en cuenta que esta versión de la función `tentex` es experimental.

<!-- category: Tensors -->
<!-- keywords: undiff -->
<!-- signatures: undiff(expr) -->
### Function: undiff (expr)

Devuelve una expresión equivalente a *expr* pero con todas las derivadas de los objetos indexados reemplazadas por la forma nominal de la función `idiff`.

<!-- category: Tensors -->
<!-- keywords: | -->
<!-- signatures: | -->
### Variable: |

La barra vertical `|` representa la operación "contracción con un vector". Cuando un tensor covariante totalmente antisimétrico se contrae con un vector contravariante, el resultado no depende del índice utilizado para la contracción. Así, es posible definir la operación de contracción de forma que no se haga referencia al índice.


En el paquete `itensor` la contracción con un vector se realiza siempre respecto del primer índice de la ordenación literal. Ejemplo:



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


Nótese que es primordial que los tensores utilizados junto con el operador `|` se declaren totalmente antisimétricos en sus  índices covariantes. De no ser así, se pueden obtener resultados incorrectos.

<!-- category: Tensors -->
<!-- keywords: ~ -->
<!-- signatures: ~ -->
### Variable: ~

El operador del producto exterior se representa por el símbolo `~`. Este es un operador binario. Sus argumentos deben ser expresiones que tengan escalares, tensores covariantes de rango uno o tensores covariantes de rango `l` que hayan sido declarados antisimétricos en todos los índices covariantes.


El comportamiento del operador del producto exterior se controla con la variable `igeowedge_flag`, como en el ejemplo siguiente:



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

