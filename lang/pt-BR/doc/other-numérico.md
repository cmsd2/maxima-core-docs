## Numérico

<!-- category: Other -->
<!-- keywords: fft, ift, recttopolar, polartorect -->
<!-- signatures: fft(real_array, imaginary_array), ift(real_array, imaginary_array), recttopolar(real_array, imaginary_array), polartorect(magnitude_array, phase_array) -->
### Function: fft (real_array, imaginary_array)

Transformação rápidada de Fourier e funções relacionadas. `load ("fft")`
chama essas funções dentro do Maxima.


`fft` e `ift` realiza transformação rápida complexa de Fourier e
a transformação inversa, respectivamente, sobre arrays em ponto flutuante
unidimensionais. O tamanho de *imaginary_array* deve ser igual ao tamanho de *real_array*.


`fft` e `ift` operam in-loco. Isto é, sobre o retorno de `fft` ou de `ift`,
O conteúdo original dos arrays de entrada é substituído pela saída.
A função `fillarray` pode fazer uma cópia de um array, isso pode
ser necessário.


A transformação discreta de Fourier e sua transformação inversa são definidas
como segue. Tome `x` sendo os dados originais, com



```maxima
x[i]: real_array[i] + %i imaginary_array[i]
```

  

Tome `y` sendo os dados transformados. A transformação normal e sua transformação inversa são



```maxima
y[k]: (1/n) sum (x[j] exp (-2 %i %pi j k / n), j, 0, n-1)

x[j]:       sum (y[j] exp (+2 %i %pi j k / n), k, 0, n-1)
```


Arrays adequadas podem ser alocadas pela função `array`. Por exemplo:



```maxima
array (my_array, float, n-1)$
```


declara um array unidimensional com n elementos, indexado de 0 a
n-1 inclusive. O número de elementos n deve ser igual a 2^m para algum m.


`fft` pode ser aplicada a dados reais (todos os arrays imaginários são iguais a zero) para obter
coeficientes seno e cosseno.  Após chamar `fft`, os coeficientes
seno e cosseno, digamos `a` e `b`, podem ser calculados como



```maxima
a[0]: real_array[0]
b[0]: 0
```


e



```maxima
a[j]: real_array[j] + real_array[n-j]
b[j]: imaginary_array[j] - imaginary_array[n-j]
```


para j variando de 1 a n/2-1, e



```maxima
a[n/2]: real_array[n/2]
b[n/2]: 0
```


`recttopolar` traduz valores complexos da forma `a + b %i` para
a forma `r %e^(%i t)`. Veja `recttopolar`.


`polartorect` traduz valores complexos da forma `r %e^(%i t)`
para a forma `a + b %i`. Veja `polartorect`.


`demo ("fft")` exibe uma demonstração do pacote `fft`.

<!-- category: Other -->
<!-- keywords: find_root -->
<!-- signatures: find_root(f(x), x, a, b), find_root(f, a, b) -->
### Function: find_root (f(x), x, a, b)

Encontra a raíz da função *f* com a variável *x* percorrendo o intervalo `[a, b]`.
A função deve ter um
sinal diferente em cada ponto final.  Se essa condição não for alcançada, a
action of the function is governed by `find_root_error`.  If
`find_root_error` is `true` then an error occurs, otherwise the value of
`find_root_error` is returned (thus for plotting `find_root_error` might be set to
0.0).  De outra forma (dado que Maxima pode avaliar o primeiro argumento
no intervalo especificado, e que o intervalo é contínuo) `find_root` é
garantido vir para cima com a raíz (ou um deles se existir mais
que uma raíz).  A precisão de `find_root` é governada por
`intpolabs` e `intpolrel` os quais devem ser números em ponto flutuante
não negativos.  `find_root` encerrará quando o primeiro argumento avaliar para
alguma coisa menor que ou igual a `intpolabs` ou se sucessivas
aproximações da raíz diferirem por não mais que `intpolrel * <um dos aproximandos>`.
O valor padrão de `intpolabs` e `intpolrel` são
0.0 de forma que `find_root` pega como boa uma resposta como for possível com a
precisão aritmética simples que tivermos.  O primeiro argumento pode ser uma
equação.  A ordem dos dois últimos argumentos é irrelevante.  Dessa forma



```maxima
find_root (sin(x) = x/2, x, %pi, 0.1);
```


é equivalente a



```maxima
find_root (sin(x) = x/2, x, 0.1, %pi);
```


O método usado é uma busca binária no intervalo especificado pelos últimos
dois argumentos.  Quando o resultado da busca for encontrado a função é fechada o suficiente para ser
linear, isso inicia usando interpolação linear.


Examples:
















```maxima
(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2
(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981
(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981
(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981
(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981
```

<!-- category: Other -->
<!-- keywords: find_root_abs -->
<!-- signatures: find_root_abs -->
### Variable: find_root_abs

