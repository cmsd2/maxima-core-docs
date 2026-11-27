## simplification

<!-- category: Simplification -->
<!-- keywords: agd -->
<!-- signatures: agd(x) -->
### Function: agd (x)

逆Gudermannian函数`log (tan (%pi/4 + x/2)))`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: arithmetic -->
<!-- signatures: arithmetic(a, d, n) -->
### Function: arithmetic (a, d, n)

算術級数`a, a + d, a + 2*d, ..., a + (n - 1)*d`の第*n*項を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: arithsum -->
<!-- signatures: arithsum(a, d, n) -->
### Function: arithsum (a, d, n)

算術級数の1から*n*までの和を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: collectterms -->
<!-- signatures: collectterms(expr, arg_1, ..., arg_n) -->
### Function: collectterms (expr, arg_1, ..., arg_n)

もしいくつかの式が`facsum`もしくは`factorfacsum`, `factenexpand`, `facexpten`,
 `factorfacexpten`で整理されていて、それらが一緒に加算されているなら、
関数`collectterms`を使ってそれらを結合することが望まれる場合があります。
`collectterms`は、`nextlayerfactor`を除いてこれらの他の関連した関数に渡すことができる引数すべてを
引数として取ることができます。
`collectterms`の利点は、`facsum`と似た形式を返すことです。
しかし、既に`facsum`で処理された加算形式なのでこの処理を繰り返す必要はありません。
この能力は加算する式が非常に大きい時特に役立ちます。

<!-- category: Simplification -->
<!-- keywords: combination -->
<!-- signatures: combination(n, r) -->
### Function: combination (n, r)

一度に*r*個を取る*n*個のオブジェクトの組み合わせの数を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: covers -->
<!-- signatures: covers(x) -->
### Function: covers (x)

余矢(よし)`1 - sin (x)`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: exsec -->
<!-- signatures: exsec(x) -->
### Function: exsec (x)

外正割(exsecant)`sec (x) - 1`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: facsum -->
<!-- signatures: facsum(expr, arg_1, ..., arg_n) -->
### Function: facsum (expr, arg_1, ..., arg_n)

引数*arg_1*, ..., *arg_n*に依存する
*expr*の形式を返します。
引数は`ratvars`に適した任意の形式か、そんな形式のリストを取り得ます。
もし引数がリストでなければ、
返される形式は、引数に関して完全に展開され、引数の係数は因数分解されます。
これらの係数は、非合理的な意味合いを除いて引数に依存しません。


引数のいずれかがリストなら、リストすべては1つのリストに結合されて、
引数の係数に対して`factor`をコールする代わりに
`facsum`は、
これらの係数に対して自分自身をコールします。
この再帰コールに関しては、上記で新しく構成されたリストが新しい引数リストとして使われます。
この処理は、リストの中に望まれた要素を入れ子にすることで、任意の深さまで繰り返すことができます。



It is possible that one may wish to `facsum` with respect  to more
complicated subexpressions,  such as  
`log (x + y)`のような、より複雑な部分式に関して
`facsum`したいかも知れません。
そんな引数も許されています。







時々、ユーザーは
式に関して、先頭演算子によってのみ指定された上記形式いずれかが欲しいかもしれません。
例えば、
すべての`log`に関して`facsum`したかもしれません。
この場合、
この方法で扱われる特定の`log`か、
代わりに式`operator (log)`や`'operator (log)`
を引数に含むことができます。
もし
演算子*op_1*, ..., *op_n*に関して
式*expr*を`facsum`したいなら、
`facsum (expr, operator (op_1, ..., op_n))`を評価します。
`operator`形式はリスト引数の中でも可能です。


更に、
スイッチ`facsum_combine`と`nextlayerfactor`の設定は
`facsum`の結果に影響するかもしれません。

<!-- category: Simplification -->
<!-- keywords: facsum_combine -->
<!-- signatures: facsum_combine -->
### Variable: facsum_combine

デフォルト値: `true`


引数が多項式の商の時、
`facsum_combine`は
`facsum`が返す最終結果の形式を制御します。
もし`facsum_combine`が`false`なら、
形式は既に記述したような完全に展開された和として返されますが、
もし`true`なら、
返される式は、既に記述した形式の多項式の比です。


有理式の分子と分母両方を`facsum`したいが、
分母が分子の項ずつに掛けられたくない時、
このスイッチの`true`設定は役に立ちます。

<!-- category: Simplification -->
<!-- keywords: factorfacsum -->
<!-- signatures: factorfacsum(expr, arg_1, ...arg_n) -->
### Function: factorfacsum (expr, arg_1, ...arg_n)

