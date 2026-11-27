## Evaluation

<!-- category: Programming -->
<!-- keywords: ' -->
<!-- signatures: ' -->
### Function: '

シングルクォート演算子`'`は評価を抑制します。


シンボルにシングルクォートを用いると、シンボルが評価されません。


関数コールにシングルクォートを用いると、
関数の引数は（抑制されない限り）評価されますが、関数コールは評価されません。結果は、関数コールの名詞形です。


括弧でくくられた式にシングルクォートを用いると、
式の中のすべてのシンボルと関数コールは評価されません。

例えば、`'(f(x))`は、式`f(x)`を評価しないことを意味します。
`'f(x)`（`f(x)`ではなく`f`へ適用されたシングルクォート）は`[x]`に適用された`f`の名詞形を返します。


シングルクォートは式整理を抑制しません。


グローバルフラグ `noundisp`が `true`の時、名詞はシングルクォート付きで表示されます。
このスイッチは関数定義を表示するときには、常に`true`です。


クォートクォート演算子 `quote-quote`と `nouns`も参照ください。


例:


シンボルにシングルクォートを用いると、シンボルが評価されません。









```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) aa^2;
(%o2)                        1048576
(%i3) 'aa^2;
                                 2
(%o3)                          aa
(%i4) ''%;
(%o4)                        1048576
```


関数コールにシングルクォートを用いると、関数の引数は評価されますが、関数コールが評価されません。
結果は、関数コールの名詞形です。










```maxima
(%i1) x0: 5;
(%o1)                           5
(%i2) x1: 7;
(%o2)                           7
(%i3) integrate (x^2, x, x0, x1);
                               218
(%o3)                          ---
                                3
(%i4) 'integrate (x^2, x, x0, x1);
                             7
                            /
                            [   2
(%o4)                       I  x  dx
                            ]
                            /
                             5
(%i5) %, nouns;
                               218
(%o5)                          ---
                                3
```


括弧でくくられた式にシングルクォートを用いると、式の中のすべてのシンボルと関数コールは評価されません。










```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) bb: 19;
(%o2)                          19
(%i3) sqrt(aa) + bb;
(%o3)                          51
(%i4) '(sqrt(aa) + bb);
(%o4)                     bb + sqrt(aa)
(%i5) ''%;
(%o5)                          51
```


シングルクォートは式整理を抑制しません。







```maxima
(%i1) sin (17 * %pi) + cos (17 * %pi);
(%o1)                          - 1
(%i2) '(sin (17 * %pi) + cos (17 * %pi));
(%o2)                          - 1
```


Maximaは組み込み数学関数による浮動小数点演算を整理とみなします。







```maxima
(%i1) sin(1.0);
(%o1)                          .8414709848078965
(%i2) '(sin(1.0));
(%o2)                          .8414709848078965
```

See also: `noundisp`, `quote-quote`, `nouns`.

<!-- category: Programming -->
<!-- keywords: '' -->
<!-- signatures: '' -->
### Function: ''

