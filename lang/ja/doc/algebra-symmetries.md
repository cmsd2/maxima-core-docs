## Symmetries

<!-- category: Algebra -->
<!-- keywords: comp2pui -->
<!-- signatures: comp2pui(n, L) -->
### Function: comp2pui (n, L)

リスト*L*で与えられた与えられた完全対称関数から
0から*n*までの基本対称関数にパスすることを実装します。
もしリスト*L*が
*n+1*個より少ない要素を含むなら、
タイプ*h1*, *h2*などの
形式的な値で完成されます。
もし
リスト*L*の最初の要素が存在するなら、
それはアルファベットのサイズを指定します。
そうでないなら、サイズは*n*に設定されます。




```maxima
(%i1) comp2pui (3, [4, g]);
                        2                    2
(%o1)    [4, g, 2 h2 - g , 3 h3 - g h2 + g (g  - 2 h2)]
```

<!-- category: Algebra -->
<!-- keywords: cont2part -->
<!-- signatures: cont2part(pc, lvar) -->
### Function: cont2part (pc, lvar)

変数が*lvar*の中に含まれている短縮形*pc*に
関連付けられた分割多項式を返します。






```maxima
(%i1) pc: 2*a^3*b*x^4*y + x^5;
                           3    4      5
(%o1)                   2 a  b x  y + x


(%i2) cont2part (pc, [x, y]);
                                   3
(%o2)              [[1, 5, 0], [2 a  b, 4, 1]]
```

<!-- category: Algebra -->
<!-- keywords: direct -->
<!-- signatures: direct([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n]) -->
### Function: direct ([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n])

変数*lvar_1*, ..., *lvar_n*のリストと
変数*y*についての多項式*p_1*, ..., *p_n*に関して、
関数*f*に関連付けられた順像
(M. Giusti, D. Lazard et A. Valibouze,
ISSAC 1988, Romeを参照してください)
を計算します。
関数*f*のアリティが計算にとって重要です。
例えば、
*f*についての式がある変数に依存しないなら、
この変数を含むことは役に立たず、含めなければ、
計算量を相当に減らすことにもなるでしょう。









```maxima
(%i1) direct ([z^2  - e1* z + e2, z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]);
       2
(%o1) y  - e1 f1 y

                                 2            2             2   2
                  - 4 e2 f2 - (e1  - 2 e2) (f1  - 2 f2) + e1  f1
                + -----------------------------------------------
                                         2


(%i2) ratsimp (%);
              2                2                   2
(%o2)        y  - e1 f1 y + (e1  - 4 e2) f2 + e2 f1


(%i3) ratsimp (direct ([z^3-e1*z^2+e2*z-e3,z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]));
       6            5         2                        2    2   4
(%o3) y  - 2 e1 f1 y  + ((2 e1  - 6 e2) f2 + (2 e2 + e1 ) f1 ) y

                          3                               3   3
 + ((9 e3 + 5 e1 e2 - 2 e1 ) f1 f2 + (- 2 e3 - 2 e1 e2) f1 ) y

         2       2        4    2
 + ((9 e2  - 6 e1  e2 + e1 ) f2

                    2       2       2                   2    4
 + (- 9 e1 e3 - 6 e2  + 3 e1  e2) f1  f2 + (2 e1 e3 + e2 ) f1 )

  2          2                      2     3          2
 y  + (((9 e1  - 27 e2) e3 + 3 e1 e2  - e1  e2) f1 f2

                 2            2    3                5
 + ((15 e2 - 2 e1 ) e3 - e1 e2 ) f1  f2 - 2 e2 e3 f1 ) y

           2                   3           3     2   2    3
 + (- 27 e3  + (18 e1 e2 - 4 e1 ) e3 - 4 e2  + e1  e2 ) f2

         2      3                   3    2   2
 + (27 e3  + (e1  - 9 e1 e2) e3 + e2 ) f1  f2

                   2    4        2   6
 + (e1 e2 e3 - 9 e3 ) f1  f2 + e3  f1
```


根が和$a+u$である多項式を見つけること。
ただし、$a$は$z^2 - e_1 z + e_2$の根で、
$u$は$z^2 - f_1 z + f_2$の根です。






