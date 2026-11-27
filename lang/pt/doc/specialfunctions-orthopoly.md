## orthopoly

<!-- category: SpecialFunctions -->
<!-- keywords: assoc_legendre_p -->
<!-- signatures: assoc_legendre_p(n, m, x) -->
### Function: assoc_legendre_p (n, m, x)

As funções de Legendre associadas de primeiro tipo. 


Referência: Abramowitz e Stegun, equações 22.5.37, página 779, 8.6.6
(segunda equação), página 334, e 8.2.5, página 333.

<!-- category: SpecialFunctions -->
<!-- keywords: assoc_legendre_q -->
<!-- signatures: assoc_legendre_q(n, m, x) -->
### Function: assoc_legendre_q (n, m, x)

A função de Legendre associada de segundo tipo.


Referência: Abramowitz e Stegun, equação 8.5.3 e 8.1.8.

<!-- category: SpecialFunctions -->
<!-- keywords: chebyshev_t -->
<!-- signatures: chebyshev_t(n, x) -->
### Function: chebyshev_t (n, x)

A função de Chebyshev de primeiro tipo.


Referência: Abramowitz e Stegun, equação 22.5.47,página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: chebyshev_u -->
<!-- signatures: chebyshev_u(n, x) -->
### Function: chebyshev_u (n, x)

A função de Chebyshev do segundo tipo.


Referência: Abramowitz e Stegun, equação 22.5.48,página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: gen_laguerre -->
<!-- signatures: gen_laguerre(n, a, x) -->
### Function: gen_laguerre (n, a, x)

O poliomio generalizado de Laguerre.


Referência: Abramowitz e Stegun, equação 22.5.54,página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: hermite -->
<!-- signatures: hermite(n, x) -->
### Function: hermite (n, x)

O polinómio de Hermite.


Referência: Abramowitz e Stegun, equação 22.5.55,página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: intervalp -->
<!-- signatures: intervalp(e) -->
### Function: intervalp (e)

Retorna `true` se a entrada for um intervalo e retorna `false` se não for.

<!-- category: SpecialFunctions -->
<!-- keywords: jacobi_p -->
<!-- signatures: jacobi_p(n, a, b, x) -->
### Function: jacobi_p (n, a, b, x)

o polinómio de Jacobi.


Os polinómios de Jacobi são actualmente definidos para todo
*a* e *b*; todavia, o peso do polinómio de
Jacobi `(1 - x)^a (1 + x)^b` não é integrável para `a <= -1` ou
`b <= -1`. 


Referência: Abramowitz e Stegun, equação 22.5.42,página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: laguerre -->
<!-- signatures: laguerre(n, x) -->
### Function: laguerre (n, x)

O polinómio de Laguerre.


Referência: Abramowitz e Stegun, equatções 22.5.16 e 22.5.54,página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: legendre_p -->
<!-- signatures: legendre_p(n, x) -->
### Function: legendre_p (n, x)

O polinómio de Legendre de primeiro tipo.


Referência: Abramowitz e Stegun, equações 22.5.50 e 22.5.51,página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: legendre_q -->
<!-- signatures: legendre_q(n, x) -->
### Function: legendre_q (n, x)

O polinómio de Legendre de primeiro tipo.


Referência: Abramowitz e Stegun, equações 8.5.3 e 8.1.8.

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_recur -->
<!-- signatures: orthopoly_recur(f, args) -->
### Function: orthopoly_recur (f, args)

Retorna uma relação recursiva para a família de funções ortogonais
*f* com argumentos *args*. A recursividade é com 
relação ao grau do polinómio.






```maxima
(%i1) orthopoly_recur (legendre_p, [n, x]);
                (2 n - 1) P     (x) x + (1 - n) P     (x)
                           n - 1                 n - 2
(%o1)   P (x) = -----------------------------------------
         n                          n
```


O segundo argumento a `orthopoly_recur` deve ser uma lista com o 
número correcto de argumentos para a função *f*; se o número de argumentos não for o correcto, 
Maxima sinaliza com um erro.






```maxima
(%i1) orthopoly_recur (jacobi_p, [n, x]);

Function jacobi_p needs 4 arguments, instead it received 2
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Adicionalmente, quando *f* não for o nome de uma das
famílias de polinómios ortogonais, um erro é sinalizado.






```maxima
(%i1) orthopoly_recur (foo, [n, x]);

A recursion relation for foo isn't known to Maxima
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_returns_intervals -->
<!-- signatures: orthopoly_returns_intervals -->
### Variable: orthopoly_returns_intervals

Valor por omissão: `true`


Quando `orthopoly_returns_intervals` for `true`, resultados em ponto flutuante são retornados na
forma `interval (c, r)`, onde *c* é o centro de um intervalo
e *r* é seu raio. O centro pode ser um número complexo; nesse
caso, o intervalo é um disco no plano complexo.

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_weight -->
<!-- signatures: orthopoly_weight(f, args) -->
### Function: orthopoly_weight (f, args)

