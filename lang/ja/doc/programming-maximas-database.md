## Maximas Database

<!-- category: Programming -->
<!-- keywords: activate -->
<!-- signatures: activate(context_1, ..., context_n) -->
### Function: activate (context_1, ..., context_n)

文脈*context_1*, ..., *context_n*をアクティベートします。
これらの文脈に関する事実は、演繹し情報を検索するために利用可能となります。
これらの文脈に関する事実は、`facts ()`によってリストされません。


変数`activecontexts`は、
`activate`関数を使ってアクティブになった文脈のリストです。

<!-- category: Programming -->
<!-- keywords: activecontexts -->
<!-- signatures: activecontexts -->
### Variable: activecontexts

デフォルト値: `[]`


変数`activecontexts`は、
アクティブである文脈と対照的に、
`activate`関数を使ってアクティブになった文脈のリストです。
ゆえに、それらは現在の文脈の部分文脈です。

<!-- category: Programming -->
<!-- keywords: askexp -->
<!-- signatures: askexp -->
### Variable: askexp

`asksign`がコールされた時、
`askexp`は、`asksign`がテストしている式です。


以前は、control-AでMaximaブレイクに入ることによって、
ユーザーが`askexp`を検査することができました。

<!-- category: Programming -->
<!-- keywords: askinteger -->
<!-- signatures: askinteger(expr, integer), askinteger(expr), askinteger(expr, even), askinteger(expr, odd) -->
### Function: askinteger (expr, integer)

`askinteger (expr, integer)`は、
`assume`データベースから、*expr*が整数かどうかを決定しようとします。
そうでなく、もし決定できなければ、`askinteger`はユーザーに入力を促し、


可能ならばデータベースに情報をインストールしようとします。
`askinteger (expr)`は、
`askinteger (expr, integer)`と同値です。


同様に、
`askinteger (expr, even)`や`askinteger (expr, odd)`は、
それぞれ、*expr*が偶数か奇数か、決定しようとします。

<!-- category: Programming -->
<!-- keywords: asksign -->
<!-- signatures: asksign(expr) -->
### Function: asksign (expr)

最初に、指定された式が正か負かゼロか決定しようとします。
できなければ、演繹を完了するのに必要な質問をユーザーに尋ねます。
ユーザーの答えは、現在の計算の演繹のため、データベースに記録されます。
`asksign`の戻り値は、`pos`, `neg`もしくは`zero`のいずれか１つです。

<!-- category: Programming -->
<!-- keywords: assume -->
<!-- signatures: assume(pred_1, ..., pred_n) -->
### Function: assume (pred_1, ..., pred_n)

述語論理*pred_1*, ..., *pred_n*を現在の文脈に追加します。
もし述語論理が現在の文脈と矛盾していたり、冗長だったりしたなら、文脈に追加されません。
文脈は`assume`がコールされる毎に述語論理を累積していきます。


`assume`は、文脈に追加された述語論理を要素に持つリストか、
適用されたアトム`redundant`もしくは`inconsistent`を返します。


述語論理*pred_1*, ..., *pred_n*は
関係演算子`< <= equal notequal >= >`を持つ式のみ許されます。
述語論理はリテラル等号`=`やリテラル不等号`#`の式は使えません。
`integerp`のような述語関数も使えません。


形式`pred_1 and ...and pred_n`の合成された述語論理が認識されます。
しかし、`pred_1 or ... or pred_n`は認識されません。
もし`pred_k`が関係述語論理なら、`not pred_k`は認識されます。
形式`not (pred_1 and pred_2)`の式や
`not (pred_1 or pred_2)`は認識されません。


Maximaの推論メカニズムはそれほど強くありません;
`is`によって決定されない多くの明らかな結果があります。
これは既知の弱みです。


`assume`は複素数を伴う述語論理を扱いません。
もし述語論理が複素数を含むなら、`assume`は`inconsistent`か`redundant`を返します。


`assume`は引数を評価します。


`is`や`facts`, `forget`, `context`, `declare`も参照してください。


例:















```maxima
(%i1) assume (xx > 0, yy < -1, zz >= 0);
(%o1)              [xx > 0, yy < - 1, zz >= 0]
(%i2) assume (aa < bb and bb < cc);
(%o2)                  [bb > aa, cc > bb]
(%i3) facts ();
(%o3)     [xx > 0, - 1 > yy, zz >= 0, bb > aa, cc > bb]
(%i4) is (xx > yy);
(%o4)                         true
(%i5) is (yy < -yy);
(%o5)                         true
(%i6) is (sinh (bb - aa) > 0);
(%o6)                         true
(%i7) forget (bb > aa);
(%o7)                       [bb > aa]
(%i8) prederror : false;
(%o8)                         false
(%i9) is (sinh (bb - aa) > 0);
(%o9)                        unknown
(%i10) is (bb^2 < cc^2);
(%o10)                       unknown
```

<!-- category: Programming -->
<!-- keywords: assume_pos -->
<!-- signatures: assume_pos -->
### Variable: assume_pos

デフォルト値: `false`


