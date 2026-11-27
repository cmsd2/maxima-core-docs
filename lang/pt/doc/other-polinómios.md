## Polinómios

<!-- category: Other -->
<!-- keywords: algebraic -->
<!-- signatures: algebraic -->
### Variable: algebraic

Valor Padrão: `false`


`algebraic` deve ser escolhida para `true` com o objectivo de que a
simplificação de inteiros algébricos tenha efeito.

<!-- category: Other -->
<!-- keywords: berlefact -->
<!-- signatures: berlefact -->
### Variable: berlefact

Valor Padrão: `true`


Quando `berlefact` for `false` então o algoritmo de factorização de
Kronecker será usado.  De outra forma o algoritmo de Berlekamp, que é o
padrão, será usado.

<!-- category: Other -->
<!-- keywords: bezout -->
<!-- signatures: bezout(p1, p2, x) -->
### Function: bezout (p1, p2, x)

uma alternativa para o comando `resultant`.  Isso
retorna uma matriz.  `determinant` dessa matriz é o resultante desejado.

<!-- category: Other -->
<!-- keywords: bothcoef -->
<!-- signatures: bothcoef(expr, x) -->
### Function: bothcoef (expr, x)

Retorna uma lista da qual o primeiro membro é o
coeficiente de *x* em *expr* (como achado por `ratcoef` se *expr* está na forma CRE
de outro modo por `coeff`) e cujo segundo membro é a parte restante de
*expr*.  Isto é, `[A, B]` onde `expr = A*x + B`.


Exemplo:








```maxima
(%i1) islinear (expr, x) := block ([c],
        c: bothcoef (rat (expr, x), x),
        é (freeof (x, c) and c[1] # 0))$
(%i2) islinear ((r^2 - (x - r)^2)/x, x);
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: coeff -->
<!-- signatures: coeff(expr, x, n) -->
### Function: coeff (expr, x, n)

Retorna o coeficiente de `x^n` em *expr*.  *n* pode ser
omitido se for 1.  *x* pode ser um átomo, ou subexpressão completa de
*expr* e.g., `sin(x)`, `a[i+1]`, `x + y`, etc. (No último caso a
expressão `(x + y)` pode ocorrer em *expr*).  Algumas vezes isso pode ser necessário
para expandir ou factorizar *expr* com o objectivo de fazer `x^n` explicito.  Isso não é
realizado por `coeff`.


Exemplos:






```maxima
(%i1) coeff (2*a*tan(x) + tan(x) + b = 5*tan(x) + 3, tan(x));
(%o1)                      2 a + 1 = 5
(%i2) coeff (y + x*%e^x + 1, x, 0);
(%o2)                         y + 1
```

<!-- category: Other -->
<!-- keywords: combine -->
<!-- signatures: combine(expr) -->
### Function: combine (expr)

Simplifica a adição *expr* por termos combinados com o mesmo
denominador dentro de um termo simples.

<!-- category: Other -->
<!-- keywords: content -->
<!-- signatures: content(p_1, x_1, ..., x_n) -->
### Function: content (p_1, x_1, ..., x_n)

Retorna uma lista cujo primeiro elemento é
o máximo divisor comum dos coeficientes dos termos do
polinómio *p_1* na variável *x_n* (isso é o conteúdo) e cujo
segundo elemento é o polinómio *p_1* dividido pelo conteúdo.




Exemplos:





```maxima
(%i1) content (2*x*y + 4*x^2*y^2, y);
                                   2
(%o1)                   [2 x, 2 x y  + y]
```

<!-- category: Other -->
<!-- keywords: denom -->
<!-- signatures: denom(expr) -->
### Function: denom (expr)

Retorna o denominador da expressão racional *expr*.

<!-- category: Other -->
<!-- keywords: divide -->
<!-- signatures: divide(p_1, p_2, x_1, ..., x_n) -->
### Function: divide (p_1, p_2, x_1, ..., x_n)

calcula o quocietne e o resto
do polinómio *p_1* dividido pelo polinómio *p_2*, na variável
principal do polinómio, *x_n*.

As outras variáveis são como na função `ratvars`.
O resultado é uma lista cujo primeiro elemento é o quociente
e cujo segundo elemento é o resto.


Exemplos:






```maxima
(%i1) divide (x + y, x - y, x);
(%o1)                       [1, 2 y]
(%i2) divide (x + y, x - y);
(%o2)                      [- 1, 2 x]
```



Note que `y` é a variável principal no segundo exemplo.

<!-- category: Other -->
<!-- keywords: eliminate -->
<!-- signatures: eliminate([eqn_1, ..., eqn_n], [x_1, ..., x_k]) -->
### Function: eliminate ([eqn_1, ..., eqn_n], [x_1, ..., x_k])

Elimina variáveis de
equações (ou expressões assumidas iguais a zero) obtendo resultantes
sucessivos. Isso retorna uma lista de `n - k` expressões com *k*
variáveis *x_1*, ..., *x_k* eliminadas.  Primeiro *x_1* é eliminado retornando `n - 1`
expressões, então `x_2` é eliminado, etc.  Se `k = n` então uma expressão simples em uma
lista é retornada livre das variáveis *x_1*, ..., *x_k*.  Nesse caso `solve`
é chamado para resolver a última resultante para a última variável.


Exemplo:








```maxima
(%i1) expr1: 2*x^2 + y*x + z;
                                      2
(%o1)                    z + x y + 2 x
(%i2) expr2: 3*x + 5*y - z - 1;
(%o2)                  - z + 5 y + 3 x - 1
(%i3) expr3: z^2 + x - y^2 + 5;
                          2    2
(%o3)                    z  - y  + x + 5
(%i4) eliminate ([expr3, expr2, expr1], [y, z]);
             8         7         6          5          4
(%o4) [7425 x  - 1170 x  + 1299 x  + 12076 x  + 22887 x

                                    3         2
                            - 5154 x  - 1291 x  + 7688 x + 15376]
