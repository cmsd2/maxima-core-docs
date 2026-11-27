## Operators

<!-- category: Programming -->
<!-- keywords: ** -->
<!-- signatures: ** -->
### Function: **

べき乗演算子。
Maximaは入力の中で `**`を `^`と同じ演算子と認識し、
1次元出力の中では `^`として表示し、
また、2次元出力の中では指数を上付き添字として配置します。


`fortran`関数は、入力が `**`でも `^`でも、
べき乗演算子を `**`として表示します。


例:









```maxima
(%i1) is (a**b = a^b);
(%o1)                         true
(%i2) x**y + x^z;
                              z    y
(%o2)                        x  + x
(%i3) string (x**y + x^z);
(%o3)                        x^z+x^y
(%i4) fortran (x**y + x^z);
      x**z+x**y
(%o4)                         done
```

See also: `fortran`.

<!-- category: Programming -->
<!-- keywords: +, -, *, /, ^ -->
<!-- signatures: -, *, /, ^ -->
### Function: +

シンボル `+` `*` `/` `^`はそれぞれ、
足し算、かけ算、割り算、べき乗を表します。
これらの演算子の名前は `"+"` `"*"` `"/"` `"^"`です。
これらは関数や演算子の名前が求められるところで使います。


シンボル `+`や `-`はそれぞれ、プラスとマイナスの単項演算子を示し、
それらの名前はそれぞれ `"+"`と`"-"`です。


引き算 `a - b`はMaximaの中では足し算 `a + (- b)`として表されます。
`a + (- b)`のような式は引き算として表示されます。
Maximaは `"-"`を足し算の単項逆元演算子の名前としてのみ認識して、
二項引き算演算子としては認識しません。


Maximaの中では割り算`a / b`をかけ算`a * b^(- 1)`として表現します。
`a * b^(- 1)`のような式は割り算として表示されます。
Maximaは`"/"`を割り算演算子の名前として認識します。


足し算とかけ算はn項可換演算子です。
割り算とべき乗は二項の非可換演算子です。


Maximaは正準表現を構成するために可換演算子のオペランド(訳注：引数)を並べ替えます。
順序は内部的には `orderlessp`で決定します。
表示のためには、足し算の順序は `ordergreatp`で決定し、
かけ算は内部的な順序と同じです。


算術計算は、数リテラル（整数、有理数、通常の浮動小数点、多倍長浮動小数点）上で実行されます。
べき乗を除いて、数に対するすべての算術演算子は数に整理されます。
べき乗は、オペランドが通常の浮動小数点か多倍長浮動小数点の時、もしくは結果が厳密に整数もしくは有理数の時、数に整理されます;
そうでなければ、べき乗は `sqrt`か他のべき乗に整理されるか、そのまま残されます。


浮動小数点の伝搬が算術計算に適用されます:
もしどれか１つでもオペランドが多倍長浮動小数点なら、結果は多倍長浮動小数点です;
そうでなければ、もしどれか１つでもオペランドが通常の浮動小数点なら、結果は通常の浮動小数点です;
そうでなければオペランドは有理数か整数であり、結果は有理数か整数です。


算術計算は式整理であって、評価ではありません。
従って、クォートされた（しかし整理される）式の中で算術計算は実行されます。


算術演算は、
グローバルフラグ `listarith`が `true`の時
リストに対して要素毎に適用され、
行列に対しては常に要素毎に適用されます。
オペランドの１つがリストか行列であり、もう１つのオペランドが別のタイプの時、
他のオペランドはリストか行列の要素のそれぞれに組み合わされます。


例:


足し算とかけ算は、n項可換演算子です。
Maximaは、正準表現を構成するために、可換演算子のオペランドを並べ替えます。
それらの名前はそれぞれ `"+"`と `"*"`です。











