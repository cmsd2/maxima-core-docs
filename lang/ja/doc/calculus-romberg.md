## romberg

<!-- category: Calculus -->
<!-- keywords: romberg -->
<!-- signatures: romberg(expr, x, a, b), romberg(F, a, b) -->
### Function: romberg (expr, x, a, b)

Romberg法による数値積分を計算します。


`romberg(expr, x, a, b)`は
積分`integrate(expr, x, a, b)`の概算を返します。


*expr*は、
*x*が浮動小数点値にバインドされた時
浮動小数点値に評価される
式でなければいけません。


`romberg(F, a, b)`は
積分`integrate(F(x), x, a, b)`の概算を返します。
ここで、`x`は*F*の名付けられない唯一の引数を表します;
実際の引数は`x`と名付けられません。
*F*は、
引数が浮動小数点値の時、浮動小数点値を返す
MaximaかLispの関数でなければいけません。
*F*は翻訳またはコンパイルされたMaxima関数を指定することができます。


`romberg`の精度は
グローバル変数`rombergabs`と`rombergtol`によって決定されます。
`romberg`は
連続する近似の間の絶対差が`rombergabs`よりも小さい時か、
連続する近似に関する相対差が`rombergtol`よりも小さい時、
成功のうちに終了します。
従って、
`rombergabs`が0.0 (デフォルト)の時、
相対誤差テストだけが`romberg`に効果を持ちます。


`romberg`は
あきらめる前に、せいぜい`rombergit`回、ステップサイズを半分にします;
それゆえ、関数評価の最大回数は`2^rombergit`です。
もし
`rombergabs`や`rombergtol`によって確立される誤差基準が満たされないなら、
`romberg`はエラーメッセージを印字します。
`romberg`はいつも、少なくとも`rombergmin`回の繰り返しを行います;
これは、被積分関数が振動的な時、見せかけの終了を防ぐつもりの発見的方法です。


`romberg`は、
積分変数を特定の値にバインド(する前ではなく)した後、
被積分関数を繰り返し評価します。
この評価ポリシーは、多次元積分を計算するための
`romberg`の入れ子のコールを可能にします。
しかしながら、誤差計算は
入れ子の積分の誤差を考慮しないので、エラーは過小評価されるかもしれません。
また、多次元問題のために特別に工夫された方法はより少ない関数評価で同じ精度をもたらす可能性があります。


`load("romberg")`はこの関数をロードします。


`QUADPACK`、数値積分関数のコレクションも参照してください。


例:


1次元積分。













```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) f(x) := 1/((x - 1)^2 + 1/100) + 1/((x - 2)^2 + 1/1000)
              + 1/((x - 3)^2 + 1/200);
                    1                 1                1
(%o2) f(x) := -------------- + --------------- + --------------
                     2    1           2    1            2    1
              (x - 1)  + ---   (x - 2)  + ----   (x - 3)  + ---
                         100              1000              200
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) rombergit : 15;
(%o4)                          15
(%i5) estimate : romberg (f(x), x, -5, 5);
(%o5)                   173.6730736617464
(%i6) exact : integrate (f(x), x, -5, 5);
(%o6) 10 sqrt(10) atan(70 sqrt(10))
 + 10 sqrt(10) atan(30 sqrt(10)) + 10 sqrt(2) atan(80 sqrt(2))
 + 10 sqrt(2) atan(20 sqrt(2)) + 10 atan(60) + 10 atan(40)
(%i7) abs (estimate - exact) / exact, numer;
(%o7)                7.5527060865060088E-11
```


`romberg`の入れ子のコールで実装された
2次元積分。













```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) g(x, y) := x*y / (x + y);
                                    x y
(%o2)                   g(x, y) := -----
                                   x + y
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) estimate : romberg (romberg (g(x, y), y, 0, x/2), x, 1, 3);
(%o4)                   0.81930239628356
(%i5) assume (x > 0);
(%o5)                        [x > 0]
(%i6) integrate (integrate (g(x, y), y, 0, x/2), x, 1, 3);
                                          3
                                    2 log(-) - 1
                    9                     2        9
(%o6)       - 9 log(-) + 9 log(3) + ------------ + -
                    2                    6         2
(%i7) exact : radcan (%);
                    26 log(3) - 26 log(2) - 13
(%o7)             - --------------------------
                                3
(%i8) abs (estimate - exact) / exact, numer;
(%o8)                1.3711979871851024E-10
```

<!-- category: Calculus -->
<!-- keywords: rombergabs -->
<!-- signatures: rombergabs -->
### Variable: rombergabs

デフォルト値: 0.0


`romberg`の精度は、
グローバル変数`rombergabs`と`rombergtol`で決定されます。
`romberg`は
連続する近似の間の絶対差が`rombergabs`よりも小さい時か、
連続する近似に関する相対差が`rombergtol`よりも小さい時、
成功のうちに終了します。
従って、
`rombergabs`が0.0 (デフォルト)の時、
相対誤差テストだけが`romberg`に効果を持ちます。


`rombergit`と`rombergmin`も参照してください。

<!-- category: Calculus -->
<!-- keywords: rombergit -->
<!-- signatures: rombergit -->
### Variable: rombergit

デフォルト値: 11


`romberg`は
あきらめる前に、せいぜい`rombergit`回、ステップサイズを半分にします;
それゆえ、関数評価の最大回数は`2^rombergit`です。
`romberg`はいつも、少なくとも`rombergmin`回の繰り返しを行います;
これは、被積分関数が振動的な時、見せかけの終了を防ぐつもりの発見的方法です。


`rombergabs`と`rombergtol`も参照してください。

<!-- category: Calculus -->
<!-- keywords: rombergmin -->
<!-- signatures: rombergmin -->
### Variable: rombergmin

デフォルト値: 0


`romberg`はいつも、少なくとも`rombergmin`回の繰り返しを行います;
これは、被積分関数が振動的な時、見せかけの終了を防ぐつもりの発見的方法です。


`rombergit`, `rombergabs`, `rombergtol`も参照してください。

<!-- category: Calculus -->
<!-- keywords: rombergtol -->
<!-- signatures: rombergtol -->
### Variable: rombergtol

デフォルト値: 1e-4


`romberg`の精度は
グローバル変数`rombergabs`と`rombergtol`によって決定されます。
`romberg`は
連続する近似の間の絶対差が`rombergabs`よりも小さい時か、
連続する近似に関する相対差が`rombergtol`よりも小さい時、
成功のうちに終了します。
従って、
`rombergabs`が0.0 (デフォルト)の時、
相対誤差テストだけが`romberg`に効果を持ちます。


`rombergit`と`rombergmin`も参照してください。

