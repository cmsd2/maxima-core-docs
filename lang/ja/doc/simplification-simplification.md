## Simplification

<!-- category: Simplification -->
<!-- keywords: additive -->
<!-- signatures: additive -->
### Variable: additive

もし`declare(f, additive)`が実行されると:


(1) もし`f`が1変数関数なら、`f`が和に適用された時はいつでも、
`f`は和の上に分配整理されます。
例えば、`f(y+x)`は、`f(y)+f(x)`に整理されます。


(2) もし`f`が2変数以上の関数なら、
`sum`や`integrate`の場合と同様に
加法性が第一番目の引数に対して定義されます。
例えば、`f(h(x)+g(x),x)`は`f(h(x),x)+f(g(x),x)`に整理されます。
`f`が`sum(x[i],i,lower-limit,upper-limit)`の形の式に適用されたときには
この整理はされません。

<!-- category: Simplification -->
<!-- keywords: antisymmetric -->
<!-- signatures: antisymmetric -->
### Variable: antisymmetric

もし`declare(h,antisymmetric)`が実行されると、
`h`は反対称として整理されます。
例えば、`h(x,z,y)`は`-h(x,y,z)`と整理されます。
即ち、`symmetric`か`commutative`で得られた結果に(-1)^nを掛けたものとなります。
ここで、nはその形に変換するのに必要な置換の回数です。

<!-- category: Simplification -->
<!-- keywords: combine -->
<!-- signatures: combine(expr) -->
### Function: combine (expr)

同じ分母を持つ項を単一の項に結合することによって和*expr*を整理します。

<!-- category: Simplification -->
<!-- keywords: commutative -->
<!-- signatures: commutative -->
### Variable: commutative

もし`declare(h,commutative)`が実行されたなら、
`h`は可換関数として整理されます。
例えば、`h(x,z,y)`は`h(x,y,z)`に整理されます。
これは`symmetric`と同じです。

<!-- category: Simplification -->
<!-- keywords: demoivre -->
<!-- signatures: demoivre(expr) -->
### Function: demoivre (expr)

関数`demoivre (expr)`は、
グローバル変数`demoivre`を設定することなしに式を変換します。


変数`demoivre`が`true`の時、
複素数の指数関数は、円関数の項で表した同値な式に変換されます:
もし`b`が`%i`を含まなければ、
`exp (a + b*%i)`は、`%e^a * (cos(b) + %i*sin(b))`に整理されます。
`a`と`b`は展開されません。


`demoivre`のデフォルト値は`false`です。


`exponentialize`は、円関数や双曲関数を指数関数形に変換します。
`demoivre`と`exponentialize`は、同時に両方trueにはできません。

<!-- category: Simplification -->
<!-- keywords: distrib -->
<!-- signatures: distrib(expr) -->
### Function: distrib (expr)

和を積上に分配します。
式のトップレベルのみで働き、すなわち、再帰的でなく、
`expand`より速い点で、`expand`とは違います。
トップレベルの和すべてを展開する点で、`multthru`とは違います。


例:



```maxima
(%i1) distrib ((a+b) * (c+d));
(%o1)                 b d + a d + b c + a c
(%i2) multthru ((a+b) * (c+d));
(%o2)                 (b + a) d + (b + a) c
(%i3) distrib (1/((a+b) * (c+d)));
                                1
(%o3)                    ---------------
                         (b + a) (d + c)
(%i4) expand (1/((a+b) * (c+d)), 1, 0);
                                1
(%o4)                 ---------------------
                      b d + a d + b c + a c
```

<!-- category: Simplification -->
<!-- keywords: distribute_over -->
<!-- signatures: distribute_over -->
### Variable: distribute_over

デフォルト値: `true`


`distribute_over`は、
リストや行列や等式のようなバッグ(重複を許す集合)上の関数のマッピングを制御します。
今回、すべてのMaxima関数がこのプロパティを持つ訳ではありません。
このプロパティはコマンド`properties`で調べることが可能です。


`distribute_over`を値`false`に設定した時、
関数のマッピングはオフにスイッチされます。


例:


`sin`関数はリスト上にマップします:






```maxima
(%i1) sin([x,1,1.0]);
(%o1)                 [sin(x), sin(1), .8414709848078965]
```


