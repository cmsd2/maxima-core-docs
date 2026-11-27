## f90

<!-- category: IO -->
<!-- keywords: f90 -->
<!-- signatures: f90(expr) -->
### Function: f90 (expr)

O comando f90 é uma atualização para o comando `fortran` original do
maxima. A diferença primária é o caminho através do qual linhas longas são quebradas.


No exemplo seguinte, observe como o comando `fortran` para linhas dentro de símbolos. O comando
`f90` jamais para linha dentro de um símbolo.



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


A implementação `f90` termina como um rápido reparo em `fortran`. Não é
necessáriamente um bom exemplo sobre o qual se deva basear outros tradutores do
Maxima para outras linguagens de programação.


Para usar essa função escreva primeiro `load("f90")`.

