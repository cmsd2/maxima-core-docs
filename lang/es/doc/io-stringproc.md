## stringproc

<!-- category: IO -->
<!-- keywords: alphacharp -->
<!-- signatures: alphacharp(char) -->
### Function: alphacharp (char)

Devuelve `true` si *char* es una carácter alfabético.

<!-- category: IO -->
<!-- keywords: alphanumericp -->
<!-- signatures: alphanumericp(char) -->
### Function: alphanumericp (char)

Devuelve `true` si *char* es una carácter alfabético o
un dígito.

<!-- category: IO -->
<!-- keywords: ascii -->
<!-- signatures: ascii(int) -->
### Function: ascii (int)

Devuelve el carácter correspondiente al número ASCII *int*,
debiendo ser $-1 < int < 256$.








```maxima
(%i1) for n from 0 thru 255 do ( 
  tmp: ascii(n),
  if alphacharp(tmp) then sprint(tmp), if n=96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

<!-- category: IO -->
<!-- keywords: base64 -->
<!-- signatures: base64(string) -->
### Function: base64 (string)

Devuelve la representación en base 64 de *string* en formato de
cadena de caracteres.


Ejemplo:



```maxima
(%i1) base64 : base64("foo bar baz");
(%o1)                       Zm9vIGJhciBiYXo=
(%i2) string : base64_decode(base64);
(%o2)                          foo bar baz
```

<!-- category: IO -->
<!-- keywords: base64_decode -->
<!-- signatures: base64_decode(base64-string) -->
### Function: base64_decode (base64-string)

Decodifica la cadena de caracteres *base64-string*, codificada
en base 64, y devuelve la cadena original.


Para un ejemplo, véase `base64`.

<!-- category: IO -->
<!-- keywords: cequal -->
<!-- signatures: cequal(char_1, char_2) -->
### Function: cequal (char_1, char_2)

Devuelve `true` si *char_1* y *char_2* son el mismo carácter.

<!-- category: IO -->
<!-- keywords: cequalignore -->
<!-- signatures: cequalignore(char_1, char_2) -->
### Function: cequalignore (char_1, char_2)

Como `cequal`, pero ignora si las letras están en mayúsculas o
minúsculas.

<!-- category: IO -->
<!-- keywords: cgreaterp -->
<!-- signatures: cgreaterp(char_1, char_2) -->
### Function: cgreaterp (char_1, char_2)

Devuelve  `true` si el número ASCII de *char_1* es mayor que el 
de *char_2*.

<!-- category: IO -->
<!-- keywords: cgreaterpignore -->
<!-- signatures: cgreaterpignore(char_1, char_2) -->
### Function: cgreaterpignore (char_1, char_2)

Como `cgreaterp`, pero ignora si las letras están en mayúsculas o
minúsculas.

<!-- category: IO -->
<!-- keywords: charat -->
<!-- signatures: charat(string, n) -->
### Function: charat (string, n)

Devuelve el *n*-ésimo carácter de *string*.
Al primer carácter de *string* le corresponde *n* = 1.






```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
```

<!-- category: IO -->
<!-- keywords: charlist -->
<!-- signatures: charlist(string) -->
### Function: charlist (string)

Devuelve una lista con todos los caracteres de *string*. 







```maxima
(%i1) charlist("Lisp");
(%o1)                     [L, i, s, p]
(%i2) %[1];
(%o2)                           L
```

<!-- category: IO -->
<!-- keywords: charp -->
<!-- signatures: charp(obj) -->
### Function: charp (obj)

Devuelve `true` si *obj* es un carácter de Maxima.

<!-- category: IO -->
<!-- keywords: cint -->
<!-- signatures: cint(char) -->
### Function: cint (char)

Devuelve el número ASCII de *char*.

<!-- category: IO -->
<!-- keywords: clessp -->
<!-- signatures: clessp(char_1, char_2) -->
### Function: clessp (char_1, char_2)

Devuelve  `true` si el número ASCII de *char_1* es menor que el 
de *char_2*.

<!-- category: IO -->
<!-- keywords: clesspignore -->
<!-- signatures: clesspignore(char_1, char_2) -->
### Function: clesspignore (char_1, char_2)

Como `clessp`, pero ignora si las letras están en mayúsculas o
minúsculas.

<!-- category: IO -->
<!-- keywords: close -->
<!-- signatures: close(stream) -->
### Function: close (stream)

Cierra el flujo de datos *stream* y devuelve `true` si *stream* había
sido abierto.

<!-- category: IO -->
<!-- keywords: constituent -->
<!-- signatures: constituent(char) -->
### Function: constituent (char)

Devuelve `true` si *char* es un carácter gráfico y no el
carácter espacio. Un carácter gráfico es el que se puede ver y con un
espacio añadido; `constituent` está definido por Paul Graham,
ANSI Common Lisp, 1996, page 67.







```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if constituent(tmp) then sprint(tmp) )$
! " #  %  ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c
d e f g h i j k l m n o p q r s t u v w x y z { | } ~
```

<!-- category: IO -->
<!-- keywords: cunlisp -->
<!-- signatures: cunlisp(lisp_char) -->
### Function: cunlisp (lisp_char)

Convierte un carácter Lisp en uno de Maxima. El uso de esta función por
parte del usuario no será necesario.

<!-- category: IO -->
<!-- keywords: digitcharp -->
<!-- signatures: digitcharp(char) -->
### Function: digitcharp (char)

Devuelve `true` si *char* es un dígito.

<!-- category: IO -->
<!-- keywords: eval_string -->
<!-- signatures: eval_string(str) -->
### Function: eval_string (str)

Analiza sintácticamente la cadena *str* como una expresión de Maxima
y la evalúa. La cadena *str* puede terminar o no con cualquiera de los 
símbolos de final de sentencia (dólar `$` o punto y coma `;`).
Sólo se analiza la primera expresión si hay más de una.


Se emitirá un mensaje de error si *str* no es una cadena.


Ejemplos:







```maxima
(%i1) eval_string ("foo: 42; bar: foo^2 + baz");
(%o1)                       42
(%i2) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o2)                   baz + 1764
```


Véase también `parse_string`.

<!-- category: IO -->
<!-- keywords: flength -->
<!-- signatures: flength(stream) -->
### Function: flength (stream)

Devuelve el número de elementos en *stream*,
el cual debe ser un flujo de datos desde o hacia un fichero.

<!-- category: IO -->
<!-- keywords: fposition -->
<!-- signatures: fposition(stream), fposition(stream, pos) -->
### Function: fposition (stream)

Devuelve la posición actual en el flujo de datos *stream* si no se utiliza *pos*.
Si se utiliza *pos*, `fposition` fija la posición en *stream*.
*stream* debe ser un flujo de datos desde o hacia un fichero y *pos* 
debe ser un entero positivo que hace corresponder al primer elemento de
*stream* la posición 1.

<!-- category: IO -->
<!-- keywords: freshline -->
<!-- signatures: freshline(), freshline(stream) -->
### Function: freshline ()

Escribe una nueva línea (en el flujo de datos *stream*)
si la posición actual no corresponde al inicio de la línea.


Véase también `newline`.

<!-- category: IO -->
<!-- keywords: get_output_stream_string -->
<!-- signatures: get_output_stream_string(stream) -->
### Function: get_output_stream_string (stream)

Devuelve una cadena con todos los caracteres presentes en *stream*,
que debe ser un flujo de datos de salida abiero.
Los caracteres devueltos son eliminados de *stream*.


Para un ejemplo, véase `make_string_output_stream` .

<!-- category: IO -->
<!-- keywords: lcharp -->
<!-- signatures: lcharp(obj) -->
### Function: lcharp (obj)

Devuelve `true` si *obj* es un carácter de Lisp.
El uso de esta función por parte del usuario no será necesario.

<!-- category: IO -->
<!-- keywords: lowercasep -->
<!-- signatures: lowercasep(char) -->
### Function: lowercasep (char)

Devuelve  `true` si *char* es un carácter en minúscula.

<!-- category: IO -->
<!-- keywords: make_string_input_stream -->
<!-- signatures: make_string_input_stream(string), make_string_input_stream(string, start), make_string_input_stream(string, start, end) -->
### Function: make_string_input_stream (string)

Devuelve un flujo de entrada que contiene partes de *string* junto con
el carácter de final de fichero. Sin argumentos opcionales, el flujo contiene
la cadena entera y se posiciona frente al primer carácter.
Los argumentos *start* y *end* definen la subcadena contenida en el
flujo. El primer carácter está disponible en la posición 1.


Ejemplo:



```maxima
(%i1) istream : make_string_input_stream("text", 1, 4);
(%o1)              #<string-input stream from "text">
(%i2) (while (c : readchar(istream)) # false do sprint(c), newline())$
t e x 
(%i3) close(istream)$
```

<!-- category: IO -->
<!-- keywords: make_string_output_stream -->
<!-- signatures: make_string_output_stream() -->
### Function: make_string_output_stream ()

Devuelve un flujo de salida que acepta caracteres. Los caracteres de
este flujo podrán obtenerse con `get_output_stream_string`.


Ejemplo:



```maxima
(%i1) ostream : make_string_output_stream();
(%o1)               #<string-output stream 09622ea0>
(%i2) printf(ostream, "foo")$

(%i3) printf(ostream, "bar")$

(%i4) string : get_output_stream_string(ostream);
(%o4)                            foobar
(%i5) printf(ostream, "baz")$

(%i6) string : get_output_stream_string(ostream);
(%o6)                              baz
(%i7) close(ostream)$
```

<!-- category: IO -->
<!-- keywords: md5sum -->
<!-- signatures: md5sum(string) -->
### Function: md5sum (string)

Devuelve, en formato de cadena de caracteres, el resultado de la suma de verificación
md5 del argumento *string*. Para obtener el valor devuelto por la función como
número entero, fijar la base numérica de entrada a 16 y a~nadir como prefijo
el cero.


Ejemplo:



```maxima
(%i1) string : md5sum("foo bar baz");
(%o1)                  ab07acbb1e496801937adfa772424bf7
(%i2) ibase : obase : 16.$

(%i3) integer : parse_string(sconcat(0, string));
(%o3)                 0ab07acbb1e496801937adfa772424bf7
```

<!-- category: IO -->
<!-- keywords: newline -->
<!-- signatures: newline(), newline(stream) -->
### Function: newline ()

Escribe una nueva línea (en el flujo de datos  *stream*).


Véase `sprint` para un ejemplo de uso de `newline()`.


Nótese que hay algunos casos en los que `newline` no trabaja
según lo esperado.

<!-- category: IO -->
<!-- keywords: opena -->
<!-- signatures: opena(file) -->
### Function: opena (file)

Devuelve un flujo de datos al fichero *file*.
Si se abre un fichero ya existente, `opena` añade elementos al final
del fichero.

<!-- category: IO -->
<!-- keywords: openr -->
<!-- signatures: openr(file) -->
### Function: openr (file)

Devuelve un flujo de datos de entrada al fichero *file*.
Si *file* no existe, será creado.

<!-- category: IO -->
<!-- keywords: openw -->
<!-- signatures: openw(file) -->
### Function: openw (file)

Devuelve un flujo de datos de salida al fichero *file*.
Si *file* no existe, será creado.
Si se abre un fichero ya existente, `openw` lo modifica 
borrando el contenido anterior.

<!-- category: IO -->
<!-- keywords: parse_string -->
<!-- signatures: parse_string(str) -->
### Function: parse_string (str)

Analiza sintácticamente la cadena *str* como una expresión de Maxima,
pero no la evalúa. La cadena *str* puede terminar o no con cualquiera de los 
símbolos de final de sentencia (dólar `$` o punto y coma `;`).
Sólo se analiza la primera expresión si hay más de una.


Se emitirá un mensaje de error si *str* no es una cadena.


Ejemplos:







```maxima
(%i1) parse_string ("foo: 42; bar: foo^2 + baz");
(%o1)                    foo : 42
(%i2) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o2)          (foo : 42, bar : foo  + baz)
```


Véase también `eval_string`.

<!-- category: IO -->
<!-- keywords: printf -->
<!-- signatures: printf(dest, string), printf(dest, string, expr_1, ..., expr_n) -->
### Function: printf (dest, string)

Genera una cadena de caracteres a partir de la cadena de control *string*,
teniendo en cuenta que las tildes introducen directivas. El carácter que
va después de la tilde, posiblemente precedido por parámetros y modificadores,
especifica el tipo de formato que se desea. La mayor parte de las directivas usan
uno o más elementos de los argumentos *expr_1*, ..., *expr_n*
para crear la salida.


Si *dest* es un flujo o vale `true`, entonces `printf` devuelve `false`.
En otro caso, `printf` devuelve una cadena conteniendo la salida.


`printf` da acceso a la función `format` de Common Lisp.
El siguiente ejemplo muestra la relación entre estas dos funciones.



```maxima
(%i1) printf(true, "R~dD~d~%", 2, 2);
R2D2
(%o1)                                false
(%i2) :lisp (format t "R~dD~d~%" 2 2)
R2D2
NIL
```


La siguiente descripción es un simple resumen de las posibilidades de `printf`.
La función `format` de Common Lisp se encuentra descrita en detalle en muchas
referencias, como el manual libre "Common Lisp the Language" de Guy L. Steele; en
particular, el capítulo 22.3.3.



```maxima
~%       nueva línea
   ~&       línea de refresco
   ~t       tabulación
   ~$       moneda
   ~d       entero en base decimal
   ~b       entero en base binaria
   ~o       entero en base octal
   ~x       entero en base hexadecimal
   ~br      entero en base b
   ~r       deletrea un entero
   ~p       plural
   ~f       decimal en coma flotante
   ~e       notación científica
   ~g       ~f o ~e, dependiendo de la magnitud
   ~h       número decimal grande (bigfloat)
   ~a       utiliza la función string de Maxima
   ~s       como ~a, pero las cadenas se devuelven entre "comillas dobles"
   ~~       ~
   ~<       justificación, ~> termina
   ~(       conversor mayúscula/minúscula, ~) termina 
   ~[       selección, ~] termina 
   ~{       iteración, ~} termina
