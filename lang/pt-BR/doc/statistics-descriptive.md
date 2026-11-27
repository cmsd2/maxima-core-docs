## descriptive

<!-- category: Statistics -->
<!-- keywords: barsplot -->
<!-- signatures: barsplot(lista), barsplot(lista, opção_1, opção_2, ...), barsplot(one_column_matrix), barsplot(one_column_matrix, opção_1, opção_2, ...) -->
### Function: barsplot (lista)

Similar a `histogram` mas para variáveis estatísticas, numéricas ou divididas em categorias. As opções estão abaixo,



- *
`'outputdev`, o valor padrão é `"x"`, indica o formato de arquivo da figura de saída; valores corretos são `"x"`, `"eps"` e `"png"`, para a tela, formato de arquivo postscript e formato de arquivo png, respectivamente.
- *
`'maintitle`, o valor padrão é `""`, é o título principal entre aspas duplas.
- *
`'axisnames`, o valor padrão é `["x", "Fr."]`, é uma lista de nomes dos eixos `x` e `y`.
- *
`'picturescales`, o valor padrão é `[1.0, 1.0]`, fator de proporcionalidade para o tamanho do gráfico.
- *
`'relbarwidth`, o valor padrão é `0.9`, um número decimao entre 0 e 1 para controlar a largura das barras.
- *
`'barcolor`, o valor padrão é `1`, um inteiro para indicar a cor das barras.
- *
`'colorintensity`, o valor padrão é `1`, um número decimal entre 0 e 1 para estabelecer a intensidade da cor.


Esse exemplo monta um gráfico de barras para os grupos `A` e `B` de pacientes na amostra `s3`,










```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) barsplot (col (s3, 1), 'maintitle = "Grupos de pacientes",
 'axisnames = ["Grupo", "# de indivíduos"], 'colorintensity = 0.2)$
```

