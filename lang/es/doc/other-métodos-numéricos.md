## Métodos numéricos

<!-- category: Other -->
<!-- keywords: find_root, bf_find_root, find_root_error, find_root_abs, find_root_rel -->
<!-- signatures: find_root(expr, x, a, b, [abserr, relerr]), find_root(f, a, b, [abserr, relerr]), bf_find_root(expr, x, a, b, [abserr, relerr]), bf_find_root(f, a, b, [abserr, relerr]), find_root_error, find_root_abs, find_root_rel -->
### Function: find_root (expr, x, a, b, [abserr, relerr])

Calcula una raíz de la expresión *expr* o de
la función *f* en el intervalo cerrado $[a, b]$.
La expresión *expr* puede ser una ecuación, en cuyo caso 
`find_root` busca una raíz de
`lhs(expr) - rhs(expr)`.


Dado que Maxima puede evaluar *expr* o *f* en 
$[a, b]$, entonces, si *expr* o *f* es
continua, `find_root` encuentrará la raíz
buscada, o raíces, en caso de existir varias.


La función `find_root` aplica al principio la
búsqueda por bipartición. Si la expresión es lo suficientemente
suave, entonces `find_root` aplicará el método
de interpolación lineal.


`bf_find_root` es una versión de `find_root` para números
reales de precisión arbitraria (bigfloat). La función se 
evalúa utilizando la aritmética de estos números, devolviendo
un resultado numérico de este tipo. En cualquier otro aspecto,
`bf_find_root` es idéntica a `find_root`, siendo la
explicación que sigue igualmente válida para `bf_find_root`. 


La precisión de `find_root` está controlada por `abserr` y
`relerr`, que son claves opcionales para `find_root`. 
Estas claves toman la forma `key=val`. Las claves disponibles son:



**abserr** — Error absoluto deseado de la función en la raíz. El
valor por defecto es `find_root_abs`.
**relerr** — Error relativo deseado de la raíz. El valor por defecto
es `find_root_rel`.


`find_root` se detiene cuando la función alcanza un valor menor o
igual que `abserr`, o si las sucesivas aproximaciones *x_0*, *x_1*
difieren en no más que `relerr * max(abs(x_0), abs(x_1))`. Los
valores por defecto de `find_root_abs` y `find_root_rel` son
ambos cero.


`find_root` espera que la función en cuestión tenga signos
diferentes en los extremos del intervalo.
Si la función toma valores numéricos en ambos extremos y estos
números son del mismo signo, entonces
el comportamiento de `find_root` se controla con `find_root_error`.
Cuando `find_root_error` vale `true`, `find_root`
devuelve un mensaje de error; en caso contrario, `find_root`
devuelve el valor de `find_root_error`. El valor por defecto
de `find_root_error` es `true`.


Si en algún momento del proceso de búsqueda *f* alcanza un valor
no numérico, `find_root` devuelve una expresión parcialmente evaluada.


Se ignora el orden de *a* y *b*; la región de búsqueda es
$[min(a, b), max(a, b)]$.


Ejemplos:
























```maxima
(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2
(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981
(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981
(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981
(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981
(%i6) find_root (exp(x) = y, x, 0, 100);
                            x
(%o6)           find_root(%e  = y, x, 0.0, 100.0)
(%i7) find_root (exp(x) = y, x, 0, 100), y = 10;
(%o7)                   2.302585092994046
(%i8) log (10.0);
(%o8)                   2.302585092994046
(%i9) fpprec:32;
(%o9)                           32
(%i10) bf_find_root (exp(x) = y, x, 0, 100), y = 10;
(%o10)                  2.3025850929940456840179914546844b0
(%i11) log(10b0);
(%o11)                  2.3025850929940456840179914546844b0
```

<!-- category: Other -->
<!-- keywords: horner -->
<!-- signatures: horner(expr, x), horner(expr) -->
### Function: horner (expr, x)

