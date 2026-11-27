## Command Line

<!-- category: Programming -->
<!-- keywords: % -->
<!-- signatures: % -->
### Variable: %

`%`はMaximaが直前に計算した出力式です。
(例えば、 `%o1`, `%o2`, `%o3`, ...)
出力の表示には無関係です。


`batch`と `load`は`%`を認識します。
`batch`が処理するファイル内では、
`%`は対話プロンプトでのそれと同じ意味になります。
`load`が処理するファイル内では、
`%`は、対話プロンプトやバッチファイルの中で、直前に計算された出力式にバインドされます;
`%`は、処理中のファイル内の出力式にはバインドされません。


`_`, `%%`, `%th`も参照してください。

See also: `_`, `%%`, `%th`.

<!-- category: Programming -->
<!-- keywords: %% -->
<!-- signatures: %% -->
### Variable: %%

合成文、すなわち`block`, `lambda`,
もしくは`(s_1, ..., s_n)`の中で、 `%%`は前の文の値です。


合成文の最初の文もしくは合成文の外側では`%%`は未定義です。


`%%`は、`batch`や `load`で認識され、
対話プロンプトでのそれと同じ意味になります。


`%`も参照してください。


例:


以下の二つの例は同じ結果になります。



```maxima
(%i1) block (integrate (x^5, x), ev (%%, x=2) - ev (%%, x=1));
                               21
(%o1)                          --
                               2
(%i2) block ([prev], prev: integrate (x^5, x),
               ev (prev, x=2) - ev (prev, x=1));
                               21
(%o2)                          --
                               2
```


合成文は他の合成文を含むかもしれません。
文が単文か合成文かに関係なく、
`%%`は前の文の値です。



```maxima
(%i3) block (block (a^n, %%*42), %%/6);
                                 n
(%o3)                         7 a
```


合成文の中ではブレイクプロンプトで`%%`の値を検査することができます。
ブレイクプロンプトは `break`関数を実行することで開きます。
例えば、以下の例で`%%;`を入力すると、`42`が出力されます。



```maxima
(%i4) block (a: 42, break ())$

Entering a Maxima break point. Type 'exit;' to resume.
_%%;
42
_
```

See also: `batch`, `load`.

<!-- category: Programming -->
<!-- keywords: %th -->
<!-- signatures: %th(i) -->
### Function: %th (i)

*i*番前の出力式の値。
すなわち、計算される次の式を*n*番目の出力とすると
`%th (m)`は、(*n* - *m*)番目の出力です。


`batch`と`load`は`%th`を認識されます。
`batch`が処理するファイル内では、
`%th`は、対話プロンプトでのそれと同じ意味になります。
`load`が処理するファイル内では、
`%th`は、対話プロンプトやバッチファイルの中で、直前に計算された出力式にバインドされます;
`%th`は、処理中のファイル内の出力式にはバインドされません。


`%`と `%%`も参照してください。


例:


`batch`ファイルの中でとか、出力式のグループを参照する時`%th`は役立ちます。
この例は`s`を最後の5つの出力式の和に設定します。



```maxima
(%i1) 1;2;3;4;5;
(%o1)                           1
(%o2)                           2
(%o3)                           3
(%o4)                           4
(%o5)                           5
(%i6) block (s: 0, for i:1 thru 5 do s: s + %th(i), s);
(%o6)                          15
```

See also: `%`, `%%`.

<!-- category: Programming -->
<!-- keywords: ? -->
<!-- signatures: ? -->
### Function: ?

関数名や変数名の前置としての`?`は、
名前が、Maximaの名前ではなくLispの名前であることを意味します。
例えば、`?round`は、Lisp関数`ROUND`を意味します。
この点に関して更に知るには`Lisp-and-Maxima`を参照してください。


表記`? word` (空白を空けて単語が続くクエスチョンマーク)は
`describe("word")`と同値です。
クエスチョンマークは入力ラインの先頭になければいけません;
そうでなければドキュメンテーションのリクエストとして認識されません。
`describe`も参照してください。

See also: `Lisp-and-Maxima`, `describe`.

<!-- category: Programming -->
<!-- keywords: ?? -->
<!-- signatures: ?? -->
### Function: ??

表記`?? word`(空白を空けて単語が続く`??`)は
`describe("word", inexact)`と同値です。
クエスチョンマークは入力行の先頭になければいけません;
そうでなければドキュメンテーションのリクエストとして認識されません。
`describe`も参照してください。

See also: `describe`.

