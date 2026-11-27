## ggf

<!-- category: Other -->
<!-- keywords: ggf -->
<!-- signatures: ggf(l) -->
### Function: ggf (l)

(もし母関数が２つの多項式の分数なら)
与えられた最初の数項に対する、
数列の母関数を計算します。
*l*は数のリストです。


解は２つの多項式の分数として返されます。
解が見つからなかったら、`done`を返します。


この関数は
グローバル変数*GGFINFINITY*と*GGFCFMAX*で制御されます。
*GGFINFINITY*と*GGFCFMAX*も参照してください。


この関数を使うには、最初に`load("ggf")`を書いてください。

<!-- category: Other -->
<!-- keywords: GGFCFMAX -->
<!-- signatures: GGFCFMAX -->
### Variable: GGFCFMAX

デフォルト値: 3


これは
関数`ggf`のオプション変数です。


母関数の連分数を計算する時、
もし
*GGFCFMAX*個の部分商を計算した後、よい結果が見つからないなら
(*GGFINFINITY*フラグを参照してください)、
母関数は２つの多項式の分数でないように考えられ、
関数は抜けます。
もっと複雑な母関数のためにより大きな値を自由に入れてください。


`ggf`も参照してください。

<!-- category: Other -->
<!-- keywords: GGFINFINITY -->
<!-- signatures: GGFINFINITY -->
### Variable: GGFINFINITY

デフォルト値: 3


これは関数`ggf`のオプション変数です。


母関数の連分数を計算する時、
(厳密に)*GGFINFINITY*より大きな次数を持つ
部分商は捨てられます。
現在のコンバージェントは母関数の正確な値として考えられます;
部分商すべての次数はたいてい0か1です;
もしより大きな値を使うなら、
十分精度の高い計算を行うために十分な項を与えるべきです。


`ggf`も参照してください。