Valor padrão: 0.0


`find_root_abs` é a precisão do comando `find_root`. A precisão é
governada por `find_root_abs` e `find_root_rel` que devem ser
números não negativos em ponto flutuante.  `find_root` terminará quando o
primeiro argumento avaliar para alguma coisa menor que ou igual a `find_root_abs` ou se
sucessivos aproximandos para a raíz diferirem por não mais que `find_root_rel * <um dos aproximandos>`.
Os valores padrão de `find_root_abs` e
`find_root_rel` são 0.0 de forma que `find_root` tome como boa uma resposta que for possível
com a precisão aritmética simples que tivermos.

<!-- category: Other -->
<!-- keywords: find_root_error -->
<!-- signatures: find_root_error -->
### Variable: find_root_error

Valor padrão: `true`


`find_root_error` governa o comportamento de `find_root`.
Quando `find_root` for chamada, ela determina se a função
a ser resolvida satisfaz ou não a condição que os valores da
função nos pontos finais do intervalo de interpolação são opostos
em sinal.  Se eles forem de sinais opostos, a interpolação prossegue.
Se eles forem de mesmo sinal, e `find_root_error` for `true`, então um erro é
sinalizado.  Se eles forem de mesmo sinal e `find_root_error` não for `true`, o
valor de `find_root_error` é retornado.  Dessa forma para montagem de gráfico, `find_root_error`
pode ser escolhida para 0.0.

<!-- category: Other -->
<!-- keywords: find_root_rel -->
<!-- signatures: find_root_rel -->
### Variable: find_root_rel

Valor padrão: 0.0


`find_root_rel` é a precisão do comando `find_root` e é
governada por `find_root_abs` e `find_root_rel` que devem ser
números não negativos em ponto flutuante.  `find_root` terminará quando o
primeiro argumento avaliar para alguma coisa menor que ou igual a `find_root_abs` ou se
sucessivos aproximandos para a raíz diferirem de não mais que `find_root_rel * <um dos aproximandos>`.
Os valores padrão de `find_root_labs` e
`find_root_rel` é 0.0 de forma que `find_root` toma como boa uma resposta que for possível
com a precisão aritmética simples que tivermos.

<!-- category: Other -->
<!-- keywords: fortindent -->
<!-- signatures: fortindent -->
### Variable: fortindent

Valor padrão: 0


`fortindent` controla a margem esquerda de indentação de
expressões mostradas pelo comando `fortran`.  0 fornece indentação
normal (i.e., 6 espaços), e valores positivos farão com que
expressões sejam mostrados mais além para a direita.

<!-- category: Other -->
<!-- keywords: fortran -->
<!-- signatures: fortran(expr) -->
### Function: fortran (expr)

Mostra *expr* como uma declaração Fortran.
A linha de saída é indentada com espaços.
Se a linha for muito longa, `fortran` imprime linhas de continuação.
`fortran` mostra o operador de exponenciação `^` como `**`,
e mostra um número complexo `a + b %i` na forma `(a,b)`.


*expr* pode ser uma equação. Nesse caso, `fortran` mostra uma declaração de
atribuição, atribuindo o primeiro membro (esquerda) da equação ao segundo membro (direita).
Em particular, se o primeiro membro *expr* é um nome de uma matriz,
então `fortran` mostra uma declaração de atribuição para cada elemento da matriz.


Se *expr* não for alguma coisa reconhecida por `fortran`,
a expressão é mostrada no formato `grind` sem reclamação.
`fortran` não conhece listas, arrays ou funções.


`fortindent` controla o margem esquerda das linhas mostradas.
0 é a margem normal (i.e., indentada 6 espaços). Incrementando `fortindent`
faz com que expressões sejam mostradas adiante para a direita.


quando `fortspaces` for `true`, `fortran` preenche
cada linha mostrada com espaços em branco até completar 80 columas.


`fortran` avalia seus argumentos;
colocando um apóstrofo em um argumento evita avaliação.
`fortran` sempre retorna `done`.


Exemplos:



```maxima
(%i1) expr: (a + b)^12$
(%i2) fortran (expr);
      (b+a)**12                                                                 
(%o2)                         done
(%i3) fortran ('x=expr);
      x = (b+a)**12                                                             
(%o3)                         done
(%i4) fortran ('x=expand (expr));
      x = b**12+12*a*b**11+66*a**2*b**10+220*a**3*b**9+495*a**4*b**8+792        
     1   *a**5*b**7+924*a**6*b**6+792*a**7*b**5+495*a**8*b**4+220*a**9*b        
     2   **3+66*a**10*b**2+12*a**11*b+a**12                                     
(%o4)                         done
(%i5) fortran ('x=7+5*%i);
      x = (7,5)                                                                 
(%o5)                         done
(%i6) fortran ('x=[1,2,3,4]);
      x = [1,2,3,4]                                                             
(%o6)                         done
(%i7) f(x) := x^2$
(%i8) fortran (f);
      f                                                                         
(%o8)                         done
```

