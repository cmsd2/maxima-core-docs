## Métodos numéricos

<!-- category: Series -->
<!-- keywords: fft -->
<!-- signatures: fft(x) -->
### Function: fft (x)

Calcula la transformada rápida compleja de Fourier.


*x* es una lista o array (declarado o no) que contiene los datos a
transformar. El número de elementos debe ser una potencia de dos.
Los elementos deben ser números literales (enteros, racionales,
de punto flotante o decimales grandes), constantes simbólicas,
expresiones del tipo `a + b*%i`, siendo `a` y `b`
números literales, o constantes simbólicas.


La función `fft` devuelve un nuevo objeto del
mismo tipo que *x*, el cual no se ve modificado. Los
resultados se calculan siempre como decimales o expresiones `a + b*%i`,
siendo `a` y `b` decimales.


La transformada discreta de Fourier se define como se indica
a continuación. Si `y` es el resultado de la transformada inversa,
entonces para `k` entre 0 y `n - 1` se tiene



```maxima
y[k] = (1/n) sum(x[j] exp(+2 %i %pi j k / n), j, 0, n - 1)
```


Si los datos *x* son reales, los coeficientes reales `a` y `b`
se pueden calcular de manera que 



```maxima
x[j] = sum(a[k]*cos(2*%pi*j*k/n)+b[k]*sin(2*%pi*j*k/n), k, 0, n/2)
```


con



```maxima
a[0] = realpart (y[0])
b[0] = 0
```


y, para k entre 1 y n/2 - 1,



```maxima
a[k] = realpart (y[k] + y[n - k])
b[k] = imagpart (y[n - k] - y[k])
```


y



```maxima
a[n/2] = realpart (y[n/2])
b[n/2] = 0
```


Para utilizar esta función ejecútese antes `load("fft")`.


Véanse también `inverse_fft` (transformada inversa), `recttopolar` y `polartorect`.


Ejemplos:


Datos reales.











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : fft (L);
(%o4) [0.0, - 1.811 %i - .1036, 0.0, .6036 - .3107 %i, 0.0, 
                         .3107 %i + .6036, 0.0, 1.811 %i - .1036]
