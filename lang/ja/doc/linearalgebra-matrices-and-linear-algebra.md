## Matrices and Linear Algebra

<!-- category: LinearAlgebra -->
<!-- keywords: addcol -->
<!-- signatures: addcol(M, list_1, ..., list_n) -->
### Function: addcol (M, list_1, ..., list_n)

１つまたは複数のリスト(または行列)が与える列を
行列*M*に追加します。

<!-- category: LinearAlgebra -->
<!-- keywords: addrow -->
<!-- signatures: addrow(M, list_1, ..., list_n) -->
### Function: addrow (M, list_1, ..., list_n)

１つまたは複数のリスト(または行列)が与える行を
行列*M*に追加します。

<!-- category: LinearAlgebra -->
<!-- keywords: adjoint -->
<!-- signatures: adjoint(M) -->
### Function: adjoint (M)

行列*M*の余因子行列を返します。
余因子行列は、*M*の余因子の行列の転置です。

<!-- category: LinearAlgebra -->
<!-- keywords: augcoefmatrix -->
<!-- signatures: augcoefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: augcoefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

線形方程式系*eqn_1*, ..., *eqn_m*の
変数*x_1*, ..., *x_n*に関する拡大係数行列を返します。
これは、
それぞれの方程式の定数項(*x_1*, ..., *x_n*に依存しないそれらの項)
に関して隣接した列を持つ係数行列です。



```maxima
(%i1) m: [2*x - (a - 1)*y = 5*b, c + b*y + a*x = 0]$
(%i2) augcoefmatrix (m, [x, y]);
                       [ 2  1 - a  - 5 b ]
(%o2)                  [                 ]
                       [ a    b      c   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: cauchy_matrix -->
<!-- signatures: cauchy_matrix([x_1, x_2, ..., x_m], [y_1, y_2, ..., y_n]), cauchy_matrix([x_1, x_2, ..., x_n]) -->
### Function: cauchy_matrix ([x_1, x_2, ..., x_m], [y_1, y_2, ..., y_n])

要素*a[i,j]* = 1/(*x_i*+*y_i*)を持つ、
`n`掛ける*m*のCauchy行列を返します。
`cauchy_matrix`の第二引数はオプションです。
この場合、Cauchy行列の要素は*a[i,j]* = 1/(*x_i*+*x_j*)です。


注意: 文献によると、Cauchy行列は2つの形式で定義されたものが見られます。
2つ目の定義は*a[i,j]* = 1/(*x_i*-*y_i*)です。


例:







```maxima
(%i1) cauchy_matrix([x1,x2],[y1,y2]);

                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x1  y2 + x1 ]
(%o1)                 [                  ]
                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x2  y2 + x2 ]


(%i2) cauchy_matrix([x1,x2]);
                      [   1         1    ]
                      [  ----    ------- ]
                      [  2 x1    x2 + x1 ]