```

<!-- category: Other -->
<!-- keywords: ezgcd -->
<!-- signatures: ezgcd(p_1, p_2, p_3, ...) -->
### Function: ezgcd (p_1, p_2, p_3, ...)

Retorna uma lista cujo primeiro elemento é o m.d.c. dos
polinómios *p_1*, *p_2*, *p_3*, ...  e cujos restantes elementos são os
polinómios divididos pelo mdc.  Isso sempre usa o algoritmo
`ezgcd`.

<!-- category: Other -->
<!-- keywords: facexpand -->
<!-- signatures: facexpand -->
### Variable: facexpand

Valor Padrão: `true`


`facexpand` controla se os factores irredutíveis
retornados por `factor` estão na forma expandida (o padrão) ou na forma recursiva
(CRE normal).

<!-- category: Other -->
<!-- keywords: factcomb -->
<!-- signatures: factcomb(expr) -->
### Function: factcomb (expr)

Tenta combinar os coeficientes de factoriais em *expr*
com os próprios factoriais convertendo, por exemplo, `(n + 1)*n!`
em `(n + 1)!`.


`sumsplitfact` se escolhida para `false` fará com que `minfactorial` seja
aplicado após um `factcomb`.

<!-- category: Other -->
<!-- keywords: factor -->
<!-- signatures: factor(expr), factor(expr, p) -->
### Function: factor (expr)

Factoriza a expressão *expr*, contendo qualquer número de
variáveis ou funções, em factores irredutíveis sobre os inteiros.
`factor (expr, p)` factoriza *expr* sobre o campo dos inteiros com um elemento
adjunto cujo menor polinómio é *p*.


`factor` usa a função `ifactors` para factorizar inteiros.


`factorflag` se `false` suprime a factorização de factores inteiros
de expressões racionais.


`dontfactor` pode ser escolhida para uma lista de variáveis com relação à qual
factorização não é para ocorrer.  (Essa é inicialmente vazia).  Factorização também
não acontece com relação a quaisquer variáveis que são menos
importantes (usando a ordenação de variável assumida pela forma CRE) como
essas na lista `dontfactor`.


`savefactors` se `true` faz com que os factores de uma expressão que
é um produto de factores seja guardada por certas funções com o objectivo de
aumentar a velocidade de futuras factorizações de expressões contendo alguns dos
mesmos factores.


`berlefact` se `false` então o algoritmo de factorização de Kronecker será
usado de outra forma o algoritmo de Berlekamp, que é o padrão, será
usado.


`intfaclim` se `true` maxima irá interromper a factorização de
inteiros se nenhum factor for encontrado após tentar divisões e o método rho de
Pollard.  Se escolhida para `false` (esse é o caso quando o utilizador chama
`factor` explicitamente), a factorização completa do inteiro será
tentada.  A escolha do utilizador para `intfaclim` é usada para chamadas
internas a `factor`. Dessa forma, `intfaclim` pode ser resetada para evitar que o
Maxima gaste um tempo muito longo factorizando inteiros grandes.


Exemplos:




















```maxima
(%i1) factor (2^63 - 1);
                    2
(%o1)              7  73 127 337 92737 649657
(%i2) factor (-8*y - 4*x + z^2*(2*y + x));
(%o2)               (2 y + x) (z - 2) (z + 2)
(%i3) -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2;
                2  2        2    2    2
(%o3)          x  y  + 2 x y  + y  - x  - 2 x - 1
(%i4) block ([dontfactor: [x]], factor (%/36/(1 + 2*y + y^2)));
                       2
                     (x  + 2 x + 1) (y - 1)
(%o4)                ----------------------
                           36 (y + 1)
(%i5) factor (1 + %e^(3*x));
                      x         2 x     x
(%o5)              (%e  + 1) (%e    - %e  + 1)
(%i6) factor (1 + x^4, a^2 - 2);
                    2              2
(%o6)             (x  - a x + 1) (x  + a x + 1)
(%i7) factor (-y^2*z^2 - x*z^2 + x^2*y^2 + x^3);
                       2
(%o7)              - (y  + x) (z - x) (z + x)
(%i8) (2 + x)/(3 + x)/(b + x)/(c + x)^2;
                             x + 2
(%o8)               ------------------------
                                           2
                    (x + 3) (x + b) (x + c)
(%i9) ratsimp (%);
                4                  3
(%o9) (x + 2)/(x  + (2 c + b + 3) x

     2                       2             2                   2
 + (c  + (2 b + 6) c + 3 b) x  + ((b + 3) c  + 6 b c) x + 3 b c )
(%i10) partfrac (%, x);
           2                   4                3
(%o10) - (c  - 4 c - b + 6)/((c  + (- 2 b - 6) c

     2              2         2                2
 + (b  + 12 b + 9) c  + (- 6 b  - 18 b) c + 9 b ) (x + c))

                 c - 2
 - ---------------------------------
     2                             2
   (c  + (- b - 3) c + 3 b) (x + c)

                         b - 2
 + -------------------------------------------------
             2             2       3      2
   ((b - 3) c  + (6 b - 2 b ) c + b  - 3 b ) (x + b)

                         1
 - ----------------------------------------------
             2
   ((b - 3) c  + (18 - 6 b) c + 9 b - 27) (x + 3)
