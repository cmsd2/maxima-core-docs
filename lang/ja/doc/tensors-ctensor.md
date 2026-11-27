## ctensor

<!-- category: Tensors -->
<!-- keywords: bdvac -->
<!-- signatures: bdvac(f) -->
### Function: bdvac (f)

Brans- Dicke重力理論の
真空場の方程式の
共変成分を生成します。
スカラ場は引数 *f*で指定されます。
*f*は、
例えば、`'p(x)`のように、
関数依存性を持つ(クォートされた)関数名でなければいけません。


二階共変場テンソルの成分は配列 `bd`で表されます。

<!-- category: Tensors -->
<!-- keywords: bimetric -->
<!-- signatures: bimetric() -->
### Function: bimetric ()

*** NOT YET IMPLEMENTED ***


Rosenの二計量(bimetric)理論の場の方程式を生成します。
場の方程式は `rosen`と名付けられた配列の成分です。

<!-- category: Tensors -->
<!-- keywords: cdisplay -->
<!-- signatures: cdisplay(ten) -->
### Function: cdisplay (ten)

多次元配列で表されるように、
テンソル *ten*の要素すべてを表示します。
他のタイプの変数はもちろん、
階数0と1のテンソルが
`ldisplay`を使ったように表示されます。
階数2のテンソルは
2次元行列として表示され、
より高い階数のテンソルは2次元行列のリストとして表示されます。
例えば、
Schwarzschild計量のRiemannテンソルは以下のように見ることができます:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) riemann(false);
(%o4)                                done
(%i5) cdisplay(riem);
          [ 0               0                   0           0     ]
          [                                                       ]
          [                              2                        ]
          [      3 m (r - 2 m)   m    2 m                         ]
          [ 0  - ------------- + -- - ----      0           0     ]
          [            4          3     4                         ]
          [           r          r     r                          ]
          [                                                       ]
