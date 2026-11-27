## numericalio

<!-- category: IO -->
<!-- keywords: assume_external_byte_order -->
<!-- signatures: assume_external_byte_order(byte_order_flag) -->
### Function: assume_external_byte_order (byte_order_flag)

Le indica a `numericalio` el orden de los bytes en que debe leer y escribir los datos.
Los valores que reconoce *byte_order_flag* son dos:
`lsb`, que indica que el byte menos significativo debe ser el primero, y `msb`,
que indica que el byte más significativo es el que debe ir en primer lugar.


En caso de no hacer ninguna selección, `numericalio` interpreta que es el byte
más significativo el que se debe leer o escribir primero.

<!-- category: IO -->
<!-- keywords: opena_binary -->
<!-- signatures: opena_binary(file_name) -->
### Function: opena_binary (file_name)

Devuelve un flujo de entrada de bytes no signados para añadir datos al fichero de nombre *file_name*.

<!-- category: IO -->
<!-- keywords: openr_binary -->
<!-- signatures: openr_binary(file_name) -->
### Function: openr_binary (file_name)

Devuelve un flujo de entrada de bytes no signados para la lectura del fichero de nombre *file_name*.

<!-- category: IO -->
<!-- keywords: openw_binary -->
<!-- signatures: openw_binary(file_name) -->
### Function: openw_binary (file_name)

Devuelve un flujo de entrada de bytes no signados para la escritura en el fichero de nombre *file_name*.

<!-- category: IO -->
<!-- keywords: read_array -->
<!-- signatures: read_array(S, A), read_array(S, A, separator_flag) -->
### Function: read_array (S, A)

Guarda el contenido de la fuente *S* en el array *A*,
hasta que *A* esté lleno o hasta que se consuma la fuente.
Los datos se almacenan fila a fila. Los datos de entrada no necesitan tener el
mismo número de filas y columnas que *A*.


La fuente *S* puede ser el nombre de un fichero o de un flujo.


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

<!-- category: IO -->
<!-- keywords: read_binary_array -->
<!-- signatures: read_binary_array(S, A) -->
### Function: read_binary_array (S, A)

Lee números decimales en coma flotante de 8 bytes desde la fuente *S* y los
va almacenando en el array *A*, bien hasta que *A* se llene, o bien hasta que
la fuente se haya consumido. *A* debe ser un array creado por `array`
o por `make_array`. El array *A* se rellena fila a fila.


La fuente *S* puede ser el nombre de un fichero o un flujo.


El orden de los bytes de los datos procedentes de la fuente se especifican
mediante `assume_external_byte_order`.

<!-- category: IO -->
<!-- keywords: read_binary_list -->
<!-- signatures: read_binary_list(S), read_binary_list(S, L) -->
### Function: read_binary_list (S)

`read_binary_list(S)` lee el contenido completo de la fuente de datos *S*
como una secuencia de números decimales en coma flotante de 8 bytes en formato binario,
devolviéndolos en forma de lista.


La fuente *S* puede ser el nombre de un fichero o un flujo.


`read_binary_list(S, L)` lee números decimales en coma flotante de 8 bytes en
formato binario desde la fuente *S* y los almacena en la lista *L*, bien hasta que
ésta esté llena, o bien hasta que se consuman los datos de la fuente.


El orden de los bytes de los datos procedentes de la fuente se especifican
mediante `assume_external_byte_order`.

<!-- category: IO -->
<!-- keywords: read_binary_matrix -->
<!-- signatures: read_binary_matrix(S, M) -->
### Function: read_binary_matrix (S, M)

Lee números decimales en coma flotante de 8 bytes desde la fuente *S* y los
va almacenando en la matriz *M*, bien hasta que *M* se llene, o bien hasta que
la fuente se haya consumido. La matriz *M* se rellena fila a fila.


La fuente *S* puede ser el nombre de un fichero o un flujo.


El orden de los bytes de los datos procedentes de la fuente se especifican
mediante `assume_external_byte_order`.

<!-- category: IO -->
<!-- keywords: read_hashed_array -->
<!-- signatures: read_hashed_array(S, A), read_hashed_array(S, A, separator_flag) -->
### Function: read_hashed_array (S, A)

Lee la fuente *S* y devuelve su contenido completo en forma de array de claves.
La fuente *S* puede ser el nombre de un fichero o de un flujo.


`read_hashed_array` interpreta el primer elemento de cada fila como una clave,
asociando el resto de la fila, en formato de lista, a la clave. Por ejemplo,
la secuencia `567 12 17 32 55` equivale a `A[567]: [12, 17, 32, 55]$`.
Las filas no necesitan tener todas ellas el mismo número de elementos.


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