```maxima
(%i1) c + g + d + a + b + e + f;
(%o1)               g + f + e + d + c + b + a
(%i2) [op (%), args (%)];
(%o2)              [+, [g, f, e, d, c, b, a]]
(%i3) c * g * d * a * b * e * f;
(%o3)                     a b c d e f g
(%i4) [op (%), args (%)];
(%o4)              [*, [a, b, c, d, e, f, g]]
(%i5) apply ("+", [a, 8, x, 2, 9, x, x, a]);
(%o5)                    3 x + 2 a + 19
(%i6) apply ("*", [a, 8, x, 2, 9, x, x, a]);
                                 2  3
(%o6)                       144 a  x
```


割り算とべき乗は、二項の非可換演算子です。
それらの名前はそれぞれ `"/"`と `"^"`です。








```maxima
(%i1) [a / b, a ^ b];
                              a   b
(%o1)                        [-, a ]
                              b
(%i2) [map (op, %), map (args, %)];
(%o2)              [[/, ^], [[a, b], [a, b]]]
(%i3) [apply ("/", [a, b]), apply ("^", [a, b])];
                              a   b
(%o3)                        [-, a ]
                              b
```


引き算と割り算は内部的にはそれぞれ、足し算とかけ算を使って表現されます。







```maxima
(%i1) [inpart (a - b, 0), inpart (a - b, 1), inpart (a - b, 2)];
(%o1)                      [+, a, - b]
(%i2) [inpart (a / b, 0), inpart (a / b, 1), inpart (a / b, 2)];
                                   1
(%o2)                       [*, a, -]
                                   b
```


計算は数リテラルに対して実行されます。
浮動小数点伝搬が適用されます。







```maxima
(%i1) 17 + b - (1/2)*29 + 11^(2/4);
                                       5
(%o1)                   b + sqrt(11) + -
                                       2
(%i2) [17 + 29, 17 + 29.0, 17 + 29b0];
(%o2)                   [46, 46.0, 4.6b1]
```


算術計算は式整理であって、評価ではありません。









```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) '(17 + 29*11/7 - 5^3);
                              29 11    3
(%o2)                    17 + ----- - 5
                                7
(%i3) simp : true;
(%o3)                         true
(%i4) '(17 + 29*11/7 - 5^3);
                                437
(%o4)                         - ---
                                 7
```


算術計算は（`listarith`に依存して）リストや行列に対して要素毎に実行されます。













```maxima
(%i1) matrix ([a, x], [h, u]) - matrix ([1, 2], [3, 4]);

                        [ a - 1  x - 2 ]
(%o1)                   [              ]
                        [ h - 3  u - 4 ]

(%i2) 5 * matrix ([a, x], [h, u]);

                          [ 5 a  5 x ]
(%o2)                     [          ]
                          [ 5 h  5 u ]
(%i3) listarith : false;
(%o3)                         false
(%i4) [a, c, m, t] / [1, 7, 2, 9];
                          [a, c, m, t]
(%o4)                     ------------
                          [1, 7, 2, 9]
(%i5) [a, c, m, t] ^ x;
                                      x
(%o5)                     [a, c, m, t]
(%i6) listarith : true;
(%o6)                         true
(%i7) [a, c, m, t] / [1, 7, 2, 9];
                              c  m  t
(%o7)                     [a, -, -, -]
                              7  2  9
(%i8) [a, c, m, t] ^ x;
                          x   x   x   x
(%o8)                   [a , c , m , t ]
```

<!-- category: Programming -->
<!-- keywords: . -->
<!-- signatures: . -->
### Function: .

行列（非可換）かけ算のためのドット演算子。
`"."`をこの意味で用いる時、
例えば `A . B`のように両側にスペースを置かなければいけません。
これで浮動小数点の小数点と区別します。


`dot`や
`dot0nscsimp`,
`dot0simp`,
`dot1simp`,
`dotassoc`,
`dotconstrules`,
`dotdistrib`,
`dotexptsimp`,
`dotident`,
`dotscrules`.
も参照してください。

<!-- category: Programming -->
<!-- keywords: : -->
<!-- signatures: : -->
### Function: :

割り当て演算子。


左辺が（添字のない）単純変数の時、 `:`は右辺を評価し、その値を左辺に関連づけます。


左辺がリストや行列、宣言されたMaxima配列、Lisp配列の添字指定された要素の時、
右辺がその要素に割り当てられます。
添字は存在している要素を示していなければなりません;
先に列挙した対象は、存在していない要素を名付けることで拡張することはできません。