<!-- category: Programming -->
<!-- keywords: _ -->
<!-- signatures: _ -->
### Variable: _

`_`は直前の入力式です。
(例えば、`%i1`, `%i2`, `%i3`, ...)


`_`は、入力が整理されたり評価されたりする前に、入力式に割り当てられます。
しかし、
`_`の値は、表示される時（評価はされませんが）整理されます。


`batch`と `load`は `_`を認識します。
`batch`が処理するファイル内では、
`_`は対話プロンプトでのそれと同じ意味になります。
`load`が処理するファイル内では、
`_`は、対話プロンプトやバッチファイルの中で、直前に入力された入力式にバインドされます;
`_`は処理中のファイル内の入力式にはバインドされません。


`__`や `%`も参照してください。


例:


















```maxima
(%i1) 13 + 29;
(%o1)                          42
(%i2) :lisp $_
((MPLUS) 13 29)
(%i2) _;
(%o2)                          42
(%i3) sin (%pi/2);
(%o3)                           1
(%i4) :lisp $_
((%SIN) ((MQUOTIENT) $%PI 2))
(%i4) _;
(%o4)                           1
(%i5) a: 13$
(%i6) b: 29$
(%i7) a + b;
(%o7)                          42
(%i8) :lisp $_
((MPLUS) $A $B)
(%i8) _;
(%o8)                         b + a
(%i9) a + b;
(%o9)                          42
(%i10) ev (_);
(%o10)                         42
```

See also: `batch`, `load`, `__`, `%`.

<!-- category: Programming -->
<!-- keywords: __ -->
<!-- signatures: __ -->
### Variable: __

`__`は、現在評価中の入力式です。
すなわち、入力式 *expr*が評価されている間、 `__`は *expr*です。


`__`は、入力が整理されたり評価されたりする前に入力式に割り当てられます。
しかし表示される時、`__`の値は（評価はされませんが）整理されます。


`batch`と `load`は `__`を認識します。
`batch`が処理するファイル内では、
`__`は対話プロンプトでのそれと同じ意味になります。
`load`が処理するファイル内では、
`__`は対話プロンプトやバッチファイルの中で直前に入力された入力式にバインドされています;
`__`は処理中のファイル内の入力式にはバインドされません。
特に、 `load (filename)`が対話プロンプトからコールされた時、
`__`は、ファイルが処理されている間、
`load (filename)`にバインドされます。


`_`や `%`も参照してください。


例:










```maxima
(%i1) print ("I was called as", __);
I was called as print(I was called as, __) 
(%o1)              print(I was called as, __)
(%i2) foo (__);
(%o2)                     foo(foo(__))
(%i3) g (x) := (print ("Current input expression =", __), 0);
(%o3) g(x) := (print("Current input expression =", __), 0)
(%i4) [aa : 1, bb : 2, cc : 3];
(%o4)                       [1, 2, 3]
(%i5) (aa + bb + cc)/(dd + ee + g(x));
                            cc + bb + aa
Current input expression = -------------- 
                           g(x) + ee + dd
                                6
(%o5)                        -------
                             ee + dd
```

See also: `batch`, `load`, `_`, `%`.

<!-- category: Programming -->
<!-- keywords: inchar -->
<!-- signatures: inchar -->
### Variable: inchar

デフォルト値: `%i`


`inchar`はユーザーが入力した式のラベルの前置です。
Maximaは、
`inchar`と`linenum`を連結することで、
入力式それぞれのラベルを自動的に構成します。


`inchar`は単一文字である必要はなく、
任意の文字列もしくはシンボルを割り当てられます。
Maximaは内部的に前置の最初の文字だけを考慮するので、
前置`inchar`, `outchar`, `linechar`は異なる最初の文字を持たなければいけません。
そうでなければ`kill(inlables)`のようないくつかのコマンドは期待通りに動きません。


`labels`も参照してください。


例:







```maxima
(%i1) inchar: "input";
(%o1)                         input
(input2) expand((a+b)^3);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(input3)
```

See also: `linenum`, `outchar`, `linechar`.

<!-- category: Programming -->
<!-- keywords: infolists -->
<!-- signatures: infolists -->
### Variable: infolists

デフォルト値: `[]`


`infolists`はMaximaに関する情報リストすべての名前のリストです。
これらは以下の通りです:



