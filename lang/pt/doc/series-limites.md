## Limites

<!-- category: Series -->
<!-- keywords: lhospitallim -->
<!-- signatures: lhospitallim -->
### Variable: lhospitallim

Valor por omissão: 4


`lhospitallim` é o máximo número de vezes que a regra
L’Hospital é usada em `limit`.  Isso evita ciclos infinitos em casos como
`limit (cot(x)/csc(x), x, 0)`.

<!-- category: Series -->
<!-- keywords: limit -->
<!-- signatures: limit(expr, x, val, dir), limit(expr, x, val), limit(expr) -->
### Function: limit (expr, x, val, dir)

Calcula o limite de *expr* com a variável real
*x* aproximando-se do valor *val* pela direção *dir*.  *dir* pode ter o
valor `plus` para um limite pela direita, `minus` para um limite pela esquerda, ou
pode ser omitido (implicando em um limite em ambos os lados é para ser computado).


`limit` usa os
seguintes símbolos especiais: `inf` (infinito positivo) e `minf` (infinito
negativo).  Em saídas essa função pode também usar `und` (undefined - não definido), `ind` (indefinido
mas associado) e `infinity` (infinito complexo).


`lhospitallim` é o máximo número de vezes que a regra
L’Hospital é usada em `limit`.  Isso evita ciclos infinitos em casos como
`limit (cot(x)/csc(x), x, 0)`.


`tlimswitch` quando `true` fará o pacote `limit` usar
série de Taylor quando possível.


`limsubst` evita que `limit` tente substituições sobre
formas desconhecidas.  Isso é para evitar erros como `limit (f(n)/f(n+1), n, inf)`
dando igual a 1.  Escolhendo `limsubst` para `true` permitirá tais
substituições.


`limit` com um argumento é muitas vezes chamado em ocasiões para simplificar expressões de constantes,
por exemplo, `limit (inf-1)`.



`example (limit)` mostra alguns exemplos.


Para saber sobre o método utilizado veja Wang, P., "Evaluation of Definite Integrals by Symbolic
Manipulation", tese de Ph.D., MAC TR-92, Outubro de 1971.

<!-- category: Series -->
<!-- keywords: limsubst -->
<!-- signatures: limsubst -->
### Variable: limsubst

valor padrão: `false` - evita que `limit` tente substituições sobre
formas desconhecidas.  Isso é para evitar erros como `limit (f(n)/f(n+1), n, inf)`
dando igual a 1.  Escolhendo `limsubst` para `true` permitirá tais
substituições.

<!-- category: Series -->
<!-- keywords: tlimit -->
<!-- signatures: tlimit(expr, x, val, dir), tlimit(expr, x, val), tlimit(expr) -->
### Function: tlimit (expr, x, val, dir)

Retorna `limit` com `tlimswitch` escolhido para `true`.

<!-- category: Series -->
<!-- keywords: tlimswitch -->
<!-- signatures: tlimswitch -->
### Variable: tlimswitch

Valor por omissão: `false`


Quando `tlimswitch` for `true`, fará o pacote `limit` usar
série de Taylor quando possível.

