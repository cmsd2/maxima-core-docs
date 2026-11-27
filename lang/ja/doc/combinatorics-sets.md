## Sets

<!-- category: Combinatorics -->
<!-- keywords: adjoin -->
<!-- signatures: adjoin(x, a) -->
### Function: adjoin (x, a)

集合*a*に要素`{x}`を加えた集合を返します。


もし*a*が集合リテラルでないなら、
`adjoin`は文句を言います。


`adjoin(x, a)`と`union(set(x), a)`は同値です;
しかしながら、`adjoin`は`union`より幾分早いかもしれません。


`disjoin`も参照してください。


例:







```maxima
(%i1) adjoin (c, {a, b});
(%o1)                       {a, b, c}
(%i2) adjoin (a, {a, b});
(%o2)                        {a, b}
```

<!-- category: Combinatorics -->
<!-- keywords: belln -->
<!-- signatures: belln(n) -->
### Function: belln (n)

$n$番目のベル数を返します。
`belln(n)`は*n*個のメンバーを持つ集合の分割の数です。


非負整数*n*に対して、
`belln(n)`は$n$番目のベル数に整理されます。
`belln`は他のいかなる引数に関して整理されません。


`belln`は等式、リスト、行列、集合上に分配されます。


例:


非負整数に適用された`belln`。









```maxima
(%i1) makelist (belln (i), i, 0, 6);
(%o1)               [1, 1, 2, 5, 15, 52, 203]
(%i2) is (cardinality (set_partitions ({})) = belln (0));
(%o2)                         true
(%i3) is (cardinality (set_partitions ({1, 2, 3, 4, 5, 6})) =
                       belln (6));
(%o3)                         true
```


非負整数でない引数に適用された`belln`。






```maxima
(%i1) [belln (x), belln (sqrt(3)), belln (-9)];
(%o1)        [belln(x), belln(sqrt(3)), belln(- 9)]
```

<!-- category: Combinatorics -->
<!-- keywords: cardinality -->
<!-- signatures: cardinality(a) -->
### Function: cardinality (a)

集合*a*の異なる要素の数を返します。


整理がディセーブルされた時でも、
`cardinality`は冗長な要素を無視します。


例:









```maxima
(%i1) cardinality ({});
(%o1)                           0
(%i2) cardinality ({a, a, b, c});
(%o2)                           3
(%i3) simp : false;
(%o3)                         false
(%i4) cardinality ({a, a, b, c});
(%o4)                           3
```

<!-- category: Combinatorics -->
<!-- keywords: cartesian_product -->
<!-- signatures: cartesian_product(b_1, ..., b_n) -->
### Function: cartesian_product (b_1, ..., b_n)

Returns a set of lists of the form 
形式`[x_1, ..., x_n]`のリストの集合を返します。
ここで、*x_1*, ..., *x_n*はそれぞれ、
集合*b_1*, ... , *b_n*の要素です。


もし任意の引数が集合リテラルでないなら、
`cartesian_product`は文句を言います。


例:









```maxima
(%i1) cartesian_product ({0, 1});
(%o1)                      {[0], [1]}
(%i2) cartesian_product ({0, 1}, {0, 1});
(%o2)           {[0, 0], [0, 1], [1, 0], [1, 1]}
(%i3) cartesian_product ({x}, {y}, {z});
(%o3)                      {[x, y, z]}
(%i4) cartesian_product ({x}, {-1, 0, 1});
(%o4)              {[x, - 1], [x, 0], [x, 1]}
```

<!-- category: Combinatorics -->
<!-- keywords: disjoin -->
<!-- signatures: disjoin(x, a) -->
### Function: disjoin (x, a)

元*x*を持たない集合*a*を返します。
もし*x*が*a*のメンバーでないなら、
変更なしに*a*を返します。


もし*a*が集合リテラルでないなら、
`disjoin`は文句を言います。


`disjoin(x, a)`, `delete(x, a)`,
`setdifference(a, set(x))`はすべて同値です。
これらの中で、
`disjoin`は一般的に他より速いです。


例:








```maxima
(%i1) disjoin (a, {a, b, c, d});
(%o1)                       {b, c, d}
(%i2) disjoin (a + b, {5, z, a + b, %pi});
(%o2)                      {5, %pi, z}
(%i3) disjoin (a - b, {5, z, a + b, %pi});
(%o3)                  {5, %pi, b + a, z}
```

<!-- category: Combinatorics -->
<!-- keywords: disjointp -->
<!-- signatures: disjointp(a, b) -->
### Function: disjointp (a, b)

集合*a*と*b*がばらばらなら、
`true`を返します。


もし*a*か*b*が集合リテラルでないなら、
`disjointp`は文句を言います。


例:







```maxima
(%i1) disjointp ({a, b, c}, {1, 2, 3});
(%o1)                         true
(%i2) disjointp ({a, b, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: divisors -->
<!-- signatures: divisors(n) -->
### Function: divisors (n)

*n*の約数の集合を表します。


*n*がゼロでない整数の時、
`divisors(n)`は整数の集合に整理されます。
約数の集合は元1と*n*を含みます。
負の整数の約数は、その絶対値の約数です。


`divisors`は、等式、リスト、行列、集合上に分配されます。


例:


28は完全数であることを検証できます:
(自身を除いた)約数が28です。







```maxima
(%i1) s: divisors(28);
(%o1)                 {1, 2, 4, 7, 14, 28}
(%i2) lreduce ("+", args(s)) - 28;
(%o2)                          28
```


`divisors`は整理関数です。
`divisors(a)`の中で`a`に8を代入することは、
`divisors(8)`を再評価せずに約数をもたらします。







```maxima
(%i1) divisors (a);
(%o1)                      divisors(a)
(%i2) subst (8, a, %);
(%o2)                     {1, 2, 4, 8}
```


`divisors`は、等式、リスト、行列、集合上に分配されます。









```maxima
(%i1) divisors (a = b);
(%o1)               divisors(a) = divisors(b)
(%i2) divisors ([a, b, c]);
(%o2)        [divisors(a), divisors(b), divisors(c)]
(%i3) divisors (matrix ([a, b], [c, d]));
                  [ divisors(a)  divisors(b) ]
(%o3)             [                          ]
                  [ divisors(c)  divisors(d) ]