**labels** — すべてのバインドされた`%i`, `%o`, `%t`ラベル
**values** — `:`や`::`や関数バインドが生成する、
ユーザー変数であって、Maximaオプションやスイッチでない、
すべてのバインドされたアトム
**functions** — `:=`や`define`が生成するすべてのユーザー定義関数
**arrays** — `:`, `::`, または`:=`が生成するすべての宣言配列と未宣言配列
**macros** — `::=`が生成したすべてのユーザー定義マクロ関数
**myoptions** — (それらが後にデフォルト値に再設定されようがされまいが)
ユーザーが再設定したすべてのオプション
**rules** — `tellsimp`, `tellsimpafter`, `defmatch`,
または`defrule`が生成するすべてのユーザー定義パターンマッチングと整理規則
**aliases** — `alias`, `ordergreat`, `orderless`関数が生成するか、
`declare`を使ってアトムを`noun`として宣言することで生成された、
ユーザー定義エーリアスを持つすべてのアトム
**dependencies** — `depends`や`gradef`関数が生成する関数依存性を持つすべてのアトム
**gradefs** — `gradef`関数が生成するユーザー定義の導関数を持つすべての関数
**props** — `declare`関数で確立されるプロパティはもちろん、
`atvalue`や`matchdeclare`などが確立するプロパティで、
上で述べたもの以外の任意のプロパティを持つすべてのアトム
**let_rule_packages** — 特別パッケージ`default_let_rule_package`に加えて
すべてのユーザー定義`let`規則パッケージ 
(`default_let_rule_package`は、
ユーザーが陽に設定していない時使われる規則パッケージの名前です。)

See also: `:`, `::`, `:=`, `define`, `::=`, `tellsimp`, `tellsimpafter`, `defmatch`, `defrule`, `alias`, `ordergreat`, `orderless`, `declare`, `noun`, `depends`, `gradef`, `atvalue`, `matchdeclare`, `default_let_rule_package`, `let`.

<!-- category: Programming -->
<!-- keywords: kill -->
<!-- signatures: kill(a_1, ..., a_n), kill(labels), kill(inlabels, outlabels, linelabels), kill(n), kill([m, n]), kill(values, functions, arrays, ...), kill(all), kill(allbut(a_1, ..., a_n)) -->
### Function: kill (a_1, ..., a_n)

引数*a_1*, ..., *a_n*からすべてのバインド（値、関数、配列、ルール）を解除します。
引数*a_k*はシンボルか配列要素を取り得ます。
*a_k*が配列要素の時、`kill`は配列の他の要素には影響することなくその要素をアンバインドします。


いくつかの特殊な引数が認識されます。
例えば、`kill (inlabels, functions, allbut (foo, bar))`のように、異なる引数の種類が組み合わされます。


`kill (labels)`はそれまでに作られた入力、出力、中間式のラベルすべてをアンバインドします。
`kill (inlabels)`は `inchar`の現在の値で始まる入力ラベルのみをアンバインドします。
同様に、
`kill (outlabels)`は `outchar`の現在の値で始まる出力ラベルのみをアンバインドし、
`kill (linelabels)`は `linechar`の現在の値で始まる中間式ラベルのみをアンバインドします。


`kill (`*n*`)`（nは整数）は入力、出力ラベルの最近のn個をアンバインドします。


`kill ([m, n])`は入力、出力ラベル*m*から*n*までをアンバインドします。


`kill (infolist)`は *infolist*の中のすべての項目をアンバインドします。
ここで、*infolist*は（`values`, `functions`, `arrays`のような)
`infolists`の中の任意の項目です。
`infolists`も参照してください。


`kill (all)`はinfolistsのすべての項目をアンバインドします。
`kill (all)`はグローバル変数をデフォルト値にリセットしません;
この点に関しては`reset`を参照してください。


`kill (allbut (a_1, ..., a_n))`は、
*a_1*, ..., *a_n*を除いて
すべてのinfolistsの中のすべての項目をアンバインドします。
`kill (allbut (infolist))`は
*infolist*（*infolist*は`values`, `functions`, `arrays`など）
上の項目を除いてすべての項目をアンバインドします。


バインドされたプロパティによって使われたメモリは、すべてのシンボルがプロパティからアンバインドされるまで解放されません。
特に、シンボルの値によって使われているメモリを解放するには、
シンボルそのもののアンバインドだけでなく、バインドされた値を表示する出力ラベルをアンバインドします。


`kill`は引数をクォートします。
引数を評価するにはクォートクォート演算子`''`を使います。


`kill (symbol)`はシンボルのすべてのプロパティをアンバインドします。
対照的に、関数`remvalue`, `remfunction`, `remarray`,
`remrule`は特定のプロパティをアンバインドします。


