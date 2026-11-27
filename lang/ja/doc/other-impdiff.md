## impdiff

<!-- category: Other -->
<!-- keywords: implicit_derivative -->
<!-- signatures: implicit_derivative(f, indvarlist, orderlist, depvar) -->
### Function: implicit_derivative (f, indvarlist, orderlist, depvar)

このサブルーチンは多変数関数の陰導関数を計算します。
*f*は配列関数で、
インデックスは*indvarlist*順の微分の階数です;
*indvarlist*は独立変数リストです;
*orderlist*は望みの次数です;
*depvar*は従属変数です。


この関数を使うには、最初に`load("impdiff")`を書いてください。

