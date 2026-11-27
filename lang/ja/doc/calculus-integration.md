## Integration

<!-- category: Calculus -->
<!-- keywords: changevar -->
<!-- signatures: changevar(expr, f(x,y), y, x) -->
### Function: changevar (expr, f(x,y), y, x)

*x*に関する積分を含む*expr*の中に現れるすべての積分に関して、
`f(x,y) = 0`で与えられる変数変換を生成します。
新しい変数は*y*です。




```maxima
(%i1) assume(a > 0)$

(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     [    sqrt(a) sqrt(y)
(%o2)                I  %e                dy
                     ]
                     /
                      0


(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     [                abs(z)
                   2 I            z %e       dz
                     ]
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


上の`'integrate`のインスタンスのように、名詞形を含む式は
`nouns`フラグありの`ev`によって評価されるかもしれません。
例えば、上の`changevar`が返す式は`ev (%o3, nouns)`で評価することができます。


`changevar`は、
和や積のインデックスに関する変更にも使えます。
しかしながら、
変更が和や積の中でなされる時、
この変更はシフトすなわち`i = j+ ...`
でなければならず、高階関数ではなことをはっきり理解しなければいけません。
例えば、



```maxima
(%i4) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ====
                         \         i - 2
(%o4)                     >    a  x
                         /      i
                         ====
                         i = 0


(%i5) changevar (%, i-2-n, n, i);
                        inf
                        ====
                        \               n
(%o5)                    >      a      x
                        /        n + 2
                        ====
                        n = - 2
```

<!-- category: Calculus -->
<!-- keywords: dblint -->
<!-- signatures: dblint(f, r, s, a, b) -->
### Function: dblint (f, r, s, a, b)

トップレベルMaximaで書かれ、翻訳され機械語にコンパイルされた二重積分ルーチン。
このパッケージをアクセスするには`load ("dblint")`を使ってください。
以下を計算するため、xとy方向に関して
シンプソンの規則方法を使います。



$$
\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx.
$$


```maxima
/b /s(x)
|  |
|  |    f(x,y) dy dx
|  |
/a /r(x)
```


関数*f*は、２つの変数の翻訳されコンパイルされた関数でなければいけなく、
*r*と*s*はそれぞれ、翻訳されコンパイルされた変数でなければいけません。
一方で、*a*と*b*は浮動小数点数でなければいけません。
ルーチンは、
xとyの区間の分割の数を決める２つのグローバル変数を持ちます:
`dblint_x`と`dblint_y`,
両方とも初期は10で、他の整数値（x方向に計算される`2*dblint_x+1`点があり、
y方向に計算される`2*dblint_y+1`点があります）に独立に変えることができます。
ルーチンは、X軸を更に分割します。
Xのそれぞれの値に関して、最初、
`r(x)`と`s(x)`を計算します;
そして`r(x)`と`s(x)`の間でY軸が更に分割され、
シンプソン規則を使ってY軸に沿っての積分が実行されます;
そして、
シンプソン規則を使って
Y積分である関数値を用いてX軸に沿っての積分が実行されます;
この手続きは、様々な理由のため数値的に不安定かもしれませんが、
かなり速いです:
非常に振動的な関数や特異点（領域内の極や分岐点）を持つ関数にこれを使うことは避けてください。
Y積分は、`r(x)`と`s(x)`がどこくらい離れているかに依存します。
だから、もし距離`s(x) - r(x)`がXに関して急速に変化するなら、
様々なY積分での異なるステップサイズでの切り詰めから起こる本質的なエラーがあるかもしれません。
領域の範囲を改善するために、計算時間という犠牲を払って、`dblint_x`と`dblint_y`を増やすことができます。
関数値は保存されないので、もし関数が非常に時間がかかるものなら、
もし何か変えたら再計算を待たなければいけません（すいません）。
関数*f*, *r*, *s*は、 `dblint`コールの前に、翻訳されるかコンパイルされるかどちらかが要求されます。
これは、多くの場合、インタープリタコードに対して桁違いの速度改善がなされるでしょう！


`demo (dblint)`は、
例の問題に適用された`dblint`のデモンストレーションを実行します。

