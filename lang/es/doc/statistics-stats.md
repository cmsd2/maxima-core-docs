## stats

<!-- category: Statistics -->
<!-- keywords: cdf_rank_sum -->
<!-- signatures: cdf_rank_sum(x, n, m) -->
### Function: cdf_rank_sum (x, n, m)

Función de probabilidad acumulada de la distribución exacta
del estadístico de contraste de Wilcoxon-Mann-Whitney.
El argumento *x* es un número real y
*n* y *m* son ambos enteros positivos.


Véase también `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: cdf_signed_rank -->
<!-- signatures: cdf_signed_rank(x, n) -->
### Function: cdf_signed_rank (x, n)

Función de probabilidad acumulada de la distribución exacta
del estadístico de contraste del test de los
rangos signados. El argumento *x* es un número real y
*n* un entero positivo.


Véase también `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: inference_result -->
<!-- signatures: inference_result(title, values, numbers) -->
### Function: inference_result (title, values, numbers)

Construye un objeto `inference_result` del tipo devuelto por las funciones
estadísticas. El argumento *title* es una cadena con
el nombre del procedimiento; *values* es una lista con elementos de la
forma `symbol = value` y *numbers* es una lista con enteros positivos
desde uno hasta `length(values)`, que indican qué valores serán
mostrados por defecto.


Ejemplo:


Este es un ejemplo que muestra los resultados asociados a un rectángulo. El
título de este objeto es la cadena `"Rectangle"`, el cual
almacena cinco resultados, a saber, `'base`, `'height`, 
`'diagonal`, `'area` y `'perimeter`, pero sólo muestra
el primero, segundo, quinto y cuarto. El resultado `'diagonal` también
se almacena en este objeto, pero no se muestra por defecto; para tener acceso
a este valor, hágase uso de la función `take_inference`.















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) inference_result("Rectangle",
                        ['base=b,
                         'height=h,
                         'diagonal=sqrt(b^2+h^2),
                         'area=b*h,
                         'perimeter=2*(b+h)],
                        [1,2,5,4] );
                        |   Rectangle
                        |
                        |    base = 3
                        |
(%o3)                   |   height = 2
                        |
                        | perimeter = 10
                        |
                        |    area = 6
(%i4) take_inference('diagonal,%);
(%o4)                        sqrt(13)
```


Véase también `take_inference`.

<!-- category: Statistics -->
<!-- keywords: inferencep -->
<!-- signatures: inferencep(obj) -->
### Function: inferencep (obj)

Devuelve `true` o `false`, dependiendo de que *obj* sea un
objeto de tipo `inference_result` o no.

<!-- category: Statistics -->
<!-- keywords: items_inference -->
<!-- signatures: items_inference(obj) -->
### Function: items_inference (obj)

Devuelve una lista con los nombres de los elementos almacenados en
*obj*, el cual debe ser un objeto de tipo `inference_result`.


Ejemplo:


El objeto `inference_result` almacena dos valores, cuyos nombres son `'pi` y `'e`,
pero sólo se muestra el segundo. La función `items_inference` devuelve los nombres de 
todos los elementos almacenados, independientemente de que sean mostrados o no.








```maxima
(%i1) load("inference_result")$
(%i2) inference_result("Hi", ['pi=%pi,'e=%e],[2]);
                            |   Hi
(%o2)                       |
                            | e = %e
(%i3) items_inference(%);
(%o3)                        [pi, e]
```

<!-- category: Statistics -->
<!-- keywords: linear_regression -->
<!-- signatures: linear_regression(x), linear_regression(xoption) -->
### Function: linear_regression (x)

Regresión lineal múltiple, 
$y_i = b0 + b1*x_1i + b2*x_2i + ... + bk*x_ki + u_i$,
donde $u_i$ son variables aleatorias independientes 
$N(0,sigma)$. El argumento *x* debe ser una matriz 
con más de una columna. La última columna se considera
que son las respuestas ($y_i$).


Opción:



- *
`'conflevel`, valor por defecto `95/100`, nivel de
confianza para los intervalos de confianza; debe ser una expresión 
que tome un valor en el intervalo (0,1).


El resultado devuelto por la función `linear_regression` es
un objeto `inference_result` de Maxima con los siguientes campos:



1. `'b_estimation`: estimadores de los coeficientes de regresión.
2. `'b_covariances`: matriz de covarianzas de los estimadores
de los coeficientes de regresión.
3. `b_conf_int`: intervalos de confianza para los coeficientes de regresión.
4. `b_statistics`: estadísticos para los contrastes
de los coeficientes.
5. `b_p_values`: p-valores para los contrastes de los coeficientes.
6. `b_distribution`: distribución de probabilidad para
los contrastes de los coeficientes.
7. `v_estimation`: estimador insesgado de la varianza.
8. `v_conf_int`: intervalo de confianza de la varianza.
9. `v_distribution`: distribución de probabilidad para
el contraste de la varianza.
10. `residuals`: residuos.
11. `adc`: coeficiente de determinación ajustado.
12. `aic`: Criterio de información de Akaike.
13. `bic`: Criterio de información de Bayes.


Solamente los apartados 1, 4, 5, 6, 7, 8, 9 y 11, en este orden, 
se muestran por defecto. El resto permanecen ocultos hasta que
el usuario haga uso de las funciones `items_inference`
y `take_inference`.


Ejemplo:


Ajustando un modelo lineal a una muestra tridimensional. La 
última columna se considera que son las respuestas ($y_i$).




















```maxima
(%i2) load("stats")$
(%i3) X:matrix(
    [58,111,64],[84,131,78],[78,158,83],
    [81,147,88],[82,121,89],[102,165,99],
    [85,174,101],[102,169,102])$
(%i4) fpprintprec: 4$
(%i5) res: linear_regression(X);
             |       LINEAR REGRESSION MODEL         
             |                                       
             | b_estimation = [9.054, .5203, .2397]  
             |                                       
             | b_statistics = [.6051, 2.246, 1.74]   
             |                                       
             | b_p_values = [.5715, .07466, .1423]   
             |                                       
(%o5)        |   b_distribution = [student_t, 5]     
             |                                       
             |         v_estimation = 35.27          
             |                                       
             |     v_conf_int = [13.74, 212.2]       
             |                                       
             |      v_distribution = [chi2, 5]       
             |                                       
             |             adc = .7922               
(%i6) items_inference(res);
(%o6) [b_estimation, b_covariances, b_conf_int, b_statistics, 
b_p_values, b_distribution, v_estimation, v_conf_int, 
v_distribution, residuals, adc, aic, bic]
(%i7) take_inference('b_covariances, res);
                  [  223.9    - 1.12   - .8532  ]
                  [                             ]
(%o7)             [ - 1.12    .05367   - .02305 ]
                  [                             ]
                  [ - .8532  - .02305   .01898  ]
(%i8) take_inference('bic, res);
(%o8)                          30.98
(%i9) load("draw")$
(%i10) draw2d(
    points_joined = true,
    grid = true,
    points(take_inference('residuals, res)) )$
```

<!-- category: Statistics -->
<!-- keywords: pdf_rank_sum -->
<!-- signatures: pdf_rank_sum(x, n, m) -->
### Function: pdf_rank_sum (x, n, m)

Función de densidad de probabilidad de la distribución exacta
del estadístico de contraste de Wilcoxon-Mann-Whitney.
El argumento *x* es un número real y
*n* y *m* son ambos enteros positivos.


Véase también `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: pdf_signed_rank -->
<!-- signatures: pdf_signed_rank(x, n) -->
### Function: pdf_signed_rank (x, n)

Función de densidad de probabilidad de la distribución exacta
del estadístico de contraste del test de los
rangos signados. El argumento *x* es un número real y
*n* un entero positivo.


Véase también `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: stats_numer -->
<!-- signatures: stats_numer -->
### Variable: stats_numer

Valor por defecto: `true`


Cuando `stats_numer` vale `true`, las funciones de inferencia
estadística devuelven sus resultados en formato decimal de
coma flotante. Cuando vale `false`, los resultados se devuelven en
formato simbólico y racional.

<!-- category: Statistics -->
<!-- keywords: take_inference -->
<!-- signatures: take_inference(n, obj), take_inference(name, obj), take_inference(list, obj) -->
### Function: take_inference (n, obj)

Si *n* es un entero positivo, devuelve el *n*-ésimo
valor almacenado en *obj*; si el símbolo *name*
es el nombre de uno de los elementos almacenados, también
devuelve su valor. Si el primer elemento es una lista de números y/o 
símbolos, la función `take_inference`
devuelve una lista con los resultados correspondientes.


Ejemplo:


Dado un objeto `inference_result`, la función `take_inference`
es invocada para extraer cierta información almacenada en él.


















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) sol: inference_result("Rectangle",
                            ['base=b,
                             'height=h,
                             'diagonal=sqrt(b^2+h^2),
                             'area=b*h,
                             'perimeter=2*(b+h)],
                            [1,2,5,4] );
                        |   Rectangle
                        |
                        |    base = 3
                        |
(%o3)                   |   height = 2
                        |
                        | perimeter = 10
                        |
                        |    area = 6
(%i4) take_inference('base,sol);
(%o4)                           3
(%i5) take_inference(5,sol);
(%o5)                          10
(%i6) take_inference([1,'diagonal],sol);
(%o6)                     [3, sqrt(13)]
(%i7) take_inference(items_inference(sol),sol);
(%o7)                [3, 2, sqrt(13), 6, 10]
```


Véanse también `inference_result` y `take_inference`.

<!-- category: Statistics -->
<!-- keywords: test_mean -->
<!-- signatures: test_mean(x), test_mean(x, options...) -->
### Function: test_mean (x)

Es el test *t* de la media. El argumento *x* es una lista o matriz
columna con los datos de una muestra unidimensional. También realiza el
test asintótico basado en el *Teorema Central del límite*
si se le asigna a la opción `'asymptotic` el valor `true`.


Opciones:



- *
`'mean`, valor por defecto `0`, es el valor de la media a contrastar.
- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'dev`, valor por defecto `'unknown`, este es el valor de la desviación
típica cuando se conoce; valores válidos son: `'unknown` o una
expresión con valor positivo.
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el intervalo de confianza;
debe ser una expresión que tome un valor en el intervalo (0,1).
- *
`'asymptotic`, valor por defecto `false`, indica si debe realizar el test
exacto basado en la *t* de Student, o el asintótico basado en el
*Teorema Central del límite*; valores válidos son `true` y `false`.


El resultado devuelto por la función  `test_mean` es un objeto
`inference_result` con los siguientes apartados:



1. `'mean_estimate`: la media muestral.
2. `'conf_level`: nivel de confianza seleccionado por el usuario.
3. `'conf_interval`: intervalo de confianza para la media poblacional.
4. `'method`: procedimiento de inferencia.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con su(s) parámetro(s).
8. `'p_value`: $p$-valor del test.


Ejemplos:


Realiza el contraste exacto *t* con varianza desconocida. La
hipótesis nula es $H_0: mean=50$, frente a la alternativa
unilátera $H_1: mean<50$; de acuerdo con los resultados,
no hay evidencia para rechazar $H_0$, pues el $p$-valor
es muy grande.








```maxima
(%i1) load("stats")$
(%i2) data: [78,64,35,45,45,75,43,74,42,42]$
(%i3) test_mean(data,'conflevel=0.9,'alternative='less,'mean=50);
          |                 MEAN TEST
          |
          |            mean_estimate = 54.3
          |
          |              conf_level = 0.9
          |
          | conf_interval = [minf, 61.51314273502712]
          |
(%o3)     |  method = Exact t-test. Unknown variance.
          |
          | hypotheses = H0: mean = 50 , H1: mean < 50
          |
          |       statistic = .8244705235071678
          |
          |       distribution = [student_t, 9]
          |
          |        p_value = .7845100411786889
```


En esta ocasión Maxima realiza un test asintótico. La hipótesis
nula es $H_0: equal(mean, 50)$ frente a la alternativa bilátera $H_1: not equal(mean, 50)$;
de acuerdo con los resultados, $H_0$ debe rechazarse en favor de
la alternativa $H_1$, pues el $p$-valor es muy pequeño. 
Nótese que, tal como indica la componente `Method`, este
procedimiento sólo puede aplicarse en muestras grandes.










```maxima
(%i1) load("stats")$
(%i2) test_mean([36,118,52,87,35,256,56,178,57,57,89,34,25,98,35,
              98,41,45,198,54,79,63,35,45,44,75,42,75,45,45,
              45,51,123,54,151],
              'asymptotic=true,'mean=50);
          |                       MEAN TEST
          |
          |           mean_estimate = 74.88571428571429
          |
          |                   conf_level = 0.95
          |
          | conf_interval = [57.72848600856194, 92.04294256286663]
          |
(%o2)     |    method = Large sample z-test. Unknown variance.
          |
          |       hypotheses = H0: mean = 50 , H1: mean # 50
          |
          |             statistic = 2.842831192874313
          |
          |             distribution = [normal, 0, 1]
          |
          |             p_value = .004471474652002261
```

<!-- category: Statistics -->
<!-- keywords: test_means_difference -->
<!-- signatures: test_means_difference(x1, x2), test_means_difference(x1, x2, options...) -->
### Function: test_means_difference (x1, x2)

Este es el test *t* para la diferencia de medias con muestras.
Los argumentos *x1* y *x2* son listas o matrices columna
que contienen dos muestras independientes. En caso de varianzas
diferentes y desconocidas (véanse las opciones `'dev1`,
`'dev2` y `'varequal` más abajo) los grados de libertad
se calculan mediante la aproximación de Welch.
También realiza el test asintótico basado en el
*Teorema Central del límite* si se le asigna a 
la opción `'asymptotic` el valor `true`.


Opciones:



- *
- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'dev1`, valor por defecto `'unknown`, es el valor de la desviación 
típica de la muestra *x1* cuando se conoce; valores válidos 
son: `'unknown` o una expresión positiva.
- *
`'dev2`, valor por defecto `'unknown`, es el valor de la desviación 
típica de la muestra *x2* cuando se conoce; valores válidos 
son: `'unknown` o una expresión positiva.
- *
`'varequal`, valor por defecto `false`, indica si las varianzas deben considerarse iguales o no; esta opción sólo toma efecto cuando `'dev1` y/o `'dev2` tienen el valor `'unknown`.
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el
intervalo de confianza; debe ser una expresión que tome un valor en el intervalo (0,1).
- *
`'asymptotic`, valor por defecto `false`, indica si debe realizar el test
exacto basado en la *t* de Student, o el asintótico basado en el
*Teorema Central del límite*; valores válidos son `true` y `false`.


El resultado devuelto por la función  `test_means_difference` es un objeto
`inference_result` con los siguientes apartados:



1. `'diff_estimate`: el estimador de la diferencia de medias.
2. `'conf_level`: nivel de confianza seleccionado por el usuario.
3. `'conf_interval`: intervalo de confianza para la diferencia de medias.
4. `'method`: procedimiento de inferencia.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con su(s) parámetro(s).
8. `'p_value`: $p$-valor del test.


Ejemplos:


La igualdad de medias se contrasta con dos pequeñas muestras
*x* y *y*, contra la alternativa $H_1: m_1>m_2$,
siendo $m_1$ y $m_2$ las medias poblacionales; las
varianzas son desconocidas y se supone que diferentes.














```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: [1.2,6.9,38.7,20.4,17.2]$
(%i4) test_means_difference(x,y,'alternative='greater);
            |              DIFFERENCE OF MEANS TEST
            |
            |         diff_estimate = 20.31999999999999
            |
            |                 conf_level = 0.95
            |
            |    conf_interval = [- .04597417812882298, inf]
            |
(%o4)       |        method = Exact t-test. Welch approx.
            |
            | hypotheses = H0: mean1 = mean2 , H1: mean1 > mean2
            |
            |           statistic = 1.838004300728477
            |
            |    distribution = [student_t, 8.62758740184604]
            |
            |            p_value = .05032746527991905
```


El mismo test que antes, pero ahora se suponen las varianzas
iguales.
















```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: matrix([1.2],[6.9],[38.7],[20.4],[17.2])$
(%i4) test_means_difference(x,y,
                            'alternative='greater,
                            'varequal=true);
            |              DIFFERENCE OF MEANS TEST
            |
            |         diff_estimate = 20.31999999999999
            |
            |                 conf_level = 0.95
            |
            |     conf_interval = [- .7722627696897568, inf]
            |
(%o4)       |   method = Exact t-test. Unknown equal variances
            |
            | hypotheses = H0: mean1 = mean2 , H1: mean1 > mean2
            |
            |           statistic = 1.765996124515009
            |
            |           distribution = [student_t, 9]
            |
            |            p_value = .05560320992529344
```

<!-- category: Statistics -->
<!-- keywords: test_normality -->
<!-- signatures: test_normality(x) -->
### Function: test_normality (x)

Test de Shapiro-Wilk para el contraste de normalidad. El argumento
*x* es una lista de números, con tamaño muestral mayor que 2
y menor o igual que 5000; bajo cualesquiera otras condiciones, la
función `test_normality` emite un mensaje de error.


Referencia:


  

[1] Algorithm AS R94, Applied Statistics (1995), vol.44, no.4, 547-551


El resultado devuelto por la función `test_normality` es
un objeto `inference_result` con los siguientes apartados:




1. `'statistic`: valor del estadístico *W*.
2. `'p_value`: $p$-valor bajo la hipótesis de normalidad.


Ejemplos:


Contrasta la normalidad de una población a partir de una muestra
de tamaño 9.












```maxima
(%i1) load("stats")$
(%i2) x:[12,15,17,38,42,10,23,35,28]$
(%i3) test_normality(x);
                       |      SHAPIRO - WILK TEST
                       |
(%o3)                  | statistic = .9251055695162436
                       |
                       |  p_value = .4361763918860381
```

<!-- category: Statistics -->
<!-- keywords: test_proportion -->
<!-- signatures: test_proportion(x, n), test_proportion(x, n, options...) -->
### Function: test_proportion (x, n)

Inferencias sobre una proporción. El argumento *x* es el
número de éxitos observados en *n* pruebas de Bernoulli
con probabilidad desconocida.


Opciones:



- *
`'proportion`, valor por defecto `1/2`, es el valor de la
probabilidad a contrastar.
- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el intervalo
de confianza; debe ser una expresión que tome un valor en el intervalo (0,1).
- *
`'asymptotic`, valor por defecto `false`, indica si debe realizar el test
exacto basado en la binomial, o el asintótico basado en el
*Teorema Central del límite*; valores válidos son `true` y `false`.
- *
`'correct`, valor por defecto `true`, indica si se aplica o no la
corrección de Yates.


El resultado devuelto por la función `test_proportion` es un objeto
`inference_result` con los siguientes apartados:



1. `'sample_proportion`: proporción muestral.
2. `'conf_level`: nivel de confianza seleccionado.
3. `'conf_interval`: intervalo de confianza de Wilson para la proporción.
4. `'method`: procedimiento de inferencia.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado
para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con sus parámetros.
8. `'p_value`: $p$-valor del test.


Ejemplos:


Realiza un contraste exacto. La hipótesis nula es $H_0: p=1/2$ 
y la alternativa unilátera es $H_1: p<1/2$.







```maxima
(%i1) load("stats")$
(%i2) test_proportion(45, 103, alternative = less);
         |            PROPORTION TEST              
         |                                         
         | sample_proportion = .4368932038834951   
         |                                         
         |           conf_level = 0.95             
         |                                         
         | conf_interval = [0, 0.522714149150231]  
         |                                         
(%o2)    |     method = Exact binomial test.       
         |                                         
         | hypotheses = H0: p = 0.5 , H1: p < 0.5  
         |                                         
         |             statistic = 45              
         |                                         
         |  distribution = [binomial, 103, 0.5]    
         |                                         
         |      p_value = .1184509388901454
```


Un contraste asintótico bilátero. El nivel de confianza es 99/100.









```maxima
(%i1) load("stats")$
(%i2) fpprintprec:7$
(%i3) test_proportion(45, 103, 
                  conflevel = 99/100, asymptotic=true);
      |                 PROPORTION TEST                  
      |                                                  
      |           sample_proportion = .43689             
      |                                                  
      |                conf_level = 0.99                 
      |                                                  
      |        conf_interval = [.31422, .56749]          
      |                                                  
(%o3) | method = Asympthotic test with Yates correction. 
      |                                                  
      |     hypotheses = H0: p = 0.5 , H1: p # 0.5       
      |                                                  
      |               statistic = .43689                 
      |                                                  
      |      distribution = [normal, 0.5, .048872]       
      |                                                  
      |                p_value = .19662
```

<!-- category: Statistics -->
<!-- keywords: test_proportions_difference -->
<!-- signatures: test_proportions_difference(x1, n1, x2, n2), test_proportions_difference(x1, n1, x2, n2, options...) -->
### Function: test_proportions_difference (x1, n1, x2, n2)

Inferencias sobre la diferencia de dos proporciones. El argumento *x1* 
es el número de éxitos en *n1* experimentos de Bernoulli en la
primera población y *x2* y *n2* son los valores correspondientes
para la segunda población. Las muestras son independientes y el contraste
es asintótico.


Opciones:



- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son:: `'twosided` (`p1 # p2`), `'greater` (`p1 > p2`)
and `'less` (`p1 < p2`).
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el intervalo
de confianza; debe ser una expresión que tome un valor en el intervalo (0,1).
- *
`'correct`, valor por defecto `true`, indica si se aplica o no la
corrección de Yates.


El resultado devuelto por la función `test_proportions_difference` es un objeto
`inference_result` con los siguientes apartados:



1. `'proportions`: lista con las dos proporciones muestrales.
2. `'conf_level`: nivel de confianza seleccionado.
3. `'conf_interval`: intervalo de confianza para la diferencia de proporciones `p1 - p2`.
4. `'method`: procedimiento de inferencia y mensaje de aviso en caso de que
alguno de los tamaños muestrales sea menor de 10.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado
para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con sus parámetros.
8. `'p_value`: $p$-valor del test.


Ejemplos:


Una máquina produce 10 piezas defectuosas en un lote de 250.
Después de ciertas tareas de mantenimiento, produce 4 piezas
defectuosas de un lote de 150. A fin de saber si la tarea de 
mantenimiento produjo alguna mejora, se contrasta la hipótesis
nula `H0:p1=p2` contra la alternativa `H0:p1>p2`,
donde `p1` y `p2` son las probabilidades de que un
artículo producido por la máquina sea defectuoso,
antes y después de la reparación. De acuerdo con el p valor, no hay
evidencia suficiente para aceptar la alternativa.









```maxima
(%i1) load("stats")$
(%i2) fpprintprec:7$
(%i3) test_proportions_difference(10, 250, 4, 150,
                                alternative = greater);
      |       DIFFERENCE OF PROPORTIONS TEST         
      |                                              
      |       proportions = [0.04, .02666667]        
      |                                              
      |              conf_level = 0.95               
      |                                              
      |      conf_interval = [- .02172761, 1]        
      |                                              
(%o3) | method = Asymptotic test. Yates correction.  
      |                                              
      |   hypotheses = H0: p1 = p2 , H1: p1 > p2     
      |                                              
      |            statistic = .01333333             
      |                                              
      |    distribution = [normal, 0, .01898069]     
      |                                              
      |             p_value = .2411936
```


Desviación típica exacta de la
distribución normal asintótica con datos
desconocidos.









```maxima
(%i1) load("stats")$
(%i2) stats_numer: false$
(%i3) sol: test_proportions_difference(x1,n1,x2,n2)$
(%i4) last(take_inference('distribution,sol));
               1    1                  x2 + x1
              (-- + --) (x2 + x1) (1 - -------)
               n2   n1                 n2 + n1
(%o4)    sqrt(---------------------------------)
                           n2 + n1
```

<!-- category: Statistics -->
<!-- keywords: test_rank_sum -->
<!-- signatures: test_rank_sum(x1, x2), test_rank_sum(x1, x2, option) -->
### Function: test_rank_sum (x1, x2)

Este es el test de Wilcoxon-Mann-Whitney para comparar las medianas
de dos poblaciones continuas. Los dos primeros argumentos *x1*
y *x2* son listas o matrices columna con los datos de dos
muestras independientes. Realiza la aproximación normal si
alguna de las muestras tiene tamaño mayor que 10, o si hay
empates.



Opción:



- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.


El resultado devuelto por la función  `test_rank_sum`
es un objeto `inference_result` con los siguientes apartados:



1. `'method`: procedimiento de inferencia.
2. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
3. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
4. `'distribution`: distribución del estadístico de contraste, junto con sus parámetros.
5. `'p_value`: $p$-valor del test.


Ejemplos:


Contrasta si dos poblaciones tiene medianas similares. Al ser los tamaños
muestrales pequeños, se realiza el test exacto.














```maxima
(%i1) load("stats")$
(%i2) x:[12,15,17,38,42,10,23,35,28]$
(%i3) y:[21,18,25,14,52,65,40,43]$
(%i4) test_rank_sum(x,y);
              |                 RANK SUM TEST
              |
              |              method = Exact test
              |
              | hypotheses = H0: med1 = med2 , H1: med1 # med2
(%o4)         |
              |                 statistic = 22
              |
              |        distribution = [rank_sum, 9, 8]
              |
              |          p_value = .1995886466474702
```


Ahora, con muestras mayores y empates, el procedimiento
realiza la aproximación normal. La hipótesis
alternativa es $H_1: median1 < median2$.














```maxima
(%i1) load("stats")$
(%i2) x: [39,42,35,13,10,23,15,20,17,27]$
(%i3) y: [20,52,66,19,41,32,44,25,14,39,43,35,19,56,27,15]$
(%i4) test_rank_sum(x,y,'alternative='less);
             |                  RANK SUM TEST
             |
             |          method = Asymptotic test. Ties
             |
             |  hypotheses = H0: med1 = med2 , H1: med1 < med2
(%o4)        |
             |                 statistic = 48.5
             |
             | distribution = [normal, 79.5, 18.95419580097078]
             |
             |           p_value = .05096985666598441
```

<!-- category: Statistics -->
<!-- keywords: test_sign -->
<!-- signatures: test_sign(x), test_sign(x, options...) -->
### Function: test_sign (x)

Este es el test no paramétrico de los signos para contrastes
sobre la mediana de una población continua. El argumento *x*
es una lista o matriz columna que contiene los datos de una muestra
unidimensional.


Opciones:



- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'median`, valor por defecto `0`, es el valor de la mediana a contrastar.


El resultado devuelto por la función `test_sign` es un objeto
`inference_result` con los siguientes apartados:



1. `'med_estimate`: la mediana muestral.
2. `'method`: procedimiento de inferencia.
3. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
4. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
5. `'distribution`: distribución del estadístico de contraste, junto con sus parámetros.
6. `'p_value`: $p$-valor del test.


Ejemplos:


Contrasta si la mediana de la población de la que se ha extraido
la muestra es 6, frente a la alternativa $H_1: median > 6$.








```maxima
(%i1) load("stats")$
(%i2) x: [2,0.1,7,1.8,4,2.3,5.6,7.4,5.1,6.1,6]$
(%i3) test_sign(x,'median=6,'alternative='greater);
               |                  SIGN TEST
               |
               |              med_estimate = 5.1
               |
               |      method = Non parametric sign test.
               |
(%o3)          | hypotheses = H0: median = 6 , H1: median > 6
               |
               |                statistic = 7
               |
               |      distribution = [binomial, 10, 0.5]
               |
               |         p_value = .05468749999999989
```

<!-- category: Statistics -->
<!-- keywords: test_signed_rank -->
<!-- signatures: test_signed_rank(x), test_signed_rank(x, options...) -->
### Function: test_signed_rank (x)

Este el test de los rangos signados de Wilcoxon para hacer inferencias sobre
la mediana de una población continua. El argumento *x* es una lista
o matriz columna que contiene los datos de una muestra unidimensional.
Realiza la aproximación normal si el tamaño muestral es mayor que 20,
o si en la muestra aparece algún cero o hay empates.


Véanse también `pdf_rank_test` y `cdf_rank_test`.



Opciones:



- *
`'median`, valor por defecto `0`, es el valor de la mediana a ser contrastado.
- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.


El resultado devuelto por la función  `test_signed_rank` es
un objeto `inference_result` con los siguientes apartados:



1. `'med_estimate`: la mediana muestral.
2. `'method`: procedimiento de inferencia.
3. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
4. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
5. `'distribution`: distribución del estadístico de contraste, junto con su(s) parámetro(s).
6. `'p_value`: $p$-valor del test.


Ejemplos:


Contrasta la hipótesis nula $H_0: median = 15$ frente 
a la alternativa $H_1: median > 15$. Este test es exacto, 
puesto que no hay empates.













```maxima
(%i1) load("stats")$
(%i2) x: [17.1,15.9,13.7,13.4,15.5,17.6]$
(%i3) test_signed_rank(x,median=15,alternative=greater);
                 |             SIGNED RANK TEST
                 |
                 |           med_estimate = 15.7
                 |
                 |           method = Exact test
                 |
(%o3)            | hypotheses = H0: med = 15 , H1: med > 15
                 |
                 |              statistic = 14
                 |
                 |     distribution = [signed_rank, 6]
                 |
                 |            p_value = 0.28125
```


Contrasta la hipótesis nula $H_0: equal(median, 2.5)$ frente 
a la alternativa $H_1: not equal(median, 2.5)$. Este es un test asintótico,
debido a la presencia de empates.












```maxima
(%i1) load("stats")$
(%i2) y:[1.9,2.3,2.6,1.9,1.6,3.3,4.2,4,2.4,2.9,1.5,3,2.9,4.2,3.1]$
(%i3) test_signed_rank(y,median=2.5);
             |                 SIGNED RANK TEST
             |
             |                med_estimate = 2.9
             |
             |          method = Asymptotic test. Ties
             |
(%o3)        |    hypotheses = H0: med = 2.5 , H1: med # 2.5
             |
             |                 statistic = 76.5
             |
             | distribution = [normal, 60.5, 17.58195097251724]
             |
             |           p_value = .3628097734643669
```

<!-- category: Statistics -->
<!-- keywords: test_variance -->
<!-- signatures: test_variance(x), test_variance(x, options...) -->
### Function: test_variance (x)

Este es el test *chi^2* de la varianza. El argumento *x*
es una lista o matriz columna con los datos de una muestra unidimensional
extraída de una población normal.


Opciones:



- *
`'mean`, valor por defecto `'unknown`, es la media de la población, si se conoce.
- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'variance`, valor por defecto `1`, este es el valor (positivo) de la varianza a contrastar.
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el intervalo de confianza;
debe ser una expresión que tome un valor en el intervalo (0,1).


El resultado devuelto por la función  `test_variance` es un objeto
`inference_result` con los siguientes apartados:



1. `'var_estimate`: la varianza muestral.
2. `'conf_level`: nivel de confianza seleccionado por el usuario.
3. `'conf_interval`: intervalo de confianza para la varianza poblacional.
4. `'method`: procedimiento de inferencia.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con su parámetro.
8. `'p_value`: $p$-valor del test.


Ejemplos:


Se contrasta si la varianza de una población de media desconocida
es igual o mayor que 200.








```maxima
(%i1) load("stats")$
(%i2) x: [203,229,215,220,223,233,208,228,209]$
(%i3) test_variance(x,'alternative='greater,'variance=200);
             |                  VARIANCE TEST
             |
             |              var_estimate = 110.75
             |
             |                conf_level = 0.95
             |
             |     conf_interval = [57.13433376937479, inf]
             |
(%o3)        | method = Variance Chi-square test. Unknown mean.
             |
             |    hypotheses = H0: var = 200 , H1: var > 200
             |
             |                 statistic = 4.43
             |
             |             distribution = [chi2, 8]
             |
             |           p_value = .8163948512777689
```

<!-- category: Statistics -->
<!-- keywords: test_variance_ratio -->
<!-- signatures: test_variance_ratio(x1, x2), test_variance_ratio(x1, x2, options...) -->
### Function: test_variance_ratio (x1, x2)

Este es el test *F* del cociente de las varianzas para dos
poblaciones normales. Los argumentos *x1* y *x2* son listas
o matrices columna que contienen los datos de dos muestras 
independientes.


Opciones:



- *
`'alternative`, valor por defecto `'twosided`, es la hipótesis alternativa;
valores válidos son: `'twosided`, `'greater` y `'less`.
- *
`'mean1`, valor por defecto `'unknown`, es la media de la población de la
que procede *x1* cuando se conoce.
- *
`'mean2`, valor por defecto `'unknown`, es la media de la población de la
que procede *x2* cuando se conoce.
- *
`'conflevel`, valor por defecto `95/100`, nivel de confianza para el intervalo
de confianza del cociente; debe ser una expresión que tome un valor en el intervalo (0,1).


El resultado devuelto por la función  `test_variance_ratio` es un objeto
`inference_result` con los siguientes resultados



1. `'ratio_estimate`: el cociente de varianzas muestral.
2. `'conf_level`: nivel de confianza seleccionado por el usuario.
3. `'conf_interval`: intervalo de confianza para el cociente de varianzas.
4. `'method`: procedimiento de inferencia.
5. `'hypotheses`: hipótesis nula y alternativa a ser contrastada.
6. `'statistic`: valor del estadístico de contraste utilizado para probar la hipótesis.
7. `'distribution`: distribución del estadístico de contraste, junto con sus parámetros.
8. `'p_value`: $p$-valor del test.



Ejemplos:


Se contrasta la igualdad de varianzas de dos poblaciones normales frente
a la alternativa de que la primera es mayor que la segunda.














```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: [1.2,6.9,38.7,20.4,17.2]$
(%i4) test_variance_ratio(x,y,'alternative='greater);
              |              VARIANCE RATIO TEST
              |
              |       ratio_estimate = 2.316933391522034
              |
              |               conf_level = 0.95
              |
              |    conf_interval = [.3703504689507268, inf]
              |
(%o4)         | method = Variance ratio F-test. Unknown means.
              |
              | hypotheses = H0: var1 = var2 , H1: var1 > var2
              |
              |         statistic = 2.316933391522034
              |
              |            distribution = [f, 5, 4]
              |
              |          p_value = .2179269692254457
```