`assume_pos`が`true`で、
パラメータ*x*の符号が現在の文脈や他の考慮から決定できない時、

`sign`や`asksign (x)`は、`true`を返します。
これは、`integrate`や他の計算から起こるような、
自動生成される`asksign`問い合わせを事前に防ぐことができます。


デフォルトでは、パラメータは`symbolp (x)`もしくは
`subvarp (x)`のような*x*です。
パラメータとして考えられる式のクラスは、
変数`assume_pos_pred`を介して、ある程度変えることができます。


`sign`と`asksign`は、
式の中のオペランドの符号から式の符号を演繹しようとします。
例えば、もし`a`や`b`がともに正なら、
`a + b`も正です。


しかしながら、`asksign`問い合わせすべてを迂回する方法はありません。
特に、`asksign`引数が、差`x - y`もしくは
対数`log(x)`の時、
たとえ`assume_pos`が`true`で、`assume_pos_pred`が
引数すべてに`true`を返す関数であっても、
`asksign`は、いつもユーザーからの入力を要請します。

<!-- category: Programming -->
<!-- keywords: assume_pos_pred -->
<!-- signatures: assume_pos_pred -->
### Variable: assume_pos_pred

デフォルト値: `false`


`assume_pos_pred`が関数名や、引数*x*のラムダ式に割り当てられている時、
その関数は、
*x*が、`assume_pos`のためのパラメータと考えられるかどうかを決定するために
コールされます。
`assume_pos`が`false`の時、
`assume_pos_pred`は、無視されます。


`assume_pos_pred`関数は、引数*x*で`sign`と`asksign`によってコールされます。
ここで、*x*はアトム、添字付き変数、関数コール式のいずれかです。
もし`assume_pos_pred`関数が`true`を返すなら、
*x*は、`assume_pos`のためのパラメータと考えられます。


デフォルトでは、パラメータは、`symbolp (x)`もしくは`subvarp (x)`のような*x*です。


`assume`と`assume_pos`も参照してください。


例:
















```maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: symbolp$
(%i3) sign (a);
(%o3)                          pos
(%i4) sign (a[1]);
(%o4)                          pnz
(%i5) assume_pos_pred: lambda ([x], display (x), true)$
(%i6) asksign (a);
                              x = a

(%o6)                          pos
(%i7) asksign (a[1]);
                             x = a
                                  1

(%o7)                          pos
(%i8) asksign (foo (a));
                           x = foo(a)

(%o8)                          pos
(%i9) asksign (foo (a) + bar (b));
                           x = foo(a)

                           x = bar(b)

(%o9)                          pos
(%i10) asksign (log (a));
                              x = a

Is  a - 1  positive, negative, or zero?

p;
(%o10)                         pos
(%i11) asksign (a - b);
                              x = a

                              x = b

                              x = a

                              x = b

Is  b - a  positive, negative, or zero?

p;
(%o11)                         neg
```

<!-- category: Programming -->
<!-- keywords: assumescalar -->
<!-- signatures: assumescalar -->
### Variable: assumescalar

デフォルト値: `true`


`assumescalar`は、
`nonscalarp (expr)`が`false`であるような式`expr`が、
ある変換に関してスカラーのように振る舞うと仮定されるかどうかを決めるのを助けます。


Let 
`expr`がリストや行列以外の任意の式を表してるとし、
`[1, 2, 3]`が任意のリストや行列を表しているとすると、
もし`assumescalar`が`true`、
もしくは`scalarp (expr)`が`true`、
もしくは`constantp (expr)`が`true`なら、
`expr . [1, 2, 3]`は、`[expr, 2 expr, 3 expr]`をもたらします。


もし`assumescalar`が`true`なら、
そんな式は可換演算子に関してだけスカラーのように振る舞いますが、
非可換乗算`.`に関してはそうは振る舞いません。


`assumescalar`が`false`の時
そんな式は、非スカラーのように振る舞います。


`assumescalar`が`all`の時、
そんな式は、上でリストされた演算子すべてに関してスカラーのように振る舞います。

<!-- category: Programming -->
<!-- keywords: charfun -->
<!-- signatures: charfun(p) -->
### Function: charfun (p)

述語論理*p*が`false`に評価される時、0を返します;
述語論理*p*が`true`に評価される時、1を返します。
述語論理が`true`も`false`でもない何かに評価される時(unknown), 
名詞形を返します。


例:









```maxima
(%i1) charfun (x < 1);
(%o1)                    charfun(x < 1)
(%i2) subst (x = -1, %);
(%o2)                           1
(%i3) e : charfun ('"and" (-1 < x, x < 1))$
(%i4) [subst (x = -1, e), subst (x = 0, e), subst (x = 1, e)];
(%o4)                       [0, 1, 0]
```

<!-- category: Programming -->
<!-- keywords: compare -->
<!-- signatures: compare(x, y) -->
### Function: compare (x, y)

`is (x op y)`が
`true`に評価されるような比較演算子*op*
(`<`,`<=`,`>`,`>=`,`=`,`#`)を返します;
*x*か*y*が `%i`に依存して、`x # y`の時、
`notcomparable`を返します;
該当する演算子がなかったり、Maximaが演算子を決定できなかった時には
`unknown`を返します。