riem    = [                                m (r - 2 m)            ]
    1, 1  [ 0               0              -----------      0     ]
          [                                     4                 ]
          [                                    r                  ]
          [                                                       ]
          [                                           m (r - 2 m) ]
          [ 0               0                   0     ----------- ]
          [                                                4      ]
          [                                               r       ]

                                [    2 m (r - 2 m)       ]
                                [ 0  -------------  0  0 ]
                                [          4             ]
                                [         r              ]
                     riem     = [                        ]
                         1, 2   [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]

                                [         m (r - 2 m)    ]
                                [ 0  0  - -----------  0 ]
                                [              4         ]
                                [             r          ]
                     riem     = [                        ]
                         1, 3   [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]

                                [            m (r - 2 m) ]
                                [ 0  0  0  - ----------- ]
                                [                 4      ]
                                [                r       ]
                     riem     = [                        ]
                         1, 4   [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]

                               [       0         0  0  0 ]
                               [                         ]
                               [       2 m               ]
                               [ - ------------  0  0  0 ]
                    riem     = [    2                    ]
                        2, 1   [   r  (r - 2 m)          ]
                               [                         ]
                               [       0         0  0  0 ]
                               [                         ]
                               [       0         0  0  0 ]

             [     2 m                                         ]
             [ ------------  0        0               0        ]
             [  2                                              ]
             [ r  (r - 2 m)                                    ]
             [                                                 ]
             [      0        0        0               0        ]
             [                                                 ]
  riem     = [                         m                       ]
      2, 2   [      0        0  - ------------        0        ]
             [                     2                           ]
             [                    r  (r - 2 m)                 ]
             [                                                 ]
             [                                         m       ]
             [      0        0        0         - ------------ ]
             [                                     2           ]
             [                                    r  (r - 2 m) ]

                                [ 0  0       0        0 ]
                                [                       ]
                                [            m          ]
                                [ 0  0  ------------  0 ]
                     riem     = [        2              ]
                         2, 3   [       r  (r - 2 m)    ]
                                [                       ]
                                [ 0  0       0        0 ]
                                [                       ]
                                [ 0  0       0        0 ]

                                [ 0  0  0       0       ]
                                [                       ]
                                [               m       ]
                                [ 0  0  0  ------------ ]
                     riem     = [           2           ]
                         2, 4   [          r  (r - 2 m) ]
                                [                       ]
                                [ 0  0  0       0       ]
                                [                       ]
                                [ 0  0  0       0       ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [ m          ]
                               3, 1   [ -  0  0  0 ]
                                      [ r          ]
                                      [            ]
                                      [ 0  0  0  0 ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [    m       ]
                               3, 2   [ 0  -  0  0 ]
                                      [    r       ]
                                      [            ]
                                      [ 0  0  0  0 ]

                               [   m                      ]
                               [ - -   0   0       0      ]
                               [   r                      ]
                               [                          ]
                               [        m                 ]
                               [  0   - -  0       0      ]
                    riem     = [        r                 ]
                        3, 3   [                          ]
                               [  0    0   0       0      ]
                               [                          ]
                               [              2 m - r     ]
                               [  0    0   0  ------- + 1 ]
                               [                 r        ]

                                    [ 0  0  0    0   ]
                                    [                ]
                                    [ 0  0  0    0   ]
                                    [                ]
                         riem     = [            2 m ]
                             3, 4   [ 0  0  0  - --- ]
                                    [             r  ]
                                    [                ]
                                    [ 0  0  0    0   ]

                                [       0        0  0  0 ]
                                [                        ]
                                [       0        0  0  0 ]
                                [                        ]
                     riem     = [       0        0  0  0 ]
                         4, 1   [                        ]
                                [      2                 ]
                                [ m sin (theta)          ]
                                [ -------------  0  0  0 ]
                                [       r                ]

                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                     riem     = [ 0        0        0  0 ]
                         4, 2   [                        ]
                                [         2              ]
                                [    m sin (theta)       ]
                                [ 0  -------------  0  0 ]
                                [          r             ]

                              [ 0  0          0          0 ]
                              [                            ]
                              [ 0  0          0          0 ]
                              [                            ]
                   riem     = [ 0  0          0          0 ]
                       4, 3   [                            ]
                              [                2           ]
                              [         2 m sin (theta)    ]
                              [ 0  0  - ---------------  0 ]
                              [                r           ]

           [        2                                             ]
           [   m sin (theta)                                      ]
           [ - -------------         0                0         0 ]
           [         r                                            ]
           [                                                      ]
           [                         2                            ]
           [                    m sin (theta)                     ]
riem     = [        0         - -------------         0         0 ]
    4, 4   [                          r                           ]
           [                                                      ]
           [                                          2           ]
           [                                   2 m sin (theta)    ]
           [        0                0         ---------------  0 ]
           [                                          r           ]
           [                                                      ]
           [        0                0                0         0 ]

(%o5)                                done
```

<!-- category: Tensors -->
<!-- keywords: cframe_flag -->
<!-- signatures: cframe_flag -->
### Variable: cframe_flag

計算を
ホロノミック(holonomic)計量と対比して動標構に関係して実行するようにします。
標構は逆標構配列 `fri`と標構計量 `lfg`で定義されます。
Cartesian標構を使う計算に関して、
`lfg`は適切な次元の単位行列でなければいけません;
Lorentz標構での計算に関して、
`lfg`は適切な符号を持たなければいけません。

<!-- category: Tensors -->
<!-- keywords: cgeodesic -->
<!-- signatures: cgeodesic(dis) -->
### Function: cgeodesic (dis)

`ctensor` (成分テンソル)パッケージの関数。
`cgeodesic`は
与えられた計量での運動の測地方程式を計算します。
それらは配列 `geod[i]`に格納されます。
もし引数 *dis*が `true`なら、
これらの方程式が表示されます。

<!-- category: Tensors -->
<!-- keywords: checkdiv -->
<!-- signatures: checkdiv() -->
### Function: checkdiv ()

ベクトル場(発散)の対応するn個の成分を印字することで
(最初の添字が共変でなければいけない)混合二階テンソルの共変発散を計算します。
ここでn = `dim`です。
もし関数の引数が `g`なら、
Einsteinテンソルの発散が形成され、零にならなければいけません。
加えて、発散(ベクトル)は
配列名 `div`を与えられます。

<!-- category: Tensors -->
<!-- keywords: christof -->
<!-- signatures: christof(dis) -->
### Function: christof (dis)

`ctensor` (成分テンソル)パッケージの関数。
各種Christoffel記号を計算します。
引数 *dis*は
どの結果をすぐに表示するか決めます。
第一種と第二種Christoffel記号は
それぞれ配列 `lcs[i,j,k]`と `mcs[i,j,k]`に格納され、
最初の2つの添字に対して対称と定義されます。
もし `christof`の引数が `lcs`か `mcs`なら
それぞれ、`lcs[i,j,k]`か `mcs[i,j,k]`の固有の非零値が
表示されます。
もし引数が `all`なら、
`lcs[i,j,k]`と `mcs[i,j,k]`の固有の非零値が表示されます。
もし引数が `false`なら、
要素の表示はされません。
配列要素 `mcs[i,j,k]`は
最後の添字が反変であるような方法で定義されます。

<!-- category: Tensors -->
<!-- keywords: cmetric -->
<!-- signatures: cmetric(dis), cmetric() -->
### Function: cmetric (dis)

計量の逆元を計算し、将来の計算のためパッケージを設定する
`ctensor`(成分テンソル)パッケージの関数


もし`cframe_flag`が`false`なら、
関数は逆計量`ug`を(ユーザー定義の)行列`lg`から計算します。
計量の行列式も計算され、変数`gdet`に保存されます。
更に、パッケージは計量が対角的か調べ、結果に従って`diagmetric`の値を設定します。
もしオプション引数*dis*が渡されて、それが`false`でないなら、
ユーザーは計量の逆元を見るように促されます。


もし`cframe_flag`が`true`なら、
関数は`fri` (逆標構行列)と`lfg`(標構計量)の値が定義されていると考えます。
これらから、標構行列`fr`と逆標構計量`ufg`が計算されます。

<!-- category: Tensors -->
<!-- keywords: cnonmet_flag -->
<!-- signatures: cnonmet_flag -->
### Variable: cnonmet_flag

非計量性係数が
接続係数の計算に含まれるようにします。
コントーションテンソルは
ユーザーが提供する非計量性ベクトル `nm`から
関数 `nonmetricity`によって計算されます。

<!-- category: Tensors -->
<!-- keywords: cograd -->
<!-- signatures: cograd() -->
### Function: cograd ()

スカラ関数の
共変勾配を計算します。
`contragrad`が以下で例示する例のように
ユーザーは対応するベクトル名を選べます。

<!-- category: Tensors -->
<!-- keywords: contortion -->
<!-- signatures: contortion(tr) -->
### Function: contortion (tr)

ねじれテンソル *tr*から(2,1)コントーション(contortion)係数を計算します。

<!-- category: Tensors -->
<!-- keywords: contragrad -->
<!-- signatures: contragrad() -->
### Function: contragrad ()

スカラ関数の反変勾配を計算します。
Computes the contravariant gradient of a scalar function allowing

Schwarzschild計量に関する以下の例が例示するように
ユーザーは対応するベクトル名を選べます:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(f,r);
(%o4)                               [f(r)]
(%i5) cograd(f,g1);
(%o5)                                done
(%i6) listarray(g1);
(%o6)                            [0, f , 0, 0]
                                      r
(%i7) contragrad(f,g2);
(%o7)                                done
(%i8) listarray(g2);
                               f  r - 2 f  m
                                r        r
(%o8)                      [0, -------------, 0, 0]
                                     r
```

<!-- category: Tensors -->
<!-- keywords: csetup -->
<!-- signatures: csetup() -->
### Function: csetup ()

パッケージを初期化し、ユーザーに計量を対話的に入力可能にする
`ctensor`(成分テンソル)パッケージの関数
より詳細は`ctensor`を参照してください。

<!-- category: Tensors -->
<!-- keywords: ct_coords -->
<!-- signatures: ct_coords -->
### Variable: ct_coords

デフォルト値: `[]`


`ctensor` (成分テンソル)パッケージのオプション。
`ct_coords`は座標のリストを含みます。
関数 `csetup`がコールされる時通常定義される一方、
割り当て `ct_coords: [j1, j2, ..., jn]`で座標を再定義できます。
ここで、jは新しい座標名です。
`csetup`も参照してください。

<!-- category: Tensors -->
<!-- keywords: ct_coordsys -->
<!-- signatures: ct_coordsys(coordinate_system, extra_arg), ct_coordsys(coordinate_system) -->
### Function: ct_coordsys (coordinate_system, extra_arg)

あらかじめ定義された座標系と計量を設定します。
引数*coordinate_system*は以下のシンボルのいずれかです:



```maxima
SYMBOL             Dim Coordinates     Description/comments
 ------------------------------------------------------------------
 cartesian2d           2  [x,y]             Cartesian 2D 座標系
 polar                 2  [r,phi]           極座標系
 elliptic              2  [u,v]             楕円座標系
 confocalelliptic      2  [u,v]             共焦点楕円座標
 bipolar               2  [u,v]             二極座標系
 parabolic             2  [u,v]             放物座標系
 cartesian3d           3  [x,y,z]           Cartesian 3D 座標系
 polarcylindrical      3  [r,theta,z]       円筒z極2D
 ellipticcylindrical   3  [u,v,z]           円筒z楕円2D
 confocalellipsoidal   3  [u,v,w]           共焦点楕円
 bipolarcylindrical    3  [u,v,z]           円筒z二極2D
 paraboliccylindrical  3  [u,v,z]           円筒z放物2D
 paraboloidal          3  [u,v,phi]         Paraboloidal coords.
 conical               3  [u,v,w]           円錐座標
 toroidal              3  [u,v,phi]         環状座標
 spherical             3  [r,theta,phi]     球座標系
 oblatespheroidal      3  [u,v,phi]         偏球座標系
 oblatespheroidalsqrt  3  [u,v,phi]
 prolatespheroidal     3  [u,v,phi]         長形球座標系
 prolatespheroidalsqrt 3  [u,v,phi]
 ellipsoidal           3  [r,theta,phi]     楕円体座標系
 cartesian4d           4  [x,y,z,t]         Cartesian 4D 座標系
 spherical4d           4  [r,theta,eta,phi] 球 4D 座標系
 exteriorschwarzschild 4  [t,r,theta,phi]   Schwarzschild 計量
 interiorschwarzschild 4  [t,z,u,v]         内部 Schwarzschild 計量
 kerr_newman           4  [t,r,theta,phi]   荷電軸対称計量
```


`coordinate_system`は
座標変数を含むリストが続く変換関数のリストでもあり得ます。
例えば、
以下のように球計量を指定できます:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o2)                                done
(%i3) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o3)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
(%i4) ct_coords;
(%o4)                           [r, theta, phi]
(%i5) dim;
(%o5)                                  3
```


`cframe_flag`が `true`の時
変換関数も使うことができます:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) cframe_flag:true;
(%o2)                                true
(%i3) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o3)                                done
(%i4) fri;
(%o4)
 [cos(phi)cos(theta) -cos(phi) r sin(theta) -sin(phi) r cos(theta)]
 [                                                                ]
 [sin(phi)cos(theta) -sin(phi) r sin(theta)  cos(phi) r cos(theta)]
 [                                                                ]
 [    sin(theta)           r cos(theta)                0          ]

(%i5) cmetric();
(%o5)                                false
(%i6) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o6)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
```


