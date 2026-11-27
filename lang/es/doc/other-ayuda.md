## Ayuda

<!-- category: Other -->
<!-- keywords: apropos -->
<!-- signatures: apropos(string) -->
### Function: apropos (string)

Busca los símbolos de Maxima en los cuales aparezca 
*cadena* en cualquier lugar dentro de su nombre. Así, 
`apropos (exp)` devuelve una lista con todas las variables y 
funciones que tengan  `exp` formando parte de sus nombres, 
como  `expand`, `exp` y `exponentialize`. 
De esta forma, si el usuario tan solo recuerda parte del nombre de algo, 
puede utilizar este comando para encontrar el resto del nombre. 
De manera semejante, también se puede hacer `apropos (tr_)` 
para encontrar una lista de muchas de las variables relacionadas 
con el traductor, buena parte de las cuales comienzan con `tr_`.


`apropos("")` devuelve una lista con todos los nombres de Maxima. 


En caso de no encontrar información relevante, `apropos` 
devuelve la lista vacía `[]`.


Ejemplo:


Devuelve todos los símbolos de Maxima que
contienen la subcadena `"gamma"` en su nombre:






```maxima
(%i1) apropos("gamma");
(%o1) [%gamma, gamma, gammalim, gamma_expand, gamma_incomplete_lower, 
gamma_incomplete, gamma_incomplete_generalized, 
gamma_incomplete_regularized, Gamma, log_gamma, makegamma, 
prefer_gamma_incomplete, 
gamma_incomplete_generalized_regularized]
```

<!-- category: Other -->
<!-- keywords: demo -->
<!-- signatures: demo(archivo) -->
### Function: demo (archivo)

Evalua las expresiones Maxima contenidas en *archivo* y muestra los resultados. 
`demo` hace pausas después de evaluar  cada expresión
y continua después de que el usuario ingrese un retorno de carro. 
(Si se ejecuta en Xmaxima, `demo` puede que necesite un punto y coma
`;` a continuación del retorno de carro.)


`demo` busca la lista de directorios 
`file_search_demo` para encontrar `archivo`.
Si el archivo tiene el sufijo `dem`, 
el sufijo puede ser omitido. 
Ver también `file_search`.


`demo` evalua su argumento. 
`demo` retorna el nombre del archivo demostración. 


Ejemplo:



```maxima
(%i1) demo ("disol");

batching /home/wfs/maxima/share/simplification/disol.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i2)                      load("disol")

_
(%i3)           exp1 : a (e (g + f) + b (d + c))
(%o3)               a (e (g + f) + b (d + c))

_
(%i4)                disolate(exp1, a, b, e)
(%t4)                         d + c

(%t5)                         g + f

(%o5)                   a (%t5 e + %t4 b)

_
(%i5) demo ("rncomb");

batching /home/wfs/maxima/share/simplification/rncomb.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i6)                     load("rncomb")

_
                             z         x
(%i7)               exp1 : ----- + ---------
                           y + x   2 (y + x)
                          z         x
(%o7)                   ----- + ---------
                        y + x   2 (y + x)

_
(%i8)                     combine(exp1)
                          z         x
(%o8)                   ----- + ---------
                        y + x   2 (y + x)

_
(%i9)                     rncombine(%)
                             2 z + x
(%o9)                       ---------
                            2 (y + x)

_
                             d   c   b   a
(%i10)                exp2 : - + - + - + -
                             3   3   2   2
                          d   c   b   a
(%o10)                    - + - + - + -
                          3   3   2   2

_
(%i11)                    combine(exp2)
                      2 d + 2 c + 3 (b + a)
(%o11)                ---------------------
                                6

_
(%i12)                   rncombine(exp2)
                      2 d + 2 c + 3 b + 3 a
(%o12)                ---------------------
                                6

_
(%i13)
```

<!-- category: Other -->
<!-- keywords: describe -->
<!-- signatures: describe(string), describe(string, exact), describe(string, inexact) -->
### Function: describe (string)

La sentencia `describe(string)` equivale a `describe(string, exact)`.


La sentencia `describe(string, exact)` encuentra el elemento, si
existe, cuyo título coincide exactamente con *string*
(ignorando la diferencia entre mayúsculas y minúsculas).


La sentencia `describe(string, inexact)` encuentra todos los elementos
documentados que contengan *string* en sus títulos.


