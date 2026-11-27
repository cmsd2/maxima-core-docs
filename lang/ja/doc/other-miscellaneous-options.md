## Miscellaneous Options

<!-- category: Other -->
<!-- keywords: alphabetic -->
<!-- signatures: alphabetic -->
### Variable: alphabetic

`alphabetic`は、 `declare`が認識する宣言タイプです。
式 `declare(s, alphabetic)`は、Maximaに
*s*―は文字列でなければいけません―の中の文字のすべてをalphabeticとして認識するように
命じます。


`Identifiers`も参照してください。


例:









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

See also: `Identifiers`.

<!-- category: Other -->
<!-- keywords: genindex -->
<!-- signatures: genindex -->
### Variable: genindex

デフォルト値: `i`


`genindex`は、
必要な時、和の次の変数を生成するために使われる
アルファベットの接頭辞です。

<!-- category: Other -->
<!-- keywords: gensumnum -->
<!-- signatures: gensumnum -->
### Variable: gensumnum

デフォルト値: 0


`gensumnum`は、
和の次の変数を生成するために使われる
数値接尾辞です。
もし`false`に設定されているなら、
インデックスは数値接尾辞なしで`genindex`だけから成ります。

<!-- category: Other -->
<!-- keywords: gensym -->
<!-- signatures: gensym(), gensym(x) -->
### Function: gensym ()

`gensym()`は新鮮なシンボルを生成し、返します。


新しいシンボルの名前は、
デフォルトでは"g"の接頭辞と
Lisp内部カウンタの値がデフォルトの数の十進表現である接尾辞の連結です。


もし*x*が供給されて、それが文字列なら、
このgensymへの呼び出しに限って、
その文字列は"g"の代わりに接頭辞として使われます。


もし*x*が供給されて、それが整数なら、
このgensymへの呼び出しに限って、
内部Lisp整数の値の代わりに接尾辞として使われます。


もし陽な接尾辞が供給されないなら、また、その時だけ、
Lisp内部整数は、使われた後1だけ増分されます。


例:








```maxima
(%i1) gensym();
(%o1)                         g887
(%i2) gensym("new");
(%o2)                        new888
(%i3) gensym(123);
(%o3)                         g123
```

<!-- category: Other -->
<!-- keywords: properties -->
<!-- signatures: properties(a) -->
### Function: properties (a)

アトム*a*に関連づけられたプロパティすべての名前のリストを返します。

<!-- category: Other -->
<!-- keywords: props -->
<!-- signatures: props -->
### Variable: props

`props`は、
`declare`関数で指定されたプロパティはもちろん、
`atvalue`, `matchdeclare`, などが指定したような、
`infolists`で陽に言及されたもの以外の任意のプロパティ、を持つアトムです。

<!-- category: Other -->
<!-- keywords: propvars -->
<!-- signatures: propvars(prop) -->
### Function: propvars (prop)

`props`リスト上の、
*prop*が示すプロパティを持つアトムのリストを返します。
従って，
`propvars (atvalue)`は、atvalueを持つアトムのリストを返します。

<!-- category: Other -->
<!-- keywords: put -->
<!-- signatures: put(atom, value, indicator) -->
### Function: put (atom, value, indicator)

*value*を*atom*の(*indicator*が指定する)プロパティに割り当てます。
*indicator*は、任意のプロパティの名前を取り得ますが、
システム定義のプロパティは取りません。


`rem`は`put`の効果をひっくり返します。


`put`は引数を評価します。
`put`は*value*を返します。


例:



```maxima
(%i1) put (foo, (a+b)^5, expr);
                                   5
(%o1)                       (b + a)
(%i2) put (foo, "Hello", str);
(%o2)                         Hello
(%i3) properties (foo);
(%o3)            [[user properties, str, expr]]
(%i4) get (foo, expr);
                                   5
(%o4)                       (b + a)
(%i5) get (foo, str);
(%o5)                         Hello
```

<!-- category: Other -->
<!-- keywords: qput -->
<!-- signatures: qput(atom, value, indicator) -->
### Function: qput (atom, value, indicator)

*value*を*atom*の(*indicator*が指定する)プロパティに割り当てます。
これは、引数がクォートされることを除いて、`put`と同じです。


例:



```maxima
(%i1) foo: aa$ 
(%i2) bar: bb$
(%i3) baz: cc$
(%i4) put (foo, bar, baz);
(%o4)                          bb
(%i5) properties (aa);
(%o5)                [[user properties, cc]]
(%i6) get (aa, cc);
(%o6)                          bb
(%i7) qput (foo, bar, baz);
(%o7)                          bar
(%i8) properties (foo);
(%o8)            [value, [user properties, baz]]
(%i9) get ('foo, 'baz);
(%o9)                          bar
```

