## Detecção e Relato de Erros

<!-- category: Other -->
<!-- keywords: bug_report -->
<!-- signatures: bug_report() -->
### Function: bug_report ()

Imprime os números de versão do Maxima e do Lisp, e chama o link
para a página web de informação de erros do projeto Maxima.
A informação da versão é a mesma reportada por `build_info`.


Quando um erro é informado, é muito útil copiar a versão do Maxima
e do Lisp dentro da informação do erro.


`bug_report` retorna uma sequência de caracteres vazia `""`.

<!-- category: Other -->
<!-- keywords: build_info -->
<!-- signatures: build_info() -->
### Function: build_info ()

Imprime um sumário de parâmetros da compilação do Maxima.


`build_info` retorna uma sequência de caracteres vazia `""`.

<!-- category: Other -->
<!-- keywords: run_testsuite -->
<!-- signatures: run_testsuite(), run_testsuite(boolean), run_testsuite(boolean, boolean), run_testsuite(boolean, boolean, list) -->
### Function: run_testsuite ()

Executa o conjunto de testes do Maxima.  Testes que produzem a resposta desejada são
considerados “passes,” e testes que não produzem a resposta
desejada, são marcados como erros conhecidos.


`run_testsuite ()` mostra somente testes que não são aprovados.


`run_testsuite (true)` mostra somente testes que são marcados como erros conhecidos, bem
como as falhas.


`run_testsuite (true, true)` mostra todos os testes.


Se o terceiro argumento opcional for dado, um subconjunto de testes é executado.
O subconjunto de testes para executar é dado como uma lista de nomes dos
testes.  O conjunto completo de testes é especificado por `testsuite_files`.


`run_testsuite` altera a variável de ambiente Maxima.
Tipicamente um script de teste executa `kill` para estabelecer uma variável de ambiente
(uma a saber sem funções definidas pelo usuário e variáveis)
e então define funções e variáveis apropriadamente para o teste.


`run_testsuite` retorna `done`.

<!-- category: Other -->
<!-- keywords: testsuite_files -->
<!-- signatures: testsuite_files -->
### Variable: testsuite_files

`testsuite_files` é o conjunto de testes a ser executado por
`run_testsuite`.  Isso é uma lista de nomes de arquivos contendo
os testes a executar.  Se alguns dos testes em um arquivo falha de forma conhecida,
então em lugar de listar o nome do arquivo, uma lista contendo o
nome do arquivo e o número dos testes que falharam é usada.


por exemplo, a linha adinate é uma parte do conjunto de testes padrão:



```maxima
["rtest13s", ["rtest14", 57, 63]]
```


Essa linha especifica a suite de testes que consiste dos arquivos "rtest13s" e
"rtest14", mas "rtest14" contém dois testes que falham de forma conhecida: 57
e 63.