オプションの引数 *extra_arg*は以下のいずれかです:



`cylindrical`は `ct_coordsys`に追加の極座標を結びつけるように言います。


`minkowski`は `ct_coordsys`に
負の計量符号を持つ追加の座標を結びつけるように言います。


`all`は `ct_coordsys`に
計量を設定した後、
`cmetric`と `christof(false)`をコールするように言います。



もしグローバル変数 `verbose`が `true`に設定されているなら、
`ct_coordsys`は、
 `cframe_flag`の値に依存して、
`dim`, `ct_coords`と、 `lg`か `lfg`のいずれかと
`fri`の値を表示します。

<!-- category: Tensors -->
<!-- keywords: ctaylor -->
<!-- signatures: ctaylor() -->
### Function: ctaylor ()

`ctaylor`関数は、
`taylor`を使ってその後`ratdisrep`をコールすることで
引数をTaylor級数に変換することで、
引数を切り詰めます。
これは
展開変数 `ctayvar`に関してより高い項を落とす合わせ効果を持ちます。
落とす項の次数は`ctaypov`で定義されます;
級数展開が実行される点は
`ctaypt`で指定されます。


例として、
Minkowski計量の置換である簡単な計量を考えます。
追加の制約なしでは、
対角計量でさえ
はるかに複雑すぎるEinsteinテンソルの式を生成します:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) derivabbrev:true;
(%o3)                                true
(%i4) ct_coords:[t,r,theta,phi];
(%o4)                         [t, r, theta, phi]
(%i5) lg:matrix([-1,0,0,0],[0,1,0,0],[0,0,r^2,0],
                [0,0,0,r^2*sin(theta)^2]);
                        [ - 1  0  0         0        ]
                        [                            ]
                        [  0   1  0         0        ]
                        [                            ]
