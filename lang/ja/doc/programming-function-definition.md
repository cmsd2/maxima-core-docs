## Function Definition

<!-- category: Programming -->
<!-- keywords: apply -->
<!-- signatures: apply(F, [x_1, ..., x_n]) -->
### Function: apply (F, [x_1, ..., x_n])

`F(x_1, ..., x_n)`を構成、評価します。


`apply`は、配列関数を通常の関数と区別しようとはしません;
*F*が配列関数の名前の時、`apply`は`F(...)`(カギ括弧の代わりに括弧での関数コール）を評価します。
`arrayapply`は、この場合、カギ括弧ありで関数コールを評価します。


例:


`apply`は、引数を評価します。
この例では、`min`が`L`の値に適用されます。







```maxima
(%i1) L : [1, 5, -10.2, 4, 3];
(%o1)                 [1, 5, - 10.2, 4, 3]
(%i2) apply (min, L);
(%o2)                        - 10.2
```


`apply`は、たとえ関数*F*が引数をクォートする場合でも、引数を評価します。










```maxima
(%i1) F (x) := x / 1729;
                                   x
(%o1)                     F(x) := ----
                                  1729
(%i2) fname : F;
(%o2)                           F
(%i3) dispfun (F);
                                   x
(%t3)                     F(x) := ----
                                  1729

(%o3)                         [%t3]
(%i4) dispfun (fname);
fname is not the name of a user function.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) apply (dispfun, [fname]);

                                   x
(%t5)                     F(x) := ----
                                  1729

(%o5)                         [%t5]
```


`apply`は関数名*F*を評価します。
シングルクオート`'`は評価を無効にします。
`demoivre`はグローバル変数の名前であり、また、関数でもあります。









```maxima
(%i1) demoivre;
(%o1)                         false
(%i2) demoivre (exp (%i * x));
(%o2)                  %i sin(x) + cos(x)
(%i3) apply (demoivre, [exp (%i * x)]);
demoivre evaluates to false
Improper name or value in functional position.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) apply ('demoivre, [exp (%i * x)]);
(%o4)                  %i sin(x) + cos(x)
```

<!-- category: Programming -->
<!-- keywords: block -->
<!-- signatures: block([v_1, ..., v_m], expr_1, ..., expr_n), block(expr_1, ..., expr_n) -->
### Function: block ([v_1, ..., v_m], expr_1, ..., expr_n)

`block`は*expr_1*, ..., *expr_n*を順に評価し、評価された最後の式の値を返します。
順序は`go`, `throw`, `return`関数によって変更することができます。
最後の式は、`return`もしくは`throw`を含む式が評価されないなら、*expr_n*です。
いくつかの変数*v_1*, ..., *v_m*がブロックにローカルに宣言できます;
これらは同じ名前のグローバル変数と区別されます。
変数がローカルに宣言されないなら、リストは省略できます。
ブロック内では、*v_1*, ..., *v_m*以外の変数はグローバル変数です。


`block`は（存在するなら）変数*v_1*, ..., *v_m*の現在の値を保存し、
変数がそれ自身に評価されるよう変数のバインドを解除します。
ローカル変数はブロック内部で任意の値にバインドできますが、
ブロックが終了するとき保存された値が戻され、
ブロック内で割り当てられた値は失われます。


`block`内部の宣言`local(v_1, ..., v_m)`は
シンボル*v_1*, ..., *v_m*に関連付けられた性質を保存し、
他の式を評価する前に、性質を取り除き、ブロック終了時に元に戻します。
いくつかの宣言は、`:=`、`array`, `dependencies`, `atvalue`, `matchdeclare`,
`atomgrad`, `constant`, `nonscalar`その他を含むシンボルの性質として実装されます。
`local`の効果は、ブロック内部のみで有効な宣言を作ります;
そうでなければ、ブロック内部の宣言は実際にグローバル宣言となります。


`block`は他の`block`内部でも現れます。
ローカル変数が、新しいブロックが評価されるたびに確立されます。
ローカル変数は、内包するブロックではグローバルです。
ブロックの中で、変数がローカルでないなら、その値は内包するブロックによって割り当てられた最新の値です。
そうでなければ、グローバル環境の変数の値になります。
このポリシーは「動的スコープ」の普通の理解と一致します。


ブロックの値は、最後の文もしくはブロックから陽に終了するのに使われる関数`function`の引数の値です。
関数`go`は、`go`の引数でタグされたブロックの文に制御を移すのに使われます。
例えば、`block ([x], x:1, loop, x: x+1, ..., go(loop), ...)`。
`go`の引数はブロック内部に現れるタグの名前でなければなりません。
`go`を含んだブロック以外のブロック内部のタグへ飛ぶのに`go`を使うことはできません。


ブロックは、典型的な場合、関数定義の右辺に現れますが、他の場所でも使うことができます。

<!-- category: Programming -->
<!-- keywords: break -->
<!-- signatures: break(expr_1, ..., expr_n) -->
### Function: break (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を評価し、印字し、それから
ユーザーが環境を検査し変更できるところでMaximaブレイクを引き起こします。
`exit;`をタイプすると、計算が再開されます。

<!-- category: Programming -->
<!-- keywords: buildq -->
<!-- signatures: buildq(L, expr) -->
### Function: buildq (L, expr)

リスト*L*で指名された変数を式 *expr*に
並列に代入します。*expr*は評価しません。
`buildq`が代入を実行した後、
結果の式は整理はされますが、評価されません。


*L*の要素はシンボルまたは割り当て式`symbol: value`です。
割り当て式は並列に評価されます。
すなわち、ある変数が割り当ての右辺へバインドされるのは、
`buildq`がコールされた文脈でのバインドです。
変数リスト*L*内でその変数がバインドされるのではありません。
もし*L*の中のある変数に明示的な割り当てがないなら、
`buildq`でのバインドは、
`buildq`がコールされた文脈でのそれと同じです。


そして、*L*で指名された変数は並列に*expr*に代入されます。
すなわち、すべての変数への代入は他の代入がされる前に決まります。
だから、１つの変数の代入は他には一切効果を持ちません。


もし
任意の変数 *x*が *expr*の中で `splice (x)`のように現れるなら、
*x*はリストにバインドされなければいけませんし、
リストは、代入の代わりに*expr* に接合(内挿)されます。


*expr*の中の*L*に現れない任意の変数は、
たとえそれらが`buildq`がコールされた文脈の中でバインドを持っていても、
逐語的に結果に繰り越されます。


例


`a`は明示的に `x`にバインドされ、
一方で `b`は、コールする文脈で同じバインド(すなわち29)を持ち、
`c`は逐語的に繰り越されます。
結果の式は、明示的な評価 `''%`まで評価されません。








```maxima
(%i1) (a: 17, b: 29, c: 1729)$
(%i2) buildq ([a: x, b], a + b + c);
(%o2)                      x + c + 29
(%i3) ''%;
(%o3)                       x + 1758
```


`e`はリストにバインドされ、
`foo`の引数の中でそのように現れ、
`bar`の引数の中に内挿されます。







```maxima
(%i1) buildq ([e: [a, b, c]], foo (x, e, y));
(%o1)                 foo(x, [a, b, c], y)
(%i2) buildq ([e: [a, b, c]], bar (x, splice (e), y));
(%o2)                  bar(x, a, b, c, y)
```


代入の後、結果は整理されます。
もし代入の前に整理が適用されたら、これら２つの結果は同じになったはずです。






```maxima
(%i1) buildq ([e: [a, b, c]], splice (e) + splice (e));
(%o1)                    2 c + 2 b + 2 a
(%i2) buildq ([e: [a, b, c]], 2 * splice (e));
(%o2)                        2 a b c
```


*L*の中の変数は並列にバインドされます;
もし順次バインドされたなら、
最初の結果は、`foo (b, b)`になったはずです。
代入は並列に実行されます;
二番目の結果を`subst`の結果と比較してください。
`subst`は代入を順次実行します。










```maxima
(%i1) buildq ([a: b, b: a], foo (a, b));
(%o1)                       foo(b, a)
(%i2) buildq ([u: v, v: w, w: x, x: y, y: z, z: u],
              bar (u, v, w, x, y, z));
(%o2)                 bar(v, w, x, y, z, u)
(%i3) subst ([u=v, v=w, w=x, x=y, y=z, z=u],
             bar (u, v, w, x, y, z));
(%o3)                 bar(u, u, u, u, u, u)
```


変数や式が左辺に、それらの値が右辺にある等式のリストを構成します。
`macroexpand`は`show_values`が返す式を表示します。









```maxima
(%i1) show_values ([L]) ::= buildq ([L], map ("=", 'L, L));
(%o1)   show_values([L]) ::= buildq([L], map("=", 'L, L))
(%i2) (a: 17, b: 29, c: 1729)$
(%i3) show_values (a, b, c - a - b);
(%o3)          [a = 17, b = 29, c - b - a = 1683]
(%i4) macroexpand (show_values (a, b, c - a - b));
(%o4)    map(=, '([a, b, c - b - a]), [a, b, c - b - a])
```


複数の引数を持つ関数が与えられたとして、
引数のいくつかが固定されたもう１つの関数を生成します。









```maxima
(%i1) curry (f, [a]) :=
        buildq ([f, a], lambda ([[x]], apply (f, append (a, x))))$
(%i2) by3 : curry ("*", 3);
(%o2)        lambda([[x]], apply(*, append([3], x)))
(%i3) by3 (a + b);
(%o3)                       3 (b + a)
```

<!-- category: Programming -->
<!-- keywords: catch -->
<!-- signatures: catch(expr_1, ..., expr_n) -->
### Function: catch (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を１つずつ評価します;
もしどれかが形式`throw (arg)`の式の評価に至るなら、
`catch`の値は`throw (arg)`の値であり、もう式は評価されません。
これの「非局所的リターン」は
入れ子の任意の深さを通過して、`throw`を含む最も近い`catch`に飛びます。
もし`throw`を含む`catch`がないなら、
エラーメッセージが印字されます。


もし引数の評価が
いかなる`throw`の評価にも至らないなら、
`catch`の値は*expr_n*の値です。



```maxima
(%i1) lambda ([x], if x < 0 then throw(x) else f(x))$
(%i2) g(l) := catch (map (''%, l))$
(%i3) g ([1, 2, 3, 7]);
(%o3)               [f(1), f(2), f(3), f(7)]
(%i4) g ([1, 2, -3, 7]);
(%o4)                          - 3
```



もし`l`が非負数だけから成るなら、
`l`の要素それぞれの`f`のリストを返します;
そうでなければ、`g`は "catches" the
first negative element of 
`l`の最初の負の要素を「キャッチ」して、それを「スロー」します。

<!-- category: Programming -->
<!-- keywords: compfile -->
<!-- signatures: compfile(filename, f_1, ..., f_n), compfile(filename, functions), compfile(filename, all) -->
### Function: compfile (filename, f_1, ..., f_n)

Maxima関数をLispに翻訳し、翻訳したコードをファイル*filename*に書き込みます。


`compfile(filename, f_1, ..., f_n)`は
指定された関数を翻訳します。
`compfile (filename, functions)`と
`compfile (filename, all)`はユーザー定義関数をすべて翻訳します。


Lisp翻訳は評価されず、出力ファイルはLispコンパイラによって処理もされません。

`translate`はLisp翻訳を生成し評価します。
`compile_file`はMaximaをLispに翻訳し、Lispコンパイラを実行します。


`translate`, `translate_file`, `compile_file`も参照してください。

<!-- category: Programming -->
<!-- keywords: compile -->
<!-- signatures: compile(f_1, ..., f_n), compile(functions), compile(all) -->
### Function: compile (f_1, ..., f_n)

Maxima関数*f_1*, ..., *f_n*をLispに翻訳し、
Lisp翻訳を評価し、
翻訳された関数それぞれについてLisp関数`COMPILE`をコールします。
`compile`は、コンパイルされた関数名のリストを返します。


`compile (all)`や`compile (functions)`は、
ユーザー定義関数すべてをコンパイルします。


`compile`は引数をクォートします; 
クォートクォート演算子`''`はクォートに優先します。

<!-- category: Programming -->
<!-- keywords: compile_file -->
<!-- signatures: compile_file(filename), compile_file(filename, compiled_filename), compile_file(filename, compiled_filename, lisp_filename) -->
### Function: compile_file (filename)

Maximaファイル*filename*をLispに翻訳し、Lispコンパイラを実行し、
もし翻訳とコンパイルが成功したら、コンパイルされたコードをMaximaにロードします。


`compile_file`は４つのファイル名のリストを返します:
元のMaximaファイル、Lisp翻訳、翻訳時ノート、コンパイルされたコード。
もしコンパイルが失敗したら、4番目の項目は`false`です。


Lispコードがコンパイルされると(コンパイルされたコードをロードすることなしに)すぐに
いくつかの宣言と定義は効力を発揮します。
これらは`:=`演算子で定義された関数、
`::=`演算子で定義されたマクロ、

`alias`, `declare`,
`define_variable`,  `mode_declare`,
`infix`, `matchfix`,
`nofix`, `postfix`, `prefix`,
`compfile`
を含みます。


コンパイルされたコードがロードされるまで
割り当てと関数コールは評価されません。
特に、Maximaファイルの中で、
(`tr_numer`, など)翻訳フラグへの割り当ては翻訳時に効果を持ちません。







*filename*は`:lisp`文を含むことができません。


`compile_file`は引数を評価します。

<!-- category: Programming -->
<!-- keywords: declare_translated -->
<!-- signatures: declare_translated(f_1, f_2, ...) -->
### Function: declare_translated (f_1, f_2, ...)

MaximaコードのファイルをLispに翻訳する時、
ファイルの中で見る関数が翻訳された関数としてコールされるか、コンパイルされた関数としてコールされるか、また、どの関数がMaxima関数か未定義なのか、翻訳器が知ることは重要です。
この宣言をファイルの先頭に置くことは、
たとえまだLisp関数値を持たないシンボルがコール時にそれを持つだろうが、
それを知らせます。
`fn`がLisp関数になるつもりであることを翻訳器が知らない時、
`(MFUNCTION-CALL fn arg1 arg2 ...)`が生成されます。

<!-- category: Programming -->
<!-- keywords: define -->
<!-- signatures: define(f(x_1, ..., x_n), expr), define(f[x_1, ..., x_n], expr), define(funmake(f, [x_1, ..., x_n]), expr), define(arraymake(f, [x_1, ..., x_n]), expr), define(ev(expr_1), expr_2) -->
### Function: define (f(x_1, ..., x_n), expr)

引数*x_1*, ..., *x_n*を持ち、
*expr*の中身を持つ*f*という名前の関数を定義します。
`define`は、いつも（陽にクオートされていない限り）、２番目の引数を評価します。
定義された関数は、（かっこでくくられた引数を持つ）通常のMaxima関数
もしくは（カギ括弧でくくられた引数を持つ）配列関数です。


最後の関数の引数*x_n*が要素１つのリストの時、
`define`によって定義される関数は、可変な数の引数を受け入れます。
実際の引数は、形式的な引数, *x_1*, ..., *x_(n - 1)*に１対１に割り当てられます。
実際の引数がさらに存在するなら*x_n*にリストとして割り当てられます。


`define`の最初の引数が`f(x_1, ..., x_n)`もしくは
`f[x_1, ..., x_n]`の形の式の時、
関数の引数は評価されますが、既にその名前の関数や変数があったとしても*f*は評価されません。


最初の引数が演算子`funmake`もしくは`arraymake`, `ev`を伴う式の時、
最初の引数は評価されます；これは、本体だけでなく、関数名が計算されることを許します。


すべての関数定義は同じ名前空間で現れます;
関数gの中で関数`f`を定義することは、`f`のスコープを`g`に自動的に限定することにはなりません。
しかしながら、`local(f)`は、関数`f`の定義を、
`local`が現れたブロックや他の合成式内部でのみ有効とします。


もしある形式的な引数*x_k*が（評価の後）クォートされたシンボルならば、
`define`によって定義される関数は、対応する実際の引数を評価しません。
そうでければ、すべての実際の引数は評価されます。


`:=`や`::=`も参照してください。


例:


`define`は、(陽にクォートされない限り)いつも二番目の引数を評価します










```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) define (F1 (x, y), expr);
(%o2)              F1(x, y) := cos(y) - sin(x)
(%i3) F1 (a, b);
(%o3)                    cos(b) - sin(a)
(%i4) F2 (x, y) := expr;
(%o4)                   F2(x, y) := expr
(%i5) F2 (a, b);
(%o5)                    cos(y) - sin(x)
```


`define`が定義する関数は、通常のMaxima関数も配列関数も取り得ます。







```maxima
(%i1) define (G1 (x, y), x.y - y.x);
(%o1)               G1(x, y) := x . y - y . x
(%i2) define (G2 [x, y], x.y - y.x);
(%o2)                G2     := x . y - y . x
                       x, y
```


最後の、または唯一の引数*x_n*が１要素のリストの時、
`define`が定義した関数は可変の数の引数を受け付けます。







```maxima
(%i1) define (H ([L]), '(apply ("+", L)));
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


最初の引数が
演算子`funmake`, `arraymake`, または`ev`を含む式なら、
最初の引数は評価されます。











```maxima
(%i1) [F : I, u : x];
(%o1)                        [I, x]
(%i2) funmake (F, [u]);
(%o2)                         I(x)
(%i3) define (funmake (F, [u]), cos(u) + 1);
(%o3)                  I(x) := cos(x) + 1
(%i4) define (arraymake (F, [u]), cos(u) + 1);
(%o4)                   I  := cos(x) + 1
                         x
(%i5) define (foo (x, y), bar (y, x));
(%o5)                foo(x, y) := bar(y, x)
(%i6) define (ev (foo (x, y)), sin(x) - cos(y));
(%o6)             bar(y, x) := sin(x) - cos(y)
```

<!-- category: Programming -->
<!-- keywords: define_variable -->
<!-- signatures: define_variable(name, default_value, mode) -->
### Function: define_variable (name, default_value, mode)

グローバル変数をMaxima環境に導入します。


`define_variable`は、ユーザーが書いたパッケージで役に立ちます。
パッケージはしばしば翻訳されたりコンパイルされたりします。


`define_variable`は以下のステップを実行します:



1. `mode_declare (name, mode)`は、
*name*のモードを翻訳器に宣言します。
可能なモードのリストについては、`mode_declare`を参照してください。
2. もし変数がバインドされていなければ、*default_value*が*name*に割り当てられます。
3. `declare (name, special)`はそれをspecialと宣言します。
4. *name*が宣言されたモードのただ１つの割り当てられた値であることを
保証するために、
*name*をテスト関数に関連づけます。















`value_check`プロパティは、
`define_variable`を介して
`any`以外のモードに定義された任意の変数に割り当てられることができます。
`value_check`プロパティは、１変数のラムダ式または関数名です。
それは値を変数に割り当てようとする時にコールされます。
`value_check`関数の引数は期待値です。


`define_variable`は`default_value`を評価し、
`name`と`mode`をクォートします。
`define_variable`は`name`の現在値を返します。
それは、もし`name`がそこでバインドされてないなら`default_value`で
そうでないなら`name`の以前の値です。


例:


`foo`はブーリアン変数で、初期値`true`を持ちます。










```maxima
(%i1) define_variable (foo, true, boolean);
(%o1)                         true
(%i2) foo;
(%o2)                         true
(%i3) foo: false;
(%o3)                         false
(%i4) foo: %pi;
Error: foo was declared mode boolean, has value: %pi
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) foo;
(%o5)                         false
```


`bar`は整数変数で、素数でなければいけません。












```maxima
(%i1) define_variable (bar, 2, integer);
(%o1)                           2
(%i2) qput (bar, prime_test, value_check);
(%o2)                      prime_test
(%i3) prime_test (y) := if not primep(y) then
                           error (y, "is not prime.");