```maxima
(%i1) ratsimp (direct ([z^2 - e1* z + e2, z^2 - f1* z + f2],
                          z, a + u, [[u], [a]]));
       4                    3             2
(%o1) y  + (- 2 f1 - 2 e1) y  + (2 f2 + f1  + 3 e1 f1 + 2 e2

     2   2                              2               2
 + e1 ) y  + ((- 2 f1 - 2 e1) f2 - e1 f1  + (- 2 e2 - e1 ) f1

                  2                     2            2
 - 2 e1 e2) y + f2  + (e1 f1 - 2 e2 + e1 ) f2 + e2 f1  + e1 e2 f1

     2
 + e2
```


`direct`は２つのフラグを受け付けます:
`elementaires`と`puissances` (デフォルト)
これらは、計算の中に現れる対称多項式を
それぞれ基本対称関数またはべき関数に分解することを許します。


この関数で使われる`sym`の関数は以下の通りです:


`multi_orbit` (だから`orbit`), `pui_direct`, `multi_elem`
(だから`elem`), `multi_pui` (だから`pui`), `pui2ele`, `ele2pui`
(もしフラグ`direct`が`puissances`の中にあれば)。

<!-- category: Algebra -->
<!-- keywords: ele2comp -->
<!-- signatures: ele2comp(m, L) -->
### Function: ele2comp (m, L)

基本対称関数から完全関数に行きます。
`comp2ele`や`comp2pui`に似ています。


基数を変える他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: ele2polynome -->
<!-- signatures: ele2polynome(L, z) -->
### Function: ele2polynome (L, z)

根の基本対称関数が
リスト`L = [n, e_1, ..., e_n]`の中にあるような
*z*に関する多項式を返します。
ここで*n*は多項式の次数であり、
*e_i*は*i*番目の基本対称関数です。







```maxima
(%i1) ele2polynome ([2, e1, e2], z);
                          2
(%o1)                    z  - e1 z + e2


(%i2) polynome2ele (x^7 - 14*x^5 + 56*x^3  - 56*x + 22, x);
(%o2)          [7, 0, - 14, 0, 56, 0, - 56, - 22]


(%i3) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o3)            x  - 14 x  + 56 x  - 56 x + 22
```


The inverse: `polynome2ele (P, z)`.


Also see:
`polynome2ele`, `pui2polynome`.

<!-- category: Algebra -->
<!-- keywords: ele2pui -->
<!-- signatures: ele2pui(m, L) -->
### Function: ele2pui (m, L)

基本対称関数から完全関数に行きます。
`comp2ele`や`comp2comp`に似ています。


基数を変える他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: elem -->
<!-- signatures: elem(ele, sym, lvar) -->
### Function: elem (ele, sym, lvar)

リスト*lvar*に含まれる変数に関して、
リスト*ele*で与えられた基本対称関数を使って、
対称多項式*sym*を分解します。
もし*ele*の最初の要素が与えられたら、
アルファベットのサイズで、
そうでないなら、サイズは多項式*sym*の次数です。
もし値がリスト*ele*になければ、
タイプ*e1*, *e2*などの形式的値が加えられます。
多項式*sym*は３つの異なる形式で与えられます:
contracted (`elem`はその時、デフォルト値1であるべきです),
partitioned (`elem`は3であるべきです),または
extended(すなわち、多項式全体, かつ、`elem`は2であるべきです)。
関数`pui`は同じ方法で使われます。


サイズ3のアルファベットと値7を持つ最初の基本対称関数*e1*上で、
(ここで変数の２つにだけ依存する)短縮された形式が*x^4-2*x*y*である
3変数の対称多項式が以下のように基本対称関数で分解されます:






```maxima
(%i1) elem ([3, 7], x^4 - 2*x*y, [x, y]);
(%o1) 7 (e3 - 7 e2 + 7 (49 - e2)) + 21 e3

                                         + (- 2 (49 - e2) - 2) e2


(%i2) ratsimp (%);
                              2
(%o2)             28 e3 + 2 e2  - 198 e2 + 2401
```



基数を変える他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: explose -->
<!-- signatures: explose(pc, lvar) -->
### Function: explose (pc, lvar)

短縮形*pc*に関連付けられた対称多項式を返します。
リスト*lvar*は変数を含みます。





```maxima
(%i1) explose (a*x + 1, [x, y, z]);
(%o1)                  a z + a y + a x + 1
```

<!-- category: Algebra -->
<!-- keywords: kostka -->
<!-- signatures: kostka(part_1, part_2) -->
### Function: kostka (part_1, part_2)

P. Esperetによって書かれ、
分割*part_1*と*part_2*のKostka数を計算します。





