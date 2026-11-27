## mnewton

<!-- category: Numerical -->
<!-- keywords: mnewton -->
<!-- signatures: mnewton(FuncList, VarList, GuessList) -->
### Function: mnewton (FuncList, VarList, GuessList)

Resolución de sistemas de ecuaciones no lineales por el método de Newton.
*FuncList* es la lista de ecuaciones a resolver,
*VarList* es la lista con los nombres de las incógnitas y
*GuessList* es la lista de aproximaciones iniciales.


La solución se devuelve en el mismo formato que lo hace la función `solve()`.
Si no se le encuentra solución al sistema, se obtiene `[]` como respuesta.


Esta función se controla con las variables globales `newtonepsilon` y `newtonmaxiter`.



```maxima
(%i1) load("mnewton")$

(%i2) mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1],
              [x1, x2], [5, 5]);
(%o2) [[x1 = 3.756834008012769, x2 = 2.779849592817897]]
(%i3) mnewton([2*a^a-5],[a],[1]);
(%o3)             [[a = 1.70927556786144]]
(%i4) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o4) [[u = 1.066618389595407, v = 1.552564766841786]]
```


La variable `newtonepsilon` controla la precisión de las
aproximaciones. También controla si los cálculos se realizan con
precisión doble o arbitraria (bigfloats).



```maxima
(%i1) load("mnewton")$

(%i2) (fpprec : 25, newtonepsilon : bfloat(10^(-fpprec+5)))$

(%i3) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o3) [[u = 1.066618389595406772591173b0, 
                               v = 1.552564766841786450100418b0]]
```


Antes de hacer uso de esta función ejecútese  `load("mnewton")`.
Véanse también `newtonepsilon` y `newtonmaxiter`.

<!-- category: Numerical -->
<!-- keywords: newtonepsilon -->
<!-- signatures: newtonepsilon -->
### Variable: newtonepsilon

Valor por defecto:  `10.0^(-fpprec/2)`


Precisión que determina cuando la función `mnewton` ha conseguido una
convergencia aceptable. Si `newtonepsilon` es un número decimal de 
precisión arbitraria (bigfloat), entonces `mnewton` realiza los 
cálculos en ese formato.


Véase también `mnewton`.

<!-- category: Numerical -->
<!-- keywords: newtonmaxiter -->
<!-- signatures: newtonmaxiter -->
### Variable: newtonmaxiter

Valor por defecto:  `50`


Número máximo de iteraciones para la función `mnewton` en caso
de que no se produzca convergencia, o de que ésta se haga muy lenta.


Véase también `mnewton`.