左辺が未宣言のMaxima配列の添字指定された要素の時、
もし既に存在しているなら、右辺はその要素に割り当てられ、
もしまだ存在していなければ新しい要素が確保されます。


左辺が単純変数や添字あり変数のリストの時、
右辺はリストに評価されなければなりません。
そして、右辺の要素が左辺の要素に平行に割り当てられます。


`kill`や`remvalue`も参照してください。
それらは左辺とその値の関連をアンドゥします。


例:


単純変数への割り当て








```maxima
(%i1) a;
(%o1)                           a
(%i2) a : 123;
(%o2)                          123
(%i3) a;
(%o3)                          123
```


リストの要素への割り当て








```maxima
(%i1) b : [1, 2, 3];
(%o1)                       [1, 2, 3]
(%i2) b[3] : 456;
(%o2)                          456
(%i3) b;
(%o3)                      [1, 2, 456]
```


割り当ては未宣言配列を生成する。










```maxima
(%i1) c[99] : 789;
(%o1)                          789
(%i2) c[99];
(%o2)                          789
(%i3) c;
(%o3)                           c
(%i4) arrayinfo (c);
(%o4)                   [hashed, 1, [99]]
(%i5) listarray (c);
(%o5)                         [789]
```


多重割り当て









```maxima
(%i1) [a, b, c] : [45, 67, 89];
(%o1)                     [45, 67, 89]
(%i2) a;
(%o2)                          45
(%i3) b;
(%o3)                          67
(%i4) c;
(%o4)                          89
```


多重割り当ては平行に実行されます。
この例では`a`と`b`の値が置換されます。









```maxima
(%i1) [a, b] : [33, 55];
(%o1)                       [33, 55]
(%i2) [a, b] : [b, a];
(%o2)                       [55, 33]
(%i3) a;
(%o3)                          55
(%i4) b;
(%o4)                          33
```

See also: `kill`, `remvalue`.

<!-- category: Programming -->
<!-- keywords: :: -->
<!-- signatures: :: -->
### Function: ::

割り当て演算子。


`::`は、`::`は右辺はもちろん左辺も評価することを除いて、`:`と同じです。


例:













```maxima
(%i1) x : 'foo;
(%o1)                          foo
(%i2) x :: 123;
(%o2)                          123
(%i3) foo;
(%o3)                          123
(%i4) x : '[a, b, c];
(%o4)                       [a, b, c]
(%i5) x :: [11, 22, 33];
(%o5)                     [11, 22, 33]
(%i6) a;
(%o6)                          11
(%i7) b;
(%o7)                          22
(%i8) c;
(%o8)                          33
```

See also: `:`.

<!-- category: Programming -->
<!-- keywords: ::= -->
<!-- signatures: ::= -->
### Function: ::=

マクロ関数定義の演算子。
`::=`は、引数をクォートする関数（歴史的理由によりマクロと呼ばれる）を定義します。
そして、それが返す式（マクロ展開と呼ばれる）はマクロが呼ばれた文脈の中で評価されます。
それ以外はマクロ関数は通常の関数と同じです。


`macroexpand`は（評価せずに）マクロ展開を返します。
`foo`がマクロ関数の時、
`macroexpand (foo (x))`に続けて ```%`を実行すると、
それは `foo (x)`と同値です。


`::=`は、新しいマクロ関数の名前をグローバルリスト `macros`に追加します。
`kill`や `remove`, `remfunction`は、マクロ関数定義をアンバインドし、
`macros`から名前を削除します。


`fundef`や `dispfun`はそれぞれマクロ関数定義を返し、
それをラベルに割り当てます。


評価対象となる式を構成するために、
マクロ関数は一般的に`buildq`, `splice`式を含みます。


例


マクロ関数は引数をクォートします。
だから、メッセージ(1)は `y - z`の値ではなく、 `y - z`を示します。
マクロ展開（クォートされた式 `'(print ("(2) x is equal to", x)`）は、
マクロが呼ばれた文脈（表示メッセージ(2)）の中で評価されます。











```maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$
(%i4) printq1 (x) ::= block (print ("(1) x is equal to", x),
      '(print ("(2) x is equal to", x)))$
(%i5) printq1 (y - z);
(1) x is equal to y - z
(2) x is equal to %pi
(%o5)                                 %pi
```


通常の関数は引数を評価します。だから、メッセージ(1)は `y - z`の値を示します。
戻り値は評価されず、従って、メッセージ(2)は ```%`で陽に評価されるまで出力されません。












```maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$
(%i4) printe1 (x) := block (print ("(1) x is equal to", x),
      '(print ("(2) x is equal to", x)))$
(%i5) printe1 (y - z);
(1) x is equal to 1234 - 1729 w
(%o5)                     print((2) x is equal to, x)
(%i6) ''%;
(2) x is equal to %pi
(%o6)                                 %pi
```


`macroexpand`はマクロ展開を返します。
`foo`がマクロ関数の時、
`macroexpand (foo (x))`の後 ```%`を実行すると、`foo (x)`と同値です。












```maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$
(%i4) g (x) ::= buildq ([x], print ("x is equal to", x))$
(%i5) macroexpand (g (y - z));
(%o5)                     print(x is equal to, y - z)
(%i6) ''%;
x is equal to 1234 - 1729 w
(%o6)                            1234 - 1729 w
(%i7) g (y - z);
x is equal to 1234 - 1729 w
(%o7)                            1234 - 1729 w
```

See also: `macroexpand`, `macros`, `kill`, `remove`, `remfunction`, `fundef`, `dispfun`, `buildq`, `splice`.

<!-- category: Programming -->
<!-- keywords: := -->
<!-- signatures: := -->
### Function: :=

関数定義の演算子。
`f(x_1, .., x_n) := expr`は、
引数が*x_1*, ..., *x_n*で関数本体が*expr*の、*f*という名前の関数を定義します。
`:=`は（クォートクォート````で陽に評価されない限り）関数本体は評価しません。
定義される関数は（引数をかっこでくくる）通常のMaxima関数か、（引数をかぎかっこでくくる）配列関数です。


最後の引数*x_n*が要素１つのリストの時、`:=`で定義された関数は可変の数の引数をとります。
実際の引数は、形式的な引数*x_1*, ..., *x_(n - 1)*に一対一に割り当てられ、
さらに引数があれば、*x_n*にリストとして割り当てられます。


関数定義すべては、同じ名前空間を使います;
別の関数`g`の中で関数`f`を定義することは、`f`のスコープを`g`に限定しません。
しかし、`local(f)`は、関数`f`の定義を`local`が現れたブロックや他の合成式内に限定します。


もしある形式引数*x_k*がクォートされたシンボルなら、`:=`で定義された関数は対応する実際の引数を評価しません。
それ以外の場合、実際の引数はすべて評価されます。


`define`や`::=`も参照してください。


例:


`:=`は（クォートクォートで陽に評価されない限り）関数本体を評価しません。










```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) F1 (x, y) := expr;
(%o2)                   F1(x, y) := expr
(%i3) F1 (a, b);
(%o3)                    cos(y) - sin(x)
(%i4) F2 (x, y) := ''expr;
(%o4)              F2(x, y) := cos(y) - sin(x)
(%i5) F2 (a, b);
(%o5)                    cos(b) - sin(a)
```


`:=`で定義された関数は、通常のMaxima関数か、配列関数です。







```maxima
(%i1) G1 (x, y) := x.y - y.x;
(%o1)               G1(x, y) := x . y - y . x
(%i2) G2 [x, y] := x.y - y.x;
(%o2)                G2     := x . y - y . x
                       x, y
```


最後の引数*x_n*が要素１つのリストの時、
`:=`で定義された関数は、可変の数の引数を取ります。







