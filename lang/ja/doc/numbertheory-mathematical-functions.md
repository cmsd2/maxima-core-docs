## Mathematical Functions

<!-- category: NumberTheory -->
<!-- keywords: abs -->
<!-- signatures: abs(expr) -->
### Function: abs (expr)

*expr*の絶対値を返します。もし*expr*が複素数なら、*expr*の絶対値(modulus)を返します。


`abs`はリスト上、行列上、等式上に分配されます。
`distribute_over`を参照してください。

See also: `distribute_over`.

<!-- category: NumberTheory -->
<!-- keywords: cabs -->
<!-- signatures: cabs(expr) -->
### Function: cabs (expr)

*expr*の複素数の絶対値を返します。

<!-- category: NumberTheory -->
<!-- keywords: carg -->
<!-- signatures: carg(z) -->
### Function: carg (z)

*z*の複素偏角を返します。
複素偏角は、
`r exp (theta %i) = z`（`r`は*z*の絶対値）を満たす
`(-%pi, %pi]`の間の角`theta`です。


`carg`は、計算関数であって、式整理関数ではありません。



`abs` (複素絶対値), `polarform`, `rectform`,
`realpart`, `imagpart`も参照してください。


例:











```maxima
(%i1) carg (1);
(%o1)                           0
(%i2) carg (1 + %i);
                               %pi
(%o2)                          ---
                                4
(%i3) carg (exp (%i));
(%o3)                           1
(%i4) carg (exp (%pi * %i));
(%o4)                          %pi
(%i5) carg (exp (3/2 * %pi * %i));
                                %pi
(%o5)                         - ---
                                 2
(%i6) carg (17 * exp (2 * %i));
(%o6)                           2
```

<!-- category: NumberTheory -->
<!-- keywords: ceiling -->
<!-- signatures: ceiling(x) -->
### Function: ceiling (x)

*x*が実数の時、*x*以上の最小の整数を返します。


もし*x*が定数式(例えば`10 * %pi`)なら、
`ceiling`は、*x*を多倍長浮動小数点数を使って評価し、
その多倍長浮動小数点数に`ceiling`を適用します。
`ceiling`は浮動小数点を使うので、ほとんど起こりえませんが、
`ceiling`は定数入力に対して間違った値を返す可能性があります。
このエラーを起こさないようにするには、`fpprec`の３つの値を使って浮動小数点評価を行います。


定数でない入力に関しては、`ceiling`は整理された値を返そうとします。
以下は、`ceiling`が知っている式整理の例です:












```maxima
(%i1) ceiling (ceiling (x));
(%o1)                      ceiling(x)
(%i2) ceiling (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [ceiling (n), ceiling (abs (n)), ceiling (max (n, 6))];
(%o4)                [n, abs(n), max(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) ceiling (x);
(%o6)                           1
(%i7) tex (ceiling (a));
$$\left \lceil a \right \rceil$$
(%o7)                         false
```


関数`ceiling`は、自動ではリストや行列上にマップしません。
最終的に、明らかに複雑な入力すべてに対して、`ceiling`は名詞形を返します。


もし関数の範囲が整数の部分集合なら、
`integervalued`に宣言できます。
`ceiling`、`floor`関数両方とも、この情報を使います; 例えば:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

<!-- category: NumberTheory -->
<!-- keywords: conjugate -->
<!-- signatures: conjugate(x) -->
### Function: conjugate (x)

*x*の複素共役を返します。










```maxima
(%i1) declare ([aa, bb], real, cc, complex, ii, imaginary);

(%o1)                         done
(%i2) conjugate (aa + bb*%i);

(%o2)                      aa - %i bb
(%i3) conjugate (cc);

(%o3)                     conjugate(cc)
(%i4) conjugate (ii);

(%o4)                         - ii
(%i5) conjugate (xx + yy);

(%o5)             conjugate(yy) + conjugate(xx)
```

<!-- category: NumberTheory -->
<!-- keywords: entier -->
<!-- signatures: entier(x) -->
### Function: entier (x)

*x*が数値の場合、*x*以下の最大の整数を返します。
（`fixnum`における）`fix`はこれの別名で、
`fix(x)`は正確に同じです。

