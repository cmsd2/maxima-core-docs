## Ajuda

<!-- category: Other -->
<!-- keywords: demo -->
<!-- signatures: demo(nomeficheiro) -->
### Function: demo (nomeficheiro)

Avalia expressões Maxima em *nomeficheiro* e mostra os resultados.
`demo` faz uma pausa após avaliar cada expressão
e continua após a conclusão com um enter das entradas de utilizador.
(Se executando em Xmaxima, `demo` pode precisar ver um ponto e vírgula `;`
seguido por um enter.)


`demo` procura na lista de directórios
`file_search_demo` para achar `nomeficheiro`.
Se o ficheiro tiver o sufixo `dem`,
o sufixo pode ser omitido.
Veja também `file_search`.


`demo` avalia seus argumento.
`demo` retorna o nome do ficheiro de demonstração.


Exemplo:



```maxima
(%i1) demo ("disol");

batching /home/wfs/maxima/share/simplification/disol.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i2)                      load("disol")

_
(%i3)           exp1 : a (e (g + f) + b (d + c))
(%o3)               a (e (g + f) + b (d + c))

_
(%i4)                disolate(exp1, a, b, e)
(%t4)                         d + c

(%t5)                         g + f

(%o5)                   a (%t5 e + %t4 b)

_
(%i5) demo ("rncomb");

batching /home/wfs/maxima/share/simplification/rncomb.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i6)                     load("rncomb")

_
                             z         x
(%i7)               exp1 : ----- + ---------
                           y + x   2 (y + x)
                          z         x
(%o7)                   ----- + ---------
                        y + x   2 (y + x)

_
(%i8)                     combine(exp1)
                          z         x
(%o8)                   ----- + ---------
                        y + x   2 (y + x)

_
(%i9)                     rncombine(%)
                             2 z + x
(%o9)                       ---------
                            2 (y + x)

_
                             d   c   b   a
(%i10)                exp2 : - + - + - + -
                             3   3   2   2
                          d   c   b   a
(%o10)                    - + - + - + -
                          3   3   2   2

_
(%i11)                    combine(exp2)
                      2 d + 2 c + 3 (b + a)
(%o11)                ---------------------
                                6

_
(%i12)                   rncombine(exp2)
                      2 d + 2 c + 3 b + 3 a
(%o12)                ---------------------
                                6

_
(%i13)
```

<!-- category: Other -->
<!-- keywords: describe -->
<!-- signatures: describe(string), describe(string, exact), describe(string, inexact) -->
### Function: describe (string)

`describe(string)` é equivalente a `describe(string, exact)`.


`describe(string, exact)` encontra um item com título igual
(case-insensitive)
a *string*, se existir tal item.


`describe(string, inexact)` encontra todos os itens documentados que contiverem *string* em seus títulos.
Se existe mais de um de tal item, Maxima solicita ao utilizador seleccionar
um item ou ítens para mostrar.


Na linha de comando interativa,
`? foo` (com um espaço entre `?` e `foo`)
é equivalente a `describe("foo", exact)`.
e `?? foo` é equivalente a `describe("foo", inexact)`.


`describe("", inexact)` retorna uma lista de todos os tópicos documentados no manual on-line.


`describe` não avalia seu argumento.
`describe` retorna `true` se alguma documentação for encontrada, de outra forma retorna `false`.


Veja também *Documentação*.


Exemplo:



```maxima
(%i1) ?? integ
 0: (maxima.info)Introduction to Elliptic Functions and Integrals.
 1: Definitions for Elliptic Integrals.
 2: Integration.
 3: Introduction to Integration.
 4: Definitions for Integration.
 5: askinteger :Definitions for Simplification.
 6: integerp :Definitions for Miscellaneous Options.
 7: integrate :Definitions for Integration.
 8: integrate_use_rootsof :Definitions for Integration.
 9: integration_constant_counter :Definitions for Integration.
Enter space-separated numbers, `all' or `none': 7 8

Info from file /use/local/maxima/doc/info/maxima.info:
 - Function: integrate (expr, var)
 - Function: integrate (expr, var, a, b)
     Attempts to symbolically compute the integral of `expr' with
     respect to `var'.  `integrate (expr, var)' is an indefinite
     integral, while `integrate (expr, var, a, b)' is a definite
     integral, [...]
```


Nesse , ítens 7 e 8 foram seleccionados.
Todos ou nenhum dos ítens poderia ter sido seleccionado através da inserção de `all` ou `none`,
que podem ser abreviado para `a` ou para `n`, respectivamente.

<!-- category: Other -->
<!-- keywords: example -->
<!-- signatures: example(tópico), example() -->
### Function: example (tópico)

`example (topic)` mostra alguns exemplos de *tópico*,
que é um símbolo (não uma sequência de caracteres).
A maioria dos tópicos são nomes de função.
`example ()` retorna a lista de todos os tópicos reconhecidos.


O nome do ficheiro contendo os exemplos é dado pela
variável global `manual_demo`, cujo valor padrão é `"manual.demo"`.


`example` não avalia seu argumento.
`example` retorna `done`
a menos que ocorra um erro ou não exista o argumento fornecido pelo utilizador, nesse caso `example`
retorna uma lista de todos os tópicos reconhecidos.


Exemplos:



```maxima
(%i1) example (append);
(%i2) append([x+y,0,-3.2],[2.5E+20,x])
(%o2)             [y + x, 0, - 3.2, 2.5E+20, x]
(%o2)                         done
(%i3) example (coeff);
(%i4) coeff(b+tan(x)+2*a*tan(x) = 3+5*tan(x),tan(x))
(%o4)                      2 a + 1 = 5
(%i5) coeff(1+x*%e^x+y,x,0)
(%o5)                         y + 1
(%o5)                         done
```