(%i4) divisors ({a, b, c});
(%o4)        {divisors(a), divisors(b), divisors(c)}
```

<!-- category: Combinatorics -->
<!-- keywords: elementp -->
<!-- signatures: elementp(x, a) -->
### Function: elementp (x, a)

*x*が集合*a*の元の時だけ`true`を返します。


もし*a*が集合リテラルでないなら、
`elementp`は文句を言います。


例:







```maxima
(%i1) elementp (sin(1), {sin(1), sin(2), sin(3)});
(%o1)                         true
(%i2) elementp (sin(1), {cos(1), cos(2), cos(3)});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: emptyp -->
<!-- signatures: emptyp(a) -->
### Function: emptyp (a)

*a*が空の集合か空のリストの時だけ、`true`を返します。


例:







```maxima
(%i1) map (emptyp, [{}, []]);
(%o1)                     [true, true]
(%i2) map (emptyp, [a + b, {{}}, %pi]);
(%o2)                 [false, false, false]
```

<!-- category: Combinatorics -->
<!-- keywords: equiv_classes -->
<!-- signatures: equiv_classes(s, F) -->
### Function: equiv_classes (s, F)

集合*s*の
同値関係*F*に関する
同値クラスの集合を返します。


*F*は*s*の*s*との直積集合上の２変数関数です。
The return value of 
*F*の戻り値は、`true`か`false`、もしくは、
`is(expr)`が`true`か`false`のような
式*expr*です。


*F*が同値関数でない時、
`equiv_classes`は不平なくそれを受け入れますが、
その場合、結果は、一般に正しくありません。







例:


同値関係が
`true`か`false`を返すラムダ式です。







```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0},
                        lambda ([x, y], is (equal (x, y))));
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


同値関係が、`is`が`true`か`false`に評価される
関係関数の名前です。






```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, equal);
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


同値クラスが3の倍数だけ違う数です。







```maxima
(%i1) equiv_classes ({1, 2, 3, 4, 5, 6, 7},
                     lambda ([x, y], remainder (x - y, 3) = 0));
(%o1)              {{1, 4, 7}, {2, 5}, {3, 6}}
```

<!-- category: Combinatorics -->
<!-- keywords: every -->
<!-- signatures: every(f, s), every(f, L_1, ..., L_n) -->
### Function: every (f, s)

もし述語論理*f*が与えられた引数すべてで`true`なら、
`true`を返します。


ある集合が二番目の引数として与えられたとして、
もし`is(f(a_i))`が
*s*の中の*a_i*すべてに関して
`true`を返すなら
`every(f, s)`は`true`です。
`every`は、
*s*の中の*a_i*すべてに関して*f*を評価するかもしれないししないかもしれません。
集合は順序付けされていないので、
`every`は任意の順序で`f(a_i)`を評価します。


非キスとして１つか複数のリストが与えられたとして、
もし`is(f(x_1, ..., x_n))`が
*L_1*, ..., *L_n*それぞれの中の*x_1*, ..., *x_n*すべてに対して
`true`を返すなら、
`every(f, L_1, ..., L_n)`は`true`を返します。
`every`は、
*x_1*, ..., *x_n*のすべての組み合わせに対して*f*を評価するかもしれないししないかもしれません。
`every`はインデックスを増やす順序でリストを評価します。


空の集合`{}`または空のリスト`[]`が引数として与えられたとして、
`every`は`false`を返します。


グローバルフラグ`maperror`が`true`の時、
リスト*L_1*, ..., *L_n*すべては等しい長さを持たなければいけません。
`maperror`が`false`の時、
リスト引数は、最短のリストの長さに効果的に切り詰められます。


(`is`を介して)
`true`か`false`以外の何かに評価される述語論理*f*の戻り値は、
`prederror`によって決定されます。
`prederror`が`true`の時、
そんな値は`false`として扱われ、
`every`の戻り値は`false`です。
`prederror`が`false`の時、
そんな値は`unknown`として扱われ、
`every`の戻り値は`unknown`です。


例:


１つの集合に適用された`every`。
述語論理は１引数関数です。







```maxima
(%i1) every (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) every (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         false
```


２つのリストに適用された`every`。
述語論理は２引数関数です。







```maxima
(%i1) every ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) every ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


`true`か`false`以外の何かに評価される
述語論理*f*の戻り値は、
グローバルフラグ`prederror`によって決定されます。











```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
                   [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) prederror : true;
(%o4)                         true
(%i5) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o5)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: extremal_subset -->
<!-- signatures: extremal_subset(s, f, max), extremal_subset(s, f, min) -->
### Function: extremal_subset (s, f, max)

関数*f*が最大または最小値を取る、
*s*の部分集合を返します。


`extremal_subset(s, f, max)`は、
実数値関数*f*が最大値を取る、
集合またはリスト*s*の部分集合を返します。


`extremal_subset(s, f, min)`は、
実数値関数*f*が最小値を取る、
集合またはリスト*s*の部分集合を返します。


例:







```maxima
(%i1) extremal_subset ({-2, -1, 0, 1, 2}, abs, max);
(%o1)                       {- 2, 2}
(%i2) extremal_subset ({sqrt(2), 1.57, %pi/2}, sin, min);
(%o2)                       {sqrt(2)}
```

<!-- category: Combinatorics -->
<!-- keywords: flatten -->
<!-- signatures: flatten(expr) -->
### Function: flatten (expr)

*expr*と同じ演算子を持つ部分式の引数を集め、
これらの集めた引数から式を構成します。


`expr`の主演算子と違った演算子の部分式は、
たとえそれらが、逆に`expr`に関するものと同じ演算子の部分式を含んだとしても、
変更なしにコピーされます。


引数の数が演算子に関して宣言された引数と違う
式を`flatten`が構成する可能性があるかもしれません;
これは、整理器や評価器からのエラーメッセージを起こさせるかもしれません。
`flatten`はそんな状況を検出しようとしません。


特別な表現の式、例えば、標準有理式(CRE)、はflattenできません;
そんな場合、`flatten`は引数を変更なしに返します。


例:


リストに適用すると、`flatten`はリストの要素すべてを集めます。






```maxima
(%i1) flatten ([a, b, [c, [d, e], f], [[g, h]], i, j]);
(%o1)            [a, b, c, d, e, f, g, h, i, j]
```


集合に適用すると、`flatten`は集合の元すべてを集めます。







```maxima
(%i1) flatten ({a, {b}, {{c}}});
(%o1)                       {a, b, c}
(%i2) flatten ({a, {[a], {a}}});
(%o2)                       {a, [a]}
```