```maxima
(%i1) kostka ([3, 3, 3], [2, 2, 2, 1, 1, 1]);
(%o1)                           6
```

<!-- category: Algebra -->
<!-- keywords: lgtreillis -->
<!-- signatures: lgtreillis(n, m) -->
### Function: lgtreillis (n, m)

重み*n*と長さ*m*の分割のリストを返します。





```maxima
(%i1) lgtreillis (4, 2);
(%o1)                   [[3, 1], [2, 2]]
```


以下も参照してください: `ltreillis`, `treillis`, `treinat`。

<!-- category: Algebra -->
<!-- keywords: ltreillis -->
<!-- signatures: ltreillis(n, m) -->
### Function: ltreillis (n, m)

重み*n*と*m*以下の長さの分割のリストを返します。





```maxima
(%i1) ltreillis (4, 2);
(%o1)               [[4, 0], [3, 1], [2, 2]]
```


以下も参照してください: `lgtreillis`, `treillis`, `treinat`。

<!-- category: Algebra -->
<!-- keywords: mon2schur -->
<!-- signatures: mon2schur(L) -->
### Function: mon2schur (L)

リスト*L*は
Schur関数$S_L$を表します:
 we have
$i_1 <= i_2 <= ... <= i_q$成る$L = [i_1, i_2, ..., i_q]$
を持ちます。
Schur関数$S_[i_1, i_2, ..., i_q]$は、
最初の$q$個の行と列$1 + i_1, 2 + i_2, ..., q + i_q$
から成る無限行列$h_[i-j]$, $i <= 1, j <= 1$
の小行列式です。



このSchur関数は
`treinat`と`kostka`を使うことで
単項式の項で書かれることができます。
返される形式は、
変数

$$
x_1,x_2,\ldots
$$

$x_1,x_2,...$
の短縮表現の対称多項式です。







```maxima
(%i1) mon2schur ([1, 1, 1]);
(%o1)                       x1 x2 x3


(%i2) mon2schur ([3]);
                                  2        3
(%o2)                x1 x2 x3 + x1  x2 + x1


(%i3) mon2schur ([1, 2]);
                                      2
(%o3)                  2 x1 x2 x3 + x1  x2
```



以上は、3つの変数に関してこれが与えることを意味します:




```maxima
2 x1 x2 x3 + x1^2 x2 + x2^2 x1 + x1^2 x3 + x3^2 x1
    + x2^2 x3 + x3^2 x2
```


基数を変えるための他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: multi_elem -->
<!-- signatures: multi_elem(l_elem, multi_pc, l_var) -->
### Function: multi_elem (l_elem, multi_pc, l_var)

*l_elem*に含まれる基本対称関数を使って、リスト*l_var*のリストに含まれる
変数のグループに関して、
多重対称多項式を
多重短縮形*multi_pc*に分解します。






```maxima
(%i1) multi_elem ([[2, e1, e2], [2, f1, f2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                                  3
(%o1)         - 2 f2 + f1 (f1 + e1) - 3 e1 e2 + e1


(%i2) ratsimp (%);
                         2                       3
(%o2)         - 2 f2 + f1  + e1 f1 - 3 e1 e2 + e1
```


基数を変えるための他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: multi_orbit -->
<!-- signatures: multi_orbit(P, [lvar_1, lvar_2, ..., lvar_p]) -->
### Function: multi_orbit (P, [lvar_1, lvar_2, ..., lvar_p])

*P*は
リスト*lvar_1*, *lvar_2*, ..., *lvar_p*に含まれる
変数の集合に関する
多項式です。
この関数は
これら*p*リストで表された変数の集合の対称群の積の作用の下で
多項式*P*の
軌道を返します。






```maxima
(%i1) multi_orbit (a*x + b*y, [[x, y], [a, b]]);
(%o1)                [b y + a x, a y + b x]


(%i2) multi_orbit (x + y + 2*a, [[x, y], [a, b, c]]);
(%o2)        [y + x + 2 c, y + x + 2 b, y + x + 2 a]
```


以下も参照してください: 単対称群の作用に関する`orbit`。

<!-- category: Algebra -->
<!-- keywords: multi_pui -->
<!-- signatures: multi_pui -->
### Function: multi_pui

関数`multi_elem`が関数`elem`に対するものであるように、
関数`pui`に対するものです。





```maxima
(%i1) multi_pui ([[2, p1, p2], [2, t1, t2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                            3
                                3 p1 p2   p1
(%o1)              t2 + p1 t1 + ------- - ---
                                   2       2
```

