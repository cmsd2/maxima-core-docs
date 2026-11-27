## Conjuntos

<!-- category: Other -->
<!-- keywords: adjoin -->
<!-- signatures: adjoin(x, a) -->
### Function: adjoin (x, a)

Calcula a união do conjunto *a* com `{x}`.


`adjoin` falha se *a* não for um conjunto literal.


`adjoin(x, a)` e `union(set(x), a)`
são equivalentes; contudo, `adjoin` pode ser um pouco mais
rápida que `union`.


Veja também `disjoin`.


Exemplos:







```maxima
(%i1) adjoin (c, {a, b});
(%o1)                       {a, b, c}
(%i2) adjoin (a, {a, b});
(%o2)                        {a, b}
```

<!-- category: Other -->
<!-- keywords: belln -->
<!-- signatures: belln(n) -->
### Function: belln (n)

Representa o $n$-ésimo número de Bell.  `belln(n)` é o
número de partições de um conjunto de *n*
elementos.


Para inteiros não negativos *n*, `belln(n)` simplifica
para o $n$-ésimo número de Bell.  `belln` não simplifica
para qualquer outro tipo de argumento.


`belln`, aplicada a equações, listas, matrizes
e conjuntos, é calculada em forma distributiva.


Exemplos:


`belln` aplicado a inteiros não negativos.








```maxima
(%i1) makelist (belln (i), i, 0, 6);
(%o1)               [1, 1, 2, 5, 15, 52, 203]
(%i2) is (cardinality (set_partitions ({})) = belln (0));
(%o2)                         true
(%i3) is (cardinality (set_partitions ({1, 2, 3, 4, 5, 6})) = belln (6));
(%o3)                         true
```


`belln` aplicado a argumentos que não são inteiros não negativos.






```maxima
(%i1) [belln (x), belln (sqrt(3)), belln (-9)];
(%o1)        [belln(x), belln(sqrt(3)), belln(- 9)]
```

<!-- category: Other -->
<!-- keywords: cardinality -->
<!-- signatures: cardinality(a) -->
### Function: cardinality (a)

Calcula o número de elementos distintos do conjunto *a*.


`cardinality` ignora elementos redundantes mesmo quando a
simplificação não estiver habilitada.


Exemplos:









```maxima
(%i1) cardinality ({});
(%o1)                           0
(%i2) cardinality ({a, a, b, c});
(%o2)                           3
(%i3) simp : false;
(%o3)                         false
(%i4) cardinality ({a, a, b, c});
(%o4)                           3
```

<!-- category: Other -->
<!-- keywords: cartesian_product -->
<!-- signatures: cartesian_product(b_1, ..., b_n) -->
### Function: cartesian_product (b_1, ..., b_n)

Retorna um conjunto de listas da forma `[x_1, ..., x_n]`, onde *x_1*, ..., *x_n* são elementos dos
conjuntos *b_1*, ... , *b_n*, respectivamente.


`cartesian_product` falha se qualquer argumento não for um
conjunto literal.


Exemplos:









```maxima
(%i1) cartesian_product ({0, 1});
(%o1)                      {[0], [1]}
(%i2) cartesian_product ({0, 1}, {0, 1});
(%o2)           {[0, 0], [0, 1], [1, 0], [1, 1]}
(%i3) cartesian_product ({x}, {y}, {z});
(%o3)                      {[x, y, z]}
(%i4) cartesian_product ({x}, {-1, 0, 1});
(%o4)              {[x, - 1], [x, 0], [x, 1]}
```

<!-- category: Other -->
<!-- keywords: disjoin -->
<!-- signatures: disjoin(x, a) -->
### Function: disjoin (x, a)

Retorna o conjunto *a* sem o elemento *x*.  Se *x* não for
um elemento de *a*, retorna *a* sem
modificações.


`disjoin` reclama se *a* não for um conjunto literal.


`disjoin(x, a)`, `delete(x, a)`, e
`setdifference(a, set(x))` são todos equivalentes.
Desses, `disjoin` é geralmente mais rápido que os outros.


Exemplos:








```maxima
(%i1) disjoin (a, {a, b, c, d});
(%o1)                       {b, c, d}
(%i2) disjoin (a + b, {5, z, a + b, %pi});
(%o2)                      {5, %pi, z}
(%i3) disjoin (a - b, {5, z, a + b, %pi});
(%o3)                  {5, %pi, b + a, z}
```

<!-- category: Other -->
<!-- keywords: disjointp -->
<!-- signatures: disjointp(a, b) -->
### Function: disjointp (a, b)

Retorna `true` se e somente se os conjuntos *a* e *b* forem
disjuntos.


`disjointp` falha se ou *a* ou *b* não forem conjuntos
literais.


Exemplos:







```maxima
(%i1) disjointp ({a, b, c}, {1, 2, 3});
(%o1)                         true
(%i2) disjointp ({a, b, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: divisors -->
<!-- signatures: divisors(n) -->
### Function: divisors (n)

Representa o conjunto dos divisores de *n*.


`divisors(n)` produz um conjunto de divisores inteiros quando
*n* for um inteiro não nulo. O conjunto dos divisores inclui os
elementos 1 e *n*. Os divisores de um inteiro negativo são os
divisores do seu valor absoluto.


`divisors`, aplicada a equações, listas, matrizes
e conjuntos, é calculada em forma distributiva.


Exemplos:


Podemos verificar que 28 é um número perfeito: a
adição dos seus divisores (excepto o próprio 28) é
28.







```maxima
(%i1) s: divisors(28);
(%o1)                 {1, 2, 4, 7, 14, 28}
(%i2) lreduce ("+", args(s)) - 28;
(%o2)                          28
```


`divisors` é uma função de
simplificação.  Substituindo 8 por `a` em
`divisors(a)` calcula os divisores sem ser preciso pedir que
`divisors(8)` seja reavaliada.







```maxima
(%i1) divisors (a);
(%o1)                      divisors(a)
(%i2) subst (8, a, %);
(%o2)                     {1, 2, 4, 8}
```


`divisors`, aplicada a equações, listas, matrizes
e conjuntos, é calculada em forma distributiva.









```maxima
(%i1) divisors (a = b);
(%o1)               divisors(a) = divisors(b)
(%i2) divisors ([a, b, c]);
(%o2)        [divisors(a), divisors(b), divisors(c)]
(%i3) divisors (matrix ([a, b], [c, d]));
                  [ divisors(a)  divisors(b) ]
(%o3)             [                          ]
                  [ divisors(c)  divisors(d) ]
(%i4) divisors ({a, b, c});
(%o4)        {divisors(a), divisors(b), divisors(c)}
```

<!-- category: Other -->
<!-- keywords: elementp -->
<!-- signatures: elementp(x, a) -->
### Function: elementp (x, a)

Retorna `true` se e somente se *x* for um elemento do conjunto
*a*.


`elementp` falha se *a* não for um conjunto literal.


Exemplos:







```maxima
(%i1) elementp (sin(1), {sin(1), sin(2), sin(3)});
(%o1)                         true
(%i2) elementp (sin(1), {cos(1), cos(2), cos(3)});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: emptyp -->
<!-- signatures: emptyp(a) -->
### Function: emptyp (a)

