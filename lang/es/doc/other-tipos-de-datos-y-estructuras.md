## Tipos de datos y estructuras

<!-- category: Other -->
<!-- keywords: @ -->
<!-- signatures: @ -->
### Function: @

`@` es el operador para acceder a los campos de las estructuras.


La expresión `x@ a` hace referencia al valor del
campo *a* del individuo *x* de una estructura dada. El nombre del campo no se evalúa.


Si el campo *a* de *x* no tiene valor asignado, `x@ a`
se evalúa a sí mismo; es decir, devuelve la propia expresión
`x@ a` tal cual.


La sentencia `kill(x@ a)` elimina el valor del campo *a* de *x*.


Ejemplos:













```maxima
(%i1) defstruct (foo (x, y, z));
(%o1)                    [foo(x, y, z)]
(%i2) u : new (foo (123, a - b, %pi));
(%o2)           foo(x = 123, y = a - b, z = %pi)
(%i3) u@z;
(%o3)                          %pi
(%i4) u@z : %e;
(%o4)                          %e
(%i5) u;
(%o5)            foo(x = 123, y = a - b, z = %e)
(%i6) kill (u@z);
(%o6)                         done
(%i7) u;
(%o7)              foo(x = 123, y = a - b, z)
(%i8) u@z;
(%o8)                          u@z
```


El nombre del campo no se evalúa.













```maxima
(%i1) defstruct (bar (g, h));
(%o1)                      [bar(g, h)]
(%i2) x : new (bar);
(%o2)                       bar(g, h)
(%i3) x@h : 42;
(%o3)                          42
(%i4) h : 123;
(%o4)                          123
(%i5) x@h;
(%o5)                          42
(%i6) x@h : 19;
(%o6)                          19
(%i7) x;
(%o7)                    bar(g, h = 19)
(%i8) h;
(%o8)                          123
```

<!-- category: Other -->
<!-- keywords: bfloat -->
<!-- signatures: bfloat(expr) -->
### Function: bfloat (expr)

Convierte todos los números y  funciones numéricas a números decimales de punto flotante grandes ("bigfloats").
El número de dígitos significativos de los "bigfloats" resultantes se especifica mediante la variable global `fpprec`.


Si `float2bf` vale `false` se mostrará un mensaje de aviso cuando un número en punto flotante se convierte a decimal de tipo "bigfloats", puesto que tal transformación puede conllevar pérdida de precisión.

<!-- category: Other -->
<!-- keywords: bfloatp -->
<!-- signatures: bfloatp(expr) -->
### Function: bfloatp (expr)

Devuelve `true` si *expr* es un número decimal en punto flotante grande ("bigfloats"), en caso contrario devuelve `false`.

<!-- category: Other -->
<!-- keywords: bftorat -->
<!-- signatures: bftorat -->
### Variable: bftorat

Valor por defecto: `false`


La variable `bftorat` controla la conversión de números decimales de punto flotante grandes ("bigfloats") a números racionales. Si `bftorat` vale `false`, se utilizará `ratepsilon` para controlar la conversión  (lo cual resulta en números racionales relativamente pequeños). Si  `bftorat` vale `true`, el número racional generado representará exactamente al número decimal de punto flotante grande ("bigfloat").

<!-- category: Other -->
<!-- keywords: bftrunc -->
<!-- signatures: bftrunc -->
### Variable: bftrunc

Valor por defecto: `true`


La variable `bftrunc` provoca la eliminación de ceros en números decimales grandes no nulos para que no se muestren.  Así, si `bftrunc` vale `false`, `bfloat (1)`
se muestra como `1.000000000000000B0`. En otro caso, se mostrará como `1.0B0`.

<!-- category: Other -->
<!-- keywords: concat -->
<!-- signatures: concat(arg_1, arg_2, ...) -->
### Function: concat (arg_1, arg_2, ...)

Concatena sus argumentos, que deben ser todos átomos.
El valor devuelto es un símbolo si el primer argumento es a su vez un símbolo, o una cadena en caso contrario.


La función `concat` evalúa sus argumentos.
El apátrofo  `'` evita la evaluación.



```maxima
(%i1) y: 7$
(%i2) z: 88$
(%i3) concat (y, z/2);
(%o3)                          744
(%i4) concat ('y, z/2);
(%o4)                          y44
```


A un símbolo construido por `concat` se le puede asignar un valor y ser utilizado posteriormente en expresiones.
La asignación con el operador `::` evalúa su expresión izquierda.



```maxima
(%i5) a: concat ('y, z/2);
(%o5)                          y44
(%i6) a:: 123;
(%o6)                          123
(%i7) y44;
(%o7)                          123
(%i8) b^a;
                               y44
(%o8)                         b
(%i9) %, numer;
                               123
(%o9)                         b
```