(%i11) map ('factor, %);
              2
             c  - 4 c - b + 6                 c - 2
(%o11) - ------------------------- - ------------------------
                2        2                                  2
         (c - 3)  (c - b)  (x + c)   (c - 3) (c - b) (x + c)

                       b - 2                        1
            + ------------------------ - ------------------------
                             2                          2
              (b - 3) (c - b)  (x + b)   (b - 3) (c - 3)  (x + 3)
(%i12) ratsimp ((x^5 - 1)/(x - 1));
                       4    3    2
(%o12)                x  + x  + x  + x + 1
(%i13) subst (a, x, %);
                       4    3    2
(%o13)                a  + a  + a  + a + 1
(%i14) factor (%th(2), %);
                       2        3        3    2
(%o14)   (x - a) (x - a ) (x - a ) (x + a  + a  + a + 1)
(%i15) factor (1 + x^12);
                       4        8    4
(%o15)               (x  + 1) (x  - x  + 1)
(%i16) factor (1 + x^99);
                 2            6    3
(%o16) (x + 1) (x  - x + 1) (x  - x  + 1)

   10    9    8    7    6    5    4    3    2
 (x   - x  + x  - x  + x  - x  + x  - x  + x  - x + 1)

   20    19    17    16    14    13    11    10    9    7    6
 (x   + x   - x   - x   + x   + x   - x   - x   - x  + x  + x

    4    3            60    57    51    48    42    39    33
 - x  - x  + x + 1) (x   + x   - x   - x   + x   + x   - x

    30    27    21    18    12    9    3
 - x   - x   + x   + x   - x   - x  + x  + 1)
```

<!-- category: Other -->
<!-- keywords: factorflag -->
<!-- signatures: factorflag -->
### Variable: factorflag

Valor Padrão: `false`



Quando `factorflag` for `false`, suprime a factorização de
factores inteiros em expressões racionais.

<!-- category: Other -->
<!-- keywords: factorout -->
<!-- signatures: factorout(expr, x_1, x_2, ...) -->
### Function: factorout (expr, x_1, x_2, ...)

Rearranja a adição *expr* em uma adição de
parcelas da forma `f (x_1, x_2, ...)*g` onde `g` é um produto de
expressões que não possuem qualquer *x_i* e `f` é factorizado.

<!-- category: Other -->
<!-- keywords: factorsum -->
<!-- signatures: factorsum(expr) -->
### Function: factorsum (expr)

Tenta agrupar parcelas em factores de *expr* que são adições
em grupos de parcelas tais que sua adição é factorável.  `factorsum` pode
recuperar o resultado de `expand ((x + y)^2 + (z + w)^2)` mas não pode recuperar
`expand ((x + 1)^2 + (x + y)^2)` porque os termos possuem variáveis em comum.


Exemplo:






```maxima
(%i1) expand ((x + 1)*((u + v)^2 + a*(w + z)^2));
           2      2                            2      2
(%o1) a x z  + a z  + 2 a w x z + 2 a w z + a w  x + v  x

                                     2        2    2            2
                        + 2 u v x + u  x + a w  + v  + 2 u v + u
(%i2) factorsum (%);
                                   2          2
(%o2)            (x + 1) (a (z + w)  + (v + u) )
```

<!-- category: Other -->
<!-- keywords: fasttimes -->
<!-- signatures: fasttimes(p_1, p_2) -->
### Function: fasttimes (p_1, p_2)

Retorna o produto dos polinómios *p_1* e *p_2* usando um
algoritmo especial para a multiplicação de polinómios.  `p_1` e `p_2` podem ser
de várias variáveis, densos, e aproximadamente do mesmo tamanho.  A multiplicação
clássica é de ordem `n_1 n_2` onde
`n_1` é o grau de `p_1`
and `n_2` é o grau de `p_2`.
`fasttimes` é da ordem `max (n_1, n_2)^1.585`.

<!-- category: Other -->
<!-- keywords: fullratsimp -->
<!-- signatures: fullratsimp(expr) -->
### Function: fullratsimp (expr)

`fullratsimp` aplica
repetidamente `ratsimp` seguido por simplificação não racional a uma
expressão até que nenhuma mudança adicional ocorra,
e retorna o resultado.


Quando expressões não racionais estão envolvidas, uma chamada
a `ratsimp` seguida como é usual por uma simplificação não racional
("geral") pode não ser suficiente para retornar um resultado simplificado.
Algumas vezes, mais que uma tal chamada pode ser necessária. 
`fullratsimp` faz esse processo convenientemente.


`fullratsimp (expr, x_1, ..., x_n)` aceita um ou
mais argumentos similar a `ratsimp` e `rat`.


Exemplo:








```maxima
(%i1) expr: (x^(a/2) + 1)^2*(x^(a/2) - 1)^2/(x^a - 1);
                       a/2     2   a/2     2
                     (x    - 1)  (x    + 1)
(%o1)                -----------------------
                              a
                             x  - 1
(%i2) ratsimp (expr);
                          2 a      a
                         x    - 2 x  + 1
(%o2)                    ---------------
                              a
                             x  - 1
(%i3) fullratsimp (expr);
                              a
(%o3)                        x  - 1
(%i4) rat (expr);
                       a/2 4       a/2 2
                     (x   )  - 2 (x   )  + 1
(%o4)/R/             -----------------------
                              a
                             x  - 1
```

<!-- category: Other -->
<!-- keywords: fullratsubst -->
<!-- signatures: fullratsubst(a, b, c) -->
### Function: fullratsubst (a, b, c)

é o mesmo que `ratsubst` excepto que essa chama
a si mesma recursivamente sobre esse resultado até que o resultado para de mudar.
Essa função é útil quando a expressão de substituição e a
expressão substituída tenham uma ou mais variáveis em comum.


`fullratsubst` irá também aceitar seus argumentos no formato de
`lratsubst`.  Isto é, o primeiro argumento pode ser uma substituição simples
de equação ou uma lista de tais equações, enquanto o segundo argumento é a
expressão sendo processada.


`load ("lrats")` chama `fullratsubst` e `lratsubst`.


Exemplos:














```maxima
(%i1) load ("lrats")$
```


- *
`subst` pode realizar multiplas substituições.
`lratsubst` é analogo a `subst`.


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
Se somente uma substituição é desejada, então uma equação
simples pode ser dada como primeiro argumento.


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```


- *
`fullratsubst` é equivalente a `ratsubst`
excepto que essa executa recursivamente até que seu resultado para de mudar.


```maxima
(%i5) ratsubst (b*a, a^2, a^3);
                               2
(%o5)                         a  b
(%i6) fullratsubst (b*a, a^2, a^3);
                                 2
(%o6)                         a b
```


- *
`fullratsubst` também aceita uma lista de equações ou uma equação
simples como primeiro argumento.


```maxima
(%i7) fullratsubst ([a^2 = b, b^2 = c, c^2 = a], a^3*b*c);
(%o7)                           b
(%i8) fullratsubst (a^2 = b*a, a^3);
                                 2
(%o8)                         a b
```


- *
`fullratsubst` pode causar uma recursão infinita.


```maxima
(%i9) errcatch (fullratsubst (b*a^2, a^2, a^3));

*** - Lisp stack overflow. RESET
```

<!-- category: Other -->
<!-- keywords: gcd -->
<!-- signatures: gcd(p_1, p_2, x_1, ...) -->
### Function: gcd (p_1, p_2, x_1, ...)

Retorna o máximo divisor comum entre *p_1* e *p_2*.
O sinalizador `gcd` determina qual algoritmo é empregado.
Escolhendo `gcd` para `ez`, `subres`, `red`, ou `spmod` selecciona o algoritmo `ezgcd`,
subresultante `prs`, reduzido, ou modular,
respectivamente.  Se `gcd` for `false` então `gcd (p_1, p_2, x)` sempre retorna 1
para todo *x*.  Muitas funções (e.g.  `ratsimp`, `factor`, etc.) fazem com que mdc’s
sejam feitos implicitamente.  Para polinómios homogêneos é recomendado
que `gcd` igual a `subres` seja usado.  Para obter o mdc quando uma expressão algébrica está
presente, e.g. `gcd (x^2 - 2*sqrt(2)*x + 2, x - sqrt(2))`, `algebraic` deve ser
`true` e `gcd` não deve ser `ez`.  `subres` é um novo algoritmo, e pessoas
que tenham estado usando a opção `red` podem provavelmente alterar isso para
`subres`.


O sinalizador `gcd`, padrão: `subres`, se `false` irá também evitar o máximo
divisor comum de ser usado quando expressões são convertidas para a forma de expressão racional
canónica (CRE).  Isso irá algumas vezes aumentar a velocidade dos cálculos se mdc’s não são
requeridos.

<!-- category: Other -->
<!-- keywords: gcdex -->
<!-- signatures: gcdex(f, g), gcdex(f, g, x) -->
### Function: gcdex (f, g)

Retornam uma lista `[a, b, u]`
onde *u* é o máximo divisor comum (mdc) entre *f* e *g*,
e *u* é igual a `a f + b g`.
Os argumentos *f* e *g* podem ser polinómios de uma variável,
ou de outra forma polinómios em *x* uma **main**(principal) variável suprida
desde que nós precisamos estar em um domínio de ideal principal para isso trabalhar.
O mdc significa o mdc considerando *f* e *g* como polinómios de uma única variável com coeficientes
sendo funções racionais em outras variáveis.


`gcdex` implementa o algoritmo Euclideano,
onde temos a sequência
of `L[i]: [a[i], b[i], r[i]]` que são todos perpendiculares
a `[f, g, -1]` e o próximo se é construído como
se `q = quotient(r[i]/r[i+1])` então `L[i+2]: L[i] - q L[i+1]`, e isso
encerra em `L[i+1]` quando o resto `r[i+2]` for zero.







```maxima
(%i1) gcdex (x^2 + 1, x^3 + 4);
                       2
                      x  + 4 x - 1  x + 4
(%o1)/R/           [- ------------, -----, 1]
                           17        17
(%i2) % . [x^2 + 1, x^3 + 4, -1];
(%o2)/R/                        0
```



Note que o mdc adiante é `1`
uma vez que trabalhamos em `k(y)[x]`, o `y+1` não pode ser esperado em `k[y, x]`.






```maxima
(%i1) gcdex (x*(y + 1), y^2 - 1, x);
                               1
(%o1)/R/                 [0, ------, 1]
                              2
                             y  - 1
```

<!-- category: Other -->
<!-- keywords: gcfactor -->
<!-- signatures: gcfactor(n) -->
### Function: gcfactor (n)

Factoriza o inteiro Gaussiano *n* sobre os inteiros Gaussianos, i.e.,
números da forma `a + b %i` onde *a* e *b* são inteiros raconais
(i.e.,  inteiros comuns).  Factorizações são normalizadas fazendo *a* e *b*
não negativos.

<!-- category: Other -->
<!-- keywords: gfactor -->
<!-- signatures: gfactor(expr) -->
### Function: gfactor (expr)

Factoriza o polinómio *expr* sobre os inteiros de Gauss
(isto é, os inteiros com a unidade imaginária `%i` adjunta).

Isso é como `factor (expr, a^2+1)` trocando *a* por `%i`.


Exemplo:





```maxima
(%i1) gfactor (x^4 - 1);
(%o1)           (x - 1) (x + 1) (x - %i) (x + %i)
```

<!-- category: Other -->
<!-- keywords: gfactorsum -->
<!-- signatures: gfactorsum(expr) -->
### Function: gfactorsum (expr)

é similar a `factorsum` mas aplica `gfactor` em lugar
de `factor`.

<!-- category: Other -->
<!-- keywords: hipow -->
<!-- signatures: hipow(expr, x) -->
### Function: hipow (expr, x)

Retorna o maior expoente explícito de *x* em *expr*.
*x* pode ser uma variável ou uma expressão geral.
Se *x* não aparece em *expr*,
`hipow` retorna `0`.


`hipow` não considera expressões equivalentes a `expr`.
Em particular, `hipow` não expande `expr`,
então `hipow (expr, x)` e `hipow (expand (expr, x))`
podem retornar diferentes resultados.


Exemplos:



```maxima
(%i1) hipow (y^3 * x^2 + x * y^4, x);
(%o1)                           2
(%i2) hipow ((x + y)^5, x);
(%o2)                           1
(%i3) hipow (expand ((x + y)^5), x);
(%o3)                           5
(%i4) hipow ((x + y)^5, x + y);
(%o4)                           5
(%i5) hipow (expand ((x + y)^5), x + y);
(%o5)                           0
```

<!-- category: Other -->
<!-- keywords: intfaclim -->
<!-- signatures: intfaclim -->
### Variable: intfaclim

Valor por omissão: true


Se `true`, maxima irá interromper a factorização de
inteiros se nenhum factor for encontrado após tentar divisões e o método rho de
Pollard e a factorização não será completada.


Quando `intfaclim` for `false` (esse é o caso quando o utilizador
chama `factor` explicitamente), a factorização completa será
tentada.  `intfaclim` é escolhida para `false` quando factores são
calculados em `divisors`, `divsum` e `totient`.




Chamadas internas a `factor` respeitam o valor especificado pelo utilizador para
`intfaclim`. Setting `intfaclim` to `true` may reduce
`intfaclim`.  Escolhendo `intfaclim` para `true` podemos reduzir
o tempo gasto factorizando grandes inteiros.

<!-- category: Other -->
<!-- keywords: keepfloat -->
<!-- signatures: keepfloat -->
### Variable: keepfloat

Valor Padrão: `false`


Quando `keepfloat` for `true`, evitamos que números
em ponto flutuante sejam racionalizados quando expressões que os possuem
são então convertidas para a forma de expressão racional canónica (CRE).

<!-- category: Other -->
<!-- keywords: lratsubst -->
<!-- signatures: lratsubst(L, expr) -->
### Function: lratsubst (L, expr)

é análogo a `subst (L, expr)`
excepto que esse usa `ratsubst` em lugar de `subst`.


O primeiro argumento de
`lratsubst` é uma equação ou uma lista de equações idênticas em
formato para que sejam aceitas por `subst`.  As
substituições são feitas na ordem dada pela lista de equações,
isto é, da esquerda para a direita.


`load ("lrats")` chama `fullratsubst` e `lratsubst`.


Exemplos:









```maxima
(%i1) load ("lrats")$
```


- *
`subst` pode realizar multiplas substituições.
`lratsubst` é analoga a `subst`.


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
Se somente uma substituição for desejada, então uma equação
simples pode ser dada como primeiro argumento.


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```

<!-- category: Other -->
<!-- keywords: modulus -->
<!-- signatures: modulus -->
### Variable: modulus

Valor Padrão: `false`


Quando `modulus` for um número positivo *p*,
operações sobre os números racionais (como retornado por `rat` e funções relacionadas)
são realizadas módulo *p*,
usando o então chamado sistema de módulo "balanceado"
no qual `n módulo p` é definido como 
um inteiro *k* em `[-(p-1)/2, ..., 0, ..., (p-1)/2]`
quando *p* for ímpar, ou `[-(p/2 - 1), ..., 0, ...., p/2]` quando *p* for par,
tal que `a p + k` seja igual a *n* para algum inteiro *a*.





Se *expr* já estiver na forma de expressão racional canónica
(CRE) quando `modulus` for colocado no seu valor original, então
pode precisar repetir o rat *expr*, e.g., `expr: rat (ratdisrep (expr))`, com o objectivo de obter resultados correctos.


Tipicamente `modulus` é escolhido para um número primo.
Se `modulus` for escolhido para um inteiro não primo positivo,
essa escolha é aceita, mas uma mensagem de alerta é mostrada.
Maxima permitirá que zero ou um inteiro negativo seja atribuído a `modulus`,
embora isso não seja limpo se aquele tiver quaisquer consequências úteis.

<!-- category: Other -->
<!-- keywords: num -->
<!-- signatures: num(expr) -->
### Function: num (expr)

Retorna o numerador de *expr* se isso for uma razão.
Se *expr* não for uma razão, *expr* é retornado.


`num` avalia seu argumento.

<!-- category: Other -->
<!-- keywords: polydecomp -->
<!-- signatures: polydecomp(p, x) -->
### Function: polydecomp (p, x)

Decompões o polinómio *p* na variável  *x*
em uma composição funcional de polinómios em *x*.
`polydecomp` retorna uma lista `[p_1, ..., p_n]` tal que



```maxima
lambda ([x], p_1) (lambda ([x], p_2) (... (lambda ([x], p_n) (x)) ...))
```


seja igual a *p*.
O grau de *p_i* é maior que 1 para *i* menor que *n*.


Tal decomposição não é única.


Exemplos:








```maxima
(%i1) polydecomp (x^210, x);
                          7   5   3   2
(%o1)                   [x , x , x , x ]
(%i2) p : expand (subst (x^3 - x - 1, x, x^2 - a));
                6      4      3    2
(%o2)          x  - 2 x  - 2 x  + x  + 2 x - a + 1
(%i3) polydecomp (p, x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


As seguintes funções compõem `L = [e_1, ..., e_n]` como funções em `x`;
essa funçào é a inversa de `polydecomp`:







```maxima
compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $
```


Re-exprimindo o exemplo acima usando `compose`:






```maxima
(%i3) polydecomp (compose ([x^2 - a, x^3 - x - 1], x), x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


Note que apesar de `compose (polydecomp (p, x), x)`
sempre retornar *p* (não expandido),
`polydecomp (compose ([p_1, ..., p_n], x), x)` *não*
necessáriamente retorna `[p_1, ..., p_n]`:







```maxima
(%i4) polydecomp (compose ([x^2 + 2*x + 3, x^2], x), x);
                          2       2
(%o4)                   [x  + 2, x  + 1]
(%i5) polydecomp (compose ([x^2 + x + 1, x^2 + x + 1], x), x);
                      2       2
                     x  + 3  x  + 5
(%o5)               [------, ------, 2 x + 1]
                       4       2
```

<!-- category: Other -->
<!-- keywords: quotient -->
<!-- signatures: quotient(p_1, p_2), quotient(p_1, p_2, x_1, ..., x_n) -->
### Function: quotient (p_1, p_2)

Retorna o polinómio *p_1* dividido pelo polinómio *p_2*.
Os argumentos *x_1*, ..., *x_n* são interpretados como em `ratvars`.


`quotient` retorna o primeiro elemento de uma lista de dois elementos retornada por `divide`.

<!-- category: Other -->
<!-- keywords: rat -->
<!-- signatures: rat(expr), rat(expr, x_1, ..., x_n) -->
### Function: rat (expr)

Converte *expr* para a forma de expressão racional canónica (CRE) expandindo e
combinando todos os termos sobre um denominador comum e cancelando para fora o
máximo divisor comum entre o numerador e o denominador, também
convertendo números em ponto flutuante para números racionais dentro da
tolerância de `ratepsilon`.
As variáveis são ordenadas de acordo com
*x_1*, ..., *x_n*, se especificado, como em `ratvars`.


`rat` geralmente não simplifica funções outras que não sejam
adição `+`, subtração `-`, multiplicação `*`, divisão `/`, e
exponenciação com expoente inteiro,
uma vez que `ratsimp` não manuseia esses casos.
Note que átomos (números e variáveis) na forma CRE não são os
mesmos que eles são na forma geral.
Por exemplo, `rat(x)- x` retorna 
`rat(0)` que tem uma representação interna diferente de 0.



Quando `ratfac` for `true`, `rat` retorna uma forma parcialmente factorizada para CRE.
Durante operações racionais a expressão é
mantida como totalmente factorizada como possível sem uma chamada ao
pacote de factorização (`factor`).  Isso pode sempre economizar espaço de memória e algum tempo
em algumas computações.  O numerador e o denominador são ainda tidos como
relativamente primos
(e.g.  `rat ((x^2 - 1)^4/(x + 1)^2)` retorna `(x - 1)^4 (x + 1)^2)`,
mas os factores dentro de cada parte podem não ser relativamente primos.


`ratprint` se `false` suprime a impressão de mensagens
informando o utilizador de conversões de números em ponto flutuante para
números racionais.


`keepfloat` se `true` evita que números em ponto flutuante sejam
convertidos para números racionais.


Veja também `ratexpand` e  `ratsimp`.


Exemplos:






```maxima
(%i1) ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x) /(4*y^2 + x^2);
                                           4
                                  (x - 2 y)
              (y + a) (2 y + x) (------------ + 1)
                                   2      2 2
                                 (x  - 4 y )
