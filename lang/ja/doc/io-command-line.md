## Command Line

<!-- category: IO -->
<!-- keywords: %edispflag -->
<!-- signatures: %edispflag -->
### Variable: %edispflag

デフォルト値: `false`


`%edispflag`が`true`の時、
Maximaは `%e`の負の指数乗を商として表示します。
例えば、`%e^-x`は `1/%e^x`と表示されます。
`exptdispflag`も参照してください。


例:








```maxima
(%i1) %e^-10;
                               - 10
(%o1)                        %e
(%i2) %edispflag:true$
(%i3) %e^-10;
                               1
(%o3)                         ----
                                10
                              %e
```

See also: `exptdispflag`.

<!-- category: IO -->
<!-- keywords: absboxchar -->
<!-- signatures: absboxchar -->
### Variable: absboxchar

デフォルト値: `!`


`absboxchar`は１行より広い式の回りに絶対値記号を描くのに使われる文字です。


例:



```maxima
(%i1) abs((x^3+1));
                            ! 3    !
(%o1)                       !x  + 1!
```

<!-- category: IO -->
<!-- keywords: disp -->
<!-- signatures: disp(expr_1, expr_2, ...) -->
### Function: disp (expr_1, expr_2, ...)

`display`のようですが、
等式ではなく引数の値だけが表示されます。
これは名前を持たない複雑な引数や引数の値だけに興味があって
名前には興味がない引数に役立ちます。


`ldisp`と`print`も参照してください。


例:








```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) disp(x, b[1,2], sin(1.0));
                               123

                                  2
                             x - x

                        .8414709848078965

(%o3)                         done
```

See also: `display`, `ldisp`, `print`.

<!-- category: IO -->
<!-- keywords: display -->
<!-- signatures: display(expr_1, expr_2, ...) -->
### Function: display (expr_1, expr_2, ...)

左辺が未評価の*expr_i*で、右辺が式の値の等式を行の中央に表示します。
この関数は、中間結果を表示するのにブロックや`for`文の中で役立ちます。
`display`の引数は、通常アトムや、添字付き変数、関数コールです。
`disp`も参照してください。


`ldisplay`, `disp`, `ldisp`も参照してください。


例:








```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) display(x, b[1,2], sin(1.0));
                             x = 123

                                      2
                         b     = x - x
                          1, 2

                  sin(1.0) = .8414709848078965

(%o3)                         done
```

See also: `for`, `ldisplay`, `disp`, `ldisp`.

<!-- category: IO -->
<!-- keywords: display2d -->
<!-- signatures: display2d -->
### Variable: display2d

デフォルト値: `true`


`display2d`が`false`の時、
コンソール表示は（２次元）形式ではなく文字列（１次元）形式です。


例:








```maxima
(%i1) x/(x^2+1);
                               x
(%o1)                        ------
                              2
                             x  + 1
(%i2) display2d:false$
(%i3) x/(x^2+1);
(%o3) x/(x^2+1)
```

<!-- category: IO -->
<!-- keywords: display_format_internal -->
<!-- signatures: display_format_internal -->
### Variable: display_format_internal

デフォルト値: `false`


`display_format_internal`が`true`の時、
式は数学的内部表現を隠すように変換されることなく表示されます。
表示は`part`ではなく`inpart`が返すものに対応します。


例:



```maxima
User     part       inpart
a-b;      a - b     a + (- 1) b

           a            - 1
a/b;       -         a b
           b
                       1/2
sqrt(x);   sqrt(x)    x

          4 X        4
X*4/3;    ---        - X
           3         3
```

<!-- category: IO -->
<!-- keywords: dispterms -->
<!-- signatures: dispterms(expr) -->
### Function: dispterms (expr)