Si hay más de una opción, Maxima preguntará al usuario para que
seleccione las opciones que desee consultar.


La sentencia `? foo` (con espacio entre `?` y `foo`)
equivale a  `describe("foo", exact)`, mientras que `?? foo`
equivale a `describe("foo", inexact)`.


`describe ("", inexact)` produce una lista de todos los temas documentados en
el manual en línea. 


`describe` no evalúa su argumento. La función `describe` devuelve
`true` si encuentra la documentación solicitada y `false` en caso
contrario.


Véase también `Documentación`.


Ejemplo:



```maxima
(%i1) ?? integ
 0: Functions and Variables for Elliptic Integrals
 1: Functions and Variables for Integration
 2: Introduction to Elliptic Functions and Integrals
 3: Introduction to Integration
 4: askinteger  (Functions and Variables for Simplification)
 5: integerp  (Functions and Variables for Miscellaneous Options)
 6: integer_partitions  (Functions and Variables for Sets)
 7: integrate  (Functions and Variables for Integration)
 8: integrate_use_rootsof  (Functions and Variables for
    Integration)
 9: integration_constant_counter  (Functions and Variables for
    Integration)
 10: nonnegintegerp  (Functions and Variables for linearalgebra)
Enter space-separated numbers, `all' or `none': 7 8

 -- Function: integrate (<expr>, <x>)
 -- Function: integrate (<expr>, <x>, <a>, <b>)
     Attempts to symbolically compute the integral of <expr> with
     respect to <x>.  `integrate (<expr>, <x>)' is an indefinite
     integral, while `integrate (<expr>, <x>, <a>, <b>)' is a
     definite integral, [...]
     
 -- Option variable: integrate_use_rootsof
     Default value: `false'

     When `integrate_use_rootsof' is `true' and the denominator of
     a rational function cannot be factored, `integrate' returns
     the integral in a form which is a sum over the roots (not yet
     known) of the denominator.
     [...]
```


En este ejemplo fueron seleccionadas las opciones 7 y 8 
(la salida ha sido recortada, tal como indica `[...]`).
Todas o ninguna de las opciones pueden ser seleccionadas escribiendo
`all` o `none`, las cuales pueden ser abreviadas por
`a` o `n`, respectivamente.

<!-- category: Other -->
<!-- keywords: example -->
<!-- signatures: example(topic), example() -->
### Function: example (topic)

`example (topic)` muestra algunos ejemplos sobre *topic*,
el cual debe ser un símbolo o cadena de texto. Para ver
ejemplos sobre operadores como `if`, `do` o `lambda`
el argumento debe ser necesariamente una cadena de texto, como
`example ("do")`. La función `example` no distingue entre minúsculas
y mayúsculas. La mayor parte de ejemplos versan sobre funciones.


La sentencia `example ()` devuelve la lista de todos los ejemplos
existentes.


El nombre del fichero que contine los ejemplos existentes se guarda en
la variable global `manual_demo`, cuyo valor por defecto es
`"manual.demo"`.


La función `example` no evalúa su argumento.


Ejemplos:








```maxima
(%i1) example(append);
(%i2) append([x+y,0,-3.2],[2.5E+20,x])
(%o2)                    [y + x, 0, - 3.2, 2.5E+20, x]
(%o2)                                done
(%i3) example("lambda");
(%i4) lambda([x,y,z],z^2+y^2+x^2)
                                           2    2    2
(%o4)                   lambda([x, y, z], z  + y  + x )
(%i5) %(1,2,a)
                                     2
(%o5)                               a  + 5
(%i6) a+2+1
(%o6)                                a + 3
(%o6)                                done
(%i7) example("allROOTS");
(%i8) (1+2*x)^3 = 13.5*(1+x^5)
                                   3          5
(%o8)                     (2 x + 1)  = 13.5 (x  + 1)
(%i9) allroots(%)
(%o9) [x = .8296749902129361, x = - 1.015755543828121, 
x = .9659625152196369 %i - .4069597231924075, 
x = - .9659625152196369 %i - .4069597231924075, x = 1.0]
(%o9)                                done
```

<!-- category: Other -->
<!-- keywords: manual_demo -->
<!-- signatures: manual_demo -->
### Variable: manual_demo

Valor por defecto: `"manual.demo"`


`manual_demo` especifica el nombre del fichero que contiene
los ejemplo para la función `example`. 


Véase `example`.

