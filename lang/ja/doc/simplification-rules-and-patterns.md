## Rules and Patterns

<!-- category: Simplification -->
<!-- keywords: apply1 -->
<!-- signatures: apply1(expr, rule_1, ..., rule_n) -->
### Function: apply1 (expr, rule_1, ..., rule_n)

*rule_1*を *expr*に、失敗するまで繰り返し適用して、
それから同じルールを *expr*の部分式すべてに左から右へ、
部分式すべてで *rule_1*が失敗するまで繰り返し適用します。


この方法で *expr*を変換した結果を *expr_2*と呼ぶことにします。
次に、 *rule_2*を *expr_2*の最上部から始めて同じ方法で適用します。
*rule_n*が最後の部分式上で失敗する時、結果が返されます。


`maxapplydepth`は、
`apply1`と `apply2`が処理する最も深い部分式の深さです。


`applyb1`, `apply2`, `let`も参照してください。

<!-- category: Simplification -->
<!-- keywords: apply2 -->
<!-- signatures: apply2(expr, rule_1, ..., rule_n) -->
### Function: apply2 (expr, rule_1, ..., rule_n)

もし*rule_1*が与えられた部分式上で失敗したら、
*rule_2*が繰り返し適用されます、などなど。
すべてのルールが与えられた部分式上で失敗した時だけ、
ルールの全組が次の部分式に繰り返し適用されます。
もしルールの１つが成功したら、
同じ部分式が最初のルールから再処理されます。


`maxapplydepth`は、
`apply1`と`apply2`が処理する最も深い部分式の深さです。


`apply1`と`let`も参照してください。

<!-- category: Simplification -->
<!-- keywords: applyb1 -->
<!-- signatures: applyb1(expr, rule_1, ..., rule_n) -->
### Function: applyb1 (expr, rule_1, ..., rule_n)

失敗するまで、繰り返し
*expr*の最も深い部分式に
*rule_1*を適用し、
その後、
*rule_1*がトップレベルの式で失敗するまで、
同じルールを１つ高いレベル(すなわち、より大きな部分式)に適用します。
その後、*rule_2*が*rule_1*の結果に
同様に適用されます。
*rule_n*がトップレベルの式に適用された後、結果が返されます。


`applyb1`は
`apply1`に似ていますが、
トップダウンからの代わりにボトムアップから働きます。


`maxapplyheight`は
`applyb1`が、あきらめる前に届く
最大の高さです


`apply1`, `apply2`, `let`も参照してください。

<!-- category: Simplification -->
<!-- keywords: clear_rules -->
<!-- signatures: clear_rules() -->
### Function: clear_rules ()

`kill (rules)`を実行し、
足し算`+`, 掛け算`*`, べき`^`に関して
次のルール番号を1に再設定します。

<!-- category: Simplification -->
<!-- keywords: current_let_rule_package -->
<!-- signatures: current_let_rule_package -->
### Variable: current_let_rule_package

デフォルト値: `default_let_rule_package`


`current_let_rule_package`は、
もし他のルールパッケージが指定されないなら、
(`letsimp`など)`let`パッケージの関数で使われる
ルールパッケージの名前です。
 
この変数は、`let`コマンドを介して定義された任意の規格パッケージの名前を
割り当てられます。


もし
`letsimp (expr, rule_pkg_name)`のようなコールがされたら、
ルールパッケージ`rule_pkg_name`は
その関数コールだけのために使われ、
`current_let_rule_package`の値は変わりません。

<!-- category: Simplification -->
<!-- keywords: default_let_rule_package -->
<!-- signatures: default_let_rule_package -->
### Variable: default_let_rule_package

デフォルト値: `default_let_rule_package`



`default_let_rule_package`は、
`let`でユーザーによって、
また、`current_let_rule_package`の値を変更することによって、
陽に設定されない時使われる
ルールルールの名前です。

<!-- category: Simplification -->
<!-- keywords: defmatch -->
<!-- signatures: defmatch(progname, pattern, x_1, ..., x_n), defmatch(progname, pattern) -->
### Function: defmatch (progname, pattern, x_1, ..., x_n)

*pattern*にマッチするか見るために *expr*をテストする
関数`progname(expr, x_1, ..., x_n)`
を定義します。


*pattern*は、
 (引数として与えられているなら)
パターン引数 *x_1*, ..., *x_n*を含む式です。
パターン引数は `defmatch`の引数として明示的に与えます。
一方、`matchdeclare`関数がパターン変数を宣言します。
`matchdeclare`のパターン変数か `defmatch`のパターン引数として宣言されていない
任意の変数はそれ自身とのみマッチします。


