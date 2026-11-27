## grobner

<!-- category: Polynomials -->
<!-- keywords: poly_add -->
<!-- signatures: poly_add(poly1, poly2, varlist) -->
### Function: poly_add (poly1, poly2, varlist)

Suma los polinomios *poly1* y *poly2*.


```maxima
(%i1) poly_add(z+x^2*y,x-z,[x,y,z]);
                                    2
(%o1)                              x  y + x
```

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger -->
<!-- signatures: poly_buchberger(polylist_flvarlist) -->
### Function: poly_buchberger (polylist_flvarlist)

`poly_buchberger` ejecuta el algoritmo de Buchberger sobre una
lista de polinomios y devuelve la base de Groebner resultante.

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger_criterion -->
<!-- signatures: poly_buchberger_criterion(polylist, varlist) -->
### Function: poly_buchberger_criterion (polylist, varlist)

Devuelve `true` si *polylist* es una base de Groebner respecto del orden 
de términos activo, utilizando el criterio de Buchberger: 
para cualesquiera polinomios $h1$ y $h2$ de *polylist* el
S-polinomio $S(h1,h2)$ se reduce a 0 $modulo$ *polylist*.

<!-- category: Polynomials -->
<!-- keywords: poly_coefficient_ring -->
<!-- signatures: poly_coefficient_ring -->
### Variable: poly_coefficient_ring

Valor por defecto: `expression_ring`


Indica el anillo de coeficientes de los polinomios que se va
a utilizar en los cálculos. Si no se le asigna ningún valor,
se utilizará el anillo de expresiones propio de *maxima*.
A esta variable se le puede asignar el valor `ring_of_integers`.

<!-- category: Polynomials -->
<!-- keywords: poly_colon_ideal -->
<!-- signatures: poly_colon_ideal(polylist1, polylist2, varlist) -->
### Function: poly_colon_ideal (polylist1, polylist2, varlist)

Devuelve la base de Groebner reducida del ideal


$I(polylist1):I(polylist2)$



siendo $polylist1$ y $polylist2$ dos listas de polinomios.

<!-- category: Polynomials -->
<!-- keywords: poly_content -->
<!-- signatures: poly_content(poly.varlist) -->
### Function: poly_content (poly.varlist)

`poly_content` calcula el MCD de los coeficientes.


```maxima
(%i1) poly_content(35*y+21*x,[x,y]);
(%o1)                                  7
```

<!-- category: Polynomials -->
<!-- keywords: poly_depends_p -->
<!-- signatures: poly_depends_p(poly, var, varlist) -->
### Function: poly_depends_p (poly, var, varlist)

`poly_depends` comprueba si el polinomio depende de la variable *var*.

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_ideal -->
<!-- signatures: poly_elimination_ideal(polylist, n, varlist) -->
### Function: poly_elimination_ideal (polylist, n, varlist)

`poly_elimination_ideal` devuelve la base de Groebner del $n$-ésimo
ideal de eliminación de un ideal especificado como una lista de polinomios
generadores (no necesariamente una base de Groebner).

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_order -->
<!-- signatures: poly_elimination_order -->
### Variable: poly_elimination_order

Valor por defecto: `false`


Nombre del orden de eliminación por defecto utilizado en
los cálculos de eliminación. Si se le asigna un valor,
ignorará los guardados en `poly_primary_elimination_order`
y `poly_secondary_elimination_order`.
El usuario se asegurará que este es un orden válido de eliminación.

<!-- category: Polynomials -->
<!-- keywords: poly_exact_divide -->
<!-- signatures: poly_exact_divide(poly1, poly2, varlist) -->
### Function: poly_exact_divide (poly1, poly2, varlist)

Divide el polinomio *poly1* por otro polinomio *poly2*. Da por supuesto
que es posible la división de resto nulo. Devuelve el cociente.

<!-- category: Polynomials -->
<!-- keywords: poly_expand -->
<!-- signatures: poly_expand(poly, varlist) -->
### Function: poly_expand (poly, varlist)

Esta función expande los polinomios. Equivale a `expand(poly)`
si *poly* es un polinomio. Si la representación no es compatible 
con un polinomio de variables *varlist*, devuelve un error.


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
<!-- signatures: poly_expt(poly, number, varlist) -->
### Function: poly_expt (poly, number, varlist)