(%o2)                 [                  ]
                      [    1       1     ]
                      [ -------   ----   ]
                      [ x2 + x1   2 x2   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: charpoly -->
<!-- signatures: charpoly(M, x) -->
### Function: charpoly (M, x)

行列*M*の変数*x*に関する特性多項式を返します。
すなわち、
`determinant (M - diagmatrix (length (M), x))`です。



```maxima
(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]
(%i2) expand (charpoly (a, lambda));
                           2
(%o2)                lambda  - 7 lambda + 10
(%i3) (programmode: true, solve (%));
(%o3)               [lambda = 5, lambda = 2]
(%i4) matrix ([x1], [x2]);
                             [ x1 ]
(%o4)                        [    ]
                             [ x2 ]
(%i5) ev (a . % - lambda*%, %th(2)[1]);
                          [ x2 - 2 x1 ]
(%o5)                     [           ]
                          [ 2 x1 - x2 ]
(%i6) %[1, 1] = 0;
(%o6)                     x2 - 2 x1 = 0
(%i7) x2^2 + x1^2 = 1;
                            2     2
(%o7)                     x2  + x1  = 1
(%i8) solve ([%th(2), %], [x1, x2]);

                  1               2
(%o8) [[x1 = - -------, x2 = - -------], 
               sqrt(5)         sqrt(5)

                                             1             2
                                    [x1 = -------, x2 = -------]]
                                          sqrt(5)       sqrt(5)
```

<!-- category: LinearAlgebra -->
<!-- keywords: coefmatrix -->
<!-- signatures: coefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: coefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

線形方程式系*eqn_1*, ..., *eqn_m*の
変数*x_1*, ..., *x_n*に関する係数行列を返します。



```maxima
(%i1) coefmatrix([2*x-(a-1)*y+5*b = 0, b*y+a*x = 3], [x,y]);
                                 [ 2  1 - a ]
(%o1)                            [          ]
                                 [ a    b   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: col -->
<!-- signatures: col(M, i) -->
### Function: col (M, i)

行列*M*の*i*番目の列を返します。
戻り値は行列です。

<!-- category: LinearAlgebra -->
<!-- keywords: columnvector, covect -->
<!-- signatures: columnvector(L), covect(L) -->
### Function: columnvector (L)

リスト*L*の要素を含む１列`length (L)`行の行列を返します。


`covect`は、`columnvector`と同義です。


`load ("eigen")`はこの関数をロードします。



もしこのパッケージの関数の出力の一部を行列計算で使いたいなら、これは役に立ちます。


例:





```maxima
(%i1) load ("eigen")$
Warning - you are redefining the Macsyma function eigenvalues
Warning - you are redefining the Macsyma function eigenvectors
(%i2) columnvector ([aa, bb, cc, dd]);
                             [ aa ]
                             [    ]
                             [ bb ]
(%o2)                        [    ]
                             [ cc ]
                             [    ]
                             [ dd ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: copymatrix -->
<!-- signatures: copymatrix(M) -->
### Function: copymatrix (M)

行列*M*のコピーを返します。
これは、*M*を要素毎にコピーすることは別にして、コピーを作る唯一の方法です。


`m2: m1`のように、１つの行列のもう１つへの割り当ては`m1`をコピーしない
ことに注意してください。
An assignment 
割り当て`m2 [i,j]: x`または`setelmx (x, i, j, m2`は、
`m1 [i,j]`も変更します。
Creating a copy with 
`copymatrix`を使ってコピーを生成し、割り当てを使うことは、
別個の変更されたコピーを生成します。

<!-- category: LinearAlgebra -->
<!-- keywords: determinant -->
<!-- signatures: determinant(M) -->
### Function: determinant (M)

*M*の行列式をガウスの消去法と似た方法で計算します。



結果の形式は、スイッチ`ratmx`の設定に依ります。



スイッチ`ratmx`と`sparse`がともに`true`の時コールされる
粗な行列式を計算するための特殊なルーチンがあります。

See also: `ratmx`, `sparse`.

<!-- category: LinearAlgebra -->
<!-- keywords: detout -->
<!-- signatures: detout -->
### Variable: detout

デフォルト値: `false`


`detout`が`true`の時、
逆行列が計算された行列の行列式は、逆行列から因子として外に出されます。


このスイッチが効果を持つには、
`doallmxops`と`doscmxops`は、`false`でなければいけません。
(それらの記述を参照してください。)
`ev`は他の２つを正しく設定するので、
代わりに、このスイッチを`ev`に与えるという方法もあります。


例:



```maxima
(%i1) m: matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) detout: true$
(%i3) doallmxops: false$
(%i4) doscmxops: false$
(%i5) invert (m);
                          [  d   - b ]
                          [          ]
                          [ - c   a  ]
(%o5)                     ------------
                           a d - b c
```

See also: `doallmxops`, `doscmxops`, `ev`.

<!-- category: LinearAlgebra -->
<!-- keywords: diagmatrix -->
<!-- signatures: diagmatrix(n, x) -->
### Function: diagmatrix (n, x)

対角要素すべてが*x*に等しい、
サイズが*n*掛ける*n*の対角線行列を返します。
`diagmatrix (n, 1)`は、
(`ident (n)`と同じように)単位行列を返します。


*n*は、整数に評価されなければいけなく、そうでなければ、
`diagmatrix`はエラーメッセージを出力します。


*x*は、別の行列を含む、任意の種類の式を取り得ます
もし*x*が行列なら、それはコピーされません;
対角要素すべては、同じインスタンス*x*を参照します。

<!-- category: LinearAlgebra -->
<!-- keywords: doallmxops -->
<!-- signatures: doallmxops -->
### Variable: doallmxops

デフォルト値: `true`


`doallmxops`が`true`の時、

行列に関係する演算すべてが実行されます。
`false`の時、
 then the setting of the
個々の`dot`スイッチの設定が、どの演算を実行するか決めます。

<!-- category: LinearAlgebra -->
<!-- keywords: domxexpt -->
<!-- signatures: domxexpt -->
### Variable: domxexpt

デフォルト値: `true`


`domxexpt`が`true`の時、
行列の指数関数, `exp (M)` ただし*M*は行列,
は、要素`[i,j`が`exp (m[i,j])`に等しい行列として解釈されます。


そうでなければ、`exp (M)`は、`exp (ev(M)`に評価されます。


`domxexpt`は、
形式`base^power`の式すべてに影響します。
ここで、*base*はスカラーまたは定数と仮定された式、
*power*は、リストまたは行列です。


例:



```maxima
(%i1) m: matrix ([1, %i], [a+b, %pi]);
                         [   1    %i  ]
(%o1)                    [            ]
                         [ b + a  %pi ]
(%i2) domxexpt: false$
(%i3) (1 - c)^m;
                             [   1    %i  ]
                             [            ]
                             [ b + a  %pi ]
(%o3)                 (1 - c)
(%i4) domxexpt: true$
(%i5) (1 - c)^m;
                  [                      %i  ]
                  [    1 - c      (1 - c)    ]
(%o5)             [                          ]
                  [        b + a         %pi ]
                  [ (1 - c)       (1 - c)    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: domxmxops -->
<!-- signatures: domxmxops -->
### Variable: domxmxops

デフォルト値: `true`


`domxmxops`が`true`の時、
行列-行列演算、行列-リスト演算すべてが実行されます
(しかし、スカラー-行列演算は実行されません);
もしこのスイッチが`false`なら、
演算は実行されません。

<!-- category: LinearAlgebra -->
<!-- keywords: domxnctimes -->
<!-- signatures: domxnctimes -->
### Variable: domxnctimes

デフォルト値: `false`


`domxnctimes`が`true`の時、
行列の非可換積が実行されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dontfactor -->
<!-- signatures: dontfactor -->
### Variable: dontfactor

デフォルト値: `[]`


ある変数に関する因数分解が起こらないよう、
`dontfactor`をその変数のリストに設定することができます。
(リストは初期には空です。)
標準有理式(CRE)形で仮定される変数順序に従って、
`dontfactor`リスト上のそれらよりも重要でない変数に関しても
因数分解は、
行われなくなります。

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxops -->
<!-- signatures: doscmxops -->
### Variable: doscmxops

デフォルト値: `false`


`doscmxops`が`true`の時、
スカラー-行列演算が実行されます。

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxplus -->
<!-- signatures: doscmxplus -->
### Variable: doscmxplus

デフォルト値: `false`


`doscmxplus`が`true`の時、
スカラー-行列演算は、行列の結果をもたらします。
このスイッチは、`doallmxops`の下に包括されません。

See also: `doallmxops`.

<!-- category: LinearAlgebra -->
<!-- keywords: dot0nscsimp -->
<!-- signatures: dot0nscsimp -->
### Variable: dot0nscsimp

デフォルト値: `true`



`dot0nscsimp`が`true`の時、
ゼロと非スカラー項の非可換積は、可換積に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dot0simp -->
<!-- signatures: dot0simp -->
### Variable: dot0simp

デフォルト値: `true`



`dot0simp`が`true`の時、
ゼロとスカラー項の非可換積は、
可換積に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dot1simp -->
<!-- signatures: dot1simp -->
### Variable: dot1simp

デフォルト値: `true`



`dot1simp`が`true`の時、
１ともう１つの項の非可換積は、可換積に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dotassoc -->
<!-- signatures: dotassoc -->
### Variable: dotassoc

デフォルト値: `true`


`dotassoc`が`true`の時、
式`(A.B).C`は`A.(B.C)`に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dotconstrules -->
<!-- signatures: dotconstrules -->
### Variable: dotconstrules

デフォルト値: `true`


`dotconstrules`が`true`の時、
定数ともう１つの項の非可換積は、可換積に整理されます。


このフラグをオンにすることは、事実上、
`dot1simp`はもちろん、`dot0simp`, `dot0nscsimp`もオンにします。

See also: `dot1simp`, `dot0simp`, `dot0nscsimp`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotdistrib -->
<!-- signatures: dotdistrib -->
### Variable: dotdistrib

デフォルト値: `false`


`dotdistrib`が`true`の時、
式`A.(B + C)`は`A.B + A.C`に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dotexptsimp -->
<!-- signatures: dotexptsimp -->
### Variable: dotexptsimp

デフォルト値: `true`


`dotexptsimp`が`true`の時、
式`A.A`は`A^^2`に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: dotident -->
<!-- signatures: dotident -->
### Variable: dotident

デフォルト値: 1


`dotident`は`X^^0`が返す値です。

<!-- category: LinearAlgebra -->
<!-- keywords: dotscrules -->
<!-- signatures: dotscrules -->
### Variable: dotscrules

デフォルト値: `false`


`dotscrules`が`true`の時、
式`A.SC`または`SC.A`は、`SC*A`に整理され、
`A.(SC*B)`は`SC*(A.B)`に整理されます。

<!-- category: LinearAlgebra -->
<!-- keywords: echelon -->
<!-- signatures: echelon(M) -->
### Function: echelon (M)

ガウスの消去法で生成される、行列*M*の階段形を返します。
階段形は、*M*から初等行演算によって計算され、
それぞれの行の最初の非ゼロ要素が１で、
その要素の下の列要素がすべてゼロであるような行列です。


`triangularize`もガウスの消去法を実行しますが、
それぞれの行の先頭の非ゼロ要素を規格化しません。


`lu_factor`と`cholesky`は、他の、三角行列をもたらす関数です。







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) echelon (M);
                  [ 1  - 8  - 5      - 2     ]
                  [                          ]
                  [         28       11      ]
                  [ 0   1   --       --      ]
(%o2)             [         37       37      ]
                  [                          ]
                  [              37 bb - 119 ]
                  [ 0   0    1   ----------- ]
                  [              37 aa - 313 ]
```

See also: `triangularize`, `lu_factor`, `cholesky`.

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvalues, eivals -->
<!-- signatures: eigenvalues(M), eivals(M) -->
### Function: eigenvalues (M)

行列*M*の固有値を含む２つのリストのリストを返します。
戻り値の最初の部分リストは、行列の固有値のリストで、
二番目の部分リストは、対応する順序で固有値の重複度のリストです。


`eivals`は、`eigenvalues`と同義です。


`eigenvalues`は、
行列の特性多項式の根を見つけるために、
関数`solve`をコールします。
時々、
`solve`は、多項式の根を見つけられないかもしれません;
その場合、このパッケージの
(`innerproduct`, `unitvector`, `columnvector`,
`gramschmidt`を除いた)いくつかの他の関数はうまく動かないでしょう。





いくつかの場合、`solve`が見つける固有値は、
複雑な式かもしれません。
(これは、
`solve`が
実数とわかっている固有値について
見てもすぐにはわからない実数式を返す時、起こることがあります。)
他のいくつかの関数を使って固有値を整理することが可能なことがあります。



パッケージ`eigen.mac`は、
`eigenvalues`や`eigenvectors`が参照された時、
自動的にロードされます。
もし`eigen.mac`がまだロードされていないなら、
`load ("eigen")`はそれをロードします。
ロードした後は、パッケージの中の関数と変数すべてが利用可能です。

See also: `solve`, `innerproduct`, `unitvector`, `columnvector`, `gramschmidt`, `eigenvectors`.

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvectors, eivects -->
<!-- signatures: eigenvectors(M), eivects(M) -->
### Function: eigenvectors (M)

行列*M*の固有ベクトルを計算します。
戻り値は、２つの要素のリストです。
最初のものは、*M*の固有値のリストと固有値の重複度のリストです。
二番目のものは、固有ベクトルのリストのリストです。
固有値それぞれに対して固有ベクトルのリストが１つあります。
リストそれぞれの中には、固有ベクトルが１つの時も複数のときもあります。


`eivects`は、`eigenvectors`と同義です。


パッケージ`eigen.mac`は、
`eigenvalues`や`eigenvectors`が参照された時、
自動的にロードされます。
もし`eigen.mac`がまだロードされていないなら、
`load ("eigen")`はそれをロードします。
ロードした後は、パッケージの中の関数と変数すべてが利用可能です。


この関数に影響するフラグは以下の通りです:


`nondiagonalizable`は、
`eigenvectors`が戻った後、行列が対角化不可能か可能かに依って
`true`か`false`に設定されます。


`hermitianmatrix`が`true`の時、
エルミート行列の縮退した固有ベクトルが、グラム-シュミットアルゴリズムを使って直交化されるようにします。


`knowneigvals`が`true`の時、
 causes the 
`eigen`パッケージが、
行列の固有値がユーザーに知られていて、グローバル名`listeigvals`の下記憶されていることを仮定するようにします。
`listeigvals`は、
出力`eigenvalues`に似たリストに設定されなければいけません。


ここで、関数`algsys`が固有ベクトルについて解くために使われます。
もし固有値がごちゃごちゃしているなら、
`algsys`は、時々、解を見つけられないかもしれません。
いくつかの場合、
最初に`eigenvalues`コマンドを使って固有値を見つけ、
それらをもっと簡潔な何かに換算するために他の関数を使うことによって、
固有値を整理することが可能かもしれません。
整理に続いて、
`true`に設定された`knowneigvals`フラグとともに
再び`eigenvectors`をコールすることができます。


`eigenvalues`も参照してください。


例:


固有値１つにただ１つの固有ベクトルを持つ行列。









```maxima
(%i1) M1 : matrix ([11, -1], [1, 7]);
                           [ 11  - 1 ]
(%o1)                      [         ]
                           [ 1    7  ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[9 - sqrt(3), sqrt(3) + 9], [1, 1]], 
                        [[[1, sqrt(3) + 2]], [[1, 2 - sqrt(3)]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                       val  = 9 - sqrt(3)
                          1

                            mult  = 1
                                1

                    vec  = [[1, sqrt(3) + 2]]
                       1

                       val  = sqrt(3) + 9
                          2

                            mult  = 1
                                2

                    vec  = [[1, 2 - sqrt(3)]]
                       2

(%o3)                         done
```


１つの固有値(ここでは2)に２つの固有ベクトルを持つ行列。









```maxima
(%i1) M1 : matrix ([0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], 
                   [0, 0, 0, 2]);
                         [ 0  1  0  0 ]
                         [            ]
                         [ 0  0  0  0 ]
(%o1)                    [            ]
                         [ 0  0  2  0 ]
                         [            ]
                         [ 0  0  0  2 ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[0, 2], [2, 2]], [[[1, 0, 0, 0]],
                                   [[0, 0, 1, 0], [0, 0, 0, 1]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                            val  = 0
                               1

                            mult  = 2
                                1

                      vec  = [[1, 0, 0, 0]]
                         1

                            val  = 2
                               2

                            mult  = 2
                                2

               vec  = [[0, 0, 1, 0], [0, 0, 0, 1]]
                  2

(%o3)                         done
```

See also: `eigenvalues`, `algsys`.

<!-- category: LinearAlgebra -->
<!-- keywords: ematrix -->
<!-- signatures: ematrix(m, n, x, i, j) -->
### Function: ematrix (m, n, x, i, j)

値が*x*の`[i, j]`要素を除いて、すべての要素がゼロの
*m*行*n*列行列を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: entermatrix -->
<!-- signatures: entermatrix(m, n) -->
### Function: entermatrix (m, n)

対話的に要素を読み、*m*行*n*列行列を返します。


もし*n*が*m*と等しいなら、
Maximaは、行列のタイプ(対角、対称、反対称、一般)の入力を促し、
それぞれの要素の入力を促します。
応答それぞれは、セミコロン`;`かドル記号`$`で終了させます。


もし*n*が*m*と等しくなければ、
Maximaは、それぞれの要素の入力を促します。


要素は、任意の式を取り得、また、その式は評価されます。
`entermatrix`は引数を評価します。



```maxima
(%i1) n: 3$
(%i2) m: entermatrix (n, n)$

Is the matrix  1. Diagonal  2. Symmetric  3. Antisymmetric 
4. General
Answer 1, 2, 3 or 4 : 
1$
Row 1 Column 1: 
(a+b)^n$
Row 2 Column 2: 
(a+b)^(n+1)$
Row 3 Column 3: 
(a+b)^(n+2)$

Matrix entered.
(%i3) m;
                [        3                     ]
                [ (b + a)      0         0     ]
                [                              ]
(%o3)           [                  4           ]
                [    0      (b + a)      0     ]
                [                              ]
                [                            5 ]
                [    0         0      (b + a)  ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: genmatrix -->
<!-- signatures: genmatrix(a, i_2, j_2, i_1, j_1), genmatrix(a, i_2, j_2, i_1), genmatrix(a, i_2, j_2) -->
### Function: genmatrix (a, i_2, j_2, i_1, j_1)

*a*から生成される行列を返します。
返される行列は、要素`a[i_1,j_1]`を
左上の要素として取り、
`a[i_2,j_2]`を
右下の要素として取ります。
ここで、*a*は、
(`make_array`ではなく`array`が生成する)宣言配列か、
未宣言配列か、配列関数か、２つの引数を持つラムダ式のいずれかです。
(配列関数は、他の関数のように、`:=`や`define`で生成されますが、
引数は括弧の代わりにカギ括弧でくくられます。)


もし*j_1*が省略されたら、
それは、*i_1*と等しいと仮定されます。
もし*j_1*と*i_1*両方が省略されたら、
両方とも1と等しいと仮定されます。


もし配列の選択された要素`i,j`が未定義なら、
行列は、シンボル要素`a[i,j]`を含みます。


例:













```maxima
(%i1) h [i, j] := 1 / (i + j - 1);
                                    1
(%o1)                  h     := ---------
                        i, j    i + j - 1
(%i2) genmatrix (h, 3, 3);
                           [    1  1 ]
                           [ 1  -  - ]
                           [    2  3 ]
                           [         ]
                           [ 1  1  1 ]
(%o2)                      [ -  -  - ]
                           [ 2  3  4 ]
                           [         ]
                           [ 1  1  1 ]
                           [ -  -  - ]
                           [ 3  4  5 ]
(%i3) array (a, fixnum, 2, 2);
(%o3)                           a
(%i4) a [1, 1] : %e;
(%o4)                          %e
(%i5) a [2, 2] : %pi;
(%o5)                          %pi
(%i6) genmatrix (a, 2, 2);
                           [ %e   0  ]
(%o6)                      [         ]
                           [ 0   %pi ]
(%i7) genmatrix (lambda ([i, j], j - i), 3, 3);
                         [  0    1   2 ]
                         [             ]
(%o7)                    [ - 1   0   1 ]
                         [             ]
                         [ - 2  - 1  0 ]
(%i8) genmatrix (B, 2, 2);
                        [ B      B     ]
                        [  1, 1   1, 2 ]
(%o8)                   [              ]
                        [ B      B     ]
                        [  2, 1   2, 2 ]
```

See also: `make_array`, `:=`, `define`.

<!-- category: LinearAlgebra -->
<!-- keywords: gramschmidt -->
<!-- signatures: gramschmidt(x), gramschmidt(x, F) -->
### Function: gramschmidt (x)

*x*に対してグラム-シュミット直交化アルゴリズムを実行します。
*x*は、行列かリストのリストのいずれかです。
`gramschmidt`は*x*を変更しません。
もし引数にあれば、`gramschmidt`は*F*を内積として使います。
そうでなければ、内積は関数`innerproduct`です。


もし*x*が行列なら、
アルゴリズムは *x*の行に適用されます。
もし*x*がリストのリストなら、
アルゴリズムは部分リストに適用されます。
部分リストは、要素数が同じでなければいけません。
いずれの場合も、
戻り値は、リストのリストです。
この部分リストは互いに直交し、*x*と同じ空間を埋めます。
もし、*x*の全範囲の次元が行や部分リストの数よりちいさいなら、
戻り値の部分リストのいくつかはゼロです。


中間結果を整理するために、アルゴリズムのそれぞれの段階で`factor`がコールされます。
結果として、戻り値は、素因数分解された整数を含みます。


`load("eigen")`はこの関数をロードします。


例:


デフォルトの内積関数を使ったグラム-シュミットアルゴリズム。









```maxima
(%i1) load ("eigen")$
(%i2) x: matrix ([1, 2, 3], [9, 18, 30], [12, 48, 60]);
                         [ 1   2   3  ]
                         [            ]
(%o2)                    [ 9   18  30 ]
                         [            ]
                         [ 12  48  60 ]
(%i3) y: gramschmidt (x);
                       2      2            4     3
                      3      3   3 5      2  3  2  3
(%o3)  [[1, 2, 3], [- ---, - --, ---], [- ----, ----, 0]]
                      2 7    7   2 7       5     5
(%i4) map (innerproduct, [y[1], y[2], y[3]], [y[2], y[3], y[1]]);
(%o4)                       [0, 0, 0]
```


指定した内積関数を使ったグラム-シュミットアルゴリズム。









```maxima
(%i1) load ("eigen")$
(%i2) ip (f, g) := integrate (f * g, u, a, b);
(%o2)          ip(f, g) := integrate(f g, u, a, b)
(%i3) y : gramschmidt([1, sin(u), cos(u)], ip), a= -%pi/2, b=%pi/2;
                               %pi cos(u) - 2
(%o3)              [1, sin(u), --------------]
                                    %pi
(%i4) map (ip, [y[1], y[2], y[3]], [y[2], y[3], y[1]]), 
                                                a= -%pi/2, b=%pi/2;
(%o4)                       [0, 0, 0]
```

<!-- category: LinearAlgebra -->
<!-- keywords: ident -->
<!-- signatures: ident(n) -->
### Function: ident (n)

*n*行*n*列の単位行列を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: innerproduct, inprod -->
<!-- signatures: innerproduct(x, y), inprod(x, y) -->
### Function: innerproduct (x, y)

*x*と*y*の(スカラー積やドット積とも呼ばれる)内積を返します。
*x*と*y*は、等しい長さのリストか、ともに等しい長さの1列行列か1行行列です。
戻り値は、`conjugate (x) . y`です。
ここで、`.`は非可換乗算演算子です。


`load ("eigen")`はこの関数をロードします。


`inprod`は、`innerproduct`と同義です。

<!-- category: LinearAlgebra -->
<!-- keywords: invert -->
<!-- signatures: invert(M) -->
### Function: invert (M)

行列*M*の逆行列を返します。
逆行列は随伴法で計算されます。


これは、ユーザーが
要素が多倍長浮動小数点の行列や
要素が浮動小数点係数多項式の行列の逆行列を、
CRE形に変換することなしに計算することを可能にします。


余因子は、`determinant`関数で計算されるので、
もし`ratmx`が`false`なら、
要素の表現を変えることなしに、逆行列が計算されます。


現在の実装は、高次の行列には非効率的です。


`detout`が`true`の時、
行列式は、逆行列から係数として外に出されます。


逆行列の要素は自動的には展開されません。
もし*M*が多項式の要素を持つなら、
`expand (invert (m)), detout`が、見た目がよりよい出力を生成することができます。
もし全体を行列式で割られたものが望ましいなら、
`xthru (%)`で達成することができます。
また、代わりに最初から以下のようにしても達成できます。



```maxima
expand (adjoint (m)) / expand (determinant (m))
invert (m) := adjoint (m) / determinant (m)
```


行列の逆を計算する別の方法について`^^` (非可換べき乗)を参照してください。

See also: `determinant`, `ratmx`, `detout`.

<!-- category: LinearAlgebra -->
<!-- keywords: list_matrix_entries -->
<!-- signatures: list_matrix_entries(M) -->
### Function: list_matrix_entries (M)

行列*M*の要素を含むリストを返します。


例:






```maxima
(%i1) list_matrix_entries(matrix([a,b],[c,d]));
(%o1)                     [a, b, c, d]
```

<!-- category: LinearAlgebra -->
<!-- keywords: lmxchar -->
<!-- signatures: lmxchar -->
### Variable: lmxchar

デフォルト値: `[`


`lmxchar`は、行列の左区切り記号として表示される文字です。
`rmxchar`も参照してください。


例:



```maxima
(%i1) lmxchar: "|"$
(%i2) matrix ([a, b, c], [d, e, f], [g, h, i]);
                           | a  b  c ]
                           |         ]
(%o2)                      | d  e  f ]
                           |         ]
                           | g  h  i ]
