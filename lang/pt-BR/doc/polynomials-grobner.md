## grobner

<!-- category: Polynomials -->
<!-- keywords: poly_add -->
<!-- signatures: poly_add(poli1, poli2, varlist) -->
### Function: poly_add (poli1, poli2, varlist)

Adiciona dois polinômios *poli1* e *poli2*.


```maxima
(%i1) poly_add(z+x^2*y,x-z,[x,y,z]);
                                    2
(%o1)                              x  y + x
```

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger -->
<!-- signatures: poly_buchberger(polilist_flvarlist) -->
### Function: poly_buchberger (polilist_flvarlist)

`poly_buchberger` realiza o algorítmo de Buchberger sobre uma lista de
polinômios e retorna a base de Grobner resultante.

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger_criterion -->
<!-- signatures: poly_buchberger_criterion(polilist, varlist) -->
### Function: poly_buchberger_criterion (polilist, varlist)

Returns `true` if *polilist* is a Groebner basis with respect to the current term
order, by using the Buchberger
criterion: for every two polynomials $h1$ and $h2$ in *polilist* the
S-polynomial $S(h1,h2)$ reduces to 0 $modulo$ *polilist*.

<!-- category: Polynomials -->
<!-- keywords: poly_coefficient_ring -->
<!-- signatures: poly_coefficient_ring -->
### Variable: poly_coefficient_ring

Valor padrão: `expression_ring`


Esse comutador indica o anel de coeficiente dos polinômios que
irá ser usado em cálculos de grobner. Se não for escolhido, o anel de expressão
geral do *maxima’s* irá ser usado. Essa variável pode ser escolhida para
`ring_of_integers` se for desejado.

<!-- category: Polynomials -->
<!-- keywords: poly_colon_ideal -->
<!-- signatures: poly_colon_ideal(polilist1, polilist2, varlist) -->
### Function: poly_colon_ideal (polilist1, polilist2, varlist)

Retorna a base reduzida de Groebner do ideal quociente 


$I(polilist1):I(polilist2)$



onde $polilist1$ e $polilist2$ são duas listas de polinômios.

<!-- category: Polynomials -->
<!-- keywords: poly_content -->
<!-- signatures: poly_content(poli.varlist) -->
### Function: poly_content (poli.varlist)

`poly_content` extrai o MDC entre seus coeficientes


```maxima
(%i1) poly_content(35*y+21*x,[x,y]);
(%o1)                                  7
```

<!-- category: Polynomials -->
<!-- keywords: poly_depends_p -->
<!-- signatures: poly_depends_p(poli, var, varlist) -->
### Function: poly_depends_p (poli, var, varlist)

`poly_depends` testa se um polinômio depende da variável *var*.

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_ideal -->
<!-- signatures: poly_elimination_ideal(polilist, num, varlist) -->
### Function: poly_elimination_ideal (polilist, num, varlist)

`poly_elimination_ideal` retorna a base de grobner do $num$-ésimo ideal de eliminação de um
ideal especificado como uma lista de polinômios geradores (não necessáriamente base de Groebner)

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_order -->
<!-- signatures: poly_elimination_order -->
### Variable: poly_elimination_order

Valor padrão: `false`


Nome da ordem padrão de funções de 
eliminação. Se escolhida, irá sobrescrever as escolhas nas variáveis
`poly_primary_elimination_order` e `poly_secondary_elimination_order`.
O usuário deve garantir que essa é uma ordem de eliminação verdadeira válida
para o número de variáveis eliminadas.

<!-- category: Polynomials -->
<!-- keywords: poly_exact_divide -->
<!-- signatures: poly_exact_divide(poli1, poli2, varlist) -->
### Function: poly_exact_divide (poli1, poli2, varlist)

Divide um polinômio *poli1* por outro polinômio *poli2*. Assume que a divisão
exata (sem resto) é possível. Retorna o quociente.

<!-- category: Polynomials -->
<!-- keywords: poly_expand -->
<!-- signatures: poly_expand(poli, varlist) -->
### Function: poly_expand (poli, varlist)

Essa função transforma polinômios para a forma interna e da forma interna para a forma geral. `poly_expand`
é equivalente a `expand(poly)` se *poli* passa corretamente para
um polinômio. Se a representação não for compatível com um
polinômio nas variáveis *varlist*, o resultado é um erro.
Esse resultado em erro pode ser usado para testar se uma expressão transforma-se corretamente para a
representação interna. Os seguintes exemplos ilustra que
variáveis de funções indexadas e transcendentes são permitidas.