`flatten`は、主演算子をn項に宣言する効果に似ています。
しかしながら、`flatten`は、
主演算子と違う演算子を持つ部分式上に影響を持ちません。
一方、n項宣言はそれらに影響します。








```maxima
(%i1) expr: flatten (f (g (f (f (x)))));
(%o1)                     f(g(f(f(x))))
(%i2) declare (f, nary);
(%o2)                         done
(%i3) ev (expr);
(%o3)                      f(g(f(x)))
```


`flatten`は、他の任意の演算子と同じように添字付き関数を扱います。






```maxima
(%i1) flatten (f[5] (f[5] (x, y), z));
(%o1)                      f (x, y, z)
                            5
```


引数の数が演算子に関して宣言された引数と違う
式を`flatten`が構成する可能性があるかもしれません;








```maxima
(%i1) 'mod (5, 'mod (7, 4));
(%o1)                   mod(5, mod(7, 4))
(%i2) flatten (%);
(%o2)                     mod(5, 7, 4)
(%i3) ''%, nouns;
Wrong number of arguments to mod
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Combinatorics -->
<!-- keywords: full_listify -->
<!-- signatures: full_listify(a) -->
### Function: full_listify (a)

*a*の中のすべての集合演算子をリスト演算子で置き換え、
結果を返します。
`full_listify`は、
たとえ主演算子が`set`でなくても
入れ子の部分式の中の集合演算子を置き換えます。


`listify`は主演算子だけを置き換えます。


例:







```maxima
(%i1) full_listify ({a, b, {c, {d, e, f}, g}});
(%o1)               [a, b, [c, [d, e, f], g]]
(%i2) full_listify (F (G ({a, b, H({c, d, e})})));
(%o2)              F(G([a, b, H([c, d, e])]))
```

<!-- category: Combinatorics -->
<!-- keywords: fullsetify -->
<!-- signatures: fullsetify(a) -->
### Function: fullsetify (a)

*a*がリストの時、
リスト演算子を集合演算子で置き換え、
`fullsetify`を集合であるメンバーそれぞれに適用します。
*a*がリストでない時、変更なしで返します。


`setify`は主演算子だけを置き換えます。


例:



`f([b])`の主演算子はリストでないので、
行`(%o2)`で、
`f`の引数は集合に変換されません。







```maxima
(%i1) fullsetify ([a, [a]]);
(%o1)                       {a, {a}}
(%i2) fullsetify ([a, f([b])]);
(%o2)                      {a, f([b])}
```

<!-- category: Combinatorics -->
<!-- keywords: identity -->
<!-- signatures: identity(x) -->
### Function: identity (x)

任意の引数*x*に対して*x*を返します。


例:


`identity`は、
引数が既にブーリアン値の時、
述語論理として使うことができます。






```maxima
(%i1) every (identity, [true, true]);
(%o1)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: integer_partitions -->
<!-- signatures: integer_partitions(n), integer_partitions(n, len) -->
### Function: integer_partitions (n)

*n*の整数分割を返します。
すなわち、和が*n*になる整数のリストです。


`integer_partitions(n)`は、
整数*n*の分割すべての集合を返します。
分割それぞれは、大きい順に並べられたリストです。


`integer_partitions(n, len)`は、
長さ*len*以下の分割すべてを返します;
この場合、
*len*より少ない項を持つ分割それぞれには、
厳密に*len*項持つ分割にするように、ゼロが足されます。
分割それぞれは、大きい順に並べられたリストです。


リスト$[a_1, ..., a_m]$は、
(1) $a_i$それぞれが非ゼロ整数、かつ、
(2) $a_1 + ... + a_m = n.$
の時、非負整数$n$の分割です。
従って0は分割を持ちません。


例:











```maxima
(%i1) integer_partitions (3);
(%o1)               {[1, 1, 1], [2, 1], [3]}
(%i2) s: integer_partitions (25)$
(%i3) cardinality (s);
(%o3)                         1958
(%i4) map (lambda ([x], apply ("+", x)), s);
(%o4)                         {25}
(%i5) integer_partitions (5, 3);
(%o5) {[2, 2, 1], [3, 1, 1], [3, 2, 0], [4, 1, 0], [5, 0, 0]}
(%i6) integer_partitions (5, 2);
(%o6)               {[3, 2], [4, 1], [5, 0]}
```


条件を満たす分割すべてを見つけるには、
関数`subset`を使ってください;
以下は素数から成る10の分割すべてを見つける例です。









```maxima
(%i1) s: integer_partitions (10)$
(%i2) cardinality (s);
(%o2)                          42
(%i3) xprimep(x) := integerp(x) and (x > 1) and primep(x)$
(%i4) subset (s, lambda ([x], every (xprimep, x)));
(%o4) {[2, 2, 2, 2, 2], [3, 3, 2, 2], [5, 3, 2], [5, 5], [7, 3]}
```

<!-- category: Combinatorics -->
<!-- keywords: intersect -->
<!-- signatures: intersect(a_1, ..., a_n) -->
### Function: intersect (a_1, ..., a_n)

`intersect`は、以下に見る`intersection`と同じです。

<!-- category: Combinatorics -->
<!-- keywords: intersection -->
<!-- signatures: intersection(a_1, ..., a_n) -->
### Function: intersection (a_1, ..., a_n)

集合*a_1*から*a_n*までに共通な
要素を含む
集合を返します。


もし引数のいずれかが集合リテラルでないなら、
`intersection`は文句を言います。


例:













```maxima
(%i1) S_1 : {a, b, c, d};
(%o1)                     {a, b, c, d}
(%i2) S_2 : {d, e, f, g};
(%o2)                     {d, e, f, g}
(%i3) S_3 : {c, d, e, f};
(%o3)                     {c, d, e, f}
(%i4) S_4 : {u, v, w};
(%o4)                       {u, v, w}
(%i5) intersection (S_1, S_2);
(%o5)                          {d}
(%i6) intersection (S_2, S_3);
(%o6)                       {d, e, f}
(%i7) intersection (S_1, S_2, S_3);
(%o7)                          {d}
(%i8) intersection (S_1, S_2, S_3, S_4);
(%o8)                          {}
```

<!-- category: Combinatorics -->
<!-- keywords: kron_delta -->
<!-- signatures: kron_delta(x, y, ..., xp) -->
### Function: kron_delta (x, y, ..., xp)

クロネッカーのデルタ関数を表します。