A primeira coluna na amostra `s3` armazena os valores das categorias `A` e `B`, também conhecidos algumas vezes como fatores. Por outro lado, os números inteiros positivos na segunda coluna sào idades, em anos, que se comportam como variável discreta, então podemos montar um gráfico as frequências absolutas para esses valores,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) barsplot (col (s3, 2), 'maintitle = "Idades",
 'axisnames = ["Anos", "# dos indivíduos"], 'colorintensity = 0.2,
 'relbarwidth = 0.6)$
```



Veja também a função `histogram`.

<!-- category: Statistics -->
<!-- keywords: boxplot -->
<!-- signatures: boxplot(data), boxplot(data, opção_1, opção_2, ...) -->
### Function: boxplot (data)

Essa função monta diagramas em caixas. O argumento *data* pode ser uma lista, que não é de grande interesse, uma vez que esses diagramas são principalmente usados para comparação entre diferentes amostras, ou uma matriz, eentão é possível comparar dois ou mais componentes de uma variável estatística de várias variáveis. Mas é também permitido *data* se uma lista de amostras com tamanhos diferentes de amostra, de fato essa é aa única função no pacote `descriptive` que admite esse tipo de estrutura de dados. Veja o exemplo abaixo.  Abaixo etão as opções,



- *
`'outputdev`, o valor padrão é `"x"`, indica o formato de arquivo da figura de saída; valores corretos são `"x"`, `"eps"` e `"png"`, para a tela, formato de arquivo postscript e formato de arquivo png, respectivamente.
- *
`'maintitle`, o valor padrão é `""`, é o título principal entre aspas duplas.
- *
`'axisnames`, o valor padrão é `["sample", "y"]`, é uma lista de nomes dos eixos `x` e `y`.
- *
`'picturescales`, o valor padrão é `[1.0, 1.0]`, fator de proporcionalidade para o tamanho do gráfico.


Examples:















```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) boxplot (s2, 'maintitle = "Velocidade do vento em nós",
 'axisnames = ["Estação do ano", ""])$
(%i5) A :
 [[6, 4, 6, 2, 4, 8, 6, 4, 6, 4, 3, 2],
  [8, 10, 7, 9, 12, 8, 10],
  [16, 13, 17, 12, 11, 18, 13, 18, 14, 12]]$
(%i6) boxplot (A)$
```

<!-- category: Statistics -->
<!-- keywords: central_moment -->
<!-- signatures: central_moment(lista, k), central_moment(matriz, k) -->
### Function: central_moment (lista, k)

O momento central de ordem $k$, definido como

$$
{{1\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^k}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) central_moment (s1, 2), numer; /* a variância */
(%o4)                   8.425899999999999
(%i6) s2 : read_matrix (file_search ("wind.data"))$
(%i7) central_moment (s2, 3);
(%o7) [11.29584771375004, 16.97988248298583, 5.626661952750102, 
                             37.5986572057918, 25.85981904394192]
```


Veja também as funções `central_moment` e `mean`.

<!-- category: Statistics -->
<!-- keywords: continuous_freq -->
<!-- signatures: continuous_freq(list), continuous_freq(list, m) -->
### Function: continuous_freq (list)

O argumetno de `continuous_freq` deve ser uma lista de números, que serão então agrupadas em intervalos e contado quantos desses dados pertencem a cada grupo. Opcionalmente, a função `continuous_freq` admite um segundo argumento indicando o número de classes, 10 é o valor padrão,









```maxima
(%i1) load ("numericalio")$
(%i2) load ("descriptive")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) continuous_freq (s1, 5);
(%o4) [[0, 1.8, 3.6, 5.4, 7.2, 9.0], [16, 24, 18, 17, 25]]
```


A primeira lista contém os limites de intervalos e o segundo a correspondente contagem: existem 16 algarismos da parte decimal de `%pi` dentro do intervalo `[0, 1.8]`, isto é 0’s e 1’s, 24 algarismos em `(1.8, 3.6]`, isto é 2’s e 3’s, e assim por diante.

<!-- category: Statistics -->
<!-- keywords: cor -->
<!-- signatures: cor(matriz), cor(matriz, valor_lógico) -->
### Function: cor (matriz)

A matriz de correlação da maostra de várias variáveis.


Exemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) fpprintprec:7$
(%i4) s2 : read_matrix (file_search ("wind.data"))$
(%i5) cor (s2);
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o5) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


A função `cor` tem um argumento lógico opcional: `cor(x,true)` diz ao Maxima que `x` é a matriz de dados, fazendo o mesmo que `cor(x)`. Por outro lado, `cor(x,false)` significa que `x` não é a matriz de dados, mas a matriz de covariância, evitando a repetição de seu cálculo,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) fpprintprec:7$
(%i4) s2 : read_matrix (file_search ("wind.data"))$
(%i5) s : cov1 (s2)$
(%i6) cor (s, false); /* this is faster */
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o6) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


Veja também `cov` e `cov1`.

<!-- category: Statistics -->
<!-- keywords: cov -->
<!-- signatures: cov(matriz) -->
### Function: cov (matriz)

A matriz de covariância da amostra de várias variáveis, definida como

$$
{S={1\over{n}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$

onde $X_j$ é a $j$-ésima linha da matriz de amostra.


Exemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) fpprintprec : 7$  /* modifique a precisão para obter uma saída melhor */
(%i5) cov (s2);
      [ 17.22191  13.61811  14.37217  19.39624  15.42162 ]
      [                                                  ]
      [ 13.61811  14.98774  13.30448  15.15834  14.9711  ]
      [                                                  ]
(%o5) [ 14.37217  13.30448  15.47573  17.32544  16.18171 ]
      [                                                  ]
      [ 19.39624  15.15834  17.32544  32.17651  20.44685 ]
      [                                                  ]
      [ 15.42162  14.9711   16.18171  20.44685  24.42308 ]
```


Veja também a função `cov1`.

<!-- category: Statistics -->
<!-- keywords: cov1 -->
<!-- signatures: cov1(matriz) -->
### Function: cov1 (matriz)

A matriz de covariância da amostra de várias variáveis, definida como

