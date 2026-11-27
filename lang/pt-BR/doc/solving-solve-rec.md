## solve_rec

<!-- category: Solving -->
<!-- keywords: product_use_gamma -->
<!-- signatures: product_use_gamma -->
### Variable: product_use_gamma

Valor padrão: `true`


Quando simplificando produtos, `solve_rec` introduz a função gama
dentro da expressão se `product_use_gamma` for `true`.


Veja também: `simplify_products`, `solve_rec`.

<!-- category: Solving -->
<!-- keywords: reduce_order -->
<!-- signatures: reduce_order(rec, sol, var) -->
### Function: reduce_order (rec, sol, var)

Reduz a ordem de recorrência linear *rec* quando uma solução particular
*sol* for conhecida. A recorrência reduzida pode ser usada para pegar outras soluções.


Exemplo:



```maxima
(%i3) rec: x[n+2] = x[n+1] + x[n]/n;
                                      x
                                       n
(%o3)               x      = x      + --
                     n + 2    n + 1   n
(%i4) solve_rec(rec, x[n]);
WARNING: found some hypergeometrical solutions! 
(%o4)                    x  = %k  n
                          n     1
(%i5) reduce_order(rec, n, x[n]);
(%t5)                    x  = n %z
                          n       n

                           n - 1
                           ====
                           \
(%t6)                %z  =  >     %u
                       n   /        %j
                           ====
                           %j = 0

(%o6)             (- n - 2) %u     - %u
                              n + 1     n
(%i6) solve_rec((n+2)*%u[n+1] + %u[n], %u[n]);
                                     n
                            %k  (- 1)
                              1
(%o6)                 %u  = ----------
                        n    (n + 1)!

So the general solution is

             n - 1
             ====        n
             \      (- 1)
       %k  n  >    -------- + %k  n
         2   /     (n + 1)!     1
             ====
             n = 0
```

<!-- category: Solving -->
<!-- keywords: simplify_products -->
<!-- signatures: simplify_products -->
### Variable: simplify_products

Valor padrão: `true`


Se `simplify_products` for `true`, `solve_rec` irá tentar
simplificar produtos no resultado.


Veja também: `solve_rec`.

<!-- category: Solving -->
<!-- keywords: simplify_sum -->
<!-- signatures: simplify_sum(expr) -->
### Function: simplify_sum (expr)

Tenta simplificar todos os somatórios que aparecem na *expr* para uma forma a mais simplificada possível.


`simplify_sum` usa os algorítmos de Gosper e de Zeilberger para simplificar somatórios.


Para usar essa função primeiramente chame o pacote `simplify_sum` com
`load("simplify_sum")`.


Exemplo:



```maxima
(%i1) load("simplify_sum")$
(%i2) sum(binom(n+k,k)/2^k, k, 0, n) + sum(binom(2*n, 2*k), k, 0, n);
         n                            n
        ====                         ====
        \      binomial(n + k, k)    \
(%o2)    >     ------------------ +   >    binomial(2 n, 2 k)
        /               k            /
        ====           2             ====
        k = 0                        k = 0
(%i3) simplify_sum(%);
                               n
                              4     n
(%o3)                         -- + 2
                              2
```

<!-- category: Solving -->
<!-- keywords: solve_rec -->
<!-- signatures: solve_rec(eqn, var, [init]) -->
### Function: solve_rec (eqn, var, [init])

Encontra soluções hipergeométricas para a recorrência linear *eqn* com
coeficientes polinomiais na variável *var*. Argumentos opcionais *init*
são as condições iniciais.


`solve_rec` pode resolver recorrências lineares com coeficientes constantes,
encontrando soluções hipergeométricas para recorrências lineares homogêneas com
coeficientes polinomiais, soluções racionais para recorrências lineares com
coeficientes polinomiais e pode resolver recorrências do tipo de Ricatti.


Note que o tempo de execução do algorítmo usado para encontrar soluções
hipergeométricas aumenta exponencialmente com o grau do coeficiente lider e
guia.


Para usar essa função primeiramente chame o pacote `solve_rec` com
`load("solve_rec");`.


Exemplo de recorrência linear com coeficientes constantes:



```maxima
(%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);
                        n          n
           (sqrt(5) - 1)  %k  (- 1)
                            1           n
(%o2) a  = ------------------------- - ----
       n               n                  n
                      2                5 2
                                                n
                                   (sqrt(5) + 1)  %k
                                                    2    2
                                 + ------------------ - ----
                                            n              n
                                           2            5 2
```


Exemplo de recorrência linear com coeficientes polinomiais:



```maxima
(%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];
                         2
(%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y
               x + 2                   x + 1                x
(%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);
                              x
                           3 2    x!
(%o9)                 y  = ---- - --
                       x    4     2
```


Exemplo de recorrência do tipo de Ricatti:



```maxima
(%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;
                            y         y
                             x + 1     x
(%o2)         x y  y      - ------ + ----- = 0
                 x  x + 1   x + 2    x - 1
(%i3) solve_rec(%, y[x], y[3]=5)$
(%i4) ratsimp(minfactorial(factcomb(%)));
                                   3
                               30 x  - 30 x
(%o4) y  = - -------------------------------------------------
       x        6      5       4       3       2
             5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584
```



Veja também: `solve_rec_rat`, `simplify_products`, e `product_use_gamma`.

<!-- category: Solving -->
<!-- keywords: solve_rec_rat -->
<!-- signatures: solve_rec_rat(eqn, var, [init]) -->
### Function: solve_rec_rat (eqn, var, [init])

Encontra soluções racionais para recorrências lineares. Veja solve_rec para
uma descrição dos argumentos.


Para usar essa função primeirametne chame o pacote `solve_rec` com
`load("solve_rec");`.


Exemplo:



```maxima
(%i1) (x+4)*a[x+3] + (x+3)*a[x+2] - x*a[x+1] + (x^2-1)*a[x];
(%o1)  (x + 4) a      + (x + 3) a      - x a
                x + 3            x + 2      x + 1
                                                   2
                                               + (x  - 1) a
                                                            x
(%i2) solve_rec_rat(% = (x+2)/(x+1), a[x]);
                       1
(%o2)      a  = ---------------
            x   (x - 1) (x + 1)
```



Veja também: `solve_rec`.

<!-- category: Solving -->
<!-- keywords: summand_to_rec -->
<!-- signatures: summand_to_rec(summand, k, n), summand_to_rec(summand, [k, lo, hi], n) -->
### Function: summand_to_rec (summand, k, n)

Retorna a recorrência satisfeita pelo somatório



```maxima
sup
    ====
    \
     >     x
    /
    ====
  k = inf
```


onde x é hipergeométrico em *k* e *n*. SE *inf* e *sup*
forem omitidos, são assumidos como sendo `inf = -inf` e `sup = inf`.


Para usar essa função primeiro chame o pacote `simplify_sum` com
`load("simplify_sum")`.


Exemplo:



```maxima
(%i1) load("simplify_sum")$
(%i2) summand: binom(n,k);
(%o2)                           binomial(n, k)
(%i3) summand_to_rec(summand,k,n);
(%o3)                      2 sm  - sm      = 0
                               n     n + 1
(%i7) summand: binom(n, k)/(k+1);
                                binomial(n, k)
(%o7)                           --------------
                                    k + 1
(%i8) summand_to_rec(summand, [k, 0, n], n);
(%o8)               2 (n + 1) sm  - (n + 2) sm      = - 1
                                n             n + 1
```

