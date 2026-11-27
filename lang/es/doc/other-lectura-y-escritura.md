## Lectura y escritura

<!-- category: Other -->
<!-- keywords: appendfile -->
<!-- signatures: appendfile(filename) -->
### Function: appendfile (filename)

Añade información de la consola a *filename*, de igual manera que lo hace `writefile`, pero con la salvedad de que si el archivo ya existe la información queda añadida al final de su contenido.


La función `closefile` cierra los archivos abiertos por `appendfile` o `writefile`.

<!-- category: Other -->
<!-- keywords: batch -->
<!-- signatures: batch(filename), batch(filename, option) -->
### Function: batch (filename)

`batch(filename)` lee expresiones de Maxima desde *filename* y 
las evalúa. La función `batch` busca *filename* en la lista 
`file_search_maxima`. Véase `file_search`.


`batch(filename, test)` es como `run_testsuite` con la
opción `display_all=true`. En este caso `batch` busca *filename* 
en la lista `file_search_maxima` y no en `file_search_tests` como hace
`run_testsuite`. Además, `run_testsuite` ejecuta tests que están
en la lista `testsuite_files`. Con `batch` es posible ejecutar
cualquier fichero que se encuentre en `file_search_maxima` en modo de prueba.


El contenido de *filename* debe ser una secuencia de expresiones de Maxima,
cada una de las cuales termina en `;` o `$`.
La variable especial `%` y la función `%th`
se refieren a resultados previos dentro del archivo.
El archivo puede incluir construcciones del tipo `:lisp`.
Espacios, tabulaciones y saltos de línea en el archivo se ignoran.
Un archivo de entrada válido puede crearse con un editor de texto o con la 
función `stringout`.


La función `batch` lee las expresiones del archivo *filename*, 
muestra las entradas en la consola, realiza los cálculos solicitados y 
muestra las expresiones de los resultados.
A las expresiones de entrada se les asignan etiquetas, así 
como a las de salida. La función `batch` evalúa todas las expresiones 
de entrada del archivo a menos que se produzca un error. Si se le solicita 
información al usuario (con `asksign` o `askinteger`, por ejemplo)
`batch` se detiene para leer la nueva información para luego continuar.


Es posible detener  `batch` tecleando `control-C` desde la consola.
El efecto de `control-C` depende del entorno Lisp instalado.


La función `batch` tiene diversas aplicaciones, tales como servir de 
almacén de código escrito por el usuario, suministrar demostraciones
libres de errores o ayudar a organizar el trabajo del usuario en la resolución 
de problemas complejos.


La función `batch` evalúa su argumento y devuelve la ruta hacia
*filename* en formato cadena cuando es invocada sin segundo argumento
o con la opción `demo`. Cuando es llamada con la opción `test`, 
devuelve la lista vacía `[]` o una lista con *filename*
y los números de tests que han fallado.


Véanse también  `load`, `batchload` y `demo`.

<!-- category: Other -->
<!-- keywords: batchload -->
<!-- signatures: batchload(filename) -->
### Function: batchload (filename)

Lee expresiones de Maxima desde *filename* y las evalúa sin mostrar las entradas ni las salidas y sin asignarles etiquetas. Sin embargo, las salidas producidas por  `print` o `describe` sí se muestran.


La variable especial `%` y la función `%th` se refieren a resultados previos del intérprete interactivo, no a los del propio archivo. El archivo no puede incluir construcciones del tipo `:lisp`.


La función `batchload` devuelve la ruta de *filename* en formato de cadena.


La función `batchload` evalúa sus argumentos.


Véanse también `batch` y `load`.

<!-- category: Other -->
<!-- keywords: closefile -->
<!-- signatures: closefile() -->
### Function: closefile ()

La función `closefile` cierra los archivos abiertos por `appendfile` o `writefile`.

<!-- category: Other -->
<!-- keywords: file_output_append -->
<!-- signatures: file_output_append -->
### Variable: file_output_append

Valor por defecto: `false`


La variable `file_output_append` controla si las funciones de escritura de ficheros añaden información o sustituyen el fichero de salida. Cuando `file_output_append` toma el valor `true`, estas funciones amplían el contenido de sus ficheros de salida; en otro caso, sustituyen el fichero anterior de igual nombre por otro con el nuevo contenido.


