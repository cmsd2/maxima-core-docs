## linearalgebra

<!-- category: LinearAlgebra -->
<!-- keywords: addmatrices -->
<!-- signatures: addmatrices(f, M_1, ..., M_n) -->
### Function: addmatrices (f, M_1, ..., M_n)

関数*f*を加算関数として使い、
行列*M_1*, ..., *M_n*の和を返します。
関数*f*は任意の数の引数を受け付けなければいけません(Maxima n項関数)。


例:









```maxima
(%i1) m1 : matrix([1,2],[3,4])$
(%i2) m2 : matrix([7,8],[9,10])$
(%i3) addmatrices('max,m1,m2);
(%o3) matrix([7,8],[9,10])
(%i4) addmatrices('max,m1,m2,5*m1);
(%o4) matrix([7,10],[15,20])
```

<!-- category: LinearAlgebra -->
<!-- keywords: blockmatrixp -->
<!-- signatures: blockmatrixp(M) -->
### Function: blockmatrixp (M)

*M*のエントリがすべて行列なら、その時に限って、
trueを返します。

<!-- category: LinearAlgebra -->
<!-- keywords: cholesky -->
<!-- signatures: cholesky(M), cholesky(M, field) -->
### Function: cholesky (M)

自己共役(すなわちHermite)行列のCholesky分解を返します。


二番目の引数はデフォルトでは’generalring’です。
*field*の取り得る値の説明については `lu_factor`を参照してください。

<!-- category: LinearAlgebra -->
<!-- keywords: columnop -->
<!-- signatures: columnop(M, i, j, theta) -->
### Function: columnop (M, i, j, theta)

もし*M*が行列なら、
列演算`C_i <- C_i - theta * C_j`を施すことで生じる行列を返します。
もし*M*が行*i*か行*j*を持たないなら
エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: columnspace -->
<!-- signatures: columnspace(M) -->
### Function: columnspace (M)

もし *M*が行列なら、
`span (v_1, ..., v_n)`を返します。
ここで、集合 `{v_1, ..., v_n}`は
*M*の列空間の基底です。
空集合の包は `{0}`です。
従って、列空間が1員だけ持つ時、
`span ()`を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: columnswap -->
<!-- signatures: columnswap(M, i, j) -->
### Function: columnswap (M, i, j)

もし *M*が行列なら、列 *i*と *j*を交換します。
もし *M*に列 *i*か *j*がないなら、
エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: copy -->
<!-- signatures: copy(e) -->
### Function: copy (e)

Maxima式 *e*のコピーを返します。
*e*は任意のMaxima式であり得ますが、
*e*がリストか行列の時、
コピー関数はもっとも役立ちます;
以下を考えてください:










```maxima
(%i1) m : [1,[2,3]]$
(%i2) mm : m$
(%i3) mm[2][1] : x$
(%i4) m;
(%o4)                      [1,[x,3]]
(%i5) mm;
(%o5)                      [1,[x,3]]
```


同じ実験を試みましょう。
しかし、今回 *mm*を *m*のコピーとします。










```maxima
(%i6) m : [1,[2,3]]$
(%i7) mm : copy(m)$
(%i8) mm[2][1] : x$
(%i9) m;
(%o9)                     [1,[2,3]]
(%i10) mm;
(%o10)                    [1,[x,3]]
```


今回、 *mm*への割り当ては*m*の値を変えません。

<!-- category: LinearAlgebra -->
<!-- keywords: ctranspose -->
<!-- signatures: ctranspose(M) -->
### Function: ctranspose (M)

行列 *M*の複素共役転置を返します。
関数 `ctranspose`は
それぞれの行列要素を転置するのに
`matrix_element_transpose`を使います。

<!-- category: LinearAlgebra -->
<!-- keywords: diag_matrix -->
<!-- signatures: diag_matrix(d_1, d_2, ..., d_n) -->
### Function: diag_matrix (d_1, d_2, ..., d_n)

