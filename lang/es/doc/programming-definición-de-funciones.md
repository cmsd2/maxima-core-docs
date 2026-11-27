## Definición de Funciones

<!-- category: Programming -->
<!-- keywords: buildq -->
<!-- signatures: buildq(L, expr) -->
### Function: buildq (L, expr)

Sustituye en paralelo las variables nombradas en la lista *L* en la expresión *expr*, sin evaluar ésta.
La expresión resultante se simplifica pero no se evalúa hasta que `buildq` termine de hacer las sustituciones.


Los elementos de *L* son símbolos o expresiones de asignación del tipo `symbol: value`,
evaluadas en paralelo. Esto es, el valor de una variable en la parte derecha de una asignación es el valor que toma dicha variable en el contexto desde el que se invoca a `buildq`. En caso de que a una variable de *L* no se le haga una signación explícita, su valor en `buildq` es el mismo que tiene en el contexto desde el que se llama a `buildq`.


Las variables referenciadas en *L* se sustituyen en *expr* en paralelo. Esto es, la sustitución para cada variable se determina antes de que se hagan las sustituciones, de forma que la sustitución de una variable no tiene efecto alguno sobre las otras.


Si alguna variable *x* aparece como `splice (x)` en *expr*, entonces a *x* se le debe asignar una lista, la cual será interpolada en *expr* en lugar de hacer una simple sustitución; ver ejemplo más abajo.


Cualesquiera otras variables de *expr* que no aparezcan en *L* se traspasan al resultado tal cual, incluso cuando tienen asignados valores en el contexto desde el que se llama a `buildq`.


Ejemplos:


`a` queda asociada explícitamente a `x`, mientras que `b` tiene la misma asociación (29) que en el contexto de llamada y `c` es traspasado al resultado sin ser sustituido. La expresión resultante no se evalúa hasta que no se le obligue a ello mediante la evaluación explícita `''%`.








```maxima
(%i1) (a: 17, b: 29, c: 1729)$
(%i2) buildq ([a: x, b], a + b + c);
(%o2)                      x + c + 29
(%i3) ''%;
(%o3)                       x + 1758
```


En este ejemplo, `e` se asocia a una lista, la cual aparece como tal en los argumentos de `foo` e interpolada en los argumentos de `bar`.







```maxima
(%i1) buildq ([e: [a, b, c]], foo (x, e, y));
(%o1)                 foo(x, [a, b, c], y)
(%i2) buildq ([e: [a, b, c]], bar (x, splice (e), y));
(%o2)                  bar(x, a, b, c, y)
```


Como se ve a continuación, el resultado se simplifica tras las sustituciones. Si la simplificación se realizase antes que las sustituciones, ambos resultados serían iguales.







```maxima
(%i1) buildq ([e: [a, b, c]], splice (e) + splice (e));
(%o1)                    2 c + 2 b + 2 a
(%i2) buildq ([e: [a, b, c]], 2 * splice (e));
(%o2)                        2 a b c
```


Las variables de *L* se asocian en paralelo; si se hiciese secuencialmente, el primer resultado sería `foo (b, b)`. Las sustituciones se llevan a cabo en paralelo. Compárese el segundo resultado con el resultado de `subst`, que hace las sustituciones de forma secuencial.










```maxima
(%i1) buildq ([a: b, b: a], foo (a, b));
(%o1)                       foo(b, a)
(%i2) buildq ([u: v, v: w, w: x, x: y, y: z, z: u],
              bar (u, v, w, x, y, z));
(%o2)                 bar(v, w, x, y, z, u)
(%i3) subst ([u=v, v=w, w=x, x=y, y=z, z=u],
             bar (u, v, w, x, y, z));
(%o3)                 bar(u, u, u, u, u, u)
```


Se construye a continuación un sistema de ecuaciones con algunas variables o expresiones en el lado izquierdo y sus valores en el derecho; `macroexpand` muestra la expresión devuelta por `show_values`.









```maxima
(%i1) show_values ([L]) ::= buildq ([L], map ("=", 'L, L));
(%o1)   show_values([L]) ::= buildq([L], map("=", 'L, L))
(%i2) (a: 17, b: 29, c: 1729)$
(%i3) show_values (a, b, c - a - b);
(%o3)          [a = 17, b = 29, c - b - a = 1683]
(%i4) macroexpand (show_values (a, b, c - a - b));
(%o4)    map(=, '([a, b, c - b - a]), [a, b, c - b - a])
```