(%o1)         ------------------------------------
                              2    2
                           4 y  + x
(%i2) rat (%, y, a, x);
                            2 a + 2 y
(%o2)/R/                    ---------
                             x + 2 y
```

<!-- category: Other -->
<!-- keywords: ratalgdenom -->
<!-- signatures: ratalgdenom -->
### Variable: ratalgdenom

Valor Padrão: `true`


Quando `ratalgdenom` for `true`, permite racionalização de
denominadores com respeito a radicais tenham efeito.
`ratalgdenom` tem efeito somente quando expressões racionais canónicas (CRE) forem usadas no modo algébrico.

<!-- category: Other -->
<!-- keywords: ratcoef -->
<!-- signatures: ratcoef(expr, x, n), ratcoef(expr, x) -->
### Function: ratcoef (expr, x, n)

Retorna o coeficiente da expressão `x^n`
dentro da expressão *expr*.
Se omitido, *n* é assumido ser 1.


O valor de retorno está livre
(excepto possivelmente em um senso não racional) das variáveis em *x*.
Se nenhum coeficiente desse tipo existe, 0 é retornado.


`ratcoef`
expande e simplifica racionalmente seu primeiro argumento e dessa forma pode
produzir respostas diferentes das de `coeff` que é puramente
sintática.

Dessa forma `ratcoef ((x + 1)/y + x, x)` retorna `(y + 1)/y` ao passo que `coeff` retorna 1.


`ratcoef (expr, x, 0)`, visualiza *expr* como uma adição,
retornando uma soma desses termos que não possuem *x*.

portanto se *x* ocorre para quaisquer expoentes negativos, `ratcoef` pode não ser usado.



Uma vez que *expr* é racionalmente
simplificada antes de ser examinada, coeficientes podem não aparecer inteiramente
no caminho que eles foram pensados.


Exemplo:






```maxima
(%i1) s: a*x + b*x + 5$
(%i2) ratcoef (s, a + b);
(%o2)                           x
```

<!-- category: Other -->
<!-- keywords: ratdenom -->
<!-- signatures: ratdenom(expr) -->
### Function: ratdenom (expr)

Retorna o denominador de *expr*,
após forçar a conversão de *expr* para expressão racional canónica (CRE).
O valor de retorno é a CRE.



*expr* é forçada para uma CRE por `rat`
se não for já uma CRE.
Essa conversão pode mudar a forma de *expr* colocando todos os termos
sobre um denominador comum.


`denom` é similar, mas retorna uma expressão comum em lugar de uma CRE.
Também, `denom` não tenta colocar todos os termos sobre um denominador comum,
e dessa forma algumas expressões que são consideradas razões por `ratdenom`
não são consideradas razões por `denom`.

<!-- category: Other -->
<!-- keywords: ratdenomdivide -->
<!-- signatures: ratdenomdivide -->
### Variable: ratdenomdivide

Valor Padrão: `true`


Quando `ratdenomdivide` for `true`,
`ratexpand` expande uma razão cujo o numerador for uma adição 
dentro de uma soma de razões,
tendo todos um denominador comum.
De outra forma, `ratexpand` colapsa uma adição de razões dentro de uma razão simples,
cujo numerador seja a adição dos numeradores de cada razão.


Exemplos:



```maxima
(%i1) expr: (x^2 + x + 1)/(y^2 + 7);
                            2
                           x  + x + 1