`kron_delta`は、
*xi*と*yj*が引数のすべての対で等しい時
1に整理され、
*xi*と*yj*が引数のある対で等しくない時
0に整理されます。
等号は`is(equal(xi,j))`を使って決定され、
不等号は`is(notsqual(xi,xj))`を使って決定されます。
厳密に1つの引数に対して、`kron_delta`はエラーをシグナルします。


例:










```maxima
(%i1) kron_delta(a,a);
(%o1)                                  1
(%i2) kron_delta(a,b,a,b);
(%o2)                          kron_delta(a, b)
(%i3) kron_delta(a,a,b,a+1);
(%o3)                                  0
(%i4) assume(equal(x,y));
(%o4)                            [equal(x, y)]
(%i5) kron_delta(x,y);
(%o5)                                  1
```

<!-- category: Combinatorics -->
<!-- keywords: listify -->
<!-- signatures: listify(a) -->
### Function: listify (a)

*a*が集合の時、
*a*の元を含む
リストを返します。
そうでなければ、`listify`は*a*を返します。


`full_listify`は
*a*の中の集合演算子をリスト演算子に置き換えます。


例:







```maxima
(%i1) listify ({a, b, c, d});
(%o1)                     [a, b, c, d]
(%i2) listify (F ({a, b, c, d}));
(%o2)                    F({a, b, c, d})
```

<!-- category: Combinatorics -->
<!-- keywords: lreduce -->
<!-- signatures: lreduce(F, s), lreduce(F, s, s_0) -->
### Function: lreduce (F, s)

二項関数*F*を合成によってn項関数に拡張します。
ここで*s*はリストです。


`lreduce(F, s)`は`F(... F(F(s_1, s_2), s_3), ... s_n)`を返します。


オプション引数*s_0*が存在する時、
結果は`lreduce(F, cons(s_0, s))`と同値です。


関数*F*は、最初の*leftmost*の元に適用されます。
だから、"lreduce"と名付けられています。


`rreduce`, `xreduce`, `tree_reduce`も参照してください。


例:


オプション引数なしの`lreduce`。







```maxima
(%i1) lreduce (f, [1, 2, 3]);
(%o1)                     f(f(1, 2), 3)
(%i2) lreduce (f, [1, 2, 3, 4]);
(%o2)                  f(f(f(1, 2), 3), 4)
```


オプション引数ありの`lreduce`。






```maxima
(%i1) lreduce (f, [1, 2, 3], 4);
(%o1)                  f(f(f(4, 1), 2), 3)
```


組み込み二項演算子に適用された`lreduce`。
`/`は割り算演算子。







```maxima
(%i1) lreduce ("^", args ({a, b, c, d}));
                               b c d
(%o1)                       ((a ) )
(%i2) lreduce ("/", args ({a, b, c, d}));
                                a
(%o2)                         -----
                              b c d
```

<!-- category: Combinatorics -->
<!-- keywords: makeset -->
<!-- signatures: makeset(expr, x, s) -->
### Function: makeset (expr, x, s)

式*expr*から生成された元を持つ集合を返します。
ここで、*x*は*expr*の中の変数のリストであり、
*s*はリストの集合かリストです。
集合の元それぞれを生成するために、
*expr*は、
*s*の元に並列にバインドされた変数*x*で評価されます。


*s*の元それぞれは
*x*と同じ長さを持たなければいけません。
変数*x*のリストは、添字の付かないシンボルのリストでなければいけません。
たとえシンボルが１つしかない場合でも、*x*は１要素のリストでなければいけなく、
*s*の元それぞれは１要素のリストでなければいけません。






`makelist`も参照してください。


例:










```maxima
(%i1) makeset (i/j, [i, j], [[1, a], [2, b], [3, c], [4, d]]);
                           1  2  3  4
(%o1)                     {-, -, -, -}
                           a  b  c  d
(%i2) S : {x, y, z}$
(%i3) S3 : cartesian_product (S, S, S);
(%o3) {[x, x, x], [x, x, y], [x, x, z], [x, y, x], [x, y, y], 
[x, y, z], [x, z, x], [x, z, y], [x, z, z], [y, x, x], 
[y, x, y], [y, x, z], [y, y, x], [y, y, y], [y, y, z], 
[y, z, x], [y, z, y], [y, z, z], [z, x, x], [z, x, y], 
[z, x, z], [z, y, x], [z, y, y], [z, y, z], [z, z, x], 
[z, z, y], [z, z, z]}
(%i4) makeset (i + j + k, [i, j, k], S3);
(%o4) {3 x, 3 y, y + 2 x, 2 y + x, 3 z, z + 2 x, z + y + x, 
                                       z + 2 y, 2 z + x, 2 z + y}
(%i5) makeset (sin(x), [x], {[1], [2], [3]});
(%o5)               {sin(1), sin(2), sin(3)}
```

<!-- category: Combinatorics -->
<!-- keywords: moebius -->
<!-- signatures: moebius(n) -->
### Function: moebius (n)

メビウス関数を表します。


*n*が$k$個の異なる素数の積の時、
`moebius(n)`は$(-1)^k$に整理されます;
$n = 1$の時、1に整理されます;
他の正の数すべてに対して、0に整理されます。


`moebius`は等式、リスト、行列、集合上に分配されます。


例:














```maxima
(%i1) moebius (1);
(%o1)                           1
(%i2) moebius (2 * 3 * 5);
(%o2)                          - 1
(%i3) moebius (11 * 17 * 29 * 31);
(%o3)                           1
(%i4) moebius (2^32);
(%o4)                           0
(%i5) moebius (n);
(%o5)                      moebius(n)
(%i6) moebius (n = 12);
(%o6)                    moebius(n) = 0
(%i7) moebius ([11, 11 * 13, 11 * 13 * 15]);
(%o7)                      [- 1, 1, 1]
(%i8) moebius (matrix ([11, 12], [13, 14]));
                           [ - 1  0 ]
(%o8)                      [        ]
                           [ - 1  1 ]
(%i9) moebius ({21, 22, 23, 24});
(%o9)                      {- 1, 0, 1}
```

<!-- category: Combinatorics -->
<!-- keywords: multinomial_coeff -->
<!-- signatures: multinomial_coeff(a_1, ..., a_n), multinomial_coeff() -->
### Function: multinomial_coeff (a_1, ..., a_n)

多項係数を返します。


*a_k*それぞれが非負の整数の時、
多項係数は、
`a_1 + ... + a_n`個の別々のオブジェクトを
$k$番目の枠の中に*a_k*の要素を持つ$n$個の枠に置く方法の数を与えます。