Eleva el polinomio *poly* a la potencia *number*, siendo este un entero
positivo. Si *number* no es un número entero positivo, devolverá un error.


```maxima
(%i1) poly_expt(x-y,3,[x,y])-(x-y)^3,expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_gcd -->
<!-- signatures: poly_gcd(poly1, poly2, varlist) -->
### Function: poly_gcd (poly1, poly2, varlist)

Devuelve el MCD de *poly1* y *poly2*.


Véanse también `ezgcd`, `gcd`, `gcdex` y
`gcdivide`.


Ejemplo:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) poly_gcd(p1, p2, [x]);
                            2
(%o3)                    6 x  + 13 x + 6
```

<!-- category: Polynomials -->
<!-- keywords: poly_grobner -->
<!-- signatures: poly_grobner(polylist, varlist) -->
### Function: poly_grobner (polylist, varlist)

Devuelve la base de Groebner del ideal asociado a los polinomios
de *polylist*. El resultado depende de las variables globales.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_algorithm -->
<!-- signatures: poly_grobner_algorithm -->
### Variable: poly_grobner_algorithm

Valor por defecto: `buchberger`


Valores posibles: 


- * 
`buchberger`
- * 
`parallel_buchberger`
- * 
`gebauer_moeller`


Es el nombre del algoritmo utilizado para encontrar las bases de Groebner.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_debug -->
<!-- signatures: poly_grobner_debug -->
### Variable: poly_grobner_debug

Valor por defecto: `false`


Si vale `true`, genera una salida de seguimiento y depuración.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_equal -->
<!-- signatures: poly_grobner_equal(polylist1, polylist2, varlist) -->
### Function: poly_grobner_equal (polylist1, polylist2, varlist)

`poly_grobner_equal` comprueba si dos bases de Groebner generan el mismo
ideal. Devuelve `true` si dos listas de polinomios *polylist1* y *polylist2*,
supuestas bases de Groebner, generan el mismo ideal, o `false` en caso contrario.
Eso equivale a comprobar si cada polinomio de la primera base se reduce a 0
módulo la segunda base y viceversa. Nótese que en el ejemplo que sigue la
primera lista no es una base de Groebner, por lo que el resultado es `false`.



```maxima
(%i1) poly_grobner_equal([y+x,x-y],[x,y],[x,y]);
(%o1)                         false
```

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_member -->
<!-- signatures: poly_grobner_member(poly, polylist, varlist) -->
### Function: poly_grobner_member (poly, polylist, varlist)

Devuelve `true` si el polinomio *poly* pertenece al ideal generado por la
lista de polinomios *polylist*, la cual se supone una base de Groebner.
Devolverá `false` en caso contrario.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_subsetp -->
<!-- signatures: poly_grobner_subsetp(polylist1, polylist2, varlist) -->
### Function: poly_grobner_subsetp (polylist1, polylist2, varlist)

`poly_grobner_subsetp` comprueba si el ideal generado por *polylist1*
está contenido en el ideal generado por *polylist2*. Para que esta comprobación
tenga éxito, *polylist2* debe ser una base de Groebner.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_intersection -->
<!-- signatures: poly_ideal_intersection(polylist1, polylist2, varlist) -->
### Function: poly_ideal_intersection (polylist1, polylist2, varlist)

`poly_ideal_intersection` devuelve la intersección de dos ideales.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation -->
<!-- signatures: poly_ideal_polysaturation(polylist, polylistlist, varlist) -->
### Function: poly_ideal_polysaturation (polylist, polylistlist, varlist)

*polylistlist* es una lista de n listas de polinomios `[polylist1,...,polylistn]`.
Devuelve la base de Groebner reducida de la saturación del ideal


I(polylist):I(polylist_1)^inf:...:I(polylist_n)^inf

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation1 -->
<!-- signatures: poly_ideal_polysaturation1(polylist1, polylist2, varlist) -->
### Function: poly_ideal_polysaturation1 (polylist1, polylist2, varlist)

*polylist2* es una lista de n poliomios `[poly1,...,polyn]`.
Devuelve la base de Groebner reducida del ideal


