## ggf

<!-- category: Other -->
<!-- keywords: ggf -->
<!-- signatures: ggf(l) -->
### Function: ggf (l)

Calcula la función generatriz de una sucesión de la que
se suministran tan solo los primeros valores y cuyo término
general es una fracción algebraica (cociente de dos
polinomios).


La solución se devuelve como una fracción de polinomios. 
En caso de no poder encontrar una solución, se devuelve
`done`.


Esta función está controlada por las variables globales 
*GGFINFINITY* y *GGFCFMAX*. Véanse también *GGFINFINITY* y *GGFCFMAX*.


Antes de hacer uso de esta función ejecútese  `load("ggf")`.

<!-- category: Other -->
<!-- keywords: GGFCFMAX -->
<!-- signatures: GGFCFMAX -->
### Variable: GGFCFMAX

Valor por defeco: 3


Variable opcional para la función `ggf`.


Cuando se calcula la fracción continua de la función
generatriz, si no se ha encontrado un resultado aceptable
(véase la variable *GGFINFINITY*) después de haber 
calculado *GGFCFMAX* cocientes parciales, la función
generatriz será considerada no equivalente a una fracción
racional y la función `ggf` se detendrá. Puede
asignársele a *GGFCFMAX* un valor mayor para funciones
generatrices más complicadas.


Véase también `ggf`.

<!-- category: Other -->
<!-- keywords: GGFINFINITY -->
<!-- signatures: GGFINFINITY -->
### Variable: GGFINFINITY

Valor por defecto: 3


Variable opcional para la función `ggf`.


Cuando se calcula la fracción continua de la función
generatriz, si un cociente parcial tiene grado estrictamente
mayor que *GGFINFINITY* será descartado y la convergencia
alcanzada hasta ese momento será considerada como exacta para
la función generatriz. Lo más frecuente es que el grado de
todos los cocientes parciales sea 0 ó 1, de modo que si se
utiliza un valor mayor se deberán dar más términos para
conseguir un cálculo más exacto.


Véase también `ggf`.