Retorna uma lista de três elementos; o primeiro elemento é 
a fórmula do peso para a família de polinómios ortogonais
*f* com argumentos fornecidos pela lista *args*; os 
segundos e terceiros elementos fornecem os pontos finais inferior e superior
do intervalo de ortogonalidade. Por exemplo,







```maxima
(%i1) w : orthopoly_weight (hermite, [n, x]);
                            2
                         - x
(%o1)                 [%e    , - inf, inf]
(%i2) integrate (w[1] * hermite (3, x) * hermite (2, x), x, w[2], w[3]);
(%o2)                           0
```


A variável principal de *f* deve ser um símbolo; Se não for, Maxima
sinaliza com um erro.

<!-- category: SpecialFunctions -->
<!-- keywords: pochhammer -->
<!-- signatures: pochhammer(n, x) -->
### Function: pochhammer (n, x)

O símbolo de Pochhammer. Para inteiros não negativos *n* com
`n <= pochhammer_max_index`, a expressão `pochhammer (x, n)` 
avalia para o produto `x (x + 1) (x + 2) ... (x + n - 1)`
when `n > 0` e
para 1 quando `n = 0`. Para valores negativos de *n*,
`pochhammer (x, n)` é definido como `(-1)^n / pochhammer (1 - x, -n)`.
Dessa forma







```maxima
(%i1) pochhammer (x, 3);
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, -3);
                                 1
(%o2)               - -----------------------
                      (1 - x) (2 - x) (3 - x)
```


Para converter um símbolo de Pochhammer em um quociente de funções gama,
(veja Abramowitz e Stegun, equação 6.1.22) use `makegamma`; por exemplo 






```maxima
(%i1) makegamma (pochhammer (x, n));
                          gamma(x + n)
(%o1)                     ------------
                            gamma(x)
```


Quando *n* exceder `pochhammer_max_index` ou quando *n* 
for simbólico, `pochhammer` retorna uma forma substantiva.






```maxima
(%i1) pochhammer (x, n);
(%o1)                         (x)
                                 n
```

<!-- category: SpecialFunctions -->
<!-- keywords: pochhammer_max_index -->
<!-- signatures: pochhammer_max_index -->
### Variable: pochhammer_max_index

Valor por omissão: 100


`pochhammer (n, x)` expande para um produto se e somente se
`n <= pochhammer_max_index`.


Exemplos:







```maxima
(%i1) pochhammer (x, 3), pochhammer_max_index : 3;
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, 4), pochhammer_max_index : 3;
(%o2)                         (x)
                                 4
```


Referência: Abramowitz e Stegun, equação 6.1.16,página 256.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_bessel_j -->
<!-- signatures: spherical_bessel_j(n, x) -->
### Function: spherical_bessel_j (n, x)

A Função de Bessel esférica de primeiro tipo.


Referência: Abramowitz e Stegun, equações 10.1.8,página 437 e 10.1.15,página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_bessel_y -->
<!-- signatures: spherical_bessel_y(n, x) -->
### Function: spherical_bessel_y (n, x)

A Função de Bessel esférica de segundo tipo. 


Referência: Abramowitz e Stegun, equações 10.1.9,página 437 e 10.1.15,página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_hankel1 -->
<!-- signatures: spherical_hankel1(n, x) -->
### Function: spherical_hankel1 (n, x)

A Função de Hankel esférica de
primeiro tipo.


Referência: Abramowitz e Stegun, equação 10.1.36,página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_hankel2 -->
<!-- signatures: spherical_hankel2(n, x) -->
### Function: spherical_hankel2 (n, x)

A Função de Hankel esférica de segundo tipo.


Referência: Abramowitz e Stegun, equação 10.1.17,página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_harmonic -->
<!-- signatures: spherical_harmonic(n, m, x, y) -->
### Function: spherical_harmonic (n, m, x, y)

A função armonica esférica.


Referência: Merzbacher 9.64.

<!-- category: SpecialFunctions -->
<!-- keywords: ultraspherical -->
<!-- signatures: ultraspherical(n, a, x) -->
### Function: ultraspherical (n, a, x)

A função polinomial ultraesférica (também conhecida como função polinomial de Gegenbauer).


Referência: Abramowitz e Stegun, equação 22.5.46,página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: unit_step -->
<!-- signatures: unit_step(x) -->
### Function: unit_step (x)

A função de passo de unidade contínua à esquerda; dessa forma
`unit_step (x)` tende para `x <= 0` e é igual a
1 para `x > 0`.


Se quiser uma função de degrau unitário que tome o
valor 1/2 em zero, use `(1 + signum (x))/2`.

