## cobyla

<!-- category: Numerical -->
<!-- keywords: bf_fmin_cobyla -->
<!-- signatures: bf_fmin_cobyla(F, X, Y), bf_fmin_cobyla(F, X, Y, optional_args) -->
### Function: bf_fmin_cobyla (F, X, Y)

この関数は、
多倍長浮動小数点演算が使われること、
*rhoend*のデフォルト値が`10^(fpprec/2)`であることを除いて、
`fmin_cobyla`と同一です。


更に知るには`fmin_cobyla`を参照してください。


`load("fmin_cobyla")`はこの関数をロードします。

<!-- category: Numerical -->
<!-- keywords: fmin_cobyla -->
<!-- signatures: fmin_cobyla(F, X, Y), fmin_cobyla(F, X, Y, optional_args) -->
### Function: fmin_cobyla (F, X, Y)

オプションの制約の組を条件として多変数*X*に関する式*F*の近似的最小を返します。
*Y*は*X*に対する初期推測のリストです。


*F*は関数名やラムダ式ではなく、通常の式でなければいけません。


`optional_args`は、
`symbol = value`のように指定される付加的な引数を表します。
認識されるオプションの引数は以下の通りです:



**constraints** — *X*が満たさなければいけない不等式と等式の制約のリスト。
不等式制約は、
形式`g(X) >= h(X)`もしくは`g(X) <= h(X)`の
実際の不等式でなければいけません。
等式制約は
形式`g(X) = h(X)`のものでなければいけません。
**rhobeg** — 単体のサイズを制御する内部RHO変数の初期値(デフォルトは1.0)。
**rhoend** — 要望される最終値rhoパラメータ。
近似的に変数の精度です。(デフォルトは1d-6)
**iprint** — 冗長な出力レベル(デフォルトは0)。 
- *
0 - 出力なし
- *
1 - 計算終了時にまとめ
- *
2 - 変数のベクトルやRHOが減らされる時のある函数情報と一緒に、
RHOとSIGMAのそれぞれの新しい値が印字されます。
- *
3 - 2と同様ですが、F(X)が計算される時情報が印字されます。
**maxfun** — 函数評価の最大回数(デフォルトは1000)。


返す時、ベクトルが与えられます:


1. 最小を与える変数の値。
これは
*X*の中にリストされた変数のそれぞれに関する
形式`var = value`の
要素のリストです。
2. 最小化された函数値
3. 函数評価の回数
4. 以下の意味を持つリターンコード
 

  1. 0 - エラーなし。
  2. 1 - 函数評価の最大回数の上限に到達した。
  3. 2 - 進行を妨げる丸め誤差。


`load("fmin_cobyla")`はこの関数をロードします。