<!-- category: Calculus -->
<!-- keywords: defint -->
<!-- signatures: defint(expr, x, a, b) -->
### Function: defint (expr, x, a, b)

定積分を計算しようとします。
`integrate`は、
積分の範囲が指定されている時、
すなわち、`integrate`が
`integrate (expr, x, a, b)`としてコールされた時、
`defint`をコールします。


このように、ユーザーの観点からは、`integrate`をコールすることは十分です。



`defint`は、シンボリック式、計算された積分または積分の名詞形、
を返します。
定積分の数値近似に関しては、`quad_qag`と関連関数を参照してください。

<!-- category: Calculus -->
<!-- keywords: erfflag -->
<!-- signatures: erfflag -->
### Variable: erfflag

デフォルト値: `true`


`erfflag`が`false`の時、
`risch`が
もしまず第一に被積分になにもないなら、
答えの中に`erf`関数を導入することを妨げます。

<!-- category: Calculus -->
<!-- keywords: ilt -->
<!-- signatures: ilt(expr, s, t) -->
### Function: ilt (expr, s, t)

*expr*の*s*とパラメータ*t*に関する逆ラプラス変換を計算します。
*expr*は、
分子は線形２次因子だけを持つ多項式の比でなければいけません。
`solve`または`linsolve`と合わせて
関数`laplace`や`ilt`を使うことによって
ユーザーは１つの微分または畳み込み積分方程式やそれらの組を解くことができます。



```maxima
(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             [                                    2
(%o1)        I  f(t - x) sinh(a x) dx + b f(t) = t
             ]
             /
              0


(%i2) laplace (%, t, s);
                               a laplace(f(t), t, s)   2
(%o2)  b laplace(f(t), t, s) + --------------------- = --
                                       2    2           3
                                      s  - a           s


(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s


(%i4) ilt (rhs (first (%)), s, t);
Is  a b (a b - 1)  positive, negative, or zero?

pos;
               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a

                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a
```

<!-- category: Calculus -->
<!-- keywords: intanalysis -->
<!-- signatures: intanalysis -->
### Variable: intanalysis

デフォルト値: `true`


`true`の時、定積分は、積分区間内の被積分関数の極を見つけようとします。
もしあれば、積分は主値積分として適切に評価されます。
もしintanalysisが`false`なら、
このチェックは実行されず、積分は極がないことを仮定して実行されます。


`ldefint`も参照してください。


例:


`intanalysis`が`false`に設定されている時
Maximaは以下の積分を解くことができます:










```maxima
(%i1) integrate(1/(sqrt(x)+1),x,0,1);
                                1
                               /
                               [       1
(%o1)                          I  ----------- dx
                               ]  sqrt(x) + 1
                               /
                                0

(%i2) integrate(1/(sqrt(x)+1),x,0,1),intanalysis:false;
(%o2)                            2 - 2 log(2)

(%i3) integrate(cos(a)/sqrt((tan(a))^2 +1),a,-%pi/2,%pi/2);
The number 1 isn't in the domain of atanh
 -- an error. To debug this try: debugmode(true);

(%i4) intanalysis:false$
(%i5) integrate(cos(a)/sqrt((tan(a))^2+1),a,-%pi/2,%pi/2);
                                      %pi
(%o5)                                 ---
                                       2
```

<!-- category: Calculus -->
<!-- keywords: integrate -->
<!-- signatures: integrate(expr, x), integrate(expr, x, a, b) -->
### Function: integrate (expr, x)

*x*に関する*expr*の積分をシンボリックに計算しようとします。
`integrate (expr, x)`は不定積分で、
`integrate (expr, x, a, b)`は*a*,*b*の上限下限を持つ定積分です。
`integrate`はこの制限を強制しませんが、上限下限は*x*を含んではいけません。
*a*は*b*より小さい必要はありません。
*b*が*a*と等しいなら、`integrate`は0を返します。


定積分の数値近似に関しては`quad_qag`と関連関数を参照してください。
（複素積分）留数の計算に関しては`residue`を参照してください。
不定積分の代替計算方法に関しては`antid`を参照してください。


`integrate`が成功すれば、積分（`integrate`を含まない式）を返します。
そうでなければ、積分の名詞形式（クォートされた演算子`'integrate`)もしくは１つ以上の名詞形式を含む式を返します。
`integrate`の名詞形式は積分記号で表示されます。