Retorna `true` se e somente se *a* for o conjunto vazio ou uma
lista vazia.


Exemplos:







```maxima
(%i1) map (emptyp, [{}, []]);
(%o1)                     [true, true]
(%i2) map (emptyp, [a + b, {{}}, %pi]);
(%o2)                 [false, false, false]
```

<!-- category: Other -->
<!-- keywords: equiv_classes -->
<!-- signatures: equiv_classes(s, F) -->
### Function: equiv_classes (s, F)

Retorna um conjunto das classes de equivalências do conjunto *s*
com relação à relação de
equivalência *F*.


*F* é uma função de duas variáveis definida
sobre o produto cartesiano *s* por *s*.  O valor de retorno de
*F* é ou `true` ou `false`, ou uma expressão
*expr* tal que `is(expr)` é ou `true` ou
`false`.


Quando *F* não for uma relação de equivalência,
`equiv_classes` aceita-a sem reclamação,
mas o resultado é geralmente incorrecto nesse caso.







Exemplos:


A relação de equivalência é uma expressão lambda a
qual retorna `true` ou `false`.






```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, lambda ([x, y], is (equal (x, y))));
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


A relação de equivalência é o nome de uma
função relacional que avalia para `true` ou
`false`.






```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, equal);
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


As classes de equivalência são números que diferem por um múltiplo
de 3.






```maxima
(%i1) equiv_classes ({1, 2, 3, 4, 5, 6, 7}, lambda ([x, y], remainder (x - y, 3) = 0));
(%o1)              {{1, 4, 7}, {2, 5}, {3, 6}}
```

<!-- category: Other -->
<!-- keywords: every -->
<!-- signatures: every(f, s), every(f, L_1, ..., L_n) -->
### Function: every (f, s)

Retorna `true` se o predicado *f* for `true` para todos os
argumentos fornecidos.


Dado um conjunto como segundo argumento, `every(f, s)`
retorna `true` se `is(f(a_i))` retornar
`true` para todos os *a_i* em *s*.  `every` pode ou
não avaliar *f* para todos os *a_i* em *s*. Uma vez que
os conjuntos são desordenados, `every` pode avaliar
`f(a_i)` em qualquer ordem.


Dada uma ou mais listas como argumentos, `every(f, L_1, ..., L_n)` retorna `true` se `is(f(x_1, ..., x_n))` retornar `true` para todos os *x_1*, ...,
*x_n* em *L_1*, ..., *L_n*, respectivamente. `every`
pode ou não avaliar *f* para toda combinação
*x_1*, ..., *x_n*.  `every` avalia listas na ordem de
incremento do índice.


Dado um conjunto vazio `{}` ou uma lista vazia `[]` como
argumentos, `every` retorna `false`.


Quando o sinalizador global `maperror` for `true`, todas as
listas *L_1*, ..., *L_n* deverão ter o mesmo comprimento.
Quando `maperror` for falso, as listas dadas como argumentos
serão efectivamente truncadas para o comprimento da menor lista.


Os resultados do predicado *f* que avaliarem (via `is`) para
algo diferente de `true` ou `false` são governados através
da variável global `prederror`. Quando `prederror` for
`true`, tais valores são tratados como `false`, e o valor de
retorno de `every` é `false`.  Quando `prederror` for
`false`, tais valores são tratados como `unknown`, e o valor
de retorno de `every` é `unknown`.


Exemplos:


`every` aplicada a um conjunto simples. O predicado é uma
função de um argumento.







```maxima
(%i1) every (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) every (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         false
```


`every` aplicada a duas listas. O predicado é uma
função de dois argumentos.







```maxima
(%i1) every ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) every ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Predicado *f* que produz resultados diferentes de `true` ou
`false`, governados por meio da variável global `prederror`.










```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z], [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) prederror : true;
(%o4)                         true
(%i5) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o5)                         false
```

<!-- category: Other -->
<!-- keywords: extremal_subset -->
<!-- signatures: extremal_subset(s, f, max), extremal_subset(s, f, min) -->
### Function: extremal_subset (s, f, max)

Encontra o subconjunto de *s* para o qual a função
*f* toma valores máximos ou mínimos.


`extremal_subset(s, f, max)` encontra o subconjunto do
conjunto ou lista *s* para os quais a função real
*f* assume um valor máximo.


`extremal_subset(s, f, min)` encontra o subconjunto do
conjunto ou lista *s* para a qual a função real
*f* assume um valor mínimo.


Exemplos:







```maxima
(%i1) extremal_subset ({-2, -1, 0, 1, 2}, abs, max);
(%o1)                       {- 2, 2}
(%i2) extremal_subset ({sqrt(2), 1.57, %pi/2}, sin, min);
(%o2)                       {sqrt(2)}
```

<!-- category: Other -->
<!-- keywords: flatten -->
<!-- signatures: flatten(expr) -->
### Function: flatten (expr)

Colecta argumentos de subexpressões que possuem o mesmo operador que
*expr* e constrói uma expressão a partir desses argumentos
colectados.


Subexpressões nas quais o operador é diferente do operador principal
de `expr` são copiadas sem modificação, mesmo se
tiverem subexpressões com o mesmo operador que `expr`.


É possível que `flatten` construia expressões nas
quais o número de argumentos difira dos argumentos declarados para um
operador; isso pode provocar uma mensagem de erro do simplificador ou do
avaliador.  `flatten` não tenta detectar tais
situações.


Expressões com representações especiais, por exemplo,
expressões racionais canónicas (CRE), não podem usar a
função `flatten`; nesses casos, `flatten`
retorna os seus argumentos sem modificação.


Exemplos:


Aplicado a uma lista, `flatten` reúne todos os elementos da
lista que sejam listas.






```maxima
(%i1) flatten ([a, b, [c, [d, e], f], [[g, h]], i, j]);
(%o1)            [a, b, c, d, e, f, g, h, i, j]
```


Aplicado a um conjunto, `flatten` reúne todos os elementos do
conjunto que sejam conjuntos.







```maxima
(%i1) flatten ({a, {b}, {{c}}});
(%o1)                       {a, b, c}
(%i2) flatten ({a, {[a], {a}}});
(%o2)                       {a, [a]}
```


o efeito de `flatten` é similar a declarar o operador principal
para ser enário. No entanto, `flatten` não faz efeito sobre
subexpressões que possuem um operador diferente do operador principal,
enquanto uma declaração enária faz efeito.








```maxima
(%i1) expr: flatten (f (g (f (f (x)))));
(%o1)                     f(g(f(f(x))))
(%i2) declare (f, nary);
(%o2)                         done
(%i3) ev (expr);
(%o3)                      f(g(f(x)))
```


`flatten` trata funções subscritas da mesma forma
que qualquer outro operador.






```maxima
(%i1) flatten (f[5] (f[5] (x, y), z));
(%o1)                      f (x, y, z)
                            5
