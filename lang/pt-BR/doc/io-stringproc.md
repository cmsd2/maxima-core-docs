## stringproc

<!-- category: IO -->
<!-- keywords: alphacharp -->
<!-- signatures: alphacharp(caractere) -->
### Function: alphacharp (caractere)

Retorna `true` se *caractere* for um caractere alfabético.

<!-- category: IO -->
<!-- keywords: alphanumericp -->
<!-- signatures: alphanumericp(caractere) -->
### Function: alphanumericp (caractere)

Retorna `true` se *caractere* for um caractere alfabético ou um dígito.

<!-- category: IO -->
<!-- keywords: ascii -->
<!-- signatures: ascii(int) -->
### Function: ascii (int)

Retorna o caractere correspondente ao código numérico ASCII *int*.
( -1 < int < 256 )







```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if alphacharp(tmp) then sprint(tmp), if n=96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

<!-- category: IO -->
<!-- keywords: cequal -->
<!-- signatures: cequal(caractere_1, caractere_2) -->
### Function: cequal (caractere_1, caractere_2)

Retorna `true` se *caractere_1* e *caractere_2* forem os mesmos.

<!-- category: IO -->
<!-- keywords: cequalignore -->
<!-- signatures: cequalignore(caractere_1, caractere_2) -->
### Function: cequalignore (caractere_1, caractere_2)

como `cequal` mas ignora a caixa alta/baixa.

<!-- category: IO -->
<!-- keywords: cgreaterp -->
<!-- signatures: cgreaterp(caractere_1, caractere_2) -->
### Function: cgreaterp (caractere_1, caractere_2)

Retorna `true` se o código numérico ASCII do *caractere_1* for maior que o código numérico ASCII do *caractere_2*.

<!-- category: IO -->
<!-- keywords: cgreaterpignore -->
<!-- signatures: cgreaterpignore(caractere_1, caractere_2) -->
### Function: cgreaterpignore (caractere_1, caractere_2)

Como `cgreaterp` mas ignora a caixa alta/baixa.

<!-- category: IO -->
<!-- keywords: charat -->
<!-- signatures: charat(seq_caracte, n) -->
### Function: charat (seq_caracte, n)

Retorna o *n*-ésimo caractere de *seq_caracte*.
O primeiro caractere em *seq_caracte* é retornado com *n* = 1.






```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
```

<!-- category: IO -->
<!-- keywords: charlist -->
<!-- signatures: charlist(seq_caracte) -->
### Function: charlist (seq_caracte)

Retorna a lsita de todos os caracteres em *seq_caracte*. 







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

Retorna `true` se *obj* for um caractere do Maxima.
Veja na seção "Introdução a manipulação de sequências de caracteres" para ter um exemplo.

<!-- category: IO -->
<!-- keywords: cint -->
<!-- signatures: cint(caractere) -->
### Function: cint (caractere)

Retorna o código numéico ASCII de *caractere*.

<!-- category: IO -->
<!-- keywords: clessp -->
<!-- signatures: clessp(caractere_1, caractere_2) -->
### Function: clessp (caractere_1, caractere_2)

Retorna `true` se o código numérico ASCII de *caractere_1* for menor que o código numérico ASCII de *caractere_2*.

<!-- category: IO -->
<!-- keywords: clesspignore -->
<!-- signatures: clesspignore(caractere_1, caractere_2) -->
### Function: clesspignore (caractere_1, caractere_2)

Como em `clessp` ignora a caixa alta/baixa.

<!-- category: IO -->
<!-- keywords: close -->
<!-- signatures: close(fluxo) -->
### Function: close (fluxo)

Fecha  *fluxo* e retorna `true` se *fluxo* tiver sido aberto anteriormente.

<!-- category: IO -->
<!-- keywords: constituent -->
<!-- signatures: constituent(caractere) -->
### Function: constituent (caractere)

Retorna `true` se *caractere* for caractere  gráfico e não o caractere de espaço em branco.
Um caractere gráfico é um caractere que se pode ver, adicionado o caractere de espaço em branco.
(`constituent` foi definida por Paul Graham, em ANSI Common Lisp, 1996, página 67.)







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

Converte um caractere do Lisp em um caractere do Maxima.
(Você pode não precisar dessa função.)

<!-- category: IO -->
<!-- keywords: digitcharp -->
<!-- signatures: digitcharp(caractere) -->
### Function: digitcharp (caractere)

Retorna `true` se *caractere* for um dígito (algarismo de 0 a 9).

<!-- category: IO -->
<!-- keywords: flength -->
<!-- signatures: flength(fluxo) -->
### Function: flength (fluxo)

Retorna o número de elementos em *fluxo*.

<!-- category: IO -->
<!-- keywords: fposition -->
<!-- signatures: fposition(fluxo), fposition(fluxo, pos) -->
### Function: fposition (fluxo)

Retorna a posição corrente em *fluxo*, se *pos* não está sendo usada.
Se *pos* estiver sendo usada,
`fposition` escolhe a posição em *fluxo*.
*pos* tem que ser um número positivo,
o primeiro elemento em *fluxo* está na posição 1.

<!-- category: IO -->
<!-- keywords: freshline -->
<!-- signatures: freshline(), freshline(fluxo) -->
### Function: freshline ()

escreve uma nova linha (em *fluxo*),
se a posição atual não for um início de linha.
Veja também `newline`.

<!-- category: IO -->
<!-- keywords: lcharp -->
<!-- signatures: lcharp(obj) -->
### Function: lcharp (obj)

Retorna `true` se *obj* for um caractere do Lisp.
(Você pode não precisar dessa função.)

<!-- category: IO -->
<!-- keywords: lowercasep -->
<!-- signatures: lowercasep(caractere) -->
### Function: lowercasep (caractere)

Retorna `true` se *caractere* for um caractere em caixa baixa.

<!-- category: IO -->
<!-- keywords: lstringp -->
<!-- signatures: lstringp(obj) -->
### Function: lstringp (obj)

Retorna `true` se *obj* is uma sequência de caracteres do Lisp.
(Em geral você pode não precisar dessa função.)

<!-- category: IO -->
<!-- keywords: newline -->
<!-- signatures: newline(), newline(fluxo) -->
### Function: newline ()

Escreve uma nova linha (para *fluxo*).
Veja `sprint` para um exemplo de uso de `newline()`.
Note que existem alguns casos, onde `newline()`não trabalha como esperado.

<!-- category: IO -->
<!-- keywords: opena -->
<!-- signatures: opena(arquivo) -->
### Function: opena (arquivo)

Retorna um fluxo de saída para *arquivo*.
Se um arquivo já existente tiver sido aberto, `opena` anexa os elementos ao final do arquivo.

<!-- category: IO -->
<!-- keywords: openr -->
<!-- signatures: openr(arquivo) -->
### Function: openr (arquivo)

Retorna um fluxo para *arquivo*.
Se *arquivo* não existir, ele será criado.

<!-- category: IO -->
<!-- keywords: openw -->
<!-- signatures: openw(arquivo) -->
### Function: openw (arquivo)

Retorna um fluxo de saída para *arquivo*.
Se *arquivo* não existir, será criado.
Se um arquivo já existente for aberto, `openw` modifica destrutivametne o *arquivo*.

<!-- category: IO -->
<!-- keywords: parsetoken -->
<!-- signatures: parsetoken(seq_caracte) -->
### Function: parsetoken (seq_caracte)

`parsetoken` converte a primeira ficha em *seq_caracte* para o correspondente número ou retorna `false` se o número não puder ser determinado.
O conjunto de delimitadores para a troca de fichas é `{space, comma, semicolon, tab, newline}`


Nota de tradução:
espaço, vírgula, ponto e vírgula, tabulação e nova linha.






```maxima
(%i1) 2*parsetoken("1.234 5.678");
(%o1)                         2.468
```


Para analizar você pode também usar  a função `parse_string`.
Veja a descrição no arquivo ’share\contrib\eval_string.lisp’.

<!-- category: IO -->
<!-- keywords: printf -->
<!-- signatures: printf(dest, seq_caracte), printf(dest, seq_caracte, expr_1, ..., expr_n) -->
### Function: printf (dest, seq_caracte)

Torna a função FORMAT do Lisp Comum disponível no Maxima. 
(Retirado de gcl.info: "format produces formatted output by outputting the caracteres of 
control-string string and observing that a tilde introduces a directive.
The caractere after the tilde,
possibly preceded by prefix parameters and modifiers,
specifies what kind of formatting is desired.
Most directives use one or more elements of args to create their output.")


A seguinte descrição e oa exemplos podem fornecer uma idéia de uso de `printf`.
Veja um referência de Lisp para maiores informações.



```maxima
~%       nova linha
   ~&       novíssima line
   ~t       tabulação
   ~$       monetário
   ~d       inteiro decimal
   ~b       inteiro binário
   ~o       inteiro octal
   ~x       inteiro hexadecimal
   ~br      inteiro de base b
   ~r       soletra um inteiro
   ~p       plural
   ~f       ponto flutuante
   ~e       notação científica
   ~g       ~f ou ~e, dependendo  da magnitude
   ~a       como mostrado pela função print do Maxima
   ~s       sequências de caracteres entre "aspas duplas"
   ~~       ~
   ~<       justificação de texto, ~> terminador de justificação de texto
   ~(       conversão de caixa alta/baixa, ~) terminador de conversão de caixa
   ~[       seleção, ~] terminador de seleção 
   ~{       iteração, ~} terminador de iteração