(%o1)                      ----------
                              2
                             y  + 7
(%i2) ratdenomdivide: true$
(%i3) ratexpand (expr);
                       2
                      x        x        1
(%o3)               ------ + ------ + ------
                     2        2        2
                    y  + 7   y  + 7   y  + 7
(%i4) ratdenomdivide: false$
(%i5) ratexpand (expr);
                            2
                           x  + x + 1
(%o5)                      ----------
                              2
                             y  + 7
(%i6) expr2: a^2/(b^2 + 3) + b/(b^2 + 3);
                                     2
                           b        a
(%o6)                    ------ + ------
                          2        2
                         b  + 3   b  + 3
(%i7) ratexpand (expr2);
                                  2
                             b + a
(%o7)                        ------
                              2
                             b  + 3
```

<!-- category: Other -->
<!-- keywords: ratdiff -->
<!-- signatures: ratdiff(expr, x) -->
### Function: ratdiff (expr, x)

Realiza a derivação da expressão racional *expr* com relação a *x*.
*expr* deve ser uma razão de polinómios ou um polinómio em *x*.
O argumento *x* pode ser uma variável ou uma subexpressão de *expr*.





O resultado é equivalente a `diff`, embora talvez em uma forma diferente.
`ratdiff` pode ser mais rápida que `diff`, para expressões racionais.


`ratdiff` retorna uma expressão racional canónica (CRE) se `expr` for uma CRE.
De outra forma, `ratdiff` retorna uma expressão geral.


`ratdiff` considera somente as dependências de *expr* sobre *x*,
e ignora quaisquer dependências estabelecidas por `depends`.







Exemplo:










```maxima
(%i1) expr: (4*x^3 + 10*x - 11)/(x^5 + 5);
                           3
                        4 x  + 10 x - 11