<!-- category: NumberTheory -->
<!-- keywords: fix -->
<!-- signatures: fix(x) -->
### Function: fix (x)

`entier (x)`の別名です。

<!-- category: NumberTheory -->
<!-- keywords: floor -->
<!-- signatures: floor(x) -->
### Function: floor (x)

*x*が実数の時、*x*以下の最大の整数を返します。


もし*x*が定数式(例えば`10 * %pi`)なら、
`floor`は、多倍長浮動小数点数を使って*x*を評価し、
結果の多倍長浮動小数点に`floor`を適用します。
`floor`は浮動小数点を使うので、ほとんど起こりえませんが、
`floor`は定数入力に対して間違った値を返す可能性があります。
このエラーを起こさないようにするには、`fpprec`の３つの値を使って浮動小数点評価を行います。


定数でない入力に関しては、`floor`は整理された値を返そうとします。
以下は、`ceiling`が知っている式整理の例です:












```maxima
(%i1) floor (ceiling (x));
(%o1)                      ceiling(x)
(%i2) floor (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [floor (n), floor (abs (n)), floor (min (n, 6))];
(%o4)                [n, abs(n), min(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) floor (x);
(%o6)                           0
(%i7) tex (floor (a));
$$\left \lfloor a \right \rfloor$$
(%o7)                         false
```


関数`floor`は、自動ではリストや行列上にマップしません。
最終的に、明らかに複雑な入力すべてに対して、`floor`は名詞形を返します。


もし関数の範囲が整数の部分集合なら、
`integervalued`に宣言できます。
`ceiling`、`floor`関数両方とも、この情報を使います; 例えば:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

<!-- category: NumberTheory -->
<!-- keywords: imagpart -->
<!-- signatures: imagpart(expr) -->
### Function: imagpart (expr)

式*expr*の虚部を返します。


`imagpart`は、計算関数であり、整理関数ではありません。




`abs`, `carg`, `polarform`, `rectform`, `realpart`も
参照してください。

<!-- category: NumberTheory -->
<!-- keywords: lmax -->
<!-- signatures: lmax(L) -->
### Function: lmax (L)

*L*がリストもしくは集合の時、`apply ('max, args (L))`を返します。
*L*がリストでも集合でもない時、エラーを示します。

<!-- category: NumberTheory -->
<!-- keywords: lmin -->
<!-- signatures: lmin(L) -->
### Function: lmin (L)

*L*がリストもしくは集合の時、`apply ('min, args (L))`を返します。
*L*がリストでも集合でもない時、エラーを示します。

<!-- category: NumberTheory -->
<!-- keywords: make_random_state -->
<!-- signatures: make_random_state(n), make_random_state(s), make_random_state(true), make_random_state(false) -->
### Function: make_random_state (n)

ランダムステートオブジェクトは、乱数生成器の状態を表します。
状態は、627個の32ビットワードで構成されます。


`make_random_state (n)`は、
*n*を2^32で割った余りに等しい整数シードの値から新しいランダムステートオブジェクトを
生成します。*n*は負でもいいです。






`make_random_state (s)`は、ランダムステート*s*のコピーを返します。


`make_random_state (true)`は、新しいランダムステートオブジェクトを返します。
シードとしてコンピュータの現在時刻を使います。


`make_random_state (false)`は、乱数生成器の現在のステートのコピーを返します。

<!-- category: NumberTheory -->
<!-- keywords: max -->
<!-- signatures: max(x_1, ..., x_n) -->
### Function: max (x_1, ..., x_n)

式*x_1*から*x_n*の中の最大値に関して整理された値を返します。
`get (trylevel, maxmin)`が２以上の時、
`max`は、式整理`max (e, -e) --> |e|`を使います。
`get (trylevel, maxmin)`が３以上の時、
*max*は、２つの他の引数の間の式を消去しようとします;
例えば、`max (x, 2*x, 3*x) --> max (x, 3*x)`。
`trylevel`を2に設定するには、`put (trylevel, 2, maxmin)`を使います。

<!-- category: NumberTheory -->
<!-- keywords: min -->
<!-- signatures: min(x_1, ..., x_n) -->
### Function: min (x_1, ..., x_n)