I(polylist):poly1^inf:...:polyn^inf



obtenida a partir de una secuencia de saturaciones sucesivas de
los polinomios de la lista *polylist2* del ideal generado
por la lista de polinomios *polylist1*.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation -->
<!-- signatures: poly_ideal_saturation(polylist1, polylist2, varlist) -->
### Function: poly_ideal_saturation (polylist1, polylist2, varlist)

Devuelve la base de Groebner reducida de la saturación del ideal


I(polylist1):I(polylist2)^inf



Desde un punto de vista geométrico, sobre un campo algebraicamente
cerrado, este es el conjunto de polinomios del ideal generado por 
*polylist1* que no se anulan sobre la variedad de  *polylist2*.

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation1 -->
<!-- signatures: poly_ideal_saturation1(polylist, poly, varlist) -->
### Function: poly_ideal_saturation1 (polylist, poly, varlist)

Devuelve la base de Groebner reducida de la saturación del ideal


I(polylist):poly^inf



Desde un punto de vista geométrico, sobre un campo algebraicamente
cerrado, este es el conjunto de polinomios del ideal generado por 
*polylist* que no se anulan sobre la variedad de  *poly*.

<!-- category: Polynomials -->
<!-- keywords: poly_lcm -->
<!-- signatures: poly_lcm(poly1, poly2, varlist) -->
### Function: poly_lcm (poly1, poly2, varlist)

Devuelve el MCM de *poly1* y *poly2*.

<!-- category: Polynomials -->
<!-- keywords: poly_minimization -->
<!-- signatures: poly_minimization(polylist, varlist) -->
### Function: poly_minimization (polylist, varlist)

Devuelve una sublista de la lista de polinomios *polylist* con
el mismo ideal de monomios que *polylist*, pero mínimo, 
esto es, ningún monomio principal de los polinomios de la sublista divide
a los monomios principales de los demás polinomios.

<!-- category: Polynomials -->
<!-- keywords: poly_monomial_order -->
<!-- signatures: poly_monomial_order -->
### Variable: poly_monomial_order

Valor por defecto: `lex`


Controla qué orden de monomios utiliza en los cálculos con
polinomios y bases de Groebner. Si no se le asigna valor alguno,
se utilizará `lex`.

<!-- category: Polynomials -->
<!-- keywords: poly_multiply -->
<!-- signatures: poly_multiply(poly1, poly2, varlist) -->
### Function: poly_multiply (poly1, poly2, varlist)

Multiplica *poly1* por *poly2*.