```

See also: `rmxchar`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrix -->
<!-- signatures: matrix(row_1, ..., row_n) -->
### Function: matrix (row_1, ..., row_n)

行*row_1*, ..., *row_n*を持つ長方形行列を返します。
行それぞれは、式のリストです。
すべての行は同じ長さでなければいけません。


オペランドが、２つの行列、スカラーと行列、行列とスカラーのいずれかの時、
演算`+` (足し算), `-` (引き算), `*` (掛け算),
`/` (割り算)は要素毎に実行されます。
もしオペランドが、スカラーと行列、行列とスカラーのいずれかなら、
演算`^` (べき乗, `**`と同値)は、要素毎に実行されますが、
もしオペランドが２つの行列なら要素毎には実行されません。

`.` (非可換乗算)を含むすべての演算は、通常、完全に実行されます。


行列の掛け算は、非可換乗算演算子`.`で表されます。
対応する非可換べき乗演算子は`^^`です。
行列 `A`に関して、
`A.A = A^^2`であり、
もし存在するなら、`A^^-1`は*A*の逆行列です。


ドット演算や行列-リスト演算を含む式の整理を制御するためのスイッチがあります。
それらは、
`doallmxops`, `domxexpt`
`domxmxops`, `doscmxops`, `doscmxplus`です。



行列に関係する付加的なオプションがあります。
それらは以下の通りです:
`lmxchar`, `rmxchar`, `ratmx`, `listarith`, `detout`,
`scalarmatrix`,
 `sparse`



行列を引数として取ったり、行列を戻り値としてもたらしたりするたくさんの関数があります。
`eigenvalues`, `eigenvectors`,
`determinant`,
`charpoly`, `genmatrix`, `addcol`, `addrow`, 
`copymatrix`, `transpose`, `echelon`,
`rank`を参照してください。



例:



- *
リストからの行列の組み立て。


```maxima
(%i1) x: matrix ([17, 3], [-8, 11]);
                           [ 17   3  ]