$$
{{1\over{n-1}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$

where $X_j$ is the $j$-th row of the sample matrix.


Exemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) fpprintprec : 7$ /* modifique a precisão para obter uma saída melhor */
(%i5) cov1 (s2);
      [ 17.39587  13.75567  14.51734  19.59216  15.5774  ]
      [                                                  ]
      [ 13.75567  15.13913  13.43887  15.31145  15.12232 ]
      [                                                  ]
(%o5) [ 14.51734  13.43887  15.63205  17.50044  16.34516 ]
      [                                                  ]
      [ 19.59216  15.31145  17.50044  32.50153  20.65338 ]
      [                                                  ]
      [ 15.5774   15.12232  16.34516  20.65338  24.66977 ]
```


Veja também a função `cov`.

<!-- category: Statistics -->
<!-- keywords: cv -->
<!-- signatures: cv(lista), cv(matriz) -->
### Function: cv (lista)

O coeficiente de variação é o quociente entre o desvio padrão da amostra (`std`) e a média `mean`,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) cv (s1), numer;
(%o4)                   .6193977819764815
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) cv (s2);
(%o6) [.4192426091090204, .3829365309260502, 0.363779605385983, 
                            .3627381836021478, .3346021393989506]
```


Veja também as funções `std` e `mean`.

<!-- category: Statistics -->
<!-- keywords: dataplot -->
<!-- signatures: dataplot(lista), dataplot(lista, opção_1, opção_2, ...), dataplot(matriz), dataplot(matriz, opção_1, opção_2, ...) -->
### Function: dataplot (lista)

A função `dataplot` permite visualização direta de dados de amostra, ambas d uma única variável (*lista*) e de várias variáveis (*matriz*). Fornecendo valores para as seguintes *opções* que são alguns aspéctos de impressão que podem ser controlados:



- *
`'outputdev`, o valor padrão é `"x"`, indica o formato de dispositivo/arquivo da figura de saída; valores corretos são `"x"`, `"eps"` e `"png"`, para a tela, formato de arquivo postscript e formato de arquivo png, respectivamente.
- *
`'maintitle`, o valor padrão é `""`, é o título principal entre aspas duplas.
- *
`'axisnames`, o valor padrão é `["x","y","z"]`, é uma lista de nomes dos eixos `x`, `y` e `z`.
- *
`'joined`, o valor padrão é `false`, um valor lógico para selecionar pontos em 2D para serem unidos ou isolados.
- *
`'picturescales`, o valor padrão é `[1.0, 1.0]`, fator de proporcionalidade para o tamanho do gráfico.
- *
`'threedim`, o valor padrão é `true`, diz ao Maxima se ou monta-se o gráfico de uma matriz de três colunas como um diagrama 3D ou se monta-se o gráfico como um diagrama de dispersão de várias variáveis. Veja exemplos abaixo.
- *
`'axisrot`, o valor padrão é `[60, 30]`, modifica o ponto de visualização quando `'threedim` for escolhido para `true` dados forem armazenados em uma matriz de três colunas. O primeiro número é o ângulo de rotação do eixo *x*, e o segundo número é o angulo de rotação do eixo *z*-axis, ambas as medidas em graus.
- *
`'nclasses`, o valor padrão é `10`, é o número de classes para histogramas na diagonal de gráficos de dispersão de várias variáveis.
- *
`'pointstyle`, o valor padrão é `1`, é um inteiro que indica como mostrar pontos de amostra.


Por exemplo, com a seguite entrada um gráfico simples dos primeiros vinte dígitos de `%pi` é requisitado e a saída é armazenada em um arquivo no formato eps.









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) dataplot (makelist (s1[k], k, 1, 20), 'pointstyle = 3)$
```


Note que dados unidimensionais são colocados no gráfico como uma série de tempo. No caso seguinte, ocorre a mesma coisa só que com mais dados e com mais configurações,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) dataplot (makelist (s1[k], k, 1, 50), 'maintitle = "Primeiros dígitos de pi",
 'axisnames = ["ordem do dígito", "valor do dígito"], 'pointstyle = 2,
 'joined = true)$
```


A função `dataplot` pode ser usada para montar gráficos de pontos no plano. O exemplo seguinte é gráfico de dispersão de pares de pontos de velocidades de vento para o primeira e para o quinta estação meteorológica,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) dataplot (submatrix (s2, 2, 3, 4), 'pointstyle = 2,
 'maintitle = "Pares de medidas de velocidade do vento em nós",
 'axisnames = ["Velocidade do vento em A", "Velocidade do vento em E"])$
```


Se pontos forem armazenados em uma matriz de duas colunas, `dataplot` pode montar o gráfico desses pontos diretamente, mas se eles forem formatados em uma lista de pares, essa lista deve ser transformada em uma matriz como no seguinte exemplo.









```maxima
(%i1) load ("descriptive")$
(%i2) x : [[-1, 2], [5, 7], [5, -3], [-6, -9], [-4, 6]]$
(%i3) dataplot (apply ('matrix, x), 'maintitle = "Pontos",
 'joined = true, 'axisnames = ["", ""], 'picturescales = [0.5, 1.0])$
```


Pontos no espaço tridimensional podem ser vistos como uma projeção no plano. Nesse exemplo, o gráfico de velocidades do vento correspondendo a três estações meteorológicas são requisitados, primeiramente em um gráfico em 3D e a seguir em um gráfico de dispersão de várias variáveis.













```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) /* 3D plot */ dataplot (submatrix (s2, 4, 5), 'pointstyle = 2,
 'maintitle = "Pares de medidas de velocidades do vento em nós",
 'axisnames = ["Estação A", "Estação B", "Estação C"])$
(%i5) /* Gráfico de dispersão de várias variáveis */ dataplot (submatrix (s2, 4, 5),
 'nclasses = 6, 'threedim = false)$
```

Note que no último exemplo, o número de classes no histogramas da diagonal é escolhido para 6, e aquela opção `'threedim` for escolhida para `false`.


Para mais que três dimensões somente gráficos de dispersão de várias variáveis são possível, como em









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) dataplot (s2)$
```

<!-- category: Statistics -->
<!-- keywords: discrete_freq -->
<!-- signatures: discrete_freq(list) -->
### Function: discrete_freq (list)

Conta as frequências absolutas em amostras discretas, em amostras numéricas e em amostras divididas em categorias. Seu único argumento é uma lista,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"));
(%o3) [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 
4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 
1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 
5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 
6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7]
(%i4) discrete_freq (s1);
(%o4) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```


A primeira lista fornece os valores da amostra e a segunda seuas frequências absolutas. Os comandos `? col` e `? transpose` podem ajudar a você a entender a última entrada.

<!-- category: Statistics -->
<!-- keywords: geometric_mean -->
<!-- signatures: geometric_mean(lista), geometric_mean(matriz) -->
### Function: geometric_mean (lista)

A média geométrica, definida como

$$
\left(\prod_{i=1}^{n}{x_{i}}\right)^{{{1}\over{n}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$
(%i4) geometric_mean (y), numer;
(%o4)                   4.454845412337012
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) geometric_mean (s2);
(%o6) [8.82476274347979, 9.22652604739361, 10.0442675714889, 
                            14.61274126349021, 13.96184163444275]
```


Veja também as funções `mean` e `harmonic_mean`.

<!-- category: Statistics -->
<!-- keywords: global_variances -->
<!-- signatures: global_variances(matriz), global_variances(matriz, valor_lógico) -->
### Function: global_variances (matriz)

A função `global_variances` retorna uma lista de medidas de variância global:



- *
*variância total*: `trace(S_1)`,
- *
*variância média*: `trace(S_1)/p`,
- *
*variância generalizada*: `determinant(S_1)`,
- *
*desvio padrão generalizado*: `sqrt(determinant(S_1))`,
- *
*variância efetiva* `determinant(S_1)^(1/p)`, (defined in: Peña, D. (2002) *Análisis de datos multivariantes*; McGraw-Hill, Madrid.)
- *
*desvio padrão efetivo*: `determinant(S_1)^(1/(2*p))`.

onde *p* é a dimensão das várias variáveis aleatórias e $S_1$ a matriz de covariância retornada por `cov1`.


Exemplo:









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) global_variances (s2);
(%o4) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608502, 6.636590811800794, 2.576158149609762]
```


A função `global_variances` tem um argumento lógico opcional: `global_variances(x,true)` diz ao Maxima que `x` é a matriz de dados, fazendo o mesmo que `global_variances(x)`. Por outro lado, `global_variances(x,false)` significa que `x` não é a matriz de dados, mas a matriz de covariância, evitando a repetição seu cálculo,










```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) s : cov1 (s2)$
(%i5) global_variances (s, false);
(%o5) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608502, 6.636590811800794, 2.576158149609762]
```


Veja também `cov` e `cov1`.

<!-- category: Statistics -->
<!-- keywords: harmonic_mean -->
<!-- signatures: harmonic_mean(lista), harmonic_mean(matriz) -->
### Function: harmonic_mean (lista)

A média harmônica, definida como

$$
{{n}\over{\sum_{i=1}^{n}{{{1}\over{x_{i}}}}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$
(%i4) harmonic_mean (y), numer;
(%o4)                   3.901858027632205
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) harmonic_mean (s2);
(%o6) [6.948015590052786, 7.391967752360356, 9.055658197151745, 
                            13.44199028193692, 13.01439145898509]
```


Veja também as funções `mean` e `geometric_mean`.

<!-- category: Statistics -->
<!-- keywords: histogram -->
<!-- signatures: histogram(lista), histogram(lista, opção_1, opção_2, ...), histogram(one_column_matrix), histogram(one_column_matrix, opção_1, opção_2, ...) -->
### Function: histogram (lista)

Essa função monta um gráfico de um histograma. Dados de amostras devem ser armazenados em uma lista de números ou em uma matriz de uma coluna. Fornecendo valores para as seguintes *opções* alguns aspéctos do gráfico podem ser controlados:



- *
`'outputdev`, o valor padrão é `"x"`, indica o formato de arquivo da figura de saída; valores corretos são `"x"`, `"eps"` e `"png"`, para a tela, formato de arquivo postscript e formato de arquivo png, respectivamente.
- *
`'maintitle`, o valor padrão é `""`, é o título principal entre aspas duplas.
- *
`'axisnames`, o valor padrão é `["x", "Fr."]`, é uma lista de nomes dos eixos `x` e `y`.
- *
`'picturescales`, o valor padrão é `[1.0, 1.0]`, fator de proporcionalidade para o tamanho do gráfico.
- *
`'nclasses`, o valor padrão é `10`, é o número de classes ou o número de barras.
- *
`'relbarwidth`, o valor padrão é `0.9`, um número decimao entre 0 e 1 para controlar a largura das barras.
- *
`'barcolor`, o valor padrão é `1`, um inteiro para indicar a cor das barras.
- *
`'colorintensity`, o valor padrão é `1`, um número decimal entre 0 e 1 para estabelecer a intensidade da cor.


Nos próximos dois exemplos, histogramas são requisitados para os primeiros 100 dígitos do número `%pi` e para velocidades do vento na terceira estação meteorológica.












```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) histogram (s1, 'maintitle = "dígitos de pi", 'axisnames = ["", "Frequência absoluta"],
 'relbarwidth = 0.2, 'barcolor = 3, 'colorintensity = 0.6)$
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) histogram (col (s2, 3), 'colorintensity = 0.3)$
```

Note tque no primeiro caso, `s1` é uma lista  e o segundo exemplo, `col(s2,3)` é uma matriz.


Veja também a função `barsplot`.

<!-- category: Statistics -->
<!-- keywords: kurtosis -->
<!-- signatures: kurtosis(lista), kurtosis(matriz) -->
### Function: kurtosis (lista)

O coeficiente de curtose, definido como

$$
{{1\over{n s^4}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^4}}-3}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) kurtosis (s1), numer;
(%o4)                  - 1.273247946514421
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) kurtosis (s2);
(%o6) [- .2715445622195385, 0.119998784429451, 
   - .4275233490482866, - .6405361979019522, - .4952382132352935]
```


Veja também as funções `mean`, `var` e `skewness`.

<!-- category: Statistics -->
<!-- keywords: list_correlations -->
<!-- signatures: list_correlations(matriz), list_correlations(matriz, valor_lógico) -->
### Function: list_correlations (matriz)

A função `list_correlations` retorna uma lista de medidas de correlação:



- *
*matriz de precisão*: o inverso da matriz de covariância $S_1$,
$$
{S_{1}^{-1}}={\left(s^{ij}\right)_{i,j=1,2,\ldots, p}}
$$
- *
*vetor de correlação multipla*:  $(R_1^2, R_2^2, ..., R_p^2)$, com 
$$
{R_{i}^{2}}={1-{{1}\over{s^{ii}s_{ii}}}}
$$
sendo um indicador do melhor do ajuste do modelo de regressão linear de várias variáveis dobre $X_i$ quando o resto das variáveis são usados como regressores.
- *
*matriz de correlação parcial*: como elemento $(i, j)$ sendo
$$
{r_{ij.rest}}={-{{s^{ij}}\over \sqrt{s^{ii}s^{jj}}}}
$$


Exemplo:













```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) z : list_correlations (s2)$
(%i5) fpprintprec : 5$ /* for pretty output */
(%i6) z[1];  /* precision matrix */
      [  .38486   - .13856   - .15626   - .10239    .031179  ]
      [                                                      ]
      [ - .13856   .34107    - .15233    .038447   - .052842 ]
      [                                                      ]
