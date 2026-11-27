## Mathematical Functions

<!-- category: Combinatorics -->
<!-- keywords: !! -->
<!-- signatures: !! -->
### Function: !!

二重階乗演算子。


整数や浮動小数点、有理数 `n`に対して、 `n!!`は、
積 `n (n-2) (n-4) (n-6) ... (n - 2 (k - 1))`
（`k`は `entier (n/2)`、すなわち `n/2`以下の最大整数に等しい）に評価します。
この定義は、非整数の引数に対して他の出版物の定義と一致しないことに注意してください。



偶数(もしくは奇数) `n`に対して、 `n!!`は、2(もしくは1)からnまでのすべての偶数
(もしくは奇数)の積に評価されます。


整数でも浮動小数点でも有理数でもない引数 `n`に対して、
`n!!`は名詞形 `genfact (n, n/2, 2)`を返します。

<!-- category: Combinatorics -->
<!-- keywords: binomial -->
<!-- signatures: binomial(x, y) -->
### Function: binomial (x, y)

二項係数`x!/(y! (x - y)!)`。
もし*x*と*y*が整数なら、
二項係数の数値が計算されます。
もし*y*もしくは*x - y*が整数なら、
二項係数は多項式として表現されます。


例:










```maxima
(%i1) binomial (11, 7);
(%o1)                          330
(%i2) 11! / 7! / (11 - 7)!;
(%o2)                          330
(%i3) binomial (x, 7);
        (x - 6) (x - 5) (x - 4) (x - 3) (x - 2) (x - 1) x
(%o3)   -------------------------------------------------
                              5040
(%i4) binomial (x + 7, x);
      (x + 1) (x + 2) (x + 3) (x + 4) (x + 5) (x + 6) (x + 7)
(%o4) -------------------------------------------------------
                               5040
(%i5) binomial (11, y);
(%o5)                    binomial(11, y)
```

<!-- category: Combinatorics -->
<!-- keywords: factcomb -->
<!-- signatures: factcomb(expr) -->
### Function: factcomb (expr)

例えば、`(n + 1)*n!`を`(n + 1)!`に変換することによって、
*expr*の中の階乗の係数を階乗それ自身と結合しようとします。


もし`sumsplitfact`が`false`に設定されたなら、
`minfactorial`が`factcomb`の後適用されるようになります。

<!-- category: Combinatorics -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

デフォルト値: -1


`factlim`は、自動的に展開される最高の階乗を指定します。
もし-1なら、すべての整数は展開されます。

<!-- category: Combinatorics -->
<!-- keywords: factorial, ! -->
<!-- signatures: ! -->
### Function: factorial

階乗演算子。


（整数、有理数、実数を含む）負の整数を除いた任意の複素数 `x`に対して、
`x!`は `gamma(x+1)`として定義されます。


整数 `x`に対して、 `x!`は1からxまでの整数の積に整理されます。
`0!`は1に整理されます。
浮動小数点または多倍長浮動小数点精度の実数または複素数 `x`に対して、
`x!`は `gamma(x+1)`の値に整理されます。
`x`が `n/2`（`n`は奇数）に等しい時、
（`gamma (1/2)`は`sqrt (%pi)`に等しいから）
`x!`は有理因子に`sqrt (%pi)`を掛けたものに整理されます。


変数 `factlim`, `gammalim`は整数や有理数の引数の階乗の数値評価を制御します。
関数 `minfactorial`, `factcomb`は階乗を含む式の整理を制御します。
`factlim`, `gammalim`, `minfactorial`, `factcomb`を参照してください。


関数 `gamma`, `bffac`, `cbffac`はガンマ関数の変形です。
多倍長浮動小数点精度の実数と複素数のガンマ関数を評価するために、
`gamma`は内部で `bffac`や `cbffac`をコールします。


`makegamma`は階乗や関係した関数に`gamma`を代入します。


Maximaは階乗関数の導関数や、負の整数のような特殊な値の極限を知っています。