(%o1)                      [         ]
                           [ - 8  11 ]
(%i2) y: matrix ([%pi, %e], [a, b]);
                           [ %pi  %e ]
(%o2)                      [         ]
                           [  a   b  ]
```


- *
足し算、要素毎に。


```maxima
(%i3) x + y;
                      [ %pi + 17  %e + 3 ]
(%o3)                 [                  ]
                      [  a - 8    b + 11 ]
```


- *
引き算、要素毎に。


```maxima
(%i4) x - y;
                      [ 17 - %pi  3 - %e ]
(%o4)                 [                  ]
                      [ - a - 8   11 - b ]
```


- *
掛け算。要素毎に。


```maxima
(%i5) x * y;
                        [ 17 %pi  3 %e ]
(%o5)                   [              ]
                        [ - 8 a   11 b ]
```


- *
割り算。要素毎に。


```maxima
(%i6) x / y;
                        [ 17       - 1 ]
                        [ ---  3 %e    ]
                        [ %pi          ]
(%o6)                   [              ]
                        [   8    11    ]
                        [ - -    --    ]
                        [   a    b     ]
```


- *
行列のスカラーべき、要素毎に。


```maxima
(%i7) x ^ 3;
                         [ 4913    27  ]
(%o7)                    [             ]
                         [ - 512  1331 ]