(%o6) [ - .15626  - .15233    .47296    - .024816  - .10054  ]
      [                                                      ]
      [ - .10239   .038447   - .024816   .10937    - .034033 ]
      [                                                      ]
      [ .031179   - .052842  - .10054   - .034033   .14834   ]
(%i7) z[2];  /* multiple correlation vector */
(%o7)       [.85063, .80634, .86474, .71867, .72675]
(%i8) z[3];  /* partial correlation matrix */
       [  - 1.0     .38244   .36627   .49908   - .13049 ]
       [                                                ]
       [  .38244    - 1.0    .37927  - .19907   .23492  ]
       [                                                ]
(%o8)  [  .36627    .37927   - 1.0    .10911    .37956  ]
       [                                                ]
       [  .49908   - .19907  .10911   - 1.0     .26719  ]
       [                                                ]
       [ - .13049   .23492   .37956   .26719    - 1.0   ]
```


A função `list_correlations` também tem um argumento lógico opcional: `list_correlations(x,true)` diz ao Maxima que `x` é a matriz de dados, fazendo o mesmo que `list_correlations(x)`. Por outro lado, `list_correlations(x,false)` significa que `x` não é a matriz de correlação, mas a matriz de covariancia, evitando a repetição de seu cálculo.


Veja também `cov` e `cov1`.

<!-- category: Statistics -->
<!-- keywords: maxi -->
<!-- signatures: maxi(lista), maxi(matriz) -->
### Function: maxi (lista)

É o valor máximo da amostra *lista*,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) maxi (s1);
(%o4)                           9
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) maxi (s2);
(%o6)          [20.25, 21.46, 20.04, 29.63, 27.63]
```


