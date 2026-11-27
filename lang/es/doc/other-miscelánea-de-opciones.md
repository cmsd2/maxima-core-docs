## Miscelánea de opciones

<!-- category: Other -->
<!-- keywords: askexp -->
<!-- signatures: askexp -->
### Variable: askexp

Cuando se invoca a `asksign`, la expresión que se va 
a analizar es precisamente `askexp`.

<!-- category: Other -->
<!-- keywords: genindex -->
<!-- signatures: genindex -->
### Variable: genindex

Valor por defecto: `i`


La variable `genindex` es el prefijo alfabético utilizado para generar la siguiente variable de sumación en caso de necesidad.

<!-- category: Other -->
<!-- keywords: gensumnum -->
<!-- signatures: gensumnum -->
### Variable: gensumnum

Valor por defecto: 0


La variable `gensumnum` es el sufijo numérico utilizado para generar la siguiente variable de sumación. Si vale  `false` entonces el índice consistirá solamente de  `genindex`, sin sufijo numérico.

<!-- category: Other -->
<!-- keywords: gensym -->
<!-- signatures: gensym(), gensym(x) -->
### Function: gensym ()

`gensym()` crea y devuelve una nueva símbolo o
variable sin valor asignado.


El nombre del nuevo símbolo está formado por la
concatenación de un prefijo, cuyo valor por defecto es "g", y de
un sufijo, el cual es la representación decimal de un número que
coincide, por defecto, con el valor de un contador interno de Lisp.


En caso de suministrar el argumento *x*, siendo este una cadena,
se utilizará como prefijo en lugar de "g", lo cual tendrá efecto
sólo para esta llamada a `gensym`Â·


En caso de suministrar el argumento *x*, siendo este un número
entero, se utilizará como sufijo en lugar del contador interno de
Lisp, lo cual tendrá efecto sólo para esta llamada a `gensym`Â·


Si no se suministra el sufijo en forma explícita, y sólo
en este caso, el contador interno sufrirá un incremento después de
haber sido utilizado.


Ejemplos:








```maxima
(%i1) gensym();
(%o1)                         g887
(%i2) gensym("new");
(%o2)                        new888
(%i3) gensym(123);
(%o3)                         g123
```

<!-- category: Other -->
<!-- keywords: remvalue -->
<!-- signatures: remvalue(nombre_1, ..., nombre_n), remvalue(all) -->
### Function: remvalue (nombre_1, ..., nombre_n)

Elimina del sistema los valores de las variable de usuario *nombre_1*, ..., *nombre_n* (incluso las que tienen subíndices).


La llamada `remvalue (all)` elimina los valores de todas las variables en `values`, la lista de todas las variables a las que el usuario a dado algún nombre, pero no de aquéllas a las que Maxima asigna automáticamente un valor.


Véase también `values`.

<!-- category: Other -->
<!-- keywords: rncombine -->
<!-- signatures: rncombine(expr) -->
### Function: rncombine (expr)

Transforma *expr* combinando todos los términos de *expr* que tengan denominadores idénticos o que difieran unos de otros por factores numéricos. Su comportamiento es diferente al de la función `combine`, que combina términos con iguales denominadores.


Haciendo `pfeformat: true` y utilizando `combine` se consiguen resultados similares a aquéllos que se pueden obtener con  `rncombine`, pero `rncombine` realiza el paso adicional de multiplicar denominadores numéricos. Esto da como resultado expresiones en las que se pueden reconocer algunas cancelaciones.


Antes de utilizar esta función ejecútese `load("rncomb")`.

<!-- category: Other -->
<!-- keywords: setup_autoload -->
<!-- signatures: setup_autoload(nombre_fichero, función_1, ..., función_n) -->
### Function: setup_autoload (nombre_fichero, función_1, ..., función_n)

Especifica que si alguna de las funciones *function_1*, ..., *function_n* es referenciada pero todavía no ha sido definida, se cargará *nombre_fichero* mediante una llamada a `load`. El *nombre_fichero* normalmente contendrá las definiciones de las funciones especificadas, aunque esto no es imperativo.


La función `setup_autoload` no opera con arreglos de funciones.


La función `setup_autoload` no evalúa sus argumentos.


Ejemplo:



```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma function ultraspherical
Warning - you are redefining the Macsyma function legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);
                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

<!-- category: Other -->
<!-- keywords: tcl_output -->
<!-- signatures: tcl_output(list, i0, skip), tcl_output(list, i0), tcl_output([list_1, ..., list_n], i) -->
### Function: tcl_output (list, i0, skip)

Imprime los elementos de una lista encerrándolos con llaves `{ }`,
de forma apropiada para ser utilizado en un programa en el lenguaje Tcl/Tk.


`tcl_output (list, i0, skip)`
imprime *list*, empezando por el elemento *i0* siguiendo luego con los
elementos `i0 + skip`, `i0 + 2 skip`, etc.


`tcl_output (list, i0)`
equivale a `tcl_output (list, i0, 2)`.


`tcl_output ([list_1, ..., list_n], i)`
imprime los *i*-ésimos elementos de *list_1*, ..., *list_n*.


Ejemplos:














```maxima
(%i1) tcl_output ([1, 2, 3, 4, 5, 6], 1, 3)$

 {1.000000000     4.000000000     
 }
(%i2) tcl_output ([1, 2, 3, 4, 5, 6], 2, 3)$

 {2.000000000     5.000000000     
 }
(%i3) tcl_output ([3/7, 5/9, 11/13, 13/17], 1)$

 {((RAT SIMP) 3 7) ((RAT SIMP) 11 13) 
 }
(%i4) tcl_output ([x1, y1, x2, y2, x3, y3], 2)$

 {$Y1 $Y2 $Y3 
 }
(%i5) tcl_output ([[1, 2, 3], [11, 22, 33]], 1)$

 {SIMP 1.000000000     11.00000000     
 }
```