例:











```maxima
(%i1) compare (1, 2);
(%o1)                           <
(%i2) compare (1, x);
(%o2)                        unknown
(%i3) compare (%i, %i);
(%o3)                           =
(%i4) compare (%i, %i + 1);
(%o4)                     notcomparable
(%i5) compare (1/x, 0);
(%o5)                           #
(%i6) compare (x, abs(x));
(%o6)                          <=
```


関数`compare`は引数の実領域が空でないか決定しようとはしません; 従って、






```maxima
(%i1) compare (acos (x^2 + 1), acos (x^2 + 1) + 1);
(%o1)                           <
```



`acos (x^2 + 1)`の実領域は空です。

<!-- category: Programming -->
<!-- keywords: constant -->
<!-- signatures: constant -->
### Function: constant

`declare (a, constant)`は、*a*を定数に宣言します。
`declare`を参照してください。

See also: `declare`.

<!-- category: Programming -->
<!-- keywords: constantp -->
<!-- signatures: constantp(expr) -->
### Function: constantp (expr)

もし*expr*が定数式なら、`true`を返します。
そうでなければ、`false`を返します。



もし引数が、（`/R/`をつけて表示される有理数を含む）数や
`%pi`, `%e`, `%i`にようなシンボル定数、
定数にバインドされた変数、`declare`で宣言された定数、
引数が定数の関数のいずれかなら、
式は定数式と考えられます。


`constantp`は引数を評価します。


例:












```maxima
(%i1) constantp (7 * sin(2));
(%o1)                                true
(%i2) constantp (rat (17/29));
(%o2)                                true
(%i3) constantp (%pi * sin(%e));
(%o3)                                true
(%i4) constantp (exp (x));
(%o4)                                false
(%i5) declare (x, constant);
(%o5)                                done
(%i6) constantp (exp (x));
(%o6)                                true
(%i7) constantp (foo (x) + bar (%e) + baz (2));
(%o7)                                false
(%i8)
```

See also: `%pi`, `%e`, `%i`, `declare`.

<!-- category: Programming -->
<!-- keywords: context -->
<!-- signatures: context -->
### Variable: context

デフォルト値: `initial`


`context`は、`assume`と`forget`によって保守される事実の集まりの名前です。


`assume`は、`context`と名付けられた集まりに事実を追加する一方、
`forget`は、事実を取り除きます。


`context`を名前*foo*にバインドすることは、
現在の文脈を*foo*に変えます。
もし指定された文脈*foo*がまだ存在しないなら、
`newcontext`のコールによって自動的に生成されます。

指定された文脈は自動的にアクティベートされます。


文脈メカニズムの一般的な記述に関しては、`contexts`を参照してください。

<!-- category: Programming -->
<!-- keywords: contexts -->
<!-- signatures: contexts -->
### Variable: contexts

デフォルト値: `[initial, global]`


`contexts`は、
現在アクティブな文脈を含んでいる、現在存在する文脈のリストです。


文脈メカニズムは、ユーザーが
文脈と呼ばれる事実の集まりにバインドし、名付けることを可能にします。
一旦これがなされると、ユーザーは、
文脈を単にアクティベートしたりデアクティベートすることで、
たくさんの数の事実をMaximaに仮定させたり忘れさせたりできます。


任意のシンボルのアトムは、文脈となりえ、
その文脈の中に含まれた事実は、
`forget`をコールすることで１つ１つ破壊されるまで、
あるいは、それらが属する文脈を破壊するために`kill`をコールすることで、全体として破壊されるまで、記憶装置に保持されます。


文脈は階層的に存在します。
その根はいつも文脈`global`であり、
文脈`global`は、いくつかの関数が必要とするMaximaについての情報を含みます。
アクティブな文脈の部分文脈である任意の文脈の中の事実すべてそうであるように、
与えられた文脈の中では、
その文脈の中の事実すべては、「アクティブ」（それらが演繹や探索に使われるという意味）
です。


新鮮なMaximaが起動された時、
ユーザーは、`initial`と呼ばれる文脈の中にいます。
それは、部分文脈として`global`を持ちます。


`facts`, `newcontext`,
`supcontext`, `killcontext`, `activate`, `deactivate`, `assume`, `forget`も参照してください。

<!-- category: Programming -->
<!-- keywords: deactivate -->
<!-- signatures: deactivate(context_1, ..., context_n) -->
### Function: deactivate (context_1, ..., context_n)

特定の文脈*context_1*, ..., *context_n*をデアクティベートします。

<!-- category: Programming -->
<!-- keywords: declare -->
<!-- signatures: declare(a_1, p_1, a_2, p_2, ...) -->
### Function: declare (a_1, p_1, a_2, p_2, ...)

アトムやアトムのリスト*a_i*に、プロパティやプロパティのリスト*p_i*を割り当てます。
*a_i*や*p_i*がリストの時、
アトムのそれぞれは、プロパティすべてを得ます。


`declare`は引数をクォートします。
`declare`はいつも`done`を返します。