Veja também a função `mini`.

<!-- category: Statistics -->
<!-- keywords: mean -->
<!-- signatures: mean(lista), mean(matriz) -->
### Function: mean (lista)

Essa função calcula a média de uma amostra, definida como

$$
{\bar{x}={1\over{n}}{\sum_{i=1}^{n}{x_{i}}}}
$$



Exemplo:












```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) mean (s1);
                               471
(%o4)                          ---
                               100
(%i5) %, numer;
(%o5)                         4.71
(%i6) s2 : read_matrix (file_search ("wind.data"))$
(%i7) mean (s2);
(%o7)     [9.9485, 10.1607, 10.8685, 15.7166, 14.8441]
```

<!-- category: Statistics -->
<!-- keywords: mean_deviation -->
<!-- signatures: mean_deviation(lista), mean_deviation(matriz) -->
### Function: mean_deviation (lista)

O desvio médio, definido como

$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-\bar{x}|}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) mean_deviation (s1);
                               51
(%o4)                          --
                               20
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) mean_deviation (s2);
(%o6) [3.287959999999999, 3.075342, 3.23907, 4.715664000000001, 
                                               4.028546000000002]
```


Veja também a função `mean`.

<!-- category: Statistics -->
<!-- keywords: median -->
<!-- signatures: median(lista), median(matriz) -->
### Function: median (lista)

Uma vez que a amostra está ordenada, se o tamanho da amostra for ímpar a mediana é o valor central, de outra forma a mediana será a média dos dois valores centrais.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) median (s1);
                                9
(%o4)                           -
                                2
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) median (s2);
(%o6)         [10.06, 9.855, 10.73, 15.48, 14.105]
```