Nótese que aunque `concat (1, 2)` parezca un número, se trata de una cadena.



```maxima
(%i10) concat (1, 2) + 3;
(%o10)                       12 + 3
```

<!-- category: Other -->
<!-- keywords: defstruct -->
<!-- signatures: defstruct(S(a_1, ..., a_n)), defstruct(S(a_1=v_1, ..., a_n=v_n)) -->
### Function: defstruct (S(a_1, ..., a_n))

Define una estructura, la cual es una lista de nombres de campos *a_1*, ..., *a_n*
asociados a un símbolo *S*.
Todo individuo de una estructura dada consiste en una expresión con operador *S*
y exactamente `n` argumentos. La sentencia `new(S)` crea un nuevo
individuo con estructura *S*.


Un argumento consistente en un símbolo *a* especifica el nombre de
un campo. Un argumento consistente en una ecuación `a = v` especifica
el nombre del campo *a* junto con su valor por defecto *v*. El valor por
defecto puede ser cualquier tipo de expresión.


La llamada a `defstruct` añade *S* a la lista de estructuras definidas
por el usuario, `structures`.


La sentencia `kill(S)` borra *S* de la lista de estructuras
definidas por el usuario y elimina la definición de la estructura.


Ejemplos:













```maxima
(%i1) defstruct (foo (a, b, c));
(%o1)                    [foo(a, b, c)]
(%i2) structures;
(%o2)                    [foo(a, b, c)]
(%i3) new (foo);
(%o3)                     foo(a, b, c)
(%i4) defstruct (bar (v, w, x = 123, y = %pi));
(%o4)             [bar(v, w, x = 123, y = %pi)]
(%i5) structures;
(%o5)      [foo(a, b, c), bar(v, w, x = 123, y = %pi)]
(%i6) new (bar);
(%o6)              bar(v, w, x = 123, y = %pi)
(%i7) kill (foo);
(%o7)                         done
(%i8) structures;
(%o8)             [bar(v, w, x = 123, y = %pi)]
```

<!-- category: Other -->
<!-- keywords: evenp -->
<!-- signatures: evenp(expr) -->
### Function: evenp (expr)

Devuelve `true` si *expr* es un entero par y `false` en cualquier otro caso.

<!-- category: Other -->
<!-- keywords: float -->
<!-- signatures: float(expr) -->
### Function: float (expr)

Convierte los enteros, números racionales y los decimales de punto flotante grandes ("bigfloats") que están presentes en *expr* a números de punto flotante. También actúa como símbolo `evflag`.

<!-- category: Other -->
<!-- keywords: float2bf -->
<!-- signatures: float2bf -->
### Variable: float2bf

Valor por defecto: `true`

 

Si `float2bf` vale `false` se mostrará un mensaje de aviso cuando un número
en punto flotante se convierte a decimal de tipo "bigfloats", puesto que tal transformación
puede conllevar pérdida de precisión.

<!-- category: Other -->
<!-- keywords: floatnump -->
<!-- signatures: floatnump(expr) -->
### Function: floatnump (expr)

Devuelve `true` si *expr* es un número de punto flotante, en caso contario retorna `false`.

<!-- category: Other -->
<!-- keywords: fpprec -->
<!-- signatures: fpprec -->
### Variable: fpprec

Valor por defecto: 16


La variable `fpprec` guarda el número de dígitos significativos en la aritmética con números decimales de punto flotante grandes ("bigfloats"). La variable `fpprec` no afecta a los cálculos con números decimales de punto flotante ordinarios.


Véanse también `bfloat` y `fpprintprec`.

<!-- category: Other -->
<!-- keywords: fpprintprec -->
<!-- signatures: fpprintprec -->
### Variable: fpprintprec

Valor por defecto: 0


La variable `fpprintprec` guarda el número de dígitos
a imprimir de los números decimales en coma flotante, tanto los ordinarios
como los de precisión ilimitada (*bigfloats*).


En el caso de los decimales ordinarios, si `fpprintprec` toma un valor
entre 2 y 16 (inclusive), el número de dígitos que se 
imprimen es igual a `fpprintprec`. En caso contrario, `fpprintprec` es 0
o mayor que 16, siendo el número de dígitos
a imprimir en todos loa casos igual a 16.


En el caso de los decimales de precisión ilimitada (*bigfloats*),
si `fpprintprec` toma un valor entre 2 y 16 (inclusive),
el número de dígitos que se imprimen es igual a 
`fpprintprec`. En caso contrario, `fpprintprec` es 0
o mayor que `fpprec`, siendo el número de dígitos
a imprimir igual a `fpprec`.


La variable `fpprintprec` no admite el valor 1.