<!-- category: Algebra -->
<!-- keywords: multinomial -->
<!-- signatures: multinomial(r, part) -->
### Function: multinomial (r, part)

ここで*r*は分割*part*の重みです。
この関数は、同類の多項係数を返します:
もし*part*の部分が
*i_1*, *i_2*, ..., *i_k*なら、
結果は
`r!/(i_1! i_2! ... i_k!)`
です。

<!-- category: Algebra -->
<!-- keywords: multsym -->
<!-- signatures: multsym(ppart_1, ppart_2, n) -->
### Function: multsym (ppart_1, ppart_2, n)

次数*n*の対称群の作用を法としてのみ働くことで、
*n*個の変数に関する２つの対称多項式の積を返します。
多項式は分割形式です。


*x*, *y*に関する鵜２つの対称多項式:
分割形式が`[[3, 1], [2, 1, 1]]`と`[[5, 2]]`である
`3*(x + y) + 2*x*y`と`5*(x^2 + y^2)`
が与えられたとして、それらの積は、





```maxima
(%i1) multsym ([[3, 1], [2, 1, 1]], [[5, 2]], 2);
(%o1)         [[10, 3, 1], [15, 3, 0], [15, 2, 1]]
```


、すなわち、`10*(x^3*y + y^3*x) + 15*(x^2*y + y^2*x) + 15*(x^3 + y^3)`です。


対称多項式の表現を変える関数は以下の通りです:


`contract`, `cont2part`, `explose`, `part2cont`,
`partpol`, `tcontract`, `tpartpol`。

<!-- category: Algebra -->
<!-- keywords: orbit -->
<!-- signatures: orbit(P, lvar) -->
### Function: orbit (P, lvar)

リスト*lvar*の変数の集合の対称群の作用の下で
リスト*lvar*の変数に関する多項式*P*の軌道を計算します。






```maxima
(%i1) orbit (a*x + b*y, [x, y]);
(%o1)                [a y + b x, b y + a x]


(%i2) orbit (2*x + x^2, [x, y]);
                        2         2
(%o2)                 [y  + 2 y, x  + 2 x]
```


多項式に関する対称群の積の作用に関しては`multi_orbit`も参照してください。

<!-- category: Algebra -->
<!-- keywords: part2cont -->
<!-- signatures: part2cont(ppart, lvar) -->
### Function: part2cont (ppart, lvar)

対称式を分割形から短縮形に変換します。
短縮形は*lvar*の中の変数で表されます。





```maxima
(%i1) part2cont ([[2*a^3*b, 4, 1]], [x, y]);
                              3    4
(%o1)                      2 a  b x  y
```

<!-- category: Algebra -->
<!-- keywords: partpol -->
<!-- signatures: partpol(psym, lvar) -->
### Function: partpol (psym, lvar)

*psym*は
リスト*lvar*の変数に関する対称多項式です。
この関数は分割表現を返します。





```maxima
(%i1) partpol (-a*(x + y) + 3*x*y, [x, y]);
(%o1)               [[3, 1, 1], [- a, 1, 0]]
```

<!-- category: Algebra -->
<!-- keywords: permut -->
<!-- signatures: permut(L) -->
### Function: permut (L)

リスト*L*の置換のリストを返します。

<!-- category: Algebra -->
<!-- keywords: polynome2ele -->
<!-- signatures: polynome2ele(P, x) -->
### Function: polynome2ele (P, x)

リスト`l = [n, e_1, ..., e_n]`を与えます。
ここで*n*は
変数*x*に関する多項式*P*の次数であり、
*e_i*は
*P*の根の*i*番目の基本対称関数です。






```maxima
(%i1) polynome2ele (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x);
(%o1)          [7, 0, - 14, 0, 56, 0, - 56, - 22]


(%i2) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o2)            x  - 14 x  + 56 x  - 56 x + 22
```


逆: `ele2polynome (l, x)`

<!-- category: Algebra -->
<!-- keywords: prodrac -->
<!-- signatures: prodrac(L, k) -->
### Function: prodrac (L, k)

*L*は
集合*A*上の基本対称関数を含む
リストです。
`prodrac`は、
根が
*A*の要素の
*k*掛ける*k*の積の
多項式を返します。


`somrac`も参照してください。

<!-- category: Algebra -->
<!-- keywords: pui -->
<!-- signatures: pui(L, sym, lvar) -->
### Function: pui (L, sym, lvar)