A mediana é o 1/2-`quantil`.


Veja também function `quantile`.

<!-- category: Statistics -->
<!-- keywords: median_deviation -->
<!-- signatures: median_deviation(lista), median_deviation(matriz) -->
### Function: median_deviation (lista)

O desvio da mediana, definido como

$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-med|}}}
$$

onde `med` é a mediana da *lista*.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) median_deviation (s1);
                                5
(%o4)                           -
                                2
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) median_deviation (s2);
(%o6)           [2.75, 2.755, 3.08, 4.315, 3.31]
```


Veja também a função `mean`.

<!-- category: Statistics -->
<!-- keywords: mini -->
<!-- signatures: mini(lista), mini(matriz) -->
### Function: mini (lista)

É o valor mínimo da amostra *lista*,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) mini (s1);
(%o4)                           0
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) mini (s2);
(%o6)             [0.58, 0.5, 2.67, 5.25, 5.17]
```


Veja também função `maxi`.

<!-- category: Statistics -->
<!-- keywords: noncentral_moment -->
<!-- signatures: noncentral_moment(lista, k), noncentral_moment(matriz, k) -->
### Function: noncentral_moment (lista, k)

O momento não central de ordem $k$, definido como

$$
{{1\over{n}}{\sum_{i=1}^{n}{x_{i}^k}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) noncentral_moment (s1, 1), numer; /* the mean */
(%o4)                         4.71
(%i6) s2 : read_matrix (file_search ("wind.data"))$
(%i7) noncentral_moment (s2, 5);
(%o7) [319793.8724761506, 320532.1923892463, 391249.5621381556, 
                            2502278.205988911, 1691881.797742255]
```


Veja também a função `central_moment`.

<!-- category: Statistics -->
<!-- keywords: pearson_skewness -->
<!-- signatures: pearson_skewness(lista), pearson_skewness(matriz) -->
### Function: pearson_skewness (lista)

O coeficiente de assimetria de pearson, definido como 

$$
{{3\,\left(\bar{x}-med\right)}\over{s}}
$$

onde *med* é a mediana de *lista*.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) pearson_skewness (s1), numer;
(%o4)                   .2159484029093895
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) pearson_skewness (s2);
(%o6) [- .08019976629211892, .2357036272952649, 
         .1050904062491204, .1245042340592368, .4464181795804519]
```


Veja também as funções `mean`, `var` e `median`.

<!-- category: Statistics -->
<!-- keywords: qrange -->
<!-- signatures: qrange(lista), qrange(matriz) -->
### Function: qrange (lista)

A amplitude do interquartil é a diferença entre o terceiro e o primeiro quartil, `quantile(lista,3/4) - quantile(lista,1/4)`,











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) qrange (s1);
                               21
(%o4)                          --
                               4
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) qrange (s2);
(%o6) [5.385, 5.572499999999998, 6.0225, 8.729999999999999, 
                                               6.650000000000002]
