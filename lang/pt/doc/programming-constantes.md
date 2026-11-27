## Constantes

<!-- category: Programming -->
<!-- keywords: %e -->
<!-- signatures: %e -->
### Variable: %e

`%e` representa a base do logaritmo natural, também conhecido como constante de Euler.
O valor numérico de `%e` é um número em ponto flutuante de precisão dupla 2.718281828459045d0.

<!-- category: Programming -->
<!-- keywords: %i -->
<!-- signatures: %i -->
### Variable: %i

`%i` representa a unidade imaginária, $sqrt(- 1)$.

<!-- category: Programming -->
<!-- keywords: %phi -->
<!-- signatures: %phi -->
### Variable: %phi

`%phi` representa o então chamado *número áureo*,
$(1 + sqrt(5))/2$.
O valor numérico de `%phi` é o número em ponto flutuante de de dupla precisão 1.618033988749895d0.


`fibtophi` expressa números de Fibonacci `fib(n)` em termos de `%phi`.


Por padrão, Maxima não conhece as propriedade algébricas de `%phi`.
Após avaliar `tellrat(%phi^2 - %phi - 1)` e `algebraic: true`,
`ratsimp` pode simplificar algumas expressãoes contendo `%phi`.


Exemplos:


`fibtophi` expresses Fibonacci numbers `fib(n)` in terms of `%phi`.









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```


Por padrão, Maxima não conhece as propriedade algébricas de `%phi`.
Após avaliar `tellrat(%phi^2 - %phi - 1)` e `algebraic: true`,
`ratsimp` pode simplificar algumas expressãoes contendo `%phi`.










```maxima
(%i1) e : expand ((%phi^2 - %phi - 1) * (A + 1));
                 2                      2
(%o1)        %phi  A - %phi A - A + %phi  - %phi - 1
(%i2) ratsimp (e);
                  2                     2
(%o2)        (%phi  - %phi - 1) A + %phi  - %phi - 1
(%i3) tellrat (%phi^2 - %phi - 1);
                            2
(%o3)                  [%phi  - %phi - 1]
(%i4) algebraic : true;
(%o4)                         true
(%i5) ratsimp (e);
(%o5)                           0
```

<!-- category: Programming -->
<!-- keywords: %pi -->
<!-- signatures: %pi -->
### Variable: %pi

`%pi` representa a razão do perímetro de um círculo para seu diâmetro.
O valor numérico de `%pi` é o n;umero em ponto flutuante de dupla precisão 3.141592653589793d0.

<!-- category: Programming -->
<!-- keywords: false -->
<!-- signatures: false -->
### Variable: false

`false` representa a constante Booleana falso.
Maxima implementa `false` através do valor `NIL` no Lisp.

<!-- category: Programming -->
<!-- keywords: inf -->
<!-- signatures: inf -->
### Variable: inf

`inf` representa o infinito positivo real.

<!-- category: Programming -->
<!-- keywords: infinity -->
<!-- signatures: infinity -->
### Variable: infinity

`infinity` representa o infinito complexo.

<!-- category: Programming -->
<!-- keywords: minf -->
<!-- signatures: minf -->
### Variable: minf

`minf` representa o menos infinito (i.e., negativo) real.

<!-- category: Programming -->
<!-- keywords: true -->
<!-- signatures: true -->
### Variable: true

`true` representa a constante Booleana verdadeiro.
Maxima implementa `true` através do valor `T` no Lisp.

