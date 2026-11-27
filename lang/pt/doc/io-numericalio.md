## numericalio

<!-- category: IO -->
<!-- keywords: read_hashed_array -->
<!-- signatures: read_hashed_array(nomeficheiro, A), read_hashed_array(nomeficheiro, A, separator_flag) -->
### Function: read_hashed_array (nomeficheiro, A)

`read_hashed_array` trata o primeiro item sobre uma linha como uma
chave hash, e associa o restante da linha (como uma lista) com a chava.
Por exemplo,
a linha `567 12 17 32 55` é equivalente a `A[567]: [12, 17, 32, 55]$`.
Linhas não precisam ter o mesmo número de elementos.

<!-- category: IO -->
<!-- keywords: read_lisp_array -->
<!-- signatures: read_lisp_array(nomeficheiro, A), read_lisp_array(nomeficheiro, A, separator_flag) -->
### Function: read_lisp_array (nomeficheiro, A)

`read_lisp_array` exige que o array
seja declarado através de `make_array` antes de chamar
a função de leitura. (Isso obviamente é necessário para inferir a dimensão 
do array, que pode ser um problema para arrays com múltiplas dimensões.)


`read_lisp_array` não verifica para ver se o 
ficheiro de entrada está de acordo com as dimensãoes do array; a entrada
é lida como uma lista monótona, então o array é preenchido usando `fillarray`.

<!-- category: IO -->
<!-- keywords: read_list -->
<!-- signatures: read_list(nomeficheiro), read_list(nomeficheiro, separator_flag) -->
### Function: read_list (nomeficheiro)

`read_list` lê todas as entradas em uma lista monótona.
`read_list` ignora o caractere de fim de linha.

<!-- category: IO -->
<!-- keywords: read_matrix -->
<!-- signatures: read_matrix(nomeficheiro), read_matrix(nomeficheiro, separator_flag) -->
### Function: read_matrix (nomeficheiro)

Lê o ficheiro *nomeficheiro* e retorna seu conteúdo completo como uma matriz.
Se *separator_flag* não for especificado, o ficheiro é assumido como delimitado por espaços em branco.


`read_matrix` infere o tamanho da matriz dos dados de entrada.
Cada linha do ficheiro inicia uma linha da matriz.
Se algumas linhas possuirem diferentes comprimentos, `read_matrix` reclama.

<!-- category: IO -->
<!-- keywords: read_maxima_array -->
<!-- signatures: read_maxima_array(nomeficheiro, A), read_maxima_array(nomeficheiro, A, separator_flag) -->
### Function: read_maxima_array (nomeficheiro, A)

`read_maxima_array` requer que o array
seja declarado através de `array` antes de chamar
a função de leitura. (Isso obviamente é necessário para inferir a dimensão 
do array, que pode ser uma hassle para arrays com múltiplas dimensões.)


`read_maxima_array` não verifica para ver se o 
ficheiro de entrada está de acordo com as dimensãoes do array; a entrada
é lida como uma lista monótona, então o array é preenchido usando `fillarray`.

<!-- category: IO -->
<!-- keywords: read_nested_list -->
<!-- signatures: read_nested_list(nomeficheiro), read_nested_list(nomeficheiro, separator_flag) -->
### Function: read_nested_list (nomeficheiro)

`read_nested_list` retorna uma lista que tem uma sublista para cada
linha de entrada. Linhas não precisam ter o mesmo número de elementos.
Linhas vazias *não* são ignoradas: uma linha vazia retorna uma sublista vazia.

<!-- category: IO -->
<!-- keywords: write_data -->
<!-- signatures: write_data(X, nomeficheiro), write_data(object, nomeficheiro, separator_flag) -->
### Function: write_data (X, nomeficheiro)

`write_data` escreve o objecto *X* no ficheiro *nomeficheiro*.


`write_data` escreve matrizes da forma usual,
com uma linha por fileira.


`write_data` escreve arrays declarados do Lisp e do Maxima da
forma usual, com um caractere de nova linha no final de todo pedaço.
Pedaços dimensionais muito grandes são separados por meio de novas linhas adicionais.


`write_data` escreve arrays desordenados com uma chave seguida por
a lista associada sobre cada linha.


`write_data` escreve a lista seguinte com cada sublista em uma linha.


`write_data` escreve uma lista monótona toda em uma linha.


Se `write_data` anexa ao final ou abandona os excessos em seus ficheiros de saída
é governado através da variável global `file_output_append`.