(%o5)                   [          2                 ]
                        [  0   0  r         0        ]
                        [                            ]
                        [              2    2        ]
                        [  0   0  0   r  sin (theta) ]
(%i6) h:matrix([h11,0,0,0],[0,h22,0,0],[0,0,h33,0],[0,0,0,h44]);
                            [ h11   0    0    0  ]
                            [                    ]
                            [  0   h22   0    0  ]
(%o6)                       [                    ]
                            [  0    0   h33   0  ]
                            [                    ]
                            [  0    0    0   h44 ]
(%i7) depends(l,r);
(%o7)                               [l(r)]
(%i8) lg:lg+l*h;
      [ h11 l - 1      0          0                 0            ]
      [                                                          ]
      [     0      h22 l + 1      0                 0            ]
      [                                                          ]
(%o8) [                        2                                 ]
      [     0          0      r  + h33 l            0            ]
      [                                                          ]
      [                                    2    2                ]
      [     0          0          0       r  sin (theta) + h44 l ]
(%i9) cmetric(false);
(%o9)                                done
(%i10) einstein(false);
(%o10)                               done
(%i11) ntermst(ein);
[[1, 1], 62]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 24]
[[2, 3], 0]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 0]
[[3, 3], 46]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 46]
(%o12)                               done
```


しかし、もしこの例を
変数 `l`に対して線形という近似として
再研鑽するなら、
もっと簡潔な式を得ます:



```maxima
(%i14) ctayswitch:true;
(%o14)                               true
(%i15) ctayvar:l;
(%o15)                                 l
(%i16) ctaypov:1;
(%o16)                                 1
(%i17) ctaypt:0;
(%o17)                                 0
(%i18) christof(false);
(%o18)                               done
(%i19) ricci(false);
(%o19)                               done
(%i20) einstein(false);
(%o20)                               done
(%i21) ntermst(ein);
[[1, 1], 6]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 13]
[[2, 3], 2]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 2]
[[3, 3], 9]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 9]
(%o21)                               done
(%i22) ratsimp(ein[1,1]);
                         2      2  4               2     2
(%o22) - (((h11 h22 - h11 ) (l )  r  - 2 h33 l    r ) sin (theta)
                              r               r r

                            2               2      4    2
              - 2 h44 l    r  - h33 h44 (l ) )/(4 r  sin (theta))
                       r r                r