```maxima
(%i1) poly_expand((x-y)*(y+x),[x,y]);
                                     2    2
(%o1)                               x  - y
(%i2) poly_expand((y+x)^2,[x,y]);
                                2            2
(%o2)                          y  + 2 x y + x
(%i3) poly_expand((y+x)^5,[x,y]);
                  5      4         2  3       3  2      4      5
(%o3)            y  + 5 x y  + 10 x  y  + 10 x  y  + 5 x  y + x
(%i4) poly_expand(-1-x*exp(y)+x^2/sqrt(y),[x]);
                                          2
                                  y      x
(%o4)                       - x %e  + ------- - 1
                                       sqrt(y)

(%i5) poly_expand(-1-sin(x)^2+sin(x),[sin(x)]);
                                2
(%o5)                      - sin (x) + sin(x) - 1
```

<!-- category: Polynomials -->
<!-- keywords: poly_expt -->
<!-- signatures: poly_expt(poli, número, varlist) -->
### Function: poly_expt (poli, número, varlist)

eleva *poli* a um inteiro positivo *número*. If *número* não for um inteiro positivo um erro irá ser mostrado.


```maxima
(%i1) poly_expt(x-y,3,[x,y])-(x-y)^3,expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_gcd -->
<!-- signatures: poly_gcd(poli1, poli2, varlist) -->
### Function: poly_gcd (poli1, poli2, varlist)

Retorna máximo divisor comum de *poli1* e *poli2*.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner -->
<!-- signatures: poly_grobner(polilist, varlist) -->
### Function: poly_grobner (polilist, varlist)

Retorna uma base de Groebner do ideal gerado pelos polinômios *polilist*. Afetado pelos sinalizadores globais.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_algorithm -->
<!-- signatures: poly_grobner_algorithm -->
### Variable: poly_grobner_algorithm

Valor padrão: `buchberger`


Valores possíveis: 


- * 
`buchberger`
- * 
`parallel_buchberger`
- * 
`gebauer_moeller`


O nome do algorítmo usado para encontrar as bases de Groebner.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_debug -->
<!-- signatures: poly_grobner_debug -->
### Variable: poly_grobner_debug

Valor padrão: `false`


Se escolhida para `true`, produz saída de depuração e rastros.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_equal -->
<!-- signatures: poly_grobner_equal(polilist1, polilist2, varlist) -->
### Function: poly_grobner_equal (polilist1, polilist2, varlist)

`poly_grobner_equal` testa se duas bases de Groebner geram o mesmo ideal.
Retorna `true` se as duas listas de polinômios *polilist1* e *polilist2*, assumidas serem bases de Groebner,
geram o mesmo ideal, e `false` de outra forma.
Isso é equivalente a verificar que todo polinômio da primeira base é reduzido a 0
módulo a segunda base e vice-versa. Note que no exemplo abaixo a
primeira lista não é uma base de Groebner, e dessa forma o resultado é `false`.



```maxima
(%i1) poly_grobner_equal([y+x,x-y],[x,y],[x,y]);
(%o1)                         false
```

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_member -->
<!-- signatures: poly_grobner_member(poli, polilist, varlist) -->
### Function: poly_grobner_member (poli, polilist, varlist)

Retorna `true` se um polinômio *poli* pertence ao ideal gerado pela
lista polinomial *polilist*, que é assumida como sendouma base de Groebner. Retorna `false` de outra forma.


`poly_grobner_member` testa se um polinômio pertence a um ideal gerado por uma lista de polinômios,
que é assumida ser uma base de Groebner. Equivale a `normal_form` sendo 0.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_subsetp -->
<!-- signatures: poly_grobner_subsetp(polilist1, polilist2, varlist) -->
### Function: poly_grobner_subsetp (polilist1, polilist2, varlist)

`poly_grobner_subsetp` testa se um ideal gerado pela *polilist1*
está contido em um ideal gerado pela *polilist2*. Para esse teste sempre tenha sucesso,
*polilist2* deve ser uma base de Groebner.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_intersection -->
<!-- signatures: poly_ideal_intersection(polilist1, polilist2, varlist) -->
### Function: poly_ideal_intersection (polilist1, polilist2, varlist)

`poly_ideal_intersection` retorna a intersecção entre dois ideais.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation -->
<!-- signatures: poly_ideal_polysaturation(polilist, polilistlist, varlist) -->
### Function: poly_ideal_polysaturation (polilist, polilistlist, varlist)

*polilistlist* is a list of n list of polynomials `[polylist1,...,polylistn]`.
Retorna a base reduzida de Groebner da saturação do ideal


I(polylist):I(polylist_1)^inf:...:I(polylist_n)^inf

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation1 -->
<!-- signatures: poly_ideal_polysaturation1(polilist1, polilist2, varlist) -->
### Function: poly_ideal_polysaturation1 (polilist1, polilist2, varlist)

*polilist2* ist a list of n polynomials `[poly1,...,polyn]`.
Retorna a base de Groebner reduzida do ideal


I(polylist):poly1^inf:...:polyn^inf



obtido por uma
sequência de sucessivas saturações nos polinômios
da lista  polinômial *polilist2* do ideal gerado pela
lista polinomial *polilist1*.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation -->
<!-- signatures: poly_ideal_saturation(polilist1, polilist2, varlist) -->
### Function: poly_ideal_saturation (polilist1, polilist2, varlist)

Retorna a base de Groebner reduzida da saturação do ideal


I(polylist1):I(polylist2)^inf



Geometricamente, sobre um corpo algebricamente fechado, esse é um conjunto
de polinmios no ideal gerado por *polilist1* que não tende identicamente a
zero sobre a variação de *polilist2*.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation1 -->
<!-- signatures: poly_ideal_saturation1(polilist, poli, varlist) -->
### Function: poly_ideal_saturation1 (polilist, poli, varlist)

Retorna abase de Groebner reduzida da saturação do ideal


I(polylist):poly^inf



Geometricamente, sobre um corpo algebricamente fechado, esse é um conjunto
de polinmios no ideal gerado por *polilist* que não tende identicamente a
zero sobre a variação de *poli*.

<!-- category: Polynomials -->
<!-- keywords: poly_lcm -->
<!-- signatures: poly_lcm(poli1, poli2, varlist) -->
### Function: poly_lcm (poli1, poli2, varlist)

Retorna o mínimo múltiplo comum entre *poli1* e *poli2*.

<!-- category: Polynomials -->
<!-- keywords: poly_minimization -->
<!-- signatures: poly_minimization(polilist, varlist) -->
### Function: poly_minimization (polilist, varlist)

Retorna uma sublista da lista de polinômios *polilist* gerando o mesmo
ideal de monômio que *polilist* mas minimo, i.e. nenhum monômio líder
de um polinômio na sublista divide o monômio líder
de outro polinômio.

<!-- category: Polynomials -->
<!-- keywords: poly_monomial_order -->
<!-- signatures: poly_monomial_order -->
### Variable: poly_monomial_order

Valor padrão: `lex`


Esse comutador globalcontrola qual a ordenação monomial é usada em polinomio e em cálculos com Bases de Groebner. Se não for escolhidat, `lex` será usada.

<!-- category: Polynomials -->
<!-- keywords: poly_multiply -->
<!-- signatures: poly_multiply(poli1, poli2, varlist) -->
### Function: poly_multiply (poli1, poli2, varlist)

Retorna o produto dos polinômios *poli1* e *poli2*.


```maxima
(%i2) poly_multiply(z+x^2*y,x-z,[x,y,z])-(z+x^2*y)*(x-z),expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_normal_form -->
<!-- signatures: poly_normal_form(poli, polilist, varlist) -->
### Function: poly_normal_form (poli, polilist, varlist)