(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 2.168L-19 %i + 2.0, 7.525L-20 %i + 3.0, 
4.256L-19 %i + 4.0, - 1.0, - 2.168L-19 %i - 2.0, 
- 7.525L-20 %i - 3.0, - 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```


Datos complejos.











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : fft (L);
(%o4) [0.5, .3536 %i + .3536, - 0.25 %i - 0.25, 
0.5 - 6.776L-21 %i, 0.0, - .3536 %i - .3536, 0.25 %i - 0.25, 
0.5 - 3.388L-20 %i]
(%i5) L2 : inverse_fft (L1);
(%o5) [1.0 - 4.066E-20 %i, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
- 1.008L-19 %i - 1.0, 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.947L-20 %i + 1.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       6.83L-17
```


Cálculo de los coeficientes del seno y coseno.

























```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, 5, 6, 7, 8] $
(%i4) n : length (L) $
(%i5) x : make_array (any, n) $
(%i6) fillarray (x, L) $
(%i7) y : fft (x) $
(%i8) a : make_array (any, n/2 + 1) $
(%i9) b : make_array (any, n/2 + 1) $
(%i10) a[0] : realpart (y[0]) $
(%i11) b[0] : 0 $
(%i12) for k : 1 thru n/2 - 1 do
   (a[k] : realpart (y[k] + y[n - k]),
    b[k] : imagpart (y[n - k] - y[k]));
(%o12)                        done
(%i13) a[n/2] : y[n/2] $
(%i14) b[n/2] : 0 $
(%i15) listarray (a);
(%o15)          [4.5, - 1.0, - 1.0, - 1.0, - 0.5]
(%i16) listarray (b);
(%o16)           [0, - 2.414, - 1.0, - .4142, 0]
(%i17) f(j) := sum (a[k] * cos (2*%pi*j*k / n) + b[k] * sin (2*%pi*j*k / n), k, 0, n/2) $
(%i18) makelist (float (f (j)), j, 0, n - 1);
(%o18)      [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
```

<!-- category: Series -->
<!-- keywords: inverse_fft -->
<!-- signatures: inverse_fft(y) -->
### Function: inverse_fft (y)

Calcula la transformada inversa rápida de Fourier.


*y* es una lista o array (declarado o no) que contiene los datos a
transformar. El número de elementos debe ser una potencia de dos.
Los elementos deben ser números literales (enteros, racionales,
de punto flotante o decimales grandes), constantes simbólicas,
expresiones del tipo `a + b*%i`, siendo `a` y `b`
números literales, o constantes simbólicas.


La función `inverse_fft` devuelve un nuevo objeto del
mismo tipo que *y*, el cual no se ve modificado. Los
resultados se calculan siempre como decimales o expresiones `a + b*%i`,
siendo `a` y `b` decimales.


La transformada inversa discreta de Fourier se define como se indica
a continuación. Si `x` es el resultado de la transformada inversa,
entonces para `j` entre 0 y `n - 1` se tiene



```maxima
x[j] = sum(y[k] exp(-2 %i %pi j k / n), k, 0, n - 1)
```


Para utilizar esta función ejecútese antes `load("fft")`.


Véanse también `fft` (transformada directa), `recttopolar` y `polartorect`.


Ejemplos:


Datos reales.











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : inverse_fft (L);
(%o4) [0.0, 14.49 %i - .8284, 0.0, 2.485 %i + 4.828, 0.0, 
                       4.828 - 2.485 %i, 0.0, - 14.49 %i - .8284]
(%i5) L2 : fft (L1);
(%o5) [1.0, 2.0 - 2.168L-19 %i, 3.0 - 7.525L-20 %i, 
4.0 - 4.256L-19 %i, - 1.0, 2.168L-19 %i - 2.0, 
7.525L-20 %i - 3.0, 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```


Datos complejos.











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $                 
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : inverse_fft (L);
(%o4) [4.0, 2.711L-19 %i + 4.0, 2.0 %i - 2.0, 
- 2.828 %i - 2.828, 0.0, 5.421L-20 %i + 4.0, - 2.0 %i - 2.0, 
2.828 %i + 2.828]
(%i5) L2 : fft (L1);
(%o5) [4.066E-20 %i + 1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
1.55L-19 %i - 1.0, - 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.0 - 7.368L-20 %i]
(%i6) lmax (abs (L2 - L));                    
(%o6)                       6.841L-17
```

<!-- category: Series -->
<!-- keywords: polartorect -->
<!-- signatures: polartorect(magnitude_array, phase_array) -->
### Function: polartorect (magnitude_array, phase_array)

Transforma valores complejos de la forma `r %e^(%i t)` a la forma
`a + b %i`, siendo *r* el módulo y *t* la fase.
Ambos valores *r* y *t* son arrays unidimensionales cuyos
tamños son iguales a la misma potencia de dos.


Los valores originales de los arrays de entrada son reemplazados por
las partes real e imaginaria, `a` y `b`, de los correspondientes
números complejos. El resultado se calcula como



```maxima
a = r cos(t)
b = r sin(t)
```


`polartorect` es la función inversa de `recttopolar`.


Para utilizar esta función ejecútese antes `load("fft")`.
Véase también `fft`.

<!-- category: Series -->
<!-- keywords: recttopolar -->
<!-- signatures: recttopolar(real_array, imaginary_array) -->
### Function: recttopolar (real_array, imaginary_array)

Transforma valores complejos de la forma `a + b %i` a la forma
`r %e^(%i t)`, siendo *a* la parte real y *a* la imaginaria.
Ambos valores *a* y *b* son arrays unidimensionales cuyos
tamños son iguales a la misma potencia de dos.


Los valores originales de los arrays de entrada son reemplazados por
los módulos y las fases, `r` y `t`, de los correspondientes
números complejos. El resultado se calcula como



```maxima
r = sqrt(a^2 + b^2)
t = atan2(b, a)
```


El ángulo calculado pertence al rango de `-%pi` a `%pi`. 


`recttopolar` es la función inversa de `polartorect`.


Para utilizar esta función ejecútese antes `load("fft")`.
Véase también `fft`.