```


Por favor note que não existe especificador de formato para grandes números em ponto flutuante. Todavia grandes números em ponto flutuante podem 
simplesmente serem mostrados por meio da diretiva `~a`. 
`~s` mostra a sequências de caracteres entre "aspas duplas", você pode evitar isso usando `~a`.
Note que a diretiva de seleção `~[` é indexada em zero.
Também note que existem algumas diretivas, que não trabalham no Maxima.
Por exemplo, `~:[` falha.












```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf( true,"~{~{~9,1f ~}~%~}",mat ),
              mat = args( matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]) )$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false,control, n,n,if n=1 then 0 else 1 ), n=2;
(%o5)                    Two birds are singing.
```


Se *dest* for um fluxo ou `true`, então `printf` retorna `false`.
De outra forma, `printf` retorna uma sequência de caracteres contendo a saída.

<!-- category: IO -->
<!-- keywords: readline -->
<!-- signatures: readline(fluxo) -->
### Function: readline (fluxo)

Retorna uma sequência de caracteres contendo os caracteres a partir da posição corrente em *fluxo* até o fim de linha ou *false* se o fim de linha do arquivo for encontrado.

<!-- category: IO -->
<!-- keywords: sconc -->
<!-- signatures: sconc(expr_1, ..., expr_n) -->
### Function: sconc (expr_1, ..., expr_n)

Avalia seus argumentos e concatena-os em uma sequência de caracteres.
`sconc` é como `sconcat` mas retorna uma sequência de caracteres do Maxima.







```maxima
(%i1) sconc("xx[",3,"]:",expand((x+y)^3));
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) stringp(%);
(%o2)                         true
```

<!-- category: IO -->
<!-- keywords: scopy -->
<!-- signatures: scopy(seq_caracte) -->
### Function: scopy (seq_caracte)

Retorna uma cópia de *seq_caracte* como uma nova sequência de caracteres.

<!-- category: IO -->
<!-- keywords: sdowncase -->
<!-- signatures: sdowncase(seq_caracte), sdowncase(seq_caracte, início), sdowncase(seq_caracte, início, fim) -->
### Function: sdowncase (seq_caracte)

Como em `supcase`, mas caracteres em caixa alta são convertidos para caracteres em caixa baixa.

<!-- category: IO -->
<!-- keywords: sequal -->
<!-- signatures: sequal(seq_caracte__1, seq_caracte__2) -->
### Function: sequal (seq_caracte__1, seq_caracte__2)

Retorna `true` se *seq_caracte__1* e *seq_caracte__2* tiverem o mesmo comprimento e contiverem os mesmos caracteres.

<!-- category: IO -->
<!-- keywords: sequalignore -->
<!-- signatures: sequalignore(seq_caracte__1, seq_caracte__2) -->
### Function: sequalignore (seq_caracte__1, seq_caracte__2)

Como em `sequal` mas igonara a caixa alta/baixa.

<!-- category: IO -->
<!-- keywords: sexplode -->
<!-- signatures: sexplode(seq_caracte) -->
### Function: sexplode (seq_caracte)

`sexplode` é um apelido para a função `charlist`.

<!-- category: IO -->
<!-- keywords: simplode -->
<!-- signatures: simplode(lista), simplode(lista, delim) -->
### Function: simplode (lista)

`simplode` takes uma `lista` ou expressões  e concatena-as em uma sequência de caracteres.
Se nenhum delimitador *delim* for usado, `simplode` funciona como `sconc` e não utiliza delimitador.
*delim* pode ser qualquer sequência de caracteres.








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
<!-- signatures: sinsert(seq, seq_caracte, pos) -->
### Function: sinsert (seq, seq_caracte, pos)

Retorna uma sequência de caracteres que é uma concatenação de `substring (seq_caracte, 1, pos - 1)`,
a sequência de caracteres *seq* e `substring (seq_caracte, pos)`.
Note que o primeiro caractere está em *seq_caracte* e está na posição 1.








```maxima
(%i1) s: "A submarine."$
(%i2) sconc( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

<!-- category: IO -->
<!-- keywords: sinvertcase -->
<!-- signatures: sinvertcase(seq_caracte), sinvertcase(seq_caracte, início), sinvertcase(seq_caracte, início, fim) -->
### Function: sinvertcase (seq_caracte)

Retorna *seq_caracte* exceto que cada caractere da posição *início* até a posição *fim* está invertido.
Se a posição *fim* não for fornecida,
todos os caracteres do início ao *fim* de *seq_caracte* são substituídos.






```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

<!-- category: IO -->
<!-- keywords: slength -->
<!-- signatures: slength(seq_caracte) -->
### Function: slength (seq_caracte)

Retorna número de caracteres em *seq_caracte*.

<!-- category: IO -->
<!-- keywords: smake -->
<!-- signatures: smake(num, caractere) -->
### Function: smake (num, caractere)

Retorna uma nova sequência de caracteres repetindo *num* vezes *caractere*. 






```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

<!-- category: IO -->
<!-- keywords: smismatch -->
<!-- signatures: smismatch(seq_caracte__1, seq_caracte__2), smismatch(seq_caracte__1, seq_caracte__2, test) -->
### Function: smismatch (seq_caracte__1, seq_caracte__2)

Retorna a posição do primeiro caractere de *seq_caracte__1* no qual *seq_caracte__1* e *seq_caracte__2* diferem ou `false` em caso contrário.
A função padrao de teste para coincidência é `sequal`.
Se `smismatch` pode ignorar a caixa alta/baixa, use `sequalignore` como função de teste.






```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

<!-- category: IO -->
<!-- keywords: space -->
<!-- signatures: space -->
### Variable: space

O caractere de espaço em branco.

<!-- category: IO -->
<!-- keywords: split -->
<!-- signatures: split(seq_caracte), split(seq_caracte, delim), split(seq_caracte, delim, multiple) -->
### Function: split (seq_caracte)

Retorna a lista de todas as fichas em *seq_caracte*.
Cada ficha é uma sequência de caracteres não analisada.
`split` usa *delim* como delimitador.
Se *delim* não for fornecido, o caractere de espaço é o delimitador padrão.
*multiple* é uma variável booleana com `true` como valor padrão.
Multiplos delimitadores são lidos como um.
Essa função é útil se tabulações são gravadas com caracteres de espaço multiplos.
Se *multiple* for escolhido para `false`, cada delimitador é considerado.







```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

<!-- category: IO -->
<!-- keywords: sposition -->
<!-- signatures: sposition(caractere, seq_caracte) -->
### Function: sposition (caractere, seq_caracte)

Retorna a posição do primeiro caractere em *seq_caracte* que coincide com *caractere*.
O primeiro caractere em *seq_caracte* está na posição 1.
Para que os caracteres que coincidirem desconsiderem a caixa alta/baixa veja `ssearch`.

<!-- category: IO -->
<!-- keywords: sprint -->
<!-- signatures: sprint(expr_1, ..., expr_n) -->
### Function: sprint (expr_1, ..., expr_n)

Avalia e mostra seus argumentos um após o outro ‘sobre uma linha’ iniciando na posição mais à esquerda.
Os números são mostrados com o ’-’ à direita do número,
e isso desconsidera o comprimento da linha. `newline()`, que irá ser chamada automaticamente a partir de `stringproc.lisp` 
pode ser útil, se você desejar colocar uma parada de linha intermediária.








```maxima
(%i1) for n:0 thru 22 do sprint( fib(n) )$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), if mod(n,10)=9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

<!-- category: IO -->
<!-- keywords: sremove -->
<!-- signatures: sremove(seq, seq_caracte), sremove(seq, seq_caracte, test), sremove(seq, seq_caracte, test, início), sremove(seq, seq_caracte, test, início, fim) -->
### Function: sremove (seq, seq_caracte)

Retorna uma sequência de caracteres como *seq_caracte* mas com todas as subsequências de caracteres que coincidirem com *seq*.
A função padrão de teste de coincidência é `sequal`.
Se `sremove` puder ignorar a caixa alta/baixa enquanto busca por *seq*, use `sequalignore` como teste.
Use *início* e *fim* para limitar a busca.
Note que o primeiro caractere em *seq_caracte* está na posição 1.







```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

<!-- category: IO -->
<!-- keywords: sremovefirst -->
<!-- signatures: sremovefirst(seq, seq_caracte), sremovefirst(seq, seq_caracte, test), sremovefirst(seq, seq_caracte, test, início), sremovefirst(seq, seq_caracte, test, início, fim) -->
### Function: sremovefirst (seq, seq_caracte)

Como em `sremove` exceto qie a primeira subsequência de caracteres que coincide com `seq` é removida.

<!-- category: IO -->
<!-- keywords: sreverse -->
<!-- signatures: sreverse(seq_caracte) -->
### Function: sreverse (seq_caracte)

Retorna uma sequência de caracteres com todos os caracteres de *seq_caracte* em ordem reversa.

<!-- category: IO -->
<!-- keywords: ssearch -->
<!-- signatures: ssearch(seq, seq_caracte), ssearch(seq, seq_caracte, test), ssearch(seq, seq_caracte, test, início), ssearch(seq, seq_caracte, test, início, fim) -->
### Function: ssearch (seq, seq_caracte)

Retorna a posição da primeira subsequência de caracteres de *seq_caracte* que coincide com a sequência de caracteres *seq*.
A função padrão de teste de coincidência é `sequal`.
Se `ssearch` puder igonorar a caixa alta/baixa, use `sequalignore` como função de teste.
Use *início* e *fim* para limitar a busca.
Note que o primeiro caractere em *seq_caracte* está na posição 1.



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

<!-- category: IO -->
<!-- keywords: ssort -->
<!-- signatures: ssort(seq_caracte), ssort(seq_caracte, test) -->
### Function: ssort (seq_caracte)

Retorna uma sequência de caracteres que contém todos os caracteres de *seq_caracte* em uma ordem tal que não existam dois caracteres *c* sucessivos e *d* seja tal que `test (c, d)` seja `false` e `test (d, c)` seja `true`.
A função padrão de teste para ordenaçào é *clessp*.
O conjunto de funções de teste é `{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`.







```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

<!-- category: IO -->
<!-- keywords: ssubst -->
<!-- signatures: ssubst(nova, antiga, seq_caracte), ssubst(nova, antiga, seq_caracte, test), ssubst(nova, antiga, seq_caracte, test, início), ssubst(nova, antiga, seq_caracte, test, início, fim) -->
### Function: ssubst (nova, antiga, seq_caracte)

Retorna uma sequência de caracteres como *seq_caracte* exceto que todas as subsequências de caracteres que coincidirem com *antiga* são substituídas por *nova*.
*antiga* e *nova* não precisam ser de mesmo comprimento.
A função padrão de teste para coincidência é para coincidências é `sequal`.
Se `ssubst` puder ignorar a cixa alta/baixa enquanto procurando por *antiga*, use `sequalignore` como função de teste.
Use *início* e *fim* para limitar a busca.
Note que o primeiro caractere em *seq_caracte* está na posição 1.







```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

<!-- category: IO -->
<!-- keywords: ssubstfirst -->
<!-- signatures: ssubstfirst(nova, antiga, seq_caracte), ssubstfirst(nova, antiga, seq_caracte, test), ssubstfirst(nova, antiga, seq_caracte, test, início), ssubstfirst(nova, antiga, seq_caracte, test, início, fim) -->
### Function: ssubstfirst (nova, antiga, seq_caracte)

Como em `subst` exceto que somente a primeira subsequência de caracteres que coincidir com *antiga* é substituída.

<!-- category: IO -->
<!-- keywords: strim -->
<!-- signatures: strim(seq, seq_caracte) -->
### Function: strim (seq, seq_caracte)

Retorna uma sequência de caracteres como *seq_caracte*,
mas com todos os caracteres que aparecerem em *seq* removidos de ambas as extremidades. 








```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

<!-- category: IO -->
<!-- keywords: striml -->
<!-- signatures: striml(seq, seq_caracte) -->
### Function: striml (seq, seq_caracte)

Como em `strim` exceto que somente a extremidade esquerda de *seq_caracte* é recordada.

<!-- category: IO -->
<!-- keywords: strimr -->
<!-- signatures: strimr(seq, seq_caracte) -->
### Function: strimr (seq, seq_caracte)

Como em `strim` exceto que somente a extremidade direita de sequência de caracteres é recortada.

<!-- category: IO -->
<!-- keywords: stringp -->
<!-- signatures: stringp(obj) -->
### Function: stringp (obj)

Retorna `true` se *obj* for uma sequência de caracteres do Maxima.
Veja a introdução para obter exemplos.

<!-- category: IO -->
<!-- keywords: substring -->
<!-- signatures: substring(seq_caracte, início), substring(seq_caracte, início, fim) -->
### Function: substring (seq_caracte, início)

Retorna a subsequência de caracteres de *seq_caracte* começando na posição *início* e terminando na posição *fim*.
O caractere na posição *fim* não é incluído.
Se *fim* não for fornecido, a subsequência de caracteres contém o restante da sequência de caracteres.
Note que o primeiro caractere em *seq_caracte* está na posição 1.







```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

<!-- category: IO -->
<!-- keywords: sunlisp -->
<!-- signatures: sunlisp(lisp_string) -->
### Function: sunlisp (lisp_string)

Converte uma sequência de caracteres do Lisp em uma sequência de caracteres do Maxima.
(Em geral você pode não precisar dessa função.)

<!-- category: IO -->
<!-- keywords: supcase -->
<!-- signatures: supcase(seq_caracte), supcase(seq_caracte, início), supcase(seq_caracte, início, fim) -->
### Function: supcase (seq_caracte)

Retorna *seq_caracte* exceto que caracteres em caixa baixa a partir da posição *início* até a posição *fim* são substituídos pelo correspondente caracteres em caixa alta.
Se *fim* não for fornecido,
todos os caracteres em caixa baixa de *início* até o fim de *seq_caracte* são substituídos.






```maxima
(%i1) load("stringproc")$
(%i1) supcase("english",1,2);
(%o1)                        English
```

<!-- category: IO -->
<!-- keywords: tab -->
<!-- signatures: tab -->
### Variable: tab

O caractere de tabulação.

<!-- category: IO -->
<!-- keywords: tokens -->
<!-- signatures: tokens(seq_caracte), tokens(seq_caracte, test) -->
### Function: tokens (seq_caracte)

Retorna uma lista de fichas, que tiverem sido extrídos de *seq_caracte*.
As fichas são subsequências de caracteres cujos caracteres satisfazem a uma determinada função de teste.
Se o teste não for fornecido, *constituent* é usada como teste padrão.
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}` é o conjunto de fnções de teste. 
(A verão Lisp de `tokens` é escrita por Paul Graham. ANSI Common Lisp, 1996, page 67.)









```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parsetoken,%);
(%o3)                      [5, 10, 24]
```

<!-- category: IO -->
<!-- keywords: uppercasep -->
<!-- signatures: uppercasep(caractere) -->
### Function: uppercasep (caractere)

Retorna `true` se *caractere* for um caractere em caixa alta.

