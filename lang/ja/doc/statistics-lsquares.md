## lsquares

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates -->
<!-- signatures: lsquares_estimates(D, x, e, a), lsquares_estimates(D, x, e, a, initial=L, tol=t) -->
### Function: lsquares_estimates (D, x, e, a)

最小二乗の方法で決定されるような
変数*x*と*a*の方程式*e*を
データ*D*に最良フィットする
パラメータ*a*を見積もります。
`lsquares_estimates`は最初に厳密な解を探し、
それが失敗したら、近似的な解を探します。


戻り値は
形式 `[a = ..., b = ..., c = ...]`の等式のリストのリストです。
リストのそれぞれの要素は
二乗平均誤差の、個別の等価な最小です。


データ *D*は行列でなければいけません。
行それぞれは(文脈によって「レコード」とか「ケース」とか呼ばれる)1つのデータで、
列それぞれは
すべてのデータに関するある変数の値を含みます。
変数のリスト *x*は *D*の列それぞれの名前を与えます。
解析をしない列にも名前を与えます。


パラメータのリスト *a*は
見積もられるパラメータの名前を与えます。
方程式 *e*は変数 *x*と *a*に関する式か等式です;
もし *e*が等式でないなら、
`e = 0`と同様に扱われます。


`lsquares_estimates`の付加引数は
等式として指定され、
厳密な結果が見つからなかった時
数値方法で見積もりを見つけるためにコールされる関数 `lbfgs`へそのまま渡されます。


もしある厳密解が(`solve`を介して)見つけることができるなら、
データ *D*は非数値を含むかもしれません。
しかし、もし厳密解が見つからないなら、
*D*の要素それぞれは数値でなければいけません。
これは
数リテラル(整数、有理数、通常の浮動小数点、多倍長浮動小数点)はもちろん、
`%pi`や`%e`のような数値定数を含みます。
数値計算は通常の浮動小数点算出で実行されます。
他の種類の数値は計算のため、すべて通常の浮動小数点に変換されます。


`load("lsquares")`はこの関数をロードします。


`lsquares_estimates_exact`,
`lsquares_estimates_approximate`,

`lsquares_mse`,
`lsquares_residuals`,
`lsquares_residual_mse`も参照してください。


例:


厳密解が見つかる問題。










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
        [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);

                                  [ 1  1  1 ]
                                  [         ]
                                  [ 3       ]
                                  [ -  1  2 ]
                                  [ 2       ]
                                  [         ]
(%o2)                             [ 9       ]
                                  [ -  2  1 ]
                                  [ 4       ]
                                  [         ]
                                  [ 3  2  2 ]
                                  [         ]
                                  [ 2  2  1 ]