それぞれの宣言フラグに関する記述で注意しているように、
いくつかのフラグに関して、
もし*object*が*feature*を持つよう宣言されているなら、
`featurep(object, feature)`は、
`true`を返します。
しかしながら、`featurep`はいくつかのフラグを認識しません;
これはバグです。


`features`も参照してください。


`declare`は以下のプロパティを認識します:



**`evfun`** — `ev`のフラグ引数として*a_i*が現れた時
*a_i*で名付けられた関数を適用するように
`ev`に伝えます。
`evfun`を参照してください。
**`evflag`** — `ev`のフラグ引数として*a_i*が現れた時
`ev`の実行中*a_i*が`true`にバインドされるように
`ev`に伝えます。
`evflag`を参照してください。
**`bindtest`** — *a_i*がバインドされていない状態に評価された時、
Maximaにエラーをトリガーするように伝えます。
**`noun`** — *a_i*を名詞としてパースするようにMaximaに伝えます。
この効果は、*a_i*のインスタンスを`'a_i`や`nounify(a_i)`
で置き換えることです。どちらに置き換えるかは文脈に依存します。
**`constant`** — *a_i*をシンボル定数と考えるようにMaximaに伝えます。
**`scalar`** — *a_i*をスカラー変数と考えるようにMaximaに伝えます。
**`nonscalar`** — *a_i*を非スカラー変数と考えるようにMaximaに伝えます。
普通の使い方は、変数をシンボルベクトルや行列として宣言することです。
**`nonarray`** — Maximaに*a_i*を配列でないものと考えるように伝えます。
この宣言は添字付き変数名の多重評価を抑制します。
**`mainvar`** — *a_i*を「主変数」と考えるようにMaximaに伝えます。
`ordergreatp`で決定されるように、
Maximaの式の標準順序では、主変数は他のすべての定数や変数に続きます。
**`alphabetic`** — （文字列の）*a_i*の中の文字すべてをアルファベット文字として認識するように
Maximaに伝えます。
**`feature`** — *a_i*をfeature名として認識するようにMaximaに伝えます。
他のアトムは、*a_i*プロパティを持つように定義されます。
**`rassociative`, `lassociative`** — *a_i*を右結合、もしくは左結合関数として認識するようにMaximaに伝えます。
**`nary`** — *a_i*をn項関数として認識するようにMaximaに伝えます。 
`nary`宣言は、`nary`関数をコールするのとは同じではありません。
`declare(foo, nary)`だけの効果は、Maxima整理器を
ネストされた式を平坦にするように指示することです。
例えば、`foo(x, foo(y, z))`を`foo(x, y, z)`に整理します。
**`symmetric`, `antisymmetric`, `commutative`** — *a_i*を対称もしくは反対称関数として認識するようにMaximaに伝えます。
`commutative`は`symmetric`と同じです。
**`oddfun`, `evenfun`** — *a_i*を偶関数もしくは奇関数として認識するようにMaximaに伝えます。
**`outative`** — *a_i*式を最初の引数から定数因子を引き出すことで整理するようにMaximaに伝えます。 
*a_i*が１つ引数を持つ時、
もしリテラル定数や宣言定数なら、因子は定数とみなされます。 
*a_i*が２つ以上の引数を持つ時、
もし２番目の引数がシンボルであり、因子が２番目の引数の制約を受けなければ、
因子は定数とみなされます。
**`multiplicative`** — 代入`a_i(x * y * z * ...)` `-->`
`a_i(x) * a_i(y) * a_i(z) * ...`.
によって、*a_i*式を整理するようにMaximaに伝えます。
代入は、１番目の引数のみで実行されます。
**`additive`** — 代入`a_i(x + y + z + ...)` `-->`
`a_i(x) + a_i(y) + a_i(z) + ...`.
によって、*a_i*式を整理するようにMaximaに伝えます。
代入は、１番目の引数のみで実行されます。
**`linear`** — *a_i*を`outative`かつ`additive`に宣言することと同値です。
**`integer`, `noninteger`** — *a_i*を整数もしくは非整数変数として認識するようにMaximaに伝えます。
**`even`, `odd`** — *a_i*を偶数変数もしくは奇数変数として認識するようにMaximaに伝えます。
**`rational`, `irrational`** — *a_i*を有理変数もしくは非有理実変数として認識するようにMaximaに伝えます。
**`real`, `imaginary`, `complex`** — *a_i*を実変数もしくは純虚数変数もしくは複素変数として認識するようにMaximaに伝えます。
**`increasing`, `decreasing`** — *a_i*を単調増加関数もしくは単調減少関数として認識するようにMaximaに伝えます。
**`posfun`** — *a_i*を正関数として認識するようにMaximaに伝えます。
**`integervalued`** — *a_i*を整数値を返す関数として認識するようにMaximaに伝えます。


例:


`evfun`と`evflag`宣言。