いくつかの環境では、（例えば、`'integrate (expr, x)`のように、
シングルクオートされた`integrate`で手動で名詞形式を構成することが役に立ちます。
例えば、積分が、また計算されていないいくつかのパラメータに依存しているかもしれません。
名詞は、*i*が注目の名詞形式であるところの`ev (i, nouns)`によって、引数に適用されるかもしれません。



`integrate`は不定積分とは別に、定積分を扱います。
それぞれの場合を扱うため、ある範囲の発見法を用意しています。
定積分の特別な場合は、0や無限大に等しい積分の下限上限を含んだり、
0や`%pi`や`2 %pi`に等しい下限上限を持つ三角関数を含んだり、
有理関数やベータやプサイ関数の定義に関連した積分やいくつかの対数的な積分、三角関数積分を含んだりします。
有理関数の処理は、留数の計算を含むかもしれません。
もし適用可能な特殊な場合が見つからなければ、不定積分を計算し、下限上限でそれを評価しようとするでしょう。
これは、下限上限に無限大の極限を取ることを含みます。`ldefint`も参照してください。


不定積分の特殊な場合は、三角関数、指数対数関数、有理関数を含みます。
`integrate`は初等積分の短いテーブルもまた利用しています。


もし非積分関数が形式`f(g(x)) * diff(g(x), x)`を持つなら、`integrate`は、変数の交換を実行します。
`integrate`は、`g(x)`の導関数が非積分関数を割るような部分式`g(x)`を見つけようとします。
この探索は、`gradef`関数によって定義された導関数を利用します。
`changevar`や`antid`も参照ください。


もしこれまでの発見法のどれも不定積分を見つけられなければ、リッシュのアルゴリズムが実行されます。
フラグ`risch`が、`ev`のコールやコマンドライン上で`evflag`として設定されるかもしれません。
例えば、`ev (integrate (expr, x), risch)`や
`integrate (expr, x), risch`というように。
もし`risch`が`true`なら、`integrate`は、発見法を最初に試さずに、`risch`関数をコールします。
`risch`も参照ください。



`integrate`は`f(x)`記法で陽に表現された関数関係のみに動作します。
`integrate`は`depends`関数で規定された陰の依存性を考慮しません。


`integrate`は非積分関数のパラメータのある性質を知っている必要がある場合があります。
`integrate`は`assume`データベースを最初に参照し、
注目の変数がそこになければ、`integrate`はユーザーに問い合わせます。
質問に依存して、適切な応答は、`yes;`や`no;`や`pos;`, `zero;`, `neg;`など。


`integrate`は線形には宣言されていません。`declare`と`linear`を参照ください。


`integrate`は２、３の特集な場合だけ、部分積分を企てます。


例:



- *
初等不定積分、定積分

```maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3

(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )

(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5

(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```
- *
`assume`と対話的問い合わせの利用

```maxima
(%i1) assume (a > 1)$
(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
    2 a + 2
Is  -------  an integer?
       5
no;
Is  2 a - 3  positive, negative, or zero?
neg;
                                   3
(%o2)                  beta(a + 1, - - a)
                                   2
```
- *
変数変換。この例では２回変数変換があります。
`gradef`で規定された導関数を使ったものと未知関数`r(x)`の微分`diff(r(x))`を使ったもの。

```maxima
(%i3) gradef (q(x), sin(x**2));
(%o3)                         q(x)

(%i4) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o4)                ----------------------
                            q(r(x))

(%i5) integrate (%, x);
(%o5)                     log(q(r(x)))
```
- *
`'integrate`名詞形を含む戻り値。
この例では、Maximaは有理関数の分母の因子を抽出できますが、剰余を因数分解できないか積分をみつけられません。
`grind`は、結果として名詞形`'integrate`を示します。
積分や有理関数について更に知るには`integrate_use_rootsof`も参照ください。

```maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4

(%i2) integrate (1/%, x);
                              /  2
                              [ x  + 4 x + 18
                              I ------------- dx
                              ]  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73

(%i3) grind (%);
log(x-4)/73-('integrate((x^2+4*x+18)/(x^3+2*x+1),x))/73$
```
- *
積分を使った関数の定義。
関数の本体は、関数が定義された時には評価されません。
この例では、`f_1`の本体は、`integrate`の名詞形を含みます。
クォートクォート演算子`''`があると、積分が評価され、結果が`f_2`の本体になります。

```maxima
(%i1) f_1 (a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)

(%i2) ev (f_1 (7), nouns);
(%o2)                          600

(%i3) /* Note parentheses around integrate(...) here */
      f_2 (a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4

(%i4) f_2 (7);
(%o4)                          600
```

<!-- category: Calculus -->
<!-- keywords: integrate_use_rootsof -->
<!-- signatures: integrate_use_rootsof -->
### Variable: integrate_use_rootsof

デフォルト値: `false`


`integrate_use_rootsof`が`true`かつ有理関数の分子が因数分解できない時、
`integrate`は、
分子の（まだ知られていない）根上の和という形式で積分を返します。


例えば、
`integrate_use_rootsof`を`false`に設定すると、
`integrate`は、有理関数の未解決積分を名詞形で返します:



```maxima
(%i1) integrate_use_rootsof: false$

(%i2) integrate (1/(1+x+x^5), x);
        /  2
        [ x  - 4 x + 5
        I ------------ dx                            2 x + 1
        ]  3    2                2            5 atan(-------)
        / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2)   ----------------- - --------------- + ---------------
                7                 14             7 sqrt(3)
```


さて、フラグを`true`に設定し、
積分の未解決部分を
有理関数の分子の根上の和として表現しましょう:



```maxima
(%i3) integrate_use_rootsof: true$

(%i4) integrate (1/(1+x+x^5), x);
      ====        2
      \       (%r4  - 4 %r4 + 5) log(x - %r4)
       >      -------------------------------
      /                    2
      ====            3 %r4  - 2 %r4
                        3      2
      %r4 in rootsof(%r4  - %r4  + 1, %r4)
(%o4) ----------------------------------------------------------
               7

                                                      2 x + 1
                                  2            5 atan(-------)
                             log(x  + x + 1)          sqrt(3)
                           - --------------- + ---------------
                                   14             7 sqrt(3)
```


代わりにユーザーは別々に分子の根を計算できます。
例えば、もし分子が3次多項式なら
`1/((x - a)*(x - b)*(x - c))`または`1/((x^2 - (a+b)*x + a*b)*(x - c))`
というように
これらの根を使って被積分関数を表現できます。
時々、これはMaximaがもっと役立つ結果を得るのを助けます。

<!-- category: Calculus -->
<!-- keywords: integration_constant -->
<!-- signatures: integration_constant -->
### Variable: integration_constant

デフォルト値: `%c`


積分定数は、等式の不定積分によって導入され、
定数名は、
`integration_constant`と`integration_constant_counter`を連結することで構成されます。


`integration_constant`は、任意のシンボルに割り当てられます。


例:








```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integration_constant : 'k;
(%o2)                           k


(%i3) integrate (x^2 = 1, x);
                            3
                           x
(%o3)                      -- = x + k2
                           3
```

<!-- category: Calculus -->
<!-- keywords: integration_constant_counter -->
<!-- signatures: integration_constant_counter -->
### Variable: integration_constant_counter

デフォルト値: 0


積分定数が等式の不定積分によって導入された時、
定数名は、
`integration_constant`と`integration_constant_counter`を連結することで構成されます。


`integration_constant_counter`は、
次の積分定数を構成する前に増分されます。


例:










```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integrate (x^2 = 1, x);
                           3
                          x
(%o2)                     -- = x + %c2
                          3


(%i3) integrate (x^2 = 1, x);
                           3
                          x
(%o3)                     -- = x + %c3
                          3


(%i4) reset (integration_constant_counter);
(%o4)            [integration_constant_counter]


(%i5) integrate (x^2 = 1, x);
                           3
                          x
(%o5)                     -- = x + %c1
                          3
```

<!-- category: Calculus -->
<!-- keywords: ldefint -->
<!-- signatures: ldefint(expr, x, a, b) -->
### Function: ldefint (expr, x, a, b)

