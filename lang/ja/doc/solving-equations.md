## Equations

<!-- category: Solving -->
<!-- keywords: %rnum_list -->
<!-- signatures: %rnum_list -->
### Variable: %rnum_list

デフォルト値: `[]`


`%rnum_list`は、
`solve`や`algsys`による解で導入された
変数のリストです。
`%r`変数は、それらが生成された順に
`%rnum_list`に追加されます。
これは、あとで解への代入を行うのに便利です。

`concat ('%r, j)`をするよりこのリストを使うことを推奨します。












```maxima
(%i1) solve ([x + y = 3], [x,y]);
(%o1)              [[x = 3 - %r1, y = %r1]]


(%i2) %rnum_list;
(%o2)                       [%r1]


(%i3) sol : solve ([x + 2*y + 3*z = 4], [x,y,z]);
(%o3)   [[x = - 2 %r3 - 3 %r2 + 4, y = %r3, z = %r2]]


(%i4) %rnum_list;
(%o4)                     [%r2, %r3]


(%i5) for i : 1 thru length (%rnum_list) do
        sol : subst (t[i], %rnum_list[i], sol)$


(%i6) sol;
(%o6)     [[x = - 2 t  - 3 t  + 4, y = t , z = t ]]
                     2      1           2       1
```

See also: `solve`, `algsys`.

<!-- category: Solving -->
<!-- keywords: algepsilon -->
<!-- signatures: algepsilon -->
### Variable: algepsilon

デフォルト値: 10^8



`algsys`が
`algepsilon`を使います。

See also: `algepsilon`.

<!-- category: Solving -->
<!-- keywords: algexact -->
<!-- signatures: algexact -->
### Variable: algexact

デフォルト値: `false`


`algexact`は、以下のように`algsys`の振る舞いに影響を与えます:


もし`algexact`が`true`なら、
`algsys`はいつも`solve`をコールし、
`solve`の失敗時には`realroots`を使います。


もし`algexact`が`false`なら、
問題が１変数でないときだけ、
もしくは、方程式が二次もしくは四次なら
`solve`がコールされます。


このように、`algexact: true`は、
厳密解だけを保証せず、ただ、
`algsys`は最初に厳密解を与えるように最大限努力して、
他のすべてが失敗した時近似をもたらすことだけを保証します。

See also: `algsys`, `solve`, `realroots`.