*expr*の因子に関して引数として
*arg_1*, ... *arg_n*を付けて`facsum`をコールすることで得られる
*expr*の形式を返します。
もし*expr*の因子のいずれかがべきに累乗されるなら、
因子と指数と両方がこの方法で処理されます。

<!-- category: Simplification -->
<!-- keywords: gaussprob -->
<!-- signatures: gaussprob(x) -->
### Function: gaussprob (x)

Gaussian確率函数`%e^(-x^2/2) / sqrt(2*%pi)`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: gcdivide -->
<!-- signatures: gcdivide(p, q) -->
### Function: gcdivide (p, q)

`takegcd`が`true`の時、
`gcdivide`は多項式*p*と*q*を最大公約多項式で割り、
結果の比を返します。


`takegcd`が`false`の時、
`gcdivide`は比`p/q`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。


`ezgcd`, `gcd`, `gcdex`, `poly_gcd`も参照してください。


例:



```maxima
(%i1) load("functs")$

(%i2) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o2)                6 x  + 19 x  + 19 x + 6
(%i3) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o3)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i4) gcdivide(p1, p2);
                             x + 1
(%o4)                        ------
                              3
                             x  + x
(%i5) takegcd:false;
(%o5)                         false
(%i6) gcdivide(p1, p2);
                       3       2
                    6 x  + 19 x  + 19 x + 6
(%o6)          ----------------------------------
                  5       4       3       2
               6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i7) ratsimp(%);
                             x + 1
(%o7)                        ------
                              3
                             x  + x
```

See also: `ezgcd`, `gcd`, `gcdex`, `poly_gcd`.

<!-- category: Simplification -->
<!-- keywords: gcfac -->
<!-- signatures: gcfac(expr) -->
### Function: gcfac (expr)

`gcfac`は
科学者が式をより簡単にしようとする時に適用するのと同じ発見的方法の適用を試みる
因数分解関数です。
`gcfac`は単項式タイプの因数分解に限られます。
和に関しては、`gcfac`は以下を行います:



1. 整数上で素因数分解します。
2. 項の複雑さに関わらず、生じる項の最大の冪を係数として因数分解します。
3. 項の隣同士の対を因数分解する時に、(1)と(2)を使います。
4. 式がもはや変化しなくなるまで、
これらのテクニックを繰り返し、再帰的に適用します。


対のすべての可能な再配列の中から最も簡潔な対因数分解された結果を産むものを見つけることの
組み合わせ的に困難な性質のため、
項目(3)は必ずしも、対での因数分解の最善の仕事をしません。


`load ("scifac")`はこの関数をロードします。
`demo (scifac)`はこの関数のデモを見せます。

<!-- category: Simplification -->
<!-- keywords: gd -->
<!-- signatures: gd(x) -->
### Function: gd (x)

Gudermannian函数`2*atan(%e^x)-%pi/2`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: geometric -->
<!-- signatures: geometric(a, r, n) -->
### Function: geometric (a, r, n)

幾何級数`a, a*r, a*r^2, ..., a*r^(n - 1)`の第*n*項を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: geosum -->
<!-- signatures: geosum(a, r, n) -->
### Function: geosum (a, r, n)

幾何級数の1から*n*までの和を返します。
もし*n*が無限大(`inf`)なら、
*r*の絶対値が1未満でのみ、和は有限です。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: harmonic -->
<!-- signatures: harmonic(a, b, c, n) -->
### Function: harmonic (a, b, c, n)

調和級数`a/b, a/(b + c), a/(b + 2*c), ..., a/(b + (n - 1)*c)`の第*n*項を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: hav -->
<!-- signatures: hav(x) -->
### Function: hav (x)

半正矢`(1 - cos(x))/2`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: nextlayerfactor -->
<!-- signatures: nextlayerfactor -->
### Variable: nextlayerfactor

デフォルト値: `false`


`nextlayerfactor`が`true`の時、
`facsum`の再帰コールが
引数の係数の因数分解された形式の因子に適用されます。


`false`の時、
`facsum`は、
`facsum`への再帰コールが起こる時はいつでも、全体としてそれぞれの係数に適用されます。



`facsum`の引数リストに
アトム`nextlayerfactor`を入れると、
`nextlayerfactor: true`の効果がありますが、
式の次のレベル*だけ*に関してです。


`nextlayerfactor`はいつも
`true`か`false`にバインドされているので、
`facsum`の引数リストの中に現れる時はいつでも、
シングルクォートで表さなければいけません。