```maxima
(%i2) poly_multiply(z+x^2*y,x-z,[x,y,z])-(z+x^2*y)*(x-z),expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_normal_form -->
<!-- signatures: poly_normal_form(poly, polylist, varlist) -->
### Function: poly_normal_form (poly, polylist, varlist)

`poly_normal_form` encuentra la forma normal de un polinomio *poly* respecto
de un conjunto de polinomios *polylist*.

<!-- category: Polynomials -->
<!-- keywords: poly_normalize -->
<!-- signatures: poly_normalize(poly, varlist) -->
### Function: poly_normalize (poly, varlist)

Devuelve el polinomio *poly* dividido por el coeficiente
principal. Da por supuesto que la división es posible, lo cual
puede no ser siempre cierto en anillos que no son campos.

<!-- category: Polynomials -->
<!-- keywords: poly_normalize_list -->
<!-- signatures: poly_normalize_list(polylist, varlist) -->
### Function: poly_normalize_list (polylist, varlist)

`poly_normalize_list` aplica `poly_normalize` a cada polinomio 
de la lista. Esto significa que divide cada polinomio de *polylist*
por su coeficiente principal.

<!-- category: Polynomials -->
<!-- keywords: poly_polysaturation_extension -->
<!-- signatures: poly_polysaturation_extension(poly, polylist, varlist1, varlist2) -->
### Function: poly_polysaturation_extension (poly, polylist, varlist1, varlist2)

<!-- category: Polynomials -->
<!-- keywords: poly_primary_elimination_order -->
<!-- signatures: poly_primary_elimination_order -->
### Variable: poly_primary_elimination_order

Valor por defecto: `false`


Nombre del orden por defecto para las variables eliminadas en
las funciones basadas en eliminaciones. Si no se le asigna
ningún valor, se utilizará `lex`.

<!-- category: Polynomials -->
<!-- keywords: poly_primitive_part -->
<!-- signatures: poly_primitive_part(poly1, varlist) -->
### Function: poly_primitive_part (poly1, varlist)

Devuelve el polinomio *poly* dividido por el MCD de sus coeficientes. 



```maxima
(%i1) poly_primitive_part(35*y+21*x,[x,y]);
(%o1)                              5 y + 3 x
```

<!-- category: Polynomials -->
<!-- keywords: poly_pseudo_divide -->
<!-- signatures: poly_pseudo_divide(poly, polylist, varlist) -->
### Function: poly_pseudo_divide (poly, polylist, varlist)

Realiza la seudo-división del polinomio *poly* por la
lista de $n$ polinomios de *polylist*.
Devuelve varios resultados. El primer resultado es una lista de 
cocientes $a$. El segundo resultado es el resto $r$. El
tercer resultado es un coeficiente escalar $c$, tal que $c*poly$
puede dividirse por *polylist* dentro del anillo de coeficientes, el
cual no es necesariamente un campo. Por último, el cuarto resultado es
un entero que guarda el recuento de reducciones realizadas. El objeto 
resultante satisface la ecuación:


$c*poly=sum(a[i]*polylist[i],i=1...n)+r$.

<!-- category: Polynomials -->
<!-- keywords: poly_reduced_grobner -->
<!-- signatures: poly_reduced_grobner(polylist, varlist) -->
### Function: poly_reduced_grobner (polylist, varlist)

Devuelve la base de Groebner reducida del ideal asociado a los polinomios
de *polylist*. El resultado depende de las variables globales.

<!-- category: Polynomials -->
<!-- keywords: poly_reduction -->
<!-- signatures: poly_reduction(polylist, varlist) -->
### Function: poly_reduction (polylist, varlist)

`poly_reduction` reduce una lista de polinomios *polylist* de manera
que cada polinomio se reduce completamente respecto de los otros polinomios.

<!-- category: Polynomials -->
<!-- keywords: poly_return_term_list -->
<!-- signatures: poly_return_term_list -->
### Variable: poly_return_term_list

Valor por defecto: `false`


Si vale `true`, todas las funciones de este paquete devolverán
los polinomios como una lista de términos en el orden activo de
monomios, en lugar de una expresión ordinaria de *maxima*.

<!-- category: Polynomials -->
<!-- keywords: poly_s_polynomial -->
<!-- signatures: poly_s_polynomial(poly1, poly2, varlist) -->
### Function: poly_s_polynomial (poly1, poly2, varlist)

Devuelve el *polinomio syzygy* (*S-polinomio*) de dos polinomios *poly1* y *poly2*.

<!-- category: Polynomials -->
<!-- keywords: poly_saturation_extension -->
<!-- signatures: poly_saturation_extension(poly, polylist, varlist1, varlist2) -->
### Function: poly_saturation_extension (poly, polylist, varlist1, varlist2)

`poly_saturation_extension` ejecuta el truco de Rabinowitz.

<!-- category: Polynomials -->
<!-- keywords: poly_secondary_elimination_order -->
<!-- signatures: poly_secondary_elimination_order -->
### Variable: poly_secondary_elimination_order

Valor por defecto: `false`


Nombre del orden por defecto para las variables almacenadas
en funciones basadas en eliminaciones. Si no se le asigna
ningún valor, se utilizará `lex`.

<!-- category: Polynomials -->
<!-- keywords: poly_subtract -->
<!-- signatures: poly_subtract(poly1, poly2, varlist) -->
### Function: poly_subtract (poly1, poly2, varlist)

Resta el polinomio *poly2* de *poly1*.


```maxima
(%i1) poly_subtract(z+x^2*y,x-z,[x,y,z]);
                                      2
(%o1)                          2 z + x  y - x
```

<!-- category: Polynomials -->
<!-- keywords: poly_top_reduction_only -->
<!-- signatures: poly_top_reduction_only -->
### Variable: poly_top_reduction_only

Valor por defecto: `false`


Si no vale `false`, siempre que sea posible el algoritmo
de división se detendrá tras la primera reducción.