Las funciones `save`, `stringout` y `with_stdout` se ven afectadas por el valor que tome la variable `file_output_append`. Otras funciones que también escriben en ficheros de salida no tienen en cuenta este valor; en concreto, las funciones para la representación de gráficos y las de traducción siempre sustituyen el fichero anterior por uno nuevo de igual nombre, mientras que las funciones `tex` y `appendfile` siempre añaden información al fichero de salida sin eliminar la información anterior.

<!-- category: Other -->
<!-- keywords: file_search -->
<!-- signatures: file_search(filename), file_search(filename, pathlist) -->
### Function: file_search (filename)

La función `file_search` busca el archivo *filename* y devuelve su ruta como una cadena; si no lo encuentra,  `file_search` devuelve `false`. La llamada 
`file_search (filename)` busca en los directorios de búsqueda por defecto,
que son los especificados por las variables `file_search_maxima`, `file_search_lisp` y `file_search_demo`.


La función `file_search` analiza primero si el nombre del argumento existe antes de hacerlo coincidir con los comodines de los patrones de búsqueda de archivos.
Véase `file_search_maxima` para más información sobre patrones de búsqueda de archivos.


El argumento *filename* puede ser una ruta con nombre de archivo,
o simplemente el nombre del archivo, o, si el directorio de búsqueda de archivo incluye un patrón de búsqueda, es suficiente con el nombre de archivo sin extensión.
Por ejemplo,



```maxima
file_search ("/home/wfs/special/zeta.mac");
file_search ("zeta.mac");
file_search ("zeta");
```


todos buscan el mismo archivo, dando por hecho que el archivo existe y que `/home/wfs/special/###.mac`
está en `file_search_maxima`.


La llamada `file_search (filename, pathlist)` busca solamente en los directorios especificados por *pathlist*, que es una lista de cadenas.
El argumento *pathlist* ignora los directorios de búsqueda por defecto, de manera que si se da la lista de rutas, `file_search` busca solamente en ellas y no en los directorios por defecto.
Incluso si hay un único directorio en *pathlist*, debe ser suministrado como una lista de un único elemento.


El usuario puede modificar los directorios de búsqueda por defecto; véase para ello See `file_search_maxima`.


La función `file_search` es llamada por `load` con los directorios de búsqueda `file_search_maxima` y `file_search_lisp`.

<!-- category: Other -->
<!-- keywords: file_search_maxima, file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
<!-- signatures: file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
### Variable: file_search_maxima

Estas variables especifican listas de directorios en los que deben buscar la funciones  `load`, `demo` y algunas otras. Los valores por defecto de estas variables nombran directorios de la instalación de Maxima.


El usuario puede modificar estas variables, bien reemplazando los valores por defecto, bien añadiendo nuevos directorios.
Por ejemplo,



```maxima
file_search_maxima: ["/usr/local/foo/###.mac",
    "/usr/local/bar/###.mac"]$
```


reemplaza el valor por defecto de `file_search_maxima`, mintras que



```maxima
file_search_maxima: append (file_search_maxima,
    ["/usr/local/foo/###.mac", "/usr/local/bar/###.mac"])$
```


añade dos directorios más. Puede ser conveniente colocar una expresión como esta en el archivo `maxima-init.mac`, de manera que la ruta de búsqueda de ficheros se asigne automáticamente cada vez que arranca Maxima.


Se pueden especificar varias extensiones de archivos y rutas con comodines especiales.
La cadena `###` representa el nombre del archivo buscado y una lista separada de comas y encerrada entre llaves,  `{foo,bar,baz}` representa múltiples cadenas.
Por ejemplo, suponiendo que se busca el nombre `neumann`,



```maxima
"/home/{wfs,gcj}/###.{lisp,mac}"
```


se interpreta como `/home/wfs/neumann.lisp`, `/home/gcj/neumann.lisp`, `/home/wfs/neumann.mac` y `/home/gcj/neumann.mac`.

<!-- category: Other -->
<!-- keywords: file_type -->
<!-- signatures: file_type(filename) -->
### Function: file_type (filename)