対角成分 *d_1*, *d_2*,...,*d_n*を持つ対角行列を返します。
対角成分が行列の時、
戻り値行列の零成分は
適切なサイズの零行列です;
例えば:







```maxima
(%i1) diag_matrix(diag_matrix(1,2),diag_matrix(3,4));

                            [ [ 1  0 ]  [ 0  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  2 ]  [ 0  0 ] ]
(%o1)                       [                    ]
                            [ [ 0  0 ]  [ 3  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  0 ]  [ 0  4 ] ]
(%i2) diag_matrix(p,q);

                                   [ p  0 ]
(%o2)                              [      ]
                                   [ 0  q ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: dotproduct -->
<!-- signatures: dotproduct(u, v) -->
### Function: dotproduct (u, v)

ベクトル *u*と *v*の内積を返します。
これは`conjugate (transpose (u)) . v`と同じです。
引数 *u*と *v*は列ベクトルでなければいけません。

<!-- category: LinearAlgebra -->
<!-- keywords: eigens_by_jacobi -->
<!-- signatures: eigens_by_jacobi(A), eigens_by_jacobi(A, field_type) -->
### Function: eigens_by_jacobi (A)

*A*の固有値と固有ベクトルを
Jacobi回転法で計算します。
*A*は対称行列でなければいけません。
(しかし、正定値である必要も半正定値である必要もありません。)
*field_type*は計算上の体を示し、`floatfield`か `bigfloatfield`です。
もし *field_type*が指定されないなら、
デフォルトは `floatfield`です。


*A*の要素は、数か、
(*field_type*に依存して)`float`か `bfloat`を介して
数に評価される式でなければいけません。


例:












```maxima
(%i1) S: matrix([1/sqrt(2), 1/sqrt(2)],[-1/sqrt(2), 1/sqrt(2)]);
                     [     1         1    ]
                     [  -------   ------- ]
                     [  sqrt(2)   sqrt(2) ]
(%o1)                [                    ]
                     [      1        1    ]
                     [ - -------  ------- ]
                     [   sqrt(2)  sqrt(2) ]
(%i2) L : matrix ([sqrt(3), 0], [0, sqrt(5)]);
                      [ sqrt(3)     0    ]
(%o2)                 [                  ]
                      [    0     sqrt(5) ]
(%i3) M : S . L . transpose (S);
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- + -------  ------- - ------- ]
            [    2         2        2         2    ]
(%o3)       [                                      ]
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- - -------  ------- + ------- ]
            [    2         2        2         2    ]