Cambia el formato de *expr* según la regla de Horner utilizando *x* como variable principal, si ésta se especifica. El argumento `x` se puede omitir, en cuyo caso se considerará como variable principal la de *expr* en su formato racional canónico (CRE).


La función `horner` puede mejorar las estabilidad si `expr` va a ser numéricamente evaluada. También es útil si Maxima se utiliza para generar programas que serán ejecutados en Fortran. Véase también `stringout`.



```maxima
(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                           2
(%o1)            1.0E-155 x  - 5.5 x + 5.2E+155
(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)            (1.0E-155 x - 5.5) x + 5.2E+155
(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 floating point overflow

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i4) ev (expr2, x=1e155);
(%o4)                       7.0E+154
```

<!-- category: Other -->
<!-- keywords: newton -->
<!-- signatures: newton(expr, x, x_0, eps) -->
### Function: newton (expr, x, x_0, eps)

Devuelve una solución aproximada de `expr = 0` obtenida
por el método de Newton, considerando *expr* como una función
de una variable, *x*.
La búsqueda comienza con `x = x_0` y continúa
hasta que se verifique `abs(expr) < eps`, donde
*expr* se evalúa con el valor actual de *x*.


La función `newton` permite que en *expr* haya variables
no definidas, siempre y cuando la condición de terminación
`abs(expr) < eps` pueda reducirse a un valor
lógico `true` o `false`; de este modo, no es necesario
que *expr* tome un valor numérico.


Ejecútese `load("newton1")` para cargar esta función.


Véanse también `realroots`, `allroots`, `find_root` y `mnewton`.


Ejemplos:











```maxima
(%i1) load ("newton1");
(%o1) /usr/share/maxima/5.10.0cvs/share/numeric/newton1.mac
(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                   1.570675277161251
(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528E-4
(%i4) assume (a > 0);
(%o4)                        [a > 0]
(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                  1.00030487804878 a
(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958E-4 a
```

<!-- category: Other -->
<!-- keywords: plotdf -->
<!-- signatures: plotdf(dydx, ...options...), plotdf(dvdu, [u, v], ...options...), plotdf([dxdt, dydt], ...options...), plotdf([dudt, dvdt], [u, v], ...options...) -->
### Function: plotdf (dydx, ...options...)

Dibuja un campo de direcciones en dos dimensiones *x* y *y*.


*dydx*, *dxdt* y *dydt* son expresiones que dependen de *x* y
*y*. Además de esas dos variables, las dos expresiones pueden depender de
un conjunto de parámetros, con valores numéricos que son dados por medio
de la opción `parameters` (la sintaxis de esa opción se explica mas al
frente), o con un rango de posibles valores definidos con la opción
*sliders*.


Varias otras opciones se pueden incluir dentro del comando, o
seleccionadas en el menú.  Haciendo click en un punto del gráfico se
puede hacer que sea dibujada la curva integral que pasa por ese punto;
lo mismo puede ser hecho dando las coordenadas del punto con la opción
`trajectory_at` dentro del comando plotdf. La dirección de
integración se puede controlar con la opción `direction`, que
acepta valores de *forward*, *backward* ou *both*. El
número de pasos realizado en la integración numérica se controla
con la opción `nsteps` y el incremento del tiempo en cada paso
con la opción `tstep`. Se usa el método de Adams Moulton para
hacer la integración numérica; también es posible cambiar para el
método de Runge-Kutta de cuarto orden con ajuste de pasos.


**Menú de la ventana del gráfico:**


El menú de la ventana gráfica dispone de las siguientes opciones:
*Zoom*, que permite cambiar el comportamiento del ratón, de
manera que hará posible el hacer zoom en la región del gráfico
haciendo clic con el botón izquierdo. Cada clic agranda la imagen
manteniendo como centro de la misma el punto sobre el cual se ha hecho
clic. Manteniendo pulsada la tecla Shift mientras se hace clic,
retrocede al tamaño anterior. Para reanudar el cálculo de las
trayectorias cuando se hace clic, seleccine la opción *Integrate*
del menú.