(%o1)                   ----------------
                              5
                             x  + 5
(%i2) ratdiff (expr, x);
                    7       5       4       2
                 8 x  + 40 x  - 55 x  - 60 x  - 50
(%o2)          - ---------------------------------
                          10       5
                         x   + 10 x  + 25
(%i3) expr: f(x)^3 - f(x)^2 + 7;
                         3       2
(%o3)                   f (x) - f (x) + 7
(%i4) ratdiff (expr, f(x));
                           2
(%o4)                   3 f (x) - 2 f(x)
(%i5) expr: (a + b)^3 + (a + b)^2;
                              3          2
(%o5)                  (b + a)  + (b + a)
(%i6) ratdiff (expr, a + b);
                    2                    2
(%o6)            3 b  + (6 a + 2) b + 3 a  + 2 a
```

<!-- category: Other -->
<!-- keywords: ratdisrep -->
<!-- signatures: ratdisrep(expr) -->
### Function: ratdisrep (expr)

Retorna seu argumento como uma expressão geral.
Se *expr* for uma expressão geral, é retornada inalterada.


Tipicamente `ratdisrep` é chamada para converter uma expressão racional canónica (CRE)
em uma expressão geral.

Isso é algumas vezes conveniente se deseja-se parar o "contágio", ou
caso se esteja usando funções racionais em contextos não racionais.


Veja também `totaldisrep`.

<!-- category: Other -->
<!-- keywords: ratepsilon -->
<!-- signatures: ratepsilon -->
### Variable: ratepsilon

Valor Padrão: 2.0e-8


`ratepsilon` é a tolerância usada em conversões
de números em ponto flutuante para números racionais.

<!-- category: Other -->
<!-- keywords: ratexpand -->
<!-- signatures: ratexpand(expr) -->
### Function: ratexpand (expr)

Expande *expr* multiplicando para fora produtos de somas e
somas exponenciadas, combinando frações sobre um denominador comum,
cancelando o máximo divisor comum entre entre o numerador e o
denominador, então quebrando o numerador (se for uma soma) dentro de suas
respectivas parcelas divididas pelo denominador.


O valor de retorno de `ratexpand` é uma expressão geral,
mesmo se *expr* for uma expressão racional canónica (CRE).



O comutador `ratexpand` se `true` fará com que expressões
CRE sejam completamente expandidas quando forem convertidas de volta para
a forma geral ou mostradas, enquanto se for `false` então elas serão colocadas
na forma recursiva.
Veja também `ratsimp`.


Quando `ratdenomdivide` for `true`,
`ratexpand` expande uma razão na qual o numerador é uma adição
dentro de uma adição de razões,
todas tendo um denominador comum.
De outra forma, `ratexpand` contrai uma soma de razões em uma razão simples,
cujo numerador é a soma dos numeradores de cada razão.


Quando `keepfloat` for `true`, evita que números
em ponto flutuante sejam racionalizados quando expressões que contenham
números em ponto flutuante forem convertidas para a forma de expressão racional canónica (CRE).


Exemplos:








```maxima
(%i1) ratexpand ((2*x - 3*y)^3);
                     3         2       2        3
(%o1)          - 27 y  + 54 x y  - 36 x  y + 8 x
(%i2) expr: (x - 1)/(x + 1)^2 + 1/(x - 1);
                         x - 1       1
(%o2)                   -------- + -----
                               2   x - 1
                        (x + 1)
(%i3) expand (expr);
                    x              1           1
(%o3)          ------------ - ------------ + -----
                2              2             x - 1
               x  + 2 x + 1   x  + 2 x + 1
(%i4) ratexpand (expr);
                        2
                     2 x                 2
(%o4)           --------------- + ---------------
                 3    2            3    2
                x  + x  - x - 1   x  + x  - x - 1