リスト*L*の中のべき関数を使って、
リスト*lvar*の中の変数に関して、
対称多項式*sym*を分解します。
もし*L*の最初の要素が与えられるなら、
アルファベットのサイズです。
そうでないなら、サイズは多項式*sym*の次数になります。
もしリスト*L*の中に値がないなら、
タイプ*p1*, *p2* , などの形式的な値が加えられます。
多項式*sym*は、
３つの異なる形式で与えられることができます:
contracted (`elem`は1でなければならず、デフォルト値です),
partitioned (`elem`は3でなければいけません),
extended (すなわち、多項式全体、そして`elem`は2でなければいけません)。
関数`pui`は同じ方法で使われます。







```maxima
(%i1) pui;
(%o1)                           1


(%i2) pui ([3, a, b], u*x*y*z, [x, y, z]);
                       2
                   a (a  - b) u   (a b - p3) u
(%o2)              ------------ - ------------
                        6              3


(%i3) ratsimp (%);
                                       3
                      (2 p3 - 3 a b + a ) u
(%o3)                 ---------------------
                                6
```


Other functions for changing bases: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: pui2comp -->
<!-- signatures: pui2comp(n, lpui) -->
### Function: pui2comp (n, lpui)

リスト*lpui*で与えられたべき関数を使って、
(最初に長さを持ち)最初の*n*個の完全関数のリストを返します。
もしリスト*lpui*が空なら、
基数は*n*で、
そうでないなら、基数は(`comp2ele`や`comp2pui`同様)
最初の要素です。







```maxima
(%i1) pui2comp (2, []);
                                       2
                                p2 + p1
(%o1)                   [2, p1, --------]
                                   2


(%i2) pui2comp (3, [2, a1]);
                                            2
                                 a1 (p2 + a1 )
                         2  p3 + ------------- + a1 p2
                  p2 + a1              2
(%o2)     [2, a1, --------, --------------------------]
                     2                  3


(%i3) ratsimp (%);
                            2                     3
                     p2 + a1   2 p3 + 3 a1 p2 + a1
(%o3)        [2, a1, --------, --------------------]
                        2               6
```


基数を変えるための他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: pui2ele -->
<!-- signatures: pui2ele(n, lpui) -->
### Function: pui2ele (n, lpui)

べき関数から基本対称関数への変転に影響します。
もしフラグ`pui2ele`が`girard`なら、
1から*n*までの基本対称関数のリストを返し、
もしフラグが`close`なら、
*n*番目の基本対称関数を返します。


基数を変えるための他の関数: `comp2ele`.

<!-- category: Algebra -->
<!-- keywords: pui2polynome -->
<!-- signatures: pui2polynome(x, lpui) -->
### Function: pui2polynome (x, lpui)

根のべき関数がリスト*lpui*で与えられる
*x*に関する多項式を計算します。







```maxima
(%i1) pui;
(%o1)                           1


(%i2) kill(labels);
(%o0)                         done


(%i1) polynome2ele (x^3 - 4*x^2 + 5*x - 1, x);
(%o1)                     [3, 4, 5, 1]


(%i2) ele2pui (3, %);
(%o2)                     [3, 4, 6, 7]


(%i3) pui2polynome (x, %);
                        3      2
(%o3)                  x  - 4 x  + 5 x - 1
```


以下も参照してください:
`polynome2ele`, `ele2polynome`。

<!-- category: Algebra -->
<!-- keywords: pui_direct -->
<!-- signatures: pui_direct(orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n]) -->
### Function: pui_direct (orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n])

*f*を
変数の*n*個のブロック*lvar_1*, ..., *lvar_n*に関する多項式とします。
*c_i*を
*lvar_i*の中の変数の数とし、
*SC*を
次数*c_1*, ..., *c_n*の
*n*個の対称群の積とします。
この群は自然に*f*に作用します。
リスト*orbite*は
*SC*の作用の下での関数*f*の軌道で、`SC(f)`を意味します。
(このリストは
関数`multi_orbit`によって得られます。)
*di*は
$c_1 <= d_1, c_2 <= d_2, ..., c_n <= d_n$.
を満たすような整数です。


*SD*を
対称群
$S_[d_1] x S_[d_2] x ... x S_[d_n]$
の積とします。
関数`pui_direct`は
`SC(f)`のべき関数から演繹された
`SD(f)`の
最初の*n*個のべき関数を返します。
ここで、*n*は`SD(f)`のサイズです。


