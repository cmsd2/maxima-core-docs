## Numérico

<!-- category: Series -->
<!-- keywords: absint -->
<!-- signatures: absint(f, x, halfplane), absint(f, x), absint(f, x, a, b) -->
### Function: absint (f, x, halfplane)

`absint (f, x, halfplane)`
retorna a integral indefinida de *f* com relação a
*x* no dado semi-plano (`pos`, `neg`, ou `both`).
*f* pode conter expressões da forma
`abs (x)`, `abs (sin (x))`, `abs (a) * exp (-abs (b) * abs (x))`.


`absint (f, x)` é equivalente a `absint (f, x, pos)`.


`absint (f, x, a, b)`
retorna a integral definida de *f* com relação a *x* de *a* até *b*.

*f* pode incluir valores absolutos.

<!-- category: Series -->
<!-- keywords: cosnpiflag -->
<!-- signatures: cosnpiflag -->
### Variable: cosnpiflag

Valor por omissão: `true`


Veja `foursimp`.

<!-- category: Series -->
<!-- keywords: equalp -->
<!-- signatures: equalp(x, y) -->
### Function: equalp (x, y)

Retorna `true` se `equal (x, y)` de outra forma `false` (não fornece uma
mensagem de erro como `equal (x, y)` poderia fazer nesse caso).

<!-- category: Series -->
<!-- keywords: fourcos -->
<!-- signatures: fourcos(f, x, p) -->
### Function: fourcos (f, x, p)

Retorna os coeficientes do co-seno de Fourier para `f(x)` definida sobre `[0, %pi]`.

<!-- category: Series -->
<!-- keywords: fourexpand -->
<!-- signatures: fourexpand(l, x, p, limit) -->
### Function: fourexpand (l, x, p, limit)

Constrói e retorna a série de Fourier partindo da lista de
coeficientes de Fourier *l* até (up through) *limit* termos (*limit*
pode ser `inf`). *x* e *p* possuem o mesmo significado que em
`fourier`.

<!-- category: Series -->
<!-- keywords: fourier -->
<!-- signatures: fourier(f, x, p) -->
### Function: fourier (f, x, p)

Retorna uma lista de coeficientes de Fourier de `f(x)` definidos
sobre o intervalo `[-p, p]`.

<!-- category: Series -->
<!-- keywords: fourint -->
<!-- signatures: fourint(f, x) -->
### Function: fourint (f, x)

Constrói e retorna uma lista de coeficientes de integral de Fourier de `f(x)`
definida sobre `[minf, inf]`.

<!-- category: Series -->
<!-- keywords: fourintcos -->
<!-- signatures: fourintcos(f, x) -->
### Function: fourintcos (f, x)

Retorna os coeficientes da integral do co-seno de Fourier para `f(x)` on `[0, inf]`.

<!-- category: Series -->
<!-- keywords: fourintsin -->
<!-- signatures: fourintsin(f, x) -->
### Function: fourintsin (f, x)

Retorna os coeficientes da integral do seno de Fourier para `f(x)` on `[0, inf]`.

<!-- category: Series -->
<!-- keywords: foursimp -->
<!-- signatures: foursimp(l) -->
### Function: foursimp (l)

Simplifica `sin (n %pi)` para 0 se `sinnpiflag` for `true` e
`cos (n %pi)` para `(-1)^n` se `cosnpiflag` for `true`.

<!-- category: Series -->
<!-- keywords: foursin -->
<!-- signatures: foursin(f, x, p) -->
### Function: foursin (f, x, p)

Retorna os coeficientes do seno de Fourier para `f(x)` definida sobre `[0, p]`.

<!-- category: Series -->
<!-- keywords: funp -->
<!-- signatures: funp(f, expr), funp(f, expr, x) -->
### Function: funp (f, expr)

`funp (f, expr)`
retorna `true` se *expr* contém a função *f*.


`funp (f, expr, x)`
retorna `true` se *expr* contém a função *f* e a variável
*x* em algum lugar no argumento de uma das instâncias de *f*.

<!-- category: Series -->
<!-- keywords: remfun -->
<!-- signatures: remfun(f, expr), remfun(f, expr, x) -->
### Function: remfun (f, expr)

`remfun (f, expr)`
substitue todas as ocorrências de `f (arg)` por *arg* em *expr*.


`remfun (f, expr, x)`
substitue todas as ocorrências de `f (arg)` por *arg* em *expr*
somente se *arg* contiver a variável *x*.

<!-- category: Series -->
<!-- keywords: sinnpiflag -->
<!-- signatures: sinnpiflag -->
### Variable: sinnpiflag

Valor por omissão: `true`


Veja `foursimp`.

<!-- category: Series -->
<!-- keywords: totalfourier -->
<!-- signatures: totalfourier(f, x, p) -->
### Function: totalfourier (f, x, p)

Retorna `fourexpand (foursimp (fourier (f, x, p)), x, p, 'inf)`.

