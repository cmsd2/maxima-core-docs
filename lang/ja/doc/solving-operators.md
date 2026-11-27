## Operators

<!-- category: Solving -->
<!-- keywords: # -->
<!-- signatures: # -->
### Function: #

構文的等号`=`の否定を表します。


述語論理式の評価のルールのため
（特に `not expr`は *expr*の評価を伴うので）、
`not a = b`は、 `a # b`ではなく、
`is(a # b)`と同値です。


例:











```maxima
(%i1) a = b;
(%o1)                         a = b
(%i2) is (a = b);
(%o2)                         false
(%i3) a # b;
(%o3)                         a # b
(%i4) not a = b;
(%o4)                         true
(%i5) is (a # b);
(%o5)                         true
(%i6) is (not a = b);
(%o6)                         true
```

<!-- category: Solving -->
<!-- keywords: = -->
<!-- signatures: = -->
### Function: =

等式演算子。


式`a = b`は、それ自身、未評価の等式を表します。
等式は成り立つかもしれませんし、成り立たないかもしれません。
未評価の等式は、`solve`や`algsys`や他の関数の引数として用いられます。


関数`is`は、`=`をブーリアン値に評価します。
`is(a = b)`は、*a*と*b*が同一のとき、
`a = b`を`true`に評価します。
すなわち、*a*と*b*が同一のアトムであるか、もしくは、それらはアトムではなく、
それらの演算子が同一で、演算子の引数が同一です。
そうでなければ、`is(a = b)`は`false`に評価されます;
決して、`unknown`には評価されません。
`is(a = b)`が`true`の時、
*a*と*b*は、同値の式と対照的に、構文法的に等しいと言われます。
同値の式は、`is(equal(a, b))`が`true`の式です。
式は、同値だが構文法的に等しくないことが起こりえます。


`=`の否定は、`#`で表されます。
`=`と同様、式`a # b`は、それ自身、評価されません。
`is(a # b)`は、`a # b`を`true`もしくは`false`に評価します。


`is`に加えて、他のいくつかの演算子が`=`と`#`を`true`もしくは`false`に評価します。`if`, `and`, `or`, `not`という演算子です。


述語論理式の評価規則のため
（特に、`not expr`は*expr*の評価を起こすため）、
`not a = b`は、`a # b`ではなく、
`is(a # b)`と同値になります。


`rhs`と`lhs`は、それぞれ、等式、不等式の右辺と左辺を返します。


`equal`や`notequal`も参照してください。


例:


式`a = b`は、それ自身、未評価の等式であり、成り立つことも成り立たないこともあります。










```maxima
(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17
(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29
(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a
(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a
(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)`は、
*a*と*b*が構文法的に等しい（すなわち、同一の）時
式は、同値だが構文法的に等しくないことがありえます。









```maxima
(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)
(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1
(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]
(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


いくつかの演算子は、`=`と`#`を`true`もしくは`false`に評価します。










```maxima
(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2 then FOO else
      BAR;
(%o1)                          FOO
(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x
(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e
(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


`not expr`は*expr*の評価をするので、
`not a = b`は、`is(a # b)`と同値です。







```maxima
(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]
(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

See also: `solve`, `algsys`, `is`, `#`, `if`, `and`, `or`, `not`, `rhs`, `lhs`, `equal`, `notequal`.