La opción *Config* del menú se puede utilizar para cambiar
la(s) EDO(S) y algunos otros ajustes. Después de hacer los cambios, se
debe utilizar la opción *Replot* para activar los nuevos ajustes.
Si en el campo *Trajectory at* del menú de diálogo de
*Config* se introducen un par de coordenadas y luego se pulsa la
tecla retorno, se mostrará una nueva curva integral, además de
las ya dibujadas.  Si se selecciona la opción *Replot*, sólo se
mostrará la última curva integral seleccionada.


Manteniendo pulsado el botón derecho del ratón mientras se mueve el
cursor, se puede arrastrar el gráfico horizontal y verticalmente.
Otros parámetros, como pueden ser el número de pasos, el valor
inicial de *t*, las coordenadas del centro y el radio, pueden
cambiarse en el submenú de la opción *Config*.


Con la opción *Save*, se puede obtener una copia del gráfico en
una impresora Postscript o guardarlo en un fichero Postscript. Para
optar entre la impresión o guardar en fichero, se debe seleccionar
*Print Options* en la ventana de diálogo de *Config*. Una
vez cubiertos los campos de la ventana de diálogo de *Save*,
será necesario seleccionar la opción *Save* del primer menú
para crear el fichero o imprimir el gráfico.


**Opciones gráficas:**


La función `plotdf` admite varias opciones, cada una de las cuales
es una lista de dos o más elementos. El primer elemento es el nombre de
la opción, y el resto está formado por el valor o valores asignados
a dicha opción.


La función `plotdf` reconoce las siguientes opciones:



- *
*tstep* establece la amplitud de los incrementos en la
variable independiente *t*, utilizados para calcular la curva
integral. Si se aporta sólo una expresión *dydx*, la variable
*x* será directamente proporcional a *t*.
El valor por defecto es 0.1.
- *
*nsteps* establece el número de pasos de longitud
`tstep` que se utilizarán en la variable independiente para
calcular la curva integral.
El valor por defecto es 100.
- *
*direction* establece la dirección de la variable
independiente que será seguida para calcular una curva integral.
Valores posibles son: `forward`, para hacer que la variable
independiente aumente `nsteps` veces, con incrementos `tstep`;
`backward`, para hacer que la variable independiente
disminuya; `both`, para extender la curva integral `nsteps`
pasos hacia adelante y `nsteps` pasos hacia atrás.
Las palabras `right` y `left` se pueden utilizar como
sinónimos de `forward` y `backward`.
El valor por defecto es `both`.
- *
*tinitial* establece el valor inicial de la variable
*t* utilizado para calcular curvas integrales. Puesto que las
ecuaciones diferenciales son autónomas, esta opción sólo
aparecerá en los gráficos de las curvas como funciones de *t*.
El valor por defecto es 0.
- *
*versus_t* se utiliza para crear una segunda ventana
gráfica, con el gráfico de una curva integral, como dos funciones
*x*, *y*, de variable independiente *t*. Si se le da a
`versus_t` cualquier valor diferente de 0, se mostrará la
segunda ventana gráfica, la cual incluye otro menú, similar
al de la ventana principal.
El valor por defecto es 0.
- *
*trajectory_at* establece las coordenadas *xinitial*
y *yinitial* para el extremo inicial de la curva integral.
No tiene asignado valor por defecto.
- *
*parameters* establece una lista de parámetros,
junto con sus valores numéricos, que son utilizados en la
definición de la ecuación diferencial. Los nombres de los
parámetros y sus valores deben escribirse en formato de cadena
de caracteres como una secuencia de pares `nombre=valor`
separados por comas.
- *
*sliders* establece una lista de parámetros que
se cambiarán interactivamente utilizando barras de deslizamiento,
así como los rangos de variación de dichos parámetros.
Los nombres de los parámetros y sus rangos deben escribirse en formato
de cadena de caracteres como una secuencia de pares `nombre=min:max`
separados por comas.
- *
*xfun* establece una cadena de caracteres con funciones
de *x* separadas por puntos y comas para ser representadas por
encima del campo de direcciones. Estas funciones serán interpretadas
por Tcl, no por Maxima.
- *
*xradius* es la mitad de la longitud del rango de valores
a representar en la dirección x.
El valor por defecto es 10.
- *
*yradius* es la mitad de la longitud del rango de valores
a representar en la dirección y.
El valor por defecto es 10.
- *
*xcenter* es la coordenada x del punto situado en el centro
del gráfico.
El valor por defecto es 0.
- *
*ycenter* es la coordenada y del punto situado en el centro
del gráfico.
El valor por defecto es 0.
- *
*width* establece el ancho de la ventana gráfica en
píxeles.
El valor por defecto es 500.
- *
*height* establece la altura de la ventana gráfica en
píxeles.
El valor por defecto es 500.


