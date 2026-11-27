## simplex

<!-- category: Numerical -->
<!-- keywords: epsilon_sx -->
<!-- signatures: epsilon_sx -->
### Variable: epsilon_sx

Valor por omissão: `10^-8`


Epsilon usando para cálculos numéricos em `linear_program`.


Veja também: `linear_program`.

<!-- category: Numerical -->
<!-- keywords: linear_program -->
<!-- signatures: linear_program(A, b, c) -->
### Function: linear_program (A, b, c)

`linear_program` é uma implementação do algoritmo simplex.
`linear_program(A, b, c)` calcula um vetor *x* para o qual `c.x` é o mínimo
possível entre vetores para os quais `A.x = b` e `x >= 0`. O argumento
*A* é uma matriz e os argumentos *b* e *c* são listas.


`linear_program` retorna uma lista contendo o vetor minimizado *x* e o
valor mínimo `c.x`. Se o problema for não associado, é retornado "Problem not bounded!" e
se o problema for não viável, é retornado "Problem not feasible!".


Para usar essa função primeiramente chame o pacote `simplex` com `load("simplex");`.


Exemplo:









```maxima
(%i2) A: matrix([1,1,-1,0], [2,-3,0,-1], [4,-5,0,0])$
(%i3) b: [1,1,6]$
(%i4) c: [1,-2,0,0]$
(%i5) linear_program(A, b, c);
                   13     19        3
(%o5)            [[--, 4, --, 0], - -]
                   2      2         2
```


Veja também: `minimize_sx`, `scale_sx`, e `epsilon_sx`.

<!-- category: Numerical -->
<!-- keywords: maximize_sx -->
<!-- signatures: maximize_sx(obj, cond, [pos]) -->
### Function: maximize_sx (obj, cond, [pos])

Maximiza a função linear objetiva *obj* submetida a alguma restrição linear
*cond*. Veja `minimize_sx` para uma descrição detalhada de argumentos e valores de
retorno.



Veja também: `minimize_sx`.

<!-- category: Numerical -->
<!-- keywords: minimize_sx -->
<!-- signatures: minimize_sx(obj, cond, [pos]) -->
### Function: minimize_sx (obj, cond, [pos])

Minimiza uma função linear objetiva *obj* submetida a alguma restrição
linear *cond*. *cond* é uma lista de equações lineares ou
desigualdades. Em desigualdades estritas `>` é  substituido por `>=`
e `<` por `<=`. O argumento opcional *pos* é uma lista de
variáveis de decisão que são assumidas como sendo positivas.


Se o mínimo existir, `minimize_sx` retorna uma lista que contém
o menor valor da função objetiva e uma lista de valores de variáveis de
decisão para os quais o mínimo é alcançado. Se o problema for não associado,
`minimize_sx` retorna "Problem not bounded!" e se o problema for
não viável, é retornado "Ploblem not feasible!".


As variáveis de decisão não são assumidas para serem não negativas por padrão. Se todas
as variáveis de dicisão forem não negativas, escolha `nonegative_sx` para `true`.
Se somente algumas das variáveis de decisão forem positivas, coloque-as então no argumento
opcional *pos* (note que isso é mais eficiente que adicionar
restrições).


`minimize_sx` utiliza o algoritmo simplex que é implementado na função
`linear_program` do Maxima.


Para usar essa função primeiramente chame o pacote `simplex` com `load("simplex");`.


Exemplos:









```maxima
(%i1) minimize_sx(x+y, [3*x+y=0, x+2*y>2]);
                      4       6        2
(%o1)                [-, [y = -, x = - -]]
                      5       5        5
(%i2) minimize_sx(x+y, [3*x+y>0, x+2*y>2]), nonegative_sx=true;
(%o2)                [1, [y = 1, x = 0]]
(%i3) minimize_sx(x+y, [3*x+y=0, x+2*y>2]), nonegative_sx=true;
(%o3)                Problem not feasible!
(%i4) minimize_sx(x+y, [3*x+y>0]);
(%o4)                Problem not bounded!
```



Veja também: `maximize_sx`, `nonegative_sx`, `epsilon_sx`.

<!-- category: Numerical -->
<!-- keywords: nonegative_sx -->
<!-- signatures: nonegative_sx -->
### Variable: nonegative_sx

Valor por omissão: `false`


Se `nonegative_sx` for verdadeiro (true) todas as variáveis de decisão para `minimize_sx`
e `maximize_sx` são assumidas para serem positivas.


Veja também: `minimize_sx`.