```


É possível que `flatten` construa expressões nas
quais o número de argumentos difira dos argumentos declarados para um
operador;








```maxima
(%i1) 'mod (5, 'mod (7, 4));
(%o1)                   mod(5, mod(7, 4))
(%i2) flatten (%);
(%o2)                     mod(5, 7, 4)
(%i3) ''%, nouns;
Wrong number of arguments to mod
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Other -->
<!-- keywords: full_listify -->
<!-- signatures: full_listify(a) -->
### Function: full_listify (a)

Substitui todo operador de conjunto em *a* por um operador de lista,
e retorna o resultado. `fullt_listify` substitui operadores de
conjunto em subexpressões aninhadas, mesmo se o operador principal
não for (`set`).


`listify` substitui unicamente o operador principal.


Exemplos:







```maxima
(%i1) full_listify ({a, b, {c, {d, e, f}, g}});
(%o1)               [a, b, [c, [d, e, f], g]]
(%i2) full_listify (F (G ({a, b, H({c, d, e})})));
(%o2)              F(G([a, b, H([c, d, e])]))
```

<!-- category: Other -->
<!-- keywords: fullsetify -->
<!-- signatures: fullsetify(a) -->
### Function: fullsetify (a)

Quando *a* for uma lista, substitui o operador de lista por um
operador de conjunto, e aplica `fullsetify` a cada elemento que for
um conjunto.  Quando *a* não for uma lista, o resultado é
*a* na sua forma original e sem modificações.


`setify` substitui unicamente o operador principal.


Exemplos:


Na linha (%o2), o argumento de `f` não é convertido para um
conjunto porque o operador principal de `f([b])` não é uma
lista.







```maxima
(%i1) fullsetify ([a, [a]]);
(%o1)                       {a, {a}}
(%i2) fullsetify ([a, f([b])]);
(%o2)                      {a, f([b])}
```

<!-- category: Other -->
<!-- keywords: identity -->
<!-- signatures: identity(x) -->
### Function: identity (x)

Retorna *x* para qualquer argumento *x*.


Exemplos:


`identity` pode ser usado como um predicado quando os argumentos
forem valores Booleanos.






```maxima
(%i1) every (identity, [true, true]);
(%o1)                         true
```

<!-- category: Other -->
<!-- keywords: integer_partitions -->
<!-- signatures: integer_partitions(n), integer_partitions(n, len) -->
### Function: integer_partitions (n)

Calcula partições inteiras de *n*, isto é, listas
de inteiros cuja soma dos elementos de cada lista é *n*.


`integer_partitions(n)` encontra o conjunto de todas as
partições do inteiro *n*. Cada
partição é uma lista ordenada do maior para o menor.


`integer_partitions(n, len)` encontra todas as
partições com comprimento *len* ou menor; nesse
caso, serão adicionados zeros ao final de cada
partição de comprimento menor que *len*, para fazer
com que todas as partições tenham exactamente *len* termos.
Cada partição é uma lista ordenada do maior para o
menor.


Uma lista $[a_1, ..., a_m]$ é uma partição de um
inteiro não negativo $n$ quando: (1) cada $a_i$ é um
inteiro não nulo, e (2) $a_1 + ... + a_m = n.$ Dessa forma, 0
não tem partições.


Exemplos:











```maxima
(%i1) integer_partitions (3);
(%o1)               {[1, 1, 1], [2, 1], [3]}
(%i2) s: integer_partitions (25)$
(%i3) cardinality (s);
(%o3)                         1958
(%i4) map (lambda ([x], apply ("+", x)), s);
(%o4)                         {25}
(%i5) integer_partitions (5, 3);
(%o5) {[2, 2, 1], [3, 1, 1], [3, 2, 0], [4, 1, 0], [5, 0, 0]}
(%i6) integer_partitions (5, 2);
(%o6)               {[3, 2], [4, 1], [5, 0]}
```


Para encontrar todas as partições que satisfazem uma
condição, use a função `subset`;
aqui está um exemplo que encontra todas as partições
de 10 cujos elementos da lista são números primos.









```maxima
(%i1) s: integer_partitions (10)$
(%i2) cardinality (s);
(%o2)                          42
(%i3) xprimep(x) := integerp(x) and (x > 1) and primep(x)$
(%i4) subset (s, lambda ([x], every (xprimep, x)));
(%o4) {[2, 2, 2, 2, 2], [3, 3, 2, 2], [5, 3, 2], [5, 5], [7, 3]}
```

<!-- category: Other -->
<!-- keywords: intersect -->
<!-- signatures: intersect(a_1, ..., a_n) -->
### Function: intersect (a_1, ..., a_n)

`intersect` é o mesmo que `intersection`, como veremos.

<!-- category: Other -->
<!-- keywords: intersection -->
<!-- signatures: intersection(a_1, ..., a_n) -->
### Function: intersection (a_1, ..., a_n)

Retorna um conjunto contendo os elementos que são comuns aos conjuntos
*a_1* até *a_n*.


`intersection` falha se qualquer dos argumentos não for um
conjunto literal.


Exemplos:













```maxima
(%i1) S_1 : {a, b, c, d};
(%o1)                     {a, b, c, d}
(%i2) S_2 : {d, e, f, g};
(%o2)                     {d, e, f, g}
(%i3) S_3 : {c, d, e, f};
(%o3)                     {c, d, e, f}
(%i4) S_4 : {u, v, w};
(%o4)                       {u, v, w}
(%i5) intersection (S_1, S_2);
(%o5)                          {d}
(%i6) intersection (S_2, S_3);
(%o6)                       {d, e, f}
(%i7) intersection (S_1, S_2, S_3);
(%o7)                          {d}
(%i8) intersection (S_1, S_2, S_3, S_4);
(%o8)                          {}
```

<!-- category: Other -->
<!-- keywords: kron_delta -->
<!-- signatures: kron_delta(x, y) -->
### Function: kron_delta (x, y)

Representa a função delta de Kronecker.


`kron_delta` simplifica para 1 quando *x* e *y* forem
idênticos ou equivalentes, e simplifica para 0 quando *x* e
*y* não forem equivalentes. De outra forma, se não for certo que
*x* e *y* são equivalentes, `kron_delta` simplificará
para uma expressão substantiva. `kron_delta` implementa uma
política de segurança para expressões em
ponto flutuante: se a diferença `x - y`
for um número em ponto flutuante, `kron_delta` simplifica para
uma expressão substantiva quando *x* for aparentemente equivalente
a *y*.


Especificamente, `kron_delta(x, y)` simplifica para 1
quando `is(x = y)` for `true`. `kron_delta` também
simplifica para 1 quando `sign(abs(x - y))` for
`zero` e `x - y` não for um número em ponto
flutuante (e também não for um número de precisão simples em
ponto flutuante nem um número de precisão dupla em poto flutuante,
isto é, não for um bigfloat). `kron_delta` simplifica para 0
quando `sign(abs(x - y))` for `pos`.


