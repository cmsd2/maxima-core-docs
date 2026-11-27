## Groups

<!-- category: Other -->
<!-- keywords: todd_coxeter -->
<!-- signatures: todd_coxeter(relations, subgroup), todd_coxeter(relations) -->
### Function: todd_coxeter (relations, subgroup)

G/Hの次数を見つけます。
ここで、Gは法*relations*に関する自由群で、
Hは、*subgroup*が生成するGの部分群です。
*subgroup*は、オプションの引数であり、
省略すると[]になります。
これをする時には、
GのG/H上の右作用に関する乗算テーブルを生成します。
ここで、剰余類が[H,Hg2,Hg3,...]と数え上げられます。
これは、内部的に変数`todd_coxeter_state`で見ることができます。


例:














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

