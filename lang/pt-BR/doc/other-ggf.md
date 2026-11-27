## ggf

<!-- category: Other -->
<!-- keywords: ggf -->
<!-- signatures: ggf(l) -->
### Function: ggf (l)

Calcula a função geradora (se for uma fração de dois
polinômios) de uma sequência, sendo dados seus primeiros termos. *l*
é uma lista de números.


A solução é retornada como uma fração de dois polinômios.
Se nenhuma solução tiver sido encontrada, é retornado `done`.


Essa função é controlada attravés das variáveis globais *GGFINFINITY* e *GGFCFMAX*. Veja também *GGFINFINITY* e *GGFCFMAX*.


Para usar essa função primeiro escreva `load("ggf")`.

<!-- category: Other -->
<!-- keywords: GGFCFMAX -->
<!-- signatures: GGFCFMAX -->
### Variable: GGFCFMAX

Valor padrão: 3


Essa é uma variável de opção para a função `ggf`.


Quando calculando a fração contínua da
função geradora, se nenhum bom resultado for encontrado (veja
o sinalizador *GGFINFINITY*) após se ter calculado uma quantidade de *GGFCFMAX* quocientes
parciais, a função geradora será considerada como
não sendo uma fração de dois polinômios e a função irá
terminar. Coloque livemente um valor muito grande para funções geradoras
mais complicadas.


Veja também `ggf`.

<!-- category: Other -->
<!-- keywords: GGFINFINITY -->
<!-- signatures: GGFINFINITY -->
### Variable: GGFINFINITY

Valor padrão: 3


Essa é uma variável de opção para a função `ggf`.


Quando calculando a fração contínua da
função geradora, um quociente parcial tendo um grau
(estritamente) maior que *GGFINFINITY* será descartado e
o convergente atual será considerado como o valor exato
da função geradora; na grande mioria dos casos o grau de todos
os quocientes parciais será ou 0 ou 1; se você usar um valor muito grande,
então você poderá fornecer termos suficientes com o objetivo de fazer o
cálculo preciso o bastante.



Veja também `ggf`.