<!-- category: Solving -->
<!-- keywords: algsys -->
<!-- signatures: algsys([expr_1, ..., expr_m], [x_1, ..., x_n]), algsys([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: algsys ([expr_1, ..., expr_m], [x_1, ..., x_n])

同時多項式*expr_1*, ..., *expr_m*
または多項式方程式*eqn_1*, ..., *eqn_m*
を変数*x_1*, ..., *x_n*について解きます。
式*expr*は、等式`expr = 0`と同値です。
変数より等式が多い場合も逆もあります。


`algsys`は、解のリストを返します。
ここで、それぞれの解は、
方程式系を満たす変数*x_1*, ..., *x_n*の値を指定する等式のリストとして
与えられます。
もし`algsys`が解を見つけられなければ、
空のリスト`[]`が返されます。


シンボル`%r1`, `%r2`, ...,
が、解の任意パラメータを表すために、必要に応じて導入されます;
これらの変数は、リスト `%rnum_list`にも追加されます。


方法は以下の通りです:



1. 最初に、方程式は因数分解され、サブシステムに分割されます。
2. それぞれのサブシステム*S_i*に関して、等式*E*と変数*x*が選択されます。
変数はゼロでない最低次を持つよう選ばれます。
そして、
*x*に関する*E*と*E_j*の終結式が
サブシステム*S_i*の中の残っている等式群*E_j*のそれぞれに関して計算されます。


これは、*x*が消去されるので、
１つ変数の少ない新しいサブシステム*S_i’*をもたらします
ここでプロセスは(1)に戻ります。
3. いつか、１つの等式から成るサブシステムが得られます。
もし等式が多変数なら、浮動小数点数の形式の近似は導入されず、
厳密解を見つけるために`solve`がコールされます。


いくつかの場合、`solve`は解を見つけることができないか、
もし見つけたら、絵が非常に大きな式になるかもしれません。



もし等式が１変数で、線形か二次か四次なら、
もし近似が導入されないなら、再び`solve`がコールされます。
もし近似が導入されるか、等式が１変数でなく、線形でも二次でも、四次でもないなら、
もしスイッチ`realonly`が`true`なら、
実数解を見つけるため関数`realroots`がコールされます。
もし`realonly`が`false`なら、
実数解と複素数解を探す`allroots`がコールされます。


もし`algsys`が
要求よりも有効数字が少ない解を生成するなら、
ユーザーは`algepsilon`の値をより高い値に変更できます。


もし`algexact`が`true`に設定されているなら、
いつも`solve`がコールされます。
4. 最終的に、ステップ(3)で得られた解は以前のレベルに代入され、解処理は(1)に戻ります。


`algsys`が（通常、初期の段階での厳密解発見の失敗による）浮動小数点近似を含む多変数方程式に出会う時、
厳密な方法をそんな方程式に適用しようとせず、かわりにメッセージを表示します:
"`algsys` cannot solve - system too complicated."


`radcan`との対話は、多きなもしくは複雑な式を生成することができます。
この場合、`pickapart`または `reveal`を使って結果の一部を分離することができるかもしれません。


時々、`radcan`は、実際には実数値の解に虚数単位`%i`を導入するかもしれません。


例:













```maxima
(%i1) e1: 2*x*(1 - a1) - 2*(x - 1)*a2;
(%o1)              2 (1 - a1) x - 2 a2 (x - 1)
(%i2) e2: a2 - a1; 
(%o2)                        a2 - a1
(%i3) e3: a1*(-y - x^2 + 1); 
                                   2
(%o3)                   a1 (- y - x  + 1)
(%i4) e4: a2*(y - (x - 1)^2);
                                       2
(%o4)                   a2 (y - (x - 1) )
(%i5) algsys ([e1, e2, e3, e4], [x, y, a1, a2]);
(%o5) [[x = 0, y = %r1, a1 = 0, a2 = 0], 

                                  [x = 1, y = 0, a1 = 1, a2 = 1]]
(%i6) e1: x^2 - y^2;
                              2    2
(%o6)                        x  - y
(%i7) e2: -1 - y + 2*y^2 - x + x^2;
                         2        2
(%o7)                 2 y  - y + x  - x - 1
(%i8) algsys ([e1, e2], [x, y]);
                 1            1
(%o8) [[x = - -------, y = -------], 
              sqrt(3)      sqrt(3)

        1              1             1        1
[x = -------, y = - -------], [x = - -, y = - -], [x = 1, y = 1]]
     sqrt(3)        sqrt(3)          3        3
```

See also: `%rnum_list`, `solve`, `realonly`, `realroots`, `allroots`, `algepsilon`, `radcan`, `pickapart`, `reveal`.

<!-- category: Solving -->
<!-- keywords: allroots -->
<!-- signatures: allroots(expr), allroots(eqn) -->
### Function: allroots (expr)

1変数多項式*expr*もしくは1変数多項式方程式*eqn*の実数と複素数の根の数値近似を
計算する。


フラグ`polyfactor`が`true`の時、
`allroots`は、多項式が実数なら多項式を実数上で因数分解し、
多項式が複素数なら複素数上で因数分解します。


`allroots`は、多重根の場合、不正確な結果をもたらすことがあります。
もし多項式が実数なら、`allroots (%i*p)`は、
`allroots (p)`より精確な近似を生成します。
`allroots`はこの場合異なるアルゴリズムを呼ぶので。


`allroots`は非多項式を却下します。
`rat`された分子が多項式であることを要求し、
分母はせいぜい複素数であることを要求します。
この結果、もし`polyfactor`が`true`なら、
`allroots`はいつも（因数分解された）同値の式を返します。


複素多項式のために、JenkinsとTraubのアルゴリズムが使われます
（Algorithm 419, Comm. ACM, vol. 15, (1972), .97)。
実多項式のために、Jenkinsのアルゴリズム
(Algorithm 493, ACM TOMS, vol. 1, (1975), p.178)が使われます。


例:











```maxima
(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);
                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)
(%i2) soln: allroots (eqn);
(%o2) [x = .8296749902129361, x = - 1.015755543828121, 

x = .9659625152196369 %i - .4069597231924075, 

x = - .9659625152196369 %i - .4069597231924075, x = 1.0]
(%i3) for e in soln
        do (e2: subst (e, eqn), disp (expand (lhs(e2) - rhs(e2))));
                      - 3.5527136788005E-15

                     - 5.32907051820075E-15

         4.44089209850063E-15 %i - 4.88498130835069E-15

        - 4.44089209850063E-15 %i - 4.88498130835069E-15

                       3.5527136788005E-15

(%o3)                         done
(%i4) polyfactor: true$
(%i5) allroots (eqn);
(%o5) - 13.5 (x - 1.0) (x - .8296749902129361)

                           2
 (x + 1.015755543828121) (x  + .8139194463848151 x

 + 1.098699797110288)
```

See also: `polyfactor`.

<!-- category: Solving -->
<!-- keywords: backsubst -->
<!-- signatures: backsubst -->
### Variable: backsubst

デフォルト値: `true`




`backsubst`が`false`の時、
方程式が三角行列化された後、`linsolve`の後退代入を妨げます。
これは、後退代入が極端に大きな式の生成のもととなる非常に大きな問題に関して役立つかもしれません。



```maxima
(%i1) eq1 : x + y + z = 6$
(%i2) eq2 : x - y + z = 2$
(%i3) eq3 : x + y - z = 0$
(%i4) backsubst : false$

(%i5) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o5)             [x = z - y, y = 2, z = 3]

(%i6) backsubst : true$

(%i7) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o7)               [x = 1, y = 2, z = 3]
```

See also: `linsolve`.

<!-- category: Solving -->
<!-- keywords: bfallroots -->
<!-- signatures: bfallroots(expr), bfallroots(eqn) -->
### Function: bfallroots (expr)

１変数の多項式*expr*または多項式等式*eqn*の実数根と複素数根の数値近似
を計算します。


`bfallroots`は多倍長浮動小数点を使って根を計算する以外の
すべての点で、`bfallroots`は`allroots`と同一です。
詳しい情報については`allroots`を参照してください。

See also: `allroots`.

<!-- category: Solving -->
<!-- keywords: breakup -->
<!-- signatures: breakup -->
### Variable: breakup

デフォルト値: `true`


`breakup`が`true`の時、
`solve`は、三次と四次の方程式の解を共通部分式を使って表現します。
共通部分式は、中間式ラベル(`%t1`, `%t2`, など)に割り当てられます。
そうでなければ、共通部分式は同定されません。


`breakup: true`は、
`programmode`が`false`の時だけ、効果を持ちます。


例:



```maxima
(%i1) programmode: false$
(%i2) breakup: true$
(%i3) solve (x^3 + x^2 - 1);

                        sqrt(23)    25 1/3
(%t3)                  (--------- + --)
                        6 sqrt(3)   54
Solution:

                                      sqrt(3) %i   1
                                      ---------- - -
                sqrt(3) %i   1            2        2   1
(%t4)    x = (- ---------- - -) %t3 + -------------- - -
                    2        2            9 %t3        3

                                      sqrt(3) %i   1
                                    - ---------- - -
              sqrt(3) %i   1              2        2   1
(%t5)    x = (---------- - -) %t3 + ---------------- - -
                  2        2             9 %t3         3

                                   1     1
(%t6)                  x = %t3 + ----- - -
                                 9 %t3   3
(%o6)                    [%t4, %t5, %t6]
(%i6) breakup: false$
(%i7) solve (x^3 + x^2 - 1);
Solution:

             sqrt(3) %i   1
             ---------- - -
                 2        2        sqrt(23)    25 1/3
(%t7) x = --------------------- + (--------- + --)
             sqrt(23)    25 1/3    6 sqrt(3)   54
          9 (--------- + --)
             6 sqrt(3)   54

                                              sqrt(3) %i   1    1
                                           (- ---------- - -) - -
                                                  2        2    3

           sqrt(23)    25 1/3  sqrt(3) %i   1
(%t8) x = (--------- + --)    (---------- - -)
           6 sqrt(3)   54          2        2

                                            sqrt(3) %i   1
                                          - ---------- - -
                                                2        2      1
                                      + --------------------- - -
                                           sqrt(23)    25 1/3   3
                                        9 (--------- + --)
                                           6 sqrt(3)   54

            sqrt(23)    25 1/3             1             1
(%t9)  x = (--------- + --)    + --------------------- - -
            6 sqrt(3)   54          sqrt(23)    25 1/3   3
                                 9 (--------- + --)
                                    6 sqrt(3)   54
(%o9)                    [%t7, %t8, %t9]
```

See also: `solve`, `programmode`.

<!-- category: Solving -->
<!-- keywords: dimension -->
<!-- signatures: dimension(eqn), dimension(eqn_1, ..., eqn_n) -->
### Function: dimension (eqn)

`dimen`は、次元解析パッケージです。
`load ("dimen")`はこのパッケージをロードします。
`demo ("dimen")`は短いデモンストレーションを表示します。

<!-- category: Solving -->
<!-- keywords: dispflag -->
<!-- signatures: dispflag -->
### Variable: dispflag

デフォルト値: `true`



もし`block`内で`false`に設定されたら
`block`内でコールされた解法関数が生成する出力の表示を抑制します。
`block`をドル記号$で終端すると、
`dispflag`を`false`に設定します。

<!-- category: Solving -->
<!-- keywords: funcsolve -->
<!-- signatures: funcsolve(eqn, g(t)) -->
### Function: funcsolve (eqn, g(t))

*eqn*を満たす有理関数`g(t)`が存在するかどうかに依存して、
`[g(t) = ...]`または`[]`を返します。
ここで、*eqn*は（この場合）
`g(t)`と`g(t+1)`に関して
一次、線形多項式でなければいけません。



```maxima
(%i1) eqn: (n + 1)*f(n) - (n + 3)*f(n + 1)/(n + 1) =
      (n - 1)/(n + 2);
                            (n + 3) f(n + 1)   n - 1
(%o1)        (n + 1) f(n) - ---------------- = -----
                                 n + 1         n + 2
(%i2) funcsolve (eqn, f(n));

Dependent equations eliminated:  (4 3)
                                   n
(%o2)                f(n) = ---------------
                            (n + 1) (n + 2)
```


警告: これはとても未熟な実装です – 多くの安全性チェックや
明らかな一般化が忘れられています。

<!-- category: Solving -->
<!-- keywords: globalsolve -->
<!-- signatures: globalsolve -->
### Variable: globalsolve

デフォルト値: `false`


`globalsolve`が`true`の時、
２つ以上の線形方程式を解く時、
解くべき変数が、`linsolve`や`solve`が見つけた解の値に割り当てられます。


`globalsolve`が`false`の時、
２つ以上の線形方程式を解く時、
`linsolve`や`solve`が見つけた解は、
等式として表現され、
解くべき変数は割り当てられません。


２つ以上の線形方程式以外の何かを解く時には、
`solve`は`globalsolve`を無視します。
方程式を解く他の関数(例えば`algsys`)はいつも`globalsolve`を無視します。


例:



```maxima
(%i1) globalsolve: true$
(%i2) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t2)                        x : --
                                 7

                                   1
(%t3)                        y : - -
                                   7
(%o3)                     [[%t2, %t3]]
(%i3) x;
                               17
(%o3)                          --
                               7
(%i4) y;
                                 1
(%o4)                          - -
                                 7
(%i5) globalsolve: false$
(%i6) kill (x, y)$
(%i7) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t7)                        x = --
                                 7

                                   1
(%t8)                        y = - -
                                   7
(%o8)                     [[%t7, %t8]]
(%i8) x;
(%o8)                           x
(%i9) y;
(%o9)                           y
```

See also: `solve`, `linsolve`, `algsys`.

<!-- category: Solving -->
<!-- keywords: ieqn -->
<!-- signatures: ieqn(ie, unk, tech, n, guess) -->
### Function: ieqn (ie, unk, tech, n, guess)

`inteqn`は、積分方程式を解くためのパッケージです。
`load ("inteqn")`はこのパッケージをロードします。


*ie*は、積分方程式です;
*unk*は、未知の関数です;
*tech*は、上で与えられたこれらから試される手法です;
 is the
technique to be tried from those given above
 (*tech* = `first`は以下を意味します: 解を見つける最初の手法を試みる;
*tech* = `all`は以下を意味します: 適用可能な手法すべてを試みる);
*n*は、
`taylor`, `neumann`, `firstkindseries`, または`fredseries`
に関して扱う項の最大数です (微分法に関する再帰の最大深度でもあります);
*guess*は、`neumann`または`firstkindseries`に関する
初期の推測です。


２番目から５番目までのパラメータのデフォルト値は、以下の通りです:


*unk*: `p(x)`。
ここで、*p*は被積分関数の中で出会うMaximaが知らない最初の関数であり、
*x*は、`secondkind`方程式の場合の積分の外側で見つかった*p*
の最初の出現時の引数、または、`firstkind`方程式の中の積分変数を除いた唯一の残りの変数
です。
もし*x*を探す企てが失敗したら、ユーザーは独立変数を供給するよう尋ねられるでしょう。


tech: `first`


n: 1


guess: `neumann`と`firstkindseries`が
初期推測として`f(x)`を使うようにする`none`

<!-- category: Solving -->
<!-- keywords: ieqnprint -->
<!-- signatures: ieqnprint -->
### Variable: ieqnprint

デフォルト値: `true`


`ieqnprint`は、`ieqn`コマンドが返す結果の振る舞いを決めます。
`ieqnprint`が`false`の時、
`ieqn`関数が返すリストは、形式


   

[*solution*, *technique used*, *nterms*, *flag*]


を取ります。


ここで、もし解が厳密なら*flag*はありません。


そうでなければ、厳密でない解か閉じていない形の解かに対応して、それぞれ、単語`approximate`または`incomplete`です。
もし級数法が使われたら、
*nterms*は、取った項の数を与えます。
（項の数は、もしエラーが更なる項の生成を防いだなら、`ieqn`に与えられたnよりも小さいこともあり得ます。）

See also: `ieqn`.

<!-- category: Solving -->
<!-- keywords: lhs -->
<!-- signatures: lhs(expr) -->
### Function: lhs (expr)

*expr*の演算子が関係演算子`< <= = # equal notequal >= >`の１つ、

割り当て演算子`:= ::= : ::`の１つ、
または`infix`で宣言されたユーザー定義の二項中置演算子の時、
式*expr*の左辺(すなわち、最初の項)
を返します。


*expr*がアトムか、演算子が上で記載したもの以外の何かの時、
`lhs`は*expr*を返します。


`rhs`も参照してください。


例:



















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [lhs (aa < bb), lhs (aa <= bb), lhs (aa >= bb),
       lhs (aa > bb)];
(%o4)                   [aa, aa, aa, aa]
(%i5) [lhs (aa = bb), lhs (aa # bb), lhs (equal (aa, bb)),
       lhs (notequal (aa, bb))];
(%o5)                   [aa, aa, aa, aa]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [lhs (e1), lhs (e2), lhs (e3), lhs (e4)];
(%o10)               [foo(x), bar(y), x, x]
(%i11) infix ("][");
(%o11)                         ][
(%i12) lhs (aa ][ bb);
(%o12)                         aa
```

See also: `infix`, `rhs`.

<!-- category: Solving -->
<!-- keywords: linsolve -->
<!-- signatures: linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

変数のリストに関して同時線形方程式のリストを解きます。
それぞれの式は変数に関する多項式でなければならず、等式も取り得ます。


`globalsolve`が`true`の時、
解くべき変数それぞれは、方程式の解の値にバインドされます。


`backsubst`が`false`の時、
`linsolve`は、方程式が三角行列化された後、後退代入を実行しません。
これは、後退代入が極端に大きな式の生成の原因となる非常に大きな問題に関して
必要とされるかもしれません。


`linsolve_params`が`true`の時、
`linsolve`は
`algsys`の下のマニュアルの中で記述された任意のパラメータを表すのに使われる
`%r`シンボルも生成します。
そうでなければ、
`linsolve`は、他を使って表現されたいくつかの変数を持つ
決定中の方程式系を解きます。


`programmode`が`false`の時、
`linsolve`は、中間式(`%t`)ラベルを使って解を表示し、
ラベルのリストを返します。




















```maxima
(%i1) e1: x + z = y;
(%o1)                       z + x = y
(%i2) e2: 2*a*x - y = 2*a^2;
                                       2
(%o2)                   2 a x - y = 2 a
(%i3) e3: y - 2*z = 2;
(%o3)                      y - 2 z = 2
(%i4) [globalsolve: false, programmode: true];
(%o4)                     [false, true]
(%i5) linsolve ([e1, e2, e3], [x, y, z]);
(%o5)            [x = a + 1, y = 2 a, z = a - 1]
(%i6) [globalsolve: false, programmode: false];
(%o6)                    [false, false]
(%i7) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t7)                       z = a - 1

(%t8)                        y = 2 a

(%t9)                       x = a + 1
(%o9)                    [%t7, %t8, %t9]
(%i9) ''%;
(%o9)            [z = a - 1, y = 2 a, x = a + 1]
(%i10) [globalsolve: true, programmode: false];
(%o10)                    [true, false]
(%i11) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t11)                      z : a - 1

