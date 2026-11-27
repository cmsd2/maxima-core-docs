## Definição de Função

<!-- category: Programming -->
<!-- keywords: buildq -->
<!-- signatures: buildq(L, expr) -->
### Function: buildq (L, expr)

Substitue variáveis nomeadas pela lista *L* dentro da expressão *expr*,
paralelamente,
sem avaliar *expr*.
A expressão resultante é simplificada,
mas não avaliada,
após `buildq` realizar a substituição.


Os elementos de *L* são símbolos ou expressões de atribuição `símbolo: valor`,
avaliadas paralelamente.
Isto é, a associação de uma variável sobre o lado direito de uma atribuição
é a associação daquela variável no contexto do qual `buildq` for chamada,
não a associação daquela variável na lista *L* de variáveis.
Se alguma variável em *L* não dada como uma atribuição explícita,
sua associação em `buildq` é a mesma que no contexto no qual `buildq` for chamada.


Então as variáveis nomeadas em *L* são substituidas em *expr* paralelamente.
Isto é, a substituição para cada variável é determinada antes que qualquer substituição seja feita,
então a substituição para uma variável não tem efeito sobre qualquer outra.


Se qualquer variável *x* aparecer como `splice (x)` em *expr*,
então *x* deve estar associada para uma lista,
e a lista recebe uma aplicação da função `splice` (é interpolada) na *expr* em lugar de substituída.


Quaisquer variáveis em *expr* não aparecendo em *L* são levados no resultado tal como foram escritos,
mesmo se elas tiverem associações no contexto do qual `buildq` tiver sido chamada.


Exemplos


`a` é explicitamente associada a `x`,
enquanto `b` tem a mesma associação (nomeadamente 29) como no contexto chamado,
e `c` é levada do começo ao fim da forma como foi escrita.
A expressão resultante não é avaliada até a avaliação explícita ( com duplo apóstrofo - não com aspas - `''%`.








```maxima
(%i1) (a: 17, b: 29, c: 1729)$
(%i2) buildq ([a: x, b], a + b + c);
(%o2)                      x + c + 29
(%i3) ''%;
(%o3)                       x + 1758
```


`e` está associado a uma lista, a qual aparece também como tal nos argumentos de `foo`,
e interpolada nos argumentos de `bar`.







```maxima
(%i1) buildq ([e: [a, b, c]], foo (x, e, y));
(%o1)                 foo(x, [a, b, c], y)
(%i2) buildq ([e: [a, b, c]], bar (x, splice (e), y));
(%o2)                  bar(x, a, b, c, y)
```


O resultado é simplificado após substituição.
Se a simplificação for aplicada antes da substituição, esses dois resultados podem ser iguais.






```maxima
(%i1) buildq ([e: [a, b, c]], splice (e) + splice (e));
(%o1)                    2 c + 2 b + 2 a
(%i2) buildq ([e: [a, b, c]], 2 * splice (e));
(%o2)                        2 a b c
```


As variáveis em *L* são associadas em paralelo; se associadas sequêncialmente,
o primeiro resultado pode ser `foo (b, b)`.
Substituições são realizadas em paralelo;
compare o segundo resultado com o resultado de `subst`,
que realiza substituições sequêncialmente.








```maxima
(%i1) buildq ([a: b, b: a], foo (a, b));
(%o1)                       foo(b, a)
(%i2) buildq ([u: v, v: w, w: x, x: y, y: z, z: u], bar (u, v, w, x, y, z));
(%o2)                 bar(v, w, x, y, z, u)
(%i3) subst ([u=v, v=w, w=x, x=y, y=z, z=u], bar (u, v, w, x, y, z));
(%o3)                 bar(u, u, u, u, u, u)
```


Constrói uma lista de euqções com algumas variáveis ou expressões sobre o lado esquerdo
e seus valores sobre o lado direito.
`macroexpand` mostra a expressão retornada por `show_values`.









```maxima
(%i1) show_values ([L]) ::= buildq ([L], map ("=", 'L, L));
(%o1)   show_values([L]) ::= buildq([L], map("=", 'L, L))
(%i2) (a: 17, b: 29, c: 1729)$
(%i3) show_values (a, b, c - a - b);
(%o3)              [a = 17, b = 29, c = 1729]
```

<!-- category: Programming -->
<!-- keywords: macroexpand -->
<!-- signatures: macroexpand(expr) -->
### Function: macroexpand (expr)

Retorna a expansão da macro de *expr* sem avaliar a expressão,
quando `expr` for uma chamada de função de macro.
De outra forma, `macroexpand` retorna *expr*.


Se a expansão de *expr* retorna outra chamada de função de macro,
aquela chamada de função de macro é também expandida.


`macroexpand` coloca apóstrofo em seus argumentos, isto é, não os avalia.
Todavia, se a expansão de uma chamada de função de macro tiver algum efeito,
esse efeito colateral é executado.


Veja também `::=`, `macros`, e `macroexpand1`.


Exemplos










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

Retorna a expansão de macro de *expr* sem avaliar a expressão,
quando `expr` for uma chamada de função de macro.
De outra forma, `macroexpand1` retorna *expr*.


`macroexpand1` não avalia seus argumentos.
Todavia, se a expansão de uma chamada de função de macro tiver algum efeito,
esse efeito colateral é executado.


Se a expansão de *expr* retornar outra chamada de função de macro,
aquela chamada de função de macro não é expandida.


Veja também `::=`, `macros`, e `macroexpand`.


Examples










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

Default value: `[]`


`macros` é a lista de funções de macro definidas pelo utilizador.
O operador de definição de função de macro `::=` coloca uma nova função de macro nessa lista,
e `kill`, `remove`, e `remfunction` removem funções de macro da lista.


Veja também `infolists`.

<!-- category: Programming -->
<!-- keywords: splice -->
<!-- signatures: splice(a) -->
### Function: splice (a)

Une como se fosse um elo de ligação (interpola) a lista nomeada através do átomo *a* em uma expressão,
mas somente se `splice` aparecer dentro de `buildq`;
de outra forma, `splice` é tratada como uma função indefinida.
Se aparecer dentro de `buildq` com *a* sozinho (sem `splice`),
*a* é substituido (não interpolado) como uma lista no resultado.
O argumento de `splice` pode somente ser um átomo;
não pode ser uma lista lateral ou uma expressão que retorna uma lista.


Tipicamente `splice` fornece os argumentos para uma função ou operador.
Para uma função `f`, a expressão `f (splice (a))` dentro de `buildq`
expande para `f (a[1], a[2], a[3], ...)`.
Para um operador `o`, a expressão `"o" (splice (a)` dentro de `buildq`
expande para `"o" (a[1], a[2], a[3], ...)`,
onde `o` pode ser qualquer tipo de operador (tipicamente um que toma múltiplos argumentos).
Note que o operador deve ser contido dentro de aspas duplas `"`.


Exemplos









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