```


Veja também a função `quantile`.

<!-- category: Statistics -->
<!-- keywords: quantile -->
<!-- signatures: quantile(lista, p), quantile(matriz, p) -->
### Function: quantile (lista, p)

É o *p*-`quantile` (quantil de ordem *p*), com *p* sendo um número em $[0, 1]$ (intervalo fechado), da amostra *lista*.
Embora exista muitas definições para quantil de uma amostra (Hyndman, R. J., Fan, Y. (1996) *Sample quantiles in statistical packages*. American Statistician, 50, 361-365), aquela que se baseia em interpolação linear é a que foi implementada no pacote `descriptive`.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) /* 1st and 3rd quartiles */ [quantile (s1, 1/4), quantile (s1, 3/4)], numer;
(%o4)                      [2.0, 7.25]
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) quantile (s2, 1/4);
(%o6)    [7.2575, 7.477500000000001, 7.82, 11.28, 11.48]
```

<!-- category: Statistics -->
<!-- keywords: quartile_skewness -->
<!-- signatures: quartile_skewness(lista), quartile_skewness(matriz) -->
### Function: quartile_skewness (lista)

O coeficiented de assimetria do quartil, definido como 

$$
{{c_{{{3}\over{4}}}-2\,c_{{{1}\over{2}}}+c_{{{1}\over{4}}}}\over{c
 _{{{3}\over{4}}}-c_{{{1}\over{4}}}}}
$$

onde $c_p$ é o quartil de ordem *p* da amostra *lista*.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) quartile_skewness (s1), numer;
(%o4)                  .04761904761904762
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) quartile_skewness (s2);
(%o6) [- 0.0408542246982353, .1467025572005382, 
       0.0336239103362392, .03780068728522298, 0.210526315789474]
```


Veja também a função `quantile`.

<!-- category: Statistics -->
<!-- keywords: range -->
<!-- signatures: range(lista), range(matriz) -->
### Function: range (lista)

A amplitude é a diferença entre os valores de maximo e de mínimo.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) range (s1);
(%o4)                           9
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) range (s2);
(%o6)          [19.67, 20.96, 17.37, 24.38, 22.46]
```

<!-- category: Statistics -->
<!-- keywords: skewness -->
<!-- signatures: skewness(lista), skewness(matriz) -->
### Function: skewness (lista)

O coeficiente de assimetria, definido como

$$
{{1\over{n s^3}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^3}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) skewness (s1), numer;
(%o4)                  .009196180476450306
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) skewness (s2);
(%o6) [.1580509020000979, .2926379232061854, .09242174416107717, 
                            .2059984348148687, .2142520248890832]
```


Veja também as funções `mean`, `var` e `kurtosis`.

<!-- category: Statistics -->
<!-- keywords: std -->
<!-- signatures: std(lista), std(matriz) -->
### Function: std (lista)

A raíz quadrada da função `var`, a variância com denominador $n$.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) std (s1), numer;
(%o4)                   2.902740084816414
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) std (s2);
(%o6) [4.149928523480858, 3.871399812729241, 3.933920277534866, 
                            5.672434260526957, 4.941970881136392]
```


Veja também as funções `var` e `std1`.

<!-- category: Statistics -->
<!-- keywords: std1 -->
<!-- signatures: std1(lista), std1(matriz) -->
### Function: std1 (lista)

É a raíz quadrada da função `var1`, a variância com denominador $n-1$.


Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) std1 (s1), numer;
(%o4)                   2.917363553109228
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) std1 (s2);
(%o6) [4.17083509672109, 3.89090320978032, 3.953738641137555, 
                            5.701010936401517, 4.966867617451963]
```


Veja também as funções `var1` e `std`.

<!-- category: Statistics -->
<!-- keywords: subsample -->
<!-- signatures: subsample(matriz_de_dados, expressão_lógica), subsample(matriz_de_dados, expressão_lógica, col_num, col_num, ...) -->
### Function: subsample (matriz_de_dados, expressão_lógica)

Essas funções são um tipo de variação da função `submatrix` do Maxima. O primeiro argumento é o nome da matriz de dados, o segundo argumento é uma expressão lógica que recebeu apóstrofo e os argumentos opcionais adicionais são o número de colunas a serem tomadas. Esse comportamento é melhor entendido com exemplos,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) subsample (s2, '(%c[1] > 18));
              [ 19.38  15.37  15.12  23.09  25.25 ]
              [                                   ]
              [ 18.29  18.66  19.08  26.08  27.63 ]
(%o4)         [                                   ]
              [ 20.25  21.46  19.95  27.71  23.38 ]
              [                                   ]
              [ 18.79  18.96  14.46  26.38  21.84 ]
```


