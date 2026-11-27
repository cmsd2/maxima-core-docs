## Depurado

<!-- category: Other -->
<!-- keywords: debugmode -->
<!-- signatures: debugmode -->
### Variable: debugmode

Valor por defecto: `false`


Cuando en Maxima ocurre un error, Maxima inicializará el depurador si `debugmode` tiene el valor `true`. 
El usuario puede ingresar comandos para examinar la pila de llamadas, los puntos de interrupción; en pocas palabras ir a través del código de Maxima. Vea `debugging` para una lista de los comandos del depurador.  


Habilitando `debugmode` no se capturarán los errores tipo Lisp.

<!-- category: Other -->
<!-- keywords: refcheck -->
<!-- signatures: refcheck -->
### Variable: refcheck

Valor por defecto: `false`


Cuando `refcheck` vale `true`, Maxima imprime un mensaje cada vez que una variable es utilizada por vez primera en un cálculo.

<!-- category: Other -->
<!-- keywords: setcheck -->
<!-- signatures: setcheck -->
### Variable: setcheck

Valor por defecto: `false`


Cuando el valor de `setcheck` es una lista de variables (se admite que tengan subíndices) Maxima devuelve un mensaje indicando si los valores que han sido asignados a las variables lo han sido con el operador ordinario `:`, o con el operador de asignación `::` o como resultado de haberse realizado una llamada de función, pero en ningún caso cuando la asignación haya sido hecha mediante los operadores `:=` o `::=`. El mensaje contiene el nombre de la variable y su valor.


La variable `setcheck` admite también los valores `all` o `true` con lo que el informe incluirá todas las variables.


Cada nueva asignación de `setcheck` establece una nueva lista de variables a ser monitorizada, de forma que cualquier otra variable previamente asignada a `setcheck` es olvidada.


Los nombres asignados a `setcheck` deben estar precedidos del apóstrofo `'` a fin de evitar que las variables sean evaluadas antes de ser almacenadas en `setcheck`. Por ejemplo, si `x`, `y` y `z` ya guardan algún valor entoces se hará



```maxima
setcheck: ['x, 'y, 'z]$
```


para colocarlas en la lista de variables a monitorizar.


No se generará ninguna salida cuando una variable de la lista `setcheck` sea asignada a ella misma, como en `X: 'X`.

<!-- category: Other -->
<!-- keywords: setcheckbreak -->
<!-- signatures: setcheckbreak -->
### Variable: setcheckbreak

Valor por defecto: `false`


Si `setcheckbreak` es igual `true`, Maxima se detendrá siempre que a una variable de la lista `setcheck` se le asigne un nuevo valor. La detención tendrá lugar justo antes de hacerse la asignación. En ese momento `setval` guarda el valor que se le va a dar a la variable. Entonces el usuario podrá darle un valor diferente pasándoselo a la variable `setval`.


Véanse también `setcheck` y `setval`.

<!-- category: Other -->
<!-- keywords: setval -->
<!-- signatures: setval -->
### Variable: setval

Guarda el valor que va a ser asignado a una variable cuando `setcheckbreak` realiza una detención. Entonces se podrá asignarle otro valor pasándoselo previamente a `setval`.


Véanse también `setcheck` y `setcheckbreak`.

<!-- category: Other -->
<!-- keywords: timer -->
<!-- signatures: timer(f_1, ..., f_n), timer(all), timer() -->
### Function: timer (f_1, ..., f_n)

Dadas las funciones *f_1*, ..., *f_n*, `timer` coloca cada una de ellas en la lista de funciones para las cuales se generarán estadísticas relativas al tiempo de cómputo. Así, `timer(f)$ timer(g)$` coloca a `f` y luego a `g` en dicha lista de forma acumulativa.


La sentencia `timer(all)` coloca todas las funciones de usuario 
(las referenciadas por la variable global `functions`) en la lista
de funciones cuyos tiempos de ejecución se quieren monitorizar.


Si no se le pasan argumentos a `timer` se obtendrá la lista de funciones cuyos tiempos de ejecución se quieren monitorizar.


Maxima almacena la duración del cómputo de cada función de la lista, de forma que `timer_info` devolverá las estadísticas correspondientes, incluyendo el tiempo medio de cada llamada a la función, el número de llamadas realizadas y el tiempo total transcurrido. La instrucción `untimer` borra las funciones de la lista.


La función `timer` no evalúa sus argumentos, de forma que `f(x) := x^2$ g:f$ timer(g)$` no coloca a `f` en la lista.


Si `trace(f)` está activada, entonces `timer(f)` está desactivada; `trace` y `timer` no pueden estar operativas al mismo tiempo.


Véase también `timer_devalue`.

<!-- category: Other -->
<!-- keywords: timer_devalue -->
<!-- signatures: timer_devalue -->
### Variable: timer_devalue

Valor por defecto: `false`


Si `timer_devalue` es igual a `true`, Maxima le resta a cada función cuyos tiempos de ejecución se quiere monitorizar el tiempo gastado en llamadas a otras funciones presentes también en la lista de monitorización. En caso contrario, los tiempos que se obtienen para cada función incluyen también los consumidos en otras funciones. Nótese que el tiempo consumido en llamadas a otras funciones que no están en la lista de monitorización no se resta del tiempo total.


Véanse también `timer` y `timer_info`.

<!-- category: Other -->
<!-- keywords: timer_info -->
<!-- signatures: timer_info(f_1, ..., f_n), timer_info() -->
### Function: timer_info (f_1, ..., f_n)

