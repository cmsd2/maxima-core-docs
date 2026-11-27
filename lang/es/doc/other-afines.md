## Afines

<!-- category: Other -->
<!-- keywords: all_dotsimp_denoms -->
<!-- signatures: all_dotsimp_denoms -->
### Variable: all_dotsimp_denoms

Valor por defecto: `false`


Cuando `all_dotsimp_denoms` es una lista, los denominadores encontrados
por `dotsimp` son añadidos a la lista. La variable `all_dotsimp_denoms`
puede inicializarse como una lista vacía `[]` antes de llamar a `dotsimp`.


Por defecto, `dotsimp` no recolecta los denominadores.

<!-- category: Other -->
<!-- keywords: check_overlaps -->
<!-- signatures: check_overlaps(n, add_to_simps) -->
### Function: check_overlaps (n, add_to_simps)

Revisa la superposición hasta el grado *n*,
asegurándose de que el usuario tiene suficientes reglas de simplificación en cada
grado para que `dotsimp` trabaje correctamente. Este proceso puede acelerarse
si se conoce de antemano cuál es la dimensión del espacio de monomios.
Si éste es de dimensión global finita, entonces debería usarse `hilbert`. Si
no se conoce la dimensiones de los monomios, no se debería especificar una `rank_function`.
Un tercer argumento opcional es `reset`.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: declare_weights -->
<!-- signatures: declare_weights(x_1, w_1, ..., x_n, w_n) -->
### Function: declare_weights (x_1, w_1, ..., x_n, w_n)

Asigna los pesos *w_1*, ..., *w_n* a *x_1*, ..., *x_n*, respectivamente.
Estos pesos son los utilizados en el cálculo de `nc_degree`.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: dotsimp -->
<!-- signatures: dotsimp(f) -->
### Function: dotsimp (f)

Devuelve 0 si y sólo si  *f* está en el ideal generado por las ecuaciones, esto es,
si y sólo si *f* es una combinación lineal de los elementos de las ecuaciones.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: extract_linear_equations -->
<!-- signatures: extract_linear_equations([p_1, ..., p_n], [m_1, ..., m_n]) -->
### Function: extract_linear_equations ([p_1, ..., p_n], [m_1, ..., m_n])

Hace una lista de los coeficientes de los polinomios no conmutativos *p_1*, ..., *p_n*  
de los monomios no conmutativos *m_1*, ..., *m_n*. Los coeficientes deben escalares. Hágase uso 
de `list_nc_monomials` para construir la lista de monomios.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: fast_central_elements -->
<!-- signatures: fast_central_elements([x_1, ..., x_n], n) -->
### Function: fast_central_elements ([x_1, ..., x_n], n)

Si se ha ejecutado `set_up_dot_simplifications` con antelación, obtiene los 
polinomios centrales de grado *n* de variables *x_1*, ..., *x_n*.


Por ejemplo:


```maxima
set_up_dot_simplifications ([y.x + x.y], 3);
fast_central_elements ([x, y], 2);
[y.y, x.x];
```


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: fast_linsolve -->
<!-- signatures: fast_linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: fast_linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resuelve las ecuaciones lineales simultáneas *expr_1*, ..., *expr_m*
para las variables *x_1*, ..., *x_n*.
Cada *expr_i* puede ser una ecuación o una expresión general;
en caso de tratarse de una expresión general, será tratada como una ecuación de la forma `expr_i = 0`.


El valor que devuelve es una lista de ecuaciones de la forma
`[x_1 = a_1, ..., x_n = a_n]`
donde todas las *a_1*, ..., *a_n* están exentas de *x_1*, ..., *x_n*.


La función `fast_linsolve` es más rápida que `linsolve` para sistemas de ecuaciones con coeficientes
dispersos.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: grobner_basis -->
<!-- signatures: grobner_basis([expr_1, ..., expr_m]) -->
### Function: grobner_basis ([expr_1, ..., expr_m])

Devuelve una base de Groebner para las ecuaciones *expr_1*, ..., *expr_m*.
La función `polysimp` puede ser entonces utilizada para simplificar
otras funciones relativas a las ecuaciones.



```maxima
grobner_basis ([3*x^2+1, y*x])$

polysimp (y^2*x + x^3*9 + 2) ==> -3*x + 2
```


`polysimp(f)` alcanza 0 si y sólo si *f* está en el ideal generado por
*expr_1*, ..., *expr_m*, es decir, si y sólo si *f* es una
combinación  polinómica de los elementos de 
*expr_1*, ..., *expr_m*.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: list_nc_monomials -->
<!-- signatures: list_nc_monomials([p_1, ..., p_n]), list_nc_monomials(p) -->
### Function: list_nc_monomials ([p_1, ..., p_n])

Devuelve  una lista de los monomios no conmutativos que aparecen en el polinomio  *p*
o una lista de polinomios en *p_1*, ..., *p_n*.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: mono -->
<!-- signatures: mono([x_1, ..., x_n], n) -->
### Function: mono ([x_1, ..., x_n], n)

Devuelve la lista de monomios independientes. 


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: monomial_dimensions -->
<!-- signatures: monomial_dimensions(n) -->
### Function: monomial_dimensions (n)

Calcula el desarrollo de Hilbert de grado *n* para el algebra actual.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: nc_degree -->
<!-- signatures: nc_degree(p) -->
### Function: nc_degree (p)

Devuelve el grado de un polinomio no conmutativo *p*. Véase `declare_weights`.


Antes de utilizar esta función ejecútese `load("affine")`.

<!-- category: Other -->
<!-- keywords: set_up_dot_simplifications -->
<!-- signatures: set_up_dot_simplifications(eqns, check_through_degree), set_up_dot_simplifications(eqns) -->
### Function: set_up_dot_simplifications (eqns, check_through_degree)

Las *eqns* son ecuaciones polinómicas de variables no conmutativas.
El valor de `current_variables` es la lista de variables utilizadas para
el cálculo de los grados. Las ecuaciones deben ser homogéneas, al objeto de 
completar el procedimiento.




El grado es el devuelto por `nc_degree`. Éste a su vez depende de los pesos 
de las variables individuales.


Antes de utilizar esta función ejecútese `load("affine")`.

