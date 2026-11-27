## eval_string

<!-- category: IO -->
<!-- keywords: eval_string -->
<!-- signatures: eval_string(str) -->
### Function: eval_string (str)

Entrega a sequência de caracteres do Maxima *str* como uma expressão do Maxima e a avalia.
*str* é uma sequência de caracteres do Maxima. Essa sequência pode ou não ter um marcador de final (sinal de dólar `$` ou ponto e vírgula `;`).
Somente a primeira expressão é entregue e avaliada, se ouver mais de uma.


Reclama se *str* não for uma sequência de caracteres do Maxima.


Exemplos:


```maxima
(%i1) load("eval_string")$

(%i2) eval_string ("foo: 42; bar: foo^2 + baz");
(%o2)                       42
(%i3) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o3)                   baz + 1764
```


Para usar essa função escreva primeiro `load("eval_string")`. Veja também `parse_string`.

<!-- category: IO -->
<!-- keywords: parse_string -->
<!-- signatures: parse_string(str) -->
### Function: parse_string (str)

Entrega a sequência de caracteres do Maxima *str* como uma expressão do Maxima (sem fazer nenhuma avaliação dessa expressão).
*str* é uma sequência de caracteres do Maxima. Essa sequência pode ou não ter um marcador de final (sinal de dólar `$` ou ponto e vírgula `;`).
Somente a primeira expressão é entregue e avaliada, se ouver mais de uma.


Reclama se *str* não for uma sequência de caracteres do Maxima.


Exemplos:


```maxima
(%i1) load("eval_string")$

(%i2) parse_string ("foo: 42; bar: foo^2 + baz");
(%o2)                    foo : 42
(%i3) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o3)          (foo : 42, bar : foo  + baz)
```


Para usar essa função escreva primeiro `load("eval_string")`. Veja também a função `eval_string`.