**Ejemplos:**


NOTA: Dependiendo de la interface que se use para Maxima, las funciones
que usan `openmath`, incluida `plotdf`, pueden desencadenar un
fallo si terminan en punto y coma, en vez del símbolo de
dólar. Para evitar problemas, se usará el símbolo de
dólar en todos ejemplos.



- *
Para mostrar el campo de direcciones de la ecuación diferencial
$y' = exp(-x) + y$ y la solución que pasa por $(2, -0.1)$:

```maxima
(%i1) load("plotdf")$
(%i2) plotdf(exp(-x)+y,[trajectory_at,2,-0.1]);
```

![plotdf1](figures/plotdf1.png)
- *
Para mostrar el campo de direcciones de la ecuación diferencial
$diff(y,x) = x - y^2$ y la solución de condición
inicial $y(-1) = 3$, se puede utilizar la sentencia:

```maxima
(%i3) plotdf(x-y^2,[xfun,"sqrt(x);-sqrt(x)"],
          [trajectory_at,-1,3], [direction,forward],
          [yradius,5],[xcenter,6]);
```
El gráfico también muestra la función $y = sqrt(x)$.

![plotdf2](figures/plotdf2.png)
- *
El siguiente ejemplo muestra el campo de direcciones de un oscilador
armónico, definido por las ecuaciones $dx/dt = y$ y
$dy/dt = -k*x/m$, y la curva integral que pasa por
$(x,y) = (6,0)$, con una barra de deslizamiento que 
permitirá cambiar el valor de $m$ interactivamente
($k$ permanece fijo a 2):

```maxima
(%i4) plotdf([y,-k*x/m],[parameters,"m=2,k=2"],
            [sliders,"m=1:5"], [trajectory_at,6,0]);
```

![plotdf3](figures/plotdf3.png)
- *
Para representar el campo de direcciones de la ecuación de
Duffing, $m*x''+c*x'+k*x+b*x^3 = 0$, se introduce la
variable $y=x'$ y se hace:

```maxima
(%i5) plotdf([y,-(k*x + c*y + b*x^3)/m],
              [parameters,"k=-1,m=1.0,c=0,b=1"],
              [sliders,"k=-2:2,m=-1:1"],[tstep,0.1]);
```

![plotdf4](figures/plotdf4.png)
- *
El campo de direcciones de un péndulo amortiguado,
incluyendo la solución para condiciones iniciales dadas,
con una barra de deslizamiento que se puede utilizar para
cambiar el valor de la masa, $m$, y con el gráfico
de las dos variables de estado como funciones del tiempo:

```maxima
(%i6) plotdf([y,-g*sin(x)/l - b*y/m/l],
         [parameters,"g=9.8,l=0.5,m=0.3,b=0.05"],
         [trajectory_at,1.05,-9],[tstep,0.01],
         [xradius,6],[yradius,14],
         [xcenter,-4],[direction,forward],[nsteps,300],
         [sliders,"m=0.1:1"], [versus_t,1]);
```

![plotdf5](figures/plotdf5.png)![plotdf6](figures/plotdf6.png)

