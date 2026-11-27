## unit

<!-- category: Units -->
<!-- keywords: %unitexpand -->
<!-- signatures: %unitexpand -->
### Variable: %unitexpand

デフォルト値: `2`


これは
*unit*の初期ロードの最中に
`metricexpandall`に供給される
値です。

<!-- category: Units -->
<!-- keywords: convert -->
<!-- signatures: convert(expr, list) -->
### Function: convert (expr, list)

グローバル環境をリセットすることがやりすぎの時、
`convert`コマンドがあります。
これは1回変換を許します。
変換に使うのに、1つの引数か単位のリストを受け付けることができます。
変換演算がされた時、
望みの結果が再変換されるのを避けるために
正常なグローバル評価系は迂回されます。
結果として、
もしこの振る舞いを制御しているグローバル環境(`ratprint`)が真なら、
不正確な計算に対して、"rat"警告が見られるでしょう。
これは
グローバル変換の精度の抜き取り検査に
役に立ちます。
別の特長は
たとえグローバル環境が組立次元に整理するように設定されても
`convert`はユーザーに基本次元変換することを許すことです。



```maxima
(%i2) kg*m/s^2;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) convert(kg*m/s^2,[g,km,s]);
                                     g km
(%o3)                                ----
                                       2
                                      s


(%i4) convert(kg*m/s^2,[g,inch,minute]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                              18000000000   %in g
(%o4)                        (-----------) (-----)
                                  127           2
                                            %min


(%i5) convert(kg*m/s^2,[N]);
(%o5)                                  N


(%i6) convert(kg*m^2/s^2,[N]);
(%o6)                                 m N


(%i7) setunits([N,J]);
(%o7)                                done


(%i8) convert(kg*m^2/s^2,[N]);
(%o8)                                 m N


(%i9) convert(kg*m^2/s^2,[N,inch]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                 5000
(%o9)                           (----) (%in N)
                                 127


(%i10) convert(kg*m^2/s^2,[J]);
(%o10)                                 J


(%i11) kg*m^2/s^2;
(%o11)                                 J


(%i12) setunits([g,inch,s]);
(%o12)                               done


(%i13) kg*m/s^2;
(%o13)                                 N


(%i14) uforget(N);
(%o14)                               false


(%i15) kg*m/s^2;
                                5000000   %in g
(%o15)                         (-------) (-----)
                                  127       2
                                           s


(%i16) convert(kg*m/s^2,[g,inch,s]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                5000000   %in g
(%o16)                         (-------) (-----)
                                  127       2
                                           s
```


See also 
`setunits`と `uforget`も参照してください。
この関数を使うには、最初に `load("unit")`を書いてください。

<!-- category: Units -->
<!-- keywords: metricexpandall -->
<!-- signatures: metricexpandall(x) -->
### Function: metricexpandall (x)

望みの計量単位すべてを自動的に生成するグローバル単位リストを再構築します。
*x*は
ユーザーがいくつの計量接頭子の定義を望むか指定するのに使われる数値引数です。
引数は、より低い数字の単位を定義するより高い数字それぞれを持つような
以下のようなものです:


```maxima
0 - none. Only base units
           1 - kilo, centi, milli
(default)  2 - giga, mega, kilo, hecto, deka, deci, centi, milli,
               micro, nano
           3 - peta, tera, giga, mega, kilo, hecto, deka, deci,
               centi, milli, micro, nano, pico, femto
           4 - all
```

通常は、Maximaは
これは非常にたくさんの数の単位をもたらすので、完全な展開を定義しませんが、
多少なりとも完全な方法でリストを再構築するのに
`metricexpandall`を使うことができます。
*unit.mac*ファイルの中の適切な変数は *%unitexpand*です。

<!-- category: Units -->
<!-- keywords: setunits -->
<!-- signatures: setunits(list) -->
### Function: setunits (list)

デフォルトでは、 *unit*パッケージは
組み立てられた次元はどんなものでも使いませんが、
MKS単位を使ってすべての単位を7つの基本的な次元に変換します。


```maxima
(%i2) N;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) dyn;
                                   1      kg m
(%o3)                           (------) (----)
                                 100000     2
                                           s


(%i4) g;
                                    1
(%o4)                             (----) (kg)
                                   1000


(%i5) centigram*inch/minutes^2;
                                  127        kg m
(%o5)                       (-------------) (----)
                             1800000000000     2
                                              s
```


いくつかの場合、これは望みの振る舞いです。
もしユーザーが他の単位を使いたいなら、
これは
`setunits`コマンドで達成されます:


```maxima
(%i6) setunits([centigram,inch,minute]);
(%o6)                                done


(%i7) N;
                            1800000000000   %in cg
(%o7)                      (-------------) (------)
                                 127            2
                                            %min


(%i8) dyn;
                               18000000   %in cg
(%o8)                         (--------) (------)
                                 127          2
                                          %min


(%i9) g;
(%o9)                             (100) (cg)


(%i10) centigram*inch/minutes^2;
                                    %in cg
(%o10)                              ------
                                        2
                                    %min
```


単位の設定は実に柔軟性があります。
例えば、もしキログラム、メータ、秒に、それらの次元のデフォルトとして戻りたいなら、
以下のようにできます:


```maxima
(%i11) setunits([kg,m,s]);
(%o11)                               done


(%i12) centigram*inch/minutes^2;
                                  127        kg m
(%o12)                      (-------------) (----)
                             1800000000000     2
                                              s
```


組立単位もこのコマンドで扱います:


```maxima
(%i17) setunits(N);
(%o17)                               done


(%i18) N;
(%o18)                                 N


(%i19) dyn;
                                    1
(%o19)                           (------) (N)
                                  100000


(%i20) kg*m/s^2;
(%o20)                                 N


(%i21) centigram*inch/minutes^2;
                                    127
(%o21)                        (-------------) (N)
                               1800000000000
```


Notice that the 
*unit*パッケージは
質量、長さ、力として二乗された逆時間の非MKS組み合わせを認識し、
それをNewtonのものに変換したことに注目してください。
これは一般にMaximaがどのように働くかを示します。
例えば、もしNewtonのものよりダインを好むなら、
単に以下をします:


```maxima
(%i22) setunits(dyn);
(%o22)                               done


(%i23) kg*m/s^2;
(%o23)                          (100000) (dyn)


(%i24) centigram*inch/minutes^2;
                                  127
(%o24)                         (--------) (dyn)
                                18000000
```


任意の力に整理することを中断するには、
uforgetコマンドを使います:


```maxima
(%i26) uforget(dyn);
(%o26)                               false


(%i27) kg*m/s^2;
                                     kg m
(%o27)                               ----
                                       2
                                      s


(%i28) centigram*inch/minutes^2;
                                  127        kg m
(%o28)                      (-------------) (----)
                             1800000000000     2
                                              s
```

これは、
`uforget(N)`か `uforget(%force)`を使って
同じようにうまく働きました。


`uforget`も参照してください。
この関数を使うには、最初に `load("unit")`を書いてください。

<!-- category: Units -->
<!-- keywords: uforget -->
<!-- signatures: uforget(list) -->
### Function: uforget (list)

デフォルトでは、 *unit*パッケージは
、NKS単位を使って、単位すべてを7つの基本次元に変換します。
この振る舞いは
`setunits`コマンドを使って変えることができます。
その後、ユーザーは、
`uforget`コマンドを使って，
特定の次元に関してデフォルトの振る舞いに戻すことができます:


```maxima
(%i13) setunits([centigram,inch,minute]);
(%o13)                               done


(%i14) centigram*inch/minutes^2;
                                    %in cg
(%o14)                              ------
                                        2
                                    %min


(%i15) uforget([cg,%in,%min]);
(%o15)                      [false, false, false]


(%i16) centigram*inch/minutes^2;
                                  127        kg m
(%o16)                      (-------------) (----)
                             1800000000000     2
                                              s
```


`uforget`は単位ではなく次元上で働きます。
だから、特定の次元の任意の単位は機能します。
次元それ自身も合法な引数です。


`setunits`も参照してください。
この関数を使うには、最初に `load("unit")`を書いてください。

<!-- category: Units -->
<!-- keywords: usersetunits -->
<!-- signatures: usersetunits -->
### Variable: usersetunits

デフォルト値: none


もしユーザーが
記述されたものよりもデフォルト単位の振る舞いを持ちたいなら、
それらは
*maxima-init.mac*と *usersetunits*変数を利用することができます。
*unit*パッケージは
この変数がリストに割り当てられているかを見るためにスタートアップ時にチェックします。
もし割り当てられているなら、そのリスト上でsetunitsを使い、
そのリストからの単位をデフォルトに取ります。
`uforget`は
自身のデフォルト上にusersetunitsで定義された振る舞いに戻します。
例えば、
もし
以下を含む*maxima-init.mac*ファイルを持っているなら:


```maxima
usersetunits : [N,J];
```

we would see the following behavior:


```maxima
(%i1) load("unit")$
*******************************************************************
*                       Units version 0.50                        *
*          Definitions based on the NIST Reference on             *
*              Constants, Units, and Uncertainty                  *
*       Conversion factors from various sources including         *
*                   NIST and the GNU units package                *
*******************************************************************

Redefining necessary functions...
WARNING: DEFUN/DEFMACRO: redefining function
 TOPLEVEL-MACSYMA-EVAL ...
WARNING: DEFUN/DEFMACRO: redefining function MSETCHK ...
WARNING: DEFUN/DEFMACRO: redefining function KILL1 ...
WARNING: DEFUN/DEFMACRO: redefining function NFORMAT ...
Initializing unit arrays...
Done.
User defaults found...
User defaults initialized.


(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) kg*m^3/s^2;
(%o4)                                 J m


(%i5) kg*m*km/s^2;
(%o5)                             (1000) (J)


(%i6) setunits([dyn,eV]);
(%o6)                                done


(%i7) kg*m/s^2;
(%o7)                           (100000) (dyn)


(%i8) kg*m^2/s^2;
(%o8)                     (6241509596477042688) (eV)


(%i9) kg*m^3/s^2;
(%o9)                    (6241509596477042688) (eV m)


(%i10) kg*m*km/s^2;
(%o10)                   (6241509596477042688000) (eV)


(%i11) uforget([dyn,eV]);
(%o11)                           [false, false]


(%i12) kg*m/s^2;
(%o12)                                 N


(%i13) kg*m^2/s^2;
(%o13)                                 J


(%i14) kg*m^3/s^2;
(%o14)                                J m


(%i15) kg*m*km/s^2;
(%o15)                            (1000) (J)
```

`usersetunits`なしでは、
初期の入力はMKSに変換されたでしょうし、
uforgetはMKS規則への復帰をもたらしたでしょう。
なるほど、
ユーザーの好みは両方のケースで考慮されます。
もし望まれるなら、これらはまだオーバーライドされることができることに注目してください。
この整理を完全に消すには - 
すなわち、ユーザーデフォルトを出荷デフォルトに再設定するには - 
`dontusedimension`コマンドをつかうことができます。
`usedimension`が`uforget`を使用上自由にする時だけ
`uforget`はユーザー設定を再び戻すことができますが、
代わりに、
`kill(usersetunits)`は
ユーザーデフォルトの知識すべてをセッションから完全に削除します。
以下は
これらの様々なオプションがいかに働くかを示すいくつかの例です。


```maxima
(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) setunits([dyn,eV]);
(%o4)                                done


(%i5) kg*m/s^2;
(%o5)                           (100000) (dyn)


(%i6) kg*m^2/s^2;
(%o6)                     (6241509596477042688) (eV)


(%i7) uforget([dyn,eV]);
(%o7)                          [false, false]


(%i8) kg*m/s^2;
(%o8)                                  N


(%i9) kg*m^2/s^2;
(%o9)                                  J


(%i10) dontusedimension(N);
(%o10)                             [%force]


(%i11) dontusedimension(J);
(%o11)                         [%energy, %force]


(%i12) kg*m/s^2;
                                     kg m
(%o12)                               ----
                                       2
                                      s


(%i13) kg*m^2/s^2;
                                         2
                                     kg m
(%o13)                               -----
                                       2
                                      s


(%i14) setunits([dyn,eV]);
(%o14)                               done


(%i15) kg*m/s^2;
                                     kg m
(%o15)                               ----
                                       2
                                      s


(%i16) kg*m^2/s^2;
                                         2
                                     kg m
(%o16)                               -----
                                       2
                                      s


(%i17) uforget([dyn,eV]);
(%o17)                         [false, false]


(%i18) kg*m/s^2;
                                     kg m
(%o18)                               ----
                                       2
                                      s


(%i19) kg*m^2/s^2;
                                         2
                                     kg m
(%o19)                               -----
                                       2
                                      s


(%i20) usedimension(N);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o20)                               true


(%i21) usedimension(J);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o21)                               true


(%i22) kg*m/s^2;
                                     kg m
(%o22)                               ----
                                       2
                                      s


(%i23) kg*m^2/s^2;
                                         2
                                     kg m
(%o23)                               -----
                                       2
                                      s


(%i24) setunits([dyn,eV]);
(%o24)                               done


(%i25) kg*m/s^2;
(%o25)                          (100000) (dyn)


(%i26) kg*m^2/s^2;
(%o26)                    (6241509596477042688) (eV)


(%i27) uforget([dyn,eV]);
(%o27)                           [false, false]


(%i28) kg*m/s^2;
(%o28)                                 N


(%i29) kg*m^2/s^2;
(%o29)                                 J


(%i30) kill(usersetunits);
(%o30)                               done


(%i31) uforget([dyn,eV]);
(%o31)                          [false, false]


(%i32) kg*m/s^2;
                                     kg m
(%o32)                               ----
                                       2
                                      s


(%i33) kg*m^2/s^2;
                                         2
                                     kg m
(%o33)                               -----
                                       2
                                      s
```

不運にも、
このオプションの広い多様性は
最初は少し混乱するものですが、
一旦、ユーザーがそれらを使うのに成長すれば、
それらがワーキング環境上でまさに完全な制御を持つことをユーザーは見いだすに違いありません。