式*x_1*から*x_n*の中の最小値に関して整理された値を返します。
`get (trylevel, maxmin)`が２以上の時、
`max`は、式整理`max (e, -e) --> |e|`を使います。
`get (trylevel, maxmin)`が３以上の時、
*max*は、２つの他の引数の間の式を消去しようとします;
例えば、`max (x, 2*x, 3*x) --> max (x, 3*x)`。
`trylevel`を2に設定するには、`put (trylevel, 2, maxmin)`を使います。


`max`や `lmin`.も参照してください。

See also: `max`, `lmin`.

<!-- category: NumberTheory -->
<!-- keywords: polarform -->
<!-- signatures: polarform(expr) -->
### Function: polarform (expr)

*expr*と同値な式`r %e^(%i theta)`を返します。
ここで、`r`と`theta`は純粋な実数です。

<!-- category: NumberTheory -->
<!-- keywords: random -->
<!-- signatures: random(x) -->
### Function: random (x)

疑似乱数を返します。
もし*x*が整数なら、`random (x)`は、0から`x - 1`までの
整数を返します。
もし*x*が浮動小数点なら、`random (x)`は、*x*より小さい非負の浮動小数点を返します。
もし*x*が整数でも浮動小数点でもなかったり、*x*が正でなければ、
`random`は、エラーを出力します。


関数`make_random_state`と`set_random_state`は、
乱数生成器の状態を保守します。


Maximaの乱数生成器は、メルセンヌ・ツイスタ MT 19937の実装です。


例:


















```maxima
(%i1) s1: make_random_state (654321)$
(%i2) set_random_state (s1);
(%o2)                         done
(%i3) random (1000);
(%o3)                          768
(%i4) random (9573684);
(%o4)                        7657880
(%i5) random (2^75);
(%o5)                11804491615036831636390
(%i6) s2: make_random_state (false)$
(%i7) random (1.0);
(%o7)                   .2310127244107132
(%i8) random (10.0);
(%o8)                   4.394553645870825
(%i9) random (100.0);
(%o9)                   32.28666704056853
(%i10) set_random_state (s2);
(%o10)                        done
(%i11) random (1.0);
(%o11)                  .2310127244107132
(%i12) random (10.0);
(%o12)                  4.394553645870825
(%i13) random (100.0);
(%o13)                  32.28666704056853
```

<!-- category: NumberTheory -->
<!-- keywords: realpart -->
<!-- signatures: realpart(expr) -->
### Function: realpart (expr)

*expr*の実部を返します。
`realpart`と`imagpart`は、
平方根、対数関数、指数関数はもちろん三角関数や双曲関数を含む式上で機能します。

<!-- category: NumberTheory -->
<!-- keywords: rectform -->
<!-- signatures: rectform(expr) -->
### Function: rectform (expr)

*expr*と同値な式`a + b %i`を返します。
ここで*a*と*b*は純粋な実数です。

<!-- category: NumberTheory -->
<!-- keywords: round -->
<!-- signatures: round(x) -->
### Function: round (x)

*x*が実数の時、*x*に最も近い整数を返します。
1/2を掛けてroundして2を掛けると、最も近い偶数に丸められます。
*x*の評価は、`floor`や`ceiling`に似ています。

<!-- category: NumberTheory -->
<!-- keywords: set_random_state -->
<!-- signatures: set_random_state(s) -->
### Function: set_random_state (s)

*s*を乱数生成器状態にコピーします。


`set_random_state`はいつも`done`を返します。

<!-- category: NumberTheory -->
<!-- keywords: signum -->
<!-- signatures: signum(x) -->
### Function: signum (x)

実数か複素数*x*に対して、もし*x*が0ならsignum関数は0を返します;
非ゼロ数値入力*x*に対して、signum関数は`abs(x)/x`を返します。


非数値入力に対して、Maximaは入力の符号を決定しようと試みます。
符号が負、ゼロ、正いずれかの時、`signum`はそれぞれ、-1, 0, 1を返します。
符号に関する他の値すべてに対して、`signum`は式整理された同値形を返します。
式整理は(`signum(-x)`は`-signum(x)`を与える)反転と
(`signum(x*y)`は`signum(x) * signum(y)`を与える)乗法恒等式を含みます。


`signum`関数はリスト、行列もしくは等式上に分配されます。
`distribute_over`を参照してください。

See also: `distribute_over`.

