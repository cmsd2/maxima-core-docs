## Ponto Flutuante

<!-- category: Other -->
<!-- keywords: algepsilon -->
<!-- signatures: algepsilon -->
### Variable: algepsilon

Valor padrão: 10^8



`algepsilon` é usada por `algsys`.

<!-- category: Other -->
<!-- keywords: bffac -->
<!-- signatures: bffac(expr, n) -->
### Function: bffac (expr, n)

Versão para grandes números em ponto flutuante da função
`factorial` (usa o artifício gamma).  O segundo argumento informa quantos dígitos reter e retornar,
isso é uma boa idéia para requisitar precisão adicional.


`load ("bffac")` chama essa função.

<!-- category: Other -->
<!-- keywords: bfloat -->
<!-- signatures: bfloat(expr) -->
### Function: bfloat (expr)

Converte todos os números e funções de números em *expr* para grandes números em 
ponto flutuante (bigfloat).  O número de algarismos significativos no grande número em ponto flutuante resultante é especificado através da variável global `fpprec`.


Quando `float2bf` for `false` uma mensagem de alerta é mostrada quando
uma número em ponto flutuante (float) é convertido em um grande número em ponto flutuante (bigfloat - uma vez que
isso pode resultar em perda de precisão).

<!-- category: Other -->
<!-- keywords: bfloatp -->
<!-- signatures: bfloatp(expr) -->
### Function: bfloatp (expr)

Retorna `true` se a avaliação da *expr* resultar em um grande número em ponto flutuante, de outra forma retorna `false`.

<!-- category: Other -->
<!-- keywords: bfpsi, bfpsi0 -->
<!-- signatures: bfpsi(n, z, fpprec), bfpsi0(z, fpprec) -->
### Function: bfpsi (n, z, fpprec)

`bfpsi` é a função `polygamma` de argumentos reais *z* e ordem de inteiro *n*.
`bfpsi0` é a função `digamma`. 
`bfpsi0 (z, fpprec)` é equivalente a `bfpsi (0, z, fpprec)`.


Essas funções retornam valores em grandes números em ponto flutuante.
*fpprec* é a precisão do valor de retorno dos grandes números em ponto flutuante.






`load ("bffac")` chama essas funções.

<!-- category: Other -->
<!-- keywords: bftorat -->
<!-- signatures: bftorat -->
### Variable: bftorat

Valor padrão: `false`


`bftorat` controla a conversão de `bfloats` para
números racionais. 
Quando `bftorat` for `false`,
`ratepsilon` será usada para
controlar a conversão (isso resulta em números racionais relativametne
pequenos).
Quando `bftorat` for `true`,
o número racional gerado irá
representar precisamente o `bfloat`.

<!-- category: Other -->
<!-- keywords: bftrunc -->
<!-- signatures: bftrunc -->
### Variable: bftrunc

Valor padrão: `true`


`bftrunc` faz com que tilhas de zeros em grandes números em ponto flutuante
diferentes de zero sejam ocultadas.  Desse modo, se `bftrunc` for `false`, `bfloat (1)`
será mostrado como `1.000000000000000B0`. De outra forma, será mostrado como
`1.0B0`.

<!-- category: Other -->
<!-- keywords: cbffac -->
<!-- signatures: cbffac(z, fpprec) -->
### Function: cbffac (z, fpprec)

Fatorial complexo de grandes números em ponto flutuante.


`load ("bffac")` chama essa função.

<!-- category: Other -->
<!-- keywords: float -->
<!-- signatures: float(expr) -->
### Function: float (expr)

Converte inteiros, números racionais e grandes números em ponto flutuante em *expr*
para números em ponto flutuante.  Da mesma forma um `evflag`, `float` faz com que
números racionais não-inteiros e grandes números em ponto flutuante sejam convertidos para
ponto flutuante.

<!-- category: Other -->
<!-- keywords: float2bf -->
<!-- signatures: float2bf -->
### Variable: float2bf

Valor padrão: `false`

 

Quando `float2bf` for `false`, uma mensagem de alerta é mostrada quando
um número em ponto flutuante é convertido em um grande número em ponto flutuante (uma vez que
isso pode resultar em perda de precisão).

<!-- category: Other -->
<!-- keywords: floatnump -->
<!-- signatures: floatnump(expr) -->
### Function: floatnump (expr)

Retorna `true` se *expr* for um número em ponto flutuante, de outra forma retorna `false`.

<!-- category: Other -->
<!-- keywords: fpprec -->
<!-- signatures: fpprec -->
### Variable: fpprec

Valor padrão: 16


`fpprec` é o número de algarismos significativos para aritmética sobre grandes números em ponto flutuante
`fpprec` não afeta cálculos sobre números em ponto flutuante comuns.


Veja também `bfloat` e `fpprintprec`.

<!-- category: Other -->
<!-- keywords: fpprintprec -->
<!-- signatures: fpprintprec -->
### Variable: fpprintprec

Valor padrão: 0


`fpprintprec` é o n;umero de dígitos a serem mostrados na tela quando no caso de nuúmeros em ponto flutuante e no caso de grandes números em ponto flutuante.


Para números em ponto flutuante comuns,
quando `fpprintprec` tiver um valor entre 2 e 16  (inclusive),
o n;umero de dígitos mostrado na tela é igual a `fpprintprec`.
De outra forma, `fpprintprec` é 0, ou maior que 16,
e o número de dígitos mostrados é 16.


Para grandes números em ponto flutuante,
quando `fpprintprec` tiver um valor entre 2 e `fpprec` (inclusive),
o n;umero de dígitos mostrados é giaul a `fpprintprec`.
De outra forma, `fpprintprec` é 0, ou maior que `fpprec`,
e o n;umero de dígitos mostrados é igual a `fpprec`.


`fpprintprec` não pode ser 1.

