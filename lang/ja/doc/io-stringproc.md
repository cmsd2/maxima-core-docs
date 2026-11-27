## stringproc

<!-- category: IO -->
<!-- keywords: alphacharp -->
<!-- signatures: alphacharp(char) -->
### Function: alphacharp (char)

もし*char*がアルファベット文字なら`true`を返します。

<!-- category: IO -->
<!-- keywords: alphanumericp -->
<!-- signatures: alphanumericp(char) -->
### Function: alphanumericp (char)

もし*char*がアルファベット文字か数字なら`true`を返します。

<!-- category: IO -->
<!-- keywords: ascii -->
<!-- signatures: ascii(int) -->
### Function: ascii (int)

ASCIIコード*int*( -1 < int < 256 )に対応する文字を返します。








```maxima
(%i1) for n from 0 thru 255 do ( 
   tmp: ascii(n), if alphacharp(tmp) then sprint(tmp),
      if n=96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

<!-- category: IO -->
<!-- keywords: cequal -->
<!-- signatures: cequal(char_1, char_2) -->
### Function: cequal (char_1, char_2)

もし*char_1*と*char_2*が同じなら`true`を返します。

<!-- category: IO -->
<!-- keywords: cequalignore -->
<!-- signatures: cequalignore(char_1, char_2) -->
### Function: cequalignore (char_1, char_2)

`cequal`と同様ですが、文字の大小を無視します。

<!-- category: IO -->
<!-- keywords: cgreaterp -->
<!-- signatures: cgreaterp(char_1, char_2) -->
### Function: cgreaterp (char_1, char_2)

もし*char_1*のASCIIコードが*char_2*のそれより大きいなら`true`を返します。

<!-- category: IO -->
<!-- keywords: cgreaterpignore -->
<!-- signatures: cgreaterpignore(char_1, char_2) -->
### Function: cgreaterpignore (char_1, char_2)

`cgreaterp`と同様ですが、文字の大小を無視します。

<!-- category: IO -->
<!-- keywords: charat -->
<!-- signatures: charat(string, n) -->
### Function: charat (string, n)

*string*の*n*番目の文字を返します。
*string*の一番目の文字は*n* = 1で返されます。






```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
```

<!-- category: IO -->
<!-- keywords: charlist -->
<!-- signatures: charlist(string) -->
### Function: charlist (string)

*string*の文字すべてのリストを返します。







```maxima
(%i1) charlist("Lisp");
(%o1)                     [L, i, s, p]
(%i2) %[1];
(%o2)                           L
```

<!-- category: IO -->
<!-- keywords: charp -->
<!-- signatures: charp(obj) -->
### Function: charp (obj)

もし*obj*がMaxima-文字なら`true`を返します。
例えばイントロダクションを参照してください。

<!-- category: IO -->
<!-- keywords: cint -->
<!-- signatures: cint(char) -->
### Function: cint (char)

*char*のASCIIコードを返します。

<!-- category: IO -->
<!-- keywords: clessp -->
<!-- signatures: clessp(char_1, char_2) -->
### Function: clessp (char_1, char_2)

もし*char_1*のASCIIコードが*char_2*のそれより小さいなら`true`を返します。

<!-- category: IO -->
<!-- keywords: clesspignore -->
<!-- signatures: clesspignore(char_1, char_2) -->
### Function: clesspignore (char_1, char_2)

`clessp`と同様ですが、文字の大小を無視します。

<!-- category: IO -->
<!-- keywords: close -->
<!-- signatures: close(stream) -->
### Function: close (stream)

*stream*を閉じて、
もし*stream*が開いていたら
`true`を返します。

<!-- category: IO -->
<!-- keywords: constituent -->
<!-- signatures: constituent(char) -->
### Function: constituent (char)

もし*char*がグラフィック文字であり、スペース文字でないなら、
`true`を返します。
グラフィック文字は見ることができる文字とスペース文字です。
(`constituent`は、Paul Graham, ANSI Common Lisp, 1996, page 67で定義されています。)







```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if constituent(tmp) then sprint(tmp) )$
! " #  %  ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c
d e f g h i j k l m n o p q r s t u v w x y z { | } ~
```

<!-- category: IO -->
<!-- keywords: cunlisp -->
<!-- signatures: cunlisp(lisp_char) -->
### Function: cunlisp (lisp_char)

Lisp文字をMaxima文字に変換します。
(必要としないでしょう。)

<!-- category: IO -->
<!-- keywords: digitcharp -->
<!-- signatures: digitcharp(char) -->
### Function: digitcharp (char)

もし*char*が0から9までの数字なら、
`true`を返します。

<!-- category: IO -->
<!-- keywords: eval_string -->
<!-- signatures: eval_string(str) -->
### Function: eval_string (str)

文字列*str*をMaxima式としてパースし、評価します。
文字列*str*は終端子(ドル記号`$`またはセミコロン`;`)
を持つかもしれませんし持たないかもしれません。


もし複数あるなら、最初の式だけがパースされ、評価されます。


もし*str*が文字列でないならエラーが出力されます。


例:







```maxima
(%i1) eval_string ("foo: 42; bar: foo^2 + baz");
(%o1)                       42
(%i2) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o2)                   baz + 1764
```


`parse_string`も参照してください。

<!-- category: IO -->
<!-- keywords: flength -->
<!-- signatures: flength(stream) -->
### Function: flength (stream)

*stream*の中の要素の数を返します。

<!-- category: IO -->
<!-- keywords: fposition -->
<!-- signatures: fposition(stream), fposition(stream, pos) -->
### Function: fposition (stream)

もし*pos*が使われてないなら、
*stream*の中の現在位置を返します。
もし*pos*が使われているなら、
`fposition`は*stream*の中の位置を設定します。
*pos*は正の数でなければいけません。
*stream*の最初の要素は位置1にあります。

<!-- category: IO -->
<!-- keywords: freshline -->
<!-- signatures: freshline(), freshline(stream) -->
### Function: freshline ()

もし位置が行の最初でないなら
(*stream*に)改行を書きます。
`newline`も参照してください。

<!-- category: IO -->
<!-- keywords: lcharp -->
<!-- signatures: lcharp(obj) -->
### Function: lcharp (obj)

もし *obj*がLisp文字なら、`true`を返します。
(必要としないでしょう。)

<!-- category: IO -->
<!-- keywords: lowercasep -->
<!-- signatures: lowercasep(char) -->
### Function: lowercasep (char)

もし*char*が小文字なら、`true`を返します。

<!-- category: IO -->
<!-- keywords: newline -->
<!-- signatures: newline(), newline(stream) -->
### Function: newline ()

(*stream*に)改行を書きます。
`newline()`の使用の例に関しては、
`sprint`を参照してください。
`newline()`が期待通りに動かない
いくつかの場合があることに注意してください。

<!-- category: IO -->
<!-- keywords: opena -->
<!-- signatures: opena(file) -->
### Function: opena (file)

*file*への出力ストリームを返します。
もし存在しているファイルを開いたら、
`opena`はファイルの終わりに要素を追加します。

<!-- category: IO -->
<!-- keywords: openr -->
<!-- signatures: openr(file) -->
### Function: openr (file)

*file*への入力ストリームを返します。
もし*file*が存在しないなら、生成されます。

<!-- category: IO -->
<!-- keywords: openw -->
<!-- signatures: openw(file) -->
### Function: openw (file)

*file*への出力ストリームを返します。
もし*file*が存在しないなら、生成されます。
もし存在しているファイルを開いたら、`openw`は
*file*を破壊的に変更します。

<!-- category: IO -->
<!-- keywords: parse_string -->
<!-- signatures: parse_string(str) -->
### Function: parse_string (str)

文字列*str*をMaxima式としてパースします(評価しません)。
文字列*str*は終端子(ドル記号`$`またはセミコロン`;`)
を持つかもしれませんし持たないかもしれません。


もし複数あるなら、最初の式だけがパースされ、評価されます。


もし*str*が文字列でないならエラーが出力されます。


例:







```maxima
(%i1) parse_string ("foo: 42; bar: foo^2 + baz");
(%o1)                    foo : 42
(%i2) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o2)          (foo : 42, bar : foo  + baz)
```


`eval_string`も参照してください。

<!-- category: IO -->
<!-- keywords: printf -->
<!-- signatures: printf(dest, string), printf(dest, string, expr_1, ..., expr_n) -->
### Function: printf (dest, string)

Common Lisp関数FORMATをMaximaで利用可能にします。
(gcl.infoから:
「フォーマットは
制御文字列の文字を出力し、波形記号がディレクティブを挿入することを守ることで、
フォーマットされた出力を生成します。
波形記号の後の文字は多分、前置パラメータと修飾語が先行し、
望まれるフォーマットの種類を指定します。
ほとんどのディレクティブは、出力を生成するために1つまたは複数の引数を使います。」)


以下の記述と例は`printf`を使うアイデアを与えるかもしれません。
さらなる情報に関して、Lisp参考文献を参照してください。



```maxima
~%       改行
   ~&       行のフレッシュ
   ~t       タブ
   ~$       通貨記号
   ~d       10進整数
   ~b       2進整数
   ~o       8進整数
   ~x       16進整数
   ~br      b進整数
   ~r       整数を一字一字
   ~p       複数形
   ~f       浮動小数点
   ~e       科学的記数法
   ~g       大きさに応じて~fまたは~e
   ~h       多倍長浮動小数点
   ~a       Maxima関数文字列を使う
   ~s       ~aと同様, しかし"ダブルコーテーション"で囲まれた出力
   ~~       ~
   ~<       行揃え, ~> 終端
   ~(       大文字小文字変換, ~) 終端
   ~[       選択, ~] 終端
   ~{       繰り返し, ~} 終端