結果は*SD*に関する多重短縮された形式です。
すなわち、*SD*の作用の下で、軌道毎にただ１つの要素が保持されます。









```maxima
(%i1) l: [[x, y], [a, b]];
(%o1)                   [[x, y], [a, b]]


(%i2) pui_direct (multi_orbit (a*x + b*y, l), l, [2, 2]);
                                       2  2
(%o2)               [a x, 4 a b x y + a  x ]


(%i3) pui_direct (multi_orbit (a*x + b*y, l), l, [3, 2]);
                             2  2     2    2        3  3
(%o3) [2 a x, 4 a b x y + 2 a  x , 3 a  b x  y + 2 a  x , 

    2  2  2  2      3    3        4  4
12 a  b  x  y  + 4 a  b x  y + 2 a  x , 

    3  2  3  2      4    4        5  5
10 a  b  x  y  + 5 a  b x  y + 2 a  x , 

    3  3  3  3       4  2  4  2      5    5        6  6
40 a  b  x  y  + 15 a  b  x  y  + 6 a  b x  y + 2 a  x ]


(%i4) pui_direct ([y + x + 2*c, y + x + 2*b, y + x + 2*a],
      [[x, y], [a, b, c]], [2, 3]);
                             2              2
(%o4) [3 x + 2 a, 6 x y + 3 x  + 4 a x + 4 a , 

                 2                   3        2       2        3
              9 x  y + 12 a x y + 3 x  + 6 a x  + 12 a  x + 8 a ]
```

<!-- category: Algebra -->
<!-- keywords: puireduc -->
<!-- signatures: puireduc(n, lpui) -->
### Function: puireduc (n, lpui)

*lpui*は
最初の要素が整数*m*のリストです。
`puireduc`は
最初の*m*個を使って最初の*n*個のべき関数を与えます。





```maxima
(%i1) puireduc (3, [2]);
                                         2
                                   p1 (p1  - p2)
(%o1)          [2, p1, p2, p1 p2 - -------------]
                                         2


(%i2) ratsimp (%);
                                           3
                               3 p1 p2 - p1
(%o2)              [2, p1, p2, -------------]
                                     2
```

<!-- category: Algebra -->
<!-- keywords: resolvante -->
<!-- signatures: resolvante(P, x, f, [x_1, ..., x_d]) -->
### Function: resolvante (P, x, f, [x_1, ..., x_d])

変数*x_1*, ..., *x_d*で表現された関数*f*によって
次数*n* >= *d*の
*x*に関する多項式*P*
の解核を計算します。
計算の効率のため、
変換関数*f*に現れない変数の
リスト`[x_1, ..., x_d]`に含まれないことが重要です。


計算の効率を増すためには、
適切なアルゴリズムを使うように
`resolvante`に関するフラグを設定することができます:


もし関数*f*がユニタリなら:


- *
単変数の多項式,
- *
  
線形,
- *
  
交互の,
- *
  
和,
- *
  
対照的,
- *
  
積,
- *
(次数5まで使用に向く)Cayley解核の関数 


```maxima
(x1*x2 + x2*x3 + x3*x4 + x4*x5 + x5*x1 -
     (x1*x3 + x3*x5 + x5*x2 + x2*x4 + x4*x1))^2
```

一般的,

`resolvante`のフラグはそれぞれ:


- *
  
unitaire,
- *
  
lineaire,
- *
  
alternee,
- *
  
somme,
- *
  
produit,
- *
  
cayley,
- *
  
generale.

























