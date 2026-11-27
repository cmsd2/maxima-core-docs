## mnewton

<!-- category: Numerical -->
<!-- keywords: mnewton -->
<!-- signatures: mnewton(FuncList, VarList, GuessList) -->
### Function: mnewton (FuncList, VarList, GuessList)

Solução de multiplas funções não lineares usando o método de Newton.
*FuncList* é a lista de funções a serem resolvidas,
*VarList* é a lista dos nomes de variáveis, e
*GuessList* é a lista de aproximações iniciais.


A solução é retornada no mesmo formato retornado pela função `solve()`.
Caso a solução não seja encontrada, `[]` é retornado.


Essa função é controlada através das variáveis globais `newtonepsilon` e `newtonmaxiter`.



```maxima
(%i1) load("mnewton")$

(%i2) mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1],
              [x1, x2], [5, 5]);
(%o2) [[x1 = 3.756834008012769, x2 = 2.779849592817897]]
(%i3) mnewton([2*a^a-5],[a],[1]);
(%o3)             [[a = 1.70927556786144]]
(%i4) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o4) [[u = 1.066618389595407, v = 1.552564766841786]]
```


Para usar essa função primeiro escreva `load("mnewton")`. Veja também `newtonepsilon` e `newtonmaxiter`.

<!-- category: Numerical -->
<!-- keywords: newtonepsilon -->
<!-- signatures: newtonepsilon -->
### Variable: newtonepsilon

Valor por omissão: `10.0^(-fpprec/2)`


Precisão para determinar quando a função `mnewton` convergiu em direção à solução.


Veja também `mnewton`.

<!-- category: Numerical -->
<!-- keywords: newtonmaxiter -->
<!-- signatures: newtonmaxiter -->
### Variable: newtonmaxiter

Valor por omissão: `50`


Número máximo de iterações que para a função `mnewton`
caso essa função não seja convergente ou se convergir muito lentamente.


Veja também `mnewton`.