(%i4) eigens_by_jacobi (M);
The largest percent change was 0.1454972243679
The largest percent change was 0.0
number of sweeps: 2
number of rotations: 1
(%o4) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i5) float ([[sqrt(3), sqrt(5)], S]);
(%o5) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i6) eigens_by_jacobi (M, bigfloatfield);
The largest percent change was 1.454972243679028b-1
The largest percent change was 0.0b0
number of sweeps: 2
number of rotations: 1
(%o6) [[1.732050807568877b0, 2.23606797749979b0], 
                [  7.071067811865475b-1   7.071067811865475b-1 ]
                [                                              ]]
                [ - 7.071067811865475b-1  7.071067811865475b-1 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: get_lu_factors -->
<!-- signatures: get_lu_factors(x) -->
### Function: get_lu_factors (x)

`x = lu_factor (A)`の時、
`get_lu_factors`は
形式 `[P, L, U]`のリストを返します。
ここで、 *P*は置換行列、 *L*は対角成分を含む下三角行列、
*U*は上三角行列であり、
 `A = P L U`が成り立ちます。

<!-- category: LinearAlgebra -->
<!-- keywords: hankel -->
<!-- signatures: hankel(col), hankel(col, row) -->
### Function: hankel (col)

Hankel行列 *H*を返します。
*H*の最初の列は *col*です;
最初の成分を除いて、
*H*の最後の行は *row*です。
*row*のデフォルトは *col*と同じ長さを持つ零ベクトルです。

<!-- category: LinearAlgebra -->
<!-- keywords: hessian -->
<!-- signatures: hessian(f, x) -->
### Function: hessian (f, x)

変数 *x*のリストに関する *f*のHessian行列を返します。
Hessian行列の `(i, j)`成分は
`diff(f, x[i], 1, x[j], 1)`です。


例:








```maxima
(%i1) hessian (x * sin (y), [x, y]);
                     [   0       cos(y)   ]
(%o1)                [                    ]
                     [ cos(y)  - x sin(y) ]
(%i2) depends (F, [a, b]);
(%o2)                       [F(a, b)]
(%i3) hessian (F, [a, b]);
                        [   2      2   ]
                        [  d F    d F  ]
                        [  ---   ----- ]
                        [    2   da db ]
                        [  da          ]
(%o3)                   [              ]
                        [   2      2   ]
                        [  d F    d F  ]
                        [ -----   ---  ]
                        [ da db     2  ]
                        [         db   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: hilbert_matrix -->
<!-- signatures: hilbert_matrix(n) -->
### Function: hilbert_matrix (n)

*n*掛け*n*のHilbert行列を返します。
*n*が正の整数でない時、エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: identfor -->
<!-- signatures: identfor(M), identfor(M, fld) -->
### Function: identfor (M)

行列 *M*と同じ形を持つ単位行列を返します。
単位行列の対角成分は体 *fld*の乗算単位元です;
*fld*のデフォルトは *generalring*です。


一番目の引数 *M*は平方行列か非行列でなければいけません。
*M*が行列の時、 *M*のそれぞれの成分は平方行列であり得ます。
– 従って、 *M*は区分されたMaxima行列であり得ます。
行列は、任意の(有限の)深さに区分できます。


`zerofor`も参照してください。

<!-- category: LinearAlgebra -->
<!-- keywords: invert_by_lu -->
<!-- signatures: invert_by_lu(M, (rng generalring)) -->
### Function: invert_by_lu (M, (rng generalring))

LU分解を使って、
行列 *M*の逆行列を返します。
LU分解は環 *rng*を使って実行されます。

<!-- category: LinearAlgebra -->
<!-- keywords: jacobian -->
<!-- signatures: jacobian(f, x) -->
### Function: jacobian (f, x)

変数のリスト *x*に関する
関数のリスト *f*のJacobi行列を返します。
Jacobi行列の `(i, j)`成分は
`diff(f[i], x[j])`です。


例:








```maxima
(%i1) jacobian ([sin (u - v), sin (u * v)], [u, v]);
                  [ cos(v - u)  - cos(v - u) ]
(%o1)             [                          ]
                  [ v cos(u v)   u cos(u v)  ]
(%i2) depends ([F, G], [y, z]);
(%o2)                  [F(y, z), G(y, z)]
(%i3) jacobian ([F, G], [y, z]);
                           [ dF  dF ]
                           [ --  -- ]
                           [ dy  dz ]
(%o3)                      [        ]
                           [ dG  dG ]
                           [ --  -- ]
                           [ dy  dz ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: kronecker_product -->
<!-- signatures: kronecker_product(A, B) -->
### Function: kronecker_product (A, B)

行列 *A*と *B*のKronecker積を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: locate_matrix_entry -->
<!-- signatures: locate_matrix_entry(M, r_1, c_1, r_2, c_2, f, rel) -->
### Function: locate_matrix_entry (M, r_1, c_1, r_2, c_2, f, rel)

一番目の引数は行列でなければいけません;
引数 *r_1*から *c_2*は
行 *r_1*から *r_2*と列 *c_1*から *c_2*から成る
*M*の部分行列を決定します。


ある性質を満たす部分行列 *M*の中の成分を見つけます。
3つのケース:


(1) `rel = 'bool`で *f*が述語論理: 


左から右へ、そして上から下へ部分行列をスキャンし、
述語論理 *f*を満たす最初の成分のインデックスを返します。
もし *f*を満たす行列成分がないなら、 `false`を返します。


(2) `rel = 'max`で *f*が実関数:


*f*を最大にする成分を探して部分行列をスキャンします。
最大化の成分のインデックスを返します。


(3) `rel = 'min`で *f*が実関数:


*f*を最小にする成分を探して部分行列をスキャンします。
最小化の成分のインデックスを返します。

<!-- category: LinearAlgebra -->
<!-- keywords: lu_backsub -->
<!-- signatures: lu_backsub(M, b) -->
### Function: lu_backsub (M, b)

`M = lu_factor (A, field)`の時、
`lu_backsub (M, b)`は
線形系 `A x = b`を解きます。

<!-- category: LinearAlgebra -->
<!-- keywords: lu_factor -->
<!-- signatures: lu_factor(M, field) -->
### Function: lu_factor (M, field)

形式 `[LU, perm, fld]`か
`[LU, perm, fld, lower-cnd upper-cnd]`
のリストを返します。
ここで、


  

(1) 行列 *LU*は*M*の分解をパックされた形式で含みます。
パックされた形式は3つのことを意味します;
第一に *LU*の行はリスト *perm*に従って置換されます。
もし、例えば、 *perm*がリスト `[3,2,1]`なら、
*LU*分解の実際の一番目の行は行列 *LU*の三番目の行です。
第二に、mの下三角因子はすべて1で置き換えられた対角成分を持つ *LU*の下三角部です。
第三に、 *M*の上三角因子は *LU*の上三角部です。


  

(2) 体が `floatfield`か `complexfield`の時、
数 *lower-cnd*と *upper-cnd*は
*M*の無限ノルム条件数の下限と上限です。
すべての体に対して条件数を見積ることができるわけではありません;
そんな体に対しては `lu_factor`は2項目リストを返します。
下限と上限どちらも真の値から任意に大きな因子だけ異なる可能性があります。
(`mat_cond`も参照してください。)

   

引数 *M*は平方行列でなければいけません。


オプション引数 *fld*は環か体かを決めるシンボルでなければいけません。
予め定義された体と環は以下のものがあります:


    

(a) `generalring` – Maxima式の環,
    (b) `floatfield` –  倍精度浮動小数点数体,
    (c) `complexfield` –  倍精度浮動小数点複素数体,
    (d) `crering`  – Maxima CRE式の環,
    (e) `rationalfield` – 有理数体,
    (f) `runningerror` – 浮動小数点の丸め誤差をトラック,
    (g) `noncommutingring` – 乗算が非可換ドット演算子のMaxima式の環


体が `floatfield`か `complexfield`、`runningerror`のいずれかの時、
アルゴリズムは部分ピボットを使います;
他のすべての体に対しては、
零ピボットを避ける必要があるときだけ、行がスイッチされます。


浮動小数点加算算術は結合的でなく、
’体’の意味は数学的定義と異なります。


体 `runningerror`の要素は
形式 `[x,n]`の2つの要素のMaximaリストです。
ここで、 *x*は浮動小数点数で、
`n`は整数です。
 `x`の’真’の値と `x`の相対差は
計算機イプシロンに `n`をかけたもので近似的に抑えられます。
The running error bound drops some terms that of the order the square of the machine epsilon.


新しい体を定義するユーザーインターフェースはありません。
Common Lispに精通しているユーザーは新しい体を定義することができるはずです。
これをするには、ユーザーは算術演算のための関数と
体表現とMaximaの相互変換のための関数を定義しなければいけません。
さらに、(部分ピボットが使われる)順序体に関しては、
ユーザーは大きさの関数と体の元の比較関数を定義しなければいけません。
あとは、Common Lisp 構造体 `mring`を定義することだけです。
ファイル `mring`に多くの例があります。

 

分解を計算するために、
最初の仕事は
行列成分それぞれを指定された体の元に変換することです。
変換が不可能な時は、分解はエラーメッセージとともに停止します。
体の元はMaxima式である必要はありません。
例えば、`complexfield`の元はCommon Lisp複素数です。
そして、分解を計算した後には、行列成分はMaxima式に変換されなければいけません。


`get_lu_factors`も参照してください。


例:















```maxima
(%i1) w[i,j] := random (1.0) + %i * random (1.0);
(%o1)          w     := random(1.) + %i random(1.)
                i, j
(%i2) showtime : true$
Evaluation took 0.00 seconds (0.00 elapsed)
(%i3) M : genmatrix (w, 100, 100)$
Evaluation took 7.40 seconds (8.23 elapsed)
(%i4) lu_factor (M, complexfield)$
Evaluation took 28.71 seconds (35.00 elapsed)
(%i5) lu_factor (M, generalring)$
Evaluation took 109.24 seconds (152.10 elapsed)
(%i6) showtime : false$

(%i7) M : matrix ([1 - z, 3], [3, 8 - z]); 
                        [ 1 - z    3   ]
(%o7)                   [              ]
                        [   3    8 - z ]
(%i8) lu_factor (M, generalring);
          [ 1 - z         3        ]
          [                        ]
(%o8)    [[   3            9       ], [1, 2], generalring]
          [ -----  - z - ----- + 8 ]
          [ 1 - z        1 - z     ]
(%i9) get_lu_factors (%);
                  [   1    0 ]  [ 1 - z         3        ]
        [ 1  0 ]  [          ]  [                        ]
(%o9)  [[      ], [   3      ], [                9       ]]
        [ 0  1 ]  [ -----  1 ]  [   0    - z - ----- + 8 ]
                  [ 1 - z    ]  [              1 - z     ]
(%i10) %[1] . %[2] . %[3];
                        [ 1 - z    3   ]
(%o10)                  [              ]
                        [   3    8 - z ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: mat_cond -->
<!-- signatures: mat_cond(M, 1), mat_cond(M, inf) -->
### Function: mat_cond (M, 1)

行列 *m*の*p*-ノルムの行列条件数を返します。
*p*に許される値は1と *inf*です。
この関数は、行列 *m*の逆元を計算するのにLU分解を使います。
このため、`mat_cond`の実行時間は行列サイズの三乗に比例します;
`lu_factor`は、
行列サイズの二乗に比例する時間内に
無限大ノルム条件数の下限と上限を決定します。

<!-- category: LinearAlgebra -->
<!-- keywords: mat_fullunblocker -->
<!-- signatures: mat_fullunblocker(M) -->
### Function: mat_fullunblocker (M)

もし *M*が区分行列なら、
行列をすべてのレベルで区分解除します。
もし *M*が行列なら、
*M*を返します; それ以外ではエラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: mat_norm -->
<!-- signatures: mat_norm(M, 1), mat_norm(M, inf), mat_norm(M, frobenius) -->
### Function: mat_norm (M, 1)

行列 *M*の行列 *p*-ノルムを返します。
.  The allowed values for 
*p*に許される値は1か `inf`か `frobenius` (Frobenius行列ノルム)です。
行列 *M*は区分されない行列でなければいけません。

<!-- category: LinearAlgebra -->
<!-- keywords: mat_trace -->
<!-- signatures: mat_trace(M) -->
### Function: mat_trace (M)

行列 *M*の跡を返します。
もし *M*が行列でないなら、名詞形を返します。
*M*が区分行列の時、
`mat_trace(M)`は
`mat_trace(mat_unblocker(m))`するのと同じ値を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: mat_unblocker -->
<!-- signatures: mat_unblocker(M) -->
### Function: mat_unblocker (M)

もし *M*が区分行列なら、
*M*を1レベル区分解除します。
もし *M*が行列なら、
`mat_unblocker (M)`は *M*を返します;
それ以外ではエラーをシグナルします。


このように、
もし *M*の成分それぞれが行列なら、
`mat_unblocker (M)`は区分されていない行列を返しますが、
もし *M*の成分それぞれが区分行列なら、
`mat_unblocker (M)`は
区分が1レベル少ない区分行列を返します。


もし区分行列を使うなら、
おそらく、
`matrix_element_mult`を `"."`に、
`matrix_element_transpose`を `'transpose`に設定したくなるでしょう。
`mat_fullunblocker`も参照してください。


例:









```maxima
(%i1) A : matrix ([1, 2], [3, 4]);
                            [ 1  2 ]
(%o1)                       [      ]
                            [ 3  4 ]
(%i2) B : matrix ([7, 8], [9, 10]);
                            [ 7  8  ]
(%o2)                       [       ]
                            [ 9  10 ]
(%i3) matrix ([A, B]);

                     [ [ 1  2 ]  [ 7  8  ] ]
(%o3)                [ [      ]  [       ] ]
                     [ [ 3  4 ]  [ 9  10 ] ]

(%i4) mat_unblocker (%);
                         [ 1  2  7  8  ]
(%o4)                    [             ]
                         [ 3  4  9  10 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_size -->
<!-- signatures: matrix_size(M) -->
### Function: matrix_size (M)

行列 *M*の行数と列数をそれぞれ与える2要素リストを返します。

<!-- category: LinearAlgebra -->
<!-- keywords: nullity -->
<!-- signatures: nullity(M) -->
### Function: nullity (M)

もし *M*が行列なら、
*M*の零空間の次元を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: nullspace -->
<!-- signatures: nullspace(M) -->
### Function: nullspace (M)

もし *M*が行列なら、
`span (v_1, ..., v_n)`を返します。
ここで、, where the set
集合 `{v_1, ..., v_n}`は
*M*の零空間の基底です。
空集合のスパンは `{0}`です。
なので、零空間が要素を1つだけ持つときは、`span ()`を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: orthogonal_complement -->
<!-- signatures: orthogonal_complement(v_1, ..., v_n) -->
### Function: orthogonal_complement (v_1, ..., v_n)

`span (u_1, ..., u_m)`を返します。
ここで、, where the se
集合 `{u_1, ..., u_m}`は
集合 `(v_1, ..., v_n)`の直交補空間の基底です。


ベクトル *v_1*から *v_n*それぞれは列ベクトルでなければいけません。

<!-- category: LinearAlgebra -->
<!-- keywords: polynomialp -->
<!-- signatures: polynomialp(p, L, coeffp, exponp), polynomialp(p, L, coeffp), polynomialp(p, L) -->
### Function: polynomialp (p, L, coeffp, exponp)

もし *p*がリスト *L*の中の変数に関して多項式なら、
`true`を返します。
述語論理 *coeffp*は係数それぞれに対して `true`に評価されなければいけなく、
述語論理 *exponp*は
*L*の中の変数の指数すべてに対して `true`に評価されなければいけません。
もし
*exponp*に対してデフォルトでない値を使いたいなら、
たとえ*coeffp*に関してデフォルトを使いたくても
*coeffp*を値とともに供給しなければいけません。



`polynomialp (p, L, coeffp)`は
`polynomialp (p, L, coeffp, 'nonnegintegerp)`に同値です。


`polynomialp (p, L)`は
`polynomialp (p, L, 'constantp, 'nonnegintegerp)`に同値です。


多項式は展開される必要はありません:







```maxima
(%i1) polynomialp ((x + 1)*(x + 2), [x]);
(%o1)                         true
(%i2) polynomialp ((x + 1)*(x + 2)^a, [x]);
(%o2)                         false
```


coeffpとexponpにデフォルトでない値を使う例:








```maxima
(%i1) polynomialp ((x + 1)*(x + 2)^(3/2), [x], numberp, numberp);
(%o1)                         true
(%i2) polynomialp ((x^(1/2) + 1)*(x + 2)^(3/2), [x], numberp,
                                                        numberp);
(%o2)                         true
```


2変数多項式:







```maxima
(%i1) polynomialp (x^2 + 5*x*y + y^2, [x]);
(%o1)                         false
(%i2) polynomialp (x^2 + 5*x*y + y^2, [x, y]);
(%o2)                         true
```

<!-- category: LinearAlgebra -->
<!-- keywords: polytocompanion -->
<!-- signatures: polytocompanion(p, x) -->
### Function: polytocompanion (p, x)

もし *p*が
*x*の多項式なら、
*p*のコンパニオン行列を返します。
次数 *n*のモニック多項式(最高次数の係数が1の多項式)に対しては、
`p = (-1)^n charpoly (polytocompanion (p, x))`.
があります。


*p*が *x*の多項式でないなら、エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: ptriangularize -->
<!-- signatures: ptriangularize(M, v) -->
### Function: ptriangularize (M, v)

もし *M*がそれぞれの成分が*v*の多項式の行列なら、
以下のような行列 *M2*を返します。


(1) *M2*は上三角で、


(2) `M2 = E_n ... E_1 M`,
ここで、 *E_1*から *E_n*は成分が*v*の多項式の基本行列です。


(3) `|det (M)| = |det (M2)|`,


注意: この関数はすべての成分が*v*の多項式かチェックしません。

<!-- category: LinearAlgebra -->
<!-- keywords: rowop -->
<!-- signatures: rowop(M, i, j, theta) -->
### Function: rowop (M, i, j, theta)

もし *M*が行列なら、
行演算 `R_i <- R_i - theta * R_j`をすることで生じる
行列を返します。
もし *M*に行*i*か *j*がないなら、
エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: rowswap -->
<!-- signatures: rowswap(M, i, j) -->
### Function: rowswap (M, i, j)

もし *M*が行列なら、行 *i*と *j*を入れ替えます。
もし *M*に行*i*か *j*がないなら、エラーをシグナルします。

<!-- category: LinearAlgebra -->
<!-- keywords: toeplitz -->
<!-- signatures: toeplitz(col), toeplitz(col, row) -->
### Function: toeplitz (col)

Toeplitz行列 *T*を返します。
*T*の一番目の列は *col*です;
一番目の成分を除いて、
*T*の最初の行は *row*です。
*row*のデフォルトは *col*の複素共役です。


例:






```maxima
(%i1)  toeplitz([1,2,3],[x,y,z]);


                                  [ 1  y  z ]
                                  [         ]
(%o1)                             [ 2  1  y ]
                                  [         ]
                                  [ 3  2  1 ]

(%i2)  toeplitz([1,1+%i]);

                              [   1     1 - %I ]
(%o2)                         [                ]
                              [ %I + 1    1    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: vandermonde_matrix -->
<!-- signatures: vandermonde_matrix([x_1, ..., x_n]) -->
### Function: vandermonde_matrix ([x_1, ..., x_n])

*i*番目の行が`[1, x_i, x_i^2, ... x_i^(n-1)]`の
*n*掛け*n*行列を返します。

<!-- category: LinearAlgebra -->
<!-- keywords: zerofor -->
<!-- signatures: zerofor(M), zerofor(M, fld) -->
### Function: zerofor (M)

行列 *M*と同じ形の零行列を返します。
零行列の成分すべては体 *fld*の加算の単位元です;
*fld*のデフォルトは *generalring*です。


一番目の引数 *M*は
平方行列か行列以外でなければいけません。
*M*が行列の時、
*M*の成分それぞれは平方行列であり得ます。
– 従って *M*は区分Maxima行列であり得ます。
行列は任意の(有限の)深さに区分できます。


`identfor`も参照してください。

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrixp -->
<!-- signatures: zeromatrixp(M) -->
### Function: zeromatrixp (M)

*M*が区分行列でない時、
もし行列 *M*のそれぞれの要素 *e*に対して
`is (equal (e, 0))`が真なら、
`true`を返します。
*M*が区分行列の時、
もし*e*の要素それぞれに対して `zeromatrixp`が
`true`に評価されるなら、
`true`を返します。