クォートクォート演算子`''`(シングルクォートマーク２つ）は、入力式の中の評価を部分修正します。


一般式*expr*にクォートクォートを用いると、入力式の中の*expr*に*expr*の値を代入します。


式の演算子にクォートクォートを用いると、（もし動詞でないなら）演算子は名詞から動詞に変わります。


クォートクォート演算子は入力パーサが適用します;
クォートクォート演算子はパースされた入力式の一部としては格納されません。
クォートクォート演算子は、パースされるといつもすぐに適用され、クォートできません。
このように、関数定義やラムダ式、シングルクォート`'`でクォートされた式の中のように通常評価が抑制される時も、
クォートクォートがあると評価を実行します。


`batch`や`load`はクォートクォートを認識します。


シングルクォート演算子 `quote`と `nouns`も参照ください。


例:


一般式*expr*にクォートクォートを用いると、入力式の中の*expr*に*expr*の値を代入します。



















```maxima
(%i1) expand ((a + b)^3);
                     3        2      2      3
(%o1)               b  + 3 a b  + 3 a  b + a
(%i2) [_, ''_];
                         3    3        2      2      3
(%o2)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i3) [%i1, ''%i1];
                         3    3        2      2      3
(%o3)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i4) [aa : cc, bb : dd, cc : 17, dd : 29];
(%o4)                   [cc, dd, 17, 29]
(%i5) foo_1 (x) := aa - bb * x;
(%o5)                 foo_1(x) := aa - bb x
(%i6) foo_1 (10);
(%o6)                      cc - 10 dd
(%i7) ''%;
(%o7)                         - 273
(%i8) ''(foo_1 (10));
(%o8)                         - 273
(%i9) foo_2 (x) := ''aa - ''bb * x;
(%o9)                 foo_2(x) := cc - dd x
(%i10) foo_2 (10);
(%o10)                        - 273
(%i11) [x0 : x1, x1 : x2, x2 : x3];
(%o11)                    [x1, x2, x3]
(%i12) x0;
(%o12)                         x1
(%i13) ''x0;
(%o13)                         x2
(%i14) '' ''x0;
(%o14)                         x3
```


式の演算子にクォートクォートを用いると、（もし動詞でないなら）演算子は名詞から動詞に変わります。









```maxima
(%i1) declare (foo, noun);
(%o1)                         done
(%i2) foo (x) := x - 1729;
(%o2)                 ''foo(x) := x - 1729
(%i3) foo (100);
(%o3)                       foo(100)
(%i4) ''foo (100);
(%o4)                        - 1629
```


クォートクォート演算子は入力パーサが適用します；
クォートクォート演算子はパースされた入力式の一部としては格納されません。










```maxima
(%i1) [aa : bb, cc : dd, bb : 1234, dd : 5678];
(%o1)                 [bb, dd, 1234, 5678]
(%i2) aa + cc;
(%o2)                        dd + bb
(%i3) display (_, op (_), args (_));
                           _ = cc + aa

                         op(cc + aa) = +

                    args(cc + aa) = [cc, aa]

(%o3)                         done
(%i4) ''(aa + cc);
(%o4)                         6912
(%i5) display (_, op (_), args (_));
                           _ = dd + bb

                         op(dd + bb) = +

                    args(dd + bb) = [dd, bb]

(%o5)                         done
```


関数定義やラムダ式、シングルクォート`'`でクォートされた式の中のように
通常評価が抑制される時も、
クォートクォートがあると評価を実行します。
















```maxima
(%i1) foo_1a (x) := ''(integrate (log (x), x));
(%o1)               foo_1a(x) := x log(x) - x
(%i2) foo_1b (x) := integrate (log (x), x);
(%o2)           foo_1b(x) := integrate(log(x), x)
(%i3) dispfun (foo_1a, foo_1b);
(%t3)               foo_1a(x) := x log(x) - x

(%t4)           foo_1b(x) := integrate(log(x), x)

(%o4)                      [%t3, %t4]
(%i5) integrate (log (x), x);
(%o5)                     x log(x) - x
(%i6) foo_2a (x) := ''%;
(%o6)               foo_2a(x) := x log(x) - x
(%i7) foo_2b (x) := %;
(%o7)                    foo_2b(x) := %
(%i8) dispfun (foo_2a, foo_2b);
(%t8)               foo_2a(x) := x log(x) - x

(%t9)                    foo_2b(x) := %

(%o9)                      [%t7, %t8]
(%i10) F : lambda ([u], diff (sin (u), u));
(%o10)             lambda([u], diff(sin(u), u))
(%i11) G : lambda ([u], ''(diff (sin (u), u)));
(%o11)                  lambda([u], cos(u))
(%i12) '(sum (a[k], k, 1, 3) + sum (b[k], k, 1, 3));
(%o12)         sum(b , k, 1, 3) + sum(a , k, 1, 3)
                    k                  k
(%i13) '(''(sum (a[k], k, 1, 3)) + ''(sum (b[k], k, 1, 3)));
(%o13)             b  + a  + b  + a  + b  + a
                    3    3    2    2    1    1
```

See also: `batch`, `load`, `quote`, `nouns`.

<!-- category: Programming -->
<!-- keywords: ev -->
<!-- signatures: ev(expr, arg_1, ..., arg_n) -->
### Function: ev (expr, arg_1, ..., arg_n)

引数*arg_1*, ..., *arg_n*で指定された環境下で
式*expr*を評価します。
引数は、スイッチ（ブーリアンフラグ）だったり、割り当てだったり、
等式だったり、関数だったりします。
*ev*は評価の結果（別の式）を返します。


評価は以下のようにステップを追って実行されます。



1. 最初に、以下の任意のもしくはすべての引数をスキャンして環境を準備します。



  - *
`simp`を引数に指定すると*expr*を整理します。`false`なら整理を抑制するスイッチ`simp`の設定に関わらずです。
  - *
`noeval`を引数に指定すると`ev`の評価フェイズを抑制します。
（以下のステップ(4)を参照してください。）
これは、他のスイッチとの連携時や、*expr*を再評価せずに再整理をさせる時に役に立ちます。
  - *
`nouns`を引数に指定すると*expr*の中の名詞形式
（典型的には、`'integrate`や`'diff`のような未評価関数）を評価します。
  - *
`expand`を引数に指定すると展開します。
  - *
`expand (m, n)`を引数に指定すると、
`maxposex`と`maxnegex`の値をそれぞれ*m*と*n*に設定して、展開します。
  - *
`detout`を引数に指定すると、*expr*の中で計算されるどんな逆行列も、逆行列の外側に行列式を保つようにします。
  - *
`diff`を引数に指定すると*expr*の中のすべての微分を実行します。
  - *
`derivlist (x, y, z, ...)`を引数に指定すると指定された変数に関する微分のみを実行します。
  - *
`risch`を引数に指定すると
*expr*の中の積分をRischアルゴリズムを使って評価します。
`risch`を参照してください。
特殊なシンボル`nouns`を使った時には標準の積分ルーチンが呼び出されます。
  - *
`float`を引数に指定すると非整数有理数を浮動小数点に変換します。
  - *
`numer`を引数に指定すると数値引数が指定された（指数関数を含む）いくつかの数学関数を浮動小数点に評価します。
また、*expr*の中の numerval宣言された変数は、宣言された値に置き換えられます。
また、`float`スイッチをオンにします。
  - *
`pred`を引数に指定すると述語（`true`もしくは`false`に評価される式）を評価します。
  - *
`eval`を引数に指定すると*expr*の特別な後評価をします。（ステップ(5)を参照。）
`eval`は複数回起こるかもしれません。`eval`のそれぞれのインスタンスのために、式は再評価されます。
  - *
評価フラグ（`evflag`を参照）として宣言されたアトム`A`を引数に指定すると、
*expr*の評価の最中、`A`が`true`にバインドされます。
  - *
`V: expression`（もしくは代わりに`V=expression`）を引数に指定すると、
*expr*の評価の最中、`V`が`expression`の値にバインドされます。
もし`V`がMaximaオプションなら、*expr*の評価の最中、`V`の値に`expression`が使われることに注意してください。
もし`ev`の複数の引数がこのタイプの場合、並列してバインドされます。
もし`V`が非アトムの式なら、バインドではなく、代入が実行されます。
  - *
関数名 `F`が評価関数(`evfun`参照)として宣言されている場合、
`F`を引数に指定すると `F`が *expr*に適用されます。
  - *
他のどんな関数名（例えば、`sum`)でも引数に指定すると、
*expr*の中にそれらの名前が現れた時それらが動詞であるかのように評価します。
  - *