Caso contrário, `sign(abs(x - y))` é diferente de
`pos` ou `zero`, ou é `zero` e `x - y`
é um número em ponto flutuante. Nesses casos, `kron_delta`
retorna um expressão substantiva.


`kron_delta` é declarada como sendo simétrica. Isto é,
`kron_delta(x, y)` é igual a
`kron_delta(y, x)`.


Exemplos:


Os argumentos de `kron_delta` são idênticos. `kron_delta`
simplifica para 1.








```maxima
(%i1) kron_delta (a, a);
(%o1)                           1
(%i2) kron_delta (x^2 - y^2, x^2 - y^2);
(%o2)                           1
(%i3) float (kron_delta (1/10, 0.1));
(%o3)                           1
```


Os argumentos de `kron_delta` são equivalentes, e a
diferença entre eles não é um número em ponto
flutuante.  `kron_delta` simplifica para 1.







```maxima
(%i1) assume (equal (x, y));
(%o1)                     [equal(x, y)]
(%i2) kron_delta (x, y);
(%o2)                           1
```


Os argumentos de `kron_delta` não são equivalentes.
`kron_delta` simplifica para 0.









```maxima
(%i1) kron_delta (a + 1, a);
(%o1)                           0
(%i2) assume (a > b)$
(%i3) kron_delta (a, b);
(%o3)                           0
(%i4) kron_delta (1/5, 0.7);
(%o4)                           0
```


Os argumentos de `kron_delta` podem ou não ser equivalentes.
`kron_delta` simplifica para uma expressão substantiva.








```maxima
(%i1) kron_delta (a, b);
(%o1)                   kron_delta(a, b)
(%i2) assume(x >= y)$
(%i3) kron_delta (x, y);
(%o3)                   kron_delta(x, y)
```


Os argumentos de `kron_delta` são equivalentes, mas a
diferença entre eles é um número em ponto flutuante.
`kron_delta` simplifica para uma expressão substantiva.











```maxima
(%i1) 1/4 - 0.25;
(%o1)                          0.0
(%i2) 1/10 - 0.1;
(%o2)                          0.0
(%i3) 0.25 - 0.25b0;
Warning:  Float to bigfloat conversion of 0.25
(%o3)                         0.0b0
(%i4) kron_delta (1/4, 0.25);
                                  1
(%o4)                  kron_delta(-, 0.25)
                                  4
(%i5) kron_delta (1/10, 0.1);
                                  1
(%o5)                  kron_delta(--, 0.1)
                                  10
(%i6) kron_delta (0.25, 0.25b0);
Warning:  Float to bigfloat conversion of 0.25
(%o6)               kron_delta(0.25, 2.5b-1)
```


`kron_delta` é simétrica.










```maxima
(%i1) kron_delta (x, y);
(%o1)                   kron_delta(x, y)
(%i2) kron_delta (y, x);
(%o2)                   kron_delta(x, y)
(%i3) kron_delta (x, y) - kron_delta (y, x);
(%o3)                           0
(%i4) is (equal (kron_delta (x, y), kron_delta (y, x)));
(%o4)                         true
(%i5) is (kron_delta (x, y) = kron_delta (y, x));
(%o5)                         true
```

<!-- category: Other -->
<!-- keywords: listify -->
<!-- signatures: listify(a) -->
### Function: listify (a)

Retorna uma lista contendo os elementos de *a* quando *a* for um
conjunto. De outra forma, `listify` retorna *a*.


`full_listify` substitui todos os operadores de conjunto em *a*
por operadores de lista.


Exemplos:







```maxima
(%i1) listify ({a, b, c, d});
(%o1)                     [a, b, c, d]
(%i2) listify (F ({a, b, c, d}));
(%o2)                    F({a, b, c, d})
```

<!-- category: Other -->
<!-- keywords: lreduce -->
<!-- signatures: lreduce(F, s), lreduce(F, s, s_0) -->
### Function: lreduce (F, s)

Extende a função de dois argumentos *F* para uma
função de `n` argumentos, usando
composição, onde *s* é uma lista.


`lreduce(F, s)` retorna `F(... F(F(s_1, s_2), s_3), ... s_n)`.  Quando o argumento opcional *s_0* estiver
presente, o resultado é equivalente a `lreduce(F, cons(s_0, s))`.


A função *F* é aplicada primeiro aos elementos
mais à *esquerda* de lista; daí o nome "lreduce".


Veja também `rreduce`, `xreduce`, e `tree_reduce`.


Exemplos:


`lreduce` sem o argumento opcional.







```maxima
(%i1) lreduce (f, [1, 2, 3]);
(%o1)                     f(f(1, 2), 3)
(%i2) lreduce (f, [1, 2, 3, 4]);
(%o2)                  f(f(f(1, 2), 3), 4)
```


`lreduce` com o argumento opcional.






```maxima
(%i1) lreduce (f, [1, 2, 3], 4);
(%o1)                  f(f(f(4, 1), 2), 3)
```


`lreduce` aplicada a operadores binários internos do Maxima
`/` é o operador de divisão.







```maxima
(%i1) lreduce ("^", args ({a, b, c, d}));
                               b c d
(%o1)                       ((a ) )
(%i2) lreduce ("/", args ({a, b, c, d}));
                                a
(%o2)                         -----
                              b c d
```

<!-- category: Other -->
<!-- keywords: makeset -->
<!-- signatures: makeset(expr, x, s) -->
### Function: makeset (expr, x, s)

Retorna um conjunto com elementos gerados a partir da expressão
*expr*, onde *x* é uma lista de variáveis em *expr*, e
*s*é um conjunto ou lista de listas.  Para gerar cada elemento do
conjunto, *expr* é avaliada com as variáveis *x*
substituídas, em paralelo, por elementos de *s*.


Cada elemento de *s* deve ter o mesmo comprimento que *x*.  A
lista de variáveis *x* deve ser uma lista de
símbolos, sem índices.  Mesmo se existir
somente um símbolo, *x* deve ser uma lista de um
elemento, e cada elemento de *s* deve ser uma lista de um elemento.






Veja também `makelist`.


Exemplos:










```maxima
(%i1) makeset (i/j, [i, j], [[1, a], [2, b], [3, c], [4, d]]);
                           1  2  3  4
(%o1)                     {-, -, -, -}
                           a  b  c  d
(%i2) S : {x, y, z}$
(%i3) S3 : cartesian_product (S, S, S);
(%o3) {[x, x, x], [x, x, y], [x, x, z], [x, y, x], [x, y, y], 
[x, y, z], [x, z, x], [x, z, y], [x, z, z], [y, x, x], 
[y, x, y], [y, x, z], [y, y, x], [y, y, y], [y, y, z], 
[y, z, x], [y, z, y], [y, z, z], [z, x, x], [z, x, y], 
[z, x, z], [z, y, x], [z, y, y], [z, y, z], [z, z, x], 
[z, z, y], [z, z, z]}
(%i4) makeset (i + j + k, [i, j, k], S3);
(%o4) {3 x, 3 y, y + 2 x, 2 y + x, 3 z, z + 2 x, z + y + x, 
                                       z + 2 y, 2 z + x, 2 z + y}
(%i5) makeset (sin(x), [x], {[1], [2], [3]});
(%o5)               {sin(1), sin(2), sin(3)}
```