生成関数*progname*の最初の引数はパターンに対してマッチされる式であり、
他の引数は、パターンの中のダミー変数*x_1*, ..., *x_n*に対応する
実際の引数です。


もしマッチが成功したなら、
*progname*は、
左辺がパターン引数やパターン変数で、右辺がパターン引数や変数がマッチした部分式の
等式のリストを返します。
パターン変数はそれらがマッチした部分式に割り当てられますが、
パターン引数には割り当てられません。
もしマッチが失敗したら、
*progname*は `false`を返します。


リテラルパターン(すなわち、パターン引数もパターン変数も含まないパターン)は、
もしマッチが成功したら、
`true`を返します。


`matchdeclare`, `defrule`, `tellsimp`, `tellsimpafter`も
参照してください。


例:


`a`と`b`は`x`を含まず、
`a`が非ゼロであるような
形式`a*x + b`かどうか見るために
`expr`をテストする
関数`linearp(expr, x)`を定義します。
パターン引数`x`が`defmatch`に与えられているので、
このマッチ関数は、
任意の変数に関する線形式にマッチします。













```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b,
                    freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b, x);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2, z);
                         2
(%o3)              [b = y , a = y + 4, x = z]
(%i4) a;
(%o4)                         y + 4
(%i5) b;
                                2
(%o5)                          y
(%i6) x;
(%o6)                           x
```


`a`と`b`は`x`を含まず、
`a`が非ゼロであるような
形式`a*x + b`かどうか見るために
`expr`をテストする
関数`linearp(expr, x)`を定義します。
`defmatch`にパターン引数が与えられていないので、
このマッチ関数は、
他の任意の変数ではなく変数`x`に関する線形式にマッチします。










```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b,
                    freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2);
(%o3)                         false
(%i4) linearp (3*x + (y + 1)*x + y^2);
                             2
(%o4)                  [b = y , a = y + 4]
```


定積分かどうか見るために
`expr`をテストする
関数`checklimits(expr)`を定義します。














```maxima
(%i1) matchdeclare ([a, f], true);
(%o1)                         done
(%i2) constinterval (l, h) := constantp (h - l);
(%o2)        constinterval(l, h) := constantp(h - l)
(%i3) matchdeclare (b, constinterval (a));
(%o3)                         done
(%i4) matchdeclare (x, atom);
(%o4)                         done
(%i5) simp : false;
(%o5)                         false
(%i6) defmatch (checklimits, 'integrate (f, x, a, b));
(%o6)                      checklimits
(%i7) simp : true;
(%o7)                         true
(%i8) 'integrate (sin(t), t, %pi + x, 2*%pi + x);

                       x + 2 %pi
                      /
                      [
(%o8)                 I          sin(t) dt
                      ]
                      /
                       x + %pi

(%i9) checklimits (%);
(%o9)    [b = x + 2 %pi, a = x + %pi, x = t, f = sin(t)]
```

<!-- category: Simplification -->
<!-- keywords: defrule -->
<!-- signatures: defrule(rulename, pattern, replacement) -->
### Function: defrule (rulename, pattern, replacement)

与えられたパターンに関する置き換えルールを定義し、名付けます。
もし*rulename*と名付けられたルールが
(`apply1`, `applyb1`, `apply2`によって)
式に適用されるなら、
パターンにマッチするすべての部分式はreplacementで置き換えられます。
パターンマッチが値を割り当てるreplacementの中の変数すべては
その後整理される置き換えの中のそれらの値を割り当てられます。


ルールそれ自身は、
パターンマッチと置き換えの１演算で式を変換する
関数として扱うことができます。
マッチが失敗したら、ルール関数は`false`を返します。

<!-- category: Simplification -->
<!-- keywords: disprule -->
<!-- signatures: disprule(rulename_1, ..., rulename_2), disprule(all) -->
### Function: disprule (rulename_1, ..., rulename_2)

`defrule`, `tellsimp`, `tellsimpafter`が返すような、または
`defmatch`が定義するパターンのような、
名前*rulename_1*, ..., *rulename_n*を持つルールを
表示します。
ルールそれぞれは中間式ラベル(`%t`)と一緒に表示されます。


`disprule (all)`は、ルールすべてを表示します。


`disprule`は引数をクォートします。
`disprule`は、
表示されたルールに対応する中間式ラベルのリストを返します。


`let`が定義したルールを表示する
`letrules`も参照してください。


例:










```maxima
(%i1) tellsimpafter (foo (x, y), bar (x) + baz (y));
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (x + y, special_add (x, y));
(%o2)                   [+rule1, simplus]
(%i3) defmatch (quux, mumble (x));
(%o3)                         quux
(%i4) disprule (foorule1, "+rule1", quux);
(%t4)        foorule1 : foo(x, y) -> baz(y) + bar(x)

(%t5)          +rule1 : y + x -> special_add(x, y)

(%t6)                quux : mumble(x) -> []

(%o6)                    [%t4, %t5, %t6]
(%i6) ''%;
(%o6) [foorule1 : foo(x, y) -> baz(y) + bar(x), 
     +rule1 : y + x -> special_add(x, y), quux : mumble(x) -> []]
```

<!-- category: Simplification -->
<!-- keywords: let -->
<!-- signatures: let(prod, repl, predname, arg_1, ..., arg_n), let([prod, repl, predname, arg_1, ..., arg_n], package_name) -->
### Function: let (prod, repl, predname, arg_1, ..., arg_n)

*prod*は*repl*で置き換えられるような
`letsimp`のための代入ルールを定義します。
*prod*は、以下の項の正または負のべきの積です:



- *
`letsimp`をコールする以前に`matchdeclare`関数が
述語論理をアトムと関連づけるために使われないなら、
`letsimp`が文字通りに検索するアトム。
この場合、`letsimp`はアトムを述語論理を満たす積の任意の項にマッチさせます。
- *
`sin(x)`, `n!`, `f(x,y)`などのようなカーネル。
上のアトムと同様に、
述語論理をカーネルの引数に関連づけるために
`matchdeclare`が使われないなら
`letsimp`は文字通りのマッチを検索します。


正のべきの項は、少なくともそのべきを持つ項だけにマッチするでしょう。
一方、負のべきの項は、少なくとも負としてのべきをもつ項だけにマッチするでしょう。
*prod*の中の負のべきの場合、
スイッチ`letrat`を`true`に設定しなければいけません。
`letrat`も参照してください。


もし述語論理が
引数のリストが続く`let`関数に含まれるなら、
*arg_i’*が*arg_i*にマッチした値である場合、
`predname (arg_1', ..., arg_n')`が`true`に評価される時だけ
試験的なマッチ(すなわち、述語論理が省略されたなら受け入れられるもの)
が受け入れられます。
*arg_i*は、任意のアトム名や
*prod*の中に現れる任意の核の引数を取り得ます。
*repl*は、任意の有理式を取り得ます。

もし
任意のアトムや*prod*からの引数が*repl*の中に現れるなら、
適切な代入が行われます。



グローバルフラグ`letrat`は、
`letsimp`による商の整理を制御します。
`letrat`が`false`の時、
`letsimp`は、
*expr*の分子と分母をそれぞれ整理し、章を整理はしません。
`n!/n`のような代入は`(n-1)!`に進み失敗します。
`letrat`が`true`の時、
分子、分母、商がその順番で整理されます。


これらの代入関数は、同時にいくつかのルールパッケージを使うことを許します。
ルールパッケージそれぞれは、
任意の数の`let`ルールを含むことができ、ユーザー定義名で参照されます。
コマンド`let ([prod, repl, predname, arg_1, ..., arg_n], package_name)`は、
ルール*predname*をルールパッケージ*package_name*に加えます。
コマンド`letsimp (expr, package_name)` は、
*package_name*の中でルールを適用します。
`letsimp (expr, package_name1, package_name2, ...)`は、
`letsimp (%, package_name2)`, ...が続く
`letsimp (expr, package_name1)`と同値です。


`current_let_rule_package`は、
現在使われているルールパッケージの名前です。
この変数は、
`let`コマンドを介して定義された任意のルールパッケージの名前に割れ当てられます。
`let`パッケージを構成する関数のいずれかがパッケージ名なしでコールされた時はいつでも
`current_let_rule_package`が指定したパッケージが使われます。
もし
`letsimp (expr, rule_pkg_name)`のようなコールがされたら、
ルールパッケージ*rule_pkg_name*は、
その`letsimp`コマンドだけで使われ、
`current_let_rule_package`は変わりません。
もし他に指定されないなら、
`current_let_rule_package`は`default_let_rule_package`をデフォルト値とします。



```maxima
(%i1) matchdeclare ([a, a1, a2], true)$
(%i2) oneless (x, y) := is (x = y-1)$
(%i3) let (a1*a2!, a1!, oneless, a2, a1);
(%o3)         a1 a2! --> a1! where oneless(a2, a1)
(%i4) letrat: true$
(%i5) let (a1!/a1, (a1-1)!);
                        a1!
(%o5)                   --- --> (a1 - 1)!
                        a1
(%i6) letsimp (n*m!*(n-1)!/m);
(%o6)                      (m - 1)! n!
(%i7) let (sin(a)^2, 1 - cos(a)^2);
                        2               2
(%o7)                sin (a) --> 1 - cos (a)
(%i8) letsimp (sin(x)^4);
                        4           2
(%o8)                cos (x) - 2 cos (x) + 1
```

