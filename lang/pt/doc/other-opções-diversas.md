## Opções Diversas

<!-- category: Other -->
<!-- keywords: aliases -->
<!-- signatures: aliases -->
### Variable: aliases

Valor por omissão: `[]`


`aliases` é a lista de átomos que possuem um alias definido pelo utilizador (escolhido através
das funções `alias`, `ordergreat`, `orderless` ou através da declaração do átomo como sendo um
`noun` (substantivo) com `declare`).

<!-- category: Other -->
<!-- keywords: alphabetic -->
<!-- signatures: alphabetic -->
### Variable: alphabetic

`alphabetic` é uma declaração reconhecida por `declare`.
A expressão `declare(s, alphabetic)` diz ao Maxima para reconhecer
como alfabético todos os caracteres em *s*, que deve ser uma sequência de caracteres.

 

Veja também *Identificadores*.


Exemplo:










```maxima
(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729
(%i2) declare ("~`@", alphabetic);
(%o2)                         done
(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729
(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```

<!-- category: Other -->
<!-- keywords: apropos -->
<!-- signatures: apropos(string) -->
### Function: apropos (string)

Procura por nomes Maxima que possuem *string* aparecendo em qualquer lugar dentro
de seu nome.  Dessa forma, `apropos (exp)` retorna uma lista de todos os sinalizadores
e funções que possuem `exp` como parte de seus nomes, tais como `expand`,
`exp`, e `exponentialize`.  Dessa forma, se lembrar apenas uma
parte do nome
de alguma coisa, pode usar este comando para achar o restante do nome.
Similarmente, pode dizer `apropos (tr_)` para achar uma lista de muitos dos
comutadores relatando para o tradutor, muitos dos quais começam com `tr_`.

<!-- category: Other -->
<!-- keywords: args -->
<!-- signatures: args(expr) -->
### Function: args (expr)

Retorna a lista de argumentos de `expr`,
que pode ser de qualquer tipo de expressão outra como um átomo.
Somente os argumentos do operador de nível mais alto são extraídos;
subexpressões de `expr` aparecem como elementos ou subexpressões de elementos
da lista de argumentos.


A ordem dos ítens na lista pode depender do sinalizador global `inflag`.


`args (expr)` é equivalente a `substpart ("[", expr, 0)`.
Veja também `substpart`.


Veja também `op`.

<!-- category: Other -->
<!-- keywords: genindex -->
<!-- signatures: genindex -->
### Variable: genindex

Valor por omissão: `i`


`genindex` é o prefixo usado para gerar a
próxima variável do somatório quando necessário.

<!-- category: Other -->
<!-- keywords: gensumnum -->
<!-- signatures: gensumnum -->
### Variable: gensumnum

Valor por omissão: 0


`gensumnum` é o sufixo numérico usado para gerar variável seguinte
do somatório.  Se isso for escolhido para `false` então o índice  consistirá somente
de `genindex` com um sufixo numérico.

<!-- category: Other -->
<!-- keywords: infolists -->
<!-- signatures: infolists -->
### Variable: infolists

Valor por omissão: `[]`


`infolists` é uma lista dos nomes de todas as listas de
informação no Maxima. São elas:



**labels** — Todos associam `%i`, `%o`, e rótulos `%t`.
**values** — Todos associam átomos que são variáveis de utilizador, não opções do
Maxima ou comutadores, criados através de `:` ou `::` ou associando funcionalmente.
**functions** — Todas as funções definidas pelo utilizador, criadas através de `:=` ou `define`.
**arrays** — Todos os arrays declarados e não declarados, criados através de `:`, `::`, ou `:=`.
**macros** — Todas as macros definidas pelo utilizador.
**myoptions** — Todas as opções alguma vez alteradas pelo utilizador (mesmo que tenham ou não elas
tenham mais tarde retornadas para seus valores padrão).
**rules** — Todos os modelos definidos pelo utilizador que coincidirem e regras de simplificação, criadas
através de `tellsimp`, `tellsimpafter`, `defmatch`, ou `defrule`.
**aliases** — Todos os átomos que possuem um alias definido pelo utilizador, criado através das funções
`alias`, `ordergreat`, `orderless` ou declarando os átomos como um `noun`
com `declare`.
**dependencies** — Todos os átomos que possuem dependências funcionais, criadas através das
funções `depends` ou `gradef`.
**gradefs** — Todas as funções que possuem derivadas definidas pelo utilizador, cridas através da
função `gradef`.
**props** — Todos os átomos que possuem quaisquer propriedades outras que não essas mencionadas
acima, tais como propriedades estabelecidas por `atvalue` , `matchdeclare`, etc., também propriedades
estabelecidas na função `declare`.
**let_rule_packages** — Todos os pacote de régras em uso definidos pelo utilizador
mais o pacote especial `default_let_rule_package`.
(`default_let_rule_package` é o nome do pacote de régras usado quando
um não está explicitamente escolhido pelo utilizador.)

<!-- category: Other -->
<!-- keywords: integerp -->
<!-- signatures: integerp(expr) -->
### Function: integerp (expr)

Retorna `true` se *expr* é um inteiro numérico literal, de outra forma retorna `false`.


`integerp` retorna falso se seu argumento for um símbolo,
mesmo se o argumento for declarado inteiro.


Exemplos:



```maxima
(%i1) integerp (0);
(%o1)                         true
(%i2) integerp (1);
(%o2)                         true
(%i3) integerp (-17);
(%o3)                         true
(%i4) integerp (0.0);
(%o4)                         false
(%i5) integerp (1.0);
(%o5)                         false
(%i6) integerp (%pi);
(%o6)                         false
(%i7) integerp (n);
(%o7)                         false
(%i8) declare (n, integer);
(%o8)                         done
(%i9) integerp (n);
(%o9)                         false
```

<!-- category: Other -->
<!-- keywords: m1pbranch -->
<!-- signatures: m1pbranch -->
### Variable: m1pbranch

Valor por omissão: `false`


`m1pbranch` é principal descendente de `-1` a um expoente.
Quantidades tais como `(-1)^(1/3)` (isto é, um expoente racional "ímpar") e 
`(-1)^(1/4)` (isto é, um expoente racional "par") são manuseados como segue:




```maxima
domain:real
                            
(-1)^(1/3):      -1         
(-1)^(1/4):   (-1)^(1/4)   

             domain:complex              
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```

<!-- category: Other -->
<!-- keywords: numberp -->
<!-- signatures: numberp(expr) -->
### Function: numberp (expr)

Retorna `true` se *expr* for um inteiro literal, número racional, 
número em ponto flutuante, ou um grande número em ponto flutuante, de outra forma retorna `false`.


`numberp` retorna falso se seu argumento for um símbolo,
mesmo se o argumento for um número simbólico tal como `%pi` ou `%i`,
ou declarado ser 
par, ímpar, inteiro, racional, irracional, real, imaginário, ou complexo.


Exemplos:



```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare (a, even, b, odd, c, integer, d, rational,
     e, irrational, f, real, g, imaginary, h, complex);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e, f, g, h]);