<!-- category: Other -->
<!-- keywords: rem -->
<!-- signatures: rem(atom, indicator) -->
### Function: rem (atom, indicator)

*atom*から、*indicator*が示すプロパティを取り除きます。
`rem`は`put`の効果をひっくり返します。


`rem`が呼び出された時、もし*atom*が*indicator*プロパティを持っていたなら、`rem`は`done`を返します。もしそんなプロパティを持っていなかったら`false`を返します。

<!-- category: Other -->
<!-- keywords: remove -->
<!-- signatures: remove(a_1, p_1, ..., a_n, p_n), remove([a_1, ..., a_m], [p_1, ..., p_n], ...), remove("a", operator), remove(a, transfun), remove(all, p) -->
### Function: remove (a_1, p_1, ..., a_n, p_n)

アトムに関連づけられたプロパティを取り除きます。


`remove (a_1, p_1, ..., a_n, p_n)`
は、アトム`a_k`からプロパティ`p_k`を取り除きます。


`remove ([a_1, ..., a_m], [p_1, ..., p_n], ...)`
は、
アトム*a_1*, ..., *a_m*から
プロパティ`p_1, ..., p_n`を
取り除きます。
リストのペアは複数を取り得ます。



`remove (all, p)`は、
プロパティ*p*を、それを持つアトムすべてから取り除きます。



取り除かれるプロパティは、
`function`, `macro`, `mode_declare`のようなシステム定義のプロパティ
かもしれません。
`remove`は`put`で定義されたプロパティを取り除きません。




翻訳されたLispバージョンの関数を取り除くために
プロパティは、`transfun`を取ることができます。
これを実行した後は、翻訳バージョンでなく、Maximaバージョンの関数が実行されます。


`remove ("a", operator)`または、同値な, `remove ("a", op)`
は、
*a*から
`prefix`, `infix`, `nary`, `postfix`, `matchfix`, `nofix`が宣言した演算子プロパティを取り除きます。
演算子名はクォートされた文字列として書かれなければいけないことに注意してください。


アトムが指定されたプロパティを持とうが持ちまいが、
`remove`は、いつも`done`を返します。
この振る舞いは、もっと具体的な削除関数`remvalue`, `remarray`, `remfunction`, `remrule`と似ていません。


`remove`は引数をクォートします。

<!-- category: Other -->
<!-- keywords: remvalue -->
<!-- signatures: remvalue(name_1, ..., name_n), remvalue(all) -->
### Function: remvalue (name_1, ..., name_n)

(添字付きもありえる)ユーザー変数*name_1*, ..., *name_n*の値をシステムから
取り除きます。


`remvalue (all)`は、
 removes the values of all variables in 
`values`―(Maximaが自動的に割り当てたものと対照的に)
ユーザーが名前を与えた変数すべてのリスト―
の中の変数すべての値を取り除きます。


`values`も参照してください。

<!-- category: Other -->
<!-- keywords: rncombine -->
<!-- signatures: rncombine(expr) -->
### Function: rncombine (expr)

同一の分母や、たがいに数値因子だけことなる分母を持つ
*expr*のすべての項を結合することで、
*expr*を変換します。
これは、`combine`の振る舞いとわずかに違います。
`combine`は、同一分母を持つ項を集めます。


`pfeformat: true`を設定し、`combine`を使うことは、
`rncombine`を使って得られるものと似た結果をもたらしますが、
`rncombine`は、
クロス積の数値的分母因子のおまけのステップを実行します。
これは、きれいな形式と、いくつかの相殺を認識する可能性を生みます。


`load("rncomb")`はこの関数をロードします。

<!-- category: Other -->
<!-- keywords: scalarp -->
<!-- signatures: scalarp(expr) -->
### Function: scalarp (expr)

もし*expr*が、数か、定数、
`declare`で`scalar`と宣言された変数、
数と定数とそんな変数から完全に構成され、行列やリストを含まない変数なら、
`true`を返します。

<!-- category: Other -->
<!-- keywords: setup_autoload -->
<!-- signatures: setup_autoload(filename, function_1, ..., function_n) -->
### Function: setup_autoload (filename, function_1, ..., function_n)

もし*function_1*, ..., *function_n*のいずれかが、
参照されたがまだ定義されていないなら、
`load`を通じて*filename*がロードされるように指定します。
*filename*は、
強制はされませんが、普通、指定された関数の定義を含みます。


`setup_autoload`は配列関数については機能しません。


`setup_autoload`は引数をクォートします。


例:









```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma function ultraspherical
Warning - you are redefining the Macsyma function legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);
                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