<!-- category: Other -->
<!-- keywords: integerp -->
<!-- signatures: integerp(expr) -->
### Function: integerp (expr)

Devuelve `true` si *expr* es un número entero y `false` en cualquier otro caso.


La función `integerp` devuelve `false` si su argumento es un símbolo, incluso cuando éste ha sido declarado como entero.


Ejemplos:



```maxima
(%i1) integerp (0);
(%o1)                         true
(%i2) integerp (1);
(%o2)                         true
(%i3) integerp (-17);
(%o3)                         true
(%i4) integerp (0.0);
(%o4)                         false
(%i5) integerp (1.0);
(%o5)                         false
(%i6) integerp (%pi);
(%o6)                         false
(%i7) integerp (n);
(%o7)                         false
(%i8) declare (n, integer);
(%o8)                         done
(%i9) integerp (n);
(%o9)                         false
```

<!-- category: Other -->
<!-- keywords: m1pbranch -->
<!-- signatures: m1pbranch -->
### Variable: m1pbranch

Valor por defecto: `false`


La variable `m1pbranch` es la rama principal de `-1` elevado a una potencia. Cantidades como `(-1)^(1/3)` (esto es, un exponente racional impar) y `(-1)^(1/4)` (esto es, un exponente racional par) son tratados como sigue:




```maxima
dominio real
                            
(-1)^(1/3):      -1         
(-1)^(1/4):   (-1)^(1/4)   

             dominio complejo              
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```

<!-- category: Other -->
<!-- keywords: new -->
<!-- signatures: new(S), new(S(v_1, ..., v_n)) -->
### Function: new (S)

`new` crea nuevos individuos de estructuras declaradas.


La sentencia `new(S)` crea un nuevo individuo de 
estructura *S* en el que cada campo toma su valor por defecto,
si este fue definido, o sin valor alguno en caso de que no se haya
fijado un valor por defecto en la definición de la estructura.


La sentencia `new(S(v_1, ..., v_n))`
crea un nuevo individuo de estructura *S* en el que los campos
adquieren los valores *v_1*, ..., *v_n*.


Ejemplos:








```maxima
(%i1) defstruct (foo (w, x = %e, y = 42, z));
(%o1)              [foo(w, x = %e, y = 42, z)]
(%i2) new (foo);
(%o2)               foo(w, x = %e, y = 42, z)
(%i3) new (foo (1, 2, 4, 8));
(%o3)            foo(w = 1, x = 2, y = 4, z = 8)
```

<!-- category: Other -->
<!-- keywords: nonnegintegerp -->
<!-- signatures: nonnegintegerp(n) -->
### Function: nonnegintegerp (n)

Devuelve `true` si y solo si `n >= 0`, siendo *n* un entero.

<!-- category: Other -->
<!-- keywords: numberp -->
<!-- signatures: numberp(expr) -->
### Function: numberp (expr)

Devuelve `true` si *expr* es un enúmero entero, racional, 
de coma flotante o "bigfloat", en caso contrario devuelve `false`.


La función `numberp` devuelve `false` si su argumento es un símbolo, incluso cuando el argumento es un número simbólico como `%pi` o `%i`, o aunque haya sido declarado como `even` (par), `odd` (impar), `integer` (entero), `rational` (racional), `irrational` (irracional), `real` (real), `imaginary` (imaginario) o `complex` (complejo).


Ejemplos:



```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare (a, even, b, odd, c, integer, d, rational,
     e, irrational, f, real, g, imaginary, h, complex);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e, f, g, h]);
(%o7) [false, false, false, false, false, false, false, false]
```

<!-- category: Other -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

La variable `numer` hace algunas funciones matemáticas
con argumentos numéricos se evalúen como decimales de punto flotante.
También hace que las variables de una expresión a las cuales se les ha
asignado un número sean sustituidas por sus valores.
Además, activa la variable `float`.


Véase también `%enumer`.


Ejemplos:







```maxima
(%i1) [sqrt(2), sin(1), 1/(1+sqrt(3))];
                                               1
(%o1)                   [sqrt(2), sin(1), -----------]
                                          sqrt(3) + 1
(%i2) [sqrt(2), sin(1), 1/(1+sqrt(3))],numer;
(%o2) [1.414213562373095, .8414709848078965, .3660254037844387]
```

<!-- category: Other -->
<!-- keywords: numer_pbranch -->
<!-- signatures: numer_pbranch -->
### Variable: numer_pbranch

Valor por defecto: `false`


La variable opcional `numer_pbranch` controla la evaluación
numérica de las potencias de números enteros, racionales y
decimales negativos. Si `numer_pbranch` vale `true` y el
exponente es decimal o la variable opcional `numer` vale 
`true`, Maxima evalúa el resultado numérico utilizando la rama
principal. En caso contrario, se devuleve un resultado simplificado pero
no evaluado.