一般に、`multinomial_coeff (a_1, ..., a_n)`は
`(a_1 + ... + a_n)!/(a_1! ... a_n!)`と同値です。


`multinomial_coeff()` (引数なし)は1に評価されます。


`minfactorial`は`multinomial_coeff`が返す値を整理することができます。


例:









```maxima
(%i1) multinomial_coeff (1, 2, x);
                            (x + 3)!
(%o1)                       --------
                              2 x!
(%i2) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o2)                -----------------------
                                2
(%i3) multinomial_coeff (-6, 2);
                             (- 4)!
(%o3)                       --------
                            2 (- 6)!
(%i4) minfactorial (%);
(%o4)                          10
```

<!-- category: Combinatorics -->
<!-- keywords: num_distinct_partitions -->
<!-- signatures: num_distinct_partitions(n), num_distinct_partitions(n, list) -->
### Function: num_distinct_partitions (n)

*n*が非負の整数の時、
*n*の異なる整数分割の数を返します。
そうでなければ、`num_distinct_partitions`は名詞形を返します。


`num_distinct_partitions(n, list)`は、
1, 2, 3, ..., *n*の異なる分割の数のリストを返します。


*n*の異なる分割は、
$n = k_1 + ... + k_m$となるような
異なる正の整数$k_1$, ..., $k_m$のリストです。


例:








```maxima
(%i1) num_distinct_partitions (12);
(%o1)                          15
(%i2) num_distinct_partitions (12, list);
(%o2)      [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15]
(%i3) num_distinct_partitions (n);
(%o3)              num_distinct_partitions(n)
```

<!-- category: Combinatorics -->
<!-- keywords: num_partitions -->
<!-- signatures: num_partitions(n), num_partitions(n, list) -->
### Function: num_partitions (n)

*n*が非負の整数の時、
*n*の整数分割の数を返します。
そうでなければ、`num_partitions`は名詞式を返します。


`num_partitions(n, list)`は、
1, 2, 3, ..., *n*の整数分割の数のリストを返します。


非負の整数*n*に対して、
`num_partitions(n)`は
`cardinality(integer_partitions(n))`と等しいです;
しかしながら、`num_partitions`は、
分割の集合を実際には構成しないので、はるかに速いです。


例:








```maxima
(%i1) num_partitions (5) = cardinality (integer_partitions (5));
(%o1)                         7 = 7
(%i2) num_partitions (8, list);
(%o2)            [1, 1, 2, 3, 5, 7, 11, 15, 22]
(%i3) num_partitions (n);
(%o3)                   num_partitions(n)
```

<!-- category: Combinatorics -->
<!-- keywords: partition_set -->
<!-- signatures: partition_set(a, f) -->
### Function: partition_set (a, f)

集合*a*を述語論理*f*に従って分割します。


`partition_set`は２つの集合のリストを返します。
最初の集合は
*f*が`false`に評価される
*a*の要素から成り、
二番目は*a*の他の要素すべてから成ります。
`partition_set`は
`is`を*f*の戻り値に適用しません。


もし*a*が集合リテラルなら
`partition_set`は文句を言います。


`subset`も参照してください。


例:








```maxima
(%i1) partition_set ({2, 7, 1, 8, 2, 8}, evenp);
(%o1)                   [{1, 7}, {2, 8}]
(%i2) partition_set ({x, rat(y), rat(y) + z, 1},
                     lambda ([x], ratp(x)));
(%o2)/R/              [{1, x}, {y, y + z}]
```

<!-- category: Combinatorics -->
<!-- keywords: permutations -->
<!-- signatures: permutations(a) -->
### Function: permutations (a)

リストまたは集合*a*の元の異なる順列すべての集合を返します。
順列それぞれは、集合でなくリストです。


*a*がリストの時、
*a*の重複した元が順列の中に含まれます。


もし*a*がリストリテラルや集合リテラルでないなら、
`permutations`は文句を言います。


`random_permutation`も参照してください。


例:







```maxima
(%i1) permutations ([a, a]);
(%o1)                       {[a, a]}
(%i2) permutations ([a, a, b]);
(%o2)           {[a, a, b], [a, b, a], [b, a, a]}
```

<!-- category: Combinatorics -->
<!-- keywords: powerset -->
<!-- signatures: powerset(a), powerset(a, n) -->
### Function: powerset (a)

*a*の部分集合すべての集合、または、その集合の部分集合を返します。


`powerset(a)`は
集合*a*の部分集合すべての集合を返します。
`powerset(a)`は`2^cardinality(a)`個の元を持ちます。


`powerset(a, n)`は、
濃度*n*を持つ*a*の部分集合すべての集合を返します。


もし*a*が集合リテラルでないか、
*n*が非負の整数でないなら、
`powerset`は文句を言います。


例:











```maxima
(%i1) powerset ({a, b, c});
(%o1) {{}, {a}, {a, b}, {a, b, c}, {a, c}, {b}, {b, c}, {c}}
(%i2) powerset ({w, x, y, z}, 4);
(%o2)                    {{w, x, y, z}}
(%i3) powerset ({w, x, y, z}, 3);
(%o3)     {{w, x, y}, {w, x, z}, {w, y, z}, {x, y, z}}
(%i4) powerset ({w, x, y, z}, 2);
(%o4)   {{w, x}, {w, y}, {w, z}, {x, y}, {x, z}, {y, z}}
(%i5) powerset ({w, x, y, z}, 1);
(%o5)                 {{w}, {x}, {y}, {z}}
(%i6) powerset ({w, x, y, z}, 0);
(%o6)                         {{}}
```

<!-- category: Combinatorics -->
<!-- keywords: random_permutation -->
<!-- signatures: random_permutation(a) -->
### Function: random_permutation (a)

クヌースのシャッフルアルゴリズムで構成されるような、
集合またはリスト*a*のランダムな順列を返します。


戻り値は、たとえ要素すべてが偶然同じでも
引数とは別の新しいリストです。
しかしながら、引数の要素はコピーされません。


例:









```maxima
(%i1) random_permutation ([a, b, c, 1, 2, 3]);
(%o1)                  [c, 1, 2, 3, a, b]
(%i2) random_permutation ([a, b, c, 1, 2, 3]);
(%o2)                  [b, 3, 1, c, a, 2]
(%i3) random_permutation ({x + 1, y + 2, z + 3});
(%o3)                 [y + 2, z + 3, x + 1]
(%i4) random_permutation ({x + 1, y + 2, z + 3});
(%o4)                 [x + 1, y + 2, z + 3]
```

