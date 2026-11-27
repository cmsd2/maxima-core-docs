## zeilberger

<!-- category: Series -->
<!-- keywords: AntiDifference -->
<!-- signatures: AntiDifference(F_k, k) -->
### Function: AntiDifference (F_k, k)

Retorna a anti-diferença hipergeométrica
de *F_k*, se essa anti-diferença.
De outra forma `AntiDifference` retorna `no_hyp_antidifference`.

<!-- category: Series -->
<!-- keywords: ev_point -->
<!-- signatures: ev_point -->
### Variable: ev_point

Valor por omissão: `big_primes[10]`


`ev_point` é o valor no qual a variável *n* é avaliada
no momento da execução do teste modular em `parGosper`.

<!-- category: Series -->
<!-- keywords: Gosper -->
<!-- signatures: Gosper(F_k, k) -->
### Function: Gosper (F_k, k)

Retorna o certificado racional *R(k)* para *F_k*, isto é,
uma função racional tal que


$F_k = R(k+1) F_(k+1) - R(k) F_k$

 

se essa função racional exitir.
De outra forma, `Gosper` retorna `no_hyp_sol`.

<!-- category: Series -->
<!-- keywords: gosper_in_zeilberger -->
<!-- signatures: gosper_in_zeilberger -->
### Variable: gosper_in_zeilberger

Valor por omissão: `true`


Quando `gosper_in_zeilberger` for `true`,
a função `Zeilberger` chama `Gosper` antes de chamar `parGosper`.
De outra forma, `Zeilberger` vai imediatamente para `parGosper`.

<!-- category: Series -->
<!-- keywords: GosperSum -->
<!-- signatures: GosperSum(F_k, k, a, b) -->
### Function: GosperSum (F_k, k, a, b)

Retorna o somatório de *F_k* de $k = a$ a $k = b$
se *F_k* tiver ma diferença hipergeométrica.
De outra forma, `GosperSum` retorna `nongosper_summable`.


Exemplos:













```maxima
(%i1) load ("zeilberger");
(%o1)  /usr/share/maxima/share/contrib/Zeilberger/zeilberger.mac
(%i2) GosperSum ((-1)^k*k / (4*k^2 - 1), k, 1, n);

Dependent equations eliminated:  (1)
                           3       n + 1
                      (n + -) (- 1)
                           2               1
(%o2)               - ------------------ - -
                                  2        4
                      2 (4 (n + 1)  - 1)
(%i3) GosperSum (1 / (4*k^2 - 1), k, 1, n);
                                3
                          - n - -
                                2       1
(%o3)                  -------------- + -
                                2       2
                       4 (n + 1)  - 1
(%i4) GosperSum (x^k, k, 1, n);
                          n + 1
                         x          x
(%o4)                    ------ - -----
                         x - 1    x - 1
(%i5) GosperSum ((-1)^k*a! / (k!*(a - k)!), k, 1, n);
                                n + 1
                a! (n + 1) (- 1)              a!
(%o5)       - ------------------------- - ----------
              a (- n + a - 1)! (n + 1)!   a (a - 1)!
(%i6) GosperSum (k*k!, k, 1, n);

Dependent equations eliminated:  (1)
(%o6)                     (n + 1)! - 1
(%i7) GosperSum ((k + 1)*k! / (k + 1)!, k, 1, n);
                  (n + 1) (n + 2) (n + 1)!
(%o7)             ------------------------ - 1
                          (n + 2)!
(%i8) GosperSum (1 / ((a - k)!*k!), k, 1, n);
(%o8)                  nonGosper_summable
```

<!-- category: Series -->
<!-- keywords: linear_solver -->
<!-- signatures: linear_solver -->
### Variable: linear_solver

Valor por omissão: `linsolve`


`linear_solver` nomeia o resolvedor que é usado para resolver o sistema
de equações no algoritmo de Zeilberger.

<!-- category: Series -->
<!-- keywords: MAX_ORD -->
<!-- signatures: MAX_ORD -->
### Variable: MAX_ORD

Valor por omissão: 5


`MAX_ORD` é a ordem máxima de recorrência tentada por `Zeilberger`.

<!-- category: Series -->
<!-- keywords: mod_big_prime -->
<!-- signatures: mod_big_prime -->
### Variable: mod_big_prime

Valor por omissão: `big_primes[1]`


`mod_big_prime` é o módulo usado pelo teste modular em `parGosper`.

<!-- category: Series -->
<!-- keywords: mod_test -->
<!-- signatures: mod_test -->
### Variable: mod_test

Valor por omissão: `false`


Quando `mod_test` for `true`,
`parGosper` executa um
teste modular discartando sistemas sem solução.

<!-- category: Series -->
<!-- keywords: mod_threshold -->
<!-- signatures: mod_threshold -->
### Variable: mod_threshold

Valor por omissão: 4


`mod_threshold` is the
maior ordem para a qual o teste modular em `parGosper` é tentado.

<!-- category: Series -->
<!-- keywords: modular_linear_solver -->
<!-- signatures: modular_linear_solver -->
### Variable: modular_linear_solver

Valor por omissão: `linsolve`


`modular_linear_solver` nomeia o resolvedor linear usado pelo  teste modular em `parGosper`.

<!-- category: Series -->
<!-- keywords: parGosper -->
<!-- signatures: parGosper(F_{n,k}, k, n, d) -->
### Function: parGosper (F_{n,k}, k, n, d)

Tenta encontrar uma recorrência de *d*-ésima ordem para *F_{n,k}*.


O algoritmo retorna uma sequência
$[s_1, s_2, ..., s_m]$ de soluções.
Cada solução tem a forma


$[R(n, k), [a_0, a_1, ..., a_d]]$


`parGosper` retorna `[]` caso não consiga encontrar uma recorrência.

<!-- category: Series -->
<!-- keywords: simplified_output -->
<!-- signatures: simplified_output -->
### Variable: simplified_output

Valor por omissão: `false`


Quando `simplified_output` for `true`,
funções no pacote `zeilberger` tentam
simplificação adicional da solução.

<!-- category: Series -->
<!-- keywords: trivial_solutions -->
<!-- signatures: trivial_solutions -->
### Variable: trivial_solutions

Valor por omissão: `true`


Quando `trivial_solutions` for `true`,
`Zeilberger` retorna soluções
que possuem certificado igual a zero, ou todos os coeficientes iguais a zero.

<!-- category: Series -->
<!-- keywords: warnings -->
<!-- signatures: warnings -->
### Variable: warnings

Valor por omissão: `true`


Quando `warnings` for `true`,
funções no pacote `zeilberger` imprimem
mensagens de alerta durante a execução.

<!-- category: Series -->
<!-- keywords: Zeilberger -->
<!-- signatures: Zeilberger(F_{n,k}, k, n) -->
### Function: Zeilberger (F_{n,k}, k, n)

Tenta calcular o somatório hipergeométrico indefinido de *F_{n,k}*.


`Zeilberger` primeiro invoca `Gosper`, e se `Gosper` não conseguir encontrar uma solução, então `Zeilberger` invoca
`parGosper`com ordem 1, 2, 3, ..., acima de `MAX_ORD`.
Se Zeilberger encontrar uma solução antes de esticar `MAX_ORD`,
Zeilberger para e retorna a solução.


O algoritmo retorna uma sequência
$[s_1, s_2, ..., s_m]$ de soluções.
Cada solução tem a forma


$[R(n,k), [a_0, a_1, ..., a_d]]$


`Zeilberger` retorna `[]` se não conseguir encontrar uma solução.


`Zeilberger` invoca `Gosper` somente se `gosper_in_zeilberger` for `true`.

