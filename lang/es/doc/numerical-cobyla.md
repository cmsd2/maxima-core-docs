## cobyla

<!-- category: Numerical -->
<!-- keywords: bf_fmin_cobyla -->
<!-- signatures: bf_fmin_cobyla(F, X, Y), bf_fmin_cobyla(F, X, Y, optional_args) -->
### Function: bf_fmin_cobyla (F, X, Y)

Esta función es idéntica a `fmin_cobyla`, excepto por el hecho
de que utiliza aritmética de precisión arbitraria (bigfloat) y que el
valor por defecto de *rhoend* es `10^(fpprec/2)`. 


Véase `fmin_cobyla`.


El código `load("fmin_cobyla")` carga en memoria esta función..

<!-- category: Numerical -->
<!-- keywords: fmin_cobyla -->
<!-- signatures: fmin_cobyla(F, X, Y), fmin_cobyla(F, X, Y, optional_args) -->
### Function: fmin_cobyla (F, X, Y)

Devuelve una aproximación del valor mínimo de la expresión
*F* respecto de las variables *X*, sujeta a un conjunto opcional
de restricciones. *Y* es una lista que contiene una solución semilla
inicial en *X*.


*F* debe ser una expresión ordinaria, no valen nombres de funciones
ni expresiones lambda.


`optional_args` hace referencia a argumentos adicionales, que se
especifican de la forma `symbol = value`. Los argumentos
opcionales que se reconocen son:



**constraints** — Lista de restricciones en forma de desigualdades e igualdades que debe
satisfacer *X*. Las desigualdades deben ser de la forma 
`g(X) >= h(X)` o `g(X) <= h(X)`.
Las restricciones de igualdad deben ser de la forma 
`g(X) = h(X)`.
**rhobeg** — Valor inicial de la variable interna RHO, que controla el tamaño del
simplejo. Su valor por defecto es 1.0.
**rhoend** — El valor final deseado para el parámetro RHO. Es aproximadamente la
precisión de las variables. Su valor por defecto es 1d-6.
**iprint** — Nivel de información de salida. Su valor por defecto es 0. 
- *
0 - Sin información de salida
- *
1 - Sumario al final de los cálculos
- *
2 - Se van mostrando los nuevos valores de RHO y SIGMA, incluyendo
 el vector de variables.
- *
3 - Como en 2, pero la información se muestra cuando se calcula F(X).
**maxfun** — Número máximo de evaluaciones de la función. Su valor por defecto es 1000.


El resultado devuelto es un vector:


1. Los valores de las variables con las que se alcanza el valor mínimo.
Es una lista de elementos de la forma `var = value` para cada
una de las variables listadas en *X*.
2. El valor mínimo de la función objetivo.
3. El número de evaluaciones de la función.
4. Código de retorno con los siguientes significados:
 

  1. 0 - No ha habido errores.
  2. 1 - Alcanzado el máximo número permitido de evaluaciones de la función.
  3. 2 - Errores de redondeo han impedido el avance del proceso.


El código `load("fmin_cobyla")` carga en memoria esta función..