Existem registros de várias variáveis nos quais a velocidade do vento na primeira estação meteorológica foram maiores que 18. Veja que na expressão lógica que recebeu apóstrofo o *i*-ésimo componente é referenciado como `%c[i]`. O símbolo `%c[i]` é usado dentro da função `subsample`, portanto quando usado como uma variável de uma categoria, Maxima fica confuso. No seguinte exemplo, requisitamos somente o primeiro, o segundo e o quinto componentes desses registro com velocidades de vento maiores que ou igual a 16 nós na estação meteorológica número 1 e menor que 25 nós na estação meteorológica número 4,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) subsample (s2, '(%c[1] >= 16 and %c[4] < 25), 1, 2, 5);
                     [ 19.38  15.37  25.25 ]
                     [                     ]
                     [ 17.33  14.67  19.58 ]
(%o4)                [                     ]
                     [ 16.92  13.21  21.21 ]
                     [                     ]
                     [ 17.25  18.46  23.87 ]
```


Aqui está um exemplo com as variáveis divididas em categorias do arquivo `biomed.data`. Queremos os registros correspondentes a aqueles pacientes no grupo `B` que possuem idade maior que 38 anos,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) subsample (s3, '(%c[1] = B and %c[2] > 38));
                [ B  39  28.0  102.3  17.1  146 ]
                [                               ]
                [ B  39  21.0  92.4   10.3  197 ]
                [                               ]
                [ B  39  23.0  111.5  10.0  133 ]
                [                               ]
                [ B  39  26.0  92.6   12.3  196 ]
(%o4)           [                               ]
                [ B  39  25.0  98.7   10.0  174 ]
                [                               ]
                [ B  39  21.0  93.2   5.9   181 ]
                [                               ]
                [ B  39  18.0  95.0   11.3  66  ]
                [                               ]
                [ B  39  39.0  88.5   7.6   168 ]
```



Probavelmente, a análise estatística irá envolver somente as medidas sanguíneas,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) subsample (s3, '(%c[1] = B and %c[2] > 38), 3, 4, 5, 6);
                   [ 28.0  102.3  17.1  146 ]
                   [                        ]
                   [ 21.0  92.4   10.3  197 ]
                   [                        ]
                   [ 23.0  111.5  10.0  133 ]
                   [                        ]
                   [ 26.0  92.6   12.3  196 ]
(%o4)              [                        ]
                   [ 25.0  98.7   10.0  174 ]
                   [                        ]
                   [ 21.0  93.2   5.9   181 ]
                   [                        ]
                   [ 18.0  95.0   11.3  66  ]
                   [                        ]
                   [ 39.0  88.5   7.6   168 ]
```



Essa é a média de várias variáveis de `s3`,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) mean (s3);
       65 B + 35 A  317          6 NA + 8145.0
(%o4) [-----------, ---, 87.178, -------------, 18.123, 
           100      10                100
                                                    3 NA + 19587
                                                    ------------]
                                                        100
```

Aqui, a primeira componente é sem sentido, uma vez que `A` e `B` são categorias, o segundo componente é a idade média dos indivíduos na forma racional, e o quarto eo último valores exibem um comportamento estranho. Isso ocorre porque o símbolo `NA` é usado aqui para indicar dado não disponível (*non available* em inglês), e as duas médias são certamente sem sentido. Uma solução possível pode ser jogar fora a matriz cujas linhas possuam símbolos `NA`, embora isso cause alguma perda de informação,









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s3 : read_matrix (file_search ("biomed.data"))$
(%i4) mean (subsample (s3, '(%c[4] # NA and %c[6] # NA), 3, 4, 5, 6));
(%o4) [79.4923076923077, 86.2032967032967, 16.93186813186813, 
                                                            2514
                                                            ----]
                                                             13
```

<!-- category: Statistics -->
<!-- keywords: var -->
<!-- signatures: var(list), var(matrix) -->
### Function: var (list)

This is the sample variance, defined as

$$
{{1}\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}
$$



Exemplo:









```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) var (s1), numer;
(%o4)                   8.425899999999999
```


See also function `var1`.

<!-- category: Statistics -->
<!-- keywords: var1 -->
<!-- signatures: var1(lista), var1(matriz) -->
### Function: var1 (lista)

Essa função calcula a variância da amostra, definida como

$$
{{1\over{n-1}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}}
$$



Exemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) load ("numericalio")$
(%i3) s1 : read_list (file_search ("pidigits.data"))$
(%i4) var1 (s1), numer;
(%o4)                    8.5110101010101
(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%i6) var1 (s2);
(%o6) [17.39586540404041, 15.13912778787879, 15.63204924242424, 
                            32.50152569696971, 24.66977392929294]
```


See also function `var`.