```maxima
(%i1) H ([L]) := apply ("+", L);
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


`local`はローカル関数定義を可能にします。









```maxima
(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x
(%i2) foo (100);
(%o2)                         - 99
(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200
(%i4) foo (100);
(%o4)                         - 99
```

See also: `local`, `define`, `::=`.

<!-- category: Programming -->
<!-- keywords: <, <=, >=, > -->
<!-- signatures: <=, >=, > -->
### Function: < (=)

シンボル `<`  `<=` `>=` `>`はそれぞれ、小なり、以下、以上、大なり、を表します。
これらの演算子の名前は、 `"<"`、 `"<="`、 `">="`、 `">"`です。
それらは関数や演算子の名前が求められるところで使われます。


これらの関係演算子はすべて二項演算子です;
`a < b < c`のような構成をMaximaは認識しません。


関数 `is`や `maybe`、
プログラミング構成子 `if`, `while`, `unless`が
関係式をブーリアン値に評価します。
そうでなければ、関係式はブーリアン値に評価されたり整理されたりしませんが、
関係式の引数は（評価がクォーテーションによって妨げられないかぎり）評価されます。


関係式が `true`もしくは `false`に評価できない時、
`is`や `if`の振る舞いは、グローバルフラグ `prederror`が決定します。
`prederror`が `true`の時、 `is`や `if`はエラーをトリガーします。
`prederror`が `false`の時、
`is`は `unknown`を返し、
`if`は部分的に評価された条件式を返します。


`maybe`はいつも、 `prederror`が `false`であるかのように振る舞い、
`while`や `unless`はいつも、 `prederror`が `true`であるかのように振る舞います。


関係演算子はリストやほかの集合上で展開されることはありません。


`=`や `#`、 `equal`、 `notequal`も参照してください。


例:


いくつかの関数やプログラミング構成子が関係式をブーリアン値に評価します。











```maxima
(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]
(%i2) is (x < y);
(%o2)                         true
(%i3) maybe (y > z);
(%o3)                         false
(%i4) if x >= z then 1 else 0;
(%o4)                           0
(%i5) block ([S], S : 0, for i:1 while i <= 100 do S : S + i, 
             return (S));
(%o5)                         5050
```


そうでなければ関係式はブーリアン値に評価されたり整理されたりしませんが、
関係式の引数は評価されます。








```maxima
(%o1)                    [123, 456, 789]
(%i2) [x < y, y <= z, z >= y, y > z];
(%o2)    [123 < 456, 456 <= 789, 789 >= 456, 456 > 789]
(%i3) map (is, %);
(%o3)               [true, true, true, false]
```

See also: `is`, `maybe`, `if`, `while`, `unless`, `prederror`, `=`, `#`, `equal`, `notequal`.

<!-- category: Programming -->
<!-- keywords: ^^ -->
<!-- signatures: ^^ -->
### Function: ^^

非可換べき乗演算子。
ちょうど可換なかけ算 `*`に通常のべき乗演算子 `^`が対応するように、
`^^`は非可換かけ算 `.`に対応するべき乗演算子です。


非可換べき乗演算子は、１次元出力では `^^`で表示され、
２次元出力では、指数をかっこ `< >`で囲まれた上付き添字として置きます。


例:







```maxima
(%i1) a . a . b . b . b + a * a * a * b * b;
                        3  2    <2>    <3>
(%o1)                  a  b  + a    . b
(%i2) string (a . a . b . b . b + a * a * a * b * b);
(%o2)                  a^3*b^2+a^^2 . b^^3
```

<!-- category: Programming -->
<!-- keywords: and -->
<!-- signatures: and -->
### Function: and

論理積演算子。
`and`は、n項中置演算子です;
オペランドはブーリアン値で、結果もブーリアン値です。


`and`は、（`is`のように）１以上のオペランドの評価を強制し、
すべてのオペランドの評価を強制するかもしれません。


オペランドは、出現順に評価されます。
`and`は、結果を決定するのに必要なだけオペランドを評価します。
もし任意のオペランドが`false`なら、結果は`false`であり、
ほかのオペランドは評価されません。


グローバルフラグ`prederror`は、
評価されたオペランドが`true`か`false`に決定できない時の`and`の振る舞いを決定します。
`prederror`が`true`の時、`and`は、エラーメッセージを出力します。
そうでなければ、`true`か`false`に評価されないオペランドを受け付け、
結果はブーリアン式になります。


`and`は可換ではありません:
`a and b`は、不定のオペランドの扱いのため、`b and a`と同値ではないかもしれません。

<!-- category: Programming -->
<!-- keywords: infix -->
<!-- signatures: infix(op), infix(op, lbp, rbp), infix(op, lbp, rbp, lpos, rpos, pos) -->
### Function: infix (op)

*op*を中置演算子に宣言します。
中置演算子は２つの引数の関数で、引数の間に関数名が来ます。
例えば、引き算演算子`-`は中置演算子です。


`infix (op)`は、デフォルトの結合力（左右両方とも180）と品詞
（左右両方とも`any`)に等しい）で*op*を中置演算子に宣言します。



`infix (op, lbp, rbp)`は、
記述された左右の結合力
とデフォルトの品詞（左右両方とも`any`)に等しい）で、
*op*を中置演算子に宣言します。