<!-- category: Simplification -->
<!-- keywords: let_rule_packages -->
<!-- signatures: let_rule_packages -->
### Variable: let_rule_packages

デフォルト値: `[default_let_rule_package]`


`let_rule_packages`は、
デフォルトパッケージ`default_let_rule_package`に加える
ユーザー定義のletルールパッケージすべてのリストです。

<!-- category: Simplification -->
<!-- keywords: letrat -->
<!-- signatures: letrat -->
### Variable: letrat

デフォルト値: `false`


`letrat`が`false`の時、
`letsimp`は
比の分子と分母それぞれを整理し、
商を整理しません。


`letrat`が`true`の時、
分子、分母、商はその順番に整理されます。



```maxima
(%i1) matchdeclare (n, true)$
(%i2) let (n!/n, (n-1)!);
                         n!
(%o2)                    -- --> (n - 1)!
                         n
(%i3) letrat: false$
(%i4) letsimp (a!/a);
                               a!
(%o4)                          --
                               a
(%i5) letrat: true$
(%i6) letsimp (a!/a);
(%o6)                       (a - 1)!
```

<!-- category: Simplification -->
<!-- keywords: letrules -->
<!-- signatures: letrules(), letrules(package_name) -->
### Function: letrules ()

ルールパッケージのルールを表示します。
`letrules ()`は現在のルールパッケージのルールを表示します。
`letrules (package_name)`は
*package_name*のルールを表示します。


現在のルールパッケージは
`current_let_rule_package`によって指名されます。
もし他に指定されないなら、
`current_let_rule_package`は`default_let_rule_package`がデフォルト値になります。


`disprule`も参照してください
それは、
`tellsimp`と`tellsimpafter`が定義するルールを表示します。

<!-- category: Simplification -->
<!-- keywords: letsimp -->
<!-- signatures: letsimp(expr), letsimp(expr, package_name), letsimp(expr, package_name_1, ..., package_name_n) -->
### Function: letsimp (expr)

*expr*に変化がなくなるまで
繰り返し、`let`が定義する代入ルールを適用します。


`letsimp (expr)`は
`current_let_rule_package`からルールを使います。


`letsimp (expr, package_name)`は、
`current_let_rule_package`を変えることなしに
*package_name*からルールを使います。


`letsimp (expr, package_name_1, ..., package_name_n)`は、
quivalent to 
`letsimp (%, package_name_2)`などが続く
`letsimp (expr, package_name_1`と同値です。

<!-- category: Simplification -->
<!-- keywords: matchdeclare -->
<!-- signatures: matchdeclare(a_1, pred_1, ..., a_n, pred_n) -->
### Function: matchdeclare (a_1, pred_1, ..., a_n, pred_n)

述語論理 *pred_k*を変数 *a_k*の変数やリストに関連づけます。
なので、 *a_k*は述語論理が `false`以外の何かを返す式にマッチします。


述語論理は関数の名前、ラムダ式、関数コール、最後の引数のないラムダコール、
`true`または `all`です。
任意の式が `true`や `all`にマッチします。
もし述語論理が関数コールかラムダコールとして指定されるなら、
テストされる式が引数のリストに追加されます;
マッチが評価される時引数が評価されます。
そうでないなら、述語論理は関数名またはラムダ式として指定され、
テストされる式が唯一の引数です。
`matchdeclare`がコールされた時、述語論理関数は定義されている必要はありません;
述語論理はマッチが試みられるまで評価されません。


述語論理は、
`true`か `false`はもちろん、ブーリアン式を返すかもしれません。
ブーリアン式は、構成されたルール関数内で `is`によって評価されるので、
述語論理内部で `is`をコールする必要はありません。


もし式がマッチ述語論理を満たすなら、
マッチ変数が式に割り当てられます。
例外は足し算 `+`や掛け算 `*`のオペランドのマッチ変数です。
足し算と掛け算だけは特別に扱われます;
他のn項演算子(組み込みもユーザー定義も)は通常の関数のように扱われます。



足し算と掛け算の場合、
マッチ変数はマッチ述語論理を満たす唯一の式か、
そんな式の(それぞれ)和または積に割り当てられます。
そんな多項マッチングはどん欲(greedy)です:
述語論理群はそれらの関連変数がマッチパターンの中で現れる順に評価され、
複数の述語論理を満たす項は、それが満たす最初の述語論理によってマッチされます。
述語論理それぞれは、
次の述語論理が評価される前に
和や積のオペランドすべてに対してテストされます。
加えて、
もし(それぞれ)0か1がマッチ述語論理を満たし、かつ、
述語論理を満たす他の項がないなら、
0か1が述語論理の関連マッチ変数に割り当てられます。