<!-- category: Other -->
<!-- keywords: ploteq -->
<!-- signatures: ploteq(exp, ...options...) -->
### Function: ploteq (exp, ...options...)

Dibuja curvas equipotenciales para *exp*, que debe ser una expresión
dependiente de dos variables. Las curvas se obtienen integrando la ecuación
diferencial que define las trayectorias ortogonales a las soluciones del 
sistema autónomo que se obtiene del gradiente de la expresión dada.
El dibujo también puede mostrar las curvas integrales de ese sistema
de gradientes (opción `fieldlines`).


Este programa también necesita Xmaxima, incluso si se ejecuta Maxima desde
una consola, pues el dibujo se creará por el código Tk de Xmaxima.
Por defecto, la región dibujada estará vacía hasta que el
usuario haga clic en un punto, dé sus coordenadas a través del menú o
mediante la opción `trajectory_at`.


La mayor parte de opciones aceptadas por `plotdf` se pueden utilizar
también con `ploteq` y el aspecto del interfaz es el mismo que el
descrito para `plotdf`.


Ejemplo:







```maxima
(%i1) V: 900/((x+1)^2+y^2)^(1/2)-900/((x-1)^2+y^2)^(1/2)$
(%i2) ploteq(V,[x,-2,2],[y,-2,2],[fieldlines,"blue"])$
```


Haciendo clic sobre un punto se dibujará la curva equipotencial que pasa por
ese punto (en rojo) y la trayectoria ortogonal (en azul).

<!-- category: Other -->
<!-- keywords: rk -->
<!-- signatures: rk(ODE, var, initial, dominio), rk([ODE1, ..., ODEm], [v1, ..., vm], [init1, ..., initm], dominio) -->
### Function: rk (ODE, var, initial, dominio)

La primera forma se usa para resolver numéricamente una ecuación
diferencial ordinaria de primer orden (EDO), y la segunda forma resuelve
numéricamente un sistema de *m* de esas ecuaciones, usando el método
de Runge-Kutta de cuarto orden. *var* representa la variable dependiente.
EDO debe ser una expresión que dependa únicamente de las variables
independiente y dependente, y define la derivada de la variable dependiente
en función de la variable independiente.


La variable independiente se representa con *dominio*, que debe ser
una lista con cuatro elementos, como por ejemplo:


```maxima
[t, 0, 10, 0.1]
```

el primer elemento de la lista identifica la variable independiente, el
segundo y tercer elementos son los valores inicial y final para esa
variable, y el último elemento da el valor de los incrementos que
deberán ser usados dentro de ese intervalo.


Si se van a resolver *m* ecuaciones, deberá haber *m*
variables dependientes *v1*, *v2*, ..., *vm*. Los valores
iniciales para esas variables serán *inic1*,
*inic2*, ..., *inicm*. Continuará existiendo apenas una
variable independiente definida por la lista *domain*, como en
el caso anterior. *EDO1*, ..., *EDOm* son las expresiones que
definen las derivadas de cada una de las variables dependientes en
función de la variable independiente. Las únicas variables que
pueden aparecer en cada una de esas expresiones son la variable
independiente y cualquiera de las variables dependientes. Es importante
que las derivadas *EDO1*, ..., *EDOm* sean colocadas en la lista
en el mismo orden en que fueron agrupadas las variables dependientes;
por ejemplo, el tercer elemento de la lista será interpretado como la
derivada de la tercera variable dependiente.


El programa intenta integrar las ecuaciones desde el valor inicial de la
variable independiente, hasta el valor final, usando incrementos
fijos. Si en algún paso una de las variables dependientes toma un
valor absoluto muy grande, la integración será suspendida en ese
punto.  El resultado será una lista con un número de elementos igual
al número de iteraciones realizadas. Cada elemento en la lista de
resultados es también una lista con *m*+1 elementos: el valor de
la variable independiente, seguido de los valores de las variables
dependientes correspondientes a ese punto.