`mod`は
リスト上にマップされる２変数関数です。
入れ子のリスト上のマッピングも可能です:







```maxima
(%i2) mod([x,11,2*a],10);
(%o2)                    [mod(x, 10), 1, 2 mod(a, 5)]
(%i3) mod([[x,y,z],11,2*a],10);
(%o3)       [[mod(x, 10), mod(y, 10), mod(z, 10)], 1, 2 mod(a, 5)]
```


`floor`関数の行列や等式上のマッピング:







```maxima
(%i4) floor(matrix([a,b],[c,d]));
                            [ floor(a)  floor(b) ]
(%o4)                       [                    ]
                            [ floor(c)  floor(d) ]
(%i5) floor(a=b);
(%o5)                         floor(a) = floor(b)
```


１変数以上の関数は、任意の引数上、または、すべての引数上にマップします:






```maxima
(%i6) expintegral_e([1,2],[x,y]);
(%o6) [[expintegral_e(1, x), expintegral_e(1, y)], 
       [expintegral_e(2, x), expintegral_e(2, y)]]
```


関数がプロパティdistribute_overを持つかチェックします:






```maxima
(%i7) properties(abs);
(%o7) [integral, distributes over bags, noun, rule, gradef]
```

<!-- category: Simplification -->
<!-- keywords: domain -->
<!-- signatures: domain -->
### Variable: domain

デフォルト値: `real`


`domain`が`complex`に設定されている時、
`sqrt (x^2)`は、`abs(x)`を返さず、`sqrt (x^2)`
のままを保ちます。

<!-- category: Simplification -->
<!-- keywords: evenfun, oddfun -->
<!-- signatures: oddfun -->
### Variable: evenfun

`declare(f, evenfun`や `declare(f, oddfun`は
関数 `f`を奇関数か偶関数として認識するように指示します。


例:



```maxima
(%i1) o (- x) + o (x);
(%o1)                     o(x) + o(- x)
(%i2) declare (o, oddfun);
(%o2)                         done
(%i3) o (- x) + o (x);
(%o3)                           0
(%i4) e (- x) - e (x);
(%o4)                     e(- x) - e(x)
(%i5) declare (e, evenfun);
(%o5)                         done
(%i6) e (- x) - e (x);
(%o6)                           0
```

<!-- category: Simplification -->
<!-- keywords: expand -->
<!-- signatures: expand(expr), expand(expr, p, n) -->
### Function: expand (expr)

式*expr*を展開します。
指数和や和の積の積を実行し、有理式の分子をそれぞれの項に分割し、
（可換、非可換な）積が*expr*のすべてのレベルの和で分配されます。


多項式の場合、もっと効率的なアルゴリズムの`ratexpand`を普通使うべきです。


`maxnegex`と`maxposex`はそれぞれ、展開される最大の負と正の指数を制御します。


`expand (expr, p, n)`は、
*expr*を、`maxposex`に*p*を`maxnegex`に*n*を使って展開します。
これは、式のすべてではなく、一部を展開するために役立ちます。


`expon` - 自動的に展開される最大の負のべきの指数（`expand`のコールに独立して）。
例えば、もしも`expon`が4なら`(x+1)^(-5)`は自動では展開されません。


`expop` - 自動的に展開される最大の正の指数。
もし`expop`が3以上なら、`(x+1)^3`は自動的に展開されます。
もし`n`が`expop`よりも大きい時`(x+1)^n`が展開されるのが望まれるなら、
`maxposex`が`n`より小さくない場合のみ、`expand ((x+1)^n)`の実行が行われます。


`ev`で使われる`expand`フラグによって展開が実行されます。


ファイル`share/simplification/facexp.mac`は、




ユーザーに制御された展開によって式を構成する機能を提供するいくつかの関連関数
（特に自動ロードされる`facsum`, `factorfacsum`と`collectterms`）と
変数(`nextlayerfactor`と`facsum_combine`)を含みます。

簡単な関数の記述が`simplification/facexp.usg`にあります。
`demo("facexp")`でデモが実行できます。


例:











```maxima
(%i1) expr:(x+1)^2*(y+1)^3;
                               2        3
(%o1)                   (x + 1)  (y + 1)
(%i2) expand(expr);
       2  3        3    3      2  2        2      2      2
(%o2) x  y  + 2 x y  + y  + 3 x  y  + 6 x y  + 3 y  + 3 x  y
                                                      2
                                     + 6 x y + 3 y + x  + 2 x + 1
(%i3) expand(expr,2);
               2        3              3          3
(%o3)         x  (y + 1)  + 2 x (y + 1)  + (y + 1)
(%i4) expr:(x+1)^-2*(y+1)^3;
                                   3
                            (y + 1)
(%o4)                       --------
                                   2
                            (x + 1)
(%i5) expand(expr);
            3               2
           y             3 y            3 y             1
(%o5) ------------ + ------------ + ------------ + ------------
       2              2              2              2
      x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1
(%i6) expand(expr,2,2);

                                   3
                            (y + 1)
(%o6)                     ------------
                           2
                          x  + 2 x + 1
```


展開なしに式を再整理します:








```maxima
(%i7) expr:(1+x)^2*sin(x);
                                       2
(%o7)                           (x + 1)  sin(x)
(%i8) exponentialize:true;
(%o8)                                true
(%i9) expand(expr,0,0);
                                   2    %i x     - %i x
                         %i (x + 1)  (%e     - %e      )
(%o9)                  - -------------------------------
                                        2
```

<!-- category: Simplification -->
<!-- keywords: expandwrt -->
<!-- signatures: expandwrt(expr, x_1, ..., x_n) -->
### Function: expandwrt (expr, x_1, ..., x_n)

式`expr`を、変数*x_1*, ..., *x_n*に関して展開します。
変数を含む積すべては陽に現れます。
返される形式は、変数を含む式の和の積を含みません。
*x_1*, ..., *x_n*は、変数、演算子、式であり得ます。


デフォルトでは、分母は展開されませんが、これは、スイッチ`expandwrt_denom`によって
制御することができます。


この関数は`simplification/stopex.mac`から自動ロードされます。

<!-- category: Simplification -->
<!-- keywords: expandwrt_denom -->
<!-- signatures: expandwrt_denom -->
### Variable: expandwrt_denom

デフォルト値: `false`


`expandwrt_denom`は、`expandwrt`によって有理式の扱いを制御します。
もし`true`なら、式の分子も分母も`expandwrt`の引数に従って展開されますが、
もし`expandwrt_denom`が`false`なら、分子だけがその方法で展開されます。

<!-- category: Simplification -->
<!-- keywords: expandwrt_factored -->
<!-- signatures: expandwrt_factored(expr, x_1, ..., x_n) -->
### Function: expandwrt_factored (expr, x_1, ..., x_n)

`expandwrt`に似ていますが、積の式を幾分違って扱います。
`expandwrt_factored`は、`expr`の、
変数*x_1*, ..., *x_n*を含む因子上でだけ展開します。



この関数は、`simplification/stopex.mac`から自動ロードされます。

<!-- category: Simplification -->
<!-- keywords: expon -->
<!-- signatures: expon -->
### Variable: expon

デフォルト値: 0


`expon`は、(`expand`のコールに依らず)自動的に展開される負のべき乗の最大指数です。
例えば、
もし`expon`が4なら、
`(x+1)^(-5)`は自動的には展開されません。

<!-- category: Simplification -->
<!-- keywords: exponentialize -->
<!-- signatures: exponentialize(expr) -->
### Function: exponentialize (expr)

関数`exponentialize (expr)`は、
*expr*の中の円関数や双曲関数を指数関数に変換します。
グローバル変数`exponentialize`を設定する必要はありません。


変数`exponentialize`が`true`の時、
円関数や双曲関数すべては指数関数形に変換されます。
デフォルト値は`false`です。


`demoivre`は複素数の指数関数を円関数に変換します。
`exponentialize`や`demoivre`は同時にtrueにすることはできません。

<!-- category: Simplification -->
<!-- keywords: expop -->
<!-- signatures: expop -->
### Variable: expop

デフォルト値: 0