Dadas las funciones *f_1*, ..., *f_n*, `timer_info` devuelve una matriz con información relativa a los tiempos de ejecución de cada una de estas funciones. Sin argumentos, `timer_info` devuelve la información asociada a todas las funciones cuyos tiempos de ejecución se quiere monitorizar.


La matriz devuelta por `timer_info` incluye los nombres de las funciones, tiempo de ejecución en cada llamada, número de veces que ha sido llamada, tiempo total de ejecución y tiempo consumido en la recolección de basura, `gctime` (del inglés, "garbage collection time") en la versión original de Macsyma, aunque ahora toma el valor constante cero.


Los datos con los que `timer_info` construye su respuesta pueden obtenerse también con la función `get`:



```maxima
get(f, 'calls);  get(f, 'runtime);  get(f, 'gctime);
```


Véase también `timer`.

<!-- category: Other -->
<!-- keywords: trace -->
<!-- signatures: trace(f_1, ..., f_n), trace(all), trace() -->
### Function: trace (f_1, ..., f_n)

Dadas las funciones *f_1*, ..., *f_n*, `trace` imprime información sobre depuración cada vez que estas funciones son llamadas; `trace(f)$ trace(g)$` coloca de forma acumulativa a `f` y luego a `g` en la lista de funciones a ser rastradas.


La sentencia `trace(all)` coloca todas las funciones de usuario 
(las referenciadas por la variable global `functions`) en la lista
de funciones a ser rastreadas.


Si no se suministran argumentos, `trace` devuelve una lista con todas las funciones a ser rastreadas.


La función `untrace` desactiva el rastreo. Véase también `trace_options`.


La función `trace` no evalúa sus argumentos, de forma que `f(x) := x^2$ g:f$ trace(g)$` no coloca a `f` en la lista de rastreo.


Cuando una función se redefine es eliminada de la lista de rastreo. Así, tras  `timer(f)$ f(x) := x^2$`, la función `f` dejará de estar en dicha lista.


Si `timer (f)` está activado, entonces `trace (f)` está desactivado, ya que `trace` y `timer` no pueden estar ambos activos para la misma función.

<!-- category: Other -->
<!-- keywords: trace_options -->
<!-- signatures: trace_options(f, option_1, ..., option_n), trace_options(f) -->
### Function: trace_options (f, option_1, ..., option_n)

Establece las opciones de rastreo para la función *f*. Cualquier otra opción previamente especificada queda reemplazada por las nuevas. La ejecución de `trace_options (f, ...)` no tiene ningún efecto, a menos que se haya invocado previamente a `trace (f)` (es indiferente que esta invocación sea anterior o posterior a `trace_options`). 


`trace_options (f)` inicializa todas las opciones a sus valores por defecto.


Las claves de opciones son:



- *
`noprint`:
No se imprime mensaje alguno ni a la entrada ni a la salida de la función.
- *
`break`:
Coloca un punto de referencia antes de que la función comience a ejecutarse y otro después de que termine su ejecución. Véase `break`.
- *
`lisp_print`:
Muestra los argumentos y valores retornados como objetos de Lisp.
- *
`info`:
Imprime `-> true` tanto a la entrada como a la salida de la función.
- *
`errorcatch`:
Detecta errores, otorgando la posibilidad de marcar un error, reintentar la llamada a la función o especificar un valor de retorno.


Las opciones de rastreo se especifican de dos formas. La única presencia de la clave de opción ya activa la opción. (Nótese que la opción *foo* no se activa mediante `foo: true` u otra forma similar; se tendrá en cuenta también que las claves no necesitan ir precedidas del apóstrofo.) Especificando la clave de opción junto con una función de predicado se hace que la opción quede condicionada al predicado.


La lista de argumentos para las funciones de predicado es siempre `[level, direction, function, item]` donde `level` es el nivel de recursión para la función,  `direction` puede ser tanto `enter` como `exit`, `function` es el nombre de la función  y `item` es la lista de argumentos (a la entrada) o el valor de retorno (a la salida).


A continuación un ejemplo de opciones de rastreo no condicionales:



```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1)$

(%i2) trace (ff)$

(%i3) trace_options (ff, lisp_print, break)$

(%i4) ff(3);
```


Para la misma función, con la opción `break` condicionada a un predicado:



```maxima
(%i5) trace_options (ff, break(pp))$

(%i6) pp (level, direction, function, item) := block (print (item),
    return (function = 'ff and level = 3 and direction = exit))$

(%i7) ff(6);
```

<!-- category: Other -->
<!-- keywords: untimer -->
<!-- signatures: untimer(f_1, ..., f_n), untimer() -->
### Function: untimer (f_1, ..., f_n)

Dadas las funciones *f_1*, ..., *f_n*, `untimer` las elimina de la lista de funciones cuyos tiempos de ejecución se quiere monitorizar.


Si no se le suministran argumentos, `untimer` borra completamente la lista.


Tras la ejecución de `untimer (f)`, `timer_info (f)` aún devuelve las estadísticas de tiempo previamente registradas, pero `timer_info()` (sin argumentos) no devuelve información sobre aquellas funciones que ya no están en la lista. La ejecución de `timer (f)` inicializa todas las estadísticas a cero y coloca `f` nuevamente en la lista.

<!-- category: Other -->
<!-- keywords: untrace -->
<!-- signatures: untrace(f_1, ..., f_n), untrace() -->
### Function: untrace (f_1, ..., f_n)

Dadas las funciones *f_1*, ..., *f_n*,
`untrace` desactiva el rastreo previamente activado por la función `trace`. Si no se aportan argumentos, `untrace` desactiva el rastreo de todas las funciones.


La llamada a `untrace` devuelve una lista con las funciones para las que el rastreo se ha desactivado.