*expr*の*x*に関する不定積分を上限*b*と下限*a*で評価するために
`limit`を使うことによって*expr*の定積分を計算しようとします。
もし定積分を計算するのに失敗したなら、
`ldefint`は、名詞形として極限を含む式を返します。


`ldefint`は、`integrate`からコールされないので、
o executing 
`ldefint (expr, x, a, b)`
を実行することは、
`integrate (expr, x, a, b)`
とは違った結果をもたらすかもしれません。
`ldefint`は、定積分を評価するためにいつも同じ方法を使いますが、
`integrate`は、様々な発見的方法を利用し、いくつかの特殊な場合を認識することもあります。

<!-- category: Calculus -->
<!-- keywords: potential -->
<!-- signatures: potential(givengradient) -->
### Function: potential (givengradient)

計算は、
`nonlist`または形式


```maxima
[indeterminatej=expressionj, indeterminatek=expressionk, ...]
```

でなければならないグローバル変数`potentialzeroloc[0]`を利用します。
ここで、前者は後者の中のすべての右辺のnonlist式と同値です（訳者無理解）。
示された右辺は、積分の下限として使われます。
積分の成功は、
それらの値と順序に依存するかもしれません。
`potentialzeroloc`は、0に初期化されます。

<!-- category: Calculus -->
<!-- keywords: quad_qag -->
<!-- signatures: quad_qag(f(x), x, a, b, key, [epsrel, epsabs, limit]), quad_qag(f, x, a, b, key, [epsrel, epsabs, limit]) -->
### Function: quad_qag (f(x), x, a, b, key, [epsrel, epsabs, limit])

一般関数の有限の区間上の積分。
`quad_qag`は、Aind(Piessens, 1973)の戦略を使った
簡単な大域的適応積分器を実装しています。
呼び出し側は、ルール評価コンポーネントのための
ガウスークロンロッドの求積公式の6つのペアの中から選ぶことができます。
強く振動する非積分関数には高次のルールが適切です。


quad_qagは積分
$integrate (f(x), x, a, b)$

$$
\int_a^b {f(x) \, dx}
$$

を計算します。


非積分関数は依存変数*x*の*f(x)*であり、
関数は下限*a*上限*b*の間で積分されます。
*key*は利用される積分器で、1から6までのいずれかの整数でなければなりません。
*key*の値は、ガウスークロンロッドの積分ルールの次数を選びます。
高次のルールが、強く振動する非積分関数には適切です。


非積分関数は、MaximaもしくはLisp関数もしくは演算子の名前もしくMaximaのラムダ式か、
一般的なMaximaの式として指定されます。


数値積分は、望まれる精度が達成されるまで、
積分領域を部分区間に分割することによって適応的に実行されます。


キーワード引数はオプションで、どの次数においても指定できます。
それらは形式`key=val`を取ります。キーワード引数は：



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。limitは使用する部分区間の最大数。デフォルトは200。


`quad_qag`は４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード（戻り値の４番目の要素）は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**6** — 入力が無効な場合;




例:



