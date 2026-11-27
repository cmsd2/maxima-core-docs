## Funciones matemáticas

<!-- category: Combinatorics -->
<!-- keywords: !! -->
<!-- signatures: !! -->
### Function: !!

El operador doble factorial.


Para un número entero, de punto flotante o racional `n`,
`n!!` se evaluará como el producto de `n (n-2) (n-4) (n-6) ... (n - 2 (k-1))`
donde `k` es igual a `entier(n/2)`, que es, el mayor entero
menor o igual a `n/2`. 
Note que esta definición no coincide con otras definciones publicadas para argumentos, los cuales no son enteros. 




Para un entero par (o impar) `n`, `n!` se evalua el producto de
todos los enteros pares (o impares) consecutivos desde 2 (o 1) por `n` inclusive.  


Para un argumento `n` el cual no es un número entero, punto flotante o racional, `n!!` produce una forma de nombre `genfact (n, n/2, 2)`.

<!-- category: Combinatorics -->
<!-- keywords: binomial -->
<!-- signatures: binomial(x, y) -->
### Function: binomial (x, y)

Es el coeficiente binomial `x!/(y! (x - y)!)`.
Si *x* y *y* son enteros, entonces se calcula el valor numérico 
del coeficiente binomial. Si *y* o *x - y* son enteros, 
el coeficiente binomial se expresa como un polinomio.


Ejemplos:










```maxima
(%i1) binomial (11, 7);
(%o1)                          330
(%i2) 11! / 7! / (11 - 7)!;
(%o2)                          330
(%i3) binomial (x, 7);
        (x - 6) (x - 5) (x - 4) (x - 3) (x - 2) (x - 1) x
(%o3)   -------------------------------------------------
                              5040
(%i4) binomial (x + 7, x);
      (x + 1) (x + 2) (x + 3) (x + 4) (x + 5) (x + 6) (x + 7)
(%o4) -------------------------------------------------------
                               5040
(%i5) binomial (11, y);
(%o5)                    binomial(11, y)
```

<!-- category: Combinatorics -->
<!-- keywords: factcomb -->
<!-- signatures: factcomb(expr) -->
### Function: factcomb (expr)

Trata de combinar los coeficientes de los factoriales de *expr* con los mismos factoriales, convirtiendo, por ejemplo, `(n + 1)*n!` en `(n + 1)!`.


Si la variable `sumsplitfact` vale `false` hará que `minfactorial` se aplique después de `factcomb`.

<!-- category: Combinatorics -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

Valor por defecto: -1


La variable `factlim` especifica el mayor factorial que será expandido automáticamente.  Si su valor es -1, entonces se expandirán todos los enteros.

<!-- category: Combinatorics -->
<!-- keywords: factorial, ! -->
<!-- signatures: factorial(x), ! -->
### Function: factorial (x)

Representa la función factorial. Maxima considera `factorial (x)`
y `x!` como sinónimos.


Para cualquier número complejo `x`, excepto para
enteros negativos, `x!` se define como `gamma(x+1)`. 


Para un entero `x`, `x!` se reduce al producto de los enteros
desde 1 hasta `x` inclusive. `0!` se reduce a 1.
Para un número real o complejo en formato de coma flotante `x`, 
`x!` se reduce al valor de `gamma(x+1)`. Cuando
`x` es igual a `n/2`, siendo `n` un entero impar, entonces
`x!` se reduce a un factor racional multiplicado por `sqrt(%pi)`
(pues `gamma(1/2)`) es igual a `sqrt(%pi)`).


Las variables opcionales `factlim` y `gammalim` controlan la
evaluación numérica de factoriales de argumentos enteros y racionales.


Las funciones `minfactorial` y `factcomb` simplifican expresiones
que contiene factoriales.


Véanse también `factlim`, `gammalim`, `minfactorial` y 
`factcomb`.


Las funciones `gamma`, `bffac` y `cbffac` son variaciones de
la función matemática gamma. Las funciones `bffac` y `cbffac` 
son llamadas internamente desde `gamma` para evaluar la función gamma 
de números reales y complejos decimales con precisión de reales grandes
(bigfloats).


