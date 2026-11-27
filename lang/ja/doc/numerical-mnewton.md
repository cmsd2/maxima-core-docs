## mnewton

<!-- category: Numerical -->
<!-- keywords: mnewton -->
<!-- signatures: mnewton(FuncList, VarList, GuessList) -->
### Function: mnewton (FuncList, VarList, GuessList)

Newton法を使った複数非線形関数の解。
*FuncList*は解くべき関数のリスト、
*VarList*は変数名のリスト、
*GuessList*は初期近似のリストです。


解は
`solve()`が返すのと同じフォーマットで返されます。
もし解が見つからないなら、`[]`が返されます。


この関数は
グローバル変数`newtonepsilon`と`newtonmaxiter`によって制御されます。



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


変数`newtonepsilon`は近似の精度を制御します。
それはまた、計算が浮動小数点で実行されるか、多倍長浮動小数点で実行されるかを制御します。



```maxima
(%i1) (load("mnewton"), fpprec : 25, newtonepsilon : bfloat(10^(-fpprec+5)))$

(%i2) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o2) [[u = 1.066618389595406772591173b0, v = 1.552564766841786450100418b0]]
```


この関数を使うためには、最初に`load("mnewton")`を書いてください。
`newtonepsilon`と`newtonmaxiter`も参照してください。

<!-- category: Numerical -->
<!-- keywords: newtonepsilon -->
<!-- signatures: newtonepsilon -->
### Variable: newtonepsilon

デフォルト値: `10.0^(-fpprec/2)`


`mnewton`関数が解に向かって収束した時を決定する精度。
もし`newtonepsilon`が多倍長浮動小数点なら、`mnewton`計算は多倍長浮動小数点でされます。
`mnewton`も参照してください。

<!-- category: Numerical -->
<!-- keywords: newtonmaxiter -->
<!-- signatures: newtonmaxiter -->
### Variable: newtonmaxiter

デフォルト値: `50`


もし収束しないか収束が遅すぎるなら
`mnewton`関数を止める繰り返しの最大数。


`mnewton`も参照してください。