(%o3) prime_test(y) := if not primep(y)

                                   then error(y, "is not prime.")
(%i4) bar: 1439;
(%o4)                         1439
(%i5) bar: 1440;
1440 is not prime.
#0: prime_test(y=1440)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) bar;
(%o6)                         1439
```


`baz_quux`は、値を割り当てられない変数です。
モード`any_check`は`any`のようですが、
`any_check`は`value_check`メカニズムを可能にしますが、
`any`はそうしません。












```maxima
(%i1) define_variable (baz_quux, 'baz_quux, any_check);
(%o1)                       baz_quux
(%i2) F: lambda ([y], if y # 'baz_quux then
                 error ("Cannot assign to `baz_quux'."));
(%o2) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i3) qput (baz_quux, ''F, value_check);
(%o3) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i4) baz_quux: 'baz_quux;
(%o4)                       baz_quux
(%i5) baz_quux: sqrt(2);
Cannot assign to `baz_quux'.
#0: lambda([y],if y # 'baz_quux then
                 error("Cannot assign to `baz_quux'."))(y=sqrt(2))
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) baz_quux;
(%o6)                       baz_quux
```

<!-- category: Programming -->
<!-- keywords: dispfun -->
<!-- signatures: dispfun(f_1, ..., f_n), dispfun(all) -->
### Function: dispfun (f_1, ..., f_n)

ユーザー定義関数*f_1*, ..., *f_n*の定義を表示します。
引数それぞれは、(`::=`で定義された)マクロ名、
(`:=`や`define`で定義された)通常の関数、
(`:=`y`define`で定義された、しかし引数をカギ括弧`[ ]`でくくった)
配列関数、
(`:=`y`define`で定義された、しかしいくつかの引数をカギ括弧`[ ]`で、他の引数を括弧`( )`でくくった)添字付き関数、
特別な添字の値で選択された添字付き関数の族の１つ、
定数添字で定義された添字付き関数、
のいずれかを取り得ます。


`dispfun (all)`は、
`functions`, `arrays`, `macros`リストで与えられた中で、
定数添字で定義された添字付き関数を除いたユーザー定義関数すべてを表示します。


`dispfun`は
表示された関数それぞれのために
(`%t1`, `%t2`, など)
中間式ラベルを生成し、関数定義をラベルに割り当てます。
対照的に、`fundef`は関数定義を返します。


`dispfun`は引数をクォートします; 
クォートクォート演算子`''`はクォートに優先します。
`dispfun`は表示された関数に対応する中間式ラベルのリストを返します。


例:












```maxima
(%i1) m(x, y) ::= x^(-y);
                                     - y
