## Numerical

<!-- category: Series -->
<!-- keywords: absint -->
<!-- signatures: absint(f, x, halfplane), absint(f, x), absint(f, x, a, b) -->
### Function: absint (f, x, halfplane)

`absint (f, x, halfplane)`は、
与えられた半平面(`pos`, `neg`, または`both`)での
*f*の*x*に関する不定積分を返します。
*f*は、形式
`abs (x)`, `abs (sin (x))`, `abs (a) * exp (-abs (b) * abs (x))`
の式を含むことができます。


`absint (f, x)`は`absint (f, x, pos)`と同値です。


`absint (f, x, a, b)`は、
*f*の
*x*に関する
*a*から*b*までの定積分
を返します。



*f*は、絶対値を含むことができます。

<!-- category: Series -->
<!-- keywords: cosnpiflag -->
<!-- signatures: cosnpiflag -->
### Variable: cosnpiflag

デフォルト値: `true`


`foursimp`を参照してください。

<!-- category: Series -->
<!-- keywords: equalp -->
<!-- signatures: equalp(x, y) -->
### Function: equalp (x, y)

もし`equal (x, y)`なら、`true`を返し、
そうでないなら、`false`を返します。
 (この場合、`equal (x, y)`がするようなエラーメッセージを与えません。)

<!-- category: Series -->
<!-- keywords: fft -->
<!-- signatures: fft(x) -->
### Function: fft (x)

複素高速Fourier変換を計算します。
*x*は、変換されるデータを含むリストもしくは配列です。
要素の数は2のべき乗でなければいけません。
要素は、数リテラル（整数、有理数、浮動小数点、多倍長浮動小数点）、シンボル定数、
もしくは、`a`と`b`が数リテラルもしくはシンボル定数である式`a + b*%i`
でなければいけません。


`fft`は、*x*と同じタイプの新しいオブジェクトを返します。
*x*は変更されません。
結果はいつも浮動小数点、もしくは`a`と`b`が浮動小数点であるところの式
`a + b*%i`として計算されます。


離散Fourier変換は、以下のように定義されます。
`y`を変換の出力とします。
`k`が0から`n - 1`まで変わる中、



```maxima
y[k] = (1/n) sum(x[j] exp(-2 %i %pi j k / n), j, 0, n - 1)
```


データ*x*が実数の時、
実係数`a`と`b`は以下のように計算することができます。


```maxima
x[j] = sum(a[k]*cos(2*%pi*j*k/n)+b[k]*sin(2*%pi*j*k/n), k, 0, n/2)
```


ここで、



```maxima
a[0] = realpart (y[0])
b[0] = 0
```


そして、`k`が1からn/2 - 1まで変わる中、



```maxima
a[k] = realpart (y[k] + y[n - k])
b[k] = imagpart (y[n - k] - y[k])
```


そして、



```maxima
a[n/2] = realpart (y[n/2])
b[n/2] = 0
```


`load("fft")`はこの関数をロードします。


`inverse_fft` (逆変換), `recttopolar`, `polartorect`も参照してください。


例:


実数データ。











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : fft (L);
(%o4) [0.0, - 1.811 %i - .1036, 0.0, .6036 - .3107 %i, 0.0, 
                         .3107 %i + .6036, 0.0, 1.811 %i - .1036]