```


この能力は
例えば、
重力源から遠く、弱い場極限で取り組む時に
役に立つかもしれません。

<!-- category: Tensors -->
<!-- keywords: ctaypov -->
<!-- signatures: ctaypov -->
### Variable: ctaypov

`ctayswitch`が `true`に設定されている時
Taylor級数展開で使われる最大べき数

<!-- category: Tensors -->
<!-- keywords: ctaypt -->
<!-- signatures: ctaypt -->
### Variable: ctaypt

`ctayswitch`が `true`に設定されている時
Taylor級数展開が実行される点。

<!-- category: Tensors -->
<!-- keywords: ctayswitch -->
<!-- signatures: ctayswitch -->
### Variable: ctayswitch

もし `true`に設定されているなら、
いくつかの `ctensor`計算が
Taylor級数展開を使って実行されるようにします。
現在、 `christof`, `ricci`, `uricci`, `einstein`,
`weyl`がこの設定を考慮します。

<!-- category: Tensors -->
<!-- keywords: ctayvar -->
<!-- signatures: ctayvar -->
### Variable: ctayvar

`ctayswitch`が `true`に設定されているなら
Taylor級数展開で使われる変数。

<!-- category: Tensors -->
<!-- keywords: ctorsion_flag -->
<!-- signatures: ctorsion_flag -->
### Variable: ctorsion_flag

コントーションテンソルが
接続係数の計算に含まれるようにします。
コントーションテンソル自体は
ユーザーが提供するテンソル `tr`から
`contortion`によって計算されます。

<!-- category: Tensors -->
<!-- keywords: ctransform -->
<!-- signatures: ctransform(M) -->
### Function: ctransform (M)

任意の平方対称行列 *M*上で座標変換を実行する
`ctensor` (成分テンソル)パッケージの関数。
ユーザーは変換を定義する函数を入力しなければいけません。
(以前`transform`と呼ばれていました。)

<!-- category: Tensors -->
<!-- keywords: ctrgsimp -->
<!-- signatures: ctrgsimp -->
### Variable: ctrgsimp

テンソルを計算する時、三角関数整理を使うようにします。
現在、
`ctrgsimp`は
動標構を含む計算だけに影響します。

<!-- category: Tensors -->
<!-- keywords: deleten -->
<!-- signatures: deleten(L, n) -->
### Function: deleten (L, n)

*n*番目の要素を削除した*L*から成る新しいリストを返します。

<!-- category: Tensors -->
<!-- keywords: diagmatrixp -->
<!-- signatures: diagmatrixp(M) -->
### Function: diagmatrixp (M)

もし *M*が対角行列か対角 (2D) 配列なら
`true`を返します。

<!-- category: Tensors -->
<!-- keywords: diagmetric -->
<!-- signatures: diagmetric -->
### Variable: diagmetric

デフォルト値: `false`


`ctensor` (成分テンソル)パッケージのオプション。
もし `diagmetric`が `true`なら、
特殊なルーチンが
計量の対角性を考慮して
(計量テンソルを明示的に含む)幾何的オブジェクトすべてを
計算します。
もちろん、実行時間短縮になります。
注意: 
もし対角計量が指定されたら、
`csetup`は自動的にこのオプションを設定します。

<!-- category: Tensors -->
<!-- keywords: dim -->
<!-- signatures: dim -->
### Variable: dim

デフォルト値: 4


`ctensor` (成分テンソル)パッケージのオプション。
`dim`は
デフォルト4の多様体の次元です。
コマンド `dim: n`は
次元を任意の別の値 `n`に再設定します。

<!-- category: Tensors -->
<!-- keywords: einstein -->
<!-- signatures: einstein(dis) -->
### Function: einstein (dis)

`ctensor` (成分テンソル)パッケージの関数。
`einstein`は、
(関数 `christof`と `ricci`を使って)
Christoffel記号と Ricciテンソルを得られた後、
混合 Einsteinテンソルを計算します。
もし引数 *dis*が `true`なら、
混合 Einsteinテンソル `ein[i,j]`の非零値が表示されます。
ここで `j`は反変添字です。
変数 `rateinstein`は
これらの成分上の有理整理をもたらします。
もし `ratfac`が `true`なら、
成分は因数分解もされます。

<!-- category: Tensors -->
<!-- keywords: fb -->
<!-- signatures: fb -->
### Variable: fb

`frame_bracket`によって計算される、
標構ブラケット係数。

<!-- category: Tensors -->
<!-- keywords: findde -->
<!-- signatures: findde(A, n) -->
### Function: findde (A, n)

*n*次元の平方配列 *A*要素に対応する
独自の(unique)微分方程式(式)のリストを返します。
現在、 *n*は2か3を指定できます
`deindex`は
これらの独自の微分方程式に従う
*A*の添字を含む
グローバルリストです。
2次元配列であるEinsteinテンソル (`ein`)に関して、
もし以下の例で計量に関して計算するなら、
`findde`は以下の独立微分方程式を与えます:




```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) dim:4;
(%o3)                                  4
(%i4) lg:matrix([a, 0, 0, 0], [ 0, x^2, 0, 0],
                              [0, 0, x^2*sin(y)^2, 0], [0,0,0,-d]);
                          [ a  0       0        0  ]
                          [                        ]
                          [     2                  ]
                          [ 0  x       0        0  ]
(%o4)                     [                        ]
                          [         2    2         ]
                          [ 0  0   x  sin (y)   0  ]
                          [                        ]
                          [ 0  0       0       - d ]
(%i5) depends([a,d],x);
(%o5)                            [a(x), d(x)]
(%i6) ct_coords:[x,y,z,t];
(%o6)                            [x, y, z, t]
(%i7) cmetric();
(%o7)                                done
(%i8) einstein(false);
(%o8)                                done
(%i9) findde(ein,2);
                                            2
(%o9) [d  x - a d + d, 2 a d d    x - a (d )  x - a  d d  x
        x                     x x         x        x    x

                                              2          2
                          + 2 a d d   - 2 a  d , a  x + a  - a]
                                   x       x      x
(%i10) deindex;
(%o10)                     [[1, 1], [2, 2], [4, 4]]
```

<!-- category: Tensors -->
<!-- keywords: frame_bracket -->
<!-- signatures: frame_bracket(fr, fri, diagframe) -->
### Function: frame_bracket (fr, fri, diagframe)

標構(frame)ブラケット (`fb[]`).


以下の定義に従って標構ブラケットを計算します:



```maxima
c          c         c        d     e
ifb   = ( ifri    - ifri    ) ifr   ifr
   ab         d,e       e,d      a     b