(%o7) [false, false, false, false, false, false, false, false]
```

<!-- category: Other -->
<!-- keywords: properties -->
<!-- signatures: properties(a) -->
### Function: properties (a)

Retorna uma lista de nomes de todas as
propriedades associadas com o átomo *a*.

<!-- category: Other -->
<!-- keywords: props -->
<!-- signatures: props -->
### Variable: props

`props` são átomos que possuem qualquer propriedade outra como essas explicitamente
mencionadas em `infolists`, tais como atvalues, matchdeclares, etc., também
propriedades especificadas na função  `declare`.

<!-- category: Other -->
<!-- keywords: propvars -->
<!-- signatures: propvars(prop) -->
### Function: propvars (prop)

Retorna uma lista desses átomos sobre a lista `props` que
possui a propriedade indicada através de *prop*.  Dessa forma `propvars (atvalue)`
retorna uma lista de átomos que possuem atvalues.

<!-- category: Other -->
<!-- keywords: put -->
<!-- signatures: put(átomo, valor, indicador) -->
### Function: put (átomo, valor, indicador)

Atribui *valor* para a propriedade (especificada através de *indicador*) do *átomo*.
*indicador* pode ser o nome de qualquer propriedade, não apenas uma propriedade definida pelo sistema.


`put` avalia seus argumentos. 
`put` retorna *valor*.


Exemplos:



```maxima
(%i1) put (foo, (a+b)^5, expr);
                                   5
(%o1)                       (b + a)
(%i2) put (foo, "Hello", str);
(%o2)                         Hello
(%i3) properties (foo);
(%o3)            [[user properties, str, expr]]
(%i4) get (foo, expr);
                                   5