Dada una función con varios argumentos, se crea otra función
en la cual algunos argumentos son fijos.










```maxima
(%i1) curry (f, [a]) :=
        buildq ([f, a], lambda ([[x]], apply (f, append (a, x))))$
(%i2) by3 : curry ("*", 3);
(%o2)        lambda([[x]], apply(*, append([3], x)))
(%i3) by3 (a + b);
(%o3)                       3 (b + a)
```

<!-- category: Programming -->
<!-- keywords: macroexpand -->
<!-- signatures: macroexpand(expr) -->
### Function: macroexpand (expr)

Devuelve la macroexpansión de *expr*, sin evaluarla,
cuando `expr` es una llamada a una función macro; en caso contrario,
`macroexpand` devuelve *expr*.


Si la expansión de *expr* devuelve otra llamada a una función macro, esta llamada también se expande.


La función `macroexpand` no evalúa su argumento.
Sin embargo, si la expansión de una llamada a función macro tiene efectos laterales, éstos se ejecutan.


Véanse también `::=`, `macros` y `macroexpand1`.


Ejemplos:










```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand (h (y));
                              y - a
(%o4)                         -----
                               99
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

<!-- category: Programming -->
<!-- keywords: macroexpand1 -->
<!-- signatures: macroexpand1(expr) -->
### Function: macroexpand1 (expr)

Devuelve la macroexpansión de *expr*, sin evaluarla,
cuando `expr` es una llamada a una función macro; en caso contrario,
`macroexpand1` devuelve *expr*.


La función `macroexpand1` no evalúa su argumento.
Sin embargo, si la expansión de una llamada a función macro tiene efectos laterales, éstos se ejecutan.


Si la expansión de *expr* devuelve otra llamada a una función macro, esta llamada no se expande.


Véanse también `::=`, `macros` y `macroexpand`.


Ejemplos:










```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand1 (h (y));
(%o4)                       g(y - a)
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

<!-- category: Programming -->
<!-- keywords: macros -->
<!-- signatures: macros -->
### Variable: macros

Valor por defecto: `[]`


La variable `macros` es la lista de las funciones macro definidas por el usuario.
El operador de definición de funciones macro `::=` coloca la nueva función macro en esta lista,
mientras que  `kill`, `remove` y `remfunction` eliminan las funciones macro de la lista.


Véase también `infolists`.

<!-- category: Programming -->
<!-- keywords: splice -->
<!-- signatures: splice(a) -->
### Function: splice (a)

Interpola la lista nombrada por el átomo  *a* dentro de una expresión, pero sólo si `splice` aparece dentro de `buildq`; en otro caso, `splice` se considera una función no definida. Si *a* aparece dentro de `buildq` sin `splice`, entonces queda sustituida por una lista dentro del resultado. El argumento de `splice` debe ser un átomo, no pudiendo ser una lista literal ni una expresión que devuelva una lista.


Normalmente `splice` suministra los argumentos para una función u operador. Para una función `f`, la expresión `f (splice (a))` dentro de `buildq` se convierte en `f (a[1], a[2], a[3], ...)`. Dado un operador `o`, la expresión `"o" (splice (a)` dentro de `buildq` se convierte en 
`"o" (a[1], a[2], a[3], ...)`, donde `o` puede ser cualquier tipo de operador, normalmente uno que admita varios argumentos. Nótese que el operador debe ir encerrado entre comillas dobles `"`.


Ejemplos:









```maxima
(%i1) buildq ([x: [1, %pi, z - y]], foo (splice (x)) / length (x));
                       foo(1, %pi, z - y)
(%o1)                -----------------------
                     length([1, %pi, z - y])
(%i2) buildq ([x: [1, %pi]], "/" (splice (x)));
                                1
(%o2)                          ---
                               %pi
(%i3) matchfix ("<>", "<>");
(%o3)                          <>
(%i4) buildq ([x: [1, %pi, z - y]], "<>" (splice (x)));
(%o4)                   <>1, %pi, z - y<>
```