```


- *
スカラー基数の行列べき、要素毎に。


```maxima
(%i8) exp(y); 
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o8)                    [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
行列基数の行列べき。これは要素毎には実行されません。


```maxima
(%i9) x ^ y;
                                [ %pi  %e ]
                                [         ]
                                [  a   b  ]
                     [ 17   3  ]
(%o9)                [         ]
                     [ - 8  11 ]
```


- *
非可換行列乗算。


```maxima
(%i10) x . y;
                  [ 3 a + 17 %pi  3 b + 17 %e ]
(%o10)            [                           ]
                  [ 11 a - 8 %pi  11 b - 8 %e ]
(%i11) y . x;
                [ 17 %pi - 8 %e  3 %pi + 11 %e ]
(%o11)          [                              ]
                [  17 a - 8 b     11 b + 3 a   ]
```


- *
非可換行列べき乗
スカラー基数*b*の行列べき*M*は、要素毎に実行され、
`b^^m`は`b^m`と同じです。


```maxima
(%i12) x ^^ 3;
                        [  3833   1719 ]
(%o12)                  [              ]
                        [ - 4584  395  ]
(%i13) %e ^^ y;

                         [   %pi    %e ]
                         [ %e     %e   ]
(%o13)                   [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
行列の-1指数の非可換べき乗は存在するなら、逆行列のことです。


```maxima
(%i14) x ^^ -1;
                         [ 11      3  ]
                         [ ---  - --- ]
                         [ 211    211 ]
(%o14)                   [            ]
                         [  8    17   ]
                         [ ---   ---  ]
                         [ 211   211  ]
(%i15) x . (x ^^ -1);
                            [ 1  0 ]
(%o15)                      [      ]
                            [ 0  1 ]
```

See also: `doallmxops`, `domxexpt`, `domxmxops`, `doscmxops`, `doscmxplus`, `lmxchar`, `rmxchar`, `ratmx`, `listarith`, `detout`, `sparse`, `eigenvalues`, `eigenvectors`, `determinant`, `charpoly`, `genmatrix`, `addcol`, `addrow`, `copymatrix`, `transpose`, `echelon`, `rank`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_add -->
<!-- signatures: matrix_element_add -->
### Variable: matrix_element_add

デフォルト値: `+`


`matrix_element_add`は、
行列乗算の中で足し算の代わりに呼び出される演算です。
`matrix_element_add`は、
任意のn項演算子(すなわち、任意の数の引数を扱う関数)に割り当てられます。
割り当てられた値は、クォートマークでくくられた演算子の名前か、
関数名かラムダ式を取り得ます。


`matrix_element_mult`と`matrix_element_transpose`も参照してください。


例:



```maxima
(%i1) matrix_element_add: "*"$
(%i2) matrix_element_mult: "^"$
(%i3) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o3)                      [         ]
                           [ d  e  f ]
