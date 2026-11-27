## f90

<!-- category: IO -->
<!-- keywords: f90 -->
<!-- signatures: f90(expr_1, ..., expr_n) -->
### Function: f90 (expr_1, ..., expr_n)

Imprime una o más expresiones *expr_1*, ..., *expr_n*
como un programa Fortran 90. El programa se obtiene a través de
la salida estándar.


La función `f90` imprime su salida en el llamado formato libre de
Fortran 90: no se presta atención alguna a las posiciones de caracteres
respecto de las columnas y los renglones largos se dividen a un ancho fijo con el
carácter `&` indicando continuación de código.


Ejecútese `load("f90")` antes de utilizar esta función.


Véase también `fortran`.


Ejemplos:








```maxima
(%i1) load ("f90")$
(%i2) foo : expand ((xxx + yyy + 7)^4);
         4            3         3        2    2             2
(%o2) yyy  + 4 xxx yyy  + 28 yyy  + 6 xxx  yyy  + 84 xxx yyy
          2        3             2
 + 294 yyy  + 4 xxx  yyy + 84 xxx  yyy + 588 xxx yyy + 1372 yyy
      4         3          2
 + xxx  + 28 xxx  + 294 xxx  + 1372 xxx + 2401
(%i3) f90 ('foo = foo);
foo = yyy**4+4*xxx*yyy**3+28*yyy**3+6*xxx**2*yyy**2+84*xxx*yyy**2&
+294*yyy**2+4*xxx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372*yyy+xxx**&
4+28*xxx**3+294*xxx**2+1372*xxx+2401
(%o3)                         false
```


Expresiones múltiples. Captura de la salida estándar a un fichero
por medio de la función `with_stdout`.









```maxima
(%i1) load ("f90")$
(%i2) foo : sin (3*x + 1) - cos (7*x - 2);
(%o2)              sin(3 x + 1) - cos(7 x - 2)
(%i3) with_stdout ("foo.f90",
                   f90 (x=0.25, y=0.625, 'foo=foo, 'stop, 'end));
(%o3)                         false
(%i4) printfile ("foo.f90");
x = 0.25
y = 0.625
foo = sin(3*x+1)-cos(7*x-2)
stop
end
(%o4)                        foo.f90
```

