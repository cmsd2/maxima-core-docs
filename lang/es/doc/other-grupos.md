## Grupos

<!-- category: Other -->
<!-- keywords: todd_coxeter -->
<!-- signatures: todd_coxeter(relaciones, subgrupo), todd_coxeter(relaciones) -->
### Function: todd_coxeter (relaciones, subgrupo)

Busca el orden de G/H donde G es el módulo del Grupo Libre de *relations*, y H es el subgrupo de G generado por `subgrupo`. `subgrupo` es un argumento opcional, cuyo valor por defecto es []. 


En este proceso se obtiene una tabla de multiplicación para la acción correcta de G sobre G/H, donde los co-cojuntos son enumerados [H,Hg2,Hg3,...]. Esto puede ser observado internamente en el `todd_coxeter_state`.


Ejemplo:



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