`expop`は、自動的に展開される最高の正の指数です。
例えば、`(x + 1)^3`が入力された時、
`expop`が3以下の時だけ自動的に展開されます。
もし、`n`が`expop`より大きい`(x + 1)^n`が展開されることを望むなら、
`expand ((x + 1)^n)`の実行は、
`maxposex`がn以上の時だけ機能します。

<!-- category: Simplification -->
<!-- keywords: lassociative -->
<!-- signatures: lassociative -->
### Variable: lassociative

`declare (g, lassociative)`は、
Maximaの整理器に
`g`が左結合であることを告げます。
例えば、`g (g (a, b), g (c, d))`は`g (g (g (a, b), c), d)`に整理されます。

<!-- category: Simplification -->
<!-- keywords: linear -->
<!-- signatures: linear -->
### Variable: linear

Maximaの演算子のプロパティの１つ。
そう宣言された1変数関数`f`に関して、
"expansion" `f(x + y)`は`f(x) + f(y)`を出力し、
`a`が定数の`f(a*x)`は、`a*f(x)`を出力します。
２つ以上の引数の関数に関しては、
「線形性」は、`sum`や`integrate`の場合のように定義されます。
すなわち、`a`と`b`が`x`に独立の場合，
`f (a*x + b, x)`は`a*f(x,x) + b*f(1,x)`を出力します。


`linear`は、`additive`かつ`outative`と同値です。
`opproperties`も参照してください。

<!-- category: Simplification -->
<!-- keywords: maxnegex -->
<!-- signatures: maxnegex -->
### Variable: maxnegex

デフォルト値: 1000


`maxnegex`は、
`expand`コマンドによって展開される最大の負の指数です。
（`maxposex`)も参照してください。）

<!-- category: Simplification -->
<!-- keywords: maxposex -->
<!-- signatures: maxposex -->
### Variable: maxposex

デフォルト値: 1000


`maxposex`は、
`expand`コマンドで展開される最大指数です。
（`maxnegex`)も参照してください。）

<!-- category: Simplification -->
<!-- keywords: multiplicative -->
<!-- signatures: multiplicative -->
### Variable: multiplicative

`declare (f, multiplicative)`は、Maxima整理器に
`f`が乗法的であることを告げます。



1. もし`f`が１変数関数なら、
整理器が積に適用された`f`に出会うといつでも、
`f`はその積上に分配されます。
例えば、`f(x*y)`は`f(x)*f(y)`に整理されます。
2. もし`f`が多変数関数なら、
乗法性は、`f`の最初の引数の乗法性として定義されます。
例えば、
`f (g(x) * h(x), x)`は、`f (g(x) ,x) * f (h(x), x)`に整理されます。


この式整理は、`f`が`product (x[i], i, m, n)`の形の式に適用された時にはなされません。

<!-- category: Simplification -->
<!-- keywords: multthru -->
<!-- signatures: multthru(expr), multthru(expr_1, expr_2) -->
### Function: multthru (expr)

*expr*の（和の）因子に*expr*の他の因子を掛ける。
すなわち、*expr*は`f_1 f_2 ... f_n`です。
ここで、少なくとも１つの因子、*f_i*としましょう、は項の和です。
この和の各項に、積の中の他の因子を掛けます。
（すなわち、*f_i*を除いた因子すべてです。）
`multthru`は、指数化された和を展開しません。
この関数は、（可換であれ非可換であれ）積を和上に分配する最も速い方法です。
割り算は積として表現されるので、
`multthru`は積によって和を割ることにも使うことができます。


`multthru (expr_1, expr_2)`は、
（和もしくは等式の）*expr_2*の中の各項に*expr_1*を掛けます。
もし*expr_1*がそれ自身和でなければ、
この形式は`multthru (expr_1*expr_2)`と同値です。



