## Lectura y escritura

<!-- category: IO -->
<!-- keywords: fortindent -->
<!-- signatures: fortindent -->
### Variable: fortindent

Valor por defecto: 0


La variable `fortindent` controla el margen izquierdo de las expresiones que 
escribe la instrucción `fortran`.  El valor 0 escribe con un margen normal 
de 6 espacios; valores positivos harán que las expresiones se escriban más a la derecha.

<!-- category: IO -->
<!-- keywords: fortran -->
<!-- signatures: fortran(expr) -->
### Function: fortran (expr)

Escribe *expr* en código Fortran. La salida se escribe con márgenes, y si ésta es demasiado larga `fortran` sigue escribiendo en líneas sucesivas. La función `fortran` escribe el operador de exponenciación `^` como `**`, e imprime un número complejo `a + b %i` como `(a,b)`.


El argumento *expr* puede ser una ecuación. En tal caso, `fortran` escribe una sentencia de asignación, dándole el valor del miembro derecho de la expresión al miembro izquierdo. En particular, si el miembro derecho de *expr* es el nombre de una matriz, entonces `fortran` escribe una sentencia de asignación para cada elemento de la matriz.


Si *expr* no es reconozida por `fortran`, la expresión se escribe en formato `grind` sin avisos. La función `fortran` no reconoce listas, arreglos ni funciones.


La variable `fortindent` controla el margen izquierdo de las expresiones que escribe la instrucción `fortran`.  El valor 0 escribe con un margen normal de 6 espacios; valores positivos harán que las expresiones se escriban más a la derecha.


Si `fortspaces` vale `true`, `fortran` rellena las líneas con espacios de 80 columnas.


La función `fortran` evalúa sus argumentos; un argumento precedido de apóstrofo previene de la evaluación.
La función `fortran` siempre devuelve `done`.


Ejemplos:



(%i1) expr: (a + b)^12$
(%i2) fortran (expr);
      (b+a)**12                                                                 
(%o2)                         done
(%i3) fortran ('x=expr);
      x = (b+a)**12                                                             
(%o3)                         done
(%i4) fortran ('x=expand (expr));
      x = b**12+12*a*b**11+66*a**2*b**10+220*a**3*b**9+495*a**4*b**8+792        
     1   *a**5*b**7+924*a**6*b**6+792*a**7*b**5+495*a**8*b**4+220*a**9*b        
     2   **3+66*a**10*b**2+12*a**11*b+a**12                                     
(%o4)                         done
(%i5) fortran ('x=7+5*%i);
      x = (7,5)                                                                 
(%o5)                         done
(%i6) fortran ('x=[1,2,3,4]);
      x = [1,2,3,4]                                                             
(%o6)                         done
(%i7) f(x) := x^2$
(%i8) fortran (f);
      f                                                                         
(%o8)                         done

<!-- category: IO -->
<!-- keywords: fortspaces -->
<!-- signatures: fortspaces -->
### Variable: fortspaces

Valor por defecto: `false`


Si `fortspaces` vale `true`, `fortran` rellena las líneas 
con espacios de 80 columnas.

