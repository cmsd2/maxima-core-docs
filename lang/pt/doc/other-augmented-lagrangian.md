## augmented_lagrangian

<!-- category: Other -->
<!-- keywords: augmented_lagrangian_method -->
<!-- signatures: augmented_lagrangian_method(FOM, xx, C, yy), augmented_lagrangian_method(FOM, xx, C, yy, args_opcionais) -->
### Function: augmented_lagrangian_method (FOM, xx, C, yy)

Retorna um mínimo aproximado da expressão *FOM*
com relação às variáveis *xx*,
mantendo restrito o valor de *C* a zero.
*yy* é uma lista de suposições iniciais para *xx*.
O método utilizado é o método do Lagrangiano aumentado (veja referências [1] e [2]).


`args_opcionais` representam argumentos adicionais,
especificados como `símbolo = valor`.
Os argumentos opcionais que podem ser colocados no lugar de *símbolo*:

 

**niter** — Número de iterações do algoritmo do Langrangiano aumentado
**lbfgs_tolerance** — Tolerância forneceida a LBFGS (Limited-memory, Broyden, Fletcher, Goldfarb, Shanno)
**iprint** — parâmetro IPRINT (uma lista de dois inteiros que controlam o nível de informação) fornecido a LBFGS
**%lambda** — valor inicial de `%lambda` a ser usado durante o cálculo do Lagrangiano aumentado


Essa implementação minimiza o Lagrangiano aumentado pela
pela aplicação do algoritmo de memória limitada BFGS (LBFGS),
que é um algoritmo quasi-Newton.


`load("augmented_lagrangian")` chama essa função.

 

Veja também `lbfgs`.


References:


[1] http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/continuous/constrained/nonlinearcon/auglag.html


[2] http://www.cs.ubc.ca/spider/ascher/542/chap10.pdf


Exemplo:












```maxima
(%i1) load ("lbfgs");
(%o1) /home/robert/tmp/maxima-release-branch/maxima/share/lbfgs/\
lbfgs.mac
(%i2) load ("augmented_lagrangian");
(%o2) /home/robert/tmp/maxima-release-branch/maxima/share/contri\
b/augmented_lagrangian.mac
(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x
(%i4) xx: [x, y];
(%o4)                        [x, y]
(%i5) C: [x + y - 1];
(%o5)                      [y + x - 1]
(%o6)                        [1, 1]
(%i7) augmented_lagrangian_method (FOM, xx, C, yy, iprint = [-1, 0]);
(%o7) [[x = 0.6478349888525, y = 0.32391749442625], 
                                 %lambda = [- 1.267422460983745]]
```

