## atensor

<!-- category: Tensors -->
<!-- keywords: abasep -->
<!-- signatures: abasep(v) -->
### Function: abasep (v)

引数が `atensor`基底ベクトルかチェックします。
すなわち、`asymbol`の値と同じシンボルと
1と `adim`の間の数値の添字を持つ添字付きシンボルかどうか、チェックします。

<!-- category: Tensors -->
<!-- keywords: adim -->
<!-- signatures: adim -->
### Variable: adim

デフォルト値: 0


代数の次元。
`atensor`は
添字付きオブジェクトが有効な基底ベクトルか決定するのに
`adim`の値を使います。
`abasep`を参照してください。

<!-- category: Tensors -->
<!-- keywords: af -->
<!-- signatures: af(u, v) -->
### Function: af (u, v)

交換関係で使われる反対称スカラ関数。
デフォルトの実装は
両方の引数が`abasep`を使った基底ベクトルかチェックし、
もしそうなら、行列 `aform`から対応する値を代入します。

<!-- category: Tensors -->
<!-- keywords: aform -->
<!-- signatures: aform -->
### Variable: aform

デフォルト値: `ident(3)`


双一次形式`sf`, `af`, `av`のデフォルト値。
デフォルトは、単位行列 `ident(3)`です。

<!-- category: Tensors -->
<!-- keywords: asymbol -->
<!-- signatures: asymbol -->
### Variable: asymbol

デフォルト値: `v`


基底ベクトルのシンボル。

<!-- category: Tensors -->
<!-- keywords: atensimp -->
<!-- signatures: atensimp(expr) -->
### Function: atensimp (expr)

`init_atensor`のコールで構成された規則に従って、
代数テンソル式 *expr*を整理します。
整理は、
適用可能な場所への
交換関係の再帰的な適用と`sf`, `af`, `av`のコールの決定を含みます。
複雑な式に関してさえ、
関数がいつでも終了することを確実にするために
保護手段が使われます。

<!-- category: Tensors -->
<!-- keywords: av -->
<!-- signatures: av(u, v) -->
### Function: av (u, v)

交換関係で使われる反対称スカラ関数。
デフォルトの実装は
両方の引数が`abasep`を使った基底ベクトルかチェックし、
もしそうなら、行列 `aform`から対応する値を代入します。


例えば:



```maxima
(%i1) load("atensor");
(%o1)       /share/tensor/atensor.mac
(%i2) adim:3;
(%o2)                                  3
(%i3) aform:matrix([0,3,-2],[-3,0,1],[2,-1,0]);
                               [  0    3   - 2 ]
                               [               ]
(%o3)                          [ - 3   0    1  ]
                               [               ]
                               [  2   - 1   0  ]
(%i4) asymbol:x;
(%o4)                                  x
(%i5) av(x[1],x[2]);
(%o5)                                 x
                                       3
```

<!-- category: Tensors -->
<!-- keywords: init_atensor -->
<!-- signatures: init_atensor(alg_type, opt_dims), init_atensor(alg_type) -->
### Function: init_atensor (alg_type, opt_dims)

特定の代数型で
`atensor`パッケージを初期化します。
*alg_type*は以下のいずれかであり得ます:


`universal`: 普遍代数は交換規則を持ちません。


`grassmann`: Grassman代数は交換関係 `u.v+v.u=0`で定義されます。


`clifford`: Clifford代数は
交換関係 `u.v+v.u=-2*sf(u,v)`で定義されます。
ここで、 `sf`は対称スカラ値函数です。
この代数では、 *opt_dims*は、
代数の正の次元数、縮退次元数、負の次元数をそれぞれ表す3つの非負整数までありえます。
もしいずれかの *opt_dims*値が供給されたら、
`atensor`は
`adim`と `aform`の値を適切に構成します。
そうでなければ、
`adim`はデフォルトが0で、 `aform`は未定義です。


`symmetric`: 対称代数は交換関係 `u.v-v.u=0`で定義されます。


`symplectic`: シンプレクティック代数は
交換関係 `u.v-v.u=2*af(u,v)`で定義されます。
ここで、 `af`は反対称スカラ値函数です。
シンプレクティック代数では、
*opt_dims*は
非縮退次元数、縮退次元数をそれぞれ表す2つの非負整数までありえます。
もしいずれかの *opt_dims*値が供給されたら、
`atensor`は
`adim`と `aform`の値を適切に構成します。
そうでなければ、
`adim`はデフォルトが0で、 `aform`は未定義です。


`lie_envelop`: Lie包絡代数は交換関係 `u.v-v.u=2*av(u,v)`で定義されます。
ここで、 `av`は反対称函数です。


`init_atensor`関数はいくつかの予め定義された代数型も認識します:


`complex`は複素数代数をClifford代数 Cl(0,1)として実装します。
`init_atensor(complex)`をコールすることは
`init_atensor(clifford,0,0,1)`と同値です。


`quaternion`は四元数代数を実装します。
`init_atensor (quaternion)`をコールすることは
`init_atensor (clifford,0,0,2)`と同値です。


`pauli`はPauliスピノール代数をClifford代数 Cl(3,0)として実装します。
`init_atensor(pauli)`をコールすることは
`init_atensor(clifford,3)`と同値です。


`dirac`はDiracスピノール代数をClifford代数 Cl(3,1)として実装します。
`init_atensor(dirac)`をコールすることは
`init_atensor(clifford,3,0,1)`と同値です。

<!-- category: Tensors -->
<!-- keywords: sf -->
<!-- signatures: sf(u, v) -->
### Function: sf (u, v)

交換関係で使われる対称スカラ関数。
デフォルトの実装は
両方の引数が`abasep`を使った基底ベクトルかチェックし、
もしそうなら、行列 `aform`から対応する値を代入します。

