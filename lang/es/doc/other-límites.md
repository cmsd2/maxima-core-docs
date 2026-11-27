## Límites

<!-- category: Other -->
<!-- keywords: lhospitallim -->
<!-- signatures: lhospitallim -->
### Variable: lhospitallim

Valor por defecto: 4


Es el número máximo de veces que la regla de L’Hopital es aplicada en la función `limit`, evitando bucles infinitos al iterar la regla en casos como `limit (cot(x)/csc(x), x, 0)`.

<!-- category: Other -->
<!-- keywords: limit -->
<!-- signatures: limit(expr, x, val, dir), limit(expr, x, val), limit(expr) -->
### Function: limit (expr, x, val, dir)

Calcula el límite de *expr* cuando la variable real *x*
se aproxima al valor *val* desde la dirección *dir*. El argumento 
*dir* puede ser el valor `plus` para un límite por la 
derecha, `minus` para un límite por la izquierda o simplemente 
se omite para indicar un límite en ambos sentidos.


La función `limit` utiliza los símbolos especiales 
siguientes: `inf` (más infinito) y `minf` (menos
infinito). En el resultado también puede hacer uso de `und` (indefinido), 
`ind` (indefinido pero acotado) y `infinity` (infinito complejo).


`infinity` (infinito complejo) es el resultado que se obtiene cuando
el límite del módulo de la expresión es infinito
positivo, pero el propio límite de la expresión no es infinito
positivo ni negativo. Esto sucede, por ejemplo, cuando el límite del
argumento complejo es una constante, como en `limit(log(x), x, minf)`,
o cuando el argumento complejo oscila, como en `limit((-2)^x, x, inf)`, o
en aquellos casos en los que el argumento complejo es diferente por cualquiera
de los lados de un límite, como en `limit(1/x, x, 0)`
o `limit(log(x), x, 0)`.


La variable `lhospitallim` guarda el número máximo de veces que la regla 
de L’Hopital es aplicada en la función `limit`, evitando bucles infinitos 
al iterar la regla en casos como `limit (cot(x)/csc(x), x, 0)`.


Si la variable `tlimswitch` vale `true`, hará que la función 
`limit` utilice desarrollos de Taylor siempre que le sea posible.


La variable `limsubst` evita que la función `limit` realice 
sustituciones sobre formas desconocidas, a fin de evitar fallos tales como 
que `limit (f(n)/f(n+1), n, inf)` devuelva 1.  Dándole a `limsubst` 
el valor `true` se permitirán tales sustituciones.


La función `limit` con un solo argumento se utiliza frecuentemente para 
simplificar expresiones constantes, como por ejemplo `limit (inf-1)`.



La instrucción `example (limit)` muestra algunos ejemplos.


Para información sobre el método utilizado véase Wang, P., "Evaluation of 
Definite Integrals by Symbolic
Manipulation", Ph.D. thesis, MAC TR-92, October 1971.

<!-- category: Other -->
<!-- keywords: limsubst -->
<!-- signatures: limsubst -->
### Variable: limsubst

Valor por defecto: `false`


La variable `limsubst` evita que la función `limit` realice sustituciones 
sobre formas desconocidas, a fin de evitar fallos tales como que 
`limit (f(n)/f(n+1), n, inf)` devuelva 1.  Dándole a `limsubst` el valor 
`true` se permitirán tales sustituciones.

<!-- category: Other -->
<!-- keywords: tlimit -->
<!-- signatures: tlimit(expr, x, val, dir), tlimit(expr, x, val), tlimit(expr) -->
### Function: tlimit (expr, x, val, dir)

Calcula el límite del desarrollo de Taylor de la expresión
`expr` de variable `x` en el punto `val` en la dirección `dir`.

<!-- category: Other -->
<!-- keywords: tlimswitch -->
<!-- signatures: tlimswitch -->
### Variable: tlimswitch

Valor por defecto: `true`


Si `tlimswitch` vale `true`, la función `limit` utilizará
un desarrollo de Taylor si el límite de la expresión dada no
se puede calcular directamente. Esto permite el cálculo de límites
como `limit(x/(x-1)-1/log(x),x,1,plus)`.
Si `tlimswitch` vale `false` y el límite de la expresión
no se puede calcular directamente, la función `limit` devolverá una expresión
sin evaluar.