Devuelve una descripción del contenido de *filename* basada en la 
extensión, sin intentar abrir el archivo para inspeccionar su contenido.


El valor devuelto es un símbolo `object`, `lisp` o 
`maxima`. Si la extensión es "mac", "mc", "demo", "dem", "dm1", "dm2", 
"dm3" o "dmt", `file_type` devuelve `maxima`. Si la extensión es 
"l", "lsp" o "lisp", `file_type` devuelve `lisp`. Si la extensión
no es ninguna de las anteriores, `file_type` devuelve `object`.


Véase también `pathname_type`.


Ejemplos:






```maxima
(%i2) map('file_type,["test.lisp", "test.mac", "test.dem", "test.txt"]);
(%o2)            [lisp, maxima, maxima, object]
```

<!-- category: Other -->
<!-- keywords: file_type_lisp -->
<!-- signatures: file_type_lisp -->
### Variable: file_type_lisp

Valor por defecto:  `[l, lsp, lisp]`


`file_type_lisp` es una lista con extensiones de ficheros que Maxima 
reconoce como fuente de Lisp.


Véase también `file_type`

<!-- category: Other -->
<!-- keywords: file_type_maxima -->
<!-- signatures: file_type_maxima -->
### Variable: file_type_maxima

Valor por defecto:  `[mac, mc, demo, dem, dm1, dm2, dm3, dmt]`


`file_type_maxima` es una lista con extensiones de ficheros que Maxima 
reconoce como fuente de Maxima.


Véase también `file_type`

<!-- category: Other -->
<!-- keywords: filename_merge -->
<!-- signatures: filename_merge(path, filename) -->
### Function: filename_merge (path, filename)

Construye una ruta modificada a partir de *path* y *filename*.
Si la componente final de *path* es de la forma `###.something`,
la componente se reemplaza con `filename.something`.
En otro caso, la componente final se reemplaza simplemente por *filename*.


El resultado es un objeto Lisp de tipo *pathname*.

<!-- category: Other -->
<!-- keywords: get_tex_environment, set_tex_environment -->
<!-- signatures: get_tex_environment(op), set_tex_environment(op, before, after) -->
### Function: get_tex_environment (op)

Gestiona el entorno de las salidas TeX que se obtienen de la función `tex`.
El entorno TeX está formado por dos cadenas: una que se escribe antes que
cualquier salida en TeX, y otra que se escribe después.


`get_tex_environment` devuelve el entorno TeX que se aplica al operador *op*.
Si no se ha asignado ningún entorno, devolverá el que tenga por defecto.


`set_tex_environment` asigna el entorno TeX al operador *op*.


Ejemplos:









```maxima
(%i1) get_tex_environment (":=");
(%o1) [
\begin{verbatim}
, ;
\end{verbatim}
]
(%i2) tex (f (x) := 1 - x);

\begin{verbatim}
f(x):=1-x;
\end{verbatim}

(%o2)                         false
(%i3) set_tex_environment (":=", "$$", "$$");
(%o3)                       [$$, $$]
(%i4) tex (f (x) := 1 - x);
$$f(x):=1-x$$
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: get_tex_environment_default, set_tex_environment_default -->
<!-- signatures: get_tex_environment_default(), set_tex_environment_default(before, after) -->
### Function: get_tex_environment_default ()

Gestiona el entorno de las salidas TeX que se obtienen de la función `tex`.
El entorno TeX está formado por dos cadenas: una que se escribe antes que
cualquier salida en TeX, y otra que se escribe después.


`get_tex_environment_default` devuelve el entorno TeX que se aplica
a expresiones para las cuales el operador de mayor rango no tiene entorno
TeX asignado (mediante `set_tex_environment`).


`set_tex_environment_default` asigna el entorno TeX por defecto.


Ejemplos:











```maxima
(%i1) get_tex_environment_default ();
(%o1)                       [$$, $$]
(%i2) tex (f(x) + g(x));
$$g\left(x\right)+f\left(x\right)$$
(%o2)                         false
(%i3) set_tex_environment_default ("\\begin{equation}
", "
\\end{equation}");
(%o3) [\begin{equation}
, 
\end{equation}]
(%i4) tex (f(x) + g(x));
\begin{equation}
g\left(x\right)+f\left(x\right)
\end{equation}
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: load -->
<!-- signatures: load(filename) -->
### Function: load (filename)

Evalúa las expresiones del archivo *filename*, trayendo variables,
funciones y otros objetos a Maxima. Una asignación hecha previamente a 
una variable en Maxima será destruida por otra asignación que se le 
haga en *filename*. Para encontrar el fichero, `load` llama a 
`file_search` con `file_search_maxima` y `file_search_lisp` 
como directorios de búsqueda. Si la llamada a `load` funciona correctamente, 
devuelve el nombre del fichero; en caso contrario, `load` muestra un mensaje de error.


La función `load` trabaja indistintamente con código Lisp y Maxima.
Los ficheros creados con `save`, `translate_file` y `compile_file`, 
que crea código Lisp, y `stringout`, que crea código Maxima, todos ellos 
pueden ser procesados por `load`. La función `load` llama a `loadfile` 
para cargar archivos en Lisp y a  `batchload` para cargar archivos en Maxima.


La función `load` no reconoce las construcciones de tipo `:lisp` en
ficheros de Maxima. Además, mientras se está procesando *filename*,
las variables globales `_`, `__`, `%` y `%th` mantienen los
valores que tenían cuando se realizó la llamada a `load`.


Véanse también `loadfile`, `batch`, `batchload` y `demo`;
`loadfile` procesa archivos en Lisp; `batch`, `batchload` y `demo`
procesan archivos en Maxima.


Véase `file_search` para más detalles sobre el mecanismo de búsqueda de archivos.


La función `load` evalúa sus argumentos.

<!-- category: Other -->
<!-- keywords: load_pathname -->
<!-- signatures: load_pathname -->
### Variable: load_pathname

Valor por defecto: `false`


Cuando se carga un fichero con las funciones `load`, `loadfile`
o `batchload`, a la variable `load_pathname` se le asigna la
ruta al fichero en cuestión.


Se puede acceder a la variable `load_pathname` mientras se está
cargando el fichero.


Ejemplo:


Supóngase que se tiene el fichero `test.mac` en la carpeta
`"/home/usuario/workspace/mymaxima/temp/"` con las siguientes
instrucciones:



```maxima
print("The value of load_pathname is: ", load_pathname)$
print("End of batchfile")$
```


Entonces se obtiene el siguiente resultado:



```maxima
(%i1) load("/home/usuario/workspace/mymaxima/temp/test.mac")$
The value of load_pathname is:  
                   /home/usuario/workspace/mymaxima/temp/test.mac 
End of batchfile
```

<!-- category: Other -->
<!-- keywords: loadfile -->
<!-- signatures: loadfile(filename) -->
### Function: loadfile (filename)

Evalúa las expresiones Lisp del archivo *filename*. La función
`loadfile` no llama a `file_search`, de manera que `filename` debe incluir la extensión del archivo y su ruta completa.


La función `loadfile` puede procesar ficheros creados por  `save`, `translate_file` y `compile_file`.
Puede ser más conveniente utilizar `load` en lugar de `loadfile`.

<!-- category: Other -->
<!-- keywords: loadprint -->
<!-- signatures: loadprint -->
### Variable: loadprint

Valor por defecto: `true`


La variable `loadprint` indica si mostrar un mensaje cuando se carga un archivo.



- *
Si `loadprint` vale `true`, se muestra siempre un mensaje.
- *
Si `loadprint` vale `'loadfile`, muestra un mensaje sólo si el archivo es cargado con la función `loadfile`.
- *
Si `loadprint` vale `'autoload`, muestra un mensaje sólo cuandi un archivo se carga automáticamente. Véase  `setup_autoload`.
- *
Si `loadprint` vale `false`, nunca mostrará mensajes.

<!-- category: Other -->
<!-- keywords: packagefile -->
<!-- signatures: packagefile -->
### Variable: packagefile

Valor por defecto: `false`


Los desarrolladores de paquetes que utilizan `save` o `translate`
para crear paquetes (ficheros) que van a ser utilizados por terceros pueden
hacer `packagefile: true` para evitar que se añada información a la
listas de información de Maxima, como `values` o `functions`.

<!-- category: Other -->
<!-- keywords: pathname_directory, pathname_name, pathname_type -->
<!-- signatures: pathname_directory(pathname), pathname_name(pathname), pathname_type(pathname) -->
### Function: pathname_directory (pathname)

Estas funciones devuelven las componentes de *pathname*.


Ejemplos:








```maxima
(%i1) pathname_directory("/home/usuario/maxima/changelog.txt");
(%o1)                 /home/usuario/maxima/
(%i2) pathname_name("/home/usuario/maxima/changelog.txt");
(%o2)                       changelog
(%i3) pathname_type("/home/usuario/maxima/changelog.txt");
(%o3)                          txt
```

<!-- category: Other -->
<!-- keywords: printfile -->
<!-- signatures: printfile(path) -->
### Function: printfile (path)

Envía el fichero al que hace referncia la ruta *path*
a la consola. *path* puede ser una cadena o un símbolo,
en cuyo caso se convertirá en una cadena.


Si *path* hace referencia a un fichero accesible desde el directorio
actual de trabajo, entonces se enviará a la consola; en caso contrario,
`printfile` intentará localizar el fichero añadiéndole *path*
a cada uno de los elementos de `file_search_usage` a través de 
`filename_merge`.


`printfile` devuelve la ruta del fichero encontado.

<!-- category: Other -->
<!-- keywords: save -->
<!-- signatures: save(filename, name_1, name_2, name_3, ...), save(filename, values, functions, labels, ...), save(filename, [m, n]), save(filename, name_1=expr_1, ...), save(filename, all), save(filename, name_1=expr_1, name_2=expr_2, ...) -->
### Function: save (filename, name_1, name_2, name_3, ...)

Alamacena los valores actuales de *name_1*, *name_2*, *name_3*, ..., 
en el archivo *filename*. Los argumentos son nombres de variables, funciones 
u otros objetos. Si un nombre no tiene un valor o una función asociado a él, 
entonces se ignora.


La función `save` devuelve *filename*.


La función `save` almacena datos en forma de expresiones Lisp.
Los datos almacenados por `save` pueden recuperarse con `load (filename)`.
El resultado de ejecutar  `save` cuando *filename* ya existe depende 
del soporte Lisp implementado; el archivo puede ser sobreescrito o que `save` 
envíe un mesaje de error.


La llamada `save (filename, values, functions, labels, ...)`
almacena los elementos cuyos nombres son `values`, `functions`, 
`labels`, etc. Los nombres pueden ser cualesquiera de los especificados 
por la variable `infolists`; `values` incluye todas las variables 
definidas por el usuario.


La llamada `save (filename, [m, n])` almacena los valores 
de las etiquetas de entrada y salida desde *m* hasta *n*. Nótese que 
*m* y *n* deben ser números. Las etiquetas de entrada y salida 
también se pueden almacenar una a una, por ejemplo, `save ("foo.1", %i42, %o42)`.
La llamada `save (filename, labels)` almacena todas las etiquetas de 
entrada y salida. Cuando las etiquetas almacenadas en el archivo sean posteriormente 
recuperadas, se sobreescribirán las activas en ese momento.


La llamada `save (filename, name_1=expr_1, name_2=expr_2, ...)`
almacena los valores de *expr_1*, *expr_2*, ...,
con los nombres *name_1*, *name_2*, ....
Es útil hacer este tipo de llamada para con etiquetas de entrada y salida, por ejemplo, `save ("foo.1", aa=%o88)`.
El miembro derecho de la igualdad puede ser cualquier expresión, que será evaluada.
Esta llamada a la función `save` no incorpora nuevos nombres a la sesión actual de Maxima,
simplemente los almacena en el archivo *filename*.


Todas estas formas de llamar a la función `save` se pueden combinar a voluntad.
Por ejemplo, `save (filename, aa, bb, cc=42, functions, [11, 17])`.


La llamada `save (filename, all)` almacena el estado actual de Maxima, 
lo que incluye todas las variables definidas por el usuario, funciones, arreglos, etc., 
así como algunos objetos definidos automáticamente.
Los elementos almacenados incluyen variables del sistema, como `file_search_maxima` o 
`showtime`, si han sido modificadas por el usuario. Véase `myoptions`.


`save` evalúa *filename* pero no el resto de argumentos.

<!-- category: Other -->
<!-- keywords: stringout -->
<!-- signatures: stringout(filename, expr_1, expr_2, expr_3, ...), stringout(filename, [m, n]), stringout(filename, input), stringout(filename, functions), stringout(filename, values) -->
### Function: stringout (filename, expr_1, expr_2, expr_3, ...)

La función `stringout` escribe expresiones en un archivo de la misma forma en 
que se escribirían como expresiones de entrada. El archivo puede ser 
utilizado entonces como entrada a las funciones `batch` o `demo`, y puede 
ser editado para cualquier otro propósito.


La forma general de `stringout` escribe los valores de una o más expresiones 
en el archivo de salida. Nótese que si una expresión es una variable, solamente se 
escribirá el valor de la variable y no el nombre de ésta. Como caso especial, y muy 
útil en algunas ocasiones, las expresiones pueden ser etiquetas de entrada (`%i1`, 
`%i2`, `%i3`, ...) o de salida (`%o1`, `%o2`, `%o3`, ...).


Si `grind` vale `true`, `stringout` formatea la salida utilizando `grind`. 
En caso contrario, se utilizará el formato `string`. Véanse `grind` y `string`.


La forma especial `stringout (filename, [m, n])` escribe los valores 
de las etiquetas de entrada desde la m hasta la n, ambas inclusive. 


La forma especial `stringout (filename, input)` escribe todas las etiquetas de
entrada en el archivo.


La forma especial `stringout (filename, functions)` escribe todas las funciones 
definidas por el usuario, contenidas en la lista global `functions`, en el archivo.


La forma especial `stringout (filename, values)` escribe todas las variables 
asignadas por el usuario, contenidas en la lista global `values`, en el archivo. 
Cada variable se escribe como una sentencia de asignación, con el nombre de la variable 
seguida de dos puntos y a continuación su valor. Nótese que la forma general de 
`stringout` no escribe las variables como sentencias de asignación.

<!-- category: Other -->
<!-- keywords: tex -->
<!-- signatures: tex(expr), tex(expr, destination), tex(expr, false), tex(label), tex(label, destination), tex(label, false) -->
### Function: tex (expr)

Devuelve la expresión en un formato apropiado para para ser 
incorporado a un documento basado en TeX. El resultado que se 
obtiene es un fragmento de código que puede incluirse en un documento mayor, pero que
no puede ser procesado aisladamente.


La instrucción `tex (expr)` imprime en la consola 
la representación en TeX de *expr*.


La instrucción `tex (label)` imprime en la consola la 
representación en TeX de la expresión a la que hace referencia la 
etiqueta *label*, asignándole a su vez una etiqueta de ecuación 
que será mostrada al lado izquierdo de la misma. La etiqueta de la 
expresión en TeX es la misma que la de Maxima.


*destination* puede ser tanto un flujo de salida como el nombre de un fichero.


Si *destination* es el nombre de un fichero, `tex` añade la salida al fichero.
Las funciones `openw` y `opena` crean flujos de salida.


Las instrucciones `tex (expr, false)` y `tex (label, false)`
devuelven el código TeX en formato de cadena.


La función `tex` evalúa su primer argumento tras
comprobar si se trata de una etiqueta. La doble comilla simple `''` 
fuerza la evaluación del argumento, anulando la comprobación sobre la etiqueta.


Véase también `texput`.


Ejemplos:



```maxima
(%i1) integrate (1/(1+x^3), x);
                                    2 x - 1
                  2            atan(-------)
             log(x  - x + 1)        sqrt(3)    log(x + 1)
(%o1)      - --------------- + ------------- + ----------
                    6             sqrt(3)          3
(%i2) tex (%o1);
$$-{{\log \left(x^2-x+1\right)}\over{6}}+{{\arctan \left({{2\,x-1
 }\over{\sqrt{3}}}\right)}\over{\sqrt{3}}}+{{\log \left(x+1\right)
 }\over{3}}\leqno{\tt (\%o1)}$$
(%o2)                          (\%o1)
(%i3) tex (integrate (sin(x), x));
$$-\cos x$$
(%o3)                           false
(%i4) tex (%o1, "foo.tex");
(%o4)                          (\%o1)
```


`tex (expr, false)` devuelve el código TeX en formato de cadena.







```maxima
(%i1) S : tex (x * y * z, false);
(%o1) $$x\,y\,z$$
(%i2) S;
(%o2) $$x\,y\,z$$
```

<!-- category: Other -->
<!-- keywords: tex1 -->
<!-- signatures: tex1(e) -->
### Function: tex1 (e)

Devuelve una cadena con el código TeX de la expresión *e*.
El código TeX no se encierra entre delimitadores para una ecuación
ni cualesquiera otros entornos.


Ejemplo:






```maxima
(%i1) tex1 (sin(x) + cos(x));
(%o1)                     \sin x+\cos x
```

<!-- category: Other -->
<!-- keywords: texput -->
<!-- signatures: texput(a, s), texput(a, f), texput(a, s, operator_type), texput(a, [s_1, s_2], matchfix), texput(a, [s_1, s_2, s_3], matchfix) -->
### Function: texput (a, s)

Establece el formato en TeX del átomo *a*, el cual puede ser un
símbolo o el nombre de un operador.


La instrucción `texput (a, s)` hace que la función
`tex` introduzca *s* en la salida TeX en el lugar de *a*.


La instrucción `texput (a, f)` hace que `tex` llame
a la función *f* para que genere código TeX. La función *f* 
debe aceptar un único argumento, el cual es una expresión que tenga como
operador *a* y que devuelva una cadena con el código TeX. Esta función
puede llamar a `tex1` para generar el código TeX para los argumentos
de la expresión de entrada.


La instrucción `texput (a, s, operator_type)`,
en la que *operator_type* es `prefix`, `infix` o
`postfix`, `nary` o `nofix`,hace que la función
`tex` introduzca *s* en la salida TeX en el lugar de *a*,
colocándolo en el lugar correcto.


La instrucción `texput (a, [s_1, s_2], matchfix)`
hace que la función `tex` introduzca *s_1* y *s_2* en la
salida TeX a los lados de los argumentos de *a*. Si son más de uno,
los argumentos se separan por comas.


La instrucción `texput (a, [s_1, s_2, s_3], matchfix)` hace que la función `tex` introduzca *s_1* y
*s_2* en la salida TeX a los lados de los argumentos de *a*,
con *s_3* separando los argumentos.


Ejemplos:


Asigna código TeX para una variable.






Llama a una función que genera código TeX.









```maxima
(%i1) texfoo (e) := block ([a, b], [a, b] : args (e),
  concat ("\\left[\\stackrel{", tex1 (b), 
          "}{", tex1 (a), "}\\right]"))$
(%i2) texput (foo, texfoo);
(%o2)                        texfoo
(%i3) tex (foo (2^x, %pi));
$$\left[\stackrel{\pi}{2^{x}}\right]$$
(%o3)                         false
```



```maxima
(%i1) texput (me,"\\mu_e");
(%o1)                         \mu_e
(%i2) tex (me);
$$\mu_e$$
(%o2)                         false
```


Asigna código TeX para una función ordinaria (no para un operador).







```maxima
(%i1) texput (lcm, "\\mathrm{lcm}");
(%o1)                     \mathrm{lcm}
(%i2) tex (lcm (a, b));
$$\mathrm{lcm}\left(a , b\right)$$
(%o2)                         false
```


Asigna código TeX para un operador prefijo.








```maxima
(%i1) prefix ("grad");
(%o1)                         grad
(%i2) texput ("grad", " \\nabla ", prefix);
(%o2)                        \nabla 
(%i3) tex (grad f);
$$ \nabla f$$
(%o3)                         false
```


Asigna código TeX para un operador infijo.








```maxima
(%i1) infix ("~");
(%o1)                           ~
(%i2) texput ("~", " \\times ", infix);
(%o2)                        \times 
(%i3) tex (a ~ b);
$$a \times b$$
(%o3)                         false
```


Asigna código TeX para un operador postfijo..








```maxima
(%i1) postfix ("##");
(%o1)                          ##
(%i2) texput ("##", "!!", postfix);
(%o2)                          !!
(%i3) tex (x ##);
$$x!!$$
(%o3)                         false
```


Asigna código TeX para un operador n-ario.








```maxima
(%i1) nary ("@@");
(%o1)                          @@
(%i2) texput ("@@", " \\circ ", nary);
(%o2)                         \circ 
(%i3) tex (a @@ b @@ c @@ d);
$$a \circ b \circ c \circ d$$
(%o3)                         false
```


Asigna código TeX para un operador "no-fijo".








```maxima
(%i1) nofix ("foo");
(%o1)                          foo
(%i2) texput ("foo", "\\mathsc{foo}", nofix);
(%o2)                     \mathsc{foo}
(%i3) tex (foo);
$$\mathsc{foo}$$
(%o3)                         false
```


Asigna código TeX para un operador "bi-fijo" (matchfix).













```maxima
(%i1) matchfix ("<<", ">>");
(%o1)                          <<
(%i2) texput ("<<", [" \\langle ", " \\rangle "], matchfix);
(%o2)                [ \langle ,  \rangle ]
(%i3) tex (<<a>>);
$$ \langle a \rangle $$
(%o3)                         false
(%i4) tex (<<a, b>>);
$$ \langle a , b \rangle $$
(%o4)                         false
(%i5) texput ("<<", [" \\langle ", " \\rangle ", " \\, | \\,"],
      matchfix);
(%o5)           [ \langle ,  \rangle ,  \, | \,]
(%i6) tex (<<a>>);
$$ \langle a \rangle $$
(%o6)                         false
(%i7) tex (<<a, b>>);
$$ \langle a \, | \,b \rangle $$
(%o7)                         false
```

<!-- category: Other -->
<!-- keywords: with_stdout -->
<!-- signatures: with_stdout(f, expr_1, expr_2, expr_3, ...), with_stdout(s, expr_1, expr_2, expr_3, ...) -->
### Function: with_stdout (f, expr_1, expr_2, expr_3, ...)

Evalúa  *expr_1*, *expr_2*, *expr_3*, ...
y escribe los resultados en el fichero *f* o flujo de salida *s*.
Las expresiones que se evalúan no se escriben. La salida puede generarse por medio
de `print`, `display`, `grind` entre otras funciones.


La variable global `file_output_append` controla si `with_stdout`
añade o reinicia el contenido del fichero de salida *f*.
Si `file_output_append` vale `true`, `with_stdout` añade
contenido al fichero de salida. En cualquier caso, `with_stdout`
crea el fichero si éste no existe.


La función `with_stdout` devuelve el valor de su último argumento.


Véase también `writefile`.








```maxima
(%i1) with_stdout ("tmp.out", 
                   for i:5 thru 10 do print (i, "! yields", i!))$
(%i2) printfile ("tmp.out")$
5 ! yields 120 
6 ! yields 720 
7 ! yields 5040 
8 ! yields 40320 
9 ! yields 362880 
10 ! yields 3628800
```

<!-- category: Other -->
<!-- keywords: writefile -->
<!-- signatures: writefile(filename) -->
### Function: writefile (filename)

Comienza escribiendo una transcripción de la sesión de Maxima en el archivo *filename*.
Cualquier interacción entre Maxima y el usuario se almacena también en este archivo, tal como aparece en la consola.


Puesto que la transcripción se escribe en el formato de salida a la consola, su contenido no es interpretable por Maxima.
Para hacer un archivo que contenga expresiones que puedan ser nuevamente cargadas en Maxima, véanse `save` y `stringout`; la función `save` almacena expresiones en formato Lisp, mientras que `stringout` lo hace en formato Maxima.


El resultado de ejecutar `writefile` cuando el archivo *filename* ya existe depende del entorno Lisp operativo; el contenido anterior puede ser sobreescrito o ampliado con la sesión actual. La función `appendfile` siempre añade la sesión al contenido actual.


Puede ser útil ejecutar `playback` después de `writefile` para guardar las interacciones previas de la sesión. Puesto que  `playback` muestra solamente las variables de entrada y salida (`%i1`, `%o1`, etc.),
cualquier salida generada por una sentencia de impresión desde dentro de una función no es mostrada por `playback`.


La función `closefile` cierra los archivos abiertos por `writefile` o `appendfile`.