足し算と掛け算パターンを処理するアルゴリズムは、
(例えば、「任意のものにマッチする」変数が現れるパターンのように)
マッチパターンの中やマッチされる式の中の項の順序付けに依存したいくつかのマッチ結果をもたらします。
しかしながら、もしマッチ述語論理すべてが相互に排他的なら、
１つのマッチ述語論理はべつのものがマッチした項を受け入れられないので、
マッチ結果は順序付けに影響されません。


変数 *a*を引数として `matchdeclare`をコールすると、
もし既に宣言されているなら、
*a*に関する `matchdeclare`プロパティが変わります:
ルールが定義された時、直近の `matchdeclare`だけが効果を持ちます。
(`matchdeclare`か `remove`を介した)
`matchdeclare`プロパティへの後の変更は、存在するルールに影響しません。


`propvars (matchdeclare)`は
`matchdeclare`プロパティを持つ変数すべてのリストを返します。
`printprops (a, matchdeclare)`は、
変数 `a`に関する述語論理を返します。
`printprops (all, matchdeclare)`は、
すべての `matchdeclare`変数に関する述語論理のリストを返します。
`remove (a, matchdeclare)`は、
*a*から `matchdeclare`プロパティを削除します。


関数 `defmatch`, `defrule`, `tellsimp`, `tellsimpafter`, `let`は、パターンに対して式をテストするルールを構成します。


`matchdeclare`は引数をクォートします。
`matchdeclare`はいつも `done`を返します。


例:


述語論理は、関数名か、ラムダ式か、最後の引数がない関数コールかラムダコールか、
`true`か `all`です。











```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) matchdeclare (bb, lambda ([x], x > 0));
(%o2)                         done
(%i3) matchdeclare (cc, freeof (%e, %pi, %i));
(%o3)                         done
(%i4) matchdeclare (dd, lambda ([x, y], gcd (x, y) = 1) (1728));
(%o4)                         done
(%i5) matchdeclare (ee, true);
(%o5)                         done
(%i6) matchdeclare (ff, all);
(%o6)                         done
```


もし式がマッチ述語論理を満たすなら、
マッチ変数は式に割り当てられます。








```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) defrule (r1, bb^aa, ["integer" = aa, "atom" = bb]);
                    aa
(%o2)        r1 : bb   -> [integer = aa, atom = bb]
(%i3) r1 (%pi^8);
(%o3)               [integer = 8, atom = %pi]
```


足し算と掛け算の場合、
マッチ変数は、マッチ述語論理を満たす１つの式か、
そんな式の(それぞれ)和か積に割り当てられるかもしれません。












```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + sin(x));
(%o3)     [all atoms = 8, all nonatoms = sin(x) + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * sin(x));
(%o5)    [all atoms = 8, all nonatoms = (b + a) sin(x)]
```


`+`と `*`の引数をマッチする時、
もしマッチ述語論理すべてが相互に排他的なら、
１つのマッチ述語論理は別のものがマッチした項を受け入れられないので、
マッチ結果は順序付けに影響されません。












```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + %pi + sin(x) - c + 2^n);
                                                     n
(%o3) [all atoms = %pi + 8, all nonatoms = sin(x) + 2  - c + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * %pi * sin(x) / c * 2^n);
                                                  n
                                         (b + a) 2  sin(x)
(%o5) [all atoms = 8 %pi, all nonatoms = -----------------]
                                                 c
```


関数 `propvars`と `printprops`はマッチ変数についての情報を返します。











```maxima
(%i1) matchdeclare ([aa, bb, cc], atom, [dd, ee], integerp);
(%o1)                         done
(%i2) matchdeclare (ff, floatnump, gg, lambda ([x], x > 100));
(%o2)                         done
(%i3) propvars (matchdeclare);
(%o3)             [aa, bb, cc, dd, ee, ff, gg]
(%i4) printprops (ee, matchdeclare);
(%o4)                    [integerp(ee)]
(%i5) printprops (gg, matchdeclare);
(%o5)              [lambda([x], x > 100, gg)]
(%i6) printprops (all, matchdeclare);
(%o6) [lambda([x], x > 100, gg), floatnump(ff), integerp(ee), 
                      integerp(dd), atom(cc), atom(bb), atom(aa)]
```

<!-- category: Simplification -->
<!-- keywords: maxapplydepth -->
<!-- signatures: maxapplydepth -->
### Variable: maxapplydepth

デフォルト値: 10000


`maxapplydepth`は
`apply1`と `apply2`が探索する
最大深さです。

