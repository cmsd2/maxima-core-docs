## Limits

<!-- category: Series -->
<!-- keywords: lhospitallim -->
<!-- signatures: lhospitallim -->
### Variable: lhospitallim

Default: 4


`lhospitallim`は、
`limit`の中で使われるロピタルの規則の回数の最大数です。
これは
`limit (cot(x)/csc(x), x, 0)`のような場合の
無限ループを防ぎます。

<!-- category: Series -->
<!-- keywords: limit -->
<!-- signatures: limit(expr, x, val, dir), limit(expr, x, val), limit(expr) -->
### Function: limit (expr, x, val, dir)

実変数*x*が値*val*に方向*dir*に近づく時の
*expr*の極限を計算します。
*dir*は、上からの極限には値`plus`を、下からの極限には`minus`を持ち、
また、 (両側極限が計算されることを暗示して)省略することもあります。


`limit`は以下の特殊シンボルを使います:
 `inf` (正の無限大)と`minf` (負の無限大)
出力時には、`und` (未定義), `ind` (不定しかし有界), `infinity` (複素無限大)も使うことがあります。


式の絶対値の極限は正の無限大ですが、式自体の極限は正の無限大でも負の無限大でもない時、
`infinity`(複素数の無限大)が返されます。
これは、`limit(log(x), x, minf)`のように複素偏角の極限が定数である場合、
`limit((-2)^x, x, inf)`のように複素偏角が振動する場合、
`limit(1/x, x, 0)`や`limit(log(x), x, 0)`のように複素偏角が左右の極限のいずれかで異なる場合を、
を含みます。


`lhospitallim`は、
`limit`の中で使われるロピタルの規則の回数の最大数です。
これは
`limit (cot(x)/csc(x), x, 0)`のような場合の
無限ループを防ぎます。


`tlimswitch`が`true`の時、
必要な時`limit`コマンドがテイラー級数展開を使うことを許します。


`limsubst`は、
`limit`が未知の形式の上の代入を試みることを防ぎます。
これは、1を与える`limit (f(n)/f(n+1), n, inf)`のようなバグを避けるためです。
`limsubst`を`true`に設定することはそんな代入を許します。


例えば、`limit (inf-1)`のように、
定数式を整理するために、引数１つの`limit`がしばしばコールされます。



`example (limit)`はいくつかの例を表示します。


方法に関して、
Wang, P., "Evaluation of Definite Integrals by Symbolic
Manipulation", Ph.D. thesis, MAC TR-92, October 1971を参照してください。

<!-- category: Series -->
<!-- keywords: limsubst -->
<!-- signatures: limsubst -->
### Variable: limsubst

デフォルト値: `false` - 
`limit`が未知の形式の上の代入を試みることを防ぎます。


これは、1を与える`limit (f(n)/f(n+1), n, inf)`のようなバグを避けるためです。
`limsubst`を`true`に設定することはそんな代入を許します。
`limit`が未知の形式上で代入をしようとするのを防ぎます。

<!-- category: Series -->
<!-- keywords: tlimit -->
<!-- signatures: tlimit(expr, x, val, dir), tlimit(expr, x, val), tlimit(expr) -->
### Function: tlimit (expr, x, val, dir)

`expr`の`x`に関する`val`
でのテイラー級数展開の方向`dir`からの極限を取ります。

<!-- category: Series -->
<!-- keywords: tlimswitch -->
<!-- signatures: tlimswitch -->
### Variable: tlimswitch

デフォルト値: `true`


`tlimswitch`が`true`の時、
`limit`コマンドは
もし入力式が直接計算できないなら、
テイラー級数展開を使います。
これは、`limit(x/(x-1)-1/log(x),x,1,plus)`のような
極限の評価を許します。
`tlimswitch`が`false`で、
入力式の極限は直接には計算できない時は、
`limit`は、未評価の極限式を返します。