`kil`は常に、たとえ引数がバインドされていなくても、`done`を返します。

See also: `inchar`, `outchar`, `linechar`, `values`, `functions`, `arrays`, `reset`, `remvalue`, `remfunction`, `remarray`, `remrule`.

<!-- category: Programming -->
<!-- keywords: labels -->
<!-- signatures: labels(symbol) -->
### Function: labels (symbol)

*symbol*で始まる入力、出力、中間式ラベルのリストを返します。
*symbol*は、`inchar`, `outchar`, もしくは`linechar`の値が典型的です。
ラベル文字はパーセント記号ありでもあしでもかまいませんので、
例えば、`i`と`%i`は同じ結果になります。


もし*symbol*で始まるラベルがなければ、`labels`は空のリストを返します。


関数`labels`は引数をクォートします。
引数を評価するにはクォートクォート演算子`''`を使います。
例えば，
`labels (''inchar)`は、現在の入力ラベル文字で始まる入力ラベルを返します。


変数`labels`は入力、出力、中間式ラベルのリストです。
`inchar`, `outchar`, もしくは`linechar`が再定義されても、以前のラベルすべてを含みます。


デフォルトで、Maximaはそれぞれのユーザー入力式の結果を表示し、結果に出力ラベルが与えられます。
入力を`;`(セミコロン)の代わりに`$`(ドル記号)で終了することで、出力表示は抑制されます。
出力ラベルが構成され、結果にバインドされますが、表示されません。
ラベルは表示された出力ラベルと同じ方法で参照できます。
`%`や`%%`, `%th`も参照してください。


いくつかの関数では中間式ラベルが生成されることがあります。
フラグ`programmode`は
`solve`や他の関数が式のリストを返す代わりに中間式ラベルを生成するかどうかを制御します。
`ldisplay`のようないくつかの他の関数は常に中間式ラベルを生成します。


`inchar`や`outchar`, `linechar`, `infolists`も参照してください。

See also: `inchar`, `outchar`, `linechar`, `%`, `%%`, `%th`, `programmode`, `solve`, `ldisplay`, `infolists`.

<!-- category: Programming -->
<!-- keywords: linechar -->
<!-- signatures: linechar -->
### Variable: linechar

デフォルト値: `%t`


`linechar`は
Maximaが生成する中間式のラベルの前置です。
Maximaは（もし表示されるなら）
`linechar`と`linenum`を連結することで
中間式それぞれのラベルを構成します。


`linechar`は単一文字である必要はなく、
任意の文字列もしくはシンボルを割り当てられます。
Maximaは内部的に
前置の最初の文字だけを考慮するので、
前置`inchar`, `outchar`, `linechar`は異なる最初の文字を持たなければいけません。
そうでなければ `kill(inlables)`のようないくつかのコマンドは期待通りに動きません。


中間式は表示されるかもしれませんし、表示されないかもしれません。
`programmode`と`labels`も参照してください。

See also: `linenum`, `inchar`, `outchar`, `programmode`, `labels`.

<!-- category: Programming -->
<!-- keywords: linenum -->
<!-- signatures: linenum -->
### Variable: linenum

入力出力式の現在のペアの行番号。

<!-- category: Programming -->
<!-- keywords: myoptions -->
<!-- signatures: myoptions -->
### Variable: myoptions

デフォルト値: `[]`


`myoptions`はユーザーが再設定したオプションすべてのリストです。
初期値に再設定されたか否かに関わらずです。

<!-- category: Programming -->
<!-- keywords: nolabels -->
<!-- signatures: nolabels -->
### Variable: nolabels

デフォルト値: `false`


`nolabels`は`true`であれば、
入力と出力結果のラベル（それぞれ`%i`と`%o`）は表示されますが、
ラベルは結果にバインドされず、`labels`リストにも追加されません。
ラベルは結果にバインドされないので、
ガーベッジコレクションは結果が使ったメモリを回復することができます。


そうでなければ、入力と出力の結果のラベルは結果にバインドされ、`labels`リストに追加されます。


中間式ラベル(`%t`)は`nolabels`に影響されません;
`nolabels`が`true`でも`false`でも、中間式ラベルはバインドされ、`labels`リストに追加されます。


`batch`や`load`、 `labels`も参照してください。

See also: `labels`, `batch`, `load`.

<!-- category: Programming -->
<!-- keywords: optionset -->
<!-- signatures: optionset -->
### Variable: optionset