<!-- category: Simplification -->
<!-- keywords: maxapplyheight -->
<!-- signatures: maxapplyheight -->
### Variable: maxapplyheight

デフォルト値: 10000


`maxapplyheight`は
`applyb1`があきらめる前に到達する
最大高さです。

<!-- category: Simplification -->
<!-- keywords: remlet -->
<!-- signatures: remlet(prod, name), remlet(), remlet(all), remlet(all, name) -->
### Function: remlet (prod, name)

`let`関数で直近に定義された
代入ルール*prod* –> replを削除します。
もし名前が供給されるなら、ルールはルールパッケージ名から削除されます。


`remlet()`や`remlet(all)`は
現在のルールパッケージから代入ルールすべてを削除します。
もし例えば、`remlet (all, name)`にように、ルールパッケージ名が供給されるなら、
ルールパッケージ*name*も削除されます。


もし代入が同じ積を使って変更されるなら、
`remlet`はコールされる必要はなく、
`let`関数と新しい置き換え　かつ/または述語論理名で、文字通りに同じ積を使って代入を再定義だけです。
さて、`remlet (prod)`がコールされると、
元の代入ルールが生き返ります。


`remrule`も参照してください。
`tellsimp`や`tellsimpafter`で定義されたルールを削除します。

<!-- category: Simplification -->
<!-- keywords: remrule -->
<!-- signatures: remrule(op, rulename), remrule(op, all) -->
### Function: remrule (op, rulename)

`tellsimp`や`tellsimpafter`で定義されたルールを削除します。


`remrule (op, rulename)`は、
演算子*op*から
名前*rulename*を持つ
ルールを削除します。
*op*が組み込みか
(`infix`, `prefix`, などで定義されたような)ユーザー定義演算子の時、
*op*と*rulename*はダブルクォートマークでくくられないといけません。


`remrule (op, all)`は
演算子*op*に関するルールすべてを削除します。


`remlet`も参照してください。
`let`で定義されたルールを削除します。


例:



















```maxima
(%i1) tellsimp (foo (aa, bb), bb - aa);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (aa + bb, special_add (aa, bb));
(%o2)                   [+rule1, simplus]
(%i3) infix ("@@");
(%o3)                          @@
(%i4) tellsimp (aa @@ bb, bb/aa);
(%o4)                   [@@rule1, false]
(%i5) tellsimpafter (quux (%pi, %e), %pi - %e);
(%o5)                  [quuxrule1, false]
(%i6) tellsimpafter (quux (%e, %pi), %pi + %e);
(%o6)             [quuxrule2, quuxrule1, false]
(%i7) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
       quux (%e, %pi)];
                                     bb
(%o7) [bb - aa, special_add(aa, bb), --, %pi - %e, %pi + %e]
                                     aa
(%i8) remrule (foo, foorule1);
(%o8)                          foo
(%i9) remrule ("+", ?\+rule1);
(%o9)                           +
(%i10) remrule ("@@", ?\@\@rule1);
(%o10)                         @@
(%i11) remrule (quux, all);
(%o11)                        quux
(%i12) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
        quux (%e, %pi)];
(%o12) [foo(aa, bb), bb + aa, aa @@ bb, quux(%pi, %e), 
                                         quux(%e, %pi)]
```

<!-- category: Simplification -->
<!-- keywords: tellsimp -->
<!-- signatures: tellsimp(pattern, replacement) -->
### Function: tellsimp (pattern, replacement)

`tellsimpafter`に似ていますが、
古いものの前に新しい情報を置くので、
組み込み整理ルールの前に適用されます。


整理器が働く前に式を変更することが重要な時
例えば、整理器が式について何か「知っている」が、それが返すものが好みでないなら、
`tellsimp`が使われます。
もし整理器が式の主演算子について何かを「知っている」が、単に十分でないなら、
たぶん`tellsimpafter`を使いたいでしょう。


パターンは和、積、変数１つ、または、数は取れません。


システム変数`rules`は、
`defrule`, `defmatch`, `tellsimp`, `tellsimpafter`で
定義されたルールのリストです。


例:



```maxima
(%i1) matchdeclare (x, freeof (%i));
(%o1)                         done
(%i2) %iargs: false$
(%i3) tellsimp (sin(%i*x), %i*sinh(x));
(%o3)                 [sinrule1, simp-%sin]
(%i4) trigexpand (sin (%i*y + x));
(%o4)         sin(x) cos(%i y) + %i cos(x) sinh(y)
(%i5) %iargs:true$
(%i6) errcatch(0^0);
 0
0  has been generated
(%o6)                          []
(%i7) ev (tellsimp (0^0, 1), simp: false);
(%o7)                  [^rule1, simpexpt]
(%i8) 0^0;
(%o8)                           1
(%i9) remrule ("^", %th(2)[1]);
(%o9)                           ^
(%i10) tellsimp (sin(x)^2, 1 - cos(x)^2);
(%o10)                 [^rule2, simpexpt]
(%i11) (1 + sin(x))^2;
                                      2
(%o11)                    (sin(x) + 1)
(%i12) expand (%);
                                   2
(%o12)               2 sin(x) - cos (x) + 2
(%i13) sin(x)^2;
                                  2
(%o13)                     1 - cos (x)
(%i14) kill (rules);
(%o14)                        done
(%i15) matchdeclare (a, true);
(%o15)                        done
(%i16) tellsimp (sin(a)^2, 1 - cos(a)^2);
(%o16)                 [^rule3, simpexpt]
(%i17) sin(y)^2;
                                  2
(%o17)                     1 - cos (y)
```

<!-- category: Simplification -->
<!-- keywords: tellsimpafter -->
<!-- signatures: tellsimpafter(pattern, replacement) -->
### Function: tellsimpafter (pattern, replacement)

組み込み整理ルールの後、適Maxima整理器が適用する
整理ルールを定義します。
*pattern*は
(`matchdeclare`で宣言された)
パターン変数や他のアトムや演算子から成る、
パターンマッチングの目的でリテラルと考えられる式です。
*replacement*は、
*pattern*にマッチする実際の式に代入されます;
*replacement*の中のパターン変数は
実際の式の中でマッチした値に割り当てられます。


*pattern*は、
主演算子がパターン変数でない任意の非アトム式を取り得ます;
整理ルールは主演算子に関連付けられます。
(以下で記述する１つの例外がありますが、)関数、リスト、配列の名前が、
(パターン変数でなく)ただリテラルとして、
主演算子として*pattern*の中で現れることができます;
これは、
パターンとして
もし`aa`や`bb`がパターン変数なら
`aa(x)`や`bb[y]`のような式を除外します。
パターン変数である関数、リスト、配列の名前は、
*pattern*の中で、主演算子以外の演算子として現れることができます。


上の関数名に関するルールに１つ例外があります。
`aa[x](y)`のような式の中の添字付き関数の名前は
主演算子が`aa`でなくLispアトム`mqapply`だから、
パターン変数にできます。
これは、添字付き関数を含む式の表現の結果です。










(もしクォートやフラグ`noeval`を通して抑制されないなら)
整理ルールは、
評価の後、適用されます。
`tellsimpafter`で確立されたルールは、
組み込みルールの後、それらが定義された順に適用されます。
ルールはボトムアップに適用されます。すなわち、
式全体への適用の前に、最初、部分式に適用されます。


ルールすべてが適用されることを保証するために、
(例えば、クォートクォート演算子`''`やフラグ`infeval`を介して)
結果を繰り返し整理する必要があるかもしれません。


パターン変数は、整理ルールの中でローカル変数として扱われます。
一旦ルールが定義されると、パターン変数の値は、
ルールに影響せず、ルールによって影響されません。
成功したルールマッチの結果となるパターン変数への割り当ては、
パターン変数の現在の割り当て(またはその欠落)に影響しません。
しかしながら、Maximaの中のアトムすべてで、
(`put`や関連関数で定義された)パターン変数のプロパティはグローバルです。


`tellsimpafter`によって構成されたルールは、
*pattern*の主演算子に由来します。
組み込み演算子や
`infix`, `prefix`, `postfix`, `matchfix`, `nofix`で
定義されたユーザー定義演算子に関するルールは、
Lisp識別子である名前を持ちます。


他の関数に関するルールは、Maxima識別子である名前を持ちます。




名詞と動詞形の扱いは少し混乱しています。

もしルールが名詞(または動詞)形に関して定義されて、
対応する動詞(または名詞)形に関するルールが既に存在しているなら、
新しく定義されたルールは両方の形式(名詞と動詞)に適用されます。
もし対応する動詞(名詞)形に関するルールが存在しないなら、
新しく定義されたルールは名詞(または動詞)形にだけ適用されます。


`tellsimpafter`で構成されたルールは通常のLisp関数です。
もしルール名が`$foorule1`なら、
構成子`:lisp (trace $foorule1)`は関数をトレースし、
`:lisp (symbol-function '$foorule1)`は定義を表示します。


`tellsimpafter`は引数をクォートします。
`tellsimpafter`は
新しく確立されたルールを含む、
*pattern*の主演算子に関する
ルールのリストを返します。



`matchdeclare`, `defmatch`, `defrule`, `tellsimp`, `let`, `kill`, `remrule`, `clear_rules`も参照してください。


例:


*pattern*は、
主演算子がパターン変数でない任意の非アトム式を取り得ます。












```maxima
(%i1) matchdeclare (aa, atom, [ll, mm], listp, xx, true)$
(%i2) tellsimpafter (sin (ll), map (sin, ll));
(%o2)                 [sinrule1, simp-%sin]
(%i3) sin ([1/6, 1/4, 1/3, 1/2, 1]*%pi);
                    1  sqrt(2)  sqrt(3)
(%o3)              [-, -------, -------, 1, 0]
                    2     2        2
(%i4) tellsimpafter (ll^mm, map ("^", ll, mm));
(%o4)                  [^rule1, simpexpt]
(%i5) [a, b, c]^[1, 2, 3];
                                2   3
(%o5)                      [a, b , c ]
(%i6) tellsimpafter (foo (aa (xx)), aa (foo (xx)));
(%o6)                   [foorule1, false]
(%i7) foo (bar (u - v));
(%o7)                    bar(foo(u - v))
```


ルールはそれらが定義された順に適用されます。
もし２つのルールが式にマッチできるなら、
最初に定義されたルールが適用されます。









```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) tellsimpafter (foo (aa), bar_1 (aa));
(%o2)                   [foorule1, false]
(%i3) tellsimpafter (foo (aa), bar_2 (aa));
(%o3)              [foorule2, foorule1, false]
(%i4) foo (42);
(%o4)                       bar_1(42)
```


整理ルールの中で、パターン変数はローカル変数として扱われます。
(`defmatch`と比較してください。
パターン変数をグローバル変数として扱います。)










```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) bb: 12345;
(%o3)                         12345
(%i4) foo (42, %e);
(%o4)                 bar(aa = 42, bb = %e)
(%i5) bb;
(%o5)                         12345
```


アトムすべてには、
パターン変数のプロパティは、たとえ値がローカルでも、
グローバルです。
この例では、割り当てプロパティは
`define_variable`を介して宣言されます。
Maximaの至る所で、これはアトム`bb`のプロパティです。










```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) foo (42, %e);
(%o3)                 bar(aa = 42, bb = %e)
(%i4) define_variable (bb, true, boolean);
(%o4)                         true
(%i5) foo (42, %e);
Error: bb was declared mode boolean, has value: %e
 -- an error.  Quitting.  To debug this try debugmode(true);
```


ルールは主演算子に由来します。
組み込みやユーザー定義の演算子に関するルール名はLisp識別子で、
一方、他の関数に関する名前はMaxima識別子です。

















```maxima
(%i1) tellsimpafter (foo (%pi + %e), 3*%pi);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (foo (%pi * %e), 17*%e);
(%o2)              [foorule2, foorule1, false]
(%i3) tellsimpafter (foo (%i ^ %e), -42*%i);
(%o3)         [foorule3, foorule2, foorule1, false]
(%i4) tellsimpafter (foo (9) + foo (13), quux (22));
(%o4)                   [+rule1, simplus]
(%i5) tellsimpafter (foo (9) * foo (13), blurf (22));
(%o5)                  [*rule1, simptimes]
(%i6) tellsimpafter (foo (9) ^ foo (13), mumble (22));
(%o6)                  [^rule1, simpexpt]
(%i7) rules;
(%o7) [foorule1, foorule2, foorule3, +rule1, *rule1, ^rule1]
(%i8) foorule_name: first (%o1);
(%o8)                       foorule1
(%i9) plusrule_name: first (%o4);
(%o9)                        +rule1
(%i10) remrule (foo, foorule1);
(%o10)                         foo
(%i11) remrule ("^", ?\^rule1);
(%o11)                          ^
(%i12) rules;
(%o12)        [foorule2, foorule3, +rule1, *rule1]
```


加工された例: 反可換乗算。












```maxima
(%i1) gt (i, j) := integerp(j) and i < j;
(%o1)           gt(i, j) := integerp(j) and i < j
(%i2) matchdeclare (i, integerp, j, gt(i));
(%o2)                         done
(%i3) tellsimpafter (s[i]^^2, 1);
(%o3)                 [^^rule1, simpncexpt]
(%i4) tellsimpafter (s[i] . s[j], -s[j] . s[i]);
(%o4)                   [.rule1, simpnct]
(%i5) s[1] . (s[1] + s[2]);
(%o5)                    s  . (s  + s )
                          1     2    1
(%i6) expand (%);
(%o6)                      1 - s  . s
                                2    1
(%i7) factor (expand (sum (s[i], i, 0, 9)^^5));
(%o7) 100 (s  + s  + s  + s  + s  + s  + s  + s  + s  + s )
            9    8    7    6    5    4    3    2    1    0
```