(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 2.168L-19 %i + 2.0, 7.525L-20 %i + 3.0, 
4.256L-19 %i + 4.0, - 1.0, - 2.168L-19 %i - 2.0, 
- 7.525L-20 %i - 3.0, - 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```


複素数データ











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : fft (L);
(%o4) [0.5, .3536 %i + .3536, - 0.25 %i - 0.25, 
0.5 - 6.776L-21 %i, 0.0, - .3536 %i - .3536, 0.25 %i - 0.25, 
0.5 - 3.388L-20 %i]
(%i5) L2 : inverse_fft (L1);
(%o5) [1.0 - 4.066E-20 %i, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
- 1.008L-19 %i - 1.0, 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.947L-20 %i + 1.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       6.83L-17
```


サインとコサイン係数の計算。

























```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, 5, 6, 7, 8] $
(%i4) n : length (L) $
(%i5) x : make_array (any, n) $
(%i6) fillarray (x, L) $
(%i7) y : fft (x) $
(%i8) a : make_array (any, n/2 + 1) $
(%i9) b : make_array (any, n/2 + 1) $
(%i10) a[0] : realpart (y[0]) $
(%i11) b[0] : 0 $
(%i12) for k : 1 thru n/2 - 1 do
   (a[k] : realpart (y[k] + y[n - k]),
    b[k] : imagpart (y[n - k] - y[k]));
(%o12)                        done
(%i13) a[n/2] : y[n/2] $
(%i14) b[n/2] : 0 $
(%i15) listarray (a);
(%o15)          [4.5, - 1.0, - 1.0, - 1.0, - 0.5]
(%i16) listarray (b);
(%o16)           [0, - 2.414, - 1.0, - .4142, 0]
(%i17) f(j) := sum (a[k]*cos(2*%pi*j*k/n) + b[k]*sin(2*%pi*j*k/n), 
                    k, 0, n/2) $
(%i18) makelist (float (f (j)), j, 0, n - 1);
(%o18)      [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
```

<!-- category: Series -->
<!-- keywords: find_root, bf_find_root, find_root_error, find_root_abs, find_root_rel -->
<!-- signatures: find_root(expr, x, a, b, [abserr, relerr]), find_root(f, a, b, [abserr, relerr]), bf_find_root(expr, x, a, b, [abserr, relerr]), bf_find_root(f, a, b, [abserr, relerr]), find_root_error, find_root_abs, find_root_rel -->
### Function: find_root (expr, x, a, b, [abserr, relerr])

式*expr*もしくは関数*f*の根を、閉区間$[a, b]$上で見つけます。
式*expr*は等式でも問題ありません。
その場合、`find_root`は`lhs(expr) - rhs(expr)`の根を探します。


Maximaは*expr*もしくは*f*を$[a, b]$上で評価可能であり、
*expr*もしくは*f*は連続と仮定して、`find_root`は根もしくは、
もし複数の根があるなら、根の１つを見つけることを保証します。


`find_root`は初め、２分木探索を適用します。
もし対象の関数が十分滑らかなら，`find_root`は代わりに線形内挿を適用します。


`f_find_root`は`find_root`の多倍長浮動小数点版です。
関数は多倍長浮動小数点数値を使って計算され、多倍長浮動小数点の結果が返されます。
そうでなければ、`bf_find_root`は`find_root`と同一で、以下の記述は`bf_find_root`に同様に適用されます。


`find_root`の精度は`abserr`と`relerr`に支配されます。
それらは`fine_root`へのオプションのキーワード引数です。
これらのキーワード引数は形式`key=val`を取ります。
キーワード引数は


**abserr** — 根での関数値の望まれる絶対エラー。デフォルトは、`find_root_abs`です。
**relerr** — 根の望まれる相対エラー。デフォルトは`find_root_rel`です。


懸案の関数が`abserr`以下の何かに評価される時、または、
近似値*x_0*, *x_1*の差が`relerr * max(abs(x_0), abs(x_1))`以下になるなら、`find_root`は停止します。


`find_root_abs`と`find_root_rel`のデフォルト値はともに零です。


`find_root`は、探索区間の端で対象の関数が異なる符号を持つことを期待します。
関数が両方の終端での数に評価されて、それらの数が同じ符号を持つ時、
`find_root`の振る舞いは、`find_root_error`に支配されます。
`find_root_error`が`true`の時、
`find_root`はエラーメッセージを出力します。
そうでなければ、`find_root`は`find_root_error`の値を返します。
`find_root_error`のデフォルト値は`true`です。


もし*f*が探索アルゴリズムの中の任意のステップで、数以外の何かに評価するなら、
`find_root`は、部分的に評価された`find_root`式を返します。
*a*と*b*の順序は無視されます;
根が探索される区間は$[min(a, b), max(a, b)]$です。


例:
























```maxima
(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2
(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981
(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981
(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981
(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981
(%i6) find_root (exp(x) = y, x, 0, 100);
                            x
(%o6)           find_root(%e  = y, x, 0.0, 100.0)
(%i7) find_root (exp(x) = y, x, 0, 100), y = 10;
(%o7)                   2.302585092994046
(%i8) log (10.0);
(%o8)                   2.302585092994046
(%i9) fpprec:32;
(%o9)                           32
(%i10) bf_find_root (exp(x) = y, x, 0, 100), y = 10;
(%o10)                  2.3025850929940456840179914546844b0
(%i11) log(10b0);
(%o11)                  2.3025850929940456840179914546844b0
```

<!-- category: Series -->
<!-- keywords: fortindent -->
<!-- signatures: fortindent -->
### Variable: fortindent

デフォルト値: 0


`fortindent`は、`fortran`コマンドが表示する式の
式の左マージンインデントを制御します。
0は、標準のプリントアウト(すなわち6スペース)を与え、
正の値は、式を更に右に印字するようにします。

<!-- category: Series -->
<!-- keywords: fortran -->
<!-- signatures: fortran(expr) -->
### Function: fortran (expr)

Fortran文として*expr*を印字します。
出力行は、スペースでインデントされます。
もし行が長過ぎるなら、
`fortran`は継続行を印字します。
`fortran`は、指数演算子`^`を`**`として印字し、
複素数`a + b %i`を形式`(a,b)`で印字します。


*expr*は等式も取り、もしそうなら、`fortran`は、
等式の右辺を左辺に割り当てる割り当て文を印字します。
特に、もし*expr*の右辺が行列名なら、
`fortran`は、行列の要素それぞれに対する割り当て文を印字します。


もし*expr*が`fortran`が認識する何かでないなら、
エラーなしに、式が`grind`フォーマットで印字されます。
`fortran`は、リスト、配列、関数について知りません。


`fortindent`は、`fortran`コマンドが表示する式の
式の左マージンインデントを制御します。
0は、標準のプリントアウト(すなわち6スペース)を与え、
正の値は、式を更に右に印字するようにします。


`fortspaces`が`true`の時、
`fortran`は、印字行それぞれを80カラムまでスペースで埋めます。


`fortran`は引数を評価します;
引数のクォートは評価を無効にします。
`fortran`はいつも`done`を返します。


例:



(%i1) expr: (a + b)^12$
(%i2) fortran (expr);
      (b+a)**12                                                                 
(%o2)                         done
(%i3) fortran ('x=expr);
      x = (b+a)**12                                                             
(%o3)                         done
(%i4) fortran ('x=expand (expr));
      x = b**12+12*a*b**11+66*a**2*b**10+220*a**3*b**9+495*a**4*b**8+792
     1   *a**5*b**7+924*a**6*b**6+792*a**7*b**5+495*a**8*b**4+220*a**9*b
     2   **3+66*a**10*b**2+12*a**11*b+a**12
(%o4)                         done
(%i5) fortran ('x=7+5*%i);
      x = (7,5)                                                                 
(%o5)                         done
(%i6) fortran ('x=[1,2,3,4]);
      x = [1,2,3,4]                                                             
(%o6)                         done
(%i7) f(x) := x^2$
(%i8) fortran (f);
      f                                                                         
(%o8)                         done

<!-- category: Series -->
<!-- keywords: fortspaces -->
<!-- signatures: fortspaces -->
### Variable: fortspaces

デフォルト値: `false`


`fortspaces`が`true`の時、
`fortran`は、印字行それぞれを80カラムまでスペースで埋めます。

<!-- category: Series -->
<!-- keywords: fourcos -->
<!-- signatures: fourcos(f, x, p) -->
### Function: fourcos (f, x, p)

`[0, p]`上で定義された
`f(x)`のFourierコサイン係数を返します。

<!-- category: Series -->
<!-- keywords: fourexpand -->
<!-- signatures: fourexpand(l, x, p, limit) -->
### Function: fourexpand (l, x, p, limit)

Fourier係数*l*のリストから
*limit*項までのFourier級数を構成し、返します。
(*limit*は`inf`もあり得ます。)
*x*と*p*は、`fourier`におけるものと同じ意味を持ちます。

<!-- category: Series -->
<!-- keywords: fourier -->
<!-- signatures: fourier(f, x, p) -->
### Function: fourier (f, x, p)

区間`[-p, p]`上で定義された`f(x)`のFourier係数のリストを返します。

<!-- category: Series -->
<!-- keywords: fourint -->
<!-- signatures: fourint(f, x) -->
### Function: fourint (f, x)

`[minf, inf]`上で定義された
`f(x)`のFourier積分係数のリストを構成し、返します。

<!-- category: Series -->
<!-- keywords: fourintcos -->
<!-- signatures: fourintcos(f, x) -->
### Function: fourintcos (f, x)

`[0, inf]`上の`f(x)`のFourierコサイン積分係数を返します。

<!-- category: Series -->
<!-- keywords: fourintsin -->
<!-- signatures: fourintsin(f, x) -->
### Function: fourintsin (f, x)

`[0, inf]`上の`f(x)`のFourierサイン積分係数を返します。

<!-- category: Series -->
<!-- keywords: foursimp -->
<!-- signatures: foursimp(l) -->
### Function: foursimp (l)

もし`sinnpiflag`が`true`なら、`sin (n %pi)`を0に整理します。
もし`cosnpiflag`が`true`なら、`cos (n %pi)`を`(-1)^n`に整理します。

<!-- category: Series -->
<!-- keywords: foursin -->
<!-- signatures: foursin(f, x, p) -->
### Function: foursin (f, x, p)

`[0, p]`上で定義された
`f(x)`のFourierサイン係数を返します。

<!-- category: Series -->
<!-- keywords: funp -->
<!-- signatures: funp(f, expr), funp(f, expr, x) -->
### Function: funp (f, expr)

`funp (f, expr)`は、
もし*expr*が関数*f*を含むなら
`true`を返します。


`funp (f, expr, x)`は、
もし*expr*が関数*f*を含み、変数
*x*が*f*のインスタンスの１つの引数のどこかにあるなら、
`true`を返します。

<!-- category: Series -->
<!-- keywords: horner -->
<!-- signatures: horner(expr, x), horner(expr) -->
### Function: horner (expr, x)

Horner規則に従って、もし指定されないなら*x*を主変数として使い、
*expr*の再配列された表現を返します。
`x`は、*expr*の標準有理式形の主変数が使われる場合には、省略できます。


もし`expr`が数値的に評価されるものなら、
`horner`は、時々、安定性が改善されます。
また、もしMaximaがFortranで走らせるプログラムを生成するのに使われるなら、
役に立ちます。
`stringout`も参照してください。



```maxima
(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                           2
(%o1)            1.0E-155 x  - 5.5 x + 5.2E+155
(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)            (1.0E-155 x - 5.5) x + 5.2E+155
(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 floating point overflow

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i4) ev (expr2, x=1e155);
(%o4)                       7.0E+154
```

<!-- category: Series -->
<!-- keywords: inverse_fft -->
<!-- signatures: inverse_fft(y) -->
### Function: inverse_fft (y)

複素逆高速Fourier変換を計算します。
*y*は、変換されるデータを含むリストもしくは配列です。
要素の数は2のべき乗でなければいけません。
要素は、数リテラル（整数、有理数、浮動小数点、多倍長浮動小数点）、シンボル定数、
もしくは、`a`と`b`が数リテラルもしくはシンボル定数である式`a + b*%i`
でなければいけません。


`inverse_fft`は、*y*と同じタイプの新しいオブジェクトを返します。
*y*は変更されません。
結果はいつも浮動小数点、もしくは`a`と`b`が浮動小数点であるところの式
`a + b*%i`として計算されます。


逆離散Fourier変換は、以下のように定義されます。
`x`を逆変換の出力とします。
`j`が0から`n - 1`まで変わる中、



```maxima
x[j] = sum(y[k] exp(+2 %i %pi j k / n), k, 0, n - 1)
```


`load("fft")`はこの関数をロードします。


`fft` (正変換), `recttopolar`, `polartorect`も参照してください。


例:


実数データ。











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : inverse_fft (L);
(%o4) [0.0, 14.49 %i - .8284, 0.0, 2.485 %i + 4.828, 0.0, 
                       4.828 - 2.485 %i, 0.0, - 14.49 %i - .8284]
(%i5) L2 : fft (L1);
(%o5) [1.0, 2.0 - 2.168L-19 %i, 3.0 - 7.525L-20 %i, 
4.0 - 4.256L-19 %i, - 1.0, 2.168L-19 %i - 2.0, 
7.525L-20 %i - 3.0, 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```


複素数データ











```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $                 
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : inverse_fft (L);
(%o4) [4.0, 2.711L-19 %i + 4.0, 2.0 %i - 2.0, 
- 2.828 %i - 2.828, 0.0, 5.421L-20 %i + 4.0, - 2.0 %i - 2.0, 
2.828 %i + 2.828]
(%i5) L2 : fft (L1);
(%o5) [4.066E-20 %i + 1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
1.55L-19 %i - 1.0, - 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.0 - 7.368L-20 %i]
(%i6) lmax (abs (L2 - L));                    
(%o6)                       6.841L-17
```

<!-- category: Series -->
<!-- keywords: newton -->
<!-- signatures: newton(expr, x, x_0, eps) -->
### Function: newton (expr, x, x_0, eps)

*expr*を*x*の１変数関数と考えて、
Newton法による、`expr = 0`の近似解を返します。
探索は、`x = x_0`で始まり、
(*x*の現在値で評価された*expr*を使った)`abs(expr) < eps`が成り立つまで続きます。


終了テスト`abs(expr) < eps`が`true`または`false`に評価される限り、
`newton`は、未定義変数が*expr*の中に現れることを許します。


このように、
*expr*は数に評価される必要はありません。


`load("newton1")`はこの関数をロードします。


`realroots`, `allroots`, `find_root`, `mnewton`も参照してください。


例:











```maxima
(%i1) load ("newton1");
(%o1) /usr/share/maxima/5.10.0cvs/share/numeric/newton1.mac
(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                   1.570675277161251
(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528E-4
(%i4) assume (a > 0);
(%o4)                        [a > 0]
(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                  1.00030487804878 a
(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958E-4 a
```

<!-- category: Series -->
<!-- keywords: polartorect -->
<!-- signatures: polartorect(r, t) -->
### Function: polartorect (r, t)

形式`r %e^(%i t)`の複素値を形式`a + b %i`に変換します。
ここで、*r*は大きさで、*t*は位相です。
*r*と*t*は、同じサイズの１次元配列です。
配列のサイズは2のべき乗である必要はありません。


関数が戻ると、入力配列の元の値は、実部`a`と虚部`b`に置き換えられます。
出力は、以下のように計算されます。



```maxima
a = r cos(t)
b = r sin(t)
```


`polartorect`は、`recttopolar`の逆関数です。


`load("fft")`はこの関数をロードします。
`fft`も参照してください。

<!-- category: Series -->
<!-- keywords: recttopolar -->
<!-- signatures: recttopolar(a, b) -->
### Function: recttopolar (a, b)

形式`a + b %i`の複素値を形式`r %e^(%i t)`に変換します。
ここで、*a*は実部で、*b*は虚部です。
*a*と*b*は同じサイズの１次元配列です。
配列のサイズは2のべき乗である必要はありません。


関数が戻ると、入力配列の元の値は、大きさ`r`と偏角`t`に置き換えられます。
出力は、以下のように計算されます。



```maxima
r = sqrt(a^2 + b^2)
t = atan2(b, a)
```


計算された偏角は、`-%pi`から`%pi`の範囲の中にあります。


`recttopolar`は`polartorect`の逆関数です。


`load("fft")`はこの関数をロードします。
`fft`も参照してください。

<!-- category: Series -->
<!-- keywords: remfun -->
<!-- signatures: remfun(f, expr), remfun(f, expr, x) -->
### Function: remfun (f, expr)

`remfun (f, expr)`は、
*expr*の中の`f (arg)`すべてを*arg*で置き換えます。


`remfun (f, expr, x)`は、
*expr*の中の`f (arg)`を
*arg*が変数*x*を含むときだけ
*arg*で置き換えます。

<!-- category: Series -->
<!-- keywords: sinnpiflag -->
<!-- signatures: sinnpiflag -->
### Variable: sinnpiflag

デフォルト値: `true`


`foursimp`を参照してください。

<!-- category: Series -->
<!-- keywords: totalfourier -->
<!-- signatures: totalfourier(f, x, p) -->
### Function: totalfourier (f, x, p)

`fourexpand (foursimp (fourier (f, x, p)), x, p, 'inf)`を返します。