`infix (op, lbp, rbp, lpos, rpos, pos)`は、
記述された左右の結合力と、
左オペランド、右オペランド、演算子結果それぞれについて、
品詞を*lpos*, *rpos*, *pos*に設定して、
*op*を中置演算子に宣言します。


（演算子宣言に関係して）「品詞」は、式のタイプを意味します。
３つのタイプが認識されます; `expr`, `clause`, `any`。それぞれは、
代数式、ブーリアン式、任意の種類の式を示します。
Maximaは、宣言された品詞を実際の式に比較することで、
いくつかの構文法エラーを検出します。


他の演算子に関する*op*の優先順位は、問題となっている演算子の左右結合力から演繹されます。
もし*op*の左右結合力のどちらもある他の演算子の左右結合力より大きいなら、
*op*は、他の演算子より高い優先順位をとります。
もし結合力がどちらも大きくも、どちらも小さくもなければ、
あるもっと複雑な関係が成り立ちます。


*op*の結合性は結合力に依存します。
より大きな左結合力(*lbp*)は、*op*のインスタンスが
式の中で左にある他の演算子の前に評価されることを示し、
より大きな右結合力(*rbp*)は、*op*のインスタンスが
式の中で右にある他の演算子の前に評価されることを示します。
このように、より大きな*lbp*は*op*を右結合にし、
より大きな*rbp*は*op*を左結合にします。
もし*lbp*が*rbp*と等しいなら、
*op*は左結合です。


`Syntax`も参照してください。


例:


もし*op*左右結合力それぞれが、他の演算子のそれより大きいなら、
*op*は他の演算子より高い優先順位をとります。












```maxima
(%i1) :lisp (get '$+ 'lbp)
100
(%i1) :lisp (get '$+ 'rbp)
100
(%i1) infix ("##", 101, 101);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")");
(%o2)       (a ## b) := sconcat("(", a, ",", b, ")")
(%i3) 1 + a ## b + 2;
(%o3)                       (a,b) + 3
(%i4) infix ("##", 99, 99);
(%o4)                          ##
(%i5) 1 + a ## b + 2;
(%o5)                       (a+1,b+2)
```


より大きな*lbp*は*op*を右結合にし、
より大きな*rbp*は*op*を左結合にします。










```maxima
(%i1) infix ("##", 100, 99);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")")$
(%i3) foo ## bar ## baz;
(%o3)                    (foo,(bar,baz))
(%i4) infix ("##", 100, 101);
(%o4)                          ##
(%i5) foo ## bar ## baz;
(%o5)                    ((foo,bar),baz)
```


Maximaは、宣言された品詞を実際の式と比較することで、
いくつかの構文法エラーを検出します。









```maxima
(%i1) infix ("##", 100, 99, expr, expr, expr);
(%o1)                          ##
(%i2) if x ## y then 1 else 0;
Incorrect syntax: Found algebraic expression where logical
expression expected
if x ## y then 
             ^
(%i2) infix ("##", 100, 99, expr, expr, clause);
(%o2)                          ##
(%i3) if x ## y then 1 else 0;
(%o3)                if x ## y then 1 else 0
```