<!-- category: Simplification -->
<!-- keywords: nonzeroandfreeof -->
<!-- signatures: nonzeroandfreeof(x, expr) -->
### Function: nonzeroandfreeof (x, expr)

もし *expr*がゼロでなく、
`freeof (x, expr)`が`true`を返すなら、
`true`を返します。
そうでなければ、`false`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: permutation -->
<!-- signatures: permutation(n, r) -->
### Function: permutation (n, r)

*n*個のオブジェクトの集合から選択された*r*個のオブジェクトの置換の数を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: rational -->
<!-- signatures: rational(z) -->
### Function: rational (z)

分母を有理化するように、
*z*の分子と分母に分母の複素共役を掛けます。
もし与えられたものがそうであれば、正準有理式(CRE)形式を返し、
そうでないなら、一般形式を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: reduce_consts -->
<!-- signatures: reduce_consts(expr) -->
### Function: reduce_consts (expr)

*expr*の定部分式を構成された定アトムで置き換え、
これら構成された定数すべての定義を等式のリスト`const_eqns`に保存し、
修正された*expr*を返します。
*expr*のそれらのパーツは、関数`constantp`が施された時`true`を返す
定数です。
それゆえ、
`reduce_consts`を呼び出す前に、


```maxima
declare ([objects to be given the constant property], constant)$
```

をして、自分の式に現れる定数量のデータベースを設定すべきです。


もしこれらの数式計算の後、Fortran出力を生成する予定があるなら、
最初のコードセクションの1つはすべての定数の計算であるべきです。
このコードセグメントを生成するには、


```maxima
map ('fortran, const_eqns)$
```

を実行してください。


`reduce_consts`に影響する`const_eqns`
を除いた変数は以下の通りです:
`const_prefix` (デフォルト値: `xx`)
定部分式を表すために`reduce_consts`が生成するシンボルすべてに接頭として付けるのに使われる文字列です。


`const_counter` (デフォルト値: 1)は
`reduce_consts`が見つける定部分式それぞれを表すためのユニークなシンボルを生成するのに使われる整数添字です。


`load ("rducon")`はこの関数をロードします。
`demo (rducon)`はこの関数のデモを見せます。

<!-- category: Simplification -->
<!-- keywords: rempart -->
<!-- signatures: rempart(expr, n) -->
### Function: rempart (expr, n)

式*expr*からパーツ*n*を取り除きます。


もし*n*が形式`[l, m]`のリストなら、
パーツ*l*から*m*までが取り除かれます。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: sqrtdenest -->
<!-- signatures: sqrtdenest(expr) -->
### Function: sqrtdenest (expr)

可能なら、簡単で、数値的で、二項無理数(binomial surds)の`sqrt`をdenestします。


例えば、








```maxima
(%i1) load ("sqdnst")$
(%i2) sqrt(sqrt(3)/2+1)/sqrt(11*sqrt(2)-12);
                                    sqrt(3)
                               sqrt(------- + 1)
                                       2
(%o2)                        ---------------------
                             sqrt(11 sqrt(2) - 12)
(%i3) sqrtdenest(%);
                                  sqrt(3)   1
                                  ------- + -
                                     2      2
(%o3)                            -------------
                                    1/4    3/4
                                 3 2    - 2
```


時々、
`(19601-13860 sqrt(2))^(7/4)`に対してのように、
`sqrtdenest`を複数回適用することが役立ちます。


`load ("sqdnst")`はこの関数をロードします。

<!-- category: Simplification -->
<!-- keywords: tracematrix -->
<!-- signatures: tracematrix(M) -->
### Function: tracematrix (M)

行列*M*の跡(対角要素の和)を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: vers -->
<!-- signatures: vers(x) -->
### Function: vers (x)

正矢(せいし)`1 - cos (x)`を返します。


この関数を使うには、最初に`load("functs")`を書いてください。

<!-- category: Simplification -->
<!-- keywords: wronskian -->
<!-- signatures: wronskian([f_1, ..., f_n], x) -->
### Function: wronskian ([f_1, ..., f_n], x)

変数*x*に関する式のリスト[*f_1*, ..., *f_n*]の
Wronskian行列を返します。
Wronskian行列の行列式は、
式のリストのWronskian行列式です。


`wronskian`を使うには、最初に`load("functs")`してください。例えば:







```maxima
(%i1) load("functs")$
(%i2) wronskian([f(x), g(x)],x);
(%o2) matrix([f(x),g(x)],['diff(f(x),x,1),'diff(g(x),x,1)])
```