```maxima
(%i1) x/(x-y)^2 - 1/(x-y) - f(x)/(x-y)^3;
                      1        x         f(x)
(%o1)             - ----- + -------- - --------
                    x - y          2          3
                            (x - y)    (x - y)
(%i2) multthru ((x-y)^3, %);
                           2
(%o2)             - (x - y)  + x (x - y) - f(x)
(%i3) ratexpand (%);
                           2
(%o3)                   - y  + x y - f(x)
(%i4) ((a+b)^10*s^2 + 2*a*b*s + (a*b)^2)/(a*b*s^2);
                        10  2              2  2
                 (b + a)   s  + 2 a b s + a  b
(%o4)            ------------------------------
                                  2
                             a b s
(%i5) multthru (%);  /* note that this does not expand (b+a)^10 */
                                        10
                       2   a b   (b + a)
(%o5)                  - + --- + ---------
                       s    2       a b
                           s
(%i6) multthru (a.(b+c.(d+e)+f));
(%o6)            a . f + a . c . (e + d) + a . b
(%i7) expand (a.(b+c.(d+e)+f));
(%o7)         a . f + a . c . e + a . c . d + a . b
```

<!-- category: Simplification -->
<!-- keywords: negdistrib -->
<!-- signatures: negdistrib -->
### Variable: negdistrib

デフォルト値: `true`


`negdistrib`が`true`の時,
 -1が式上に分配されます。
例えば、`-(x + y)`は`- y - x`になります。
`false`に設定すると、`- (x + y)`はそのまま表示されることになるでしょう。
これは時々役に立ちますが、非常に注意してください;
`simp`フラグ同様に、
当然のことながら、Maximaの中でローカルな使用以外には、
これは、`false`に設定したくないフラグの１つです。

<!-- category: Simplification -->
<!-- keywords: opproperties -->
<!-- signatures: opproperties -->
### Variable: opproperties

`opproperties`は、Maximaの整理器が認識する特殊演算子プロパティのリストです:
`linear`, `additive`, `multiplicative`, `outative`, `evenfun`,
`oddfun`, `commutative`, `symmetric`, `antisymmetric`, `nary`, 
`lassociative`, `rassociative`.

<!-- category: Simplification -->
<!-- keywords: outative -->
<!-- signatures: outative -->
### Variable: outative

`declare (f, outative)`は、Maximaの整理器に
`f`の引数の中の定数因子が外に出すことができることを告げます。



1. もし`f`が1変数関数なら、
整理器が積に適用された`f`に出会うといつでも、その積は定数因子と、ていすうでない因子に分割され、定数因子が外に出されます。
例えば、`f(a*x)`は、`a`を定数とすると、`a*f(x)`に整理されます。
非アトムな定数因子は外に出されません。
2. もし`f`が多変数関数なら、
outativityは、`sum`や`integrate`の場合のように定義されます。
すなわち、`f (a*g(x), x)`は、`a`が`x`に依らないとすると、
`a * f(g(x), x)`に整理されます。


`sum`, `integrate`, `limit`はすべて`outative`です。

<!-- category: Simplification -->
<!-- keywords: radcan -->
<!-- signatures: radcan(expr) -->
### Function: radcan (expr)

対数関数、指数関数、累乗根を含む*expr*を、与えられ場変数の順序で式の大きなクラス上の標準形式に整理します;
関数的に同値な形式は特殊な形式にマップされます。
式の幾分大きなクラスのため、`radcan`は正規の形式を生成します。
このクラスの２つの式は、必ずしも、同じ結果ではありませんが、それらの差は`radcan`によって0に整理されます。


いくつかの式のため、`radcan`は特殊な時間消費をします。
これは、因数分解や指数関数の部分分解展開に基づいた整理のための式のコンポーネントの間のある関係を探求するコストです。


















例:








```maxima
(%i1) radcan((log(x+x^2)-log(x))^a/log(1+x)^(a/2));
                                           a/2
(%o1)                            log(x + 1)

(%i2) radcan((log(1+2*a^x+a^(2*x))/log(1+a^x)));
(%o2)                                  2

(%i3) radcan((%e^x-1)/(1+%e^(x/2)));
                                     x/2
(%o3)                              %e    - 1
```

<!-- category: Simplification -->
<!-- keywords: radexpand -->
<!-- signatures: radexpand -->
### Variable: radexpand

デフォルト値: `true`


`radexpand`は、根号のいくつかの整理を制御します。


`radexpand`が`all`の時
n乗の積の因子のn番目の根を根号の外に出すようにします。
例えば、もし`radexpand`が`all`なら、
`sqrt (16*x^2)`は`4*x`に整理されます。



特に、`sqrt (x^2)`を考えます。