```

<!-- category: Other -->
<!-- keywords: ratfac -->
<!-- signatures: ratfac -->
### Variable: ratfac

Valor Padrão: `false`


Quando `ratfac` for `true`,
expressões racionais canónicas (CRE) são manipuladas na forma parcialmente factorizada.


Durante operações racionais a
expressão é mantida como completamente factorizada como foi possível sem chamadas a `factor`.
Isso pode sempre economizar espaço e pode economizar tempo em algumas computações.
O numerador e o denominador são feitos relativamente primos, por exemplo
`rat ((x^2 - 1)^4/(x + 1)^2)` retorna `(x - 1)^4 (x + 1)^2)`,
mas o factor dentro de cada parte pode não ser relativamente primo.


No pacote `ctensor` (Manipulação de componentes de tensores),
tensores de Ricci, Einstein, Riemann, e de Weyl e a curvatura escalar 
são factorizados automaticamente quando `ratfac` for `true`.
*`ratfac` pode somente ser
escolhido para casos onde as componentes tensoriais sejam sabidametne consistidas de
poucos termos.*


Os esquemas de `ratfac` e de `ratweight` são incompatíveis e não podem
ambos serem usados ao mesmo tempo.

<!-- category: Other -->
<!-- keywords: ratnumer -->
<!-- signatures: ratnumer(expr) -->
### Function: ratnumer (expr)

Retorna o numerador de *expr*,
após forçar *expr* para uma expressão racional canónica (CRE).
O valor de retorno é uma CRE.



*expr* é forçada para uma CRE por `rat`
se isso não for já uma CRE.
Essa conversão pode alterar a forma de *expr* pela colocação de todos os termos
sobre um denominador comum.


`num` é similar, mas retorna uma expressão comum em lugar de uma CRE.
Também, `num` não tenta colocar todos os termos sobre um denominador comum,
e dessa forma algumas expressões que são consideradas razões por `ratnumer`
não são consideradas razões por `num`.

<!-- category: Other -->
<!-- keywords: ratnump -->
<!-- signatures: ratnump(expr) -->
### Function: ratnump (expr)

Retorna `true` se *expr* for um inteiro literal ou razão de inteiros literais,
de outra forma retorna `false`.

<!-- category: Other -->
<!-- keywords: ratp -->
<!-- signatures: ratp(expr) -->
### Function: ratp (expr)

Retorna `true` se *expr* for uma expressão racional canónica (CRE) ou CRE extendida,
de outra forma retorna `false`.


CRE são criadas por `rat` e funções relacionadas.
CRE extendidas são criadas por `taylor` e funções relacionadas.

<!-- category: Other -->
<!-- keywords: ratprint -->
<!-- signatures: ratprint -->
### Variable: ratprint

Valor Padrão: `true`


Quando `ratprint` for `true`,
uma mensagem informando ao utilizador da conversão de números em ponto flutuante
para números racionais é mostrada.

<!-- category: Other -->
<!-- keywords: ratsimp -->
<!-- signatures: ratsimp(expr), ratsimp(expr, x_1, ..., x_n) -->
### Function: ratsimp (expr)

Simplifica a expressão *expr* e todas as suas subexpressões,
incluindo os argumentos para funções não racionais.
O resultado é retornado como o quociente de dois polinómios na forma recursiva,
isto é, os coeficientes de variável principal são polinómios em outras variáveis.
Variáveis podem incluir funções não racionais (e.g., `sin (x^2 + 1)`)
e os argumentos para quaisquer tais funções são também simplificados racionalmente.


`ratsimp (expr, x_1, ..., x_n)`
habilita simplificação racional com a
especiicação de variável ordenando como em `ratvars`.


Quando `ratsimpexpons` for `true`,
`ratsimp` é aplicado para os expoentes de expressões durante a simplificação.


Veja também `ratexpand`.
Note que `ratsimp` é afectado por algum dos
sinalizadores que afectam `ratexpand`.


Exemplos:









```maxima
(%i1) sin (x/(x^2 + x)) = exp ((log(x) + 1)^2 - log(x)^2);
                                         2      2
                   x         (log(x) + 1)  - log (x)
(%o1)        sin(------) = %e
                  2
                 x  + x
(%i2) ratsimp (%);
                             1          2
(%o2)                  sin(-----) = %e x
                           x + 1
(%i3) ((x - 1)^(3/2) - (x + 1)*sqrt(x - 1))/sqrt((x - 1)*(x + 1));
                       3/2
                (x - 1)    - sqrt(x - 1) (x + 1)
(%o3)           --------------------------------
                     sqrt((x - 1) (x + 1))
(%i4) ratsimp (%);
                           2 sqrt(x - 1)
(%o4)                    - -------------
                                 2
                           sqrt(x  - 1)
(%i5) x^(a + 1/a), ratsimpexpons: true;
                               2
                              a  + 1
                              ------
                                a
(%o5)                        x
```

<!-- category: Other -->
<!-- keywords: ratsimpexpons -->
<!-- signatures: ratsimpexpons -->
### Variable: ratsimpexpons

Valor Padrão: `false`


Quando `ratsimpexpons` for `true`,
`ratsimp` é aplicado para os expoentes de expressões durante uma simplificação.

<!-- category: Other -->
<!-- keywords: ratsubst -->
<!-- signatures: ratsubst(a, b, c) -->
### Function: ratsubst (a, b, c)

Substitue *a* por *b* em *c* e retorna a expressão resultante. 

*b* pode também ser uma adição, produto, expoente, etc.



`ratsubst` sabe alguma coisa do significado de expressões
uma vez que `subst` não é uma substituição puramente sintática.
Dessa forma `subst (a, x + y, x + y + z)` retorna `x + y + z`
ao passo que `ratsubst` retorna `z + a`.


Quando `radsubstflag` for `true`,
`ratsubst` faz substituição de radicais em expressões
que explicitamente não possuem esses radicais.


Exemplos:













```maxima
(%i1) ratsubst (a, x*y^2, x^4*y^3 + x^4*y^8);
                              3      4
(%o1)                      a x  y + a
(%i2) cos(x)^4 + cos(x)^3 + cos(x)^2 + cos(x) + 1;
               4         3         2
(%o2)       cos (x) + cos (x) + cos (x) + cos(x) + 1
(%i3) ratsubst (1 - sin(x)^2, cos(x)^2, %);
            4           2                     2
(%o3)    sin (x) - 3 sin (x) + cos(x) (2 - sin (x)) + 3
(%i4) ratsubst (1 - cos(x)^2, sin(x)^2, sin(x)^4);
                        4           2
(%o4)                cos (x) - 2 cos (x) + 1
(%i5) radsubstflag: false$
(%i6) ratsubst (u, sqrt(x), x);
(%o6)                           x
(%i7) radsubstflag: true$
(%i8) ratsubst (u, sqrt(x), x);
                                2
(%o8)                          u
```

<!-- category: Other -->
<!-- keywords: ratvars -->
<!-- signatures: ratvars(x_1, ..., x_n), ratvars() -->
### Function: ratvars (x_1, ..., x_n)

Declara variáveis principais *x_1*, ..., *x_n* para expressões racionais.
*x_n*, se presente em uma expressão racional, é considerada a variável principal.
De outra forma, *x_[n-1]* é considerada a variável principal se presente,
e assim por diante até as variáveis precedentes para *x_1*,
que é considerada a variável principal somente se nenhuma das variáveis que a sucedem estiver presente.


Se uma variável em uma expressão racional não está presente na lista `ratvars`,
a ela é dada uma prioridade menor que *x_1*.


Os argumentos para `ratvars` podem ser ou variáveis ou funções não racionais
tais como `sin(x)`.


A variável `ratvars` é uma lista de argumentos da
função `ratvars` quando ela foi chamada mais recentemente.
Cada chamada para a função `ratvars` sobre-grava a lista apagando seu conteúdo anterior.
`ratvars ()` limpa a lista.

<!-- category: Other -->
<!-- keywords: ratweight -->
<!-- signatures: ratweight(x_1, w_1, ..., x_n, w_n), ratweight() -->
### Function: ratweight (x_1, w_1, ..., x_n, w_n)

Atribui um peso *w_i* para a variável *x_i*.
Isso faz com que um termo seja substituído por 0 se seu peso exceder o
valor da variável `ratwtlvl` (o padrão retorna sem truncação).
O peso de um termo é a soma dos produtos dos
pesos de uma variável no termo vezes seu expoente.
Por exemplo, o peso de `3 x_1^2 x_2` é `2 w_1 + w_2`.
A truncação de acordo com `ratwtlvl` é realizada somente quando multiplicando
ou exponencializando expressões racionais canónicas (CRE).


`ratweight ()` retorna a lista cumulativa de atribuições de pesos.


Nota: Os esquemas de `ratfac` e `ratweight` são incompatíveis e não podem
ambo serem usados ao mesmo tempo.


Exemplos:









```maxima
(%i1) ratweight (a, 1, b, 1);
(%o1)                     [a, 1, b, 1]
(%i2) expr1: rat(a + b + 1)$
(%i3) expr1^2;
                  2                  2