オプション変数 `factorial_expand`は
`(n+x)!`のような式の整理を制御します。
ここで`n`は整数です。


`binomial`も参照してください。


オペランドが`factlim`より大きくないなら、整数の階乗は正確な値に整理されます。
実数と複素数の階乗は浮動小数点または多倍長浮動小数点精度に評価されます。









```maxima
(%i1) factlim : 10;
(%o1)                          10
(%i2) [0!, (7/2)!, 8!, 20!];

                            105 sqrt(%pi)
(%o2)                   [1, -------------, 40320, 20!]
                                 16

(%i3) [4.77!, (1.0+%i)!];
(%o3)    [81.44668037931197, 
          .3430658398165454 %i + .6529654964201665]
(%i4) [2.86b0!, (1.0b0+%i)!];
(%o4) [5.046635586910012b0, 
       3.430658398165454b-1 %i + 6.529654964201667b-1]
```


既知の定数や一般式の階乗は整理されません。
オペランドを評価した後階乗を整理できたとしても整理はされません。







```maxima
(%i1) [(%i + 1)!, %pi!, %e!, (cos(1) + sin(1))!];
(%o1)      [(%i + 1)!, %pi!, %e!, (sin(1) + cos(1))!]
(%i2) ev (%, numer, %enumer);
(%o2) [.3430658398165454 %i + .6529654964201665, 
       7.188082728976031, 
       4.260820476357003, 1.227580202486819]
```










```maxima
(%i1) kill (foo);
(%o1)                         done
(%i2) foo!;
(%o2)                         foo!
```


階乗の計算は整理であって、評価ではありません。
従って、`x!`はクォートされた式の中でも置き換えられます。






```maxima
(%i1) '([0!, (7/2)!, 4.77!, 8!, 20!]);
          105 sqrt(%pi)
(%o1) [1, -------------, 81.44668037931199, 40320, 
               16
                                             2432902008176640000]
```


Maximaは階乗関数の導関数を知っています。






```maxima
(%i1) diff(x!,x);
(%o1)                           x! psi (x + 1)
                                      0
```


オプション変数`factorial_expand`は、
階乗関数を含む式の展開と整理を制御します。






```maxima
(%i1) (n+1)!/n!,factorial_expand:true;
(%o1)                                n + 1
```

See also: `factlim`, `gammalim`, `minfactorial`, `factcomb`, `gamma`, `bffac`, `cbffac`, `makegamma`, `factorial_expand`.

<!-- category: Combinatorics -->
<!-- keywords: factorial_expand -->
<!-- signatures: factorial_expand -->
### Variable: factorial_expand

デフォルト値: false


オプション変数`factorial_expand`は
`(n+1)!`のような式の整理を制御します。
ここで`n`は整数です。
例は`!`を参照してください。

<!-- category: Combinatorics -->
<!-- keywords: genfact -->
<!-- signatures: genfact(x, y, z) -->
### Function: genfact (x, y, z)

一般化された階乗を返します。
`x (x-z) (x - 2 z) ... (x - (y - 1) z)`のように定義されます。
それゆえに、整数*x*に関して、
`genfact (x, x, 1) = x!`であり、`genfact (x, x/2, 2) = x!!`です。

<!-- category: Combinatorics -->
<!-- keywords: minfactorial -->
<!-- signatures: minfactorial(expr) -->
### Function: minfactorial (expr)

整数だけ違う２つの階乗の出現に関して
*expr*を検査します。
そして、`minfactorial`は、
一方を多項式掛ける他方に変えます。









```maxima
(%i1) n!/(n+2)!;
                               n!
(%o1)                       --------
                            (n + 2)!
(%i2) minfactorial (%);
                                1
(%o2)                    ---------------
                         (n + 1) (n + 2)
```

<!-- category: Combinatorics -->
<!-- keywords: sumsplitfact -->
<!-- signatures: sumsplitfact -->
### Variable: sumsplitfact

デフォルト値: `true`


`sumsplitfact`が`false`の時、

`minfactorial`は、`factcomb`の後に適用されます。