加えて、exprの中で出現する関数（`F(x)`としましょう）を、
*expr*の今回の評価の目的のため、
`F(X) := expression`を`ev`の引数に与えて、局所的に定義することができます。
  - *
もし以上で言及しなかったアトム、添字付き変数、または、添字付き式が引数として与えられたら、
それを評価して、
もしその結果が等式もしくは割り当てであったら、示されたバインドもしくは代入を実行します。
もしその結果がリストなら、リストのメンバが、 `ev`に与えられた追加の引数であるかのように扱います。
これにより、 `solve`が返すような、与えられた等式のリスト
（例えば、 `[X=1,Y=A**2]`)や
等式の名前のリスト（例えば、 `[%t1, %t2]`。ここで `%t1`, `%t2`は等式）が使えます。


`ev`の引数は、代入等式と評価関数以外はどんな順序で与えてもかまいません。
代入等式は左から右へ順に扱われ、
評価関数は、例えば、 `ev (expr, ratsimp, realpart)`は
`realpart (ratsimp (expr))`と扱われるように、合成されます。


`simp`, `numer`, `float`スイッチは、ブロックの中でローカルにも、
またMaximaの中でグローバルにも設定でき、その場合，リセットされるまで効果を保ちます。


`numer`と`float`スイッチがともに`true`でない場合、
もし*expr*が標準有理式(CRE)なら、`ev`が返す式もまたCREです。
2. step (1)の最中に、引数の中のもしくは引数の値の、等式の左辺に現れる添字なしの変数のリストを作ります。
*expr*の中の変数（添字なし変数や配列関数に関連づけられていない添字付き変数）は、
先のリストに現れるものを除いて、グローバルな値に置き換えられます。
普通、 *expr*は、ただのラベルだったり
(以下の例の `%i2`のように） `%`だったりするので、
その場合，このステップは単にラベルされた式を取り出し、
`ev`はその式に対して機能することになります。
3. 引数で指定されたどんな代入文もすぐ実行されます。
4. （引数で`noeval`が指定されていない限り）結果の式は再評価され、
引数に従って整理されます。
*expr*の中のどんな関数コールもその中の変数が評価された後実行されること、
`ev(F(x))`は `F(ev(x))`のように振る舞うことに注意してください。
5. 引数の中の`eval`のそれぞれのインスタンスのために、step (3)(4)を繰り返します。


例:







```maxima
(%i1) sin(x) + cos(y) + (w+1)^2 + 'diff (sin(w), w);
                                     d                    2
(%o1)              cos(y) + sin(x) + -- (sin(w)) + (w + 1)
                                     dw
(%i2) ev (%, numer, expand, diff, x=2, y=1);
                             2
(%o2)              cos(w) + w  + 2 w + cos(1) + 2.449599732693821
```


`ev`のために、代わりのトップレベルの文法が提供されています。
それによって、`ev()`なしに引数をタイプして入力するだけでよくなります。
すなわち、単に以下のように書けます。



```maxima
expr, arg_1, ..., arg_n
```


これは、例えば、関数やブロックの中など、他の式の一部としては許されません。


以下の例では並列のバインドプロセスに注意してください。



```maxima
(%i3) programmode: false;
(%o3)                                false
(%i4) x+y, x: a+y, y: 2;
(%o4)                              y + a + 2
(%i5) 2*x - 3*y = 3$
(%i6) -3*x + 2*y = -4$
(%i7) solve ([%o5, %o6]);
Solution

                                          1
(%t7)                               y = - -
                                          5

                                         6
(%t8)                                x = -
                                         5
(%o8)                            [[%t7, %t8]]
(%i8) %o6, %o8;
(%o8)                              - 4 = - 4
(%i9) x + 1/x > gamma (1/2);
                                   1
(%o9)                          x + - > sqrt(%pi)
                                   x
(%i10) %, numer, x=1/2;
(%o10)                      2.5 > 1.772453850905516
(%i11) %, pred;
(%o11)                               true
```

See also: `simp`, `noeval`, `nouns`, `expand`, `maxposex`, `maxnegex`, `detout`, `diff`, `risch`, `float`, `numer`, `pred`, `eval`, `evflag`, `evfun`, `sum`, `solve`.

<!-- category: Programming -->
<!-- keywords: eval -->
<!-- signatures: eval -->
### Variable: eval

`ev (expr)`のコールの引数として、
`eval`は
*expr*の追加の評価をもたらします。
`ev`を参照してください。


例:










```maxima
(%i1) [a:b,b:c,c:d,d:e];
(%o1)                            [b, c, d, e]
(%i2) a;
(%o2)                                  b
(%i3) ev(a);
(%o3)                                  c
(%i4) ev(a),eval;
(%o4)                                  e
(%i5) a,eval,eval;
(%o5)                                  e
```

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: evflag -->
<!-- signatures: evflag -->
### Variable: evflag

シンボル`x`が`evflag`プロパティを持つ時、
式`ev(expr, x)`や対話プロンプトでの`expr, x`は、
`ev(expr, x = true)`と同値です。
すなわち、*expr*が評価される間、*x*は`true`にバインドされます。


式`declare(x, evflag)`は、変数*x*に`evflag`プロパティを与えます。


デフォルトで`evflag`プロパティを持つフラグは以下の通りです:





   algebraic          cauchysum       demoivre
   dotscrules         %emode          %enumer
   exponentialize     exptisolate     factorflag
   float              halfangles      infeval
   isolate_wrt_times  keepfloat       letrat
   listarith          logabs          logarc 
   logexpand          lognegint       lognumer 
   m1pbranch          numer_pbranch   programmode 
   radexpand          ratalgdenom     ratfac 
   ratmx              ratsimpexpons   simp 
   simpproduct        simpsum         sumexpand
   trigexpand


例:

















```maxima
(%i1) sin (1/2);
                                 1
(%o1)                        sin(-)
                                 2
(%i2) sin (1/2), float;
(%o2)                   0.479425538604203
(%i3) sin (1/2), float=true;
(%o3)                   0.479425538604203
(%i4) simp : false;
(%o4)                         false
(%i5) 1 + 1;
(%o5)                         1 + 1
(%i6) 1 + 1, simp;
(%o6)                           2
(%i7) simp : true;
(%o7)                         true
(%i8) sum (1/k^2, k, 1, inf);
                            inf
                            ====
                            \     1
(%o8)                        >    --
                            /      2
                            ====  k
                            k = 1
(%i9) sum (1/k^2, k, 1, inf), simpsum;
                                 2
                              %pi
(%o9)                         ----
                               6
(%i10) declare (aa, evflag);
(%o10)                        done
(%i11) if aa = true then YES else NO;
(%o11)                         NO
(%i12) if aa = true then YES else NO, aa;
(%o12)                         YES
```

<!-- category: Programming -->
<!-- keywords: evfun -->
<!-- signatures: evfun -->
### Variable: evfun

関数*F*が`evfun`プロパティを持つ時、
式`ev(expr, F)`や（対話プロンプトでの）`expr, F`は、
`F(ev(expr))`と同値です。


もし２つ以上の`evfun`関数*F*, *G*などが指定されたなら、関数は指定された順に適用されます。


式`declare(F, evfun)`は、関数*F*に`evfun`プロパティを与えます。


デフォルトで`evfun`プロパティを持つ関数は以下の通りです:





   bfloat          factor       fullratsimp
   logcontract     polarform    radcan
   ratexpand       ratsimp      rectform
   rootscontract   trigexpand   trigreduce


例:




















```maxima
(%i1) x^3 - 1;
                              3
(%o1)                        x  - 1
(%i2) x^3 - 1, factor;
                                2
(%o2)                 (x - 1) (x  + x + 1)
(%i3) factor (x^3 - 1);
                                2
(%o3)                 (x - 1) (x  + x + 1)
(%i4) cos(4 * x) / sin(x)^4;

                            cos(4 x)
(%o4)                       --------
                               4
                            sin (x)

(%i5) cos(4 * x) / sin(x)^4, trigexpand;
                 4           2       2         4
              sin (x) - 6 cos (x) sin (x) + cos (x)
(%o5)         -------------------------------------
                                4
                             sin (x)
(%i6) cos(4 * x) / sin(x)^4, trigexpand, ratexpand;
                           2         4
                      6 cos (x)   cos (x)
(%o6)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i7) ratexpand (trigexpand (cos(4 * x) / sin(x)^4));
                           2         4
                      6 cos (x)   cos (x)
(%o7)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i8) declare ([F, G], evfun);
(%o8)                         done
(%i9) (aa : bb, bb : cc, cc : dd);
(%o9)                          dd
(%i10) aa;
(%o10)                         bb
(%i11) aa, F;
(%o11)                        F(cc)
(%i12) F (aa);
(%o12)                        F(bb)
(%i13) F (ev (aa));
(%o13)                        F(cc)
(%i14) aa, F, G;
(%o14)                      G(F(cc))
(%i15) G (F (ev (aa)));
(%o15)                      G(F(cc))
```

<!-- category: Programming -->
<!-- keywords: infeval -->
<!-- signatures: infeval -->
### Variable: infeval

「無限評価」モードにします。`ev`は、値が変わらなくなるまで式を繰り返し評価します。
このモードで変数(`X`とします）が評価されることを避けるには、単に`X='X`を`ev`の引数として含めます。
`ev (X, X=X+1, infeval)`のような式は、もちろん、無限ループを引き起こします。

<!-- category: Programming -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

`noeval`は、`ev`の評価フェイズを抑制します。
これは、他のスイッチとの関連や、
式を再評価することなしに再整理するのに役に立ちます。

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

`nouns`は`evflag`の１つです。
`ev`コマンドのオプションとして使われる時、
`nouns`は、式の中に現れる「名詞」形すべてを「動詞」に`ev`します。すなわち、それらを評価します。
`noun`, `nounify`, `verb`, `verbify`も参照してください。

See also: `evflag`, `ev`, `noun`, `nounify`, `verbify`.

<!-- category: Programming -->
<!-- keywords: pred -->
<!-- signatures: pred -->
### Variable: pred

`ev (expr)`のコールでの引数として、
`pred`は、
述語論理(`true`または`false`に評価される式)を評価するようにします。
`ev`を参照してください。


例:







```maxima
(%i1) 1<2;
(%o1)                                1 < 2
(%i2) 1<2,pred;
(%o2)                                true
```

See also: `ev`.