`poly_normal_form` encontra a forma normal de um polinômio *poli* com relação a
um conjunto de polinômios *polilist*.

<!-- category: Polynomials -->
<!-- keywords: poly_normalize -->
<!-- signatures: poly_normalize(poli, varlist) -->
### Function: poly_normalize (poli, varlist)

Retorna o polinômio *poli* dividido pelo coeficiente lider.
`poly_normalize` assume que a divisão é possível, o que nem sempre ocorre
em anéis que não são corpos (fields).

<!-- category: Polynomials -->
<!-- keywords: poly_normalize_list -->
<!-- signatures: poly_normalize_list(polilist, varlist) -->
### Function: poly_normalize_list (polilist, varlist)

`poly_normalize_list` aplica `poly_normalize` a cada polinômio na lista.
Que significa que `poly_normalize_list` divide todo polinômio em uma lista *polilist* por seu coeficiente líder.

<!-- category: Polynomials -->
<!-- keywords: poly_primary_elimination_order -->
<!-- signatures: poly_primary_elimination_order -->
### Variable: poly_primary_elimination_order

Valor padrão: `false`


Nome da ordem padrão de eliminação de variáveis em
funções de eliminação. Se não for escolhida, `lex` irá ser usada.

<!-- category: Polynomials -->
<!-- keywords: poly_primitive_part -->
<!-- signatures: poly_primitive_part(poli1, varlist) -->
### Function: poly_primitive_part (poli1, varlist)

