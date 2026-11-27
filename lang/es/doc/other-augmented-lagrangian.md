## augmented_lagrangian

<!-- category: Other -->
<!-- keywords: augmented_lagrangian_method -->
<!-- signatures: augmented_lagrangian_method(FOM, xx, C, yy), augmented_lagrangian_method(FOM, xx, C, yy, optional_args), augmented_lagrangian_method([FOM, grad], xx, C, yy), augmented_lagrangian_method([FOM, grad], xx, C, yy, optional_args) -->
### Function: augmented_lagrangian_method (FOM, xx, C, yy)

Devuelve una aproximación del valor mínimo de
la expresión *FOM* respecto de las variables *xx*,
manteniendo las restricciones *C* igual a cero. La lista
*yy* contiene las soluciones iniciales para *xx*.
El algoritmo que se utiliza es el método del lagrangiano
aumentado (ver referencias [1] y [2]).


Si *grad* está presente en la llamada a la función, se interpreta
como el gradiente de *FOM* respecto de *xx*, representado como una
lista de tantas expresiones como variables tenga *xx*. Si el
argumento *grad* no está, se calculará de forma automática.


Tanto *FOM* como cada uno de los elementos de *grad*, si se
da como argumento, deben ser expresiones ordinarias; no admitiéndose
ni nombres de funciones ni expresiones lambda.


El argumento `optional_args` hace referencia a otros argumentos adicionales,
los cuales se especifican de la forma `symbol = value`.
Los argumentos opcionales reconocidos son:



**niter** — Número de iteraciones del algoritmo.
**lbfgs_tolerance** — Tolerancia que se pasa a LBFGS.
**iprint** — Parámetro IPRINT (lista de dos enteros que controlan la frecuencia
de mensajes) que se pasa a LBFGS.
**%lambda** — Valor inicial de `%lambda` que será utilizado para calcular el
lagrangiano aumentado.


Esta función minimiza el lagrangiano aumentado haciendo uso
del algoritmo LBFGS, que es un método de los llamados
quasi-Newton.


Antes de hacer uso de esta función ejecútense `load("augmented_lagrangian")`.


Véase también `lbfgs`.


Referencias:


[1] [http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/continuous/constrained/nonlinearcon/auglag.html]()


[2] [http://www.cs.ubc.ca/spider/ascher/542/chap10.pdf]()


Ejemplos:












```maxima
(%i1) load ("lbfgs");
(%o1)     /maxima/share/lbfgs/lbfgs.mac
(%i2) load ("augmented_lagrangian");
(%o2) 
   /maxima/share/contrib/augmented_lagrangian.mac
(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x
(%i4) xx: [x, y];
(%o4)                        [x, y]
(%i5) C: [x + y - 1];
(%o5)                      [y + x - 1]
(%i6) yy: [1, 1];
(%o6)                        [1, 1]
(%i7) augmented_lagrangian_method(FOM, xx, C, yy, iprint=[-1,0]);
(%o7) [[x = 0.66665984108002, y = 0.33334027245545], 
                                 %lambda = [- 1.333337940892525]]
```


Mismo ejemplo que en el caso anterior, pero ahora el
gradiente se suministra como argumento.














```maxima
(%i1) load ("lbfgs")$
(%i2) load ("augmented_lagrangian")$
(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x
(%i4) FOM: x^2 + 2*y^2;
                               2    2
(%o4)                       2 y  + x
(%i5) xx: [x, y];
(%o5)                        [x, y]
(%i6) grad : [2*x, 4*y];
(%o6)                      [2 x, 4 y]
(%i7) C: [x + y - 1];
(%o7)                      [y + x - 1]
(%i8) yy: [1, 1];
(%o8)                        [1, 1]
(%i9) augmented_lagrangian_method ([FOM, grad], xx, C, yy,
                                   iprint = [-1, 0]);
(%o9) [[x = 0.666659841080025, y = .3333402724554462], 
                                 %lambda = [- 1.333337940892543]]
```