```

<!-- category: Tensors -->
<!-- keywords: gdet -->
<!-- signatures: gdet -->
### Variable: gdet

計量テンソル `lg`の行列式。
`cframe_flag`が `false`に設定されている時、
`cmetric`によって計算されます。

<!-- category: Tensors -->
<!-- keywords: init_ctensor -->
<!-- signatures: init_ctensor() -->
### Function: init_ctensor ()

`ctensor`パッケージを初期化します。


`init_ctensor`関数は`ctensor`パッケージを再初期化します。
それは`ctensor`が使う配列、行列すべてを削除し、
フラグすべてをリセットし、
`dim`を4にリセットし、
標構計量を Lorentz標構にリセットします。

<!-- category: Tensors -->
<!-- keywords: invariant1 -->
<!-- signatures: invariant1() -->
### Function: invariant1 ()

R^2の不変密度に関する
混合Euler- Lagrangeテンソル(場の方程式)を生成します。
場の方程式は `inv1`と名付けられた配列の成分です。

<!-- category: Tensors -->
<!-- keywords: invariant2 -->
<!-- signatures: invariant2() -->
### Function: invariant2 ()

*** NOT YET IMPLEMENTED ***


`ric[i,j]*uriem[i,j]`の不変密度に関する
混合Euler- Lagrangeテンソル(場の方程式)を生成します。
場の方程式は `inv2`と名付けられた配列の成分です。

<!-- category: Tensors -->
<!-- keywords: kinvariant -->
<!-- signatures: kinvariant -->
### Variable: kinvariant

Kretchmann不変量。
`rinvariant`が計算します。

<!-- category: Tensors -->
<!-- keywords: kt -->
<!-- signatures: kt -->
### Variable: kt

コントーションテンソル。
`contortion`が `tr`から計算します。

<!-- category: Tensors -->
<!-- keywords: leinstein -->
<!-- signatures: leinstein(dis) -->
### Function: leinstein (dis)

共変 Einsteinテンソル。
`leinstein`は
配列 `lein`に共変 Einsteinテンソルの値を格納します。
共変 Einsteinテンソルは、
計量テンソルを掛けることで
混合 Einsteinテンソル `ein`から計算されます。
もし引数 *dis*が `true`なら、
共変 Einsteinテンソルの非零値が表示されます。

<!-- category: Tensors -->
<!-- keywords: lfg -->
<!-- signatures: lfg -->
### Variable: lfg

共変標構計量。
デフォルトでは、
符号 (+,+,+,-)を持つ4次元Lorentz標構に初期化されます。
`cframe_flag`が `true`の時使われます。

<!-- category: Tensors -->
<!-- keywords: lg -->
<!-- signatures: lg -->
### Variable: lg

計量テンソル。
このテンソルは
他の計算が実行される前に
(`dim`掛け `dim`行列として)指定されなければいけません。

<!-- category: Tensors -->
<!-- keywords: lriem -->
<!-- signatures: lriem -->
### Variable: lriem

共変Riemannテンソル。
`lriemann`が計算します。

<!-- category: Tensors -->
<!-- keywords: lriemann -->
<!-- signatures: lriemann(dis) -->
### Function: lriemann (dis)

共変 Riemannテンソル (`lriem[]`).


配列 `lriem`として
共変 Riemannテンソルを計算します。
もし引数 *dis*が `true`なら、
固有の非零値が表示されます。


もし変数 `cframe_flag`が `true`なら、
共変 Riemannテンソルは
標構場係数から直接計算されます。
そうでないなら、
(3,1) Riemannテンソルが最初に計算されます。


添字順序の情報は `riemann`を参照してください。

<!-- category: Tensors -->
<!-- keywords: nm -->
<!-- signatures: nm -->
### Variable: nm

ユーザーが提供する非計量性ベクトル。
`nonmetricity`が使います。

<!-- category: Tensors -->
<!-- keywords: nmc -->
<!-- signatures: nmc -->
### Variable: nmc

`nonmetricity`が `nm`から計算する
非計量性係数。

<!-- category: Tensors -->
<!-- keywords: nonmetricity -->
<!-- signatures: nonmetricity(nm) -->
### Function: nonmetricity (nm)

非計量性ベクトル *nm*から(2,1)非計量性係数を計算します。

<!-- category: Tensors -->
<!-- keywords: np -->
<!-- signatures: np -->
### Variable: np

Newman-Penroseヌルテトラド。
`nptetrad`が計算します。

<!-- category: Tensors -->
<!-- keywords: npi -->
<!-- signatures: npi -->
### Variable: npi

上付き添字 Newman-Penroseヌルテトラド。
`nptetrad`が計算します。
`ug.np`として定義されます。
積 `np.transpose(npi)`は定数です:



```maxima
(%i39) trigsimp(np.transpose(npi));
                              [  0   - 1  0  0 ]
                              [                ]
                              [ - 1   0   0  0 ]
(%o39)                        [                ]
                              [  0    0   0  1 ]
                              [                ]
                              [  0    0   1  0 ]
```

<!-- category: Tensors -->
<!-- keywords: nptetrad -->
<!-- signatures: nptetrad() -->
### Function: nptetrad ()

Newman-Penroseヌルテトラド(null tetrad) (`np`)と上付き添字対応物
 (`npi`)を計算します。
例えば、 `petrov`を参照してください。


ヌルテトラドは
計量符号 (-,+,+,+)を持つ4次元直交標構計量が使われいるという仮定の上で
構成されます。
ヌルテトラドの成分は、
以下のように、
逆標構行列に関係します:



```maxima
np  = (fri  + fri ) / sqrt(2)
  1       1      2