Las funciones `makegamma` substituye a `gamma` para factoriales 
y funciones relacionadas. 


Maxima reconoce la derivada de la función factorial y los límites
para ciertos valores específicos, tales como los enteros negativos.


La variable opcional `factorial_expand` controla la simplificación de
expresiones como `(n+x)!`, para `n` entero.


Véase también `binomial`.


Ejemplos:


El factorial de un entero se reduce a un número exacto, a menos que
el argumento sea mayor que `factlim`. Los factoriales de números
reales o complejos se evalúan como decimales de coma flotante.









```maxima
(%i1) factlim:10;
(%o1)                                 10
(%i2) [0!, (7/2)!, 8!, 20!];
                            105 sqrt(%pi)
(%o2)                   [1, -------------, 40320, 20!]
                                 16
(%i3) [4.77!, (1.0+%i)!];
(%o3)    [81.44668037931197, 
          .3430658398165454 %i + .6529654964201665]
(%i4) [2.86b0!, (1.0b0+%i)!];
(%o4) [5.046635586910012b0, 
       3.430658398165454b-1 %i + 6.529654964201667b-1]
```


El factorial de una constante conocida o de una expresión general
no se calcula. Pero puede ser posible reducir el factorial después de
evaluado el argumento.







```maxima
(%i1) [(%i + 1)!, %pi!, %e!, (cos(1) + sin(1))!];
(%o1)      [(%i + 1)!, %pi!, %e!, (sin(1) + cos(1))!]
(%i2) ev (%, numer, %enumer);
(%o2) [.3430658398165454 %i + .6529654964201665, 
       7.188082728976031, 
       4.260820476357003, 1.227580202486819]
```


Los factoriales son simplificados o reducidos, no evaluados.
Así `x!` puede ser reemplazado en una expresión 
nominal. 






```maxima
(%i1) '([0!, (7/2)!, 4.77!, 8!, 20!]);
          105 sqrt(%pi)
(%o1) [1, -------------, 81.44668037931199, 40320, 
               16
                             2432902008176640000]
```


Maxima reconoce la derivada de la función factorial.






```maxima
(%i1) diff(x!,x);
(%o1)                           x! psi (x + 1)
                                      0
```


La variable opcional `factorial_expand` controla la simplificación de
expresiones con la función factorial.






```maxima
(%i1) (n+1)!/n!,factorial_expand:true;
(%o1)                                n + 1
```

<!-- category: Combinatorics -->
<!-- keywords: factorial_expand -->
<!-- signatures: factorial_expand -->
### Variable: factorial_expand

Valor por defecto: false


La variable `factorial_expand` controla la simplificación
de expresiones tales como `(n+1)!`, siendo `n` un entero. 


Véase `!` para un ejemplo.

<!-- category: Combinatorics -->
<!-- keywords: genfact -->
<!-- signatures: genfact(x, y, z) -->
### Function: genfact (x, y, z)

Devuelve el factorial generalizado, definido como
`x (x-z) (x - 2 z) ... (x - (y - 1) z)`.  Así, para el entero *x*,
`genfact (x, x, 1) = x!` y `genfact (x, x/2, 2) = x!!`.

<!-- category: Combinatorics -->
<!-- keywords: minfactorial -->
<!-- signatures: minfactorial(expr) -->
### Function: minfactorial (expr)

Busca en *expr* la presencia de dos factoriales que solo se
diferencien en una unidad; en tal caso, `minfactorial`
devuelve una expresión simplificada.



```maxima
(%i1) n!/(n+2)!;
                               n!
(%o1)                       --------
                            (n + 2)!
(%i2) minfactorial (%);
                                1
(%o2)                    ---------------
                         (n + 1) (n + 2)
```

<!-- category: Combinatorics -->
<!-- keywords: sumsplitfact -->
<!-- signatures: sumsplitfact -->
### Variable: sumsplitfact

Valor por defecto: `true`


Si `sumsplitfact` vale `false`,

`minfactorial` se aplica después de  `factcomb`.

