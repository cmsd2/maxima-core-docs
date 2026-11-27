## Detección e informe de fallos

<!-- category: Other -->
<!-- keywords: bug_report -->
<!-- signatures: bug_report() -->
### Function: bug_report ()

Imprime las versiones de Maxima y de Lisp y proporciona un enlace a la
página web sobre informe de fallos del proyecto Maxima. 
La información respecto a las versiones es la misma que reporta la 
función `build_info`. 


Cuando se informa sobre un fallo, es de gran ayuda que se copie la
información relacionada con la versión de Maxima y de Lisp usada,
dentro del propio informe. 


`bug_report` retorna una cadena vacía `""`.

<!-- category: Other -->
<!-- keywords: build_info -->
<!-- signatures: build_info() -->
### Function: build_info ()

Devuelve un resumen de los parÃ¡metros con los que se ha compilado Maxima
en formato de estructura `defstruct`. Los campos de la estructura son:
`version`, `timestamp`, `host`, `lisp_name` y `lisp_version`.
Cuando `display2d` toma el valor `true`, la estructura se muestra como una
pequeña tabla.


Véase también `bug_report`.


Ejemplos:













```maxima
(%i1) build_info ();
(%o1) 
Maxima version: "5.26.0_16_gb72c64c_dirty"
Maxima build date: "2012-01-29 12:29:04"
Host type: "i686-pc-linux-gnu"
Lisp implementation type: "CMU Common Lisp"
Lisp implementation version: "CVS release-19a 19a-release-20040728 + minimal debian patches"

(%i2) x : build_info ()$

(%i3) x@version;
(%o3)               5.26.0_16_gb72c64c_dirty


(%i4) x@timestamp;
(%o4)                  2012-01-29 12:29:04


(%i5) x@host;
(%o5)                   i686-pc-linux-gnu


(%i6) x@lisp_name;
(%o6)                    CMU Common Lisp


(%i7) x@lisp_version;
(%o7) 
    CVS release-19a 19a-release-20040728 + minimal debian patches


(%i8) x;
(%o8) 
Maxima version: "5.26.0_16_gb72c64c_dirty"
Maxima build date: "2012-01-29 12:29:04"
Host type: "i686-pc-linux-gnu"
Lisp implementation type: "CMU Common Lisp"
Lisp implementation version: "CVS release-19a 19a-release-20040728 + minimal debian patches"
```

<!-- category: Other -->
<!-- keywords: run_testsuite -->
<!-- signatures: run_testsuite([options]) -->
### Function: run_testsuite ([options])

Ejecuta el conjunto de pruebas de Maxima. Los tests que producen las 
respuestas deseadas son considerados como “pruebas superadas”, como
los tests que no producen las respuestas deseadas, son marcados como
fallos conocidos. 


`run_testsuite` admite las siguientes opciones:



**display_all** — Muestra todas las pruebas. Normalmente no se muestran las pruebas,
a menos que produzcan fallos. (Su valor por defecto es `false`).
**display_known_bugs** — Muestra las pruebas marcadas como fallos ya conocidos. (Su valor
por defecto es `false`).
**tests** — Esta es la lista de las pruebas que se deben ejecutar. Cada prueba
se puede especificar, tanto mediante una cadena de texto como
por un símbolo. Por defecto, todas las pruebas se ejecutan. El
conjunto completo de pruebas está especificado en `testsuite_files`.
**time** — Muestra información sobre tiempos de ejecución. Si vale `true`,
se muestran los tiempos de los ficheros de prueba. Si vale `all`,
se muestran los tiempos de cada prueba individual si `display_all`
vale `true`. El valor por defecto es `false`, por lo que no
se muestra información temporal alguna.


Por ejemplo, `run_testsuite(display_known_bugs = true, tests=[rtest5])`
ejecuta la prueba `rtest5` y muestra si está marcada como fallo
conocido.


`run_testsuite(display_all = true, tests=["rtest1", rtest1a])` ejecutará
las pruebas `rtest1` y `rtest2`, mostrando cada una de ellas.


`run_testsuite` cambia el entorno de Maxima. 
Típicamente un script de test ejecuta `kill` para establecer un entorno conocido (llámese uno sin funciones ni variables definidas por el usuario) y entonces define una serie de funciones y variables apropiadas para el test. 


`run_testsuite` retorna `done`.

<!-- category: Other -->
<!-- keywords: testsuite_files -->
<!-- signatures: testsuite_files -->
### Variable: testsuite_files

`testsuite_files` es el conjunto de tests a ejecutar por `run_testsuite`. Se trata de una lista con los nombres de los ficheros que contienen los tests a ejecutar. Si se sabe que alguno de los tests de un fichero falla, entonces en lugar de listar el nombre del fichero, se utiliza una lista que contiene el nombre del fichero y los números de los tests que fallan.


Por ejemplo, esta es una parte de los tests por defecto:



```maxima
["rtest13s", ["rtest14", 57, 63]]
```


Con esto se especifica que el conjunto de tests está formado por los ficheros "rtest13s"  y "rtest14", pero que "rtest14" contiene dos tests que se sabe que causan fallos, el 57 y el 63.

