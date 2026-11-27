## Ambiente em Tempo de Execução

<!-- category: Other -->
<!-- keywords: absolute_real_time -->
<!-- signatures: absolute_real_time() -->
### Function: absolute_real_time ()

Retorna o número de segundos desde a meia noite do dia primeiro de janeiro de 1900 (UTC).
O valor de retorno é um inteiro.


Veja também `elapsed_real_time` e `elapsed_run_time`.


Exemplo:







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

Retorna o n;umero de segundos (incluindo frações de segundo)
desde que Maxima tenha sido recentemente iniciado ou reiniciado.
O valor de retorno é um número em ponto flutuante.


Veja também `absolute_real_time` e `elapsed_run_time`.


Exemplo:








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

Retorna uma estimativa do número de segundos (incluindo frações de segundo)
que o Maxima gastou em computações desde que Maxima tenha sido recentemente iniciado ou reiniciado.
O valor de retorno é um número em ponto flutuante.


Veja também `absolute_real_time` e `elapsed_real_time`.


Exemplo:








```maxima
(%i1) elapsed_run_time ();
(%o1)                         0.04
(%i2) expand ((a + b)^500)$
(%i3) elapsed_run_time ();
(%o3)                         1.26
```

<!-- category: Other -->
<!-- keywords: feature -->
<!-- signatures: feature -->
### Variable: feature

Maxima compreende dois tipos distintos de recurso,
recursos do sistema e recursos aplicados a expressões matemáticas.
Veja Também `status` para informações sobre recursos do sistema.
Veja Também `features` e `featurep` para informações sobre recursos matemáticos.




`feature` por si mesmo não é o nome de uma função ou variável.

<!-- category: Other -->
<!-- keywords: featurep -->
<!-- signatures: featurep(a, f) -->
### Function: featurep (a, f)

Tenta determinar se o objeto *a* tem o
recurso *f* na base dos fatos dentro base de dados corrente.  Se possue,
é retornado `true`, de outra forma é retornado `false`.


Note que `featurep` retorna `false` quando nem *f*
nem a negação de *f* puderem ser estabelecidas.


`featurep` avalia seus argumentos.


Veja também `declare` e `features`.

       

```maxima
(%i1) declare (j, even)$
(%i2) featurep (j, integer);
(%o2)                           true
```

<!-- category: Other -->
<!-- keywords: maxima_tempdir -->
<!-- signatures: maxima_tempdir -->
### Variable: maxima_tempdir

`maxima_tempdir` nomeia o diretório no qual Maxima cria alguns arquivos temporários.
Em particular, arquivos temporários para impressão são criados no `maxima_tempdir`.


O valor inicial de `maxima_tempdir` é o diretório do usuário,
se o maxima puder localizá-lo; de outra forma Maxima supõe um diretório adequado.


A `maxima_tempdir` pode ser atribuído uma sequência de caracteres que corresponde a um diretório.

<!-- category: Other -->
<!-- keywords: maxima_userdir -->
<!-- signatures: maxima_userdir -->
### Variable: maxima_userdir

`maxima_userdir` nomeia um diretório no qual Maxima espera encontrar seus próprios arquivos e os do arquivos do Lisp.
(Maxima procura em alguns outros diretórios também;
`file_search_maxima` e `file_search_lisp` possuem a lista completa.)


O valor inicial de `maxima_userdir` é um subdiretório do diretório do usuário,
se Maxima puder localizá-lo; de outra forma Maxima supõe um diretório adequado.


A `maxima_userdir` pode ser atribuído uma sequência de caracteres que corresponde a um diretório.
Todavia, fazendo uma atribuição a `maxima_userdir` não muda automaticamente o valor de
`file_search_maxima` e de `file_search_lisp`;
Essas variáveis devem ser modificadas separadamente.

<!-- category: Other -->
<!-- keywords: room -->
<!-- signatures: room(), room(true), room(false) -->
### Function: room ()

Mostra uma descrição do estado de armazenamento e
gerenciamento de pilha no Maxima. `room` chama a função Lisp de
mesmo nome.



- *
`room ()` mostra uma descrição moderada.
- *
`room (true)` mostra uma descrição detalhada.
- *
`room (false)` mostra uma descrição resumida.

<!-- category: Other -->
<!-- keywords: status -->
<!-- signatures: status(feature), status(feature, recurso_ativo), status(status) -->
### Function: status (feature)

Retorna informações sobre a presença ou ausência de certos
recursos dependentes do sistema operacional.



- *
`status (feature)` retorna uma lista dos recursos do sistema.
Inclui a versão do Lisp, tipo de sistema operacional, etc.
A lista pode variar de um tipo de Lisp para outro.
- * 
`status (feature, recurso_ativo)` retorna `true` se *recurso_ativo*
está na lista de ítens retornada através de `status (feature)` e `false` de outra forma.
`status` não avalia o argumento *recurso_ativo*.
O operador apóstrofo-apóstrofo, `''`, evita a avaliação.
Um recurso cujo nome contém um caractere especial, tal como um hífem,
deve ser fornecido como um argumento em forma de sequência de caracteres. Por Exemplo,
`status (feature, "ansi-cl")`.
- *
`status (status)` retorna uma lista de dois elementos `[feature, status]`.
`feature` e `status` são dois argumentos aceitos pela função `status`;
Não está claro se essa lista tem significância adicional.


A variável `features` contém uma lista de recursos que se aplicam a
expressões matemáticas. Veja `features` e `featurep` para maiores informações.

<!-- category: Other -->
<!-- keywords: time -->
<!-- signatures: time(%o1, %o2, %o3, ...) -->
### Function: time (%o1, %o2, %o3, ...)

Retorna uma lista de tempos, em segundos, usados para calcular as linhas
de saída `%o1`, `%o2`, `%o3`, .... O tempo retornado é uma estimativa do Maxima do
tempo interno de computação, não do tempo decorrido. `time` pode somente
ser aplicado a variáveis(rótulos) de saída de linha; para quaisquer outras variáveis, `time`
retorna `unknown` (tempo desconhecido).


Escolha `showtime: true` para fazer com que Maxima moste o tempo de computação
e o tempo decorrido a cada linha de saída.

<!-- category: Other -->
<!-- keywords: timedate -->
<!-- signatures: timedate() -->
### Function: timedate ()

Retorna uma sequência de caracteres representando a data e hora atuais.
A sequência de caracteres tem o formato `HH:MM:SS Dia, mm/dd/aaaa (GMT-n)`,
Onde os campos são
horas, minutos, segundos, dia da semana, mês, dia do mês, ano, e horas que diferem da hora GMT.


O valor de retorno é uma sequência de caracteres Lisp.


Exemplo:







```maxima
(%i1) d: timedate ();
(%o1) 08:05:09 Wed, 11/02/2005 (GMT-7)
(%i2) print ("timedate mostra o tempo atual", d)$
timedate reports current time 08:05:09 Wed, 11/02/2005 (GMT-7)
```