(%o1)                   m(x, y) ::= x
(%i2) f(x, y) :=  x^(-y);
                                     - y
(%o2)                    f(x, y) := x
(%i3) g[x, y] :=  x^(-y);
                                    - y
(%o3)                     g     := x
                           x, y
(%i4) h[x](y) :=  x^(-y);
                                    - y
(%o4)                     h (y) := x
                           x
(%i5) i[8](y) :=  8^(-y);
                                    - y
(%o5)                     i (y) := 8
                           8
(%i6) dispfun (m, f, g, h, h[5], h[10], i[8]);
                                     - y
(%t6)                   m(x, y) ::= x

                                     - y
(%t7)                    f(x, y) := x


                                    - y
(%t8)                     g     := x
                           x, y

                                    - y
(%t9)                     h (y) := x
                           x

                                    1
(%t10)                     h (y) := --
                            5        y
                                    5

                                     1
(%t11)                    h  (y) := ---
                           10         y
                                    10

                                    - y
(%t12)                    i (y) := 8
                           8

(%o12)       [%t6, %t7, %t8, %t9, %t10, %t11, %t12]
(%i12) ''%;
                     - y              - y            - y
(%o12) [m(x, y) ::= x   , f(x, y) := x   , g     := x   , 
                                            x, y
                  - y           1              1             - y
        h (y) := x   , h (y) := --, h  (y) := ---, i (y) := 8   ]
         x              5        y   10         y   8
                                5             10