<!-- category: Other -->
<!-- keywords: moebius -->
<!-- signatures: moebius(n) -->
### Function: moebius (n)

Representa a função de Moebius.


Quando *n* for o produto de $k$ primos distintos,
`moebius(n)` simplifica para $(-1)^k$; quando
$n = 1$, simplifica para 1; e simplifica para 0 para todos os
outros inteiros positivos.


`moebius`, aplicada a equações, listas, matrizes
e conjuntos, é calculada em forma distributiva.


Exemplos:














```maxima
(%i1) moebius (1);
(%o1)                           1
(%i2) moebius (2 * 3 * 5);
(%o2)                          - 1
(%i3) moebius (11 * 17 * 29 * 31);
(%o3)                           1
(%i4) moebius (2^32);
(%o4)                           0
(%i5) moebius (n);
(%o5)                      moebius(n)
(%i6) moebius (n = 12);
(%o6)                    moebius(n) = 0
(%i7) moebius ([11, 11 * 13, 11 * 13 * 15]);
(%o7)                      [- 1, 1, 1]
(%i8) moebius (matrix ([11, 12], [13, 14]));
                           [ - 1  0 ]
(%o8)                      [        ]
                           [ - 1  1 ]
(%i9) moebius ({21, 22, 23, 24});
(%o9)                      {- 1, 0, 1}
```

<!-- category: Other -->
<!-- keywords: multinomial_coeff -->
<!-- signatures: multinomial_coeff(a_1, ..., a_n), multinomial_coeff() -->
### Function: multinomial_coeff (a_1, ..., a_n)

Calcula o coeficiente multinomial.


Quando cada *a_k* for um inteiro não negativo, o coeficiente
multinomial indica o número de formas possíveis de
colocar `a_1 + ... + a_n` objectos distintos em
$n$ caixas com *a_k* elementos na $k$’ésima caixa. Em
geral, `multinomial_coeff (a_1, ..., a_n)` calcula
`(a_1 + ... + a_n)!/(a_1! ... a_n!)`.


`multinomial_coeff()` (sem argumentos) produz 1.


`minfactorial` poderá conseguir simplificar o valor calculado por
`multinomial_coeff`.


Exemplos:









```maxima
(%i1) multinomial_coeff (1, 2, x);
                            (x + 3)!
(%o1)                       --------
                              2 x!
(%i2) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o2)                -----------------------
                                2
(%i3) multinomial_coeff (-6, 2);
                             (- 4)!
(%o3)                       --------
                            2 (- 6)!
(%i4) minfactorial (%);
(%o4)                          10
```

<!-- category: Other -->
<!-- keywords: num_distinct_partitions -->
<!-- signatures: num_distinct_partitions(n), num_distinct_partitions(n, list) -->
### Function: num_distinct_partitions (n)

Calcula o n;umero de partições de inteiros distintos de *n*
quando *n* for um inteiro não negativo.
De outra forma, `num_distinct_partitions` retorna uma expressão substantiva.


`num_distinct_partitions(n, list)` retorna uma 
lista do número de partições distintas de 1, 2, 3, ..., *n*. 


Uma partição distinta de *n* é
uma lista de inteiros positivos distintos $k_1$, ..., $k_m$
tais que $n = k_1 + ... + k_m$.


Exemplos:








```maxima
(%i1) num_distinct_partitions (12);
(%o1)                          15
(%i2) num_distinct_partitions (12, list);
(%o2)      [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15]
(%i3) num_distinct_partitions (n);
(%o3)              num_distinct_partitions(n)
```

<!-- category: Other -->
<!-- keywords: num_partitions -->
<!-- signatures: num_partitions(n), num_partitions(n, list) -->
### Function: num_partitions (n)

Calcula o número das partições inteiras de *n*
quando *n* for um inteiro não negativo.  De outra forma,
`num_partitions` retorna uma expressão substantiva.


`num_partitions(n, list)` retorna uma
lista do número de partições inteiras de 1, 2, 3, ..., *n*.


Para um inteiro não negativo *n*, `num_partitions(n)` é igual a
`cardinality(integer_partitions(n))`; todavia, `num_partitions` 
não constrói actualmente o conjunto das partições, nesse sentido `num_partitions` é mais rápida.


Exemplos:








```maxima
(%i1) num_partitions (5) = cardinality (integer_partitions (5));
(%o1)                         7 = 7
(%i2) num_partitions (8, list);
(%o2)            [1, 1, 2, 3, 5, 7, 11, 15, 22]
(%i3) num_partitions (n);
(%o3)                   num_partitions(n)
```

<!-- category: Other -->
<!-- keywords: partition_set -->
<!-- signatures: partition_set(a, f) -->
### Function: partition_set (a, f)

Partições do conjunto *a* que satisfazem o predicado *f*.


`partition_set` retorna uma lista de dois conjuntos.
O primeiro conjunto compreende os elementos de *a* para os quais *f* avalia para `false`,
e o segundo conjunto compreende quaisquer outros elementos de *a*.
`partition_set` não aplica `is` ao valor de retorno de *f*.


`partition_set` reclama se *a* não for um conjunto literal.


Veja também `subset`.


Exemplos:







```maxima
(%i1) partition_set ({2, 7, 1, 8, 2, 8}, evenp);
(%o1)                   [{1, 7}, {2, 8}]
(%i2) partition_set ({x, rat(y), rat(y) + z, 1}, lambda ([x], ratp(x)));
(%o2)/R/              [{1, x}, {y, y + z}]
```

<!-- category: Other -->
<!-- keywords: permutations -->
<!-- signatures: permutations(a) -->
### Function: permutations (a)

Retorna um conjunto todas as permutações distintas dos elementos da 
lista ou do conjunto *a*. Cada permutação é uma lista, não um conjunto. 


Quando *a* for uma lista, elementos duplicados de *a* são incluídos
nas permutações.


`permutations` reclama se *a* não for um conjunto literal ou uma lista literal.


Exemplos:







```maxima
(%i1) permutations ([a, a]);
(%o1)                       {[a, a]}
(%i2) permutations ([a, a, b]);
(%o2)           {[a, a, b], [a, b, a], [b, a, a]}
```

<!-- category: Other -->
<!-- keywords: powerset -->
<!-- signatures: powerset(a), powerset(a, n) -->
### Function: powerset (a)

Retorna o conjunto de todos os dubconjuntos de *a*, ou um subconjunto de *a*.


`powerset(a)` retorna o conjunto de todos os subconjuntos do conjunto *a*.
`powerset(a)` tem `2^cardinality(a)` elementos.