デフォルト値: `false`


`optionset`が`true`の時、Maximaは、Maximaオプションが再設定されるといつでも、メッセージを表示します。
もしユーザーがあるオプションの綴りが怪しく、割り当てた変数が本当にオプション変数か確認したいなら便利です。


例:



```maxima
(%i1) optionset:true;
assignment: assigning to option optionset
(%o1)                         true
(%i2) gamma_expand:true;
assignment: assigning to option gamma_expand
(%o2)                         true
```

<!-- category: Programming -->
<!-- keywords: outchar -->
<!-- signatures: outchar -->
### Variable: outchar

デフォルト値: `%o`


`outchar`はMaximaが計算した式のラベルの前置です。
`outchar`と`linenum`を連結することで、
Maximaは計算された式それぞれのラベルを自動的に構成します。
`outchar`は、単一文字である必要はなく、
任意の文字列もしくはシンボルを割り当てられます。
Maximaは内部的に前置の最初の文字だけを考慮するので、
前置`inchar`, `outchar`, `linechar`は異なる最初の文字を持たなければいけません。
そうでなければ、`kill(inlables)`のようないくつかのコマンドは期待通りに動きません。


`labels`も参照してください。


例:







```maxima
(%i1) outchar: "output";
(output1)                    output
(%i2) expand((a+b)^3);
                     3        2      2      3
(output2)           b  + 3 a b  + 3 a  b + a
(%i3)
```

See also: `linenum`, `inchar`, `linechar`.

<!-- category: Programming -->
<!-- keywords: playback -->
<!-- signatures: playback(), playback(n), playback([m, n]), playback([m]), playback(input), playback(slow), playback(time), playback(grind) -->
### Function: playback ()

入力、出力、中間式を表示します。再計算はしません。
`playback`はラベルにバインドされた式表示するだけです;
（`print`や`describe`で表示されたテキストやエラーメッセージなど）他の出力は表示されません。
`labels`も参照してください。


`playback`は引数をクォートします。
引数を評価するにはクォートクォート演算子`''`を使います。
`playback`は常に`done`を返します。


`playback ()`（引数なし）は今までに生成された入力、出力、中間式すべてを表示します。
たとえ計算時に`$`終端子で出力が抑制されていても、
出力式は表示されます。


`playback (n)`は最近の*n*個の式を表示します。
入力、出力、中間式それぞれを１と数えます。


`playback ([m, n])`は
*m*番目から*n*番目までの入力、出力、中間式を表示します。


`playback ([m])`は `playback ([m, m])`と同値です;
これは普通、入力と出力の式のペアを１つ表示します。


`playback (input)`は今までに生成された入力式をすべて表示します。


`playback (slow)`は式の間でポーズし、ユーザーが
`enter`を入力するのを待ちます。
これは `demo`と似たような振る舞いです。

`playback (slow)`は、`save`や`stringout`と関連して、
役立つ式を取り出すために２次記憶ファイルを生成するときに便利です。


`playback (time)`はそれぞれの式の計算時間を表示します。




`playback (grind)`は入力式を `grind`関数と同じ形式で表示します。
出力式は `grind`オプションで影響を受けません。
`grind`を参照してください。


例えば、`playback ([5, 10], grind, time, slow)`のように、
引数を組み合わせられます。

See also: `print`, `describe`, `labels`, `demo`, `stringout`, `grind`.

<!-- category: Programming -->
<!-- keywords: prompt -->
<!-- signatures: prompt -->
### Variable: prompt

デフォルト値: `_`


`prompt`は、`demo`関数や`playback (slow)`モード、
（`break`で呼び出された）Maximaブレイクループのプロンプトシンボルです。

See also: `demo`, `break`.

<!-- category: Programming -->
<!-- keywords: quit -->
<!-- signatures: quit() -->
### Function: quit ()

Maximaセッションを終了します。
関数は、`quit`ではなく、`quit();`もしくは`quit()$`として呼び出さなければいけないことに注意してください。


長い計算を中断するには `control-C`をタイプしてください。
デフォルトの動作では Maximaプロンプトに戻ります。
もし`*debugger-hook*`が`nil`なら、
`control-C`はLispデバッガを開きます。
`debugging`も参照してください。

<!-- category: Programming -->
<!-- keywords: read -->
<!-- signatures: read(expr_1, ..., expr_n) -->
### Function: read (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を表示し、
コンソールから式１つを読み込み、評価された式を返します。
式はセミコロン`;`もしくはドル記号`$`で終了します。