```maxima
(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3, 'epsrel=5d-8);
(%o1)    [.4444444444492108, 3.1700968502883E-9, 961, 0]


(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

<!-- category: Calculus -->
<!-- keywords: quad_qagi -->
<!-- signatures: quad_qagi(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qagi(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qagi (f(x), x, a, b, [epsrel, epsabs, limit])

一般関数の無限のもしくは半無限の区間上の積分。
区間は、有限の区間上に写像され、`quad_qags`の中で使われるのと同じ戦略が適用されます。


`quad_qagi`は、Quadpack QAGIルーチンを使って以下の積分の１つを評価します。


$integrate (f(x), x, a, inf)$

$$
\int_a^\infty {f(x) \, dx}
$$



$integrate (f(x), x, minf, a)$

$$
\int_\infty^a {f(x) \, dx}
$$



$integrate (f(x), x, minf, inf)$

$$
\int_{-\infty}^\infty {f(x) \, dx}
$$



被積分関数は、*f(x)*であり、
従属変数*x*を使って、
関数は無限範囲上で積分されます。


被積分関数は、MaximaまたはLispの関数または演算子の名前、
Maximaのラムダ式またはMaximaの一般式として指定されるかもしれません。


積分の境界の１つは、無限でなければいけません。
もしそうでなければ、
`quad_qagi`はただ名詞形を返します。


キーワード引数は随意で、任意の順序で指定できます。
それらすべては形式`key=val`を取ります。
キーワード引数は:



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。limitは使用する部分区間の最大数。デフォルトは200。


`quad_qagi`は、４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード(戻り値の４番目の要素)は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;




例:



```maxima
(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf, 'epsrel=1d-8);
(%o1)        [0.03125, 2.95916102995002E-11, 105, 0]


(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

<!-- category: Calculus -->
<!-- keywords: quad_qags -->
<!-- signatures: quad_qags(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qags(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qags (f(x), x, a, b, [epsrel, epsabs, limit])

一般関数の有限の区間上の積分。
`quad_qags`は、イプシロンアルゴリズム(Wynn, 1956)による外挿(de Doncker,1978)を
使った大域的適応積分器を実装しています。


`quad_qags`は、積分


$integrate (f(x), x, a, b)$

$$
\int_a^b {f(x) \, dx}
$$

を計算します。


非積分関数は依存変数*x*の*f(x)*であり、
関数は下限*a*上限*b*の間で積分されます。


非積分関数は、MaximaもしくはLisp関数もしくは演算子の名前もしくMaximaのラムダ式か、一般的なMaximaの式として指定されます。


キーワード引数はオプションで、どの次数においても指定できます。
それらは形式`key=val`を取ります。キーワード引数は：



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。limitは使用する部分区間の最大数。デフォルトは200。


`quad_qags`は４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード（戻り値の４番目の要素）は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;




例:



```maxima
(%i1) quad_qags (x^(1/2)*log(1/x), x, 0, 1, 'epsrel=1d-10);
(%o1)   [.4444444444444448, 1.11022302462516E-15, 315, 0]
```


この積分に関しては、`quad_qags`は、`quad_qag`よりも精確で
効率的であることに注意してください。

<!-- category: Calculus -->
<!-- keywords: quad_qawc -->
<!-- signatures: quad_qawc(f(x), x, c, a, b, [epsrel, epsabs, limit]), quad_qawc(f, x, c, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qawc (f(x), x, c, a, b, [epsrel, epsabs, limit])

$f(x)/(x - c)$のコーシーの主値を
有限の区間$(a, b)$上で指定された$c$を用いて
計算します。
戦略は、大域的適応的で、
点$x = c$を含む部分範囲上で変形Clenshaw-Curtis積分が使われます。


`quad_qawc`は、
Quadpack QAWCルーチンを使って、
$integrate (f(x)/(x - c), x, a, b)$

$$
\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}
$$



のコーシーの主値を計算します。


被積分関数は、
`f(x)/(x - c)`で、
従属変数*x*を使って、
関数は*a*から*b*までの区間上で積分されます。


被積分関数は、MaximaまたはLispの関数または演算子の名前、
Maximaのラムダ式またはMaximaの一般式として指定されるかもしれません。


キーワード引数は随意で、任意の順序で指定できます。
それらすべては形式`key=val`を取ります。
キーワード引数は:



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。limitは使用する部分区間の最大数。デフォルトは200。


`quad_qagc`は、４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード(戻り値の４番目の要素)は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;


例:



```maxima
(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5,
                 'epsrel=1d-7);
(%o1)    [- 3.130120337415925, 1.306830140249558E-8, 495, 0]


(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1),
      x, 0, 5);
Principal Value
                       alpha
        alpha       9 4                 9
       4      log(------------- + -------------)
                      alpha           alpha
                  64 4      + 4   64 4      + 4
(%o2) (-----------------------------------------
                        alpha
                     2 4      + 2

       3 alpha                       3 alpha
       -------                       -------
          2            alpha/2          2          alpha/2
    2 4        atan(4 4       )   2 4        atan(4       )   alpha
  - --------------------------- - -------------------------)/2
              alpha                        alpha
           2 4      + 2                 2 4      + 2


(%i3) ev (%, alpha=5, numer);
(%o3)                    - 3.130120337415917
```

<!-- category: Calculus -->
<!-- keywords: quad_qawf -->
<!-- signatures: quad_qawf(f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst]), quad_qawf(f, x, a, omega, trig, [epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawf (f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst])

フーリエコサイン変換またはフーリエサイン変換を、
Quadpack QAWF関数を使って、半無限区間上で計算します。
`quad_qawo`で使われるのと同じアプローチが、連続する区間に適用され、
イプシロンアルゴリズム(Wynn, 1956)を使った収束の促進が積分寄与の級数に適用されます。


`quad_qawf`は積分
$integrate (f(x)*w(x), x, a, inf)$

$$
\int_a^\infty f(x) \, w(x) \, dx
$$

を計算します。


重み関数$w$は*trig*によって選択されます:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$


被積分関数は、MaximaまたはLispの関数または演算子の名前、
Maximaのラムダ式またはMaximaの一般式として指定されるかもしれません。


キーワード引数は随意で、任意の順序で指定できます。
それらすべては形式`key=val`を取ります。
キーワード引数は:



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。(*limit* - *limlst*)/2は使用する部分区間の最大数。デフォルトは200。
**maxp1** — チェビシェフ積率の最大数。
0より大きくなければいけません。
デフォルトは100です。
**limlst** — サイクル数に関する上限。
3以上でなければいけません。
デフォルトは10です。


`quad_qawf`は、４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード(戻り値の４番目の要素)は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;


例:



```maxima
(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos, 'epsabs=1d-9);
(%o1)   [.6901942235215714, 2.84846300257552E-11, 215, 0]


(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2


(%i3) ev (%, numer);
(%o3)                   .6901942235215714
```

<!-- category: Calculus -->
<!-- keywords: quad_qawo -->
<!-- signatures: quad_qawo(f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]), quad_qawo(f, x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawo (f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst])

$cos(omega x) f(x)$

$$
\cos\left(\omega \, x\right) \, f\left(x\right)
$$

や
$sin(omega x) f(x)$

$$
\sin\left(\omega \, x\right) \, f\left(x\right)
$$

の有限の区間上の積分。
ここで、
$omega$

$$
\omega
$$

は定数です。
規則評価構成要素は、変形Clenshaw-Curtis手法に基づいています。
`quad_qawo`は、
`quad_qags`に似て、外挿とともに適応再分割を適用します。


`quad_qawo`は、
Quadpack QAWOルーチンを使って
積分を計算します:


$integrate (f(x)*w(x), x, a, b)$

$$
\int_a^b f(x) \, w(x) \, dx
$$



重み関数$w$は、*trig*によって選択されます:



**cos** — $w(x) = cos (omega x)$ $$
w\left(x\right) = \cos \left(\omega \, x\right)
$$
**sin** — $w(x) = sin (omega x)$ $$
w\left(x\right) = \sin \left(\omega \, x\right)
$$


被積分関数は、MaximaまたはLispの関数または演算子の名前、
Maximaのラムダ式またはMaximaの一般式として指定されるかもしれません。


キーワード引数は随意で、任意の順序で指定できます。
それらすべては形式`key=val`を取ります。
キーワード引数は:



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。*limit*/2は使用する部分区間の最大数。デフォルトは200。
**maxp1** — チェビシェフ積率の最大数。
0より大きくなければいけません。
デフォルトは100です。
**limlst** — サイクル数に関する上限。
3以上でなければいけません。
デフォルトは10です。


`quad_qawo`は、４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード(戻り値の４番目の要素)は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;


例:



```maxima
(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1)     [1.376043389877692, 4.72710759424899E-11, 765, 0]


(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x),
      x, 0, inf));
                   alpha/2 - 1/2            2 alpha
        sqrt(%pi) 2              sqrt(sqrt(2        + 1) + 1)
(%o2)   -----------------------------------------------------
                               2 alpha
                         sqrt(2        + 1)


(%i3) ev (%, alpha=2, numer);
(%o3)                     1.376043390090716
```

<!-- category: Calculus -->
<!-- keywords: quad_qaws -->
<!-- signatures: quad_qaws(f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]), quad_qaws(f, x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]) -->
### Function: quad_qaws (f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit])

$w(x) f(x)$の有限の区間上の積分。
ここで、$w(x)$は、ある代数的または対数関数です。
大域的適応最分割戦略が適用されます。
積分の区間の端点を含む部分区間上で変形Clenshaw-Curtis積分を使います。


`quad_qaws`は、 
Quadpack QAWSルーチンを使って
積分を計算します:


$integrate (f(x)*w(x), x, a, b)$

$$
\int_a^b f(x) \, w(x) \, dx
$$



重み関数$w$は*wfun*によって選択されます:



**1** — $w(x) = (x - a)^alpha (b - x)^beta$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta
$$
**2** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, \log\left(x - a\right)
$$
**3** — $w(x) = (x - a)^alpha (b - x)^beta log(b - x)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, \log\left(b - x\right)
$$
**4** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a) log(b - x)$ $$
w\left(x\right) = \left(x - a\right)^\alpha \, \left(b - x\right)^\beta \, \log\left(x - a\right) \, \log\left(b - x\right)
$$