(%o3)/R/         b  + (2 a + 2) b + a  + 2 a + 1
(%i4) ratwtlvl: 1$
(%i5) expr1^2;
(%o5)/R/                  2 b + 2 a + 1
```

<!-- category: Other -->
<!-- keywords: ratweights -->
<!-- signatures: ratweights -->
### Variable: ratweights

Valor Padrão: `[]`


`ratweights` é a lista de pesos atribuídos por `ratweight`.
A lista é cumulativa:
cada chamada a `ratweight` coloca ítens adicionais na lista.



`kill (ratweights)` e `save (ratweights)` ambos trabalham como esperado.

<!-- category: Other -->
<!-- keywords: ratwtlvl -->
<!-- signatures: ratwtlvl -->
### Variable: ratwtlvl

Valor Padrão: `false`


`ratwtlvl` é usada em combinação com a função 
`ratweight` para controlar a truncação de expressão racionais canónicas (CRE).
Para o valor padrão `false`, nenhuma truncação ocorre.

<!-- category: Other -->
<!-- keywords: remainder -->
<!-- signatures: remainder(p_1, p_2), remainder(p_1, p_2, x_1, ..., x_n) -->
### Function: remainder (p_1, p_2)

Retorna o resto do polinómio *p_1* dividido pelo polinómio *p_2*.
Os argumentos *x_1*, ..., *x_n* são interpretados como em `ratvars`.


`remainder` retorna o segundo elemento
de uma lista de dois elementos retornada por `divide`.

<!-- category: Other -->
<!-- keywords: resultant -->
<!-- signatures: resultant(p_1, p_2, x) -->
### Function: resultant (p_1, p_2, x)

Calcula o resultante de dois polinómios *p_1* e *p_2*,
eliminando a variável *x*.
O resultante é um determinante dos coeficientes de *x*
em *p_1* e *p_2*,
que é igual a zero
se e somente se *p_1* e *p_2* tiverem um factor em comum não constante.


Se *p_1* ou *p_2* puderem ser factorizados,
pode ser desejável chamar `factor` antes de chamar `resultant`.


A variável `resultant` controla que algoritmo será usado para calcular
o resultante.

`subres` para o prs subresultante,
`mod` para o algoritmo resultante modular,
e `red` para prs reduzido.
Para muitos problemas `subres` pode ser melhor.
Para alguns problemas com valores grandes de grau de uma única variável ou de duas variáveis `mod` pode ser melhor.


A função `bezout` aceita os mesmos argumentos que `resultant` e retorna
uma matriz.  O determinante do valor de retorno é o resultante desejado.

<!-- category: Other -->
<!-- keywords: savefactors -->
<!-- signatures: savefactors -->
### Variable: savefactors

Valor Padrão: `false`



Quando `savefactors` for `true`, faz com que os factores de uma
expressão que é um produto de factores sejam gravados por certas
funções com o objectivo de aumentar a velocidade em posteriores factorizações de expressões
contendo algum desses mesmos factores.

<!-- category: Other -->
<!-- keywords: sqfr -->
<!-- signatures: sqfr(expr) -->
### Function: sqfr (expr)

é similar a `factor` excepto que os factores do polinómio são "livres de raízes".
Isto é, eles possuem factores somente de grau um.
Esse algoritmo, que é também usado no primeiro estágio de `factor`, utiliza
o facto que um polinómio tem em comum com sua n’ésima derivada todos
os seus factores de grau maior que n.  Dessa forma obtendo o maior divisor comum
com o polinómio das
derivadas com relação a cada variável no polinómio, todos
os factores de grau maior que 1 podem ser achados.


Exemplo:





```maxima
(%i1) sqfr (4*x^4 + 4*x^3 - 3*x^2 - 4*x - 1);
                                2   2
(%o1)                  (2 x + 1)  (x  - 1)
```

<!-- category: Other -->
<!-- keywords: tellrat -->
<!-- signatures: tellrat(p_1, ..., p_n), tellrat() -->
### Function: tellrat (p_1, ..., p_n)

Adiciona ao anel dos inteiros algébricos conhecidos do Maxima
os elementos que são as soluções dos polinómios *p_1*, ..., *p_n*.
Cada argumento *p_i* é um polinómio concoeficientes inteiros.


`tellrat (x)` efectivamente significa substituir 0 por *x* em funções
racionais.


`tellrat ()` retorna uma lista das substituições correntes.


`algebraic` deve ser escolhida para `true` com o objectivo de que a simplificação de
inteiros algébricos tenha efeito.


Maxima inicialmente sabe sobre a unidade imaginária `%i`
e todas as raízes de inteiros.


Existe um comando `untellrat` que recebe núcleos e
remove propriedades `tellrat`.


Quando fazemos `tellrat` em um polinómio
de várias variáveis, e.g., `tellrat (x^2 - y^2)`, pode existir uma ambiguidade como para
ou substituir `y^2` por `x^2`
ou vice-versa.  
Maxima selecciona uma ordenação particular, mas se o utilizador desejar especificar qual e.g.
`tellrat (y^2 = x^2)` forneçe uma sintaxe que diga para substituir
`y^2` por `x^2`.









Exemplos:










```maxima
(%i1) 10*(%i + 1)/(%i + 3^(1/3));
                           10 (%i + 1)
(%o1)                      -----------
                                  1/3
                            %i + 3
(%i2) ev (ratdisrep (rat(%)), algebraic);
             2/3      1/3              2/3      1/3
(%o2)    (4 3    - 2 3    - 4) %i + 2 3    + 4 3    - 2
(%i3) tellrat (1 + a + a^2);
                            2
(%o3)                     [a  + a + 1]
(%i4) 1/(a*sqrt(2) - 1) + a/(sqrt(3) + sqrt(2));
                      1                 a
(%o4)           ------------- + -----------------
                sqrt(2) a - 1   sqrt(3) + sqrt(2)
(%i5) ev (ratdisrep (rat(%)), algebraic);
         (7 sqrt(3) - 10 sqrt(2) + 2) a - 2 sqrt(2) - 1
(%o5)    ----------------------------------------------
                               7
(%i6) tellrat (y^2 = x^2);
                        2    2   2
(%o6)                 [y  - x , a  + a + 1]
```

<!-- category: Other -->
<!-- keywords: totaldisrep -->
<!-- signatures: totaldisrep(expr) -->
### Function: totaldisrep (expr)

Converte toda subexpressão de *expr* da forma de expressão racionais canónicas (CRE) para
a forma geral e retorna o resultado.
Se *expr* é em sí mesma na forma CRE então `totaldisrep` é identica a
`ratdisrep`.


`totaldisrep` pode ser usada para
fazer um `ratdisrep` em expressões tais como equações, listas, matrizes, etc., que
tiverem algumas subexpressões na forma CRE.

<!-- category: Other -->
<!-- keywords: untellrat -->
<!-- signatures: untellrat(x_1, ..., x_n) -->
### Function: untellrat (x_1, ..., x_n)

Remove propriedades `tellrat` de *x_1*, ..., *x_n*.