np  = (fri  - fri ) / sqrt(2)
  2       1      2

np  = (fri  + %i fri ) / sqrt(2)
  3       3         4

np  = (fri  - %i fri ) / sqrt(2)
  4       3         4
```

<!-- category: Tensors -->
<!-- keywords: ntermst -->
<!-- signatures: ntermst(f) -->
### Function: ntermst (f)

ユーザーに
二重に下付き添字テンソル(配列) *f*の「サイズ」のquick pictureを与えます。
二番目の要素が
一番目の要素が指定する成分のNTERMSに対応する2つの要素のリストを印字します。
この方法で、
非零式をすばやく見つけて整理を試みることが可能です。

<!-- category: Tensors -->
<!-- keywords: petrov -->
<!-- signatures: petrov() -->
### Function: petrov ()

`psi[0]`...`psi[4]`で特徴付けられる
計量のPetrov分類を計算します。


例えば、以下は
Kerr計量の Petrov分類を得る方法を例示します:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) (cframe_flag:true,gcd:spmod,ctrgsimp:true,ratfac:true);
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) ug:invert(lg)$
(%i5) weyl(false);
(%o5)                                done
(%i6) nptetrad(true);
(%t6) np =

[ sqrt(r - 2 m)           sqrt(r)                                 ]
[---------------   ---------------------    0            0        ]
[sqrt(2) sqrt(r)   sqrt(2) sqrt(r - 2 m)                          ]
[                                                                 ]
[ sqrt(r - 2 m)            sqrt(r)                                ]
[---------------  - ---------------------   0            0        ]
[sqrt(2) sqrt(r)    sqrt(2) sqrt(r - 2 m)                         ]
[                                                                 ]
[                                          r      %i r sin(theta) ]
[       0                    0          -------   --------------- ]
[                                       sqrt(2)       sqrt(2)     ]
[                                                                 ]
[                                          r       %i r sin(theta)]
[       0                    0          -------  - ---------------]
[                                       sqrt(2)        sqrt(2)    ]

                             sqrt(r)         sqrt(r - 2 m)
(%t7) npi = matrix([- ---------------------,---------------, 0, 0],
                      sqrt(2) sqrt(r - 2 m) sqrt(2) sqrt(r)

          sqrt(r)            sqrt(r - 2 m)
[- ---------------------, - ---------------, 0, 0],
   sqrt(2) sqrt(r - 2 m)    sqrt(2) sqrt(r)

           1               %i
[0, 0, ---------, --------------------],
       sqrt(2) r  sqrt(2) r sin(theta)

           1                 %i
[0, 0, ---------, - --------------------])
       sqrt(2) r    sqrt(2) r sin(theta)

(%o7)                                done
(%i7) psi(true);
(%t8)                              psi  = 0
                                      0

(%t9)                              psi  = 0
                                      1

                                          m
(%t10)                             psi  = --
                                      2    3
                                          r

(%t11)                             psi  = 0
                                      3

(%t12)                             psi  = 0
                                      4
(%o12)                               done
(%i12) petrov();
(%o12)                                 D
```


Petrov分類関数は以下の文献で発表されたアルゴリズムに基づいています。


"Classifying geometries in general relativity: III Classification in practice"
by Pollney, Skea, and d’Inverno, Class. Quant. Grav. 17 2885-2902 (2000).


いくつかの簡単なテストケースを除いて、
2004年12月19日時点、実装はテストされていなく、
エラーを含みそうです。

<!-- category: Tensors -->
<!-- keywords: ratchristof -->
<!-- signatures: ratchristof -->
### Variable: ratchristof

`christof`が有理整理を適用するようにします。

<!-- category: Tensors -->
<!-- keywords: rateinstein -->
<!-- signatures: rateinstein -->
### Variable: rateinstein

デフォルト値: `true`


もし `true`なら、
Einsteinテンソルの非零成分上で
有理整理が実行されます;
もし
`ratfac`が `true`なら、
成分は因数分解もされます。

<!-- category: Tensors -->
<!-- keywords: ratriemann -->
<!-- signatures: ratriemann -->
### Variable: ratriemann

デフォルト値: `true`


Riemannテンソルの整理を制御するスイッチの1つです;
もし `true`なら、
有理整理がされます;
もし `ratfac`が `true`なら、
成分それぞれは因数分解もされます。

<!-- category: Tensors -->
<!-- keywords: ratweyl -->
<!-- signatures: ratweyl -->
### Variable: ratweyl

デフォルト値: `true`


もし `true`なら、
このスイッチは,
`weyl`関数が
Weylテンソルの値に有理整理を適用するようにします。
もし`ratfac`が `true`なら、
成分は因数分解もされます。

<!-- category: Tensors -->
<!-- keywords: ric -->
<!-- signatures: ric -->
### Variable: ric

混合Ricciテンソル。
`ricci`が計算します。

<!-- category: Tensors -->
<!-- keywords: ricci -->
<!-- signatures: ricci(dis) -->
### Function: ricci (dis)

`ctensor` (成分テンソル)パッケージの関数。
`ricci`は
Ricciテンソルの共変(対称)成分 `ric[i,j]`を計算します。
もし引数 *dis*が `true`なら、
非零成分が表示されます。

