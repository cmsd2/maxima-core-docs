## Data Types and Structures

<!-- category: IO -->
<!-- keywords: concat -->
<!-- signatures: concat(arg_1, arg_2, ...) -->
### Function: concat (arg_1, arg_2, ...)

引数を連結します。
引数はアトムに評価されなければいけません。
もし最初の引数がシンボルなら戻り値はシンボルで、
そうでなければ文字列です。


`concat`は引数を評価します。
シングルクォート`'`は評価を抑制します。



```maxima
(%i1) y: 7$
(%i2) z: 88$
(%i3) concat (y, z/2);
(%o3)                          744
(%i4) concat ('y, z/2);
(%o4)                          y44
```


`concat`によって組み立てられたシンボルは値に割り当てられたり、式の中に現れたりします。
`::` (ダブルコロン)割り当て演算子は左辺を評価します。



```maxima
(%i5) a: concat ('y, z/2);
(%o5)                          y44
(%i6) a:: 123;
(%o6)                          123
(%i7) y44;
(%o7)                          123
(%i8) b^a;

                               y44
(%o8)                         b

(%i9) %, numer;
                               123
(%o9)                         b
```


`concat (1, 2)`は数のように見えますが、文字列であることに注意してください。



```maxima
(%i10) concat (1, 2) + 3;
(%o10)                       12 + 3
```

See also: `::`.

<!-- category: IO -->
<!-- keywords: sconcat -->
<!-- signatures: sconcat(arg_1, arg_2, ...) -->
### Function: sconcat (arg_1, arg_2, ...)

引数を文字列に連結します。
`concat`と違い、引数はアトムである必要は*ありません*。



```maxima
(%i1) sconcat ("xx[", 3, "]:", expand ((x+y)^3));
(%o1)               xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
```

See also: `concat`.

<!-- category: IO -->
<!-- keywords: string -->
<!-- signatures: string(expr) -->
### Function: string (expr)

`expr`を、ただまるでタイプされたようにMaximaの線形表記に変換します。


`string`の戻り値は文字列であり、
計算の中で使うことはできません。

<!-- category: IO -->
<!-- keywords: stringdisp -->
<!-- signatures: stringdisp -->
### Variable: stringdisp

デフォルト値: `false`


`stringdisp`が`true`の時、
文字列はダブルクォートマークで囲まれて表示されます。
そうでなければクォートマークは表示されません。


関数定義を表示する時はいつも、`stringdisp`は `true`です。


例:











```maxima
(%i1) stringdisp: false$
(%i2) "This is an example string.";
(%o2)              This is an example string.

(%i3) foo () :=
      print ("This is a string in a function definition.");

(%o3) foo() := 
              print("This is a string in a function definition.")
(%i4) stringdisp: true$
(%i5) "This is an example string.";
(%o5)             "This is an example string."
```