```maxima
(%i1) declare (expand, evfun);
(%o1)                         done
(%i2) (a + b)^3;
                                   3
(%o2)                       (b + a)
(%i3) (a + b)^3, expand;
                     3        2      2      3
(%o3)               b  + 3 a b  + 3 a  b + a
(%i4) declare (demoivre, evflag);
(%o4)                         done
(%i5) exp (a + b*%i);
                             %i b + a
(%o5)                      %e
(%i6) exp (a + b*%i), demoivre;
                      a
(%o6)               %e  (%i sin(b) + cos(b))
```


`bindtest`宣言。










```maxima
(%i1) aa + bb;
(%o1)                        bb + aa
(%i2) declare (aa, bindtest);
(%o2)                         done
(%i3) aa + bb;
aa unbound variable
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) aa : 1234;
(%o4)                         1234
(%i5) aa + bb;
(%o5)                       bb + 1234
```


`noun`宣言。









```maxima
(%i1) factor (12345678);
                             2
(%o1)                     2 3  47 14593
(%i2) declare (factor, noun);
(%o2)                         done
(%i3) factor (12345678);
(%o3)                   factor(12345678)
(%i4) ''%, nouns;
                             2
(%o4)                     2 3  47 14593
```


`constant`, `scalar`, `nonscalar`, `mainvar`宣言。









```maxima

```


`alphabetic`宣言。