```


La directiva `~h` para números decimales grandes no pertenece al estándar
de Lisp, por lo que se ilustra más abajo.


La directiva `~*` no está soportada.


Ejemplos:


Si *dest* es un flujo o vale `true`, entonces `printf` devuelve `false`.
En otro caso, `printf` devuelve una cadena conteniendo la salida.












```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf(true,"~{~{~9,1f ~}~%~}",mat ),
          mat = args(matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]))$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false,control, n,n,if n=1 then 1 else 2 ), n=2;
(%o5)                    Two birds are singing.
```


La directiva `~h` se ha introducido para formatear decimales grandes. 



```maxima
~w,d,e,x,o,p@H
 w : width
 d : decimal digits behind floating point
 e : minimal exponent digits
 x : preferred exponent
 o : overflow character
 p : padding character
 @ : display sign for positive numbers
```



```maxima
(%i1) fpprec : 1000$
(%i2) printf(true, "|~h|~%", 2.b0^-64)$
|0.0000000000000000000542101086242752217003726400434970855712890625|
(%i3) fpprec : 26$
(%i4) printf(true, "|~h|~%", sqrt(2))$
|1.4142135623730950488016887|
(%i5) fpprec : 24$
(%i6) printf(true, "|~h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i7) printf(true, "|~28h|~%", sqrt(2))$
|   1.41421356237309504880169|
(%i8) printf(true, "|~28,,,,,'*h|~%", sqrt(2))$
|***1.41421356237309504880169|
(%i9) printf(true, "|~,18h|~%", sqrt(2))$
|1.414213562373095049|
(%i10) printf(true, "|~,,,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-3|
(%i11) printf(true, "|~,,2,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-03|
(%i12) printf(true, "|~20h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i13) printf(true, "|~20,,,,'+h|~%", sqrt(2))$
|++++++++++++++++++++|
```

<!-- category: IO -->
<!-- keywords: readchar -->
<!-- signatures: readchar(stream) -->
### Function: readchar (stream)

Elimina y devuelve el primer carácter de *stream*. 
Si se ha alcanzado el final del fichero, `readchar` devuelve `false`.


Para un ejemplo, véase `make_string_input_stream`.

<!-- category: IO -->
<!-- keywords: readline -->
<!-- signatures: readline(stream) -->
### Function: readline (stream)

Devuelve una cadena con los caracteres desde la posición actual en el flujo
de datos *stream* hasta el final de la línea, o `false`
si se ha alcanzado el final del fichero.

<!-- category: IO -->
<!-- keywords: scopy -->
<!-- signatures: scopy(string) -->
### Function: scopy (string)

Devuelve una copia nueva de la cadena *string*.

<!-- category: IO -->
<!-- keywords: sdowncase -->
<!-- signatures: sdowncase(string), sdowncase(string, start), sdowncase(string, start, end) -->
### Function: sdowncase (string)

Convierte caracteres en minúscula a mayúscula. Véase también `supcase`.

<!-- category: IO -->
<!-- keywords: sequal -->
<!-- signatures: sequal(string_1, string_2) -->
### Function: sequal (string_1, string_2)

Devuelve `true` si *string_1* y *string_2* son dos cadenas de caracteres iguales.

<!-- category: IO -->
<!-- keywords: sequalignore -->
<!-- signatures: sequalignore(string_1, string_2) -->
### Function: sequalignore (string_1, string_2)

Igual que `sequal` pero no diferencia entre minúsculas y mayúsculas..

<!-- category: IO -->
<!-- keywords: sexplode -->
<!-- signatures: sexplode(string) -->
### Function: sexplode (string)

El nombre `sexplode` es un seudónimo de la función `charlist`.

<!-- category: IO -->
<!-- keywords: simplode -->
<!-- signatures: simplode(list), simplode(list, delim) -->
### Function: simplode (list)

La función `simplode` admite como entrada una lista de expresiones para
luego convertirla en una cadena de caracteres. Si no se utiliza la opción *delim*
para indicar el delimitador, entonces `simplode` no 
hace uso de ninguno. El valor de *delim* puede ser cualquier cadena.








```maxima
(%i1) simplode(["xx[",3,"]:",expand((x+y)^3)]);
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) simplode( sexplode("stars")," * " );
(%o2)                   s * t * a * r * s
(%i3) simplode( ["One","more","coffee."]," " );
(%o3)                   One more coffee.
```

<!-- category: IO -->
<!-- keywords: sinsert -->
<!-- signatures: sinsert(seq, string, pos) -->
### Function: sinsert (seq, string, pos)

Devuelve la concatenación de las cadenas `substring (string, 1, pos - 1)`,
*seq* y `substring (string, pos)`.
Nótese que al primer carácter de *string* le corresponde la posición 1.








```maxima
(%i1) s: "A submarine."$
(%i2) concat( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

<!-- category: IO -->
<!-- keywords: sinvertcase -->
<!-- signatures: sinvertcase(string), sinvertcase(string, start), sinvertcase(string, start, end) -->
### Function: sinvertcase (string)

Devuelve la misma cadena *string* pero con todos sus caracteres desde la
posición *start* hasta *end* invertidos, esto es, las
mayúsculas se convierten en minúsculas y éstas en mayúsculas.
Si no se incluye el argumento *end*, se invierten todos los caracteres 
desde *start* hasta el final de la cadena.







```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

<!-- category: IO -->
<!-- keywords: slength -->
<!-- signatures: slength(string) -->
### Function: slength (string)

Devuelve el número de caracteres de *string*.

<!-- category: IO -->
<!-- keywords: smake -->
<!-- signatures: smake(num, char) -->
### Function: smake (num, char)

Construye una cadena de longitud *num* con todos sus
caracteres iguales a *char*. 






```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

<!-- category: IO -->
<!-- keywords: smismatch -->
<!-- signatures: smismatch(string_1, string_2), smismatch(string_1, string_2, test) -->
### Function: smismatch (string_1, string_2)

Devuelve la posición del primer carácter de *string_1* distinto del
correpondiente a *string_2*. La respuesta será `false` si no existe
tal carácter. Por defecto, la función de comparación es `sequal`.
Si se quiere ignorar la diferencia entre mayúsculas y minúsculas, hágase uso de 
`sequalignore` para el argumento *test*.






```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

<!-- category: IO -->
<!-- keywords: space -->
<!-- signatures: space -->
### Variable: space

El carácter de espacio.

<!-- category: IO -->
<!-- keywords: split -->
<!-- signatures: split(string), split(string, delim), split(string, delim, multiple) -->
### Function: split (string)

Devuelve la lista de todos los lexemas (*tokens*) de *string*.
La función `split` utiliza *delim* como delimitador, y en caso
de no ser utilizado este argumento, será utilizado el espacio en blanco
como delimitador por defecto. El argumento *multiple* es una variable
booleana con valor `true` por defecto. Los delimitadores múltiples 
se leen como uno solo, lo que resulta de utilidad si las tabulaciones son 
almacenadas como secuencias de espacios en blanco. Si a *multiple* se 
le asigna el valor `false`, se consirararán todos los delimitadores.







```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

<!-- category: IO -->
<!-- keywords: sposition -->
<!-- signatures: sposition(char, string) -->
### Function: sposition (char, string)

Devuelve la posición del primer carácter de *string* que
coincide con *char*. Al primer carácter de *string*
le corresponde la posición 1.
Para cuando se quiera ignorar la diferencia entre mayúsculas y 
minúsculas, véase *ssearch*.

<!-- category: IO -->
<!-- keywords: sprint -->
<!-- signatures: sprint(expr_1, ..., expr_n) -->
### Function: sprint (expr_1, ..., expr_n)

Evalúa y muestra sus argumentos uno tras otro en un renglón comenzando por 
su extremo izquierdo. 


La función `newline()`, que se carga automáticamente desde `stringproc.lisp`,
puede ser de utilidad si se quiere intercalar un salto de línea.








```maxima
(%i1) for n:0 thru 19 do sprint( fib(n) )$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), if mod(n,10)=9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

<!-- category: IO -->
<!-- keywords: sremove -->
<!-- signatures: sremove(seq, string), sremove(seq, string, test), sremove(seq, string, test, start), sremove(seq, string, test, start, end) -->
### Function: sremove (seq, string)

Devuelve la cadena *string* pero sin las subcadenas que coinciden con *seq*.
La función de comparación por defecto es `sequal`.
Si se quiere ignorar la diferencia entre mayúsculas y minúsculas, hágase uso de 
`sequalignore` para el argumento *test*.
Utilícense *start* y *end* para acotar la búsqueda.
Al primer carácter de *string* le corresponde la posición 1.







```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

<!-- category: IO -->
<!-- keywords: sremovefirst -->
<!-- signatures: sremovefirst(seq, string), sremovefirst(seq, string, test), sremovefirst(seq, string, test, start), sremovefirst(seq, string, test, start, end) -->
### Function: sremovefirst (seq, string)

Actúa de forma similar a la función `sremove`, pero sólo elimina
la primera aparición de la subcadena `seq`.

<!-- category: IO -->
<!-- keywords: sreverse -->
<!-- signatures: sreverse(string) -->
### Function: sreverse (string)

Devuelve una cadena con todos los caracteres de *string* en orden inverso.

<!-- category: IO -->
<!-- keywords: ssearch -->
<!-- signatures: ssearch(seq, string), ssearch(seq, string, test), ssearch(seq, string, test, start), ssearch(seq, string, test, start, end) -->
### Function: ssearch (seq, string)

Devuelve la posición de la primera subcadena de *string* que coincide con
la cadena *seq*.
La función de comparación por defecto es `sequal`.
Si se quiere ignorar la diferencia entre mayúsculas y minúsculas, hágase uso de 
`sequalignore` para el argumento *test*.
Utilícense *start* y *end* para acotar la búsqueda.
Al primer carácter de *string* le corresponde la posición 1.



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

<!-- category: IO -->
<!-- keywords: ssort -->
<!-- signatures: ssort(string), ssort(string, test) -->
### Function: ssort (string)

Devuelve una cadena con todos los caracteres de *string* en un orden
tal que no haya dos caracteres sucesivos *c* y *d* que verifiquen
que `test (c, d)` sea igual `false` y 
`test (d, c)` igual a `true`.
La función de comparación *test* por defecto es  *clessp*, siendo
el conjunto de posibles valores para este argumento 
`{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`.







```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

<!-- category: IO -->
<!-- keywords: ssubst -->
<!-- signatures: ssubst(new, old, string), ssubst(new, old, string, test), ssubst(new, old, string, test, start), ssubst(new, old, string, test, start, end) -->
### Function: ssubst (new, old, string)

Devuelve una cadena similar a *string* pero en la que aquellas subcadenas 
coincidentes con *old* han sido sustituidas por *new*. Las subcadenas
*old* y *new* no necesitan ser de la misma longitud. 
La función de comparación por defecto es `sequal`.
Si se quiere ignorar la diferencia entre mayúsculas y minúsculas durante
la búsqueda de *old*, hágase uso de 
`sequalignore` para el argumento *test*.
Utilícense *start* y *end* para acotar la búsqueda.
Al primer carácter de *string* le corresponde la posición 1.







```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

<!-- category: IO -->
<!-- keywords: ssubstfirst -->
<!-- signatures: ssubstfirst(new, old, string), ssubstfirst(new, old, string, test), ssubstfirst(new, old, string, test, start), ssubstfirst(new, old, string, test, start, end) -->
### Function: ssubstfirst (new, old, string)

Actúa de forma similar a la función `subst`, pero sólo hace
la sustitución en la primera coincidencia con *old*.

<!-- category: IO -->
<!-- keywords: strim -->
<!-- signatures: strim(seq, string) -->
### Function: strim (seq, string)

Devuelve la cadena *string* pero recortando los caracteres
de *seq* que tuviese en sus extremos.








```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

<!-- category: IO -->
<!-- keywords: striml -->
<!-- signatures: striml(seq, string) -->
### Function: striml (seq, string)

Actúa de forma similar a `strim`, pero sólo recorta
en el extremo final de *string*.

<!-- category: IO -->
<!-- keywords: strimr -->
<!-- signatures: strimr(seq, string) -->
### Function: strimr (seq, string)

Actúa de forma similar a `strim`, pero sólo recorta
en el extremo inicial de *string*.

<!-- category: IO -->
<!-- keywords: stringp -->
<!-- signatures: stringp(obj) -->
### Function: stringp (obj)

Devuelve `true` si *obj* es una cadena.
Véase un ejemplo en la introducción.

<!-- category: IO -->
<!-- keywords: substring -->
<!-- signatures: substring(string, start), substring(string, start, end) -->
### Function: substring (string, start)

Devuelve la subcadena de *string* que comienza en la posición
*start* y termina en la posición *end*.
El carácter en la posición *end* no se incluye.
En caso de no suministrarse el argumento *end*, la subcadena
se extenderá hasta el final. 
Al primer carácter de *string* le corresponde la posición 1.







```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

<!-- category: IO -->
<!-- keywords: supcase -->
<!-- signatures: supcase(string), supcase(string, start), supcase(string, start, end) -->
### Function: supcase (string)

Devuelve la cadena *string* con todos sus caracteres entre las posiciones
*start* y *end* en minúscula transformados a mayúscula.
En caso de no suministrarse el argumento *end*, los cambios
se extenderán hasta el final.






```maxima
(%i1) supcase("english",1,2);
(%o1)                        English
```

<!-- category: IO -->
<!-- keywords: tab -->
<!-- signatures: tab -->
### Variable: tab

El carácter de tabulación.

<!-- category: IO -->
<!-- keywords: tokens -->
<!-- signatures: tokens(string), tokens(string, test) -->
### Function: tokens (string)

Devuelve la lista de todos los lexemas (*tokens*) de *string*.
Los lexemas son subcadenas cuyos caracteres satisfacen la  condición *test*.
Si no se suministra el argumento *test*, se utilizará la condición
*constituent*, siendo el conjunto de las otras alternativas
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}`.








```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parse_string,%);
(%o3)                      [5, 10, 24]
```

<!-- category: IO -->
<!-- keywords: uppercasep -->
<!-- signatures: uppercasep(char) -->
### Function: uppercasep (char)

Devuelve `true` si *char* es un carácter en mayúscula.

