## Help

<!-- category: Programming -->
<!-- keywords: apropos -->
<!-- signatures: apropos(string) -->
### Function: apropos (string)

*string*を含むMaxima上の名前を検索します。
例えば、`apropos ("exp")`は、
（`expand`, `exp`, `exponentialize`のように）
`exp`を名前の一部として含むフラグ、関数すべてのリストを返します。
このように、もしなにかの名前の一部だけ覚えていたなら、
このコマンドを使って名前の残りを見つけることができます。
同様に、 `apropos ("tr_")`とすれば、翻訳器に関係した多くのスイッチのリストを
見つけることができます。翻訳器に関係したスイッチのほとんどは`tr_`で始まります。


`apropos("")`は、Maximaの名前すべてのリストを返します。


もし名前が見つからなければ、`apropos`は空のリスト`[]`を返します。


例:


`"gamma"`を含むMaximaシンボルすべてを表示します:






```maxima
(%i1) apropos("gamma");
(%o1) [%gamma, gamma, gammalim, gamma_expand, gamma_incomplete_lower, 
gamma_incomplete, gamma_incomplete_generalized, 
gamma_incomplete_regularized, Gamma, log_gamma, makegamma, 
prefer_gamma_incomplete,
gamma_incomplete_generalized_regularized]
```

<!-- category: Programming -->
<!-- keywords: demo -->
<!-- signatures: demo(filename) -->
### Function: demo (filename)

*filename*の中のMaxima式を評価し、結果を表示します。
`demo`はそれぞれの式を評価した後 停止し、
ユーザーがリターンキーを入力すると続きを実行します。
(Xmaximaで走らせている場合、
`demo`はセミコロン`;`に続けて改行を入力する必要があります。)


`demo`は、*filname*のファイルを探すため、
ディレクトリ`file_search_demo`のリストを検索します。
もしファイルの拡張子が`.dem`なら、拡張子は省略できます。
`file_search`も参照してください。


`demo`は引数を評価します。
`demo`はデモンストレーションファイルの名前を返します。


例:



```maxima
(%i1) demo ("disol");

batching /home/wfs/maxima/share/simplification/disol.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i2)                      load("disol")

_
(%i3)           exp1 : a (e (g + f) + b (d + c))
(%o3)               a (e (g + f) + b (d + c))

_
(%i4)                disolate(exp1, a, b, e)
(%t4)                         d + c

(%t5)                         g + f

(%o5)                   a (%t5 e + %t4 b)

_
```

<!-- category: Programming -->
<!-- keywords: describe -->
<!-- signatures: describe(string), describe(string, exact), describe(string, inexact) -->
### Function: describe (string)

`describe(string)`は`describe(string, exact)`と同値です。


`describe(string, exact)`は（大文字小文字は区別せず）*string*に等しいタイトルを持った項目があれば、それを見つけます。


`describe(string, inexact)`はタイトルの中に*string*を含むすべての項目を見つけます。
もし複数あれば、Maximaはユーザーに項目を選択するよう尋ねます。


対話プロンプトでは、
`? foo`(`?`と`foo`の間にスペース)は
`describe("foo", exact)`と同値であり、
`?? foo`は`describe("foo", inexact)`と同値です。


`describe("", inexact)`は、オンラインマニュアルでドキュメント化されたすべてのトピックのリストを出力します。


`describe`は引数をクォートします。
`describe`は、ドキュメントが見つかれば`true`を返し、見つからなければ`false`を返します。


`Documentation`も参照してください。


例:



```maxima
(%i1) ?? integ
 0: Functions and Variables for Elliptic Integrals
 1: Functions and Variables for Integration
 2: Introduction to Elliptic Functions and Integrals
 3: Introduction to Integration
 4: askinteger  (Functions and Variables for Simplification)
 5: integerp  (Functions and Variables for Miscellaneous Options)
 6: integer_partitions  (Functions and Variables for Sets)
 7: integrate  (Functions and Variables for Integration)
 8: integrate_use_rootsof  (Functions and Variables for
    Integration)
 9: integration_constant_counter  (Functions and Variables for
    Integration)
 10: nonnegintegerp  (Functions and Variables for linearalgebra)
Enter space-separated numbers, `all' or `none': 7 8

 -- Function: integrate (<expr>, <x>)
 -- Function: integrate (<expr>, <x>, <a>, <b>)
     Attempts to symbolically compute the integral of <expr> with
     respect to <x>.  `integrate (<expr>, <x>)' is an indefinite
     integral, while `integrate (<expr>, <x>, <a>, <b>)' is a
     definite integral, [...]
     
 -- Option variable: integrate_use_rootsof
     Default value: `false'

     When `integrate_use_rootsof' is `true' and the denominator of
     a rational function cannot be factored, `integrate' returns
     the integral in a form which is a sum over the roots (not yet
     known) of the denominator.
     [...]
```


この例では、項目7と8を選択しました。
（`[...]`でほのめかされているように出力は省略されています。）
`all`や`none`を入力すると、項目すべてを選択したり、１つも選ばなかったりできます。
それぞれ`a`もしくは`n`と省略形を使うことができます。

See also: `Documentation`.

<!-- category: Programming -->
<!-- keywords: example -->
<!-- signatures: example(topic), example() -->
### Function: example (topic)

`example (topic)`は、*topic*の例をいくつか表示します。
*topic*はシンボルもしくは文字列です。
`if`や`do`、`lambda`のような演算子の例を得るには、引数は文字列でなければなりません。例えば、 `example ("do")`。
`example`は、大文字小文字を区別しません。トピックのほとんどは関数名です。


`example ()`はわかっているトピックすべてのリストを表示します。


例を含むファイル名は、グローバル変数`manual_demo`で与えられます。デフォルトは`"manual.demo"`です。


`example`は引数をクォートします。
`example`はエラーがあったり引数がなかったりしなければ`done`を返します。
引数がない場合には
わかっているトピックすべてのリストを表示します。


例:







```maxima
(%i1) example(append);
(%i2) append([x+y,0,-3.2],[2.5e+20,x])
(%o2)                    [y + x, 0, - 3.2, 2.5e+20, x]
(%o2)                                done
(%i3) example("lambda");

(%i4) lambda([x,y,z],z^2+y^2+x^2)
                                           2    2    2
(%o4)                   lambda([x, y, z], z  + y  + x )
(%i5) %(1,2,a)
                                     2
(%o5)                               a  + 5
(%i6) a+2+1
(%o6)                                a + 3
(%o6)                                done
```

See also: `manual_demo`.

<!-- category: Programming -->
<!-- keywords: manual_demo -->
<!-- signatures: manual_demo -->
### Variable: manual_demo

デフォルト値: `"manual.demo"`


`manual_demo`は、
関数`example`のための例が入っているファイルの名前を指定します。
`example`を参照してください。

See also: `example`.