<!-- category: Programming -->
<!-- keywords: matchfix -->
<!-- signatures: matchfix(ldelimiter, rdelimiter), matchfix(ldelimiter, rdelimiter, arg_pos, pos) -->
### Function: matchfix (ldelimiter, rdelimiter)

左と右の区切り記号*ldelimiter*と*rdelimiter*を持つ
matchfix演算子を宣言します
区切り記号は文字列として指定されます。


"matchfix"演算子は、
任意の数の引数の関数で、引数は左と右の区切り記号をマッチする間で現れます。
パーサがオペランドや他の式や演算子から区切り記号を区別できる限り
区切り記号は任意の文字列を取り得ます。
実際には、これは、`%`, `,`, `$`, `;`のような
パースできない区切り記号を除外し、空白を持つ区切り記号を分離することを要求するかもしれません。
右区切り記号は、左区切り記号と同じかもしれませんし、違うかもしれません。


左区切り記号は、たった１つの右区切り記号と関連づけられることができます;
２つの異なるmatchfix演算子は同じ左区切り記号を持つことはできません。


存在する演算子は、
他のプロパティを変えることなく、
matchfix演算子として再宣言することができます。
特に、足し算`+`のような組み込み演算子が
matchfixに宣言されることが可能ですが、
演算子関数は組み込み演算子に関して定義できません。


コマンド`matchfix (ldelimiter, rdelimiter, arg_pos, pos)` は、
引数品詞*arg_pos*と結果品詞*pos*、区切り記号
*ldelimiter*と*rdelimiter*を宣言します。


演算子宣言に関して、「品詞」は式のタイプを意味します。
３つのタイプが認識されます: 
それぞれ、代数式、ブーリアン式、任意の種類の式を示す、
`expr`, `clause`, `any`。
Maximaは、
宣言された品詞を実際の式と比較することで、
いくつかの構文法エラーを検知します。









matchfix演算を実行する関数は通常のユーザー定義関数です。
演算子関数は、
関数定義演算子`:=`や`define`を使って
普通の方法で定義されます。
引数は、区切り記号の間に書かれるか、
クォートされた文字列としての左区切り記号と括弧の中で続く引数を使って書かれます。
`dispfun (ldelimiter)`は関数定義を表示します。


唯一の組み込みmatchfix演算子はリスト構成子`[ ]`です。
括弧`( )`とダブルクォート`" "`はmatchfix演算子のように振る舞いますが、
Maximaパーサによってそのようには扱われません。


`matchfix`は引数を評価します。
`matchfix`は最初の引数*ldelimiter*を返します。



例:


区切り記号はほとんど任意の文字列を取り得ます。












```maxima
(%i1) matchfix ("@@", "~");
(%o1)                          @@
(%i2) @@ a, b, c ~;
(%o2)                      @@a, b, c~
(%i3) matchfix (">>", "<<");
(%o3)                          >>
(%i4) >> a, b, c <<;
(%o4)                      >>a, b, c<<
(%i5) matchfix ("foo", "oof");
(%o5)                          foo
(%i6) foo a, b, c oof;
(%o6)                     fooa, b, coof
(%i7) >> w + foo x, y oof + z << / @@ p, q ~;
                     >>z + foox, yoof + w<<
(%o7)                ----------------------
                            @@p, q~
```


Matchfix演算子は通常のユーザー定義関数です。



```maxima
(%i1) matchfix ("!-", "-!");
(%o1)                         "!-"
(%i2) !- x, y -! := x/y - y/x;
                                    x   y
(%o2)                   !-x, y-! := - - -
                                    y   x
(%i3) define (!-x, y-!, x/y - y/x);
                                    x   y
(%o3)                   !-x, y-! := - - -
                                    y   x
(%i4) define ("!-" (x, y), x/y - y/x);
                                    x   y
(%o4)                   !-x, y-! := - - -
                                    y   x
(%i5) dispfun ("!-");
                                    x   y
(%t5)                   !-x, y-! := - - -
                                    y   x

(%o5)                         done
(%i6) !-3, 5-!;
                                16
(%o6)                         - --
                                15
(%i7) "!-" (3, 5);
                                16
(%o7)                         - --
                                15
```

