## minpack

<!-- category: Numerical -->
<!-- keywords: minpack_lsquares -->
<!-- signatures: minpack_lsquares(flist, varlist, guess), minpack_lsquares(..., 'tolerance=tolerance), minpack_lsquares(..., 'jacobian=jacobian) -->
### Function: minpack_lsquares (flist, varlist, guess)

Calcula el punto `x` que minimiza la suma de los cuadrados de las
funciones de la lista *flist*. Las variables se escriben en
la lista `varlist`. El argumento *guess* debe guardar una
estimación inicial del punto óptimo.


Los argumentos opcionales *tolerance* y *jacobian* permiten
mantener cierto control sobre el algoritmo; *tolerance* es el
error relativo estimado que se desea en la suma de cuadrados,
mientras que *jacobian* puede utilizarse para especificar el
jacobiano. Si *jacobian* no se suministra, o se le da el valor
`true`, el que ya tiene por defecto, el jacobiano se calcula
a partir de *flist*. Si *jacobian* vale `false`, se
utilizará una aproximación numérica.


`minpack_lsquares` devuelve una lista, siendo su primer 
elemento la solución estimada, el segundo la suma de cuadrados y
el tercero indica la bondad del algoritmo, siendo sus posibles valores
los siguientes:



**0** — Número incorrecto de parámetros.
**1** — El algoritmo estima que el error relativo de la suma de cuadrados
es, como mucho, igual a `tolerance`.
**2** — El algoritmo estima que el error relativo entre *x* y la solución es,
como mucho, igual a `tolerance`.
**3** — Las dos condiciones anteriores se cumplen.
**4** — El vector formado por las funciones evaluadas en el punto *x* es
ortogonal a las columnas del jacobiano dentro de la precisión de la
máquina.
**5** — El número de llamadas a las funciones ha alcanzado 100*(n+1), siendo
n el número de variables.
**6** — La tolerancia es demasiado pequeña, no siendo posible reducir más la
suma de cuadrados.
**7** — La tolerancia es demasiado pequeña, no siendo posible mejorar la
solución aproximada *x*.



```maxima
/* Problem 6: Powell singular function */
(%i1) powell(x1,x2,x3,x4) := 
         [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, 
              sqrt(10)*(x1-x4)^2]$
(%i2) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], 
                       [3,-1,0,1]);
(%o2) [[1.652117596168394e-17, - 1.652117596168393e-18, 
        2.643388153869468e-18, 2.643388153869468e-18], 
       6.109327859207777e-34, 4]
```



```maxima
/* Same problem but use numerical approximation to Jacobian */
(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], 
                       [3,-1,0,1], jacobian = false);
(%o3) [[5.060282149485331e-11, - 5.060282149491206e-12, 
        2.179447843547218e-11, 2.179447843547218e-11], 
       3.534491794847031e-21, 5]
```

<!-- category: Numerical -->
<!-- keywords: minpack_solve -->
<!-- signatures: minpack_solve(flist, varlist, guess), minpack_solve(..., 'tolerance=tolerance), minpack_solve(..., 'jacobian=jacobian) -->
### Function: minpack_solve (flist, varlist, guess)

Resuelve un sistema de `n` ecuaciones con `n` incógnitas.
Las `n` ecuaciones forman la lista *flist*, estando la
lista *varlist* formada por las incógnitas. El argumento
*guess* es una estimación inicial de la solución.


Los argumentos opcionales *tolerance* y *jacobian* permiten
mantener cierto control sobre el algoritmo; *tolerance* es el
error relativo estimado que se desea en la suma de cuadrados,
mientras que *jacobian* puede utilizarse para especificar el
jacobiano. Si *jacobian* no se suministra, o se le da el valor
`true`, el que ya tiene por defecto, el jacobiano se calcula
a partir de *flist*. Si *jacobian* vale `false`, se
utilizará una aproximación numérica.


`minpack_solve` devuelve una lista, siendo su primer 
elemento la solución estimada, el segundo la suma de cuadrados y
el tercero indica la bondad del algoritmo, siendo sus posibles valores
los siguientes:



**0** — Número incorrecto de parámetros.
**1** — El algoritmo estima que el error relativo de la suma de cuadrados
es, como mucho, igual a `tolerance`.
**2** — El número de llamadas a las funciones ha alcanzado 100*(n+1), siendo
n el número de incógnitas.
**3** — La tolerancia es demasiado pequeña, no siendo posible reducir más la
suma de cuadrados.
**4** — El algoritmo no progresa adecuadamente.