```maxima
(%i1) resolvante: unitaire$

(%i2) resolvante (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x, x^3 - 1,
      [x]);

" resolvante unitaire " [7, 0, 28, 0, 168, 0, 1120, - 154, 7840,
                         - 2772, 56448, - 33880, 

413952, - 352352, 3076668, - 3363360, 23114112, - 30494464, 

175230832, - 267412992, 1338886528, - 2292126760] 
  3       6      3       9      6      3
[x  - 1, x  - 2 x  + 1, x  - 3 x  + 3 x  - 1, 

 12      9      6      3       15      12       9       6      3
x   - 4 x  + 6 x  - 4 x  + 1, x   - 5 x   + 10 x  - 10 x  + 5 x

       18      15       12       9       6      3
 - 1, x   - 6 x   + 15 x   - 20 x  + 15 x  - 6 x  + 1, 

 21      18       15       12       9       6      3
x   - 7 x   + 21 x   - 35 x   + 35 x  - 21 x  + 7 x  - 1] 
[- 7, 1127, - 6139, 431767, - 5472047, 201692519, - 3603982011] 
       7      6        5         4          3           2
(%o2) y  + 7 y  - 539 y  - 1841 y  + 51443 y  + 315133 y

                                              + 376999 y + 125253

(%i3) resolvante: lineaire$

(%i4) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante lineaire " 
       24       20         16            12             8
(%o4) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i5) resolvante: general$

(%i6) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante generale " 
       24       20         16            12             8
(%o6) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i7) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3, x4]);

" resolvante generale " 
       24       20         16            12             8
(%o7) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i8) direct ([x^4 - 1], x, x1 + 2*x2 + 3*x3, [[x1, x2, x3]]);
       24       20         16            12             8
(%o8) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i9) resolvante :lineaire$

(%i10) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante lineaire " 
                              4
(%o10)                       y  - 1

(%i11) resolvante: symetrique$

(%i12) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante symetrique " 
                              4
(%o12)                       y  - 1


(%i13) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante symetrique " 
                           6      2
(%o13)                    y  - 4 y  - 1

(%i14) resolvante: alternee$

(%i15) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante alternee " 
            12      8       6        4        2
(%o15)     y   + 8 y  + 26 y  - 112 y  + 216 y  + 229

(%i16) resolvante: produit$

(%i17) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante produit "
        35      33         29        28         27        26
(%o17) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i18) resolvante: symetrique$

(%i19) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante symetrique " 
        35      33         29        28         27        26
(%o19) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i20) resolvante: cayley$

(%i21) resolvante (x^5 - 4*x^2 + x + 1, x, a, []);

" resolvante de Cayley "
        6       5         4          3            2
(%o21) x  - 40 x  + 4080 x  - 92928 x  + 3772160 x  + 37880832 x

                                                       + 93392896
```


Cayley解核に関して、最後の2つの引数は中立で、
入力多項式は必然的に次数5でなければいけません。


以下も参照してください:


`resolvante_bipartite`, `resolvante_produit_sym`,
`resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, 
`resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: resolvante_alternee1 -->
<!-- signatures: resolvante_alternee1(P, x) -->
### Function: resolvante_alternee1 (P, x)

関数
$product(x_i - x_j, 1 <= i < j <= n - 1)$.
によって
次数*n*の
変換`P(x)`を計算します。
以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante` , `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_bipartite`。

<!-- category: Algebra -->
<!-- keywords: resolvante_bipartite -->
<!-- signatures: resolvante_bipartite(P, x) -->
### Function: resolvante_bipartite (P, x)

関数
によって
偶次数*n*の`P(x)`の変換を計算します。


$x_1 x_2 ... x_[n/2] + x_[n/2 + 1] ... x_n$.





```maxima
(%i1) resolvante_bipartite (x^6 + 108, x);
              10        8           6             4
(%o1)        y   - 972 y  + 314928 y  - 34012224 y
```


以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_alternee1`.

<!-- category: Algebra -->
<!-- keywords: resolvante_diedrale -->
<!-- signatures: resolvante_diedrale(P, x) -->
### Function: resolvante_diedrale (P, x)

関数`x_1 x_2 + x_3 x_4`によって
`P(x)`の変換を計算します。





```maxima
(%i1) resolvante_diedrale (x^5 - 3*x^4 + 1, x);
       15       12       11       10        9         8         7
(%o1) x   - 21 x   - 81 x   - 21 x   + 207 x  + 1134 x  + 2331 x

        6         5          4          3          2
 - 945 x  - 4970 x  - 18333 x  - 29079 x  - 20745 x  - 25326 x

 - 697
```


以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante`。

<!-- category: Algebra -->
<!-- keywords: resolvante_klein -->
<!-- signatures: resolvante_klein(P, x) -->
### Function: resolvante_klein (P, x)

関数`x_1 x_2 x_4 + x_4`によって
`P(x)`の変換を計算します。


以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: resolvante_klein3 -->
<!-- signatures: resolvante_klein3(P, x) -->
### Function: resolvante_klein3 (P, x)

関数`x_1 x_2 x_4 + x_4`によって
`P(x)`の変換を計算します。


以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante`,
`resolvante_vierer`, `resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: resolvante_produit_sym -->
<!-- signatures: resolvante_produit_sym(P, x) -->
### Function: resolvante_produit_sym (P, x)

多項式`P(x)`のすべての積解核のリストを計算します。







```maxima
(%i1) resolvante_produit_sym (x^5 + 3*x^4 + 2*x - 1, x);
        5      4             10      8       7       6       5