```


選択ディレクティブ`~[`は添字がゼロから始まることに注意してください。
ディレクティブ~*がサポートされていないことにも注意してください。












```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf(true,"~{~{~9,1f ~}~%~}",mat ),
          mat = args(matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]))$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false,control, n,n,if n=1 then 0 else 1 ), n=2;
(%o5)                    Two birds are singing.
```


もし*dest*がストリームか`true`なら、
`printf`は`false`を返します。
そうでないなら、`printf`は出力を含む文字列を返します。

<!-- category: IO -->
<!-- keywords: readline -->
<!-- signatures: readline(stream) -->
### Function: readline (stream)

*stream*の現在位置から行の終わりまでの文字を含む文字列か、
もしファイルの終わりが来たら*false*を返します。

<!-- category: IO -->
<!-- keywords: scopy -->
<!-- signatures: scopy(string) -->
### Function: scopy (string)

*string*のコピーを新しい文字列として返します。

<!-- category: IO -->
<!-- keywords: sdowncase -->
<!-- signatures: sdowncase(string), sdowncase(string, start), sdowncase(string, start, end) -->
### Function: sdowncase (string)

`supcase`と同様ですが、大文字が小文字に変換されます。

<!-- category: IO -->
<!-- keywords: sequal -->
<!-- signatures: sequal(string_1, string_2) -->
### Function: sequal (string_1, string_2)

もし*string_1*と*string_2*が同じ長さで、同じ文字を含むなら、
`true`を返します。

<!-- category: IO -->
<!-- keywords: sequalignore -->
<!-- signatures: sequalignore(string_1, string_2) -->
### Function: sequalignore (string_1, string_2)

`sequal`と同様ですが、文字の大小を無視します。

<!-- category: IO -->
<!-- keywords: sexplode -->
<!-- signatures: sexplode(string) -->
### Function: sexplode (string)

`sexplode`は関数`charlist`の別名です。

<!-- category: IO -->
<!-- keywords: simplode -->
<!-- signatures: simplode(list), simplode(list, delim) -->
### Function: simplode (list)

`simplode`は式のリストを取り、それらを結合して文字列にします。
もしデリミタ*delim*が指定されないなら、
`simplode`はデリミタを使いません。
*delim*は任意の文字列を取り得ます。








```maxima
(%i1) simplode(["xx[",3,"]:",expand((x+y)^3)]);
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) simplode( sexplode("stars")," * " );
(%o2)                   s * t * a * r * s
(%i3) simplode( ["One","more","coffee."]," " );
(%o3)                   One more coffee.
```

<!-- category: IO -->
<!-- keywords: sinsert -->
<!-- signatures: sinsert(seq, string, pos) -->
### Function: sinsert (seq, string, pos)

`substring (string, 1, pos - 1)`と
文字列*seq*、`substring (string, pos)`
の結合となる文字列を返します。
*string*の一番目の文字は位置1にあることに注意してください。








```maxima
(%i1) s: "A submarine."$
(%i2) concat( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

<!-- category: IO -->
<!-- keywords: sinvertcase -->
<!-- signatures: sinvertcase(string), sinvertcase(string, start), sinvertcase(string, start, end) -->
### Function: sinvertcase (string)

位置*start*から*end*までのそれぞれの文字を逆順にすることを除いて
*string*を返します。
もし*end*が与えられないなら、
*start*から
*string*の終わりまでのすべての文字列が置き換えられます。






```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

<!-- category: IO -->
<!-- keywords: slength -->
<!-- signatures: slength(string) -->
### Function: slength (string)

*string*の中の文字の数を返します。

<!-- category: IO -->
<!-- keywords: smake -->
<!-- signatures: smake(num, char) -->
### Function: smake (num, char)

*num*個の文字*char*を持つ新しい文字列を返します。






```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

<!-- category: IO -->
<!-- keywords: smismatch -->
<!-- signatures: smismatch(string_1, string_2), smismatch(string_1, string_2, test) -->
### Function: smismatch (string_1, string_2)

*string_1*と*string_2*が異なる*string_1*の最初の文字の位置、または
`false`を返します。
マッチングのデフォルトのテスト関数は`sequal`です。
もし`smismatch`が文字の大小を無視なければいけないなら、
テストとして`sequalignore`を使ってください。






```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

<!-- category: IO -->
<!-- keywords: space -->
<!-- signatures: space -->
### Variable: space

スペース文字。

<!-- category: IO -->
<!-- keywords: split -->
<!-- signatures: split(string), split(string, delim), split(string, delim, multiple) -->
### Function: split (string)

*string*のすべてのトークンのリストを返します。
それぞれのトークンはパースされていない文字列です。
`split`は*delim*をデリミタとして使います。
もし*delim*が与えられないなら、
スペース文字がデフォルトのデリミタです。
*multiple*はデフォルトで`true`のブーリアン変数です。
重複デリミタが1つとして読まれます。
これは、
もしタブが複数スペース文字として保存されているなら、
役立ちます。
もし*multiple*が`false`に設定されるなら、
それぞれのデリミタが有効です。







```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

<!-- category: IO -->
<!-- keywords: sposition -->
<!-- signatures: sposition(char, string) -->
### Function: sposition (char, string)

*string*の中で、*char*とマッチする最初の文字の位置を返します。
*string*の一番目の文字は位置1にあります。
文字の大小を無視した文字のマッチに関しては，
`ssearch`を参照してください。

<!-- category: IO -->
<!-- keywords: sprint -->
<!-- signatures: sprint(expr_1, ..., expr_n) -->
### Function: sprint (expr_1, ..., expr_n)

引数を順に評価し、一番左から始まる「一行」に表示します。
数は数の右隣に’-’と共に印字され、行の長さを無視します。
もし中間行ブレークを置きたいなら、
`newline()`―`stringproc.lisp` から自動ロードされます―
が役に立つかもしれません。


例:








```maxima
(%i1) for n:0 thru 19 do sprint( fib(n) )$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), if mod(n,10)=9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

<!-- category: IO -->
<!-- keywords: sremove -->
<!-- signatures: sremove(seq, string), sremove(seq, string, test), sremove(seq, string, test, start), sremove(seq, string, test, start, end) -->
### Function: sremove (seq, string)

*string*同様文字列を返しますが、
*seq*とマッチする部分文字列すべてなしに返します。
マッチのデフォルトのテスト関数は`sequal`です。
もし`sremove`が*seq*を検索する間文字の大小を無視しなければいけないなら、
テストとして`sequalignore`を使ってください。
探索を限定するには*start*と*end*を使ってください。
*string*の一番目の文字は位置1にあることに注意してください。







```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

<!-- category: IO -->
<!-- keywords: sremovefirst -->
<!-- signatures: sremovefirst(seq, string), sremovefirst(seq, string, test), sremovefirst(seq, string, test, start), sremovefirst(seq, string, test, start, end) -->
### Function: sremovefirst (seq, string)

`seq`とマッチする最初の文字列だけが削除されることを除いて、
`sremove`同様です。

<!-- category: IO -->
<!-- keywords: sreverse -->
<!-- signatures: sreverse(string) -->
### Function: sreverse (string)

*string*の文字すべてが逆順の文字列を返します。

<!-- category: IO -->
<!-- keywords: ssearch -->
<!-- signatures: ssearch(seq, string), ssearch(seq, string, test), ssearch(seq, string, test, start), ssearch(seq, string, test, start, end) -->
### Function: ssearch (seq, string)

文字列*seq*とマッチする*string*の最初の部分文字列の位置を返します。
マッチのためのデフォルトのテスト関数は`sequal`です。
もし`ssearch`が文字の大小を無視しなければいけないなら、
テストとして`sequalignore`を使ってください。
検索を限定するには、*start*と*end*を使ってください。
*string*の一番目の文字は位置1にあることに注意してください。



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

<!-- category: IO -->
<!-- keywords: ssort -->
<!-- signatures: ssort(string), ssort(string, test) -->
### Function: ssort (string)

`test (c, d)`が`false`、かつ、`test (d, c)`が`true`であるような2つの連続する文字*c*と*d*がないような順で
*string*の文字すべてを含む文字列を返します。


ソートのためのデフォルトのテスト関数は*clessp*です。
テスト関数一式は`{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`です。







```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

<!-- category: IO -->
<!-- keywords: ssubst -->
<!-- signatures: ssubst(new, old, string), ssubst(new, old, string, test), ssubst(new, old, string, test, start), ssubst(new, old, string, test, start, end) -->
### Function: ssubst (new, old, string)

*string*の中の*old*にマッチするすべての部分文字列を
*new*で置き換えた文字列を返します。
*old*と*new*は同じ長さである必要はありません。
マッチのためのデフォルトのテスト関数は`sequal`です。
もし`ssubst`がoldを検索する間大文字小文字を無視すべきなら、
テストとして`sequalignore`を使ってください。
検索を制限するには、*start*と*end*を使ってください。
*string*の一番目の文字は位置1にあることに注意してください。







```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

<!-- category: IO -->
<!-- keywords: ssubstfirst -->
<!-- signatures: ssubstfirst(new, old, string), ssubstfirst(new, old, string, test), ssubstfirst(new, old, string, test, start), ssubstfirst(new, old, string, test, start, end) -->
### Function: ssubstfirst (new, old, string)

*old*とマッチする最初の部分文字列だけを置き換えることを除いて、
`subst`と同様です。

<!-- category: IO -->
<!-- keywords: strim -->
<!-- signatures: strim(seq, string) -->
### Function: strim (seq, string)

*string*の両端から*seq*に現れるすべての文字を除いた文字列を返します。








```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

<!-- category: IO -->
<!-- keywords: striml -->
<!-- signatures: striml(seq, string) -->
### Function: striml (seq, string)

*string*の左端だけトリムすることを除いて
`strim`と同様です。

<!-- category: IO -->
<!-- keywords: strimr -->
<!-- signatures: strimr(seq, string) -->
### Function: strimr (seq, string)

*string*の右端だけトリムすることを除いて
`strim`と同様です。

<!-- category: IO -->
<!-- keywords: stringp -->
<!-- signatures: stringp(obj) -->
### Function: stringp (obj)

もし*obj*が文字列なら、`true`を返します。
例はイントロダクションを参照してください。

<!-- category: IO -->
<!-- keywords: substring -->
<!-- signatures: substring(string, start), substring(string, start, end) -->
### Function: substring (string, start)

位置*start*で始まり位置*end*で終わる
*string*の部分文字列を返します。
位置*end*の文字は含まれません。
もし*end*が与えられないなら、部分文字列は文字列の残りを含みます。
*string*の一番目の文字は位置1にあることに注意してください。







```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

<!-- category: IO -->
<!-- keywords: supcase -->
<!-- signatures: supcase(string), supcase(string, start), supcase(string, start, end) -->
### Function: supcase (string)

*string*の位置*start*から*end*までの小文字を対応する大文字に置き換えた
文字列を返します。
もし*end*が与えられないなら、
*start*から*string*の終わりまでのすべての小文字が置き換えられます。






```maxima
(%i1) supcase("english",1,2);
(%o1)                        English
```

<!-- category: IO -->
<!-- keywords: tab -->
<!-- signatures: tab -->
### Variable: tab

タブ文字。

<!-- category: IO -->
<!-- keywords: tokens -->
<!-- signatures: tokens(string), tokens(string, test) -->
### Function: tokens (string)

*string*から抽出されたトークンのリストを返します。
トークンは、文字があるテスト関数を満たす部分文字列です。
もしテストが与えられないなら、
*constituent*がデフォルトテストとして使われます。
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}`はテスト関数一式です。
(The Lisp-version of 
`tokens`のLispバージョンはPaul Grahamによって書かれました。 ANSI Common Lisp, 1996, page 67.)








```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parse_string,%);
(%o3)                      [5, 10, 24]
```

<!-- category: IO -->
<!-- keywords: uppercasep -->
<!-- signatures: uppercasep(char) -->
### Function: uppercasep (char)

もし*char*が大文字なら、`true`を返します。