```maxima
(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729
(%i2) declare ("~`@", alphabetic);
(%o2)                         done
(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729
(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```


`feature`宣言。








```maxima
(%i1) declare (FOO, feature);
(%o1)                         done
(%i2) declare (x, FOO);
(%o2)                         done
(%i3) featurep (x, FOO);
(%o3)                         true
```


`rassociative`, `lassociative`宣言。







```maxima

```


`nary`宣言。








```maxima
(%i1) H (H (a, b), H (c, H (d, e)));
(%o1)               H(H(a, b), H(c, H(d, e)))
(%i2) declare (H, nary);
(%o2)                         done
(%i3) H (H (a, b), H (c, H (d, e)));
(%o3)                   H(a, b, c, d, e)
```


`symmetric`, `antisymmetric`宣言。













```maxima
(%i1) S (b, a);
(%o1)                        S(b, a)
(%i2) declare (S, symmetric);
(%o2)                         done
(%i3) S (b, a);
(%o3)                        S(a, b)
(%i4) S (a, c, e, d, b);
(%o4)                   S(a, b, c, d, e)
(%i5) T (b, a);
(%o5)                        T(b, a)
(%i6) declare (T, antisymmetric);
(%o6)                         done
(%i7) T (b, a);
(%o7)                       - T(a, b)
(%i8) T (a, c, e, d, b);
(%o8)                   T(a, b, c, d, e)
```


`oddfun`, `evenfun`宣言。











```maxima
(%i1) o (- u) + o (u);
(%o1)                     o(u) + o(- u)
(%i2) declare (o, oddfun);
(%o2)                         done
(%i3) o (- u) + o (u);
(%o3)                           0
(%i4) e (- u) - e (u);
(%o4)                     e(- u) - e(u)
(%i5) declare (e, evenfun);
(%o5)                         done
(%i6) e (- u) - e (u);
(%o6)                           0
```


`outative`宣言。










```maxima
(%i1) F1 (100 * x);
(%o1)                       F1(100 x)
(%i2) declare (F1, outative);
(%o2)                         done
(%i3) F1 (100 * x);
(%o3)                       100 F1(x)
(%i4) declare (zz, constant);
(%o4)                         done
(%i5) F1 (zz * y);
(%o5)                       zz F1(y)
```


`multiplicative`宣言。








```maxima
(%i1) F2 (a * b * c);
(%o1)                       F2(a b c)
(%i2) declare (F2, multiplicative);
(%o2)                         done
(%i3) F2 (a * b * c);
(%o3)                   F2(a) F2(b) F2(c)
```


`additive`宣言。








```maxima
(%i1) F3 (a + b + c);
(%o1)                     F3(c + b + a)
(%i2) declare (F3, additive);
(%o2)                         done
(%i3) F3 (a + b + c);
(%o3)                 F3(c) + F3(b) + F3(a)
```


`linear`宣言。








```maxima
(%i1) 'sum (F(k) + G(k), k, 1, inf);
                       inf
                       ====
                       \
(%o1)                   >    (G(k) + F(k))
                       /
                       ====
                       k = 1
(%i2) declare (nounify (sum), linear);
(%o2)                         done
(%i3) 'sum (F(k) + G(k), k, 1, inf);

                     inf          inf
                     ====         ====
                     \            \
(%o3)                 >    G(k) +  >    F(k)
                     /            /
                     ====         ====
                     k = 1        k = 1
```

<!-- category: Programming -->
<!-- keywords: equal -->
<!-- signatures: equal(a, b) -->
### Function: equal (a, b)

同値、すなわち、同じ値であることを表します。


`equal`はそれ自身で評価も整理もされません。
関数`is`は、`equal`をブーリアン値に評価しようとします。
`is(equal(a, b)`は、
もし*a*と*b*が、`ratisimp(a - b)`を評価することで決定されるように、
変数の可能な値すべてで等しいときだけ`true`を返します;
もし`ratsimp`が0を返したら、２つの式は同値と考えれます。
２つの式は構文法的に等しくなくても（すなわち同一でなくても）同値でありえます。


`is`が`equal`を`true`もしくは`false`への換算に失敗した時、
結果は、グローバルフラグ`prederror`に依ります。
`prederror`が`true`の時、`is`はエラーメッセージを出力します。
そうでなければ、`is`は`unknown`を返します。


`is`に加えて、
いくつかの他の演算子、`if`, `and`, `or`, `not`は
`equal`と`notequal`を`true`もしくは`false`に評価します。







`equal`の否定が`notequal`です。


例:


`equal`はそれ自身で評価も整理もされません。








```maxima
(%i1) equal (x^2 - 1, (x + 1) * (x - 1));
                        2
(%o1)            equal(x  - 1, (x - 1) (x + 1))
(%i2) equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) equal (x, y);
(%o3)                      equal(x, y)
```


関数`is`は、`equal`をブーリアン値に評価しようとします。
`is(equal(a, b)`は、
`ratisimp(a - b)`が0を返すとき`true`を返します。
２つの式は構文法的に等しくなくても（すなわち同一でなくても）同値でありえます。














```maxima
(%i1) ratsimp (x^2 - 1 - (x + 1) * (x - 1));
(%o1)                           0
(%i2) is (equal (x^2 - 1, (x + 1) * (x - 1)));
(%o2)                         true
(%i3) is (x^2 - 1 = (x + 1) * (x - 1));
(%o3)                         false
(%i4) ratsimp (x - (x + 1));
(%o4)                          - 1
(%i5) is (equal (x, x + 1));
(%o5)                         false
(%i6) is (x = x + 1);
(%o6)                         false
(%i7) ratsimp (x - y);
(%o7)                         x - y
(%i8) is (equal (x, y));
(%o8)                        unknown
(%i9) is (x = y);
(%o9)                         false
```


`is`が、`equal`を`true`もしくは`false`への換算に失敗したとき、
結果は、グローバルフラグ`prederror`に依ります。











```maxima
(%i1) [aa : x^2 + 2*x + 1, bb : x^2 - 2*x - 1];
                    2             2
(%o1)             [x  + 2 x + 1, x  - 2 x - 1]
(%i2) ratsimp (aa - bb);
(%o2)                        4 x + 2
(%i3) prederror : true;
(%o3)                         true
(%i4) is (equal (aa, bb));
Maxima was unable to evaluate the predicate:
       2             2
equal(x  + 2 x + 1, x  - 2 x - 1)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) prederror : false;
(%o5)                         false
(%i6) is (equal (aa, bb));
(%o6)                        unknown
```


いくつかの演算子が`equal`や`notequal`を
`true`もしくは`false`に評価します。









```maxima
(%i1) if equal (y, y - 1) then FOO else BAR;
(%o1)                          BAR
(%i2) eq_1 : equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) eq_2 : equal (y^2 + 2*y + 1, (y + 1)^2);
                         2                   2
(%o3)             equal(y  + 2 y + 1, (y + 1) )
(%i4) [eq_1 and eq_2, eq_1 or eq_2, not eq_1];
(%o4)                  [false, true, true]
```


`not expr`は、*expr*の評価を伴うので、
`not equal(a, b)`は、`is(notequal(a, b))`と同値です。







```maxima
(%i1) [notequal (2*z, 2*z - 1), not equal (2*z, 2*z - 1)];
(%o1)            [notequal(2 z, 2 z - 1), true]
(%i2) is (notequal (2*z, 2*z - 1));
(%o2)                         true
```

<!-- category: Programming -->
<!-- keywords: facts -->
<!-- signatures: facts(item), facts() -->
### Function: facts (item)

もし*item*が文脈の名前なら、
`facts (item)`は指定された文脈の`facts`のリストを返します。


もし*item*が文脈の名前でなければ、
`facts (item)`は現在の文脈の中で、
*item*について知っている`facts`のリストを返します。
異なる文脈中のアクティブな`facts`はリストされません。


`facts ()`（すなわち引数なし）は現在の文脈をリストします。

<!-- category: Programming -->
<!-- keywords: features -->
<!-- signatures: features -->
### Variable: features

Maximaは、関数や変数のある数学的プロパティを認識します。
それらは「フィーチャー」と呼ばれます。


`declare (x, foo)`は、
プロパティ*foo*を関数もしくは変数*x*に与えます。


`declare (foo, feature)`は、
新しいフィーチャー*foo*を宣言します。
例えば、
`declare ([red, green, blue], feature)`は、
３つの新しいフィーチャー`red`, `green`, `blue`を宣言します。


もし*x*が*foo*プロパティを持つなら、
述語論理`featurep (x, foo)`は、`true`を返し、
そうでなければ、`false`を返します。


インフォリスト`features`は既知のフィーチャーのリストです。
それらは、



   integer        noninteger      even
   odd            rational        irrational
   real           imaginary       complex
   analytic       increasing      decreasing
   oddfun         evenfun         posfun
   commutative    lassociative    rassociative
   symmetric      antisymmetric


プラス、任意のユーザー定義フィーチャーです。


`features`は、数学的フィーチャーのリストです。
非数学的で、システム依存のフィーチャーのリストもあります。
`status`を参照してください。

<!-- category: Programming -->
<!-- keywords: forget -->
<!-- signatures: forget(pred_1, ..., pred_n), forget(L) -->
### Function: forget (pred_1, ..., pred_n)

`assume`で規定された述語論理を取り除きます。
述語論理は以前に規定されたものと同値の（必ずしも同一である必要なない）式です。


`forget (L)`（*L*は述語論理のリスト）は、
リスト上のそれぞれの項目を忘れます。

<!-- category: Programming -->
<!-- keywords: get -->
<!-- signatures: get(a, i) -->
### Function: get (a, i)

*i*が示すアトム *a*のユーザープロパティを検索し、
もしaがプロパティ *i*を持たないなら、 `false`を返します。


`get`は、引数を評価します。


















```maxima
(%i1) put (%e, 'transcendental, 'type);
(%o1)                    transcendental
(%i2) put (%pi, 'transcendental, 'type)$
(%i3) put (%i, 'algebraic, 'type)$
(%i4) typeof (expr) := block ([q],
        if numberp (expr)
        then return ('algebraic),
        if not atom (expr)
        then return (maplist ('typeof, expr)),
        q: get (expr, 'type),
        if q=false
        then errcatch (error(expr,"is not numeric.")) else q)$
(%i5) typeof (2*%e + x*%pi);
x is not numeric.
(%o5)  [[transcendental, []], [algebraic, transcendental]]
(%i6) typeof (2*%e + %pi);
(%o6)     [transcendental, [algebraic, transcendental]]
```

<!-- category: Programming -->
<!-- keywords: is -->
<!-- signatures: is(expr) -->
### Function: is (expr)

`assume`データベースの中の事実から述語論理*expr*が確かか否かを決定
しようとします。


もし述語論理が確かに`true`もしくは`false`なら、
`is`は、それぞれ`true`もしくは`false`を返します。
そうでなければ、戻り値は、グローバルフラグ`prederror`に依存します。
`prederror`が`true`の時、
`is`はエラーメッセージを出力します。
そうでなければ、`is`は`unknown`を出力します。


`ev(expr, pred)`
(対話プロンプトでは、`expr, pred`と書けます)
は、`is(expr)`と同値です。


`assume`, `facts`, `maybe`も参照してください。


例:


`is`は述語論理の評価を引き起こします。







```maxima
(%i1) %pi > %e;
(%o1)                       %pi > %e
(%i2) is (%pi > %e);
(%o2)                         true
```


`is`は、`assume`データベースから述語論理を演繹しようとします。










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) assume (b > c);
(%o2)                        [b > c]
(%i3) is (a < b);
(%o3)                         false
(%i4) is (a > c);
(%o4)                         true
(%i5) is (equal (a, c));
(%o5)                         false
```


もし`is`が`assume`データベースから述語論理を証明もしくは否定できなかったら、
グローバルフラグ`prederror`が`is`の振る舞いを決めます。










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) prederror: true$
(%i3) is (a > 0);
Maxima was unable to evaluate the predicate:
a > 0
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) prederror: false$
(%i5) is (a > 0);
(%o5)                        unknown
```

<!-- category: Programming -->
<!-- keywords: killcontext -->
<!-- signatures: killcontext(context_1, ..., context_n) -->
### Function: killcontext (context_1, ..., context_n)

文脈*context_1*, ..., *context_n*を消します。


もし文脈の１つが現在の文脈なら、
新しい文脈は、
消されなかった現在の文脈の最初の利用可能な部分文脈になるでしょう。
もし最初の利用可能な消されなかった文脈が`global`なら、
`initial`が代わりに使われます。
もし`initial`文脈が消されたら、
新しい、空の`initial`文脈が生成されます。


`killcontext`は、現在アクティブな文脈を消すことを拒否します。
なぜなら、それは現在の文脈の部分文脈、もしくは
関数`activate`の使用によってアクティブになっているから。


`killcontext`は、引数を評価します。
`killcontext`は、`done`を返します。

<!-- category: Programming -->
<!-- keywords: maybe -->
<!-- signatures: maybe(expr) -->
### Function: maybe (expr)

述語論理*expr*が`assume`データベースの事実から正しいかどうかを
決定しようとします。


もし述語論理が確かに`true`もしくは`false`なら、
`maybe`は、それぞれ`true`もしくは`false`を返します。
そうでなければ、`maybe`は`unknown`を返します。


`maybe`は、`prederror: false`での`is`と関数的に同値です。
しかし、`prederror`に値を実際に割り当てることなく結果が計算されます。


`assume`, `facts`, `is`も参照してください。


例:








```maxima
(%i1) maybe (x > 0);
(%o1)                        unknown
(%i2) assume (x > 1);
(%o2)                        [x > 1]
(%i3) maybe (x > 0);
(%o3)                         true
```

<!-- category: Programming -->
<!-- keywords: newcontext -->
<!-- signatures: newcontext(name) -->
### Function: newcontext (name)

*name*と呼ばれる新しい、空の文脈を生成します。
*name*は、唯一の部分文脈として`global`を持ちます。
新しく生成された文脈は現在アクティブな文脈になります。


`newcontext`は、引数を評価します。
`newcontext`は、*name*を返します。

<!-- category: Programming -->
<!-- keywords: nonarray -->
<!-- signatures: nonarray -->
### Function: nonarray

コマンド`declare(a, nonarray)`はMaximaに
*a*が配列でないものと考えるように伝えます。
もし*a*が添字付き変数なら、この宣言は多重評価を抑制します。


例:









```maxima
(%i1) a:'b$ b:'c$ c:'d$


(%i4) a[x];
(%o4)                          d
                                x
(%i5) declare(a, nonarray);
(%o5)                         done
(%i6) a[x];
(%o6)                          a
                                x
```

<!-- category: Programming -->
<!-- keywords: notequal -->
<!-- signatures: notequal(a, b) -->
### Function: notequal (a, b)

`equal(a, b)`の否定を表します。


例:















```maxima
(%i1) equal (a, b);
(%o1)                      equal(a, b)
(%i2) maybe (equal (a, b));
(%o2)                        unknown
(%i3) notequal (a, b);
(%o3)                    notequal(a, b)
(%i4) not equal (a, b);
(%o4)                    notequal(a, b)
(%i5) maybe (notequal (a, b));
(%o5)                        unknown
(%i6) assume (a > b);
(%o6)                        [a > b]
(%i7) equal (a, b);
(%o7)                      equal(a, b)
(%i8) maybe (equal (a, b));
(%o8)                         false
(%i9) notequal (a, b);
(%o9)                    notequal(a, b)
(%i10) maybe (notequal (a, b));
(%o10)                        true
```

<!-- category: Programming -->
<!-- keywords: posfun -->
<!-- signatures: posfun -->
### Variable: posfun

`declare (f, posfun)`は、
`f`を正の関数と宣言します。
`is (f(x) > 0)`は`true`を出力します。

<!-- category: Programming -->
<!-- keywords: printprops -->
<!-- signatures: printprops(a, i), printprops([a_1, ..., a_n], i), printprops(all, i) -->
### Function: printprops (a, i)

アトム*a*に関連付けられた指標*i*の属性を表示します。
*a*は、アトムのリストもしくはアトム`all`もありえます。
その場合，与えられたプロパティを持つすべてのアトムに適用します。
例えば、 `printprops ([f, g], atvalue)`。
`printprops`は、表示できないプロパティ、
すなわち`atvalue`, `atomgrad`, `gradef`, `matchdeclare`のためのものです。

See also: `atvalue`, `atomgrad`, `gradef`, `matchdeclare`.

<!-- category: Programming -->
<!-- keywords: sign -->
<!-- signatures: sign(expr) -->
### Function: sign (expr)

現在のデータベースの事実に基づいて*expr*の符号を決定しようとします。
以下の答えの１つを返します;
`pos` (positive), `neg` (negative), `zero`, `pz`
(正もしくはゼロ), `nz` (負もしくはゼロ), `pn` (正もしくは負),
or `pnz` (正、負もしくはゼロ、すなわちなにもわからない).

<!-- category: Programming -->
<!-- keywords: supcontext -->
<!-- signatures: supcontext(name, context), supcontext(name) -->
### Function: supcontext (name, context)

*name*と呼ばれる新しい文脈を生成します。
*name*は、部分文脈として*context*を持ちます。
*context*は存在しなければいけません。


もし*context*が指定されないなら、
現在の文脈が仮定されます。

<!-- category: Programming -->
<!-- keywords: unknown -->
<!-- signatures: unknown(expr)] -->
### Function: unknown ((expr)])

*expr*がMaximaの整理器が認識しない演算子や関数を含む時だけ、
`true`を返します。

<!-- category: Programming -->
<!-- keywords: zeroequiv -->
<!-- signatures: zeroequiv(expr, v) -->
### Function: zeroequiv (expr, v)

変数*v*の式*expr*がゼロと同値かどうかテストし、
`true`, `false`, もしくは`dontknow`を返します。


`zeroequiv`は以下の制限を持ちます:



1. Maximaが微分や評価する方法を知らない関数を使わない。
2. もし式が実線上で極を持つなら、
結果としてエラーになります。（しかしこれは起こりにくいことです。）
3. もし式が１階微分方程式の解ではない関数（例えばベッセル関数）を含むなら、
正しくない結果になるかもしれません。
4. アルゴリズムは、注意深く選ばれた部分式に関してランダムに選ばれた点での評価を使います。
アルゴリズムはエラーの可能性を細小にしようとしますが、これはいつも危険な仕事です。


例えば、`zeroequiv (sin(2 * x) - 2 * sin(x) * cos(x), x)`は`true`を返し、
`zeroequiv (%e^x + x, x)`は`false`を返します。
一方、
`zeroequiv (log(a * b) - log(a) - log(b), a)`は、
余分なパラメータ`b`があるので、`dontknow`を返します。