(%i4) bb: matrix ([u, v, w], [x, y, z]);

                           [ u  v  w ]
(%o4)                      [         ]
                           [ x  y  z ]

(%i5) aa . transpose (bb);
                     [  u  v  w   x  y  z ]
                     [ a  b  c   a  b  c  ]
(%o5)                [                    ]
                     [  u  v  w   x  y  z ]
                     [ d  e  f   d  e  f  ]
```

See also: `matrix_element_mult`, `matrix_element_transpose`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_mult -->
<!-- signatures: matrix_element_mult -->
### Variable: matrix_element_mult

デフォルト値: `*`


`matrix_element_mult`は、
行列乗算の中で掛け算の代わりに呼び出される演算です。
`matrix_element_mult`は、
任意の二項演算子に割り当てられます。
割り当てられた値は、クォートマークでくくられた演算子の名前か、関数名か、
ラムダ式を取り得ます。


ドット演算子`.`は、いくつかの文脈で役に立つ選択です。


`matrix_element_add`と`matrix_element_transpose`も参照してください。


例:



```maxima
(%i1) matrix_element_add: lambda ([[x]], sqrt (apply ("+", x)))$
(%i2) matrix_element_mult: lambda ([x, y], (x - y)^2)$
(%i3) [a, b, c] . [x, y, z];
                          2          2          2
(%o3)         sqrt((c - z)  + (b - y)  + (a - x) )
(%i4) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o4)                      [         ]
                           [ d  e  f ]
(%i5) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o5)                      [         ]
                           [ x  y  z ]
(%i6) aa . transpose (bb);
               [             2          2          2  ]
               [ sqrt((c - w)  + (b - v)  + (a - u) ) ]
(%o6)  Col 1 = [                                      ]
               [             2          2          2  ]
               [ sqrt((f - w)  + (e - v)  + (d - u) ) ]

                         [             2          2          2  ]
                         [ sqrt((c - z)  + (b - y)  + (a - x) ) ]
                 Col 2 = [                                      ]
                         [             2          2          2  ]
                         [ sqrt((f - z)  + (e - y)  + (d - x) ) ]
```

See also: `matrix_element_add`, `matrix_element_transpose`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_transpose -->
<!-- signatures: matrix_element_transpose -->
### Variable: matrix_element_transpose

デフォルト値: `false`


`matrix_element_transpose`は、
転置される時、行列のそれぞれの要素に適用される演算です。
`matrix_element_mult`は、任意の単項演算子に割り当てられます。
割り当てられた値はクォートマークでくくられた演算子の名前か、
関数名か、ラムダ式を取り得ます。


`matrix_element_transpose`が`transpose`に等しい時、
`transpose`関数が要素すべてに適用されます。
`matrix_element_transpose`が`nonscalars`に等しい時、
`transpose`関数は非スカラー要素すべてに適用されます。
もしある要素がアトムなら、`nonscalars`オプションは
アトムが宣言された非スカラーの時だけ`transpose`を適用します。
一方、`transpose`オプションはいつも`transpose`を適用します。


デフォルト値, `false`,はいかなる演算も適用しないことを意味します。


`matrix_element_add`と`matrix_element_mult`も参照してください。


例:



```maxima
(%i1) declare (a, nonscalar)$
(%i2) transpose ([a, b]);
                        [ transpose(a) ]
(%o2)                   [              ]
                        [      b       ]
(%i3) matrix_element_transpose: nonscalars$
(%i4) transpose ([a, b]);
                        [ transpose(a) ]
(%o4)                   [              ]
                        [      b       ]
(%i5) matrix_element_transpose: transpose$
(%i6) transpose ([a, b]);
                        [ transpose(a) ]
(%o6)                   [              ]
                        [ transpose(b) ]
(%i7) matrix_element_transpose: lambda ([x], realpart(x)
      - %i*imagpart(x))$
(%i8) m: matrix ([1 + 5*%i, 3 - 2*%i], [7*%i, 11]);
                     [ 5 %i + 1  3 - 2 %i ]
(%o8)                [                    ]
                     [   7 %i       11    ]
(%i9) transpose (m);
                      [ 1 - 5 %i  - 7 %i ]
(%o9)                 [                  ]
                      [ 2 %i + 3    11   ]