Retorna o polinômio *poli* dividido pelo MDC entre seus coeficientes. 



```maxima
(%i1) poly_primitive_part(35*y+21*x,[x,y]);
(%o1)                              5 y + 3 x
```

<!-- category: Polynomials -->
<!-- keywords: poly_pseudo_divide -->
<!-- signatures: poly_pseudo_divide(poli, polilist, varlist) -->
### Function: poly_pseudo_divide (poli, polilist, varlist)

Realiza a divisão falsa do polinômio *poli* pela lista de $n$ polinômios *polilist*. Retorna
multiplos valores. O primeiro valor é uma lista de quocientes $a$. O
segundo valor é o resto $r$. O terceiro argumento é um coeficiente
escalar $c$, tal que $c*poli$ pode ser dividido por*polilist* dentro do anel
dos coeficientes, que não é necessáriamente corpo. Finalmente, o
quarto valor é um contador inteiro do número de reduções
realizadas. O objetos resultantes satisfazem à equação:


$c*poly=sum(a[i]*polylist[i],i=1...n)+r$.

<!-- category: Polynomials -->
<!-- keywords: poly_reduced_grobner -->
<!-- signatures: poly_reduced_grobner(polilist, varlist) -->
### Function: poly_reduced_grobner (polilist, varlist)

Retorna uma base de Groebner reduzida do ideal gerado pelos polinômios *polilist*. Afetado pelos sinalizadores globais.

<!-- category: Polynomials -->
<!-- keywords: poly_reduction -->
<!-- signatures: poly_reduction(polilist, varlist) -->
### Function: poly_reduction (polilist, varlist)

`poly_reduction` reduz uma lista de polinômios *polilist*, de forma que
cada poinômio é completametne reduzido com relação a outros polinômios.

<!-- category: Polynomials -->
<!-- keywords: poly_return_term_list -->
<!-- signatures: poly_return_term_list -->
### Variable: poly_return_term_list

Valor padrão: `false`


Se escolhida para `true`, todas as funções no pacote `grobner` irão retornar cada
polinômio como uma lista de termos na ordem monomial corrente em lugar de
retornar uma expressão geral do *maxima*.

<!-- category: Polynomials -->
<!-- keywords: poly_s_polynomial -->
<!-- signatures: poly_s_polynomial(poli1, poli2, varlist) -->
### Function: poly_s_polynomial (poli1, poli2, varlist)

Retorna o *polinômio syzygy* (*S-polinomial*) de dois polinômios *poli1* e *poli2*.

<!-- category: Polynomials -->
<!-- keywords: poly_saturation_extension -->
<!-- signatures: poly_saturation_extension(poli, polilist, varlist1, varlist2) -->
### Function: poly_saturation_extension (poli, polilist, varlist1, varlist2)

`poly_saturation_extension` implementa o famoso artifício de Rabinowitz.

<!-- category: Polynomials -->
<!-- keywords: poly_secondary_elimination_order -->
<!-- signatures: poly_secondary_elimination_order -->
### Variable: poly_secondary_elimination_order

Valor padrão: `false`


Nome da ordem padrão para manter variáveis em funções de eliminação. Se não for escolhida, `lex` irá ser usada.

<!-- category: Polynomials -->
<!-- keywords: poly_subtract -->
<!-- signatures: poly_subtract(poli1, poli2, varlist) -->
### Function: poly_subtract (poli1, poli2, varlist)

Subtrai o polinômio *poli2* do polinômio *poli1*.


```maxima
(%i1) poly_subtract(z+x^2*y,x-z,[x,y,z]);
                                      2
(%o1)                          2 z + x  y - x
```

<!-- category: Polynomials -->
<!-- keywords: poly_top_reduction_only -->
<!-- signatures: poly_top_reduction_only -->
### Variable: poly_top_reduction_only

Valor padrão: `false`


Se não for `false`, usa redução de topo somente se for possível. Redução de
topo significa que o algorítmo de divisão para após a primeira
redução.