Ejemplos:










```maxima
(%i1) (-2)^0.75;
(%o1) (-2)^0.75

(%i2) (-2)^0.75,numer_pbranch:true;
(%o2) 1.189207115002721*%i-1.189207115002721

(%i3) (-2)^(3/4);
(%o3) (-1)^(3/4)*2^(3/4)

(%i4) (-2)^(3/4),numer;
(%o4) 1.681792830507429*(-1)^0.75

(%i5) (-2)^(3/4),numer,numer_pbranch:true;
(%o5) 1.189207115002721*%i-1.189207115002721
```

<!-- category: Other -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, expr_1, ..., var_n, expr_n) -->
### Function: numerval (x_1, expr_1, ..., var_n, expr_n)

Declara las variables `x_1`, ..., *x_n* asignándoles los valores numéricos `expr_1`, ..., `expr_n`.
El valor numérico se evalúa y sustituye a la variable en cualquier expresión en la que ésta aparezca si `numer` toma el valor `true`. Véase también `ev`.


Las expresiones `expr_1`, ..., `expr_n` pueden ser expresiones no necesariamente numéricas.

<!-- category: Other -->
<!-- keywords: oddp -->
<!-- signatures: oddp(expr) -->
### Function: oddp (expr)

Devuelve `true` si *expr* es un entero impar y `false` en caso contrario.

<!-- category: Other -->
<!-- keywords: ratepsilon -->
<!-- signatures: ratepsilon -->
### Variable: ratepsilon

Valor por defecto: 2.0e-8


La variable `ratepsilon` guarda la tolerancia utilizada en la conversión de números decimales en coma flotante a números racionales.

<!-- category: Other -->
<!-- keywords: rationalize -->
<!-- signatures: rationalize(expr) -->
### Function: rationalize (expr)

Convierte todos los números en coma flotante de doble precisión y grandes (big float) presentes en una expresión *expr* de Maxima a sus formas racionales exactas equivalentes. Si el usuario no está familiarizado con la representación binaria de números en coma flotante, le puede extrañar que `rationalize (0.1)` no sea igual que 1/10.  Este comportamiento no es único de Maxima, ya que el número 1/10 en su forma binaria es periódico y no exacto.












```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2
(%i2) rationalize (0.1);
                               1
(%o2)                          --
                               10
(%i3) fpprec : 5$
(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152
(%i5) fpprec : 20$
(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848
(%i7) rationalize (sin (0.1*x + 5.6));
                              x    28
(%o7)                     sin(-- + --)
                              10   5
```

<!-- category: Other -->
<!-- keywords: ratnump -->
<!-- signatures: ratnump(expr) -->
### Function: ratnump (expr)

Devuelve `true` si *expr* es un entero literal o una fracción de enteros literales, en caso contrario devuelve `false`.

<!-- category: Other -->
<!-- keywords: sconcat -->
<!-- signatures: sconcat(arg_1, arg_2, ...) -->
### Function: sconcat (arg_1, arg_2, ...)

Concatena sus argumentos para producir una cadena.
Al contrario que `concat`, sus argumentos *no* necesitan ser átomos.


El resultado es una cadena.



```maxima
(%i1) sconcat ("xx[", 3, "]:", expand ((x+y)^3));
(%o1)               xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
```

<!-- category: Other -->
<!-- keywords: string -->
<!-- signatures: string(expr) -->
### Function: string (expr)

Convierte `expr` a la notación lineal de Maxima, tal como si fuese tecleada.


El valor que retorna la función `string` es una cadena, por lo que no puede ser utilizada en los cálculos.

<!-- category: Other -->
<!-- keywords: stringdisp -->
<!-- signatures: stringdisp -->
### Variable: stringdisp

Valor por defecto: `false`


Si `stringdisp` vale `true`,
las cadenas alfanuméricas se muestran encerradas entre comillas dobles. En caso contrario, no se nuestran las comillas.


La variable `stringdisp` vale siempre `true` cuando se muestra la definición de una función.



Ejemplos:











```maxima
(%i1) stringdisp: false$
(%i2) "This is an example string.";
(%o2)              This is an example string.
(%i3) foo () :=
      print ("This is a string in a function definition.");
(%o3) foo() := 
              print("This is a string in a function definition.")
(%i4) stringdisp: true$
(%i5) "This is an example string.";
(%o5)             "This is an example string."
```

<!-- category: Other -->
<!-- keywords: structures -->
<!-- signatures: structures -->
### Variable: structures

`structures` es la lista que contiene las estructuras definidas por el usuario con `defstruct`.