<!-- category: Other -->
<!-- keywords: fortspaces -->
<!-- signatures: fortspaces -->
### Variable: fortspaces

Valor padrão: `false`


Quando `fortspaces` for `true`, `fortran` preenche
cada linha mostrada com espaços em branco até completar 80 columas.

<!-- category: Other -->
<!-- keywords: horner -->
<!-- signatures: horner(expr, x), horner(expr) -->
### Function: horner (expr, x)

Retorna uma representação rearranjada de *expr* como
na regra de Horner, usando *x* como variável principal se isso for especificado.
`x` pode ser omitido e nesse caso a variável principal da forma de expressão racional
canônica de *expr* é usada.


`horner` algumas vezes melhora a estabilidade se `expr` for
ser numericamente avaliada.  Isso também é útil se Maxima é usado para
gerar programas para rodar em Fortran. Veja também `stringout`.



```maxima
(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                           2
(%o1)            1.0E-155 x  - 5.5 x + 5.2E+155
(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)            (1.0E-155 x - 5.5) x + 5.2E+155
(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 floating point overflow

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i4) ev (expr2, x=1e155);
(%o4)                       7.0E+154
```

<!-- category: Other -->
<!-- keywords: ift -->
<!-- signatures: ift(real_array, imaginary_array) -->
### Function: ift (real_array, imaginary_array)

Transformação rápida inversa discreta de Fourier . `load ("fft")` chama essa função
dentro do Maxima.


`ift` realiza a transformação rápida complexa de Fourier sobre
arrays em ponto flutuante unidimensionais. A transformação inversa é definida como



```maxima
x[j]: sum (y[j] exp (+2 %i %pi j k / n), k, 0, n-1)
```


Veja `fft` para maiores detalhes.

<!-- category: Other -->
<!-- keywords: newton -->
<!-- signatures: newton(expr, x, x_0, eps) -->
### Function: newton (expr, x, x_0, eps)

Retorna uma solução aproximada de `expr = 0` através do método de Newton,
considerando *expr* como sendo uma função de uma variável, *x*.
A busca pela solução começa com `x = x_0`
e prossegue até `abs(expr) < eps`
(com *expr* avaliada para o valor corrente de *x*).


`newton` permite que variáveis indefinidas apareçam em *expr*,
contanto que o teste de terminação `abs(expr) < eps` avalie
para `true` ou `false`.
Dessa forma não é necessário que *expr* avalie para um número.


`load("newton1")` chama essa função.


Veja também `realroots`, `allroots`, `find_root`, e `mnewton`.


Exemplos:











```maxima
(%i1) load ("newton1");
(%o1) /usr/share/maxima/5.10.0cvs/share/numeric/newton1.mac
(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                   1.570675277161251
(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528E-4
(%i4) assume (a > 0);
(%o4)                        [a > 0]
(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                  1.00030487804878 a
(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958E-4 a
```

<!-- category: Other -->
<!-- keywords: polartorect -->
<!-- signatures: polartorect(magnitude_array, phase_array) -->
### Function: polartorect (magnitude_array, phase_array)

Traduz valores complexos da forma `r %e^(%i t)` para a forma `a + b %i`.
`load ("fft")` chama essa função dentro do Maxima. Veja também `fft`.


O módulo e a fase, `r` e `t`, São tomados de *magnitude_array* e
*phase_array*, respectivamente. Os valores originais de arrays de entrada são
substituídos pelas partes real e emaginária, `a` e `b`, no retorno. As saídas são
calculadas como



```maxima
a: r cos (t)
b: r sin (t)
```


Os arrays de entrada devem ter o mesmo tamanho  e ser unidimensionais.
O tamanho do array não deve ser uma potência de 2.


`polartorect` é a função inversa de `recttopolar`.

<!-- category: Other -->
<!-- keywords: recttopolar -->
<!-- signatures: recttopolar(real_array, imaginary_array) -->
### Function: recttopolar (real_array, imaginary_array)

Traduz valores complexos da forma `a + b %i` para a forma `r %e^(%i t)`.
`load ("fft")` chama essa função dentro do Maxima. Veja também `fft`.


As partes real e imaginária, `a` e `b`, são tomadas de *real_array* e
*imaginary_array*, respectivamente. Os valores originais dos arrays de entrada
são substituídos pelo módulo e pelo ângulo, `r` e `t`, no retorno. As saídas são
calculadas como



```maxima
r: sqrt (a^2 + b^2)
t: atan2 (b, a)
```


O ângulo calculado encontra-se no intervalo de `-%pi` a `%pi`. 


Os arrays de entrada devem ter o mesmo tamanho e ser unidimensionais.
O tamanho do array não deve ser uma potência de 2.


`recttopolar` é a função inversa de `polartorect`.