```

<!-- category: Programming -->
<!-- keywords: fullmap -->
<!-- signatures: fullmap(f, expr_1, ...) -->
### Function: fullmap (f, expr_1, ...)

`map`と似ていますが、`fullmap`は、主演算子が同じでなくなるまで、
部分式すべてに再帰的にマッピングを続けます。


`fullmap`は、ある行列操作のための整理に使われています;
このように、Maximaは時々、たとえ`fullmap`がユーザーに陽にコールされなくても、
`fullmap`に関係したエラーメッセージを生成します。


例:








```maxima
(%i1) a + b * c;
(%o1)                        b c + a
(%i2) fullmap (g, %);
(%o2)                   g(b) g(c) + g(a)
(%i3) map (g, %th(2));
(%o3)                     g(b c) + g(a)
```

<!-- category: Programming -->
<!-- keywords: fullmapl -->
<!-- signatures: fullmapl(f, list_1, ...) -->
### Function: fullmapl (f, list_1, ...)

`fullmap`に似ていますが、`fullmapl`はリストや行列にのみマップします。


例:






```maxima
(%i1) fullmapl ("+", [3, [4, 5]], [[a, 1], [0, -1.5]]);
(%o1)                [[a + 3, 4], [4, 3.5]]
```

<!-- category: Programming -->
<!-- keywords: functions -->
<!-- signatures: functions -->
### Variable: functions

デフォルト値: `[]`


`functions`は、現在のセッションでの通常のMaxima関数のリストです。
通常の関数は、`define`や`:=`で構成された関数であり、
括弧`()`でコールされます。
関数はMaximaプロンプトで定義することができ、また、
`load`や`batch`がロードするMaximaファイルの中で定義することができます。


(例えば`F[x]`のように、カギ括弧でコールされる)配列関数と
(例えば`F[x](y)`のように、カギ括弧と括弧でコールされる)添字付き関数は、
`functions`ではなくグローバル変数`arrays`にリストされます。


Lisp関数はどのリストにも保持されません。


例:














```maxima
(%i1) F_1 (x) := x - 100;
(%o1)                   F_1(x) := x - 100
(%i2) F_2 (x, y) := x / y;
                                      x
(%o2)                    F_2(x, y) := -
                                      y
(%i3) define (F_3 (x), sqrt (x));
(%o3)                   F_3(x) := sqrt(x)
(%i4) G_1 [x] := x - 100;
(%o4)                    G_1  := x - 100
                            x
(%i5) G_2 [x, y] := x / y;
                                     x
(%o5)                     G_2     := -
                             x, y    y
(%i6) define (G_3 [x], sqrt (x));
(%o6)                    G_3  := sqrt(x)
                            x
(%i7) H_1 [x] (y) := x^y;
                                      y
(%o7)                     H_1 (y) := x
                             x
(%i8) functions;
(%o8)              [F_1(x), F_2(x, y), F_3(x)]
(%i9) arrays;
(%o9)                 [G_1, G_2, G_3, H_1]
```

<!-- category: Programming -->
<!-- keywords: fundef -->
<!-- signatures: fundef(f) -->
### Function: fundef (f)

関数*f*の定義を返します。



引数は、(`::=`で定義された）マクロの名前か、
(`:=`もしくは`define`で定義された）通常の関数か、
(`:=`や`define`で定義され、引数がカギ括弧でくくられた）配列関数か、
(`:=`や`define`で定義され、いくつかの引数がカギ括弧でくくられ、残りがかっこでくくられた）添字関数か、
特別な添字の値によって選択された添字関数族の１つか、一定の添字で定義された添字関数です。


`fundef`は引数をクォートします;
クォートクォート演算子`''`はクォートに優先します。


`fundef (f)`は*f*の定義を返します。
対照的に、`dispfun (f)`は中間式ラベルを生成し、ラベルに定義を割り当てます。

<!-- category: Programming -->
<!-- keywords: funmake -->
<!-- signatures: funmake(F, [arg_1, ..., arg_n]) -->
### Function: funmake (F, [arg_1, ..., arg_n])

式`F(arg_1, ..., arg_n)`を返します。
戻り値は整理されますが、評価されません。
だから関数*F*はたとえ存在してもコールされません。


`funmake`は配列関数と通常の関数を区別しようとしません;
*F*が配列関数名の時、
`funmake`は`F(...)`を返します
(すなわち、カギ括弧の代わりに括弧での関数コール)。
`arraymake`は、この場合，カギ括弧での関数コールを返します。


`funmake`は引数を評価します。


例:


通常のMaxima関数に適用された`funmake`。








```maxima
(%i1) F (x, y) := y^2 - x^2;
                                   2    2
(%o1)                  F(x, y) := y  - x
(%i2) funmake (F, [a + 1, b + 1]);
(%o2)                    F(a + 1, b + 1)
(%i3) ''%;
                              2          2
(%o3)                  (b + 1)  - (a + 1)
```


マクロに適用された`funmake`。








```maxima
(%i1) G (x) ::= (x - 1)/2;
                                  x - 1
(%o1)                    G(x) ::= -----
                                    2
(%i2) funmake (G, [u]);
(%o2)                         G(u)
(%i3) ''%;
                              u - 1
(%o3)                         -----
                                2
```


添字付き関数に適用された`funmake`。










```maxima
(%i1) H [a] (x) := (x - 1)^a;
                                        a
(%o1)                   H (x) := (x - 1)
                         a
(%i2) funmake (H [n], [%e]);
                                       n
(%o2)               lambda([x], (x - 1) )(%e)
(%i3) ''%;
                                    n
