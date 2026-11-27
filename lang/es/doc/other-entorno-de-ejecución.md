## Entorno de Ejecución

<!-- category: Other -->
<!-- keywords: absolute_real_time -->
<!-- signatures: absolute_real_time() -->
### Function: absolute_real_time ()

Devuelve el número de segundos transcurridos desde la medianoche
del 1 de enero de 1900 UTC. Este valor es un número entero
positivo.


Véanse también `elapsed_real_time` y `elapsed_run_time`.


Ejemplo:







```maxima
(%i1) absolute_real_time ();
(%o1)                      3385045277
(%i2) 1900 + absolute_real_time () / (365.25 * 24 * 3600);
(%o2)                   2007.265612087104
```

<!-- category: Other -->
<!-- keywords: elapsed_real_time -->
<!-- signatures: elapsed_real_time() -->
### Function: elapsed_real_time ()

Devuelve los segundos (incluyendo fracciones de segundo) 
transcurridos desde que Maxima se inició (o reinició) la sesión de
Maxima. Este valor es un decimal en coma flotante.


Véanse también `absolute_real_time` y `elapsed_run_time`.


Ejemplo:








```maxima
(%i1) elapsed_real_time ();
(%o1)                       2.559324
(%i2) expand ((a + b)^500)$
(%i3) elapsed_real_time ();
(%o3)                       7.552087
```

<!-- category: Other -->
<!-- keywords: elapsed_run_time -->
<!-- signatures: elapsed_run_time() -->
### Function: elapsed_run_time ()

Devuelve una estimación en segundos (incluyendo fracciones de segundo) 
durante los cuales Maxima ha estado realizando cálculos desde que se
inició (o reinició) la sesión actual. 
Este valor es un decimal en coma flotante.


Véanse también `absolute_real_time` y `elapsed_real_time`.


Ejemplo:








```maxima
(%i1) elapsed_run_time ();
(%o1)                         0.04
(%i2) expand ((a + b)^500)$
(%i3) elapsed_run_time ();
(%o3)                         1.26
```

<!-- category: Other -->
<!-- keywords: maxima_tempdir -->
<!-- signatures: maxima_tempdir -->
### Variable: maxima_tempdir

La variable `maxima_tempdir` almacena la ruta del directorio
en el que Maxima crea ciertos ficheros temporales.
En particular, los ficheros temporales para la realización de
gráficos se guardan en `maxima_tempdir`.


El valor que inicialmente toma esta variable es el directorio
de inicio del usuario, si Maxima es capaz de localizarlo; en
caso contrario, Maxima intenta encontrar un directorio que
sea aceptable.


A la variable `maxima_tempdir` se le puede asignar una
cadena de caracteres con la ruta del directorio.

<!-- category: Other -->
<!-- keywords: maxima_userdir -->
<!-- signatures: maxima_userdir -->
### Variable: maxima_userdir

La variable `maxima_userdir` almacena la ruta del 
directorio en el que Maxima buscará ficheros Lisp y de
Maxima. Maxima también busca en otros directorios, guardando las variables
`file_search_maxima` y `file_search_lisp` la lista
completa de búsqueda.


El valor que inicialmente toma esta variable es el de un subdirectorio
del directorio de inicio del usuario, si Maxima es capaz de localizarlo;
en caso contrario, Maxima intenta encontrar un directorio que
sea aceptable.


A la variable `maxima_userdir` se le puede asignar una
cadena de caracteres con la ruta del directorio.
Sin embargo, cambiando el valor de la variable `maxima_userdir`
no se alteran `file_search_maxima` ni `file_search_lisp`,
cuyos contenidos se modifican mediante otro sistema.

<!-- category: Other -->
<!-- keywords: room -->
<!-- signatures: room(), room(true), room(false) -->
### Function: room ()

Presenta una descrpción del estado de almacenamiento y gestión de la pila en Maxima. La llamada `room` invoca a la función Lisp homónima.



- *
`room ()` prints out a moderate description.
- *
`room (true)` prints out a verbose description.
- *
`room (false)` prints out a terse description.

<!-- category: Other -->
<!-- keywords: sstatus -->
<!-- signatures: sstatus(keyword, item) -->
### Function: sstatus (keyword, item)