<!-- category: Combinatorics -->
<!-- keywords: rreduce -->
<!-- signatures: rreduce(F, s), rreduce(F, s, s_{n + 1}) -->
### Function: rreduce (F, s)

合成によって二項関数*F*をn項関数に拡張します。
ここで、*s*はリストです。


`rreduce(F, s)`は
`F(s_1, ... F(s_{n - 2}, F(s_{n - 1}, s_n)))`を返します。
オプション引数*s_{n + 1}*が存在する時、
結果は、`rreduce(F, endcons(s_{n + 1}, s))`
と同値です。


関数*F*は、最初*rightmost*のリスト要素に適用されます。
だから名前が"rreduce"です。


`lreduce`, `tree_reduce`, `xreduce`も参照してください。


例:


オプション引数なしの`rreduce`。







```maxima
(%i1) rreduce (f, [1, 2, 3]);
(%o1)                     f(1, f(2, 3))
(%i2) rreduce (f, [1, 2, 3, 4]);
(%o2)                  f(1, f(2, f(3, 4)))
```


オプション引数ありの`rreduce`。






```maxima
(%i1) rreduce (f, [1, 2, 3], 4);
(%o1)                  f(1, f(2, f(3, 4)))
```


組み込み二項演算子に適用された`rreduce`。
`/`は割り算演算子。







```maxima
(%i1) rreduce ("^", args ({a, b, c, d}));
                                 d
                                c
                               b
(%o1)                         a
(%i2) rreduce ("/", args ({a, b, c, d}));
                               a c
(%o2)                          ---
                               b d
```

<!-- category: Combinatorics -->
<!-- keywords: set_partitions -->
<!-- signatures: set_partitions(a), set_partitions(a, n) -->
### Function: set_partitions (a)

*a*の分割すべての集合、または、その集合の部分集合を返します。


`set_partitions(a, n)`は
*n*個の空でないばらばらの部分集合への
*a*の分解すべての集合を返します。


`set_partitions(a)`は分割すべての集合を返します。


`stirling2`は集合の分割の集合の濃度を返します。


集合の集合$P$は



1. $P$の元それぞれが空でない集合
2. $P$の別の元はばらばらである。
3. $P$の元の和集合が$S$に等しい

時、
集合$S$の分割です。


例:


条件1と2が空ゆえに真なので、空集合はそれ自身の分割です。






```maxima
(%i1) set_partitions ({});
(%o1)                         {{}}
```


集合の分割の集合の濃度は、
`stirling2`を使って見つけられます。








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) cardinality(p) = stirling2 (6, 3);
(%o3)                        90 = 90
```


`p`の元それぞれは
*n* = 3個の元を持たなければいけません;
チェックしましょう。








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (cardinality, p);
(%o3)                          {3}
```


最後に、
`p`の元それぞれに対して、
元の和集合は`s`に等しくなければいけません;
チェックしましょう。








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (lambda ([x], apply (union, listify (x))), p);
(%o3)                 {{0, 1, 2, 3, 4, 5}}
```

<!-- category: Combinatorics -->
<!-- keywords: setdifference -->
<!-- signatures: setdifference(a, b) -->
### Function: setdifference (a, b)

集合*a*の中の、集合*b*にない要素を含む集合を返します。


もし*a*か*b*が集合リテラルでないなら、
`setdifference`は文句を言います。


例:












```maxima
(%i1) S_1 : {a, b, c, x, y, z};
(%o1)                  {a, b, c, x, y, z}
(%i2) S_2 : {aa, bb, c, x, y, zz};
(%o2)                 {aa, bb, c, x, y, zz}
(%i3) setdifference (S_1, S_2);
(%o3)                       {a, b, z}
(%i4) setdifference (S_2, S_1);
(%o4)                     {aa, bb, zz}
(%i5) setdifference (S_1, S_1);
(%o5)                          {}
(%i6) setdifference (S_1, {});
(%o6)                  {a, b, c, x, y, z}
(%i7) setdifference ({}, S_1);
(%o7)                          {}
```

<!-- category: Combinatorics -->
<!-- keywords: setequalp -->
<!-- signatures: setequalp(a, b) -->
### Function: setequalp (a, b)

集合*a*と*b*が同じ要素数を持ち、


`listify`が決定した順序で考えて
*a*の要素の中の`x`と
*b*の要素の中の`y`に対して
`is(x = y)`が`true`なら、
`true`を返します。
そうでなければ、`setequalp`は`false`を返します。


例:








```maxima
(%i1) setequalp ({1, 2, 3}, {1, 2, 3});
(%o1)                         true
(%i2) setequalp ({a, b, c}, {1, 2, 3});
(%o2)                         false
(%i3) setequalp ({x^2 - y^2}, {(x + y) * (x - y)});
(%o3)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: setify -->
<!-- signatures: setify(a) -->
### Function: setify (a)

リスト*a*の要素から集合を構成します。
リスト*a*の重複した要素は削除され、
要素は、述語論理`orderlessp`に従って並び替えられます。


もし*a*が集合リテラルでないなら、
`setify`は文句を言います。


例:








```maxima
(%i1) setify ([1, 2, 3, a, b, c]);
(%o1)                  {1, 2, 3, a, b, c}
(%i2) setify ([a, b, c, a, b, c]);
(%o2)                       {a, b, c}
(%i3) setify ([7, 13, 11, 1, 3, 9, 5]);
(%o3)                {1, 3, 5, 7, 9, 11, 13}
```

<!-- category: Combinatorics -->
<!-- keywords: setp -->
<!-- signatures: setp(a) -->
### Function: setp (a)

*a*がMaximaの集合の時だけ、`true`を返します。


`setp`は、
整理された集合はもちろん、未整理の集合(すなわち、冗長な元を持つ集合)に対して、
`true`を返します。



`setp`はMaxima関数
`setp(a) := not atom(a) and op(a) = 'set`
と同値です。


例:








```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) {a, a, a};
(%o2)                       {a, a, a}
(%i3) setp (%);
(%o3)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: some -->
<!-- signatures: some(f, a), some(f, L_1, ..., L_n) -->
### Function: some (f, a)

もし与えられた引数のうち１つ以上で述語論理*f*が`true`なら
`true`を返します。


二番目の引数として集合１つが与えられたとして、
もし
*s*の中の１つ以上の*a_i*に対して
`is(f(a_i))`が`true`を返すなら、
`some(f, s)`は`true`を返します。
`some`は
*s*の中の*a_i*すべてに対して
*f*を評価するかどうかわかりません。
集合は順序がないので、
`some`は任意の順序で`f(a_i)`評価するかもしれません。


引数として２つ以上のリストが与えられたとして、
`some(f, L_1, ..., L_n)`は`true`を返します。
もし
*L_1*, ..., *L_n*それぞれの中の１つ以上の*x_1*, ..., *x_n*で
`is(f(x_1, ..., x_n))`が`true`を返すなら、
`some`は
いくつかの組み合わせ*x_1*, ..., *x_n*に対して
*f*を評価するかどうかわかりません。
`some`はインデックスを増加する順序でリストを評価します。


引数として空集合`{}`または空のリスト`[]`が与えられたとして、
`some`は`false`を返します。


グローバルフラグ`maperror`が`true`の時、
すべてのリスト*L_1*, ..., *L_n*は同じ長さを持たなければいけません。
`maperror`が`false`の時、
リスト引数は、最短のリストの長さに効果的に切り詰められます。


(`is`を介して)`true`か`false`以外の何かに評価される
述語論理*f*の戻り値は、
グローバルフラグ`prederror`によって決定されます。
`prederror`が`true`の時、
そんな値は`false`として扱われます。
`prederror`が`false`の時、
そんな値は`unknown`として扱われます。


例:


集合１つに適用された`some`。
述語論理は引数１つの関数です。







```maxima
(%i1) some (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) some (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         true
```


２つのリストに適用された`some`。
述語論理は引数２つの関数です。







```maxima
(%i1) some ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) some ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


`true`か`false`以外の何かに評価される述語論理*f*の戻り値は、
グローバルフラグ`prederror`によって決定されます。













```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
           [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o4)                         true
(%i5) prederror : true;
(%o5)                         true
(%i6) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o6)                         false
(%i7) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o7)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: stirling1 -->
<!-- signatures: stirling1(n, m) -->
### Function: stirling1 (n, m)

第一種のスターリング数を表します。


*n*と*m*が非負の整数の時、
`stirling1 (n, m)`の大きさは
*m*個の巡回置換を持つ*n*個の元を持つ集合の順列の数です。
詳細はGraham, Knuth and Patashnik *Concrete Mathematics*を参照してください。
Maximaは、
0より小さい*m*に対して
`stirling1 (n, m)`を定義するために
再帰関係を使います;
0より小さい*n*と非整数引数に対して未定義です。


`stirling1`は整理関数です。
Maximaは以下の恒等式を知っています。




1. $stirling1(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling1(n, n) = 1$ (Ref. [1])
3. $stirling1(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling1(n + 1, 0) = 0$ (Ref. [1])
5. $stirling1(n + 1, 1) = n!$ (Ref. [1])
6. $stirling1(n + 1, 2) = 2^n - 1$ (Ref. [1])


これらの恒等式は
引数が、整数リテラルまたは整数と宣言されたシンボルで、かつ、
最初の引数が非負の時、
適用されます。
`stirling1`は、非整数引数に対して整理しません。


参考文献:


[1] Donald Knuth, *The Art of Computer Programming,*
third edition, Volume 1, Section 1.2.6, Equations 48, 49, and 50.


例:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n, n);
(%o3)                           1
```


`stirling1`は非整数引数に対して整理しません。






```maxima
(%i1) stirling1 (sqrt(2), sqrt(2));
(%o1)              stirling1(sqrt(2), sqrt(2))
```


Maximaは
`stirling1`に恒等式を適用します。









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n + 1, n);
                            n (n + 1)
(%o3)                       ---------
                                2
(%i4) stirling1 (n + 1, 1);
(%o4)                          n!
```

<!-- category: Combinatorics -->
<!-- keywords: stirling2 -->
<!-- signatures: stirling2(n, m) -->
### Function: stirling2 (n, m)

第二種スターリング数を表します。


*n*と*m*が非負の整数の時、
`stirling2 (n, m)`は、
濃度*n*の集合が*m*個のばらばらの部分集合に分割できる方法の数です。
Maximaは、
0より小さい*m*に対して
`stirling2 (n, m)`を定義するために
再帰関係を使います;
0より小さい*n*と非整数の引数に対して未定義です。


`stirling2`は整理関数です。
Maximaは以下の恒等式を知っています。




1. $stirling2(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling2(n, n) = 1$ (Ref. [1])
3. $stirling2(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling2(n + 1, 1) = 1$ (Ref. [1])
5. $stirling2(n + 1, 2) = 2^n - 1$ (Ref. [1])
6. $stirling2(n, 0) = kron_delta(n, 0)$ (Ref. [2])
7. $stirling2(n, m) = 0$ when $m > n$ (Ref. [2])
8. $stirling2(n, m) = sum((-1)^(m - k) binomial(m k) k^n,i,1,m) / m!$
when $m$ and $n$ are integers, and $n$ is nonnegative. (Ref. [3])


引数が整数リテラルまたは整数と宣言されたシンボルで、かつ、最初の引数が非負の時、
これらの恒等式が適用されます。
`stirling2`は非整数引数に対して整理されません。


参考文献:


[1] Donald Knuth. *The Art of Computer Programming*,
third edition, Volume 1, Section 1.2.6, Equations 48, 49, and 50.


[2] Graham, Knuth, and Patashnik. *Concrete Mathematics*, Table 264.


[3] Abramowitz and Stegun. *Handbook of Mathematical Functions*, Section 24.1.4.


例:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n, n);
(%o3)                           1
```


`stirling2`は非整数引数に対して整理されません。






```maxima
(%i1) stirling2 (%pi, %pi);
(%o1)                  stirling2(%pi, %pi)
```


Maximaは
`stirling2`に恒等式を適用します。









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n + 9, n + 8);
                         (n + 8) (n + 9)
(%o3)                    ---------------
                                2
(%i4) stirling2 (n + 1, 2);
                              n