`powerset(a, n)` retorna o conjunto de todos os subconjuntos de *a* que possuem 
cardinalidade *n*.


`powerset` reclama se *a* não for um conjunto literal,
ou se *n* não for um inteiro não negativo.


Exemplos:











```maxima
(%i1) powerset ({a, b, c});
(%o1) {{}, {a}, {a, b}, {a, b, c}, {a, c}, {b}, {b, c}, {c}}
(%i2) powerset ({w, x, y, z}, 4);
(%o2)                    {{w, x, y, z}}
(%i3) powerset ({w, x, y, z}, 3);
(%o3)     {{w, x, y}, {w, x, z}, {w, y, z}, {x, y, z}}
(%i4) powerset ({w, x, y, z}, 2);
(%o4)   {{w, x}, {w, y}, {w, z}, {x, y}, {x, z}, {y, z}}
(%i5) powerset ({w, x, y, z}, 1);
(%o5)                 {{w}, {x}, {y}, {z}}
(%i6) powerset ({w, x, y, z}, 0);
(%o6)                         {{}}
```

<!-- category: Other -->
<!-- keywords: rreduce -->
<!-- signatures: rreduce(F, s), rreduce(F, s, s_{n + 1}) -->
### Function: rreduce (F, s)

Extende a função de dois argumentos *F* para uma função de *n* argumentos usando composição de funções,
onde *s* é uma lista.


`rreduce(F, s)` retorna `F(s_1, ... F(s_{n - 2}, F(s_{n - 1}, s_n)))`.
Quando o argumento opcional *s_{n + 1}* estiver presente,
o resultado é equivalente a `rreduce(F, endcons(s_{n + 1}, s))`.


A função *F* é primeiro aplicada à
lista de elementos *mais à direita - rightmost*, daí o nome "rreduce". 


Veja também `lreduce`, `tree_reduce`, e `xreduce`.


Exemplos:


`rreduce` sem o argumento opcional.







```maxima
(%i1) rreduce (f, [1, 2, 3]);
(%o1)                     f(1, f(2, 3))
(%i2) rreduce (f, [1, 2, 3, 4]);
(%o2)                  f(1, f(2, f(3, 4)))
```


`rreduce` com o argumento opcional.






```maxima
(%i1) rreduce (f, [1, 2, 3], 4);
(%o1)                  f(1, f(2, f(3, 4)))
```


`rreduce` aplicada a operadores de dois argumentos internos ( definidos por padrão) ao Maxima.
`/` é o operadro de divisão.







```maxima
(%i1) rreduce ("^", args ({a, b, c, d}));
                                 d
                                c
                               b
(%o1)                         a
(%i2) rreduce ("/", args ({a, b, c, d}));
                               a c
(%o2)                          ---
                               b d
```

<!-- category: Other -->
<!-- keywords: set_partitions -->
<!-- signatures: set_partitions(a), set_partitions(a, n) -->
### Function: set_partitions (a)

Retorna o conjunto de todas as partições de *a*, ou um subconjunto daquele conjunto de partições.


`set_partitions(a, n)` retorna um conjunto de todas as
decomposições de *a* em *n* subconjutnos disjuntos não vazios.


`set_partitions(a)` retorna o conjunto de todas as partições.


`stirling2` retorna a cardinalidade de um conjuntode partições de um conjunto.


Um conjunto de conjuntos $P$ é uma partição de um conjunto $S$ quando



1. cada elemento de $P$ é um conjunto não vazio,
2. elementos distintos de $P$ são disjuntos,
3. a união dos elementos de $P$ é igual a $S$.


Exemplos:


O conjunto vazio é uma partição de si mesmo, as ondições 1 e 2 são "vaziamente" verdadeiras.






```maxima
(%i1) set_partitions ({});
(%o1)                         {{}}
```


A cardinalidade do conjunto de partições de um conjunto pode ser encontrada usando `stirling2`.








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) cardinality(p) = stirling2 (6, 3);
(%o3)                        90 = 90
```


Cada elemento de `p` pode ter *n* = 3 elementos; vamos verificar.








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (cardinality, p);
(%o3)                          {3}
```


Finalmente, para cada elementos de `p`, a união de seus elementos possivelmente será 
igua a `s`; novamente vamos comprovar.








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (lambda ([x], apply (union, listify (x))), p);
(%o3)                 {{0, 1, 2, 3, 4, 5}}
```

<!-- category: Other -->
<!-- keywords: setdifference -->
<!-- signatures: setdifference(a, b) -->
### Function: setdifference (a, b)

Retorna um conjunto contendo os elementos no conjunto *a* que
não estãono conjunto *b*.


`setdifference` reclama se ou *a* ou *b* não for um conjunto literal.


Exemplos:












```maxima
(%i1) S_1 : {a, b, c, x, y, z};
(%o1)                  {a, b, c, x, y, z}
(%i2) S_2 : {aa, bb, c, x, y, zz};
(%o2)                 {aa, bb, c, x, y, zz}
(%i3) setdifference (S_1, S_2);
(%o3)                       {a, b, z}
(%i4) setdifference (S_2, S_1);
(%o4)                     {aa, bb, zz}
(%i5) setdifference (S_1, S_1);
(%o5)                          {}
(%i6) setdifference (S_1, {});
(%o6)                  {a, b, c, x, y, z}
(%i7) setdifference ({}, S_1);
(%o7)                          {}
```

<!-- category: Other -->
<!-- keywords: setequalp -->
<!-- signatures: setequalp(a, b) -->
### Function: setequalp (a, b)

Retorna `true` se os conjuntos *a* e *b* possuirem o mesmo número de elementos


e `is(x = y)` for `true`
para `x` nos elementos de *a*
e `y` nos elementos de *b*,
considerados na ordem determinada por `listify`.
De outra forma, `setequalp` retorna `false`.


Exemplos:








```maxima
(%i1) setequalp ({1, 2, 3}, {1, 2, 3});
(%o1)                         true
(%i2) setequalp ({a, b, c}, {1, 2, 3});
(%o2)                         false
(%i3) setequalp ({x^2 - y^2}, {(x + y) * (x - y)});
(%o3)                         false
```

<!-- category: Other -->
<!-- keywords: setify -->
<!-- signatures: setify(a) -->
### Function: setify (a)

Constrói um conjunto de elementos a partir da lista *a*. Elementos
duplicados da lista *a* são apagados e os elementos
são ordenados de acordo com o predicado `orderlessp`.


`setify` reclama se *a* não for uma lista literal.


Exemplos:








```maxima
(%i1) setify ([1, 2, 3, a, b, c]);
(%o1)                  {1, 2, 3, a, b, c}
(%i2) setify ([a, b, c, a, b, c]);
(%o2)                       {a, b, c}
(%i3) setify ([7, 13, 11, 1, 3, 9, 5]);
(%o3)                {1, 3, 5, 7, 9, 11, 13}
```

<!-- category: Other -->
<!-- keywords: setp -->
<!-- signatures: setp(a) -->
### Function: setp (a)

Retorna `true` se e somente se *a* for um conjunto na interpretação do Maxima.


`setp` retorna `true` para conjuntos não simplificados (isto é, conjuntos com elementos redundantes)
e também para conjuntos simplificados.



`setp` é equivalente à função do Maxima
`setp(a) := not atom(a) and op(a) = 'set`.