- *
もし`radexpand`が`all`もしくは`assume (x > 0)`が実行されたなら、
`sqrt(x^2)`は`x`に整理されます。
- *
もし`radexpand`が`true`、かつ`domain`が`real`(これはデフォルトです)なら、
`sqrt(x^2)`は`abs(x)`に整理されます。
- *
もし`radexpand`が`false`、もしくは、`radexpand`が`true`かつ`domain`が`complex`なら、
`sqrt(x^2)`は整理されません。



`domain`は、`radexpand`が`true`の時だけ意味を持つことに注意してください。

<!-- category: Simplification -->
<!-- keywords: rassociative -->
<!-- signatures: rassociative -->
### Variable: rassociative

`declare (g, rassociative)`は、
Maximaの整理器に
`g`が右結合であることを告げます。
例えば、
`g(g(a, b), g(c, d))`は、`g(a, g(b, g(c, d)))`に整理されます。

<!-- category: Simplification -->
<!-- keywords: scsimp -->
<!-- signatures: scsimp(expr, rule_1, ..., rule_n) -->
### Function: scsimp (expr, rule_1, ..., rule_n)

順次的な相対整理(Sequential Comparative Simplification) (Stouteによる方法)。
`scsimp`は、
規則*rule_1*, ..., *rule_n*に従って、
*expr*を整理しようとします。
もしより小さな式が得られたら、
プロセスは繰り返されます。
そうでなければ、すべての整理が試された後、
元の答えを返します。



`example (scsimp)`はいくつかの例を表示します。

<!-- category: Simplification -->
<!-- keywords: simp -->
<!-- signatures: simp -->
### Variable: simp

デフォルト値: `true`


`simp`は整理を有効にします。
これは標準です。
`simp`は`evflag`でもあります。
それは関数`ev`に認識されます。`ev`を参照してください。


`simp`が
値`false`で`evflag`として使われる時、
式の評価フェイズの間だけ
整理は抑制されます。
フラグは評価フェイズに続く整理を抑制できません。


例:


整理がグローバルにオフにスイッチされます。
式`sin(1.0)`は数値に整理されません。
`simp`-フラグは整理をオンにスイッチします。








```maxima
(%i1) simp:false;
(%o1)                                false
(%i2) sin(1.0);
(%o2)                              sin(1.0)
(%i3) sin(1.0),simp;
(%o3)                          .8414709848078965
```


整理が再びオンにスイッチされます。
`simp`-フラグは完全に整理を抑制できません。
割り当ては式の評価フェイズの間に起こるので、
出力は整理された式を示しますが、
変数`x`は、値として未整理の式を持ちます。








```maxima
(%i4) simp:true;
(%o4)                                true
(%i5) x:sin(1.0),simp:false;
(%o5)                          .8414709848078965
(%i6) :lisp $X
((%SIN) 1.0)
```

<!-- category: Simplification -->
<!-- keywords: symmetric -->
<!-- signatures: symmetric -->
### Variable: symmetric

`declare (h, symmetric)`は、Maximaの整理器に
`h`が対称関数であることを告げます。
例えば、`h (x, z, y)`は`h (x, y, z)`に整理されます。


`commutative`は`symmetric`と同義です。

<!-- category: Simplification -->
<!-- keywords: xthru -->
<!-- signatures: xthru(expr) -->
### Function: xthru (expr)

（和でなければいけない）*expr*のすべての項を、
共通分母上で、`ratsimp`がするように積や指数和を展開することなしに結合させます。
`xthru`は、因子が陽であるときだけ、有理式の分子と分母の共通因子を消去します。



分子と分母の最大公約数の陽因子を消去するために、式を`ratsimp`する前に`xthru`を使うのがよい場合があります。







```maxima
(%i1) ((x+2)^20 - 2*y)/(x+y)^20 + (x+y)^(-19) - x/(x+y)^20;

                                20
                 1       (x + 2)   - 2 y       x
(%o1)        --------- + --------------- - ---------
                    19             20             20
             (y + x)        (y + x)        (y + x)

(%i2) xthru (%);
                                 20
                          (x + 2)   - y
(%o2)                     -------------
                                   20
                            (y + x)
```