(%o4)                        2  - 1
```

<!-- category: Combinatorics -->
<!-- keywords: subset -->
<!-- signatures: subset(a, f) -->
### Function: subset (a, f)

述語論理*f*を満たす
集合*a*の部分集合を返します。


`subset`は、
*f*が`false`以外の何かを返す、*a*の要素から成る集合を返します。
`subset`は
`is`を*f*の戻り値に適用しません。


もし*a*が集合リテラルでないなら
`subset`は文句を言います。


`partition_set`も参照してください。


例:







```maxima
(%i1) subset ({1, 2, x, x + y, z, x + y + z}, atom);
(%o1)                     {1, 2, x, z}
(%i2) subset ({1, 2, 7, 8, 9, 14}, evenp);
(%o2)                      {2, 8, 14}
```

<!-- category: Combinatorics -->
<!-- keywords: subsetp -->
<!-- signatures: subsetp(a, b) -->
### Function: subsetp (a, b)

集合*a*が*b*の部分集合の時だけ、
`true`を返します。


もし*a*か*b*のいずれかが集合リテラルでないなら、
`subsetp`は文句を言います。


例:







```maxima
(%i1) subsetp ({1, 2, 3}, {a, 1, b, 2, c, 3});
(%o1)                         true
(%i2) subsetp ({a, 1, b, 2, c, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: symmdifference -->
<!-- signatures: symmdifference(a_1, ..., a_n) -->
### Function: symmdifference (a_1, ..., a_n)

集合*a_1*, ..., *a_n*の対称差を返します。


２つの引数が与えられたとして、
`symmdifference ( a, b)`は
`union (setdifference ( a, b), setdifference (b, a))`と同じです。


もし引数が集合リテラルでないなら、
`symmdifference`は文句を言います。


例:













```maxima
(%i1) S_1 : {a, b, c};
(%o1)                       {a, b, c}
(%i2) S_2 : {1, b, c};
(%o2)                       {1, b, c}
(%i3) S_3 : {a, b, z};
(%o3)                       {a, b, z}
(%i4) symmdifference ();
(%o4)                          {}
(%i5) symmdifference (S_1);
(%o5)                       {a, b, c}
(%i6) symmdifference (S_1, S_2);
(%o6)                        {1, a}
(%i7) symmdifference (S_1, S_2, S_3);
(%o7)                        {1, b, z}
(%i8) symmdifference ({}, S_1, S_2, S_3);
(%o8)                        {1,b, z}
```

<!-- category: Combinatorics -->
<!-- keywords: tree_reduce -->
<!-- signatures: tree_reduce(F, s), tree_reduce(F, s, s_0) -->
### Function: tree_reduce (F, s)

合成によって二項関数*F*をn項関数に拡張します。
ここで*s*は集合かリストです。


`tree_reduce`は以下と同値です:
新しいリスト`[F(s_1, s_2), F(s_3, s_4), ...]`を形成するために
*F*を要素の連続する対に適用します。
もし奇数個の要素があるなら、
最後の要素は変化なしに通過させます。
そして、リストが１つの要素になるまで繰り返します。１つの要素になった時、それが戻り値です。


オプションの引数*s_0*がある時，
結果は
`tree_reduce(F, cons(s_0, s)`と同値です。


浮動小数点数の足し算に関して、
`tree_reduce`は、
`rreduce`や`lreduce`よりも小さな丸め誤差を持つ和を返します。


*s*の要素と部分的な結果は
最小深度の二項木の中に配列されます。
だから名前が"tree_reduce"です。


例:


偶数個の要素を持つリストに適用された`tree_reduce`。






```maxima
(%i1) tree_reduce (f, [a, b, c, d]);
(%o1)                  f(f(a, b), f(c, d))
```


奇数個の要素を持つリストに適用された`tree_reduce`。






```maxima
(%i1) tree_reduce (f, [a, b, c, d, e]);
(%o1)               f(f(f(a, b), f(c, d)), e)
```

<!-- category: Combinatorics -->
<!-- keywords: union -->
<!-- signatures: union(a_1, ..., a_n) -->
### Function: union (a_1, ..., a_n)

集合*a_1*から*a_n*の和集合を返します。


`union()` (引数なし)は空集合を返します。


もし引数が集合リテラルでないなら、
`union`は文句を言います。


例:













```maxima
(%i1) S_1 : {a, b, c + d, %e};
(%o1)                   {%e, a, b, d + c}
(%i2) S_2 : {%pi, %i, %e, c + d};
(%o2)                 {%e, %i, %pi, d + c}
(%i3) S_3 : {17, 29, 1729, %pi, %i};
(%o3)                {17, 29, 1729, %i, %pi}
(%i4) union ();
(%o4)                          {}
(%i5) union (S_1);
(%o5)                   {%e, a, b, d + c}
(%i6) union (S_1, S_2);
(%o6)              {%e, %i, %pi, a, b, d + c}
(%i7) union (S_1, S_2, S_3);
(%o7)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
(%i8) union ({}, S_1, S_2, S_3);
(%o8)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
```

<!-- category: Combinatorics -->
<!-- keywords: xreduce -->
<!-- signatures: xreduce(F, s), xreduce(F, s, s_0) -->
### Function: xreduce (F, s)

合成によって関数*F*をn項関数に拡張します。
または、もし*F*が既にn項関数なら*F*を*s*に適用します。
*F*がn項関数でない時、
`xreduce`は`lreduce`と同じです。
引数*s*はリストです。


n項関数として知られている関数は、
足し算`+`, 掛け算`*`, `and`, `or`, `max`,
`min`, `append`を含みます。
関数は、
`declare(F, nary)`によってもn項と宣言されるかもしれません。
これらの関数に対して、
`xreduce`は
`rreduce`や`lreduce`よりも速いことが期待されます。


オプション引数*s_0*がある時、
結果は、`xreduce(s, cons(s_0, s))`と同値です。




浮動小数点の足し算は、厳密には結合的ではありません;
そうはそうかもしれませんが、
*s*が浮動小数点を含む時、
`xreduce`はMaximaのn項足し算を適用します。


例:


n項と知られている関数に適用された`xreduce`。
`F`は引数すべてで、一度コールされます。








```maxima
(%i1) declare (F, nary);
(%o1)                         done
(%i2) F ([L]) := L;
(%o2)                      F([L]) := L
(%i3) xreduce (F, [a, b, c, d, e]);
(%o3)         [[[[[("[", simp), a], b], c], d], e]
```


n項とわかっていない関数に適用された`xreduce`。
`G`は、
毎回２つの引数で複数回コールされます。








```maxima
(%i1) G ([L]) := L;
(%o1)                      G([L]) := L
(%i2) xreduce (G, [a, b, c, d, e]);
(%o2)         [[[[[("[", simp), a], b], c], d], e]
(%i3) lreduce (G, [a, b, c, d, e]);
(%o3)                 [[[[a, b], c], d], e]
```