<!-- category: Tensors -->
<!-- keywords: riem -->
<!-- signatures: riem -->
### Variable: riem

(3,1) Riemannテンソル。
関数 `riemann`が呼び出された時計算されます。
添字順序についての情報については、
`riemann`の記述を参照してください。


もし `cframe_flag`が `true`なら、
`riem`は
共変Riemannテンソル `lriem`から計算されます。

<!-- category: Tensors -->
<!-- keywords: riemann -->
<!-- signatures: riemann(dis) -->
### Function: riemann (dis)

`ctensor` (成分テンソル)パッケージの関数。
`riemann`は
与えられた計量と対応するChristoffel記号から
Riemann曲率テンソルを計算します。
以下の添字慣例が使われます:



```maxima
l      _l       _l       _l   _m    _l   _m
 R[i,j,k,l] =  R    = |      - |      + |    |   - |    |
                ijk     ij,k     ik,j     mk   ij    mj   ik
```


この表記法は
`itensor`パッケージとその `icurvature`関数で使われる表記法と
一致しています。
もしオプション引数 *dis*が `true`なら、
固有の非零成分 `riem[i,j,k,l]`が表示されます。
Einsteinテンソルと同様に
ユーザーが設定する様々なスイッチが
Riemannテンソルの成分の整理を制御します。
もし `ratriemann`が `true`なら、
有理整理がされます。
もし `ratfac`が `true`なら、
成分のそれぞれは因数分解もされます。


もし変数 `cframe_flag`が `false`なら、
Riemannテンソルは
Christoffel記号から直接計算されます。
もし `cframe_flag`が `true`なら、
共変 Riemannテンソルは
標構場係数から最初に計算されます。

<!-- category: Tensors -->
<!-- keywords: rinvariant -->
<!-- signatures: rinvariant() -->
### Function: rinvariant ()

テンソル


```maxima
lriem[i,j,k,l]*uriem[i,j,k,l].
```

を縮約することで得られるKretschmann不変量 (`kinvariant`)を形成します。


このオブジェクトは非常に大きくなるかもしれないので、
自動的には整理されません。

<!-- category: Tensors -->
<!-- keywords: scurvature -->
<!-- signatures: scurvature() -->
### Function: scurvature ()

与えられた計量を持つ Riemannian多様体の
(Ricciテンソルを縮約することで得られる)スカラ曲率を返します。

<!-- category: Tensors -->
<!-- keywords: symmetricp -->
<!-- signatures: symmetricp(M) -->
### Function: symmetricp (M)

もし *M*が対称行列か対称 (2D) 配列なら
`true`を返します。

<!-- category: Tensors -->
<!-- keywords: tensorkill -->
<!-- signatures: tensorkill -->
### Variable: tensorkill

テンソルパッケージが初期化されたかを示す変数。
`csetup`が設定し使います。
`init_ctensor`が再設定します。

<!-- category: Tensors -->
<!-- keywords: tr -->
<!-- signatures: tr -->
### Variable: tr

ユーザーが提供するねじれを表す階数3のテンソル
`contortion`が使います。

<!-- category: Tensors -->
<!-- keywords: ufg -->
<!-- signatures: ufg -->
### Variable: ufg

逆標構計量。
`cframe_flag`が `true`に設定されているなら、
`cmetric`がコールされた時
`lfg`から計算されます。

<!-- category: Tensors -->
<!-- keywords: ug -->
<!-- signatures: ug -->
### Variable: ug

計量テンソルの逆元。
`cmetric`が計算します。

<!-- category: Tensors -->
<!-- keywords: uric -->
<!-- signatures: uric -->
### Variable: uric

反変Ricciテンソル。
`ricci`が計算します。

<!-- category: Tensors -->
<!-- keywords: uricci -->
<!-- signatures: uricci(dis) -->
### Function: uricci (dis)

この関数は最初にRicciテンソルの共変成分 `ric[i,j]`を計算します。
そして、混合 Ricciテンソルが反変計量テンソルを使って計算されます。
もし引数 *dis*の値が `true`なら
これらの(添字 `i`は共変で、添字 `j`は反変の)混合成分 `uric[i,j]` 
は直接表示されます。
そうでないなら、 `ricci(false)`は
結果を表示することなく、単に配列 `uric[i,j]`の要素を計算します。

<!-- category: Tensors -->
<!-- keywords: uriem -->
<!-- signatures: uriem -->
### Variable: uriem

反変Riemannテンソル。

<!-- category: Tensors -->
<!-- keywords: uriemann -->
<!-- signatures: uriemann(dis) -->
### Function: uriemann (dis)

配列要素 `uriem[i,j,k,l]`として
Riemann曲率テンソルの反変成分を計算します。
もし *dis*が `true`なら、これらが表示されます。

<!-- category: Tensors -->
<!-- keywords: weyl -->
<!-- signatures: weyl(dis) -->
### Function: weyl (dis)

Weylの共形テンソルを計算します。
もし引数 *dis*が `true`なら、
非零成分 `weyl[i,j,k,l]`がユーザーに表示されます。
そうでないなら、これらの成分は
単に計算され、格納されます。
もしスイッチ `ratweyl`が `true`に設定されているなら、
成分は有理整理されます;
もし `ratfac`が `true`なら、
結果は因数分解もされます。