```

See also: `matrix_element_mult`, `transpose`, `matrix_element_add`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrixmap -->
<!-- signatures: matrixmap(f, M) -->
### Function: matrixmap (f, M)

`f(M[i,j])`に等しい要素`i,j`を持つ行列を返します。


`map`, `fullmap`, `fullmapl`, `apply`も参照してください。

See also: `map`, `fullmap`, `fullmapl`, `apply`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrixp -->
<!-- signatures: matrixp(expr) -->
### Function: matrixp (expr)

もし*expr*が行列なら`true`を返し，そうでなければ、`false`を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: mattrace -->
<!-- signatures: mattrace(M) -->
### Function: mattrace (M)

正方行列*M*の跡(すなわち、主対角上の要素の和)を返します。


`mattrace`は、`ncharpoly`―Maximaの`charpoly`の代わり―
によってコールされます。



`load ("nchrpl")`はこの関数をロードします。

See also: `ncharpoly`, `charpoly`.

<!-- category: LinearAlgebra -->
<!-- keywords: minor -->
<!-- signatures: minor(M, i, j) -->
### Function: minor (M, i, j)

行列*M*の*i*, *j*小行列を返します。
すなわち、行*i*と列*j*を除いた*M*です。

<!-- category: LinearAlgebra -->
<!-- keywords: ncharpoly -->
<!-- signatures: ncharpoly(M, x) -->
### Function: ncharpoly (M, x)

行列*M*の
*x*に関する特性多項式を返します。
これはMaximaの`charpoly`の代わりです。


`ncharpoly`は、与えられた行列のべきの跡を計算することで機能します。
それは、特性多項式の根のべきの和に等しいことが知られています。
それらの量から根の対称関数を計算することができます。
それらは、特性多項式の係数以上のなにものでもありません。
`charpoly`は、

`x * ident [n] - a`の行列式を形成することで機能します。
このように、
`ncharpoly`
は完全に多項式算術を避けるので、
例えば、整数で埋められた大きな密な行列の場合、`ncharpoly`が勝ります。


`load ("nchrpl")`はこのファイルをロードします。

See also: `charpoly`.

<!-- category: LinearAlgebra -->
<!-- keywords: newdet -->
<!-- signatures: newdet(M) -->
### Function: newdet (M)

行列*M*の行列式を
ジョンソン-ジェントルマンのtree minorアルゴリズムを使って計算します。
`newdet`はCRE形式で結果を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalar -->
<!-- signatures: nonscalar -->
### Variable: nonscalar

アトムをドット演算子に関してリストか行列のように振る舞うようにします。

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalarp -->
<!-- signatures: nonscalarp(expr) -->
### Function: nonscalarp (expr)

もし*expr*が非スカラー、すなわち、
非スカラーとして宣言されたアトムかリスト、行列を含むなら、
`true`を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: permanent -->
<!-- signatures: permanent(M, n) -->
### Function: permanent (M, n)

行列*M*のパーマネントを計算します。
パーマネントは行列式のようですが、符号が変わりません。
`permanent`はCRE形式で結果を返します。


`newdet`も参照してください。

<!-- category: LinearAlgebra -->
<!-- keywords: rank -->
<!-- signatures: rank(M) -->
### Function: rank (M)

行列*M*のランクを計算します。
すなわち、*M*の、最も大きな非特異な小行列式の次数です。



もし*rank*がゼロと同値の行列要素が確かにそうであることを決定することができないなら、
、間違った答えを返します。

<!-- category: LinearAlgebra -->
<!-- keywords: ratmx -->
<!-- signatures: ratmx -->
### Variable: ratmx

デフォルト値: `false`


`ratmx`が`false`の時、
行列要素の表現で、行列式と行列の足し算、引き算、掛け算が実行され、
逆行列の結果は一般表現のまま残されます。


`ratmx`が`true`の時、
上で述べた４つの演算は、CRE形式で実行され、
逆行列の結果もCRE形式になります。
これは、(`ratfac`の設定に依って)
いつも望まれているわけではないですが、
要素が展開されるようになるかもしれないことに注意してください。

<!-- category: LinearAlgebra -->
<!-- keywords: rmxchar -->
<!-- signatures: rmxchar -->
### Variable: rmxchar

デフォルト値: `]`


`rmxchar`は、行列の右辺に描かれる文字です。


`lmxchar`も参照してください。

<!-- category: LinearAlgebra -->
<!-- keywords: row -->
<!-- signatures: row(M, i) -->
### Function: row (M, i)

行列*M*の*i*番目の行を返します。
戻り値は行列です。

<!-- category: LinearAlgebra -->
<!-- keywords: scalarmatrixp -->
<!-- signatures: scalarmatrixp -->
### Variable: scalarmatrixp

デフォルト値: `true`


`scalarmatrixp`が`true`の時、
1 x 1行列が行列のドット積を計算した結果として生成される時はいつでも、
スカラー、すなわち、行列の唯一の要素、に整理されます。


`scalarmatrixp`が`all`の時、
すべての1 x 1行列はスカラーに整理されます。


`scalarmatrixp`が`false`の時、
1 x 1行列はスカラーに整理されません。

<!-- category: LinearAlgebra -->
<!-- keywords: scalefactors -->
<!-- signatures: scalefactors(coordinatetransform) -->
### Function: scalefactors (coordinatetransform)

ここで、
coordinatetransformは、形式
[[expression1, expression2, ...],
indeterminate1, indeterminat2, ...]
に評価されます。また、
indeterminate1,
indeterminate2, などは曲線座標変数であり、
直交カーテシアン成分の集合は、
[expression1, expression2, ...]によって、曲線座標を使って与えられます。


`coordinates`が
ベクトル[indeterminate1, indeterminate2,...]に設定され、
`dimension`がこのベクトルの長さに設定されます。
SF[1], SF[2], ..., SF[DIMENSION]は、座標スケールファクタに設定され、
`sfprod`は、これらのスケールファクタの積に設定されます。
初期には、3次元直交カーテシアン座標に対応して、
`coordinates`は[X, Y, Z]であり、
`dimension`は3であり、SF[1]=SF[2]=SF[3]=SFPROD=1です。
式を現在の座標形の物理成分に展開するために、
形式?を利用する関数があります。

<!-- category: LinearAlgebra -->
<!-- keywords: setelmx -->
<!-- signatures: setelmx(x, i, j, M) -->
### Function: setelmx (x, i, j, M)

*x*を行列*M*の(*i*, *j*)番目の要素に割り当て、
変わった行列を返します。


`M [i, j]: x`は同じ効果を持ちますが、
*M*の代わりに*x*を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: similaritytransform, simtran -->
<!-- signatures: similaritytransform(M), simtran(M) -->
### Function: similaritytransform (M)

`similaritytransform`は、
行列`M`の相似変換を計算します。
`uniteigenvectors`コマンドの出力であるリストを返します。
更に、もしフラグ`nondiagonalizable`が`false`なら、
２つのグローバル行列`leftmatrix`と`rightmatrix`が計算されます。
これらの行列は、
`leftmatrix . M . rightmatrix`が
*M*の固有値を対角上に持つ対角行列となるという性質を持ちます。
もし`nondiagonalizable`が`true`なら、
左右の行列は計算されません。


もしフラグ`hermitianmatrix`が`true`なら、
`leftmatrix`は、`rightmatrix`の転置の複素共役です。
そうでなければ、`leftmatrix`は`rightmatrix`の逆行列です。


`rightmatrix`は、列が*M*の単位固有ベクトルである行列です。
他のフラグ(`eigenvalues`と`eigenvectors`を参照してください)は、
`similaritytransform`は、
`rightmatrix`を形成することができるようになるために、パッケージの中の他の関数をコールするので、
同じ効果を持ちます。


`load ("eigen")`はこの関数をロードします。


`simtran`は、`similaritytransform`と同義です。

<!-- category: LinearAlgebra -->
<!-- keywords: sparse -->
<!-- signatures: sparse -->
### Variable: sparse

デフォルト値: `false`


`sparse`が`true`の時、
かつ、もし`ratmx`が`true`なら、
`determinant`は、粗な行列式を計算するために特別なルーチンを使います。

<!-- category: LinearAlgebra -->
<!-- keywords: submatrix -->
<!-- signatures: submatrix(i_1, ..., i_m, M, j_1, ..., j_n), submatrix(i_1, ..., i_m, M), submatrix(M, j_1, ..., j_n) -->
### Function: submatrix (i_1, ..., i_m, M, j_1, ..., j_n)

行*i_1*, ..., *i_m*が取り除かれ、
列*j_1*, ..., *j_n*が取り除かれた
行列*M*から構成された新しい行列を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: transpose -->
<!-- signatures: transpose(M) -->
### Function: transpose (M)

*M*の転置を返します。


もし*M*が行列なら、
戻り値は、`N[i,j] = M[j,i]`であるような別の行列*N*です。


もし*M*がリストなら、
返し値は、`N[i,1] = M[i]`であるような、`length (m)`行1列の行列*N*です。


そうでなければ*M*はシンボルで、
戻り値は、名詞式`'transpose (M)`です。