Exemplos:








```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) {a, a, a};
(%o2)                       {a, a, a}
(%i3) setp (%);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: some -->
<!-- signatures: some(f, a), some(f, L_1, ..., L_n) -->
### Function: some (f, a)

Retorna `true` se o predicado *f* for `true` para um ou mais argumentos dados.


Given one set as the second argument, 
`some(f, s)` returns `true`
if `is(f(a_i))` returns `true` for one or more *a_i* in *s*.
`some` may or may not evaluate *f* for all *a_i* in *s*.
Since sets are unordered,
`some` may evaluate `f(a_i)` in any order.


Dadas uma ou mais listas como argumentos,
`some(f, L_1, ..., L_n)` retorna `true`
se `is(f(x_1, ..., x_n))` retornar `true` 
para um ou mais *x_1*, ..., *x_n* em *L_1*, ..., *L_n*, respectivamente.
`some` pode ou não avaliar 
*f* para algumas combinações *x_1*, ..., *x_n*.
`some` avalia listas na ordem do índice de incremento.


Dado um conjunto vazio `{}` ou uma lista vazia `[]` como argumentos,
`some` retorna `false`.


Quando o sinalizador global `maperror` for `true`, todas as listas
*L_1*, ..., *L_n* devem ter obrigatóriamente comprimentos iguais.
Quando `maperror` for `false`, argumentos do tipo lista são
efectivamente truncados para o comprimento da menor lista. 


Retorna o valor de um predicado *f* o qual avalia (por meio de `is`)
para alguma coisa outra que não `true` ou `false`
e são governados pelo sinalizador global `prederror`.
Quando `prederror` for `true`,
tais valores são tratados como `false`.
Quando `prederror` for `false`,
tais valores são tratados como `unknown` (desconhecidos).


Exemplos:


`some` aplicado a um conjunto simples.
O predicado é uma função de um argumento.







```maxima
(%i1) some (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) some (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         true
```


`some` aplicada a duas listas.
O predicado é uma função de dois argumentos.







```maxima
(%i1) some ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) some ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Retorna o valor do predicado *f* o qual avalia
para alguma coisa que não `true` ou `false`
e são governados através do sinalizador global `prederror`.












```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z], [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o4)                         true
(%i5) prederror : true;
(%o5)                         true
(%i6) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o6)                         false
(%i7) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o7)                         true
```

<!-- category: Other -->
<!-- keywords: stirling1 -->
<!-- signatures: stirling1(n, m) -->
### Function: stirling1 (n, m)

Representa o número de Stirling de primeiro tipo.


Quando *n* e *m* forem não negativos 
inteiros, a magnitude de `stirling1 (n, m)` é o número de 
permutações de um conjunto com *n* elementos que possui *m* ciclos.
Para detalhes, veja Graham, Knuth e Patashnik *Concrete Mathematics*.
Maxima utiliza uma relação recursiva para definir `stirling1 (n, m)` para
*m* menor que 0; `stirling1` não é definida para *n* menor que 0 e para argumentos
não inteiros.


`stirling1` é uma função de simplificação.
Maxima conhece as seguintes identidades:




1. $stirling1(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling1(n, n) = 1$ (Ref. [1])
3. $stirling1(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling1(n + 1, 0) = 0$ (Ref. [1])
5. $stirling1(n + 1, 1) = n!$ (Ref. [1])
6. $stirling1(n + 1, 2) = 2^n - 1$ (Ref. [1])


Essas identidades são aplicadas quando os argumentos forem inteiros literais
ou símbolos declarados como inteiros, e o primeiro argumento for não negativo.
`stirling1` não simplififca para argumentos não inteiros.


Referências:


[1] Donald Knuth, *The Art of Computer Programming,*
terceira edição, Volume 1, Seção 1.2.6, Equações 48, 49, e 50.


Exemplos:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n, n);
(%o3)                           1
```


`stirling1` não simplifica para argumentos não inteiros.






```maxima
(%i1) stirling1 (sqrt(2), sqrt(2));
(%o1)              stirling1(sqrt(2), sqrt(2))
```


Maxima aplica identidades a `stirling1`.









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n + 1, n);
                            n (n + 1)
(%o3)                       ---------
                                2
(%i4) stirling1 (n + 1, 1);
(%o4)                          n!
```

<!-- category: Other -->
<!-- keywords: stirling2 -->
<!-- signatures: stirling2(n, m) -->
### Function: stirling2 (n, m)

Representa o número de Stirling de segundo tipo.


Quando *n* e *m* forem inteiros
não negativos, `stirling2 (n, m)` é o número de maneiras através dos quais um conjunto com
cardinalidade *n* pode ser particionado em *m* subconjuntos disjuntos.
Maxima utiliza uma relação recursiva para definir `stirling2 (n, m)` para
*m* menor que 0; `stirling2` é indefinida para *n* menor que 0 e para argumentos
não inteiros.


`stirling2` é uma função de simplificação.
Maxima conhece as seguintes identidades.




1. $stirling2(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling2(n, n) = 1$ (Ref. [1])
3. $stirling2(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling2(n + 1, 1) = 1$ (Ref. [1])
5. $stirling2(n + 1, 2) = 2^n - 1$ (Ref. [1])
6. $stirling2(n, 0) = kron_delta(n, 0)$ (Ref. [2])
7. $stirling2(n, m) = 0$ when $m > n$ (Ref. [2])
8. $stirling2(n, m) = sum((-1)^(m - k) binomial(m k) k^n,i,1,m) / m!$
onde $m$ e $n$ são inteiros, e $n$ é não negativo. (Ref. [3])


Essas identidades são aplicadas quando os argumentos forem inteiros literais
ou símbolos declarados como inteiros, e o primeiro argumento for não negativo.
`stirling2` não simplifica para argumentos não inteiros.


Referências:


[1] Donald Knuth. *The Art of Computer Programming*,
terceira edição, Volume 1, Seção 1.2.6, Equações 48, 49, e 50.


[2] Graham, Knuth, e Patashnik. *Concrete Mathematics*, Tabela 264.


[3] Abramowitz e Stegun. *Handbook of Mathematical Functions*, Seção 24.1.4.


Exemplos:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n, n);
(%o3)                           1
```


`stirling2` não simplifica para argumentos não inteiros.






```maxima
(%i1) stirling2 (%pi, %pi);
(%o1)                  stirling2(%pi, %pi)
```


Maxima aplica identidades a `stirling2`.









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n + 9, n + 8);
                         (n + 8) (n + 9)
(%o3)                    ---------------
                                2
(%i4) stirling2 (n + 1, 2);
                              n
(%o4)                        2  - 1
```

<!-- category: Other -->
<!-- keywords: subset -->
<!-- signatures: subset(a, f) -->
### Function: subset (a, f)

Retorna o subconjuntode um conjunto *a* que satisfaz o predicado *f*. 


`subset` returns um conjunto which comprises the elements of *a*
for which *f* returns anything other than `false`.
`subset` does not apply `is` to the return value of *f*.


`subset` reclama se *a* não for um conjunto literal.


See also `partition_set`.


Exemplos:







```maxima
(%i1) subset ({1, 2, x, x + y, z, x + y + z}, atom);
(%o1)                     {1, 2, x, z}
(%i2) subset ({1, 2, 7, 8, 9, 14}, evenp);
(%o2)                      {2, 8, 14}
```

<!-- category: Other -->
<!-- keywords: subsetp -->
<!-- signatures: subsetp(a, b) -->
### Function: subsetp (a, b)

Retorna `true` se e somente se o conjunto *a* for um subconjunto de *b*.


`subsetp` reclama se ou *a* ou *b* não forem um conjunto literal.


Exemplos:







```maxima
(%i1) subsetp ({1, 2, 3}, {a, 1, b, 2, c, 3});
(%o1)                         true
(%i2) subsetp ({a, 1, b, 2, c, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: symmdifference -->
<!-- signatures: symmdifference(a_1, ..., a_n) -->
### Function: symmdifference (a_1, ..., a_n)

Retorna a diferença simétrica, isto é,
o conjunto dos elemetnos que ocorrem em exactamente um conjunto *a_k*.


Given two arguments, `symmdifference(a, b)` is
the same as `union(setdifference(a, b), setdifference(b, a))`.


`symmdifference` reclama se any argument não for um conjunto literal.


Exemplos:













```maxima
(%i1) S_1 : {a, b, c};
(%o1)                       {a, b, c}
(%i2) S_2 : {1, b, c};
(%o2)                       {1, b, c}
(%i3) S_3 : {a, b, z};
(%o3)                       {a, b, z}
(%i4) symmdifference ();
(%o4)                          {}
(%i5) symmdifference (S_1);
(%o5)                       {a, b, c}
(%i6) symmdifference (S_1, S_2);
(%o6)                        {1, a}
(%i7) symmdifference (S_1, S_2, S_3);
(%o7)                        {1, z}
(%i8) symmdifference ({}, S_1, S_2, S_3);
(%o8)                        {1, z}
```

<!-- category: Other -->
<!-- keywords: tree_reduce -->
<!-- signatures: tree_reduce(F, s), tree_reduce(F, s, s_0) -->
### Function: tree_reduce (F, s)

Extende a função binária *F* a uma função enária através de composição,
onde *s* é um conjunto ou uma lista.


`tree_reduce` é equivalente ao seguinte:
Aplicar *F* a sucessivos pares de elementos
para formar uma nova lista `[F(s_1, s_2), F(s_3, s_4), ...]`,
mantendo o elemento final inalterado caso haja um número ímpar de elementos.
Repetindo então o processo até que a lista esteja reduzida a um elemento simples, o qual é o valor de retorno da função.


Quando o argumento opcional *s_0* estiver presente,
o resultado é equivalente a `tree_reduce(F, cons(s_0, s)`.


Para adições em ponto flutuante,
`tree_reduce` pode retornar uma soma que possui um menor ero de arredondamento
que `rreduce` ou `lreduce`.


Os elementos da lista *s* e os resultados parciais podem ser arranjados em uma árvore binária de profundidade mínima,
daí o nome "tree_reduce".


Exemplos:


`tree_reduce` aplicada a uma lista com um número par de elementos.






```maxima
(%i1) tree_reduce (f, [a, b, c, d]);
(%o1)                  f(f(a, b), f(c, d))
```


`tree_reduce` aplicada a uma lista com um número ímpar de elementos.






```maxima
(%i1) tree_reduce (f, [a, b, c, d, e]);
(%o1)               f(f(f(a, b), f(c, d)), e)
```

<!-- category: Other -->
<!-- keywords: union -->
<!-- signatures: union(a_1, ..., a_n) -->
### Function: union (a_1, ..., a_n)

Retorna a união dos conjuntos de *a_1* a *a_n*. 


`union()` (sem argumentos) retorna o conjunto vazio.


`union` reclama se qualquer argumento não for um conjunto literal.


Exemplos:













```maxima
(%i1) S_1 : {a, b, c + d, %e};
(%o1)                   {%e, a, b, d + c}
(%i2) S_2 : {%pi, %i, %e, c + d};
(%o2)                 {%e, %i, %pi, d + c}
(%i3) S_3 : {17, 29, 1729, %pi, %i};
(%o3)                {17, 29, 1729, %i, %pi}
(%i4) union ();
(%o4)                          {}
(%i5) union (S_1);
(%o5)                   {%e, a, b, d + c}
(%i6) union (S_1, S_2);
(%o6)              {%e, %i, %pi, a, b, d + c}
(%i7) union (S_1, S_2, S_3);
(%o7)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
(%i8) union ({}, S_1, S_2, S_3);
(%o8)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
```

<!-- category: Other -->
<!-- keywords: xreduce -->
<!-- signatures: xreduce(F, s), xreduce(F, s, s_0) -->
### Function: xreduce (F, s)

Extendendo a função *F* para uma função enária por composição,
ou, se *F* já for enária, aplica-se *F* a *s*.
Quando *F* não for enária, `xreduce` funciona da mesma forma que `lreduce`.
O argumento *s* é uma lista.


Funções sabidamente enárias inclui
adição `+`, multiplicação `*`, `and`, `or`, `max`,
`min`, e `append`.
Funções podem também serem declaradas enárias por meio de `declare(F, nary)`.
Para essas funções,
é esperado que `xreduce` seja mais rápida que ou `rreduce` ou `lreduce`.


Quando o argumento opcional *s_0* estiver presente,
o resultado é equivalente a `xreduce(s, cons(s_0, s))`.




Adições em ponto flutuante não são exactamente associativas; quando a associatividade ocorrer,
`xreduce` aplica a adição enária do Maxima quando *s* contiver números em ponto flutuante.


Exemplos:


`xreduce` aplicada a uma função sabidamente enária.
`F` é chamada uma vez, com todos os argumentos.








```maxima
(%i1) declare (F, nary);
(%o1)                         done
(%i2) F ([L]) := L;
(%o2)                      F([L]) := L
(%i3) xreduce (F, [a, b, c, d, e]);
(%o3)         [[[[[("[", simp), a], b], c], d], e]
```


`xreduce` aplicada a uma função não sabidamente enária.
`G` é chamada muitas vezes, com dois argumentos de cada vez.








```maxima
(%i1) G ([L]) := L;
(%o1)                      G([L]) := L
(%i2) xreduce (G, [a, b, c, d, e]);
(%o2)         [[[[[("[", simp), a], b], c], d], e]
(%i3) lreduce (G, [a, b, c, d, e]);
(%o3)                 [[[[a, b], c], d], e]
```