被積分関数は、MaximaまたはLispの関数または演算子の名前、
Maximaのラムダ式またはMaximaの一般式として指定されるかもしれません。


キーワード引数は随意で、任意の順序で指定できます。
それらすべては形式`key=val`を取ります。
キーワード引数は:



**epsrel** — 望まれる近似の相対誤差。デフォルトは1d-8。
**epsabs** — 望まれる近似の絶対誤差。デフォルトは0。
**limit** — 内部の作業配列のサイズ。*limit*は使用する部分区間の最大数。デフォルトは200。


`quad_qaws`は、４つの要素のリストを返します:



- *
積分の近似
- *
見積もられた近似の絶対誤差
- *
非積分関数の評価数
- *
エラーコード


エラーコード(戻り値の４番目の要素)は以下の値を取ります:



**0** — 問題が発生しなかった場合;
**1** — 部分区間の数が上限を超えた場合;
**2** — 丸め誤差が超過した場合;
**3** — 非積分関数の振る舞いが極端に悪い場合;
**4** — 収束に失敗した場合;
**5** — 積分が発散しているか収束が遅い場合;
**6** — 入力が無効な場合;


例:



```maxima
(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1,
                 'epsabs=1d-9);
(%o1)     [8.750097361672832, 1.24321522715422E-10, 170, 0]


(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
       alpha
Is  4 2      - 1  positive, negative, or zero?

pos;
                          alpha         alpha
                   2 %pi 2      sqrt(2 2      + 1)
(%o2)              -------------------------------
                               alpha
                            4 2      + 2


(%i3) ev (%, alpha=4, numer);
(%o3)                     8.750097361672829
```