(%o1) [y  + 3 y  + 2 y - 1, y   - 2 y  - 21 y  - 31 y  - 14 y

    4       3      2       10      8       7    6       5       4
 - y  + 14 y  + 3 y  + 1, y   + 3 y  + 14 y  - y  - 14 y  - 31 y

       3      2       5      4
 - 21 y  - 2 y  + 1, y  - 2 y  - 3 y - 1, y - 1]

(%i2) resolvante: produit$

(%i3) resolvante (x^5 + 3*x^4 + 2*x - 1, x, a*b*c, [a, b, c]);

" resolvante produit "
       10      8       7    6        5       4       3     2
(%o3) y   + 3 y  + 14 y  - y  - 14 y  - 31 y  - 21 y  - 2 y  + 1
```





以下も参照してください:


`resolvante`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`,
`resolvante_klein3`, `resolvante_vierer`,
`resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: resolvante_unitaire -->
<!-- signatures: resolvante_unitaire(P, Q, x) -->
### Function: resolvante_unitaire (P, Q, x)

多項式`Q(x)`によって
多項式`P(x)`の解核を計算します。


以下も参照してください:


`resolvante_produit_sym`, `resolvante`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: resolvante_vierer -->
<!-- signatures: resolvante_vierer(P, x) -->
### Function: resolvante_vierer (P, x)

関数`x_1 x_2 - x_3 x_4`によって
`P(x)`の変換を計算します。


以下も参照してください:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante`, `resolvante_diedrale`。

<!-- category: Algebra -->
<!-- keywords: schur2comp -->
<!-- signatures: schur2comp(P, l_var) -->
### Function: schur2comp (P, l_var)

*P*はリスト*l_var*の変数の多項式です。
これらの変数のそれぞれは完全対称関数を表します。
*l_var*の中で、
*i*番目の完全対称関数は
文字`h`と整数*i*の連結`hi`によって表されます。
この関数は
*P*をSchur関数を使って表現します。







```maxima
(%i1) schur2comp (h1*h2 - h3, [h1, h2, h3]);
(%o1)                         s
                               1, 2


(%i2) schur2comp (a*h3, [h3]);
(%o2)                         s  a
                               3
```

<!-- category: Algebra -->
<!-- keywords: somrac -->
<!-- signatures: somrac(L, k) -->
### Function: somrac (L, k)

リスト*L*は
多項式*P*の基本対称関数を含みます。
関数は
根が*P*の根の*k*掛ける*k*の別個の和である
多項式を計算します。


`prodrac`も参照してください。

<!-- category: Algebra -->
<!-- keywords: tcontract -->
<!-- signatures: tcontract(pol, lvar) -->
### Function: tcontract (pol, lvar)

多項式*pol*が
リスト*lvar*の変数に関して対称かテストします。
もしそうなら、関数`contract`のように短縮表現を返します。

<!-- category: Algebra -->
<!-- keywords: tpartpol -->
<!-- signatures: tpartpol(pol, lvar) -->
### Function: tpartpol (pol, lvar)

多項式*pol*が
リスト*lvar*の中の変数に関して
対称かテストします。
もしそうなら
関数`partpol`のように
分割表現を返します。

<!-- category: Algebra -->
<!-- keywords: treillis -->
<!-- signatures: treillis(n) -->
### Function: treillis (n)

重み*n*の分割すべてを返します。





```maxima
(%i1) treillis (4);
(%o1)    [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
```


以下も参照してください: `lgtreillis`, `ltreillis`, `treinat`。

<!-- category: Algebra -->
<!-- keywords: treinat -->
<!-- signatures: treinat(part) -->
### Function: treinat (part)

自然な順序に関する分割*part*より低い分割のリストを返します。







```maxima
(%i1) treinat ([5]);
(%o1)                         [[5]]


(%i2) treinat ([1, 1, 1, 1, 1]);
(%o2) [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], 

                                                 [1, 1, 1, 1, 1]]


(%i3) treinat ([3, 2]);
(%o3)                 [[5], [4, 1], [3, 2]]
```


以下も参照してください: `lgtreillis`, `ltreillis`, `treillis`。