*expr*をパーツ毎に一行ずつ使って表示します。
すなわち、最初に*expr*の演算子が表示され、
それぞれの項が別々に表示されます。
もし*expr*が他の方法で表示するには大きすぎるなら、
これは役に立ちます。
例えば、もし`P1`, `P2`, ...が非常に大きな式なら、
`P1 + P2 + ...`を一度に表示しようとする場合、
表示プログラムは保存の空き領域を使い尽くすかもしれません。
しかしながら、
`dispterms (P1 + P2 + ...)`は、
`P1`を表示し、その下に`P2`を表示し、という具合です。
`dispterms`を使わない時、
もし指数式が`A^B`のように表示するには広すぎるなら、
それは`expt (A, B)`
(もしくは`A^^B`の場合、`ncexpt (A, B)`）のように現れます。

<!-- category: IO -->
<!-- keywords: expt, ncexpt -->
<!-- signatures: expt(a, b), ncexpt(a, b) -->
### Function: expt (a, b)

もし指数式が`a^b`のように表示するには広すぎるなら、
`expt (a, b)`
(もしくは、`a^^b`の場合、`ncexpt (a, b)`
のように現れます。




`expt`や`ncexpt`は入力では認識されません。

<!-- category: IO -->
<!-- keywords: exptdispflag -->
<!-- signatures: exptdispflag -->
### Variable: exptdispflag

デフォルト値: `true`


`exptdispflag`が`true`の時、
Maximaは式を商を使って負の指数の式を表示します。


例:



```maxima
(%i1) exptdispflag:true;
(%o1)                         true
(%i2) 10^-x;
                                1
(%o2)                          ---
                                 x
                               10
(%i3) exptdispflag:false;
(%o3)                         false
(%i4) 10^-x;
                                - x
(%o4)                         10
```

<!-- category: IO -->
<!-- keywords: grind -->
<!-- signatures: grind(expr) -->
### Function: grind (expr)

関数`grind`は
コンソールにMaximaへの入力に適した形で*expr*を印刷します。
`grind`はいつも`done`を返します。


*expr*が関数名やマクロ名の時、
`grind`は、名前だけでなく関数やマクロ定義を出力します。


`string`も参照してください。
それは出力を印刷する代わりに文字列を返します。
`grind`は
`string`の出力より若干読みやすい方法で
式を印刷しようとします。


変数`grind`が`true`の時、
`string`や`stringout`の出力は
`grind`のそれと同じフォーマットです;
そうでなければ、それらの関数の出力を特別にフォーマットしようとはしません。
変数`grind`のデフォルト値は`false`です。


`grind`は `playback`の引数としても指定できます。
`grind`が存在する時、
`playback`は `grind`関数と同じフォーマットで入力式を印刷します。
そうでなければ、入力式を特にフォーマットしようとはしません。


`grind`は引数を評価します。


例:



























```maxima
(%i1) aa + 1729;
(%o1)                       aa + 1729
(%i2) grind (%);
aa+1729$
(%o2)                         done
(%i3) [aa, 1729, aa + 1729];
(%o3)                 [aa, 1729, aa + 1729]
(%i4) grind (%);
[aa,1729,aa+1729]$
(%o4)                         done
(%i5) matrix ([aa, 17], [29, bb]);
                           [ aa  17 ]
(%o5)                      [        ]
                           [ 29  bb ]
(%i6) grind (%);
matrix([aa,17],[29,bb])$
(%o6)                         done
(%i7) set (aa, 17, 29, bb);
(%o7)                   {17, 29, aa, bb}
(%i8) grind (%);
{17,29,aa,bb}$
(%o8)                         done
(%i9) exp (aa / (bb + 17)^29);
                                aa
                            -----------
                                     29
                            (bb + 17)
(%o9)                     %e
(%i10) grind (%);
%e^(aa/(bb+17)^29)$
(%o10)                        done
(%i11) expr: expand ((aa + bb)^10);
         10           9        2   8         3   7         4   6
(%o11) bb   + 10 aa bb  + 45 aa  bb  + 120 aa  bb  + 210 aa  bb
         5   5         6   4         7   3        8   2
 + 252 aa  bb  + 210 aa  bb  + 120 aa  bb  + 45 aa  bb
        9        10
 + 10 aa  bb + aa
(%i12) grind (expr);
bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6
     +252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2
     +10*aa^9*bb+aa^10$
(%o12)                        done
(%i13) string (expr);
(%o13) bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6\
+252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2+10*aa^9*\
bb+aa^10
(%i14) cholesky (A):= block ([n : length (A), L : copymatrix (A),
  p : makelist (0, i, 1, length (A))], for i thru n do
  for j : i thru n do
  (x : L[i, j], x : x - sum (L[j, k] * L[i, k], k, 1, i - 1),
  if i = j then p[i] : 1 / sqrt(x) else L[j, i] : x * p[i]),
  for i thru n do L[i, i] : 1 / p[i],
  for i thru n do for j : i + 1 thru n do L[i, j] : 0, L)$
(%i15) grind (cholesky);
cholesky(A):=block(
         [n:length(A),L:copymatrix(A),
          p:makelist(0,i,1,length(A))],
         for i thru n do
             (for j from i thru n do
                  (x:L[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),
                   if i = j then p[i]:1/sqrt(x)
                       else L[j,i]:x*p[i])),
         for i thru n do L[i,i]:1/p[i],
         for i thru n do (for j from i+1 thru n do L[i,j]:0),L)$
(%o15)                        done
(%i16) string (fundef (cholesky));
(%o16) cholesky(A):=block([n:length(A),L:copymatrix(A),p:makelis\
t(0,i,1,length(A))],for i thru n do (for j from i thru n do (x:L\
[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),if i = j then p[i]:1/sqrt(x\
) else L[j,i]:x*p[i])),for i thru n do L[i,i]:1/p[i],for i thru \
n do (for j from i+1 thru n do L[i,j]:0),L)
```

See also: `string`.

<!-- category: IO -->
<!-- keywords: ibase -->
<!-- signatures: ibase -->
### Variable: ibase

デフォルト値: `10`


`ibase`は Maximaが読む整数の基数です。


`ibase`は2から(十進数で)36までの任意の整数を割り当てられます。
`ibase`が10よりも大きい時、
数値は十進数字0から9に加えて、
`ibase`ディジットに必要なアルファベットA, B, C, ...で構成されます。
最初のディジットが0から9の時だけ文字はディジットとして解釈されます。
大文字小文字は区別されません。
許容される最も大きな基数36の数値は0から9までとAからZまでから構成されます。


`ibase`の値がいくつでも、
整数が小数点で終了する時は基数10として解釈されます。


`obase`も参照してください。


例:


`ibase` less than 10.








```maxima
(%i1) ibase : 2 $
(%i2) obase;
(%o2)                          10
(%i3) 1111111111111111;
(%o3)                         65535
```


10より大きな`ibase`。
最初のディジットが0から9までの時だけ文字はディジットとして解釈されます。












```maxima
(%i1) ibase : 16 $
(%i2) obase;
(%o2)                          10
(%i3) 1000;
(%o3)                         4096
(%i4) abcd;
(%o4)                         abcd
(%i5) symbolp (abcd);
(%o5)                         true
(%i6) 0abcd;
(%o6)                         43981
(%i7) symbolp (0abcd);
(%o7)                         false
```


整数が小数点で終了する時、基数10として解釈されます。









```maxima
(%i1) ibase : 36 $
(%i2) obase;
(%o2)                          10
(%i3) 1234;
(%o3)                         49360
(%i4) 1234.;
(%o4)                         1234
```

See also: `obase`.

<!-- category: IO -->
<!-- keywords: ldisp -->
<!-- signatures: ldisp(expr_1, ..., expr_n) -->
### Function: ldisp (expr_1, ..., expr_n)

式*expr_1*, ..., *expr_n*をコンソールに印刷出力として表示します。
`ldisp`は
引数それぞれに中間式ラベルを割り当て、ラベルのリストを返します。


`disp`, `display`, `ldisplay`も参照してください。


例:



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisp (e, f);
                                   3
(%t3)                       (b + a)

                     3        2      2      3
(%t4)               b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                   3
(%o4)                       (b + a)
(%i5) %t4;
                     3        2      2      3
(%o5)               b  + 3 a b  + 3 a  b + a
```

See also: `disp`, `display`, `ldisplay`.

<!-- category: IO -->
<!-- keywords: ldisplay -->
<!-- signatures: ldisplay(expr_1, ..., expr_n) -->
### Function: ldisplay (expr_1, ..., expr_n)

式*expr_1*, ..., *expr_n*をコンソールに印刷出力として表示します。
式それぞれは、
`lhs`が`ldisplay`の引数の１つで、`rhs`がその値の、
形式`lhs = rhs`の等式として表示されます。
典型的には引数それぞれは変数です。
`ldisp`は式それぞれに中間式ラベルを割り当て、ラベルのリストを返します。


`display`, `disp`も参照してください。


例:



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisplay (e, f);
                                     3
(%t3)                     e = (b + a)

                       3        2      2      3
(%t4)             f = b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                     3
(%o4)                     e = (b + a)
(%i5) %t4;
                       3        2      2      3
(%o5)             f = b  + 3 a b  + 3 a  b + a
```

See also: `display`, `disp`.

<!-- category: IO -->
<!-- keywords: linel -->
<!-- signatures: linel -->
### Variable: linel

デフォルト値: `79`


`linel`はコンソールディスプレイの仮定された(文字単位の)幅です。
`linel`はユーザーによって任意の値に割り当てられます。
非常に小さい値や非常に大きな値は実用的ではありませんが。
エラーメッセージや`describe`の出力のように、
Maximaの組み込み関数が表示するテキストは`linel`の影響を受けません。

See also: `describe`.

<!-- category: IO -->
<!-- keywords: lispdisp -->
<!-- signatures: lispdisp -->
### Variable: lispdisp

デフォルト値: `false`


`lispdisp`が`true`の時、
Lispシンボルはクエスチョンマーク`?`を先頭文字として表示されます。
そうでなければ、Lispシンボルは先頭文字を持ちません。


例:









```maxima
(%i1) lispdisp: false$
(%i2) ?foo + ?bar;
(%o2)                       foo + bar
(%i3) lispdisp: true$
(%i4) ?foo + ?bar;
(%o4)                      ?foo + ?bar
```

<!-- category: IO -->
<!-- keywords: negsumdispflag -->
<!-- signatures: negsumdispflag -->
### Variable: negsumdispflag

デフォルト値: `true`


`negsumdispflag`が`true`の時、
`x - y`は `- y + x`でなく`x - y`と表示されます。
`false`に設定すると、
２つの式の違いに関する表示での特殊なチェックがされないようになります。
１つの応用は、例えば、`a + %i*b`と`a - %i*b`を同じ表示にすることです。

<!-- category: IO -->
<!-- keywords: obase -->
<!-- signatures: obase -->
### Variable: obase

デフォルト値: `10`


`obase`はMaximaが表示する整数の基数です。


`obase`は2から(十進数で)36までの任意の整数を割り当てられます。
`obase`が10よりも大きい時、
数値は十進数字0から9に加えて、
必要な大文字アルファベットA, B, C, ...で構成されます。
もし先頭ディジットがそうでなければ文字なら、0ディジットが先頭に表示されます。
許容される最も大きな基数36の数値は0から9までとAからZまでから構成されます。


`ibase`も参照してください。


例:













```maxima
(%i1) obase : 2;
(%o1)                          10
(%i2) 2^8 - 1;
(%o10)                      11111111
(%i3) obase : 8;
(%o3)                          10
(%i4) 8^8 - 1;
(%o4)                       77777777
(%i5) obase : 16;
(%o5)                          10
(%i6) 16^8 - 1;
(%o6)                       0FFFFFFFF
(%i7) obase : 36;
(%o7)                          10
(%i8) 36^8 - 1;
(%o8)                       0ZZZZZZZZ
```

See also: `ibase`.

<!-- category: IO -->
<!-- keywords: pfeformat -->
<!-- signatures: pfeformat -->
### Variable: pfeformat

デフォルト値: `false`


`pfeformat`が`true`の時、
整数の比は斜線（スラッシュ）文字で表示され、
整数分母`n`は掛け算項`1/n`として先に表示されます。



```maxima
(%i1) pfeformat: false$
(%i2) 2^16/7^3;
                              65536
(%o2)                         -----
                               343
(%i3) (a+b)/8;
                              b + a
(%o3)                         -----
                                8
(%i4) pfeformat: true$ 
(%i5) 2^16/7^3;
(%o5)                       65536/343
(%i6) (a+b)/8;
(%o6)                      1/8 (b + a)
```

<!-- category: IO -->
<!-- keywords: powerdisp -->
<!-- signatures: powerdisp -->
### Variable: powerdisp

デフォルト値: `false`


`powerdisp`が`true`の時、
べきを増やす順に項を使って和が表示されます。
例えば、
多項式は切り詰められたべき級数として表示され、
最初に定数項最後に最高次項となります。


デフォルトでは和の項はべきを減らす順に表示されます。

<!-- category: IO -->
<!-- keywords: print -->
<!-- signatures: print(expr_1, ..., expr_n) -->
### Function: print (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を１つ１つ、左から右へ評価し、
コンソールディスプレイの左端から表示します。


`print`が返す値は最後の引数の値です。
`print`は中間式ラベルを生成しません。


`display`, `disp`, `ldisplay`, `ldisp`も参照してください。
これらの関数は一行ずつ１つの式を表示しますが、
`print`は一行に２つ以上の式を表示しようとします。


ファイルの中身を表示するには `printfile`を参照してください。


例:



```maxima
(%i1) r: print ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
            3        2      2      3
(a+b)^3 is b  + 3 a b  + 3 a  b + a  log (a^10/b) is 

                                              10 log(a) - log(b) 
(%i2) r;
(%o2)                  10 log(a) - log(b)
(%i3) disp ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
                           (a+b)^3 is

                     3        2      2      3
                    b  + 3 a b  + 3 a  b + a

                         log (a^10/b) is

                       10 log(a) - log(b)
```

See also: `display`, `disp`, `ldisplay`, `ldisp`, `printfile`.

<!-- category: IO -->
<!-- keywords: sqrtdispflag -->
<!-- signatures: sqrtdispflag -->
### Variable: sqrtdispflag

デフォルト値: `true`


`sqrtdispflag`が`false`の時、
`sqrt`を指数1/2で表示するようにします。

<!-- category: IO -->
<!-- keywords: stardisp -->
<!-- signatures: stardisp -->
### Variable: stardisp

デフォルト値: `false`


`stardisp`が`true`の時
掛け算はオペランドの間のアスタリスク`*`で表示されます。

<!-- category: IO -->
<!-- keywords: ttyoff -->
<!-- signatures: ttyoff -->
### Variable: ttyoff

デフォルト値: `false`


`ttyoff`が`true`の時、
出力式は表示されません。
出力式は計算され、ラベルに割り当てられます。
`labels`を参照してください。


エラーメッセージや`describe`の出力のように、組み込みMaxima関数によって出力されたテキストは `ttyoff`の影響を受けません。