<!-- category: Programming -->
<!-- keywords: nary -->
<!-- signatures: nary(op), nary(op, bp, arg_pos, pos) -->
### Function: nary (op)

`nary`演算子は
任意の数の引数の関数を示すのに使われます。
引数それぞれは、例えば、A+BやA+B+Cように演算子の出現で分離されます。
`nary("x")`関数は
`x`を `nary`演算子に宣言する構文拡張関数です。
関数は `nary`であると宣言されるかもしれません。
もし `declare(j,nary);`が実行されたら、
これは整理器に
例えば、`j(j(a,b),j(c,d))`を `j(a, b, c, d)`に整理するよう指示します。


`Introduction-to-operators`も参照してください。

See also: `Introduction-to-operators`.

<!-- category: Programming -->
<!-- keywords: nofix -->
<!-- signatures: nofix(op), nofix(op, pos) -->
### Function: nofix (op)

`nofix`演算子は引数のない関数を示すのに使われます。
コマンドにそんな演算子が存在すると、
対応する関数が評価されるだけです。
例えば、Maximaブレイクから抜けるために"exit;"とタイプする時、
"exit"は`nofix`演算子と似たように振る舞います。
関数 `nofix("x")`は
`x`を `nofix`演算子に宣言する構文拡張関数です。


`Introduction-to-operators`も参照してください。

See also: `Introduction-to-operators`.

<!-- category: Programming -->
<!-- keywords: not -->
<!-- signatures: not -->
### Function: not

論理否定演算子。
`not`は、接頭演算子です;
オペランドはブーリアン値で、結果もブーリアン値です。


`or`は、（`is`のように）オペランドの評価を強制します。


グローバルフラグ`prederror`は、
評価されたオペランドが`true`か`false`に決定できない時の`not`の振る舞いを決定します。
`prederror`が`true`の時、`not`は、エラーメッセージを出力します。
そうでなければ、`true`か`false`に評価されないオペランドを受け付け、
結果はブーリアン式になります。

<!-- category: Programming -->
<!-- keywords: or -->
<!-- signatures: or -->
### Function: or

論理和演算子。
`or`は、n項中置演算子です;
オペランドはブーリアン値で、結果もブーリアン値です。


`or`は、（`is`のように）１以上のオペランドの評価を強制し、
すべてのオペランドの評価を強制するかもしれません。


オペランドは、出現順に評価されます。
`and`は、結果を決定するのに必要なだけオペランドを評価します。
もし任意のオペランドが`true`なら、結果は`true`であり、
ほかのオペランドは評価されません。


グローバルフラグ`prederror`は、
評価されたオペランドが`true`か`false`に決定できない時の`or`の振る舞いを決定します。
`prederror`が`true`の時、`or`は、エラーメッセージを出力します。
そうでなければ、`true`か`false`に評価されないオペランドを受け付け、
結果はブーリアン式になります。


`or`は可換ではありません:
`a or b`は、不定のオペランドの扱いのため、`b or a`と同値ではないかもしれません。

<!-- category: Programming -->
<!-- keywords: postfix -->
<!-- signatures: postfix(op), postfix(op, lbp, lpos, pos) -->
### Function: postfix (op)

`prefix`変種のような`postfix`演算子は引数一つの関数を示しますが、
この場合、例えば3!のように、入力文字列の中で引数が演算子に先行します。
`postfix("x")`関数は `x`を`postfix`演算子に宣言する構文拡張関数です。


`Introduction-to-operators`も参照してください。

See also: `Introduction-to-operators`.

<!-- category: Programming -->
<!-- keywords: prefix -->
<!-- signatures: prefix(op), prefix(op, rbp, rpos, pos) -->
### Function: prefix (op)

`prefix`演算子は引数一つの関数であり、
その引数は演算子のすぐ後ろに置かれます。
`prefix("x")`は `x`を`prefix`演算子に宣言する構文拡張関数です。


`Introduction-to-operators`も参照してください。

See also: `Introduction-to-operators`.

