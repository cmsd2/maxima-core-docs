## Detecção e Relato de Erros

<!-- category: Other -->
<!-- keywords: run_testsuite -->
<!-- signatures: run_testsuite(), run_testsuite(boolean), run_testsuite(boolean, boolean), run_testsuite(boolean, boolean, list) -->
### Function: run_testsuite ()

Executa o conjunto de testes do Maxima.  Testes que produzem a resposta
desejada são considerados “aprovações” (em inglês, passes) e testes que
não produzem a resposta desejada são marcados como erros.


`run_testsuite ()` mostra somente testes que não são aprovados.


`run_testsuite (true)` mostra somente testes que são marcados como
erros, bem como as falhas.


`run_testsuite (true, true)` mostra todos os testes.


Se for usado o terceiro argumento opcional, que deve ser uma lista,
executam-se unicamente os testes indicados nessa lista. Os nomes de
todos os testes é especificado por `testsuite_files`.


`run_testsuite` altera a variável de ambiente Maxima.  Tipicamente
um script de teste executa `kill` para estabelecer uma variável de
ambiente (uma a saber sem funções definidas pelo utilizador e variáveis)
e então define funções e variáveis apropriadamente para o teste.


`run_testsuite` retorna `done`.