<!-- category: IO -->
<!-- keywords: read_list -->
<!-- signatures: read_list(S), read_list(S, L), read_list(S, separator_flag), read_list(S, L, separator_flag) -->
### Function: read_list (S)

`read_list(S)` lee la fuente *S* y devuelve su contenido como una lista simple.


`read_list(S, L)` guarda el contenido de la fuente *S* en la lista *L*,
hasta que *L* esté llena o hasta que se consuma la fuente.


La fuente *S* puede ser el nombre de un fichero o de un flujo.


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

<!-- category: IO -->
<!-- keywords: read_matrix -->
<!-- signatures: read_matrix(S), read_matrix(S, M), read_matrix(S, separator_flag), read_matrix(S, M, separator_flag) -->
### Function: read_matrix (S)

`read_matrix(S)` lee la fuente *S* y devuelve su contenido completo en forma
de matriz. El tamaño de la matriz se deduce de los datos de entrada: 
cada fila del fichero forma una fila de la matriz. Si hay filas con diferente número de elementos,
`read_matrix` emite un mensaje de error.


`read_matrix(S, M)` lee la fuente *S* y va almacenando su contenido
en la matriz *M*, hasta que *M* esté llena o hasta que se consuma la fuente.
Los datos se almacenan fila a fila. Los datos de entrada no necesitan tener el
mismo número de filas y columnas que *M*.


La fuente *S* puede ser el nombre de un fichero o de un flujo.


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

<!-- category: IO -->
<!-- keywords: read_nested_list -->
<!-- signatures: read_nested_list(S), read_nested_list(S, separator_flag) -->
### Function: read_nested_list (S)

Lee la fuente *S* y devuelve su contenido completo en forma de lista anidada.
La fuente *S* puede ser el nombre de un fichero o de un flujo.


`read_nested_list` devuelve una lista que tiene una sublista por cada fila
de entrada. Los filas de entrada no necesitan tener todas ellas el mismo número
de elementos. Las filas en blanco no se ignoran, sino que se convierten 
en listas vacías


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

<!-- category: IO -->
<!-- keywords: write_binary_data -->
<!-- signatures: write_binary_data(X, D) -->
### Function: write_binary_data (X, D)

Escribe el objeto *X*, que contiene números decimales en
coma flotante de 8 bytes del estándar IEEE 754, en el destino *D*.
Cualesquiera otros tipos de decimales son transformados a 8 bytes. 
`write_binary_data` no puede escribir datos no numéricos.


El objeto *X* puede ser una lista, una lista anidada, una matriz, o un
array creado con `array` o `make_array`; *X* no puede ser
ni un array no declarado ni cualquier otro tipo de objeto distinto a los citados.
`write_binary_data` escribe las listas anidadas, las matrices y los arrays
fila a fila.


El destino *D* puede ser el nombre de un fichero o un flujo; en el primer caso,
la variable global `file_output_append` controla si el fichero de salida es
ampliado con la nueva información o si se borra antes; en el segundo caso,
no se realiza ningún tipo de acción por parte de `write_binary_data` después
de que se hayan escrito los datos; en particular, el flujo se mantiene abierto.


El orden de los bytes de los datos procedentes de la fuente se especifican
mediante `assume_external_byte_order`.

<!-- category: IO -->
<!-- keywords: write_data -->
<!-- signatures: write_data(X, D), write_data(X, D, separator_flag) -->
### Function: write_data (X, D)

Escribe el objeto *X* en el destino *D*.


`write_data` escribe una matriz fila a fila; cada línea de
entrada se corresponde con una fila.


`write_data` escribe un array creado por `array` o `make_array`
fila a fila, con una nueva línea al final de cada bloque de datos.
Los bloques de mayores dimensiones se separan con líneas adicionales.


`write_data` escribe un array de claves con cada clave seguida de su lista
asociada en una sola línea.


`write_data` escribe una lista anidada con una sublista por línea.


`write_data` escribe una lista simple en una única fila.


El destino *D* puede ser el nombre de un fichero o un flujo; en el primer caso,
la variable global `file_output_append` controla si el fichero de salida es
ampliado con la nueva información o si se borra antes; en el segundo caso,
no se realiza ningún tipo de acción por parte de `write_data` después
de que se hayan escrito los datos; en particular, el flujo se mantiene abierto.


Los valores aceptados para *separator_flag* son:
`comma`, `pipe`, `semicolon` y `space`.
Si no se especifica un valor para *separator_flag*,
se supone que los datos están separados por espacios.