`readonly`も参照してください。



```maxima
(%i1) foo: 42$ 
(%i2) foo: read ("foo is", foo, " -- enter new value.")$
foo is 42  -- enter new value. 
(a+b)^3;
(%i3) foo;
                                     3
(%o3)                         (b + a)
```

See also: `readonly`.

<!-- category: Programming -->
<!-- keywords: readonly -->
<!-- signatures: readonly(expr_1, ..., expr_n) -->
### Function: readonly (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を表示し、
コンソールから式を１つ読み込み、
式を（評価せずに）返します。
式はセミコロン`;`もしくはドル記号`$`で終了します。


`read`も参照してください。


例:



```maxima
(%i1) aa: 7$
(%i2) foo: readonly ("Enter an expression:");
Enter an expression: 
2^aa;
                                  aa
(%o2)                            2
(%i3) foo: read ("Enter an expression:");
Enter an expression: 
2^aa;
(%o3)                            128
```

See also: `read`.

<!-- category: Programming -->
<!-- keywords: reset -->
<!-- signatures: reset() -->
### Function: reset ()

多くのグローバル変数やオプション、いくつかの他の変数をデフォルト値に再設定します。


`reset`は Lispリスト`*variable-initial-values*`上の変数を処理します。
Lispマクロ`defmvar`は（他の動作の間に）このリストに変数を置きます。
すべてではありませんが多くのグローバル変数やオプションがdefmvarによって定義されており、
また、`defmvar`で定義されたいくつかの変数はグローバル変数でもオプションでもありません。

<!-- category: Programming -->
<!-- keywords: showtime -->
<!-- signatures: showtime -->
### Variable: showtime

デフォルト値: `false`


`showtime`が`true`の時、出力式と一緒に計算時間と経過時間を表示します。


計算時間は常に記録されており、
`showtime`が`false`の時でも、
`time`や`playback`で計算時間を表示することができます。


`timer`も参照してください。

See also: `time`, `playback`, `timer`.

<!-- category: Programming -->
<!-- keywords: to_lisp -->
<!-- signatures: to_lisp() -->
### Function: to_lisp ()

Maximaの下のLispシステムに入ります。`(to-maxima)`でMaximaに戻ります。


例:


関数を定義し、Maximaの下のLispシステムに入ります。
定義をプロパティリスト上で検査します。そして、関数定義を抽出し、因数分解し、
変数$resultに格納します。
変数はMaximaに戻った後、Maximaで使うことができます。



```maxima
(%i1) f(x):=x^2+x;
                                  2
(%o1)                    f(x) := x  + x
(%i2) to_lisp();
Type (to-maxima) to restart, ($quit) to quit Maxima.

MAXIMA> (symbol-plist '$f)
(MPROPS (NIL MEXPR ((LAMBDA) ((MLIST) $X) 
                             ((MPLUS) ((MEXPT) $X 2) $X))))
MAXIMA> (setq $result ($factor (caddr (mget '$f 'mexpr))))
((MTIMES SIMP FACTORED) $X ((MPLUS SIMP IRREDUCIBLE) 1 $X))
MAXIMA> (to-maxima)
Returning to Maxima
(%o2)                         true
(%i3) result;
(%o3)                       x (x + 1)
```

<!-- category: Programming -->
<!-- keywords: values -->
<!-- signatures: values -->
### Variable: values

初期値: `[]`


`values`は（Maximaのオプションやスイッチではなく）バインドされたユーザー変数すべてのリストです。
リストは、`:`や`::`でバインドされたシンボルを含みます。


もし変数の値がコマンド`kill`や, `remove`, `remvalue`で削除されたら、
変数は`values`から削除されます。


ユーザー定義関数のリストに関しては `functions`を参照してください。


例:


最初、`values`はシンボル`a`, `b`, `c`を示しますが、
`d`も―それは値にバインドされていません―ユーザー関数`f`も示しません。
値は変数から削除されます。`values`は空のリストです。









```maxima
(%i1) [a:99, b::a-90, c:a-b, d, f(x):= x^2];
                                           2
(%o1)              [99, 9, 90, d, f(x) := x ]
(%i2) values;
(%o2)                       [a, b, c]
(%i3) [kill(a), remove(b,value), remvalue(c)];
(%o3)                   [done, done, [c]]
(%i4) values;
(%o4)                          []
```

See also: `:`, `::`, `remove`, `remvalue`, `functions`.

