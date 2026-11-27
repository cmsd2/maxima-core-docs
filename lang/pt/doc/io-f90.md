## f90

<!-- category: IO -->
<!-- keywords: f90 -->
<!-- signatures: f90(expr) -->
### Function: f90 (expr)

O comando f90 é uma actualização do comando
`fortran` original do maxima. A principal diferença
é na forma como são divididas as linhas muito compridas.


No exemplo seguinte, observe como o comando `fortran` divide linhas
no meio de símbolos. O comando `f90` nunca separa uma
linha no meio de um símbolo.



```maxima
(%i1) load("f90")$

(%i2) expr:expand((xxx+yyy+7)^4);
         4            3         3        2    2
(%o2) yyy  + 4 xxx yyy  + 28 yyy  + 6 xxx  yyy
             2          2        3             2
 + 84 xxx yyy  + 294 yyy  + 4 xxx  yyy + 84 xxx  yyy
                               4         3          2
 + 588 xxx yyy + 1372 yyy + xxx  + 28 xxx  + 294 xxx
 + 1372 xxx + 2401
(%i3) fortran(expr);
      yyy**4+4*xxx*yyy**3+28*yyy**3+6*xxx**2*yyy**2+84*xxx*yyy**2+294*yy
     1   y**2+4*xxx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372*yyy+xxx**4+28*
     2   xxx**3+294*xxx**2+1372*xxx+2401
(%o3)                       done
(%i4) f90(expr);
yyy**4+4*xxx*yyy**3+28*yyy**3+6*xxx**2*yyy**2+84*xxx*yyy**2+294* &
     yyy**2+4*xxx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372*yyy+xxx** &
     4+28*xxx**3+294*xxx**2+1372*xxx+2401
(%o4)                       done
```


A função `f90` foi criada como uma forma rápida de resolver
um problema. Não será necessariamente um bom exemplo a seguir para
traduções de outras linguagens de programação.


Para usar esta função, use primeiro `load("f90")`.