(%o3)                       (%e - 1)
(%i4) funmake ('(H [n]), [%e]);
(%o4)                        H (%e)
                              n
(%i5) ''%;
                                    n
(%o5)                       (%e - 1)
```


いかなる種類の関数にも定義されていないシンボルへ適用された
`funmake`







```maxima
(%i1) funmake (A, [u]);
(%o1)                         A(u)
(%i2) ''%;
(%o2)                         A(u)
```


`funmake`は引数を評価しますが、戻り値を評価しません。










```maxima
(%i1) det(a,b,c) := b^2 -4*a*c;
                                    2
(%o1)              det(a, b, c) := b  - 4 a c
(%i2) (x : 8, y : 10, z : 12);
(%o2)                          12
(%i3) f : det;
(%o3)                          det
(%i4) funmake (f, [x, y, z]);
(%o4)                    det(8, 10, 12)
(%i5) ''%;
(%o5)                         - 284
```


Maximaは`funmake`の戻り値を整理します。






```maxima
(%i1) funmake (sin, [%pi / 2]);
(%o1)                           1
```

<!-- category: Programming -->
<!-- keywords: lambda -->
<!-- signatures: lambda([x_1, ..., x_m], expr_1, ..., expr_n), lambda([[L]], expr_1, ..., expr_n), lambda([x_1, ..., x_m, [L]], expr_1, ..., expr_n) -->
### Function: lambda ([x_1, ..., x_m], expr_1, ..., expr_n)

ラムダ式 (すなわち、匿名関数)を定義し返します。
関数は要求された引数*x_1*, ..., *x_m*を持ち、
また、オプション引数*L*を持つかもしれません。オプション引数は関数本体の中にリストとして現れます。
関数の戻り値は*expr_n*です。
ラムダ式は変数に割り当てることができ、通常の関数のように評価できます。
ラムダ式は関数名が期待されるいくつかのコンテキストで現れるかもしれません。


関数が評価される時、
バインドされていないローカル変数*x_1*, ..., *x_m*が生成されます。
`lambda`は
`block`の中や別の`lambda`の中で現れるかもしれません;
ローカル変数は、別の`block`や`lambda`が評価される度に毎回確立されます。
ローカル変数は内包する`block`や`lambda`にはグローバルのように見えます。
もし変数がローカルでないなら、
その値は、(もし割り当てられたなら)内包する`block`や`lambda`で直近に割り当てられた値です。
そうでなければ、グローバル環境での変数の値です。
このポリシーは「動的スコープ」の普通の理解と一致するかもしれません。


ローカル変数が確立された後、
*expr_1*から*expr_n*までが順に評価されます。
特殊変数`%%`―直前の式の値を表します―が認識されます。
`throw`と`catch`も式のリストの中に現れるかもしれません。


`block`で囲まれない限り
`return`はラムダ式の中には現れません。
`block`で囲まれた場合、
ブロックがたまたま *expr_n*に至るということでない限り、
`return`はラムダ式の戻り値ではなくブロックの戻り値を定義します。
同様に、`go`は、`block`で囲まれない限りラムダ式の中に現れません。


`lambda`は引数をクォートします;
クォートクォート演算子`''`はクォートに優先します。


例:



- *
ラムダ式は変数に割り当てることができ、通常の関数のように評価できます。







```maxima
(%i1) f: lambda ([x], x^2);
                                      2
(%o1)                    lambda([x], x )
(%i2) f(a);
                                2
(%o2)                          a
```


- *
ラムダ式は
関数評価が期待される文脈で現れるかもしれません。








```maxima
(%i3) lambda ([x], x^2) (a);
                                2
(%o3)                          a
(%i4) apply (lambda ([x], x^2), [a]);
                                2
(%o4)                          a
(%i5) map (lambda ([x], x^2), [a, b, c, d, e]);
                        2   2   2   2   2
(%o5)                 [a , b , c , d , e ]
```


- *
引数変数はローカル変数です。
他の変数はグローバル変数のように見えます。
ある特殊な評価が`''`のようにある方法で強制されない限り、
グローバル変数はラムダ式が評価される時評価されます。













```maxima
(%i6) a: %pi$
(%i7) b: %e$
(%i8) g: lambda ([a], a*b);
(%o8)                   lambda([a], a b)
(%i9) b: %gamma$
(%i10) g(1/2);
                             %gamma
(%o10)                       ------
                               2
(%i11) g2: lambda ([a], a*''b);
(%o11)                lambda([a], a %gamma)
(%i12) b: %e$
(%i13) g2(1/2);
                             %gamma
(%o13)                       ------
                               2
```


- *
ラムダ式は入れ子にできます。
外側のラムダ式の中のローカル変数は、
同じ名前のローカル変数がマスクしない限り、
内側の式にはグローバルに見えます。







```maxima
(%i14) h: lambda ([a, b], h2: lambda ([a], a*b), h2(1/2));
                                                   1
(%o14)    lambda([a, b], h2 : lambda([a], a b), h2(-))
                                                   2
(%i15) h(%pi, %gamma);
                             %gamma
(%o15)                       ------
                               2
```


- *
`lambda`は引数をクォートするので、
以下のラムダ式`i`は
"`a`を掛ける"関数を定義しません。
以下のラムダ式`i2`のように、
そんな関数は`buildq`を介して定義することができます。










```maxima
(%i16) i: lambda ([a], lambda ([x], a*x));
(%o16)            lambda([a], lambda([x], a x))
(%i17) i(1/2);
(%o17)                  lambda([x], a x)
(%i18) i2: lambda([a], buildq([a: a], lambda([x], a*x)));
(%o18)    lambda([a], buildq([a : a], lambda([x], a x)))
(%i19) i2(1/2);
                                     x
(%o19)                   lambda([x], -)
                                     2
(%i20) i2(1/2)(%pi);
                               %pi
(%o20)                         ---
                                2
```


- *
ラムダ式は、可変の数の引数を取ることができます。
それは、唯一のまたは最後の引数として`[L]`で指定されます。
引数は関数本体の中にリストとして現れます。









```maxima
(%i1) f : lambda ([aa, bb, [cc]], aa * cc + bb);
(%o1)          lambda([aa, bb, [cc]], aa cc + bb)
(%i2) f (foo, %i, 17, 29, 256);
(%o2)       [17 foo + %i, 29 foo + %i, 256 foo + %i]
(%i3) g : lambda ([[aa]], apply ("+", aa));
(%o3)             lambda([[aa]], apply(+, aa))
(%i4) g (17, 29, x, y, z, %e);
(%o4)                  z + y + x + %e + 46
```

<!-- category: Programming -->
<!-- keywords: local -->
<!-- signatures: local(v_1, ..., v_n) -->
### Function: local (v_1, ..., v_n)

シンボル*v_1*, ..., *v_n*に関連付けられた性質を保存し、
他の式を評価する前にすべての性質を取り除き、
`local`が現れたブロックや他の合成式の終了時に保存した性質を元に戻します。


いくつかの宣言は、`:=`、`array`, `dependencies`, `atvalue`, `matchdeclare`,
 `atomgrad`, `constant`, `nonscalar`その他を含むシンボルの性質として実装されます。
`local`の効果は、ブロック内部のみで有効な宣言を作ります;
そうでなければ、ブロック内部の宣言は実際にグローバル宣言となります。


`local`は、`block`や関数定義の本体や`lambda`式の中に現れます。
それぞれの中で１カ所だけ許されます。


`local`は引数をクォートします。
`local`は`done`を返します。


例:


ローカル関数定義。









```maxima
(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x
(%i2) foo (100);
(%o2)                         - 99
(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200
(%i4) foo (100);
(%o4)                         - 99
```

<!-- category: Programming -->
<!-- keywords: macroexpand -->
<!-- signatures: macroexpand(expr) -->
### Function: macroexpand (expr)

`expr`がマクロ関数コールの時、
*expr*のマクロ展開を、評価はせずに、返します。
そうでなければ、`macroexpand`は*expr*を返します。


もし*expr*の展開が別のマクロ関数コールをもたらすなら、
そのマクロ関数コールも展開されます。


`macroexpand`は引数をクォートします。
しかしながら、もしマクロ関数コールの展開が副作用を持つなら，
それらの副作用が実行されます。


`::=`, `macros`, `macroexpand1`も参照してください。


例










```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand (h (y));
                              y - a
(%o4)                         -----
                               99
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

<!-- category: Programming -->
<!-- keywords: macroexpand1 -->
<!-- signatures: macroexpand1(expr) -->
### Function: macroexpand1 (expr)

`expr`がマクロ関数コールの時、
*expr*のマクロ展開を、評価せずに、返します。
そうでなければ、`macroexpand1`は*expr*を返します。


`macroexpand`は引数をクォートします。
しかしながら、もしマクロ関数コールの展開が副作用を持つなら，
それらの副作用が実行されます。


もし*expr*の展開が別のマクロ関数コールをもたらすなら、
そのマクロ関数コールは展開されません。


`::=`, `macros`, `macroexpand`も参照してください。


例










```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand1 (h (y));
(%o4)                       g(y - a)
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

<!-- category: Programming -->
<!-- keywords: macroexpansion -->
<!-- signatures: macroexpansion -->
### Variable: macroexpansion

デフォルト値: `false`


`macroexpansion`は
マクロ関数コールを
マクロ関数の展開(すなわち戻り値)で
置き換えるかどうかを制御します。
展開を記憶する代価で、置き換えは次の式評価をスピードアップするかもしれません。



**false** — マクロ関数コールをマクロ関数の展開で置き換えられません。
**expand** — マクロ関数コールが初めて評価された時、展開が記憶されます。
展開は次のコール時に再計算されません;
(`print`やグローバル変数への割り当てのような)いかなる副作用も
最初にマクロ関数コールが評価された時だけ起こります。
式の中の展開は、同じマクロ関数コールを持つ他の式に影響を与えません。
**displace** — マクロ関数コールが初めて評価された時、展開でコールを置き換え、
マクロ関数がコールされた式を変更します。
展開は次のコールで再計算されません;
(`print`やグローバル変数への割り当てのような)いかなる副作用も
最初にマクロ関数コールが評価された時だけ起こります。
式の中の展開は、同じマクロ関数コールを持つ他の式に影響を与えません。


例


`macroexpansion`が`false`の時、
コールする式が評価される時毎回マクロ関数がコールされ、
コールする式は変更されません。














```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: false;
(%o4)                         false
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o7)                       --------
                            a b + 99
```


`macroexpansion`が`expand`の時、
マクロ関数は一度コールされ、
コールする式は変更されません。














```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: expand;
(%o4)                        expand
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```


`macroexpansion`が`expand`の時、
マクロ関数は一度コールされ、
コールする式が変更されます。














```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: displace;
(%o4)                       displace
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                 x - 99
(%t6)                    f(x) := ------
                                 x + 99

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```

<!-- category: Programming -->
<!-- keywords: macros -->
<!-- signatures: macros -->
### Variable: macros

デフォルト値: `[]`


`macros`は、ユーザー定義のマクロ関数のリストです。
マクロ関数定義演算子`::=`は、このリストに新しいマクロ関数を入れ、
`kill`, `remove`, `remfunction`はリストからマクロ関数を削除します。


`infolists`も参照してください。

<!-- category: Programming -->
<!-- keywords: mode_check_errorp -->
<!-- signatures: mode_check_errorp -->
### Variable: mode_check_errorp

デフォルト値: `false`



`mode_check_errorp`が`true`の時、
`mode_declare`はエラーをコールします。

<!-- category: Programming -->
<!-- keywords: mode_check_warnp -->
<!-- signatures: mode_check_warnp -->
### Variable: mode_check_warnp

デフォルト値: `true`



`mode_check_warnp`が`true`の時、
モードエラーが記述されます。

<!-- category: Programming -->
<!-- keywords: mode_checkp -->
<!-- signatures: mode_checkp -->
### Variable: mode_checkp

デフォルト値: `true`



`mode_checkp`が`true`の時、
`mode_declare`はバインドされた変数のモードをチェックします。

<!-- category: Programming -->
<!-- keywords: mode_declare -->
<!-- signatures: mode_declare(y_1, mode_1, ..., y_n, mode_n) -->
### Function: mode_declare (y_1, mode_1, ..., y_n, mode_n)

`mode_declare`は、
その後の関数の翻訳やコンパイルのために
変数と関数のモードを宣言するのに使われます。
`mode_declare`は、通常、
関数定義の始めやMaximaスクリプトの始めに置かれたり、対話プロンプトで実行されたりします。


`mode_declare`の引数は、
変数とモードから成る対です。
モードは
`boolean`, `fixnum`, `number`, `rational`, `float`のいずれか１つです。
変数それぞれは、
同じモードを持つように宣言される変数すべてのリストも取り得ます。



もし変数が配列で、かつ、参照される配列のすべての要素が値を持つなら、
なら、


```maxima
array(yi, dim1, dim2, ...)
```

よりむしろ`array (yi, complete, dim1, dim2, ...)`を
最初に配列のバインドを宣言する時に使うべきです。

もし配列の要素すべてが
モード`fixnum` (`float`)なら、
`complete`の代わりに`fixnum` (`float`)を使ってください。

もし配列のすべての要素が同じモード―`m`としましょう―なら、
効率的な翻訳のためには、



```maxima
mode_declare (completearray (yi), m))
```


を使うべきです。


配列を使う数値コードは、例えば、10 x 10の浮動小数点配列のために



```maxima
mode_declare (completearray (a [10, 10]), float)
```


というように、期待される配列サイズを宣言することでより速く実行されるかもしれません


引数として`function (f_1, f_2, ...)`を使うことで
関数の結果のモードを宣言することができます;
ここで`f_1`, `f_2`, ...は関数名です。
例えば、式



```maxima
mode_declare ([function (f_1, f_2, ...)], fixnum)
```


は、
`f_1`, `f_2`, ...が返す値が1ワード整数であることを宣言します。


`modedeclare`は`mode_declare`と同義です。

<!-- category: Programming -->
<!-- keywords: mode_identity -->
<!-- signatures: mode_identity(arg_1, arg_2) -->
### Function: mode_identity (arg_1, arg_2)

`mode_declare`と`macros`で
例えば、flonumsのリストのリストや他の合成データオブジェクトを宣言するのに
使われる特殊形式。
`mode_identity`の最初の引数は、`mode_declare`に与えられるような
プリミティブな値モード名(すなわち、`float`, `fixnum`, `number`,
`list`, `any`のいずれか)であり、
二番目の引数は、評価され、`mode_identity`の値として返される式です。
しかしながら、もし戻り値が最初の引数で宣言されたモードによって許されていないなら、
エラーか警告がシグナルされます。
重要なことは、MaximaによってLisp翻訳器に命じた式のモードが、二番目の引数のなかで続く一切から独立して、最初の引数として与えられるそれだということです。
例えば、`x: 3.3; mode_identity (fixnum, x);`はエラーをもたらします。
`mode_identity (flonum, x)`は3.3を返します。
これは多くの使い道があります。例えば、もし`first (l)`が数を返すと知っていたなら、
`mode_identity (number, first (l))`と書くかもしれません。
しかしながら、それをするもっと効率的な方法は、



```maxima
firstnumb (x) ::= buildq ([x], mode_identity (number, first(x)));
```


のように新しいプリミティブを定義し、
そして数のリストの最初の要素を取る時毎回`firstnumb`を使うことです。

<!-- category: Programming -->
<!-- keywords: remfunction -->
<!-- signatures: remfunction(f_1, ..., f_n), remfunction(all) -->
### Function: remfunction (f_1, ..., f_n)

シンボル*f_1*, ..., *f_n*の関数定義をアンバインドします。
引数は、（`:=`もしくは`define`で生成された）通常の関数名もしくは（`::=`で生成された）マクロ関数をとります。


`remfunction (all)`は関数定義すべてをアンバインドします。


`remfunction`は引数をクォートします。


`remfunction`は、関数定義はアンバインドされたシンボルのリストを返します。
シンボルに関数定義がなければ、シンボルの代わりに`false`を返します。


`remfunction`は配列関数すなわち添字付き関数には適用されません。
これらのタイプの関数には`remarray`を適用します。

<!-- category: Programming -->
<!-- keywords: savedef -->
<!-- signatures: savedef -->
### Variable: savedef

デフォルト値: `true`


`savedef`が`true`の時、
関数が解釈される時に
ユーザー関数のMaximaバージョンが保持されます。
これは、定義が`dispfun`によって表示されることを許し、
関数が編集されることを許します。


`savedef`が`false`の時、
解釈された関数の名前は、`functions`リストから取り除かれます。

<!-- category: Programming -->
<!-- keywords: splice -->
<!-- signatures: splice(a) -->
### Function: splice (a)

`splice`が`buildq`内部に現れた時だけ、
アトム*a*で指名されたリストを式に接合(内挿)します;
そうでなければ、`splice`は未定義関数として扱われます。
もし
`buildq`内部で
*a*単独として(`splice`なしに)現れたら、
*a*はリストとして、結果の中に代入されます(内挿されません)。
`splice`の引数はアトムだけを取り得ます;
リストリテラルやリストをもたらす式を取ることはできません。


通常、`splice`は、関数や演算子の引数を提供します。
関数`f`に対して、
`buildq`内部の式`f (splice (a))`は、
`f (a[1], a[2], a[3], ...)`に展開されます。
演算子`o`に対して、
`buildq`内部の式`"o" (splice (a)`は、
`"o" (a[1], a[2], a[3], ...)`に展開されます。
ここで`o`は、任意のタイプの演算子を取り得ます(通常は複数の引数を取るものです)。
演算子はダブルクォート`"`でくくられなければいけないことに注意してください。


例









```maxima
(%i1) buildq ([x: [1, %pi, z - y]], foo (splice (x)) / length (x));
                       foo(1, %pi, z - y)
(%o1)                -----------------------
                     length([1, %pi, z - y])
(%i2) buildq ([x: [1, %pi]], "/" (splice (x)));
                                1
(%o2)                          ---
                               %pi
(%i3) matchfix ("<>", "<>");
(%o3)                          <>
(%i4) buildq ([x: [1, %pi, z - y]], "<>" (splice (x)));
(%o4)                   <>1, %pi, z - y<>
```

<!-- category: Programming -->
<!-- keywords: tr_array_as_ref -->
<!-- signatures: tr_array_as_ref -->
### Variable: tr_array_as_ref

デフォルト値: `true`


もし`translate_fast_arrays`が`false`なら、
`translate_file`が発行するLispコードの中の配列参照は、
`tr_array_as_ref`によって影響されます。
`tr_array_as_ref`が`true`の時、
配列名は評価されます。
そうでなければ、配列名は翻訳されたコードの中で文字リテラルとして現れます。


もし`translate_fast_arrays`が`true`なら、
`tr_array_as_ref`は効果を持ちません。

<!-- category: Programming -->
<!-- keywords: tr_bound_function_applyp -->
<!-- signatures: tr_bound_function_applyp -->
### Variable: tr_bound_function_applyp

デフォルト値: `true`


`tr_bound_function_applyp`が`true`の時、
もし(関数引数のような)バインドされた変数が関数として使われていることが見つかったら
Maximaは警告を与えます。

`tr_bound_function_applyp`は、
そんな場合に生成されたコードに影響しません。


例えば、
`g (f, x) := f (x+1)`のような式は警告メッセージをトリガーします。

<!-- category: Programming -->
<!-- keywords: tr_file_tty_messagesp -->
<!-- signatures: tr_file_tty_messagesp -->
### Variable: tr_file_tty_messagesp

デフォルト値: `false`


`tr_file_tty_messagesp`が`true`の時、
ファイルの翻訳中に
`translate_file`が生成するメッセージがコンソールに表示され、
`false`の時、ファイルの翻訳に関するメッセージは
UNLISPファイルに挿入されるだけです。

<!-- category: Programming -->
<!-- keywords: tr_float_can_branch_complex -->
<!-- signatures: tr_float_can_branch_complex -->
### Variable: tr_float_can_branch_complex

デフォルト値: `true`


Maxima-to-Lisp翻訳器に
 translator to assume that
関数`acos`, `asin`, `asec`, `acsc`が複素数の結果を返すことができることを仮定するように命じます。


`tr_float_can_branch_complex`の表面上の効果は以下の通りです。
しかしながら、このフラグは翻訳器出力上の効果を持ちません。


`true`の時、
たとえ (`mode_declare`が設定したように)`x`がモード`float`でも
`acos(x)`はモード`any`です。
`false`の時、
`x`がモード`float`の時だけ
`acos(x)`はモード`float`です。

<!-- category: Programming -->
<!-- keywords: tr_function_call_default -->
<!-- signatures: tr_function_call_default -->
### Variable: tr_function_call_default

デフォルト値: `general`


`false`は、あきらめて`meval`をコールすることを意味し、
`expr`は、引数が固定されたLisp関数を仮定することを意味します。
`general`、デフォルトは
`mexprs`や`mlexprs`にはよいが`macros`にはよくないコードを与えます。
`general`は、コンパイルされたコードの中で変数バインドが正確であることを保証します。
`general`モードでは、
F(X)を翻訳する時、もしFがバインドされた変数なら、
`apply (f, [x])`を意味すると仮定され、適切な警告と合わせてそのように翻訳されます。
これをオフにする必要はありません。
デフォルト設定で警告メッセージがないことは、
Maximaインタープリタと、翻訳、コンパイルされたコードの完全互換性を意味します。

<!-- category: Programming -->
<!-- keywords: tr_numer -->
<!-- signatures: tr_numer -->
### Variable: tr_numer

デフォルト値: `false`


`tr_numer`が`true`の時、
`numer`プロパティは
それらを持つアトム、例えば、`%pi`に使われます。

<!-- category: Programming -->
<!-- keywords: tr_optimize_max_loop -->
<!-- signatures: tr_optimize_max_loop -->
### Variable: tr_optimize_max_loop

デフォルト値: 100


`tr_optimize_max_loop`は、
翻訳器のマクロ展開と最適化パスが形式を検討する際繰り返す最大回数です。
これはマクロ展開エラーや終了しない最適化プロパティをキャッチします。

<!-- category: Programming -->
<!-- keywords: tr_semicompile -->
<!-- signatures: tr_semicompile -->
### Variable: tr_semicompile

デフォルト値: `false`


`tr_semicompile`が`true`の時、
`translate_file`と`compfile`は、
マクロ展開されたが、Lispコンパイラによって機械語にコンパイルされない形式を出力します。

<!-- category: Programming -->
<!-- keywords: tr_state_vars -->
<!-- signatures: tr_state_vars -->
### Variable: tr_state_vars

デフォルト値:


```maxima
[transcompile, tr_semicompile, tr_warn_undeclared, tr_warn_meval,
tr_warn_fexpr, tr_warn_mode, tr_warn_undefined_variable,
tr_function_call_default, tr_array_as_ref,tr_numer]
```


翻訳された出力の形式に影響するスイッチのリスト。

翻訳器をデバッグしようとする時
この情報はシステムの人たちに役に立ちます。
翻訳された生成物を与えられた状態で生成されるべきだったものと比較することによって、
バグを追跡することが可能です。

<!-- category: Programming -->
<!-- keywords: tr_warn_bad_function_calls -->
<!-- signatures: tr_warn_bad_function_calls -->
### Variable: tr_warn_bad_function_calls

デフォルト値: `true`


- 翻訳時にされた不適切な宣言のせいで正確でないかもしれない関数コールが行われている時、
警告を与えます。

<!-- category: Programming -->
<!-- keywords: tr_warn_fexpr -->
<!-- signatures: tr_warn_fexpr -->
### Variable: tr_warn_fexpr

デフォルト値: `compfile`


- もしFEXPRに遭遇したら、警告を与えます。
FEXPRは、通常、翻訳コードの中で出力されるべきではありません。
合法で特殊なプログラム形式はすべて翻訳されます。

<!-- category: Programming -->
<!-- keywords: tr_warn_meval -->
<!-- signatures: tr_warn_meval -->
### Variable: tr_warn_meval

デフォルト値: `compfile`


- もし関数`meval`がコールされたら、警告を与えます。
もし`meval`がコールされたら、それは翻訳の中の問題を示します。

<!-- category: Programming -->
<!-- keywords: tr_warn_mode -->
<!-- signatures: tr_warn_mode -->
### Variable: tr_warn_mode

デフォルト値: `all`


- 変数がそのモードに不適切な値を割り当てられた時、警告を与えます。

<!-- category: Programming -->
<!-- keywords: tr_warn_undeclared -->
<!-- signatures: tr_warn_undeclared -->
### Variable: tr_warn_undeclared

デフォルト値: `compile`


- 未宣言変数についての警告をいつTTYに送るかを決めます。

<!-- category: Programming -->
<!-- keywords: tr_warn_undefined_variable -->
<!-- signatures: tr_warn_undefined_variable -->
### Variable: tr_warn_undefined_variable

デフォルト値: `all`


- 未定義のグローバル変数が見られた時、警告を与えます。

<!-- category: Programming -->
<!-- keywords: tr_warnings_get -->
<!-- signatures: tr_warnings_get() -->
### Function: tr_warnings_get ()

現在の翻訳の間に翻訳器が与える警告のリストを印字します。

<!-- category: Programming -->
<!-- keywords: transcompile -->
<!-- signatures: transcompile -->
### Variable: transcompile

デフォルト値: `true`


`transcompile`が`true`の時、
`translate`と`translate_file`は
翻訳コードをコンパイルにより適したものにする宣言を生成します。



`compfile`は実行中`transcompile: true`を設定します。

<!-- category: Programming -->
<!-- keywords: translate -->
<!-- signatures: translate(f_1, ..., f_n), translate(functions), translate(all) -->
### Function: translate (f_1, ..., f_n)

ユーザー定義関数*f_1*, ..., *f_n*をMaxima言語からLispに翻訳し、
Lisp翻訳を評価します。
通常、翻訳された関数は元の関数より速く実行されます。


`translate (all)`や`translate (functions)`は、
ユーザー定義関数すべてを翻訳します。


翻訳される関数は、
より効率的なコードを生成するために可能な時は
先頭に`mode_declare`コールを含むべきです。
例えば:



```maxima
f (x_1, x_2, ...) := block ([v_1, v_2, ...],
    mode_declare (v_1, mode_1, v_2, mode_2, ...), ...)
```




ここで、*x_1*, *x_2*, ... は関数のパラメータであり、
*v_1*, *v_2*, ...はローカル変数です。


もし`savedef`が`false`なら(以下を参照してください)
翻訳された関数の名前は、`functions`リストから削除され、
`props`リストに加えられます。


完全にデバッグされない限り、関数は翻訳すべきではありません。


式は整理されていると仮定されます;
もしされていないなら、厳密ですが、最適でないコードが生成されます。
従って、
ユーザーは
`simp`スイッチを`false`―翻訳される式の整理を抑制します―
に設定すべきではありません。


スイッチ`translate`は、もし`true`なら、
ユーザー関数のLispへの自動翻訳をもたらします。


LispとMaximaのバージョンの間である非互換性が存在する可能性があるので、
翻訳された関数は
翻訳前にした方法を同一に動作するわけではないことに注意してください。
原則として、
もし変数のいずれかが`mode_declare`された標準有理式(CRE)なら
複数の引数を取る`rat`関数と`ratvars`関数は使うべきではありません。
また、
`prederror: false`設定は翻訳されません。



`savedef` - もし`true`なら、
関数が`translate`された時、Maximaバージョンのユーザー関数を残すようにします。
これは、定義を`dispfun`で表示することを可能にし、
関数を編集することを可能にします。


`transrun` - もし`false`なら、
すべての関数について、翻訳バージョンではなく、
インタープリトされるバージョン(まだあると仮定して)が実行されるようにします。


`translate`が返す結果は、翻訳された関数名のリストです。

<!-- category: Programming -->
<!-- keywords: translate_file -->
<!-- signatures: translate_file(maxima_filename), translate_file(maxima_filename, lisp_filename) -->
### Function: translate_file (maxima_filename)

MaximaコードのファイルをLispコードのファイルに翻訳します。
`translate_file`は３つのファイル名のリストを返します:
Maximaファイル名、Lispファイル名、翻訳についての追加情報を含むファイル名。
`translate_file`は引数を評価します。


`translate_file ("foo.mac"); load("foo.LISP")`は、
例えば、`''`と`%`の利用といった若干の制約を除いて、
コマンド`batch ("foo.mac")`と同じです。



`translate_file (maxima_filename)`は
Maximaファイル*maxima_filename*を
同様に名付けらたLispファイルに翻訳します。
例えば、`foo.mac`は`foo.LISP`に翻訳されます。
Maximaのファイル名はディレクトリ名を含むかもしれません。
その場合、Lisp出力ファイルは、Maxima入力が来たのと同じディレクトリに書かれます。


`translate_file (maxima_filename, lisp_filename)`は、
Maximaファイル*maxima_filename*をLispファイル*lisp_filename*に翻訳します。
`translate_file`は、どんなものでも、`lisp_filename`の
ファイル名の拡張子を無視します;
Lisp出力ファイルのファイル名の拡張子は、いつも`LISP`です。
Lispファイル名はディレクトリ名を含むかもしれません。
その場合、Lisp出力ファイルは指定されたディレクトリに書かれます。


`translate_file`は、翻訳器のファイル
様々な度合いの厳しさの翻訳器警告メッセージのファイルも書き出します。
このファイルのファイル名拡張子は `UNLISP`です。
このファイルは、翻訳されたコードの中のバグを追跡するために、
あいまいかもしれませんが、価値ある情報を含むかもしれません。
`UNLISP`ファイルはいつもMaxima入力が来るのと同じディレクトリに書かれます。


`translate_file`は
Lispコードがコンパイルされるすぐに宣言や定義が効力を発揮するようにするLispコードを発行します。
このトピックに関してさらに知るには`compile_file`を参照してください。




`tr_array_as_ref`,



`tr_bound_function_applyp`,


`tr_exponent`,
`tr_file_tty_messagesp`, 
`tr_float_can_branch_complex`,
`tr_function_call_default`, 
`tr_numer`,
`tr_optimize_max_loop`, 
`tr_semicompile`,
`tr_state_vars`, 
`tr_warnings_get`,
`tr_warn_bad_function_calls`,
`tr_warn_fexpr`, 
`tr_warn_meval`,
`tr_warn_mode`,
`tr_warn_undeclared`, 
`tr_warn_undefined_variable`


も参照してください。

<!-- category: Programming -->
<!-- keywords: transrun -->
<!-- signatures: transrun -->
### Variable: transrun

デフォルト値: `true`


`transrun`が`false`の時、
すべての関数について、翻訳バージョンではなく、
インタープリトされるバージョン(まだあると仮定して)が実行されるようにします。