<!-- category: Calculus -->
<!-- keywords: residue -->
<!-- signatures: residue(expr, z, z_0) -->
### Function: residue (expr, z, z_0)

変数*z*が値*z_0*を仮定する時、
式*expr*の複素平面での留数を計算します。
留数は、
*expr*のローラン級数における
`(z - z_0)^(-1)`の係数です。



```maxima
(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2


(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

<!-- category: Calculus -->
<!-- keywords: risch -->
<!-- signatures: risch(expr, x) -->
### Function: risch (expr, x)

リッシュアルゴリズムの超越な場合を使って、
*expr*を
*x*に関して積分します。
（リッシュアルゴリズムの代数的な場合は実装されていません。）
これは、現在、`integrate`の主要部ができない入れ子の指数関数や対数関数の場合を扱います。
`integrate`は、これらの場合が与えられたなら、自動的に`risch`を適用します。


`erfflag`がもし`false`なら、
もしまず第一に被積分関数になにもないなら、
`risch`が
答えの中に`erf`関数を導入することを妨げます。



```maxima
(%i1) risch (x^2*erf(x), x);
                                                        2
             3                      2                - x
        %pi x  erf(x) + (sqrt(%pi) x  + sqrt(%pi)) %e
(%o1)   -------------------------------------------------
                              3 %pi


(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

<!-- category: Calculus -->
<!-- keywords: tldefint -->
<!-- signatures: tldefint(expr, x, a, b) -->
### Function: tldefint (expr, x, a, b)

`tlimswitch`が`true`に設定されている`ldefint`と同値です。

