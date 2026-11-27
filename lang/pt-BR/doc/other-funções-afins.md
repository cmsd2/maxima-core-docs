## Funções Afins

<!-- category: Other -->
<!-- keywords: all_dotsimp_denoms -->
<!-- signatures: all_dotsimp_denoms -->
### Variable: all_dotsimp_denoms

Valor padrão: `false`


Quando `all_dotsimp_denoms` é uma lista,
os denominadores encontrados por `dotsimp` são adicionados ao final da lista.
`all_dotsimp_denoms` pode ser iniciado como uma lista vazia `[]`
antes chamando `dotsimp`.


Por padrão, denominadores não são coletados por `dotsimp`.

<!-- category: Other -->
<!-- keywords: check_overlaps -->
<!-- signatures: check_overlaps(n, add_to_simps) -->
### Function: check_overlaps (n, add_to_simps)

Verifica as sobreposies através do grau *n*,
tendo certeza que você tem regras de simplificação suficiente em cada
grau, para `dotsimp` trabalhar corretamente.  Esse processo pode ter sua velocidade aumentada
se você souber antes de começar souber de qual dimensão do espaço de monômios é.
Se ele for de dimensão global finita, então `hilbert` pode ser usada.  Se você
não conhece as dimensões monomiais, não especifique um `rank_function`.
Um opcional terceiro argumento `reset`, `false` diz para não se incomodar em perguntar
sobre resetar coisas.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: declare_weights -->
<!-- signatures: declare_weights(x_1, w_1, ..., x_n, w_n) -->
### Function: declare_weights (x_1, w_1, ..., x_n, w_n)

Atribui pesos *w_1*, ..., *w_n* to *x_1*, ..., *x_n*, respectivamente.
Esses são pesos usados em cálculos `nc_degree`.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: dotsimp -->
<!-- signatures: dotsimp(f) -->
### Function: dotsimp (f)

Retorna 0 se e somente se *f* for um ideal gerado pelas equações, i.e.,
se e somente se *f* for uma combinação polinomial dos elementos das equações.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: extract_linear_equations -->
<!-- signatures: extract_linear_equations([p_1, ..., p_n], [m_1, ..., m_n]) -->
### Function: extract_linear_equations ([p_1, ..., p_n], [m_1, ..., m_n])

Faz uma lista dos coeficientes dos polinômios não comutativos *p_1*, ..., *p_n*
dos monomios não comutatvos *m_1*, ..., *m_n*.
Os coeficientes podem ser escalares.   Use `list_nc_monomials` para construir a lista dos
monômios.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: fast_central_elements -->
<!-- signatures: fast_central_elements([x_1, ..., x_n], n) -->
### Function: fast_central_elements ([x_1, ..., x_n], n)

Se `set_up_dot_simplifications` tiver sido feito previamente, ache o polinômio central
nas variáveis *x_1*, ..., *x_n* no grau dado, *n*.


Por exemplo:


```maxima
set_up_dot_simplifications ([y.x + x.y], 3);
fast_central_elements ([x, y], 2);
[y.y, x.x];
```


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: fast_linsolve -->
<!-- signatures: fast_linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: fast_linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resolve equações lineares simultâneas *expr_1*, ..., *expr_m*
para as variáveis *x_1*, ..., *x_n*.
Cada *expr_i* pode ser uma equação ou uma expressão geral;
se dada como uma expressão geral, ela  tratada como uma equação na forma `expr_i = 0`.


O valor de retorno é uma lista de equações da forma
`[x_1 = a_1, ..., x_n = a_n]`
onde *a_1*, ..., *a_n* são todas livres de *x_1*, ..., *x_n*.


`fast_linsolve` é mais rápido que `linsolve` para sistemas de equações que
são esparsas.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: grobner_basis -->
<!-- signatures: grobner_basis([expr_1, ..., expr_m]) -->
### Function: grobner_basis ([expr_1, ..., expr_m])

Retorna uma base de Groebner para as equações *expr_1*, ..., *expr_m*.
A funçã `polysimp` pode então
ser usada para simplificar outras funções relativas às equações.



```maxima
grobner_basis ([3*x^2+1, y*x])$

polysimp (y^2*x + x^3*9 + 2) ==> -3*x + 2
```


`polysimp(f)` produz 0 se e somente se *f* está no ideal gerado por
*expr_1*, ..., *expr_m*, isto é,
se e somente se *f* for uma combinação polinomial dos elementos de
*expr_1*, ..., *expr_m*.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: list_nc_monomials -->
<!-- signatures: list_nc_monomials([p_1, ..., p_n]), list_nc_monomials(p) -->
### Function: list_nc_monomials ([p_1, ..., p_n])

Retorna uma lista de monômios não comutativos que ocorrem em um polinômio *p*
ou em uma lista de polinômios *p_1*, ..., *p_n*.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: mono -->
<!-- signatures: mono([x_1, ..., x_n], n) -->
### Function: mono ([x_1, ..., x_n], n)

Retorna a lista de monômios independentes
relativamente à simplificação atual do grau *n*
nas variáveis *x_1*, ..., *x_n*.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: monomial_dimensions -->
<!-- signatures: monomial_dimensions(n) -->
### Function: monomial_dimensions (n)

Calcula a série de Hilbert através do grau *n* para a algebra corrente.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: nc_degree -->
<!-- signatures: nc_degree(p) -->
### Function: nc_degree (p)

Retorna o grau de um polinômio não comutativo *p*.  Veja `declare_weights`.


Para usar essa função escreva primeiramente `load("affine")`.

<!-- category: Other -->
<!-- keywords: set_up_dot_simplifications -->
<!-- signatures: set_up_dot_simplifications(eqns, check_through_degree), set_up_dot_simplifications(eqns) -->
### Function: set_up_dot_simplifications (eqns, check_through_degree)

As *eqns* são
equações polinomiais em variáveis não comutativas.
O valor de `current_variables`  é uma 
lista de variáveis usadas para calcular graus.  As equações devem ser
homogêneas, com o objetivo de que o procedimento termine.  


Se você checou simplificações de envoltório em `dot_simplifications`
acima do grau de *f*, então o seguinte é verdadeiro:
`dotsimp (f)` retorna 0 se e somente se *f* está no
ideal gerado pelas equações, i.e.,
se e somente se *f* for uma combinação polinomial
dos elementos das equações.


O grau é aquele retornado por `nc_degree`.   Isso por sua vez é nfluenciado pelos
pesos das variáveis individuais.


Para usar essa função escreva primeiramente `load("affine")`.

