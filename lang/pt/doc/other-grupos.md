## Grupos

<!-- category: Other -->
<!-- keywords: todd_coxeter -->
<!-- signatures: todd_coxeter(relação, subgroupo), todd_coxeter(relação) -->
### Function: todd_coxeter (relação, subgroupo)

Acha a ordem de G/H onde G é o módulo do Grupo Livre *relação*, e
H é o subgroupo de G gerado por *subgroupo*.  *subgroupo* é um argumento
opcional, cujo valor padrão é [].  Em fazendo isso a função produz uma
tabela de multiplicação à direita de G sobre G/H, onde os
co-conjuntos são enumerados [H,Hg2,Hg3,...].  Isso pode ser visto internamente no
`todd_coxeter_state`.


Exemplo:














```maxima
(%i1) symet(n):=create_list(
        if (j - i) = 1 then (p(i,j))^^3 else
            if (not i = j) then (p(i,j))^^2 else
                p(i,i) , j, 1, n-1, i, 1, j);
                                                       <3>
(%o1) symet(n) := create_list(if j - i = 1 then p(i, j)

                                <2>
 else (if not i = j then p(i, j)    else p(i, i)), j, 1, n - 1, 

i, 1, j)
(%i2) p(i,j) := concat(x,i).concat(x,j);
(%o2)        p(i, j) := concat(x, i) . concat(x, j)
(%i3) symet(5);
         <2>           <3>    <2>           <2>           <3>
(%o3) [x1   , (x1 . x2)   , x2   , (x1 . x3)   , (x2 . x3)   , 

            <2>           <2>           <2>           <3>    <2>
          x3   , (x1 . x4)   , (x2 . x4)   , (x3 . x4)   , x4   ]
(%i4) todd_coxeter(%o3);

Rows tried 426
(%o4)                          120
(%i5) todd_coxeter(%o3,[x1]);

Rows tried 213
(%o5)                          60
(%i6) todd_coxeter(%o3,[x1,x2]);

Rows tried 71
(%o6)                          20
```

