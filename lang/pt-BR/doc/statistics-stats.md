## stats

<!-- category: Statistics -->
<!-- keywords: cdf_rank_sum -->
<!-- signatures: cdf_rank_sum(x, n, m) -->
### Function: cdf_rank_sum (x, n, m)

Função de densidade cumulativa da distribuição exata da
estatística do somatório do rank. O argumento *x* é um número
real e *n* e *m* são ambos inteiro positivos. 


Veja também `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: cdf_signed_rank -->
<!-- signatures: cdf_signed_rank(x, n) -->
### Function: cdf_signed_rank (x, n)

Função de densidade cumulativa da distribuição exata da
estatística do rank sinalizado. O argumento *x* é um número
real e *n* um inteiro positivo. 


Veja também `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: inference_result -->
<!-- signatures: inference_result(título, valores, números) -->
### Function: inference_result (título, valores, números)

Constrói um objeto `inference_result` do tipo retornado pelas
funções stats. O argumento *título* é uma
sequência de caracteres do Maxima co o nome do procedimento; *valores* é uma lissta com
elementos da forma `símbolo = valor` e *números* é uma lista
com números inteiros positivos no intervalo de um para `length(valores)`,
indicando que valores serão mostrados por padrão.


Exemplo:


Este é um exemplo que mostras os resultados associados a um retángulo. O
título deste objeto é a sequência de caraceteres `"Retângulo"`, o qual armazena cinco resultados, a saber
`'base`, `'altura`, `'diagonal`, `'área`,
e `'perímetro`, porém só mostra o primeiro, segundo, quinto e quarto
resultado. O resultado `'diagonal` também é armazenado neste objeto, no entanto não é
mostrado por padrão; para se ter acesso a este valor, faz-se uso da função `take_inference`.















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) inference_result("Retângulo",
                        ['base=b,
                         'altura=h,
                         'diagonal=sqrt(b^2+h^2),
                         'área=b*h,
                         'perímetro=2*(b+h)],
                        [1,2,5,4] );
                        |   Retângulo
                        |
                        |    base = 3
                        |
(%o3)                   |   altura = 2
                        |
                        | perímetro = 10
                        |
                        |    area = 6
(%i4) take_inference('diagonal,%);
(%o4)                        sqrt(13)
```


Veja também `take_inference`.

<!-- category: Statistics -->
<!-- keywords: inferencep -->
<!-- signatures: inferencep(obj) -->
### Function: inferencep (obj)

Retorna `true` ou `false`, dependendo se *obj* é
um objeto `inference_result` ou não.

<!-- category: Statistics -->
<!-- keywords: items_inference -->
<!-- signatures: items_inference(obj) -->
### Function: items_inference (obj)

Retorna uma lista com os nomes dos itens em *obj*, que devem
ser um objeto `inference_result`.


Exemplo:


O objeto `inference_result` armazena dois valores, a saber `'pi` e `'e`,
mas somente o segundo é mostrado. A função `items_inference` retorna os nomes
de todos os itens, não importa se eles são ou não mostrados.








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
<!-- keywords: pdf_rank_sum -->
<!-- signatures: pdf_rank_sum(x, n, m) -->
### Function: pdf_rank_sum (x, n, m)

Função densidade de probabilidade da distribuição exata da
estatística do somatório do rank. O argumento *x* é um número
real e *n* e *m* são ambos inteiros positivos. 


Veja também `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: pdf_signed_rank -->
<!-- signatures: pdf_signed_rank(x, n) -->
### Function: pdf_signed_rank (x, n)

Função densidade de probabilidade da distribuição exata da
estatística do rank sinalizado. O argumento *x* é um número
real e *n* um inteiro positivo.


Veja também `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: simple_linear_regression -->
<!-- signatures: simple_linear_regression(x), simple_linear_regression(xopção_1) -->
### Function: simple_linear_regression (x)

Regressão linear simples, $y_i=a+b x_i+e_i$, onde os $e_i$ são $N(0,sigma)$
variáveis aleatórias independentes. O argumento *x* deve ser uma matriz de duas colunas ou uma lista de
pares.


Opções:



- *
`'conflevel`, o valor padrão é `95/100`, nível de confidência para o intervalo de confidência; isso deve
ser uma expressão que tome valores em (0,1).
- *
`'regressor`, o valor padrão é `'x`, nome da variável independente.


A saída da função `simple_linear_regression` é um objeto `inference_result` do Maxima
com os seguintes resultados:



1. `'model`: a equação ajustada. Útil para fazer novas previsões. Veja exemplos abaixo.
2. `'means`: média de duas variáveis pseudo-aleatórias.
3. `'variances`: variâncias de ambas as variáveis.
4. `'correlation`: coeficiente de correlação.
5. `'adc`: coeficiente de determinação ajustado.
6. `'a_estimation`: estimador do parâmetro *a*.
7. `'a_conf_int`: intervalo de confidência do parâmetro *a*.
8. `'b_estimation`: estimador do parâmetro *b*.
9. `'b_conf_int`: intervalo de confidência do parâmetro *b*.
10. `'hypotheses`: a hipótese do nulo e a hipótese alternativa sobre o parâmetro *b*.
11. `'statistic`: valor da amostra estatística usado para testar a hipótese do nulo.
12. `'distribution`: distribuição da amostra estatística, juntamente com seu parâmetro.
13. `'p_value`: o valor de $p$ do teste sobre *b*.
14. `'v_estimation`: estimador de variância imparcial, ou variância residual.
15. `'v_conf_int`: intervalo de confidência da variância.
16. `'cond_mean_conf_int`: intervalo de confidência paa a média condicionada. Veja exemplos abaixo.
17. `'new_pred_conf_int`: intervalo de confidência para uma nova previsão. Veja exemplos abaixo.
18. `'residuals`: lista de pares (previsão, resíduo), ordenados em relação às previsões.
Útil para achar o melhor da análise de ajuste. Veja exemplos abaixo.


Somente os itens 1, 4, 14, 9, 10, 11, 12, e 13 acima, nessa ordem, são mostrados por padrão. Os restantes
escondem-se até que o usuário faça uso de funções `items_inference` e `take_inference`.


Exemplo:


Ajustando um modelo linear para uma amostras de duas variáveis. A entrada `%i4` monta p gráfico
da amostra junto com a linha de regressão; a entrada `%i5`
calcula `y` dado `x=113`; a média e o 
intervalo de confidência para uma nova previsão quando `x=113` são também calculados.














```maxima
(%i1) load("stats")$
(%i2) s:[[125,140.7],[130,155.1],[135,160.3],[140,167.2],[145,169.8]]$
(%i3) z:simple_linear_regression(s,conflevel=0.99);
           |               SIMPLE LINEAR REGRESSION
           |
           |   model = 1.405999999999985 x - 31.18999999999804
           |
           |           correlation = .9611685255255155
           |
           |           v_estimation = 13.57966666666665
           |
(%o3)      | b_conf_int = [.04469633662525263, 2.767303663374718]
           |
           |          hypotheses = H0: b = 0 ,H1: b # 0
           |
           |            statistic = 6.032686683658114
           |
           |            distribution = [student_t, 3]
           |
           |             p_value = 0.0038059549413203
(%i4) plot2d([[discrete, s], take_inference(model,z)],
              [x,120,150],
              [gnuplot_curve_styles, ["with points","with lines"]] )$
(%i5) take_inference(model,z), x=133;
(%o5)                         155.808
(%i6) take_inference(means,z);
(%o6)                     [135.0, 158.62]
(%i7) take_inference(new_pred_conf_int,z), x=133;
(%o7)              [132.0728595995113, 179.5431404004887]
```

<!-- category: Statistics -->
<!-- keywords: stats_numer -->
<!-- signatures: stats_numer -->
### Variable: stats_numer

Valor padrão: `true`


Se `stats_numer` for `true`, funções de inferência estatística 
retornam seus resultados em números com ponto flutuante. Se `stats_numer` for `false`,
resultados são fornecidos em formato simbólico e racional.

<!-- category: Statistics -->
<!-- keywords: take_inference -->
<!-- signatures: take_inference(n, obj), take_inference(nome, obj), take_inference(lista, obj) -->
### Function: take_inference (n, obj)

Retorna o *n*-ésimo valor armazenado em *obj* se *n* for um inteiro positivo,
ou o item chamado *nome* se esse for o nome de um item. Se o primeiro
argumento for uma lista de números e/ou símbolos, a função `take_inference` retorna
uma lista com os resultados correspondentes.


Exemplo:


Fornece um objeto `inference_result`, a função `take_inference` é
chamada com o objetivo de extrair alguma informação armazenada nesse objeto.


















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) sol: inference_result("Retângulo",
                            ['base=b,
                             'altura=h,
                             'diagonal=sqrt(b^2+h^2),
                             'area=b*h,
                             'perímetro=2*(b+h)],
                            [1,2,5,4] );
                        |   Retângulo
                        |
                        |    base = 3
                        |
(%o3)                   |   altura = 2
                        |
                        | perímetro = 10
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


Veja também `inference_result` e `take_inference`.

<!-- category: Statistics -->
<!-- keywords: test_mean -->
<!-- signatures: test_mean(x), test_mean(x, opção_1, opção_2, ...) -->
### Function: test_mean (x)

Esse é o teste-*t* de média. O argumento *x* é uma lista ou uma matriz coluna
contendo uma amostra unidimensional. `test_mean` tamb;em executa um teste assintótico
baseado no *Teorema do Limite Central* se a opção `'asymptotic` for
`true`.


Opções:



- *
`'mean`, o valor padrão é `0`, é o valor da média a ser verificado.
- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.
- *
`'dev`, o valor padrão é `'unknown`, corresponde ao valor do desvio padrão quando esse valor de desvio padrão for
conhecido; valores válidos são: `'unknown` ou uma expressão positiva.
- *
`'conflevel`, o valor padrão é `95/100`, nível de confidência para o intervalo de confidência; deve
ser uma expressão que toma um valor em (0,1).
- *
`'asymptotic`, o valor padrão é `false`, indica se `test_mean` exeecuta um teste-*t* exato ou
um teste assintótico baseando-se no *Teorema do Limite Central*;
valores válidos são `true` e `false`.


A saída da função `test_mean` é um objeto `inference_result` do Maxima
mostrando os seguintes resultados:



1. `'mean_estimate`: a média da amostra.
2. `'conf_level`: nível de confidência selecionado pelo usuário.
3. `'conf_interval`: intervalo de confidência para a média da população.
4. `'method`: procedimento de inferência.
5. `'hypotheses`: hipótese do nulo e hipótese alternativa a ser testada.
6. `'statistic`: valor da amostra estatística a ser usado para testar a hipótese do nulo.
7. `'distribution`: distribuição da amostra estatística, juntamente com seus parâmetro(s).
8. `'p_value`: valores de $p$ do teste.


Exemplos:


Executa um teste-*t* exato com variância desconhecida. A hipótese do nulo
é $H_0: mean=50$ contra a alternativa unilatera $H_1: mean<50$;
conforme os resultados, o valor de $p$ é muito grande, não existem
evidências paa rejeitar $H_0$.








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


Nesta ocasião Maxima executa um testte assintótico, baseado no *Teorema do Limite Central*.
A hipótese do nulo é $H_0: equal(mean, 50)$ contra a alternativa de duas vias $H_1: not equal(mean, 50)$;
conforme os resultados, o valor de $p$ é muito pequeno, $H_0$ pode ser rejeitado em
favor da alternativa $H_1$. Note que, como indicado pela componente `Method`,
esse procedimento pode ser aplicado a grandes amostras.










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
<!-- signatures: test_means_difference(x1, x2), test_means_difference(x1, x2, opção_1, opção_2, ...) -->
### Function: test_means_difference (x1, x2)

Esse é o teste-*t* de diferença de médias entre duas amostras.
Os argumentos *x1* e *x2* são listas ou matrizes colunas
contendo duas amostras independentes. No caso de diferentes variâncias desconhecidas
(veja opções `'dev1`, `'dev2` e `'varequal` abaixo),
os graus de liberdade são calculados por meio da aproximação de Welch.
`test_means_difference` também executa um teste assintótico
baseado no *Teorema do Limite Central* se a opção `'asymptotic` for
escolhida para `true`.


Opções:



- *
- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.
- *
`'dev1`, o valor padrão é `'unknown`, é o valor do desvio padrão
da amostra *x1* quando esse desvio for conhecido; valores válidos são: `'unknown` ou uma expressão positiva.
- *
`'dev2`, o valor padrão é `'unknown`, é o valor do desvio padrão
da amostra *x2* quando esse desvio for conhecido; valores válidos são: `'unknown` ou uma expressão positiva.
- *
`'varequal`, o valor padrão é `false`, se variâncias podem serem consideradas como iguais ou não;
essa opção tem efeito somente quando `'dev1` e/ou `'dev2` forem  `'unknown`.
- *
`'conflevel`, o valor padrão é `95/100`, nível de confidência para o intervalo de confidência; deve
ser uma expressão que toma valores em (0,1). 

Nota de Tradução: (0,1) representa intervalo aberto.
- *
`'asymptotic`, o valor padrão é `false`, indica se `test_means_difference` executa um teste-*t* exato ou
um teste assíntótico baseando-se no *Teorema do Limite Central*;
valores válidos são `true` e `false`.


A saída da função `test_means_difference` é um objeto `inference_result` do Maxima
mostrando os seguintes resultados:



1. `'diff_estimate`: a diferença de médias estimadas.
2. `'conf_level`: nível de confidência selecionado pelo usuário.
3. `'conf_interval`: intervalo de confidência para a diferença de médias.
4. `'method`: procedimento de inferência.
5. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
6. `'statistic`: valor da amostra estatística usado para testar a hipótese do nulo.
7. `'distribution`: distribuição da amostra estatística, juntamente com seu(s) parâmetro(s).
8. `'p_value`: valor de $p$ do teste.


Exemplos:


A igualdade de médias é testada com duas pequenas amostras *x* e *y*,
contra a alternativa $H_1: m_1>m_2$, sendo $m_1$ e $m_2$
as médias das populações; variâncias são desconhecidas e supostamente admitidas para serem diferentes.














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


O mesmo teste que antes, mas agora as variâncias são admitidas serem supostamente
iguais.














```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: matrix([1.2],[6.9],[38.7],[20.4],[17.2])$
(%i4) test_means_difference(x,y,'alternative='greater,'varequal=true);
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

Teste de Shapiro-Wilk para normalidade. O argumento *x* é uma lista de números, e o tamanho
da amostra deve ser maior que 2 e menor ou igua a 5000, de outra forma, a função
`test_normality` sinaliza com um erro.


Referência:


  

[1] Algorithm AS R94, Applied Statistics (1995), vol.44, no.4, 547-551


A saída da função `test_normality` é um objeto `inference_result` do Maxima
com os seguintes resultados:



1. `'statistic`: valor do *W* estatístico.
2. `'p_value`: valor de $p$ sob a hipótese de normalidade.


Exemplos:


Verifica a normalidade de uma população, baseada em uma amostra de tamanho 9.












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
<!-- keywords: test_rank_sum -->
<!-- signatures: test_rank_sum(x1, x2), test_rank_sum(x1, x2, opção_1) -->
### Function: test_rank_sum (x1, x2)

Esse é o teste de Wilcoxon-Mann-Whitney para comparação das medianas de duas
populações contínuas. Os primeiros dois argumentos *x1* e *x2* são listas
ou matrizes colunas com os dados de duas amostras independentes. Executa aproximação
normal se quaisquer dos tamanhos de amostra for maior que 10, ou se houverem empates.


Opção:



- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.


A saída da função `test_rank_sum` é um objeto `inference_result` do Maxima
com os seguintes resultados:



1. `'method`: procedimento de inferência.
2. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
3. `'statistic`: valor da amostra estatística usada para testar a hipótese do nulo.
4. `'distribution`: distribuição da amostra estatística, juntamente com seus parâmetros.
5. `'p_value`: o valor de $p$ do teste.


Exemplos:


Verifica se populações possuem medianas similares. Tamanhos de amotra
são pequenos e é feito um teste exato.














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


Agora, com grandes amostras e empates, o procedimento faz 
aproximação norma. A hipótese alternativa é
$H_1: median1 < median2$.














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
<!-- signatures: test_sign(x), test_sign(x, opção_1, opção_2, ...) -->
### Function: test_sign (x)

Esse é o teste de sinal não paramétrico para a mediana de uma população contínua.
O argumento *x* é uma lista ou uma matriz coluna contendo uma amostra unidimensional.


Opções:



- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.
- *
`'median`, o valor padrão é `0`, é o valor da mediana a ser verificado.


A saída da função `test_sign` é um objeto `inference_result` do Maxima
mostrando os seguintes resultados:



1. `'med_estimate`: a mediana da amostra.
2. `'method`: procedimento de inferência.
3. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
4. `'statistic`: valor da amostra estatística usada para testar a hipótese do nulo.
5. `'distribution`: distribuição da amostra estatística, juntamente com seu(s) parâmetro(s).
6. `'p_value`: o valor de $p$ do teste.


Exemplos:


Verifica se a população da qual a amostra foi tomada tem mediana 6, 
contra a alternativa $H_1: median > 6$.








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
<!-- signatures: test_signed_rank(x), test_signed_rank(x, opção_1, opção_2, ...) -->
### Function: test_signed_rank (x)

Esse é o teste de ranque sinalizado de Wilcoxon para fazer inferências sobre a mediana de uma
população contínua. O argumento *x* é uma lista ou uma matriz coluna
contendo uma amostra unidimensional. Executa uma aproximação normal se o
tamanho da amostra for maior que 20, ou se existirem zeros ou houverem empates.


Veja também `pdf_rank_test` e `cdf_rank_test`.


Opções:



- *
`'median`, o valor padrão é `0`, é o valor da mediana a ser verificado.
- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.


A saída da função `test_signed_rank` é um objeto `inference_result` do Maxima
com os seguintes resultados:



1. `'med_estimate`: a mediana da amostra.
2. `'method`: procedimento de inferência.
3. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
4. `'statistic`: valor da amostra estatística usado para testar a hipótese do nulo.
5. `'distribution`: distribuição da amostra estatística, juntamente com seu(s) parâmetro(s).
6. `'p_value`: o valor de $p$ do teste.


Exemplos:


Verifica a hipótese do nulo $H_0: median = 15$ contra a 
alternativa $H_1: median > 15$. Esse é um teste exato, ua vez que
não exite empates.












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


Verifica a hipótese do nulo $H_0: equal(median, 2.5)$ contra a
alternativa $H_1: not equal(median, 2.5)$. Esse é um teste aproximado,
uma vez que ocorrem empates.












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
<!-- signatures: test_variance(x), test_variance(x, opção_1, opção_2, ...) -->
### Function: test_variance (x)

Esse é o teste da variância *chi^2*. O argumento *x* é uma lista ou uma matriz coluna
contendo uma amostra unidimensional tomada entre a população normal.


Opções:



- *
`'mean`, o valor padrão é `'unknown`, é a média da população, quando for conhecida.
- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.
- *
`'variance`, o valor padrão é `1`, isso é o valor (positivo) da variância a ser testado.
- *
`'conflevel`, o valor padrão é `95/100`, nível de confidência para o intervalo de confidência; deve
ser uma expressão que toma valores em (0,1).


A saída da função `test_variance` está no objeto `inference_result` do Maxima
mostrando os seguintes resultados:



1. `'var_estimate`: a variância da amostra.
2. `'conf_level`: nível de confidência selecionado pelo usuário.
3. `'conf_interval`: intervalo de confidência para a variância da população.
4. `'method`: procedimento de inferência.
5. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
6. `'statistic`: valor da amostra estatística usado para testar a hipótese do nulo.
7. `'distribution`: distribuição da amostra estatística, juntamente com seu parâmetro.
8. `'p_value`: o valor de $p$ do teste.


Exemplos:


Isso é testado se a variância de uma população com média desconhhecida
for igual ou maior que 200.








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
<!-- signatures: test_variance_ratio(x1, x2), test_variance_ratio(x1, x2, opção_1, opção_2, ...) -->
### Function: test_variance_ratio (x1, x2)

Isso é o teste *F* da razão de variância para duas populações normais.
Os argumentos *x1* e *x2* são listas ou matrizes colunas
contendo duas amostras independentes.


Opções:



- *
`'alternative`, o valor padrão é `'twosided`, é a hipótese alternativa;
valores válidos são: `'twosided`, `'greater` e `'less`.
- *
`'mean1`, o valor padrão é `'unknown`, quando for conhecida, isso é a média da
população da qual *x1* foi tomada.
- *
`'mean2`, o valor padrão é `'unknown`, quando for conhecida, isso é a média da
população da qual *x2* foi tomada.
- *
`'conflevel`, o valor padrão é `95/100`, nível de confidência para o intervalo de confidência da
razão; deve ser uma expressão que tome valores em (0,1).


A saída da função `test_variance_ratio` é um objeto `inference_result` do Maxima
mostrando os seguintes resultados:



1. `'ratio_estimate`: a razão de variância da amostra.
2. `'conf_level`: nível de confidência selecionado pelo usuário.
3. `'conf_interval`: intervalo de confidência para a razão de variância.
4. `'method`: procedimento de inferência.
5. `'hypotheses`: a hipótese do nulo e a hipótese alternativa a serem testadas.
6. `'statistic`: valor da amostra estatística usado para testar a hipótese do nulo.
7. `'distribution`: distribuição da amostra estatística, juntamente com seus parâmetros.
8. `'p_value`: o valor de $p$ do teste.



Exemplos:


a igualdade das variâncias de duas populações normais é verificado
contra a alternativa que a primeira é maior que a segunda.














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