(%o4)                       (b + a)
(%i5) get (foo, str);
(%o5)                         Hello
```

<!-- category: Other -->
<!-- keywords: qput -->
<!-- signatures: qput(átomo, valor, indicador) -->
### Function: qput (átomo, valor, indicador)

Atribui *valor* para a propriedade (especificada através de *indicador*) do *átomo*.
Isso é o mesmo que `put`,
excepto que os argumentos nã são avaliados.


Exemplo:



```maxima
(%i1) foo: aa$ 
(%i2) bar: bb$
(%i3) baz: cc$
(%i4) put (foo, bar, baz);
(%o4)                          bb
(%i5) properties (aa);
(%o5)                [[user properties, cc]]
(%i6) get (aa, cc);
(%o6)                          bb
(%i7) qput (foo, bar, baz);
(%o7)                          bar
(%i8) properties (foo);
(%o8)            [value, [user properties, baz]]
(%i9) get ('foo, 'baz);
(%o9)                          bar
```

<!-- category: Other -->
<!-- keywords: rem -->
<!-- signatures: rem(átomo, indicador) -->
### Function: rem (átomo, indicador)

Remove a propriedade indicada através de *indicador* do *átomo*.

<!-- category: Other -->
<!-- keywords: remove -->
<!-- signatures: remove(a_1, p_1, ..., a_n, p_n), remove([a_1, ..., a_m], [p_1, ..., p_n], ...), remove("a", operator), remove(a, transfun), remove(all, p) -->
### Function: remove (a_1, p_1, ..., a_n, p_n)

Remove propriedades associadas a átomos.


`remove (a_1, p_1, ..., a_n, p_n)`
remove a propriedade `p_k` do átomo `a_k`.


`remove ([a_1, ..., a_m], [p_1, ..., p_n], ...)`
remove as propriedades `p_1, ..., p_n`
dos átomos *a_1*, ..., *a_m*.
Pode existir mais que um par de listas.



`remove (all, p)` remove a propriedade *p* de todos os átomos que a possuem.



A propriedade removida pode ser definida pelo sistema tal como
`function`, `macro` ou `mode_declare`, ou propriedades definidas pelo utilizador.




uma propriedade pode ser `transfun` para remover
a versão traduzida Lisp de uma função.
Após executar isso, a versão Maxima da função é executada
em lugar da versão traduzida.


`remove ("a", operator)` ou, equivalentemente, `remove ("a", op)`
remove de *a* as propriedades `operator` declaradas através de
`prefix`, `infix`, `nary`, `postfix`, `matchfix`, ou `nofix`.
Note que o nome do operador deve ser escrito como uma sequência de caracteres com apóstofo.


`remove` sempre retorna `done` se um átomo possui ou não uma propriedade especificada.
Esse comportamento é diferente das funções remove mais específicas
`remvalue`, `remarray`, `remfunction`, e `remrule`.

<!-- category: Other -->
<!-- keywords: remvalue -->
<!-- signatures: remvalue(nome_1, ..., nome_n), remvalue(all) -->
### Function: remvalue (nome_1, ..., nome_n)

Remove os valores de Variáveis de utilizador *nome_1*, ..., *nome_n*
(que podem ser subscritas) do sistema.


`remvalue (all)` remove os valores de todas as variáveis em `values`,
a lista de todas as variáveis nomeadas através do utilizador
(em oposição a essas que são automaticamente atribuídas através do Maxima).


Veja também `values`.

<!-- category: Other -->
<!-- keywords: rncombine -->
<!-- signatures: rncombine(expr) -->
### Function: rncombine (expr)

Transforma *expr* combinando todos os termos de *expr* que possuem
denominadores idênticos ou denominadores que diferem de cada um dos outros apenas por
factores numéricos somente.  Isso é ligeiramente diferente do comportamento de
de `combine`, que colecta termos que possuem denominadores idênticos.


Escolhendo `pfeformat: true` e usando `combine` retorna resultados similares
a esses que podem ser obtidos com `rncombine`, mas `rncombine` pega o
passo adicional de multiplicar cruzado factores numérios do denominador.
Esses resultados em forma ideal, e a possibilidade de reconhecer alguns
cancelamentos.


Para usar essa função escreva primeiramente `load("rncomb")`.

<!-- category: Other -->
<!-- keywords: scalarp -->
<!-- signatures: scalarp(expr) -->
### Function: scalarp (expr)

Retorna `true` se *expr* for um número, constante, ou variável
declarada `scalar` com `declare`, ou composta inteiramente de números, constantes, e tais
Variáveis, bmas não contendo matrizes ou listas.

<!-- category: Other -->
<!-- keywords: setup_autoload -->
<!-- signatures: setup_autoload(nomeficheiro, função_1, ..., função_n) -->
### Function: setup_autoload (nomeficheiro, função_1, ..., função_n)

Especifica que
se qualquer entre *função_1*, ..., *função_n* for referenciado e não ainda definido,
*nomedeqrquivo* é chamado via `load`.
*nomeficheiro* usualmente contém definições para as funções especificadas,
embora isso não seja obrigatório.


`setup_autoload` não trabalha para funções array.


`setup_autoload` não avalia seus argumentos.


Exemplo:









```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma função ultraspherical
Warning - you are redefining the Macsyma função legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);
                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