<!-- category: LinearAlgebra -->
<!-- keywords: triangularize -->
<!-- signatures: triangularize(M) -->
### Function: triangularize (M)

ガウスの消去法で生成されるような、行列`M`の右上三角化行列を返します。
戻り値は、
それぞれの行の先頭の非ゼロ係数が1に規格化されないことを除いて、
`echelon`と同じです。


`lu_factor`と`cholesky`は、三角化行列をもらたす他の関数です。







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) triangularize (M);
             [ - 1   8         5            2      ]
             [                                     ]
(%o2)        [  0   - 74     - 56         - 22     ]
             [                                     ]
             [  0    0    626 - 74 aa  238 - 74 bb ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: uniteigenvectors, ueivects -->
<!-- signatures: uniteigenvectors(M), ueivects(M) -->
### Function: uniteigenvectors (M)

行列*M*の単位固有ベクトルを計算します。
戻り値は、リストのリストです。
最初の部分リストは`eigenvalues`コマンドの出力であり、
他の部分リストは、固有値それぞれに対応する行列の単位固有ベクトルです。



`eigenvectors`コマンドでの記述で言及されたフラグは、
これに関しても同じ効果を持ちます。


`knowneigvects`が`true`の時、
`eigen`パッケージは、
行列の固有ベクトルがユーザーに知られていて、
グローバル名`listeigvects`の下に記憶されていることを仮定します。
`listeigvects`は、
`eigenvectors`コマンドの出力に似たリストに設定されなければいけません。



もし`knowneigvects`が`true`に設定されていて、
固有ベクトルのリストが与えれているなら、
フラグ`nondiagonalizable`の設定は正しくないかもしれません。
もしこの場合に該当するなら、正しい値に設定してください。
作者は、ユーザーがしていることを知っていること、
固有値が適切な次元のベクトル空間を作り出さない行列を対角化しようとはしないことを
仮定しています。


`load ("eigen")`はこの関数をロードします。


`ueivects`は`uniteigenvectors`と同義です。

<!-- category: LinearAlgebra -->
<!-- keywords: unitvector, uvect -->
<!-- signatures: unitvector(x), uvect(x) -->
### Function: unitvector (x)

$x/norm(x)$を返します;
これは、*x*と同じ向きの単位ベクトルです。


`load ("eigen")`はこの関数をロードします。


`uvect`は、`unitvector`と同義です。

<!-- category: LinearAlgebra -->
<!-- keywords: vect_cross -->
<!-- signatures: vect_cross -->
### Variable: vect_cross

デフォルト値: `false`



`vect_cross`が`true`の時、
~がSHARE;VECTの中で定義されているところ
 (とにかく、VECT_CROSSが`true`に設定されているところ)
でDIFF(X~Y,T)が機能するようにします。

<!-- category: LinearAlgebra -->
<!-- keywords: vectorpotential -->
<!-- signatures: vectorpotential(givencurl) -->
### Function: vectorpotential (givencurl)

現在の座標系で与えられた回転ベクトルのベクトルポテンシャルを返します。
`potentialzeroloc`が `potential`に対して似たような役割を持ちますが、
等式の左辺側の次数は座標変数の巡回置換でなければいけません。

<!-- category: LinearAlgebra -->
<!-- keywords: vectorsimp -->
<!-- signatures: vectorsimp(expr) -->
### Function: vectorsimp (expr)

以下のグローバルフラグに従って整理と展開を適用します:



`expandall`, `expanddot`, `expanddotplus`, `expandcross`, `expandcrossplus`,
`expandcrosscross`, `expandgrad`, `expandgradplus`, `expandgradprod`,
`expanddiv`, `expanddivplus`, `expanddivprod`, `expandcurl`, `expandcurlplus`,
`expandcurlcurl`, `expandlaplacian`, `expandlaplacianplus`,
 `expandlaplacianprod`.



これらのフラグすべては、デフォルト値`false`を持ちます。
`plus`接尾辞は、加算性や分配性の利用に関係します。
`prod`接尾辞は、任意の種類の積のオペランドに関する展開に関係します。



**expandcrosscross** — $p ~ (q ~ r)$を$(p . r)*q - (p . q)*r$に整理します。
**expandcurlcurl** — $curl curl p$を$grad div p + div grad p$に整理します。
**expandlaplaciantodivgrad** — $laplacian p$を$div grad p$に整理します。
**expandcross** — `expandcrossplus`と`expandcrosscross`を有効にします。
**expandplus** — `expanddotplus`, `expandcrossplus`, `expandgradplus`,
`expanddivplus`, `expandcurlplus`, `expandlaplacianplus`を有効にします。
**expandprod** — `expandgradprod`, `expanddivprod`, `expandlaplacianprod`を有効にします。



これらのフラグはすべて`evflag`として宣言されています。

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrix -->
<!-- signatures: zeromatrix(m, n) -->
### Function: zeromatrix (m, n)

要素すべてがゼロの*m*行*n*列行列を返します。