(%i3) lsquares_estimates (
         M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                         59        27      10921        107
(%o3)            [[A = - --, B = - --, C = -----, D = - ---]]
                         16        16      1024         32
```


厳密解が見つからない問題。
だから `lsquares_estimates`は数値近似に頼ります。









```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix ([1, 1], [2, 7/4], [3, 11/4], [4, 13/4]);
                                   [ 1  1  ]
                                   [       ]
                                   [    7  ]
                                   [ 2  -  ]
                                   [    4  ]
                                   [       ]
(%o2)                              [    11 ]
                                   [ 3  -- ]
                                   [    4  ]
                                   [       ]
                                   [    13 ]
                                   [ 4  -- ]
                                   [    4  ]
(%i3) lsquares_estimates (
  M, [x,y], y=a*x^b+c, [a,b,c], initial=[3,3,3], iprint=[-1,0]);
(%o3) [[a = 1.387365874920637, b = .7110956639593767, 
                                        c = - .4142705622439105]]
```

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates_approximate -->
<!-- signatures: lsquares_estimates_approximate(MSE, a, initial=L, tol=t) -->
### Function: lsquares_estimates_approximate (MSE, a, initial=L, tol=t)

平均二乗誤差 *MSE*を最小化する
パラメータ *a*を
数値最小化関数 `lbfgs`を介して
見積もります。
平均二乗誤差は、
`lsquares_mse`が返すようなパラメータ *a*の式です。



`lsquares_estimates_approximate`が返す解は
平均二乗誤差の(たぶん大域ですが)局所最小値です。
`lsquares_estimates_exact`との一貫性のため、
戻り値は
要素1つ、すなわち、形式 `[a = ..., b = ..., c = ...]`の等式のリスト
を持つ入れ子のリストです。


`lsquares_estimates_approximate`の付加引数は
等式として指定され、
数値方法で見積もりを見つけるためにコールされる関数 `lbfgs`へそのまま渡されます。


パラメータが数値が割り当てられた時
*MSE*はは数に評価されなければいけません。
これは
This requires that the data from which 
*MSE*が構成されるデータが
`%pi`や`%e`、
数リテラル(整数、有理数、通常の浮動小数点、多倍長浮動小数点)
のような数値定数を含みます。
数値計算は通常の浮動小数点算出で実行されます。
他の種類の数値は計算のため、すべて通常の浮動小数点に変換されます。


`load("lsquares")`はこの関数をロードします。


`lsquares_estimates`,
`lsquares_estimates_exact`,
`lsquares_mse`,
`lsquares_residuals`,
`lsquares_residual_mse`も参照してください。


例:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
(%i4) lsquares_estimates_approximate (
              mse, [A, B, C, D], iprint = [-1, 0]);
(%o4) [[A = - 3.67850494740174, B = - 1.683070351177813, 
                 C = 10.63469950148635, D = - 3.340357993175206]]
```

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates_exact -->
<!-- signatures: lsquares_estimates_exact(MSE, a) -->
### Function: lsquares_estimates_exact (MSE, a)

方程式系を構成し、`solve`を介して記号的にそれらを解くことを試みることで、
平均二乗誤差 *MSE*を最小化する
パラメータ *a*を見積もります。
平均二乗誤差は
 `lsquares_mse`が返すような
パラメータ *a*の式です。


戻り値は
形式 `[a = ..., b = ..., c = ...]`の等式のリストのリストです。
戻り値は、0個か1個、2以上の要素を含むかもしれません。
もし複数の要素が返されたら、
それぞれは個別の、平均二乗誤差の等価最小を表します。


`lsquares_estimates`,
`lsquares_estimates_approximate`,
`lsquares_mse`,

`lsquares_residuals`,
`lsquares_residual_mse`も参照してください。


例:










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
(%i4) lsquares_estimates_exact (mse, [A, B, C, D]);
                  59        27      10921        107
(%o4)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```

<!-- category: Statistics -->
<!-- keywords: lsquares_mse -->
<!-- signatures: lsquares_mse(D, x, e) -->
### Function: lsquares_mse (D, x, e)

平均二乗誤差 (MSE)、
変数 *x*の 方程式*e*に関する
データ *D*の和の式を返します。


MSEは以下のように定義されます:



$$
{1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,
$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


ここで、 *n*はデータ数で、
`e[i]`は、
`i`番目のデータ `D[i]`から値を割り当てられた
*x*の中の変数に対して評価された方程式 *e*です。


`load("lsquares")`はこの関数をロードします。


例:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
```


```maxima
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
```


```maxima
(%i4) diff (mse, D);
         5
        ====
        \                             2
      4  >    (D + M    ) ((D + M    )  - C - M     B - M     A)
        /           i, 1         i, 1          i, 3      i, 2
        ====
        i = 1
(%o4) ----------------------------------------------------------
                                  5
```


```maxima
(%i5) ''mse, nouns;

               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5
```

<!-- category: Statistics -->
<!-- keywords: lsquares_residual_mse -->
<!-- signatures: lsquares_residual_mse(D, x, e, a) -->
### Function: lsquares_residual_mse (D, x, e, a)

指定されたパラメータ *a*とデータ *D*での
方程式 *e*に関する残差平均二乗誤差を返します。


残差MSEは以下のように定義されます:



$$
{1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,
$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


ここで、
`e[i]`は、
*a*から任意の残りの自由変数を割り当てて、
`i`番目のデータ `D[i]`から値を割り当てられた
*x*の中の変数に対して評価された方程式 *e*です。


`load("lsquares")`はこの関数をロードします。


例:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) a : lsquares_estimates (
             M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);

                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
(%i4) lsquares_residual_mse (
             M, [z,x,y], (z + D)^2 = A*x + B*y + C, first (a));
                              169
(%o4)                         ----
                              2560
```

<!-- category: Statistics -->
<!-- keywords: lsquares_residuals -->
<!-- signatures: lsquares_residuals(D, x, e, a) -->
### Function: lsquares_residuals (D, x, e, a)

指定されたパラメータ *a*とデータ *D*での
方程式 *e*に関する残差を返します。



*D*は行列で、 *x*は変数のリスト、
*e*は方程式か一般式です;
もし方程式でないなら、 *e*は
`e = 0`であるかのように扱われます。
*a*は
*x*を除いた*e*の任意の自由変数に値を指定する
方程式のリストです。


残差は以下のように定義されます:



$$
{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right),
$$


```maxima
lhs(e ) - rhs(e )
                             i         i
```


ここで、
`e[i]`は、
*a*から任意の残りの自由変数を割り当てて、
`i`番目のデータ `D[i]`から値を割り当てられた
*x*の中の変数に対して評価された方程式 *e*です。


`load("lsquares")`はこの関数をロードします。


例:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                                  [ 1  1  1 ]
                                  [         ]
                                  [ 3       ]
                                  [ -  1  2 ]
                                  [ 2       ]
                                  [         ]
(%o2)                             [ 9       ]
                                  [ -  2  1 ]
                                  [ 4       ]
                                  [         ]
                                  [ 3  2  2 ]
                                  [         ]
                                  [ 2  2  1 ]
(%i3) a : lsquares_estimates (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                         59        27      10921        107
(%o3)            [[A = - --, B = - --, C = -----, D = - ---]]
                         16        16      1024         32
(%i4) lsquares_residuals (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, first(a));
                            13    13    13  13  13
(%o4)                      [--, - --, - --, --, --]
                            64    64    32  64  64
```

<!-- category: Statistics -->
<!-- keywords: plsquares -->
<!-- signatures: plsquares(Mat, VarList, depvars), plsquares(Mat, VarList, depvars, maxexpon), plsquares(Mat, VarList, depvars, maxexpon, maxdegree) -->
### Function: plsquares (Mat, VarList, depvars)

「最小二乗」法によるデータ表の多変数多項式調整。
*Mat*はデータを含む行列であり、
*VarList*は変数名(Mat列それぞれの名前ですが、Mat列を無視する際には変数名の代わりに"-")のリストであり、
*depvars*は従属変数の名前か、
従属変数の1つ以上の名前(その名前*VarList*の中になければいけません)のリストであり、
*maxexpon*はオプションの、独立変数それぞれの最大指数(デフォルト1)であり、
*maxdegree*はオプションの最大多項式次数(デフォルトで*maxexpon*)です;
それぞれの項の指数の和は*maxdegree*以下でなければいけないことに注意してください。
もし `maxdgree = 0`なら制限は適用されません。


もし *depvars*が(リストではなく)従属変数の名前なら、
`plsquares`は調整された多項式を返します。
もし *depvars*が1つ以上の従属変数のリストなら、
`plsquares`は調整された多項式のリストを返します。
適合度について知らせるために
決定係数が表示されます。
それは0 (無相関)から1 (厳密相関)までの範囲です。
これらの値は
グローバル変数 *DETCOEF*(もし *depvars*がリストならリスト)にも保管されます。



多変数線形調整の簡単な例:


```maxima
(%i1) load("plsquares")$

(%i2) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z);
     Determination Coefficient for z = .9897039897039897
                       11 y - 9 x - 14
(%o2)              z = ---------------
                              3
```


次数制限のない同じ例:


```maxima
(%i3) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z,1,0);
     Determination Coefficient for z = 1.0
                    x y + 23 y - 29 x - 19
(%o3)           z = ----------------------
                              6
```


N面ポリゴンは何本の対角線を持ちますか？
いくつの多項式次数を使うべきですか？


```maxima
(%i4) plsquares(matrix([3,0],[4,2],[5,5],[6,9],[7,14],[8,20]),
                [N,diagonals],diagonals,5);
     Determination Coefficient for diagonals = 1.0
                                2
                               N  - 3 N
(%o4)              diagonals = --------
                                  2
(%i5) ev(%, N=9);   /* Testing for a 9 sides polygon */
(%o5)                 diagonals = 27
```


何通りの方法でn掛けnのチェス盤に2つのクィーンを取られないように置けますか？


```maxima
(%i6) plsquares(matrix([0,0],[1,0],[2,0],[3,8],[4,44]),
                [n,positions],[positions],4);
     Determination Coefficient for [positions] = [1.0]

                         4       3      2
                      3 n  - 10 n  + 9 n  - 2 n
(%o6)    [positions = -------------------------]
                                  6

(%i7) ev(%[1], n=8); /* Testing for a (8 x 8) chessboard */
(%o7)                positions = 1288
```


6つの従属変数を持つ例:


```maxima
(%i8) mtrx:matrix([0,0,0,0,0,1,1,1],[0,1,0,1,1,1,0,0],
                  [1,0,0,1,1,1,0,0],[1,1,1,1,0,0,0,1])$
(%i8) plsquares(mtrx,[a,b,_And,_Or,_Xor,_Nand,_Nor,_Nxor],
                     [_And,_Or,_Xor,_Nand,_Nor,_Nxor],1,0);
      Determination Coefficient for
[_And, _Or, _Xor, _Nand, _Nor, _Nxor] =
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
(%o2) [_And = a b, _Or = - a b + b + a,
_Xor = - 2 a b + b + a, _Nand = 1 - a b,
_Nor = a b - b - a + 1, _Nxor = 2 a b - b - a + 1]
```


この関数を使うには、
最初に `load("lsquares")`を書いてください。