(%t12)                       y : 2 a

(%t13)                      x : a + 1
(%o13)                 [%t11, %t12, %t13]
(%i13) ''%;
(%o13)           [z : a - 1, y : 2 a, x : a + 1]
(%i14) [x, y, z];
(%o14)                 [a + 1, 2 a, a - 1]
(%i15) [globalsolve: true, programmode: true];
(%o15)                    [true, true]
(%i16) linsolve ([e1, e2, e3], '[x, y, z]);
(%o16)           [x : a + 1, y : 2 a, z : a - 1]
(%i17) [x, y, z];
(%o17)                 [a + 1, 2 a, a - 1]
```

See also: `globalsolve`, `backsubst`, `linsolve_params`, `algsys`, `programmode`.

<!-- category: Solving -->
<!-- keywords: linsolve_params -->
<!-- signatures: linsolve_params -->
### Variable: linsolve_params

デフォルト値: `true`


`linsolve_params`が`true`の時、
`linsolve`は、
`algsys`の下のマニュアルに記述された任意のパラメータを表すのに使われる`%r`シンボルも生成します。
それでなければ、`linsolve`は、
他を使って表現されたいくつかの変数を使った
決定中の方程式系を解きます。

See also: `linsolve`, `algsys`.

<!-- category: Solving -->
<!-- keywords: linsolvewarn -->
<!-- signatures: linsolvewarn -->
### Variable: linsolvewarn

デフォルト値: `true`


`linsolvewarn`が`true`の時、
`linsolve`はメッセージ"Dependent equations eliminated"を表示します。

<!-- category: Solving -->
<!-- keywords: multiplicities -->
<!-- signatures: multiplicities -->
### Variable: multiplicities

デフォルト値: `not_set_yet`


`multiplicities`は、
`solve`や`realroots`が返す個々の解の多様性のリストに設定されます。

See also: `solve`, `realroots`.

<!-- category: Solving -->
<!-- keywords: nroots -->
<!-- signatures: nroots(p, low, high) -->
### Function: nroots (p, low, high)

半開区間`(low, high]`の中の
実数一変数多項式*p*の実根の数を返します。
区間の端点は`minf`もしくは`inf`、無限大かもしれません。
マイナス無限大とプラス無限大。


`nroots`は、Sturm列の方法を使います。



```maxima
(%i1) p: x^10 - 2*x^4 + 1/2$
(%i2) nroots (p, -6, 9.1);
(%o2)                           4
```

<!-- category: Solving -->
<!-- keywords: nthroot -->
<!-- signatures: nthroot(p, n) -->
### Function: nthroot (p, n)

pは整数係数多項式で、
nは正の整数ですが、
q^n=pのような整数上の多項式qを返すか、
pが完全なn番目のべきでないことを示すエラーメッセージを表示します。
このルーチンは、`factor`より、また`sqfr`よりさえもっと速いです。

See also: `factor`, `sqfr`.

<!-- category: Solving -->
<!-- keywords: polyfactor -->
<!-- signatures: polyfactor -->
### Variable: polyfactor

デフォルト値: `false`


オプション変数`polyfactor`が`true`の時、
`allroots`と`bfallroots`は
もし多項式が実数なら実数上で、もし多項式が複素数なら複素数上で多項式を因数分解します。


例は`allroots`を参照してください。

See also: `allroots`, `bfallroots`.

<!-- category: Solving -->
<!-- keywords: programmode -->
<!-- signatures: programmode -->
### Variable: programmode

デフォルト値: `true`


`programmode`が`true`の時、
`solve`, `realroots`, `allroots`, `linsolve`は、
リストの中の要素として解を返します。

(`backsubst`が`false`設定されている時―
その場合、`programmode: false`が仮定されます―を除いて)


`programmode`が`false`の時、
`solve`などは、中間式ラベル`%t1`, `t2`など生成し、
解をそれらに割り当てます。

See also: `solve`, `realroots`, `allroots`, `linsolve`, `backsubst`.

<!-- category: Solving -->
<!-- keywords: realonly -->
<!-- signatures: realonly -->
### Variable: realonly

デフォルト値: `false`


`realonly`が`true`の時、
`algsys`は、
`%i`を含まないそれらの解だけを返します。

See also: `algsys`.

<!-- category: Solving -->
<!-- keywords: realroots -->
<!-- signatures: realroots(expr, bound), realroots(eqn, bound), realroots(expr), realroots(eqn) -->
### Function: realroots (expr, bound)

変数多項式*expr*もしくは1変数多項方程式*eqn*の実根の有理近似を、
`bound`の許容誤差の範囲内で計算します。
*expr*もしくは*eqn*の係数はリテラル数でなければなりません。
`%pi`のようなシンボル定数は却下されます。


`realroots`は、みつけた根の多様性を
グローバル変数`multiplicities`に割り当てます。


`realroots`は、それぞれの根を囲むためSturm列を構成し、
近似を精密化するため二分法を適用します。
根を探索する前に、すべての係数は同値の有理数に変換され、
正確な有理算術によって計算が実行されます。
たとえ係数が浮動小数点でも、
（`float`もしくは`numer`フラグによって浮動小数点が強要されない限り）結果は有理数です。


*bound*が1よりも小さい時、全ての整数根は正確に計算されます。
*bound*がしてされない時、グローバル変数`rootsepsilon`と等しいと仮定されます。


グローバル変数`programmode`が`true`の時、
`realroots`は形式`[x = x_1, x = x_2, ...]`のリストを
返します。
`programmode`が`false`の時、`realroots`は
中間式ラベル`%t1`, `%t2`, ...を生成し、
結果をそれらに割り当て、ラベルのリストを返します。


例:









```maxima
(%i1) realroots (-1 - x + x^5, 5e-6);
                               612003
(%o1)                     [x = ------]
                               524288
(%i2) ev (%[1], float);
(%o2)                 x = 1.167303085327148
(%i3) ev (-1 - x + x^5, %);
(%o3)                - 7.396496210176905E-6
```








```maxima
(%i1) realroots (expand ((1 - x)^5 * (2 - x)^3 * (3 - x)), 1e-20);
(%o1)                 [x = 1, x = 2, x = 3]
(%i2) multiplicities;
(%o2)                       [5, 3, 1]
```

See also: `multiplicities`, `float`, `numer`, `rootsepsilon`, `programmode`.

<!-- category: Solving -->
<!-- keywords: rhs -->
<!-- signatures: rhs(expr) -->
### Function: rhs (expr)

*expr*の演算子が関係演算子`< <= = # equal notequal >= >`の１つ、

割り当て演算子`:= ::= : ::`の１つ、または、
`infix`で宣言されたユーザー定義の二項中置演算子の時
式*expr*の右辺(すなわち、二番目の項)を返します。


*expr*がアトムか、演算子が上で記載したもの以外の何かの時、
`rhs`は*expr*を返します。


`lhs`も参照してください。


例:



















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [rhs (aa < bb), rhs (aa <= bb), rhs (aa >= bb),
       rhs (aa > bb)];
(%o4)                   [bb, bb, bb, bb]

(%i5) [rhs (aa = bb), rhs (aa # bb), rhs (equal (aa, bb)),
       rhs (notequal (aa, bb))];

(%o5)                   [bb, bb, bb, bb]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [rhs (e1), rhs (e2), rhs (e3), rhs (e4)];
(%o10)                  [2 x, 3 y, y, y]
(%i11) infix ("][");
(%o11)                         ][
(%i12) rhs (aa ][ bb);
(%o12)                         bb
```

See also: `infix`, `lhs`.

<!-- category: Solving -->
<!-- keywords: rootsconmode -->
<!-- signatures: rootsconmode -->
### Variable: rootsconmode

デフォルト値: `true`


`rootsconmode`は、`rootscontract`コマンドの振る舞いを決定します。
詳細は`rootscontract`を参照してください。

See also: `rootscontract`.

<!-- category: Solving -->
<!-- keywords: rootscontract -->
<!-- signatures: rootscontract(expr) -->
### Function: rootscontract (expr)

根の積を積の根に変換します。
例えば、
`rootscontract (sqrt(x)*y^(3/2))`は`sqrt(x*y^3)`をもたらします。


`radexpand`が`true`かつ`domain`が`real`の時、
`rootscontract`は、 converts 
`abs`を`sqrt`に変換します。
例えば、`rootscontract (abs(x)*sqrt(y))`は`sqrt(x^2*y)`をもたらします。


以下のように`rootscontract`に影響するオプション`rootsconmode`があります:



```maxima
問題               rootsconmodeの値　rootscontractを適用した値
      
x^(1/2)*y^(3/2)      false          (x*y^3)^(1/2)
x^(1/2)*y^(1/4)      false          x^(1/2)*y^(1/4)
x^(1/2)*y^(1/4)      true           (x*y^(1/2))^(1/2)
x^(1/2)*y^(1/3)      true           x^(1/2)*y^(1/3)
x^(1/2)*y^(1/4)      all            (x^2*y)^(1/4)
x^(1/2)*y^(1/3)      all            (x^3*y^2)^(1/6)
```


`rootsconmode`が`false`の時、
`rootscontract`は、分母が同じ有理数指数に関してだけ短縮します。
`rootsconmode: true`の例のキーは、
単に、4は2で割り切れますが、4は2で割り切れないということです。
`rootsconmode: all`は、指数の分母の最小公倍数を取ることを伴います。


`rootscontract`は、
`logcontract`と似た方法で、`ratsimp`を使います。


例:



















```maxima
(%i1) rootsconmode: false$
(%i2) rootscontract (x^(1/2)*y^(3/2));
                                   3
(%o2)                      sqrt(x y )
(%i3) rootscontract (x^(1/2)*y^(1/4));
                                   1/4
(%o3)                     sqrt(x) y
(%i4) rootsconmode: true$
(%i5) rootscontract (x^(1/2)*y^(1/4));
(%o5)                    sqrt(x sqrt(y))
(%i6) rootscontract (x^(1/2)*y^(1/3));
                                   1/3
(%o6)                     sqrt(x) y
(%i7) rootsconmode: all$
(%i8) rootscontract (x^(1/2)*y^(1/4));
                              2   1/4
(%o8)                       (x  y)
(%i9) rootscontract (x^(1/2)*y^(1/3));
                             3  2 1/6
(%o9)                      (x  y )
(%i10) rootsconmode: false$
(%i11) rootscontract (sqrt(sqrt(x) + sqrt(1 + x))
                    *sqrt(sqrt(1 + x) - sqrt(x)));
(%o11)                          1
(%i12) rootsconmode: true$
(%i13) rootscontract (sqrt(5+sqrt(5)) - 5^(1/4)*sqrt(1+sqrt(5)));
(%o13)                          0
```

See also: `radexpand`, `domain`, `abs`, `sqrt`, `rootscontract`, `logcontract`, `ratsimp`.

<!-- category: Solving -->
<!-- keywords: rootsepsilon -->
<!-- signatures: rootsepsilon -->
### Variable: rootsepsilon

デフォルト値: 1.0e-7


`rootsepsilon`は、
`realroots`関数が見つけた根に関する信頼区間を確立する許容誤差です。

See also: `realroots`.

<!-- category: Solving -->
<!-- keywords: solve -->
<!-- signatures: solve(expr, x), solve(expr), solve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: solve (expr, x)

代数等式*expr*を*x*について解き、*x*の解等式のリストを返します。
もし*expr*の等式でなければ、等式`expr = 0`が仮定されます。
*x*は関数(例えば`f(x)`)でも他のアトムでない式でも問題ありません。
（sumやproductは除きます。）*expr*が変数を１つだけ含む場合、*x*は省略できます。
*expr*は有理式でも、三角関数や指数関数を含むことができます。


以下の方法が使われます:


*E*を式、*X*を変数とします。
もし*E*が*X*に関して線形なら、*X*について自明に解かれます。
そうでなければ、もし*E*が`A*X^N + B`の形なら、
結果は、`(-B/A)^(1/N)`かける1の`N`乗根です。


もし*E*が*X*について線形でなければ、
*E*の中の*X*の指数のgcd(以下*N*とする）が指数に割られ、
根に*N*がかけられます。
その後、結果に対して`solve`が再びコールされます。
もし*E*が因数分解されるなら、`solve`は因子のそれぞれに対してコールされます。
最後に、`solve`は２次方程式、３次方程式、4次方程式の解の公式を必要に応じて使います。


*E*が解くべき変数のある関数（以下`F(X)`)の多項式の場合，
最初に`F(X)`について解かれ（結果を*C*と呼ぶ）、
関数*F*の逆関数がわかっている場合、等式`F(X)=C`が*X*について解かれます。


`breakup`が`false`なら、
`solve`は３次もしくは４次方程式の解を、
デフォルトであるいくつかの共通部分式から成る表現ではなく、
単一の式で表現されます。


`multiplicities`は、`solve`や`realroots`, `allroots`が返した
多数の独立の解のリストに設定されます。
`slove`に影響するスイッチについては、`apropos (solve)`を試してください。
もしスイッチの目的がはっきりしないなら、
個々のスイッチ名について`describe`を使うことができます。


`solve ([eqn_1, ..., eqn_n], [x_1, ..., x_n])`
は、`linsolve`もしくは`algsys`をコールすることで，
同時（線形もしくは非線形）代数方程式系を解き、変数の解リストのリストを返します。
`linsolve`の場合、このリストは解の単一リストを含みます。
引数に２つのリストをとります。
最初のリストは解くべき等式を示し、２番目のリストは決定すべき未知数のリストです。
もし等式の変数の総数が等式の数に等しいなら、２番目の引数リストは省略できます。







`programmode`が`false`の時、
`solve`は中間式(`%t`)ラベルを持つ解を表示し、ラベルのリストを返します。


`globalsolve`が`true`、かつ、問題が２つ以上の線形方程式を解くことである場合、
それぞれの解くべき変数は方程式の解の値にバインドされます。


例:


















```maxima
(%i1) solve (asin (cos (3*x))*(f(x) - 1), x);

solve: using arc-trig functions to get a solution.
Some solutions will be lost.
                            %pi
(%o1)                  [x = ---, f(x) = 1]
                             6
(%i2) ev (solve (5^f(x) = 125, f(x)), solveradcan);
                                log(125)
(%o2)                   [f(x) = --------]
                                 log(5)
(%i3) [4*x^2 - y^2 = 12, x*y - x = 2];
                      2    2
(%o3)             [4 x  - y  = 12, x y - x = 2]

(%i4) solve (%, [x, y]);
(%o4) [[x = 2, y = 2], [x = .5202594388652008 %i
 - .1331240357358706, y = .07678378523787788
 - 3.608003221870287 %i], [x = - .5202594388652008 %i
 - .1331240357358706, y = 3.608003221870287 %i
 + .07678378523787788], [x = - 1.733751846381093, 
y = - .1535675710019696]]

(%i5) solve (1 + a*x + x^3, x);

                                       3
              sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(%o5) [x = (- ---------- - -) (--------------- - -)
                  2        2      6 sqrt(3)      2

        sqrt(3) %i   1
       (---------- - -) a
            2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

                          3
 sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(---------- - -) (--------------- - -)
     2        2      6 sqrt(3)      2

         sqrt(3) %i   1
      (- ---------- - -) a
             2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

         3
 sqrt(4 a  + 27)   1 1/3               a
(--------------- - -)    - --------------------------]
    6 sqrt(3)      2                  3
                              sqrt(4 a  + 27)   1 1/3
                           3 (--------------- - -)
                                 6 sqrt(3)      2
(%i6) solve (x^3 - 1);
             sqrt(3) %i - 1        sqrt(3) %i + 1
(%o6)   [x = --------------, x = - --------------, x = 1]
                   2                     2
(%i7) solve (x^6 - 1);
           sqrt(3) %i + 1      sqrt(3) %i - 1
(%o7) [x = --------------, x = --------------, x = - 1, 
                 2                   2

                     sqrt(3) %i + 1        sqrt(3) %i - 1
               x = - --------------, x = - --------------, x = 1]
                           2                     2
(%i8) ev (x^6 - 1, %[1]);

                                      6
                      (sqrt(3) %i + 1)
(%o8)                 ----------------- - 1
                             64

(%i9) expand (%);
(%o9)                           0
(%i10) x^2 - 1;
                              2
(%o10)                       x  - 1
(%i11) solve (%, x);
(%o11)                  [x = - 1, x = 1]
(%i12) ev (%th(2), %[1]);
(%o12)                          0
```


シンボル`%r`は、解の中で任意定数を示すのに使われます。



```maxima
(%i1) solve([x+y=1,2*x+2*y=2],[x,y]);

solve: dependent equations eliminated: (2)
(%o1)                      [[x = 1 - %r1, y = %r1]]
```


更に知るには、`algsys`と `%rnum_list`.

See also: `breakup`, `realroots`, `allroots`, `describe`, `linsolve`, `algsys`, `programmode`, `globalsolve`, `%rnum_list`.

<!-- category: Solving -->
<!-- keywords: solvedecomposes -->
<!-- signatures: solvedecomposes -->
### Variable: solvedecomposes

デフォルト値: `true`


`solvedecomposes`が`true`の時、
もし多項式を解くように頼まれたなら、
`solve`は、`polydecomp`をコールします。

See also: `polydecomp`.

<!-- category: Solving -->
<!-- keywords: solveexplicit -->
<!-- signatures: solveexplicit -->
### Variable: solveexplicit

デフォルト値: `false`


`solveexplicit`が`true`の時、
`solve`が
陰解―すなわち、`F`がある関数である形式`F(x) = 0`の解―
を返すことを妨げます。

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solvefactors -->
<!-- signatures: solvefactors -->
### Variable: solvefactors

デフォルト値: `true`



`solvefactors`が`false`の時、
`solve`は、式を因数分解しようとしません。
`false`設定は、
因数分解が不要ないくつかの場合に望まれるかもしれません。

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solvenullwarn -->
<!-- signatures: solvenullwarn -->
### Variable: solvenullwarn

デフォルト値: `true`


`solvenullwarn`が`true`の時、
もし空の等式リストか空の変数リストを引数にコールされたら
`solve`は、警告メッセージを表示します。
例えば、`solve ([], [])`は、２つの警告メッセージを表示し、
`[]`を返します。

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solveradcan -->
<!-- signatures: solveradcan -->
### Variable: solveradcan

デフォルト値: `false`


`solveradcan`が`true`の時、
`solve`は`radcan`をコールし、`solve`は遅くなりますが、
指数と対数を含むある問題が解けるようになります。

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solvetrigwarn -->
<!-- signatures: solvetrigwarn -->
### Variable: solvetrigwarn

デフォルト値: `true`



`solvetrigwarn`が`true`の時、
`solve`は、
方程式を解くために逆三角関数を使い、ゆえに解を失っていることを示す
メッセージを表示するかもしれません。

See also: `solve`.