Si *keyword* es el símbolo `feature`, *item*
será colocado en la lista de propiedades del sistema. Una vez ejecutado
`sstatus (keyword, item)`, `status (feature, item)` devuelve
`true`. Si *keyword* es el símbolo `nofeature`,
*item* se borrará de la lista de propiedades del sistema.
Esto puede ser de utilidad para los autores de paquetes, permitiendo
mantener el control sobre las propiedades que se han ido estableciendo.


Véase también `status`.

<!-- category: Other -->
<!-- keywords: status -->
<!-- signatures: status(feature), status(feature, item) -->
### Function: status (feature)

Devuelve información sobre la presencia o ausencia de ciertas
propiedades dependientes del sistema.



- *
`status (feature)` devuelve una lista con características
del sistema. Éstas incluyen la versión de Lisp, tipo de sistema 
operativo, etc. La lista puede variar de un Lisp a otro.
- *
`status (feature, item)` devuelve `true` si *item*
está en la lista de elementos retornados por `status (feature)`
y `false` en otro caso.
La función `status` no evalúa el argumento *item*. El operador
de doble comilla simple, `''`, permite la evaluación. Una 
propiedad cuyo nombre contenga un carácter especial debe ser suministrada
como un argumento del tipo cadena. Por ejemplo,
`status (feature, "ansi-cl")`.


Véase también `sstatus`.


La variable `features` contiene una lista de propiedades que se 
aplican a expresiones matemáticas. Véanse `features` y `featurep`
para más información.

<!-- category: Other -->
<!-- keywords: system -->
<!-- signatures: system(command) -->
### Function: system (command)

Ejecuta la instrucción *command* como un proceso independiente de Maxima.
La instrucción se le pasa a la consola del sistema para su ejecución.
La función `system` no está soportada por todos los sistemas operativos, pero suele estarlo en todos los entornos  Unix y similares.


Suponiendo que `_hist.out` es una lista de frecuencias que se quieren representar en un diagrama de barras utilizando el programa `xgraph`,



```maxima
(%i1) (with_stdout("_hist.out",
           for i:1 thru length(hist) do (
             print(i,hist[i]))),
       system("xgraph -bar -brw .7 -nl < _hist.out"));
```


A fin de hacer el diagrama y eliminar el archivo temporal posteriormente, hágase:



```maxima
system("(xgraph -bar -brw .7 -nl < _hist.out;  rm -f _hist.out)&")
```

<!-- category: Other -->
<!-- keywords: time -->
<!-- signatures: time(%o1, %o2, %o3, ...) -->
### Function: time (%o1, %o2, %o3, ...)

Devuelve una lista de los tiempos, en segundos, que fueron necesarios para calcular los resultados de las salidas `%o1`, `%o2`, `%o3`, .... Los tiempos devueltos son estimaciones hechas por Maxima del tiempo interno de computación. La función `time` sólo puede utilizarse para variables correspondientes a líneas de salida; para cualquier otro tipo de variables, `time` devuelve `unknown`.


Hágase `showtime: true` para que Maxima devuelva el tiempo de ejecución de cada línea de salida.

<!-- category: Other -->
<!-- keywords: timedate -->
<!-- signatures: timedate(), timedate(T) -->
### Function: timedate ()

Sin argumento, `timedate` devuelve una cadena que 
representa la hora y fecha actuales. La cadena tiene el
formato `YYYY-MM-DD HH:MM:SS[+|-]ZZ:ZZ`, donde
los campos indicados son: año, mes, día,
horas, minutos, segundos y número de horas de diferencia
con respecto a la hora GMT.


Con argumento, `timedate(T)` devuelve la hora
*T* como una cadena con formato `YYYY-MM-DD HH:MM:SS[+|-]ZZ:ZZ`.
*T* se interpreta como el número de segundos transcurridos
desde la medianoche del uno de enero de 1900, tal como lo devuelve
`absolute_real_time`.


Ejemplos:


`timedate` sin argumento devuelve una cadena con la hora y fecha actuales.







```maxima
(%i1) d : timedate ();
(%o1)                      2010-06-08 04:08:09+01:00
(%i2) print ("timedate reports current time", d) $
timedate reports current time 2010-06-08 04:08:09+01:00
```


`timedate` con argumento devuelve una cadena que representa al propio argumento.







```maxima
(%i1) timedate (0);
(%o1)                      1900-01-01 01:00:00+01:00
(%i2) timedate (absolute_real_time () - 7*24*3600);
(%o2)                      2010-06-01 04:19:51+01:00
```

