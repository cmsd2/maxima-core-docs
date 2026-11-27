## ezunits

<!-- category: Units -->
<!-- keywords: ` -->
<!-- signatures: ` -->
### Function: `

次元量演算子。
式 $a ` b$は次元量を表します。
`a`は無次元量を表し、`b`は次元単位を表します。
シンボルは、宣言せずに単位として使うことができます;
単位シンボルは特別なプロパティを持つ必要はありません。
式 $a ` b$の量と単位はそれぞれ、
`qty`と `units`関数で抽出することができます。


次元量の算術演算子は演算子の慣例規則に従って実行されます。



- * 
$(x ` a) * (y ` b)$は $(x * y) ` (a * b)$に等しい。
- * 
$(x ` a) + (y ` a)$は $(x + y) ` a$に等しい。
- * 
$(x ` a)^y$は `y`が無次元の時 $x^y ` a^y$に等しい。


`ezunits`は和の中の単位が同じ次元であることを要求しません;
そんな項は一緒には足されませんし、エラーは報告されません。


`load("ezunits")`はこの演算子をイネーブルにします。


例:


SI (国際単位系) 単位。










```maxima
(%i1) load ("ezunits")$
(%i2) foo : 10 ` m;
(%o2)                        10 ` m
(%i3) qty (foo);
(%o3)                          10
(%i4) units (foo);
(%o4)                           m
(%i5) dimensions (foo);
(%o5)                        length
```


"慣習"単位。









```maxima
(%i1) load ("ezunits")$
(%i2) bar : x ` acre;
(%o2)                       x ` acre
(%i3) dimensions (bar);
                                   2
(%o3)                        length
(%i4) fundamental_units (bar);
                                2
(%o4)                          m
```


アドホック単位。










```maxima
(%i1) load ("ezunits")$
(%i2) baz : 3 ` sheep + 8 ` goat + 1 ` horse;
(%o2)           8 ` goat + 3 ` sheep + 1 ` horse
(%i3) subst ([sheep = 3*goat, horse = 10*goat], baz);
(%o3)                       27 ` goat
(%i4) baz2 : 1000`gallon/fortnight;
                                gallon
(%o4)                   1000 ` ---------
                               fortnight
(%i5) subst (fortnight = 14*day, baz2);
                          500   gallon
(%o5)                     --- ` ------
                           7     day
```


次元量の算術演算子











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` kg + 200 ` kg;
(%o2)                       300 ` kg
(%i3) 100 ` m^3 - 100 ` m^3;
                                  3
(%o3)                        0 ` m
(%i4) (10 ` kg) * (17 ` m/s^2);
                                 kg m
(%o4)                      170 ` ----
                                   2
                                  s
(%i5) (x ` m) / (y ` s);
                              x   m
(%o5)                         - ` -
                              y   s
(%i6) (a ` m)^2;
                              2    2
(%o6)                        a  ` m
```

<!-- category: Units -->
<!-- keywords: `` -->
<!-- signatures: `` -->
### Function: ``

単位変換演算子。
式 $a ` b `` c$は単位 `b`を単位 `c`に変換します。
`ezunits`にはSI基本単位、SI組立単位、いくつかの非SI単位のための
組み込み変換があります。
`ezunits`がまだ知らない単位変換は宣言することができます。
`ezunits`が知っている単位変換はグローバル変数 `known_unit_conversions`に
明記されます。それは、組み込みとユーザー定義の変換を含みます。
単位の積、商、べきの変換は既知の単位変換一式から演繹されます。


単位の表示のためにより好まれる系はありません;
変換が明示的に示されない限り、
入力単位は他の単位に変換されません。
`ezunits`は、
変換が明示的に示されない限り、
前置詞(milli-, centi-, deci-, etc)で単位を整理しようとしません。


`load("ezunits")`はこの演算子を有効にします。


例:


既知の単位変換一式。








```maxima
(%i1) load ("ezunits")$
(%i2) display2d : false$
(%i3) known_unit_conversions;
(%o3) {acre = 4840*yard^2,Btu = 1055*J,cfm = feet^3/minute,
       cm = m/100,day = 86400*s,feet = 381*m/1250,ft = feet,
       g = kg/1000,gallon = 757*l/200,GHz = 1000000000*Hz,
       GOhm = 1000000000*Ohm,GPa = 1000000000*Pa,
       GWb = 1000000000*Wb,Gg = 1000000*kg,Gm = 1000000000*m,
       Gmol = 1000000*mol,Gs = 1000000000*s,ha = hectare,
       hectare = 100*m^2,hour = 3600*s,Hz = 1/s,inch = feet/12,
       km = 1000*m,kmol = 1000*mol,ks = 1000*s,l = liter,
       lbf = pound_force,lbm = pound_mass,liter = m^3/1000,
       metric_ton = Mg,mg = kg/1000000,MHz = 1000000*Hz,
       microgram = kg/1000000000,micrometer = m/1000000,
       micron = micrometer,microsecond = s/1000000,
       mile = 5280*feet,minute = 60*s,mm = m/1000,
       mmol = mol/1000,month = 2629800*s,MOhm = 1000000*Ohm,
       MPa = 1000000*Pa,ms = s/1000,MWb = 1000000*Wb,
       Mg = 1000*kg,Mm = 1000000*m,Mmol = 1000000000*mol,
       Ms = 1000000*s,ns = s/1000000000,ounce = pound_mass/16,
       oz = ounce,Ohm = s*J/C^2,
       pound_force = 32*ft*pound_mass/s^2,
       pound_mass = 200*kg/441,psi = pound_force/inch^2,
       Pa = N/m^2,week = 604800*s,Wb = J/A,yard = 3*feet,
       year = 31557600*s,C = s*A,F = C^2/J,GA = 1000000000*A,
       GC = 1000000000*C,GF = 1000000000*F,GH = 1000000000*H,
       GJ = 1000000000*J,GK = 1000000000*K,GN = 1000000000*N,
       GS = 1000000000*S,GT = 1000000000*T,GV = 1000000000*V,
       GW = 1000000000*W,H = J/A^2,J = m*N,kA = 1000*A,
       kC = 1000*C,kF = 1000*F,kH = 1000*H,kHz = 1000*Hz,
       kJ = 1000*J,kK = 1000*K,kN = 1000*N,kOhm = 1000*Ohm,
       kPa = 1000*Pa,kS = 1000*S,kT = 1000*T,kV = 1000*V,
       kW = 1000*W,kWb = 1000*Wb,mA = A/1000,mC = C/1000,
       mF = F/1000,mH = H/1000,mHz = Hz/1000,mJ = J/1000,
       mK = K/1000,mN = N/1000,mOhm = Ohm/1000,mPa = Pa/1000,
       mS = S/1000,mT = T/1000,mV = V/1000,mW = W/1000,
       mWb = Wb/1000,MA = 1000000*A,MC = 1000000*C,
       MF = 1000000*F,MH = 1000000*H,MJ = 1000000*J,
       MK = 1000000*K,MN = 1000000*N,MS = 1000000*S,
       MT = 1000000*T,MV = 1000000*V,MW = 1000000*W,
       N = kg*m/s^2,R = 5*K/9,S = 1/Ohm,T = J/(m^2*A),V = J/C,
       W = J/s}
```


基本単位変換。
















```maxima
(%i1) load ("ezunits")$
(%i2) 1 ` ft `` m;
Computing conversions to base units; may take a moment. 
                            381
(%o2)                       ---- ` m
                            1250
(%i3) %, numer;
(%o3)                      0.3048 ` m
(%i4) 1 ` kg `` lbm;
                            441
(%o4)                       --- ` lbm
                            200
(%i5) %, numer;
(%o5)                      2.205 ` lbm
(%i6) 1 ` W `` Btu/hour;
                           720   Btu
(%o6)                      --- ` ----
                           211   hour
(%i7) %, numer;
                                        Btu
(%o7)               3.412322274881517 ` ----
                                        hour
(%i8) 100 ` degC `` degF;
(%o8)                      212 ` degF
(%i9) -40 ` degF `` degC;
(%o9)                     (- 40) ` degC
(%i10) 1 ` acre*ft `` m^3;
                        60228605349    3
(%o10)                  ----------- ` m
                         48828125
(%i11) %, numer;
                                          3
(%o11)                1233.48183754752 ` m
```


フィートとメートルを相互に強制変換。











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` m + 100 ` ft;
(%o2)                  100 ` m + 100 ` ft
(%i3) (100 ` m + 100 ` ft) `` ft;
Computing conversions to base units; may take a moment. 
                           163100
(%o3)                      ------ ` ft
                            381
(%i4) %, numer;
(%o4)                428.0839895013123 ` ft
(%i5) (100 ` m + 100 ` ft) `` m;
                            3262
(%o5)                       ---- ` m
                             25
(%i6) %, numer;
(%o6)                      130.48 ` m
```


基本次元と基本単位を見つけるための次元解析











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 1 ` acre * ft;
(%o2)                      1 ` acre ft
(%i3) dimensions (foo);
                                   3
(%o3)                        length
(%i4) fundamental_units (foo);
                                3
(%o4)                          m
(%i5) foo `` m^3;
Computing conversions to base units; may take a moment. 
                        60228605349    3
(%o5)                   ----------- ` m
                         48828125
(%i6) %, numer;
                                          3
(%o6)                 1233.48183754752 ` m
```


宣言された単位変換。











```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (MMBtu = 10^6*Btu, kW = 1000*W);
(%o2)                         done
(%i3) declare_unit_conversion (kWh = kW*hour, MWh = 1000*kWh,
                               bell = 1800*s);
(%o3)                         done
(%i4) 1 ` kW*s `` MWh;
Computing conversions to base units; may take a moment. 
                             1
(%o4)                     ------- ` MWh
                          3600000
(%i5) 1 ` kW/m^2 `` MMBtu/bell/ft^2;
                       1306449      MMBtu
(%o5)                 ---------- ` --------
                      8242187500          2
                                   bell ft
```

<!-- category: Units -->
<!-- keywords: constvalue, declare_constvalue, remove_constvalue -->
<!-- signatures: constvalue(x), declare_constvalue(a, x), remove_constvalue(a) -->
### Function: constvalue (x)

シンボルの宣言された定数や、
シンボルに宣言された定数を代入した式の値をを返します。


定数は`declare_constvalue`で宣言されます。
`constvalue`が認識する定数は
`numerval`で宣言された値や`constantp`が認識する値と区別されることに
注意してください。


`physical_units`パッケージはたくさんの物理定数の定数値を宣言します。


`remove_constvalue`は
`declare_constvalue`の効果を戻します。


`load("ezunits")`はこれらの関数をロードします。


例:


物理定数の定数値。








```maxima
(%i1) load ("physical_constants")$
(%i2) constvalue (%G);
                                     3
                                    m
(%o2)                    6.67428 ` -----
                                       2
                                   kg s
(%i3) get ('%G, 'description);
(%o3)           Newtonian constant of gravitation
```


新しい定数の宣言。









```maxima
(%i1) load ("ezunits")$
(%i2) declare_constvalue (FOO, 100 ` lbm / acre);
                                 lbm
(%o2)                      100 ` ----
                                 acre
(%i3) FOO * (50 ` acre);
(%o3)                     50 FOO ` acre
(%i4) constvalue (%);
(%o4)                      5000 ` lbm
```

<!-- category: Units -->
<!-- keywords: declare_dimensions, remove_dimensions -->
<!-- signatures: declare_dimensions(a_1, d_1, ..., a_n, d_n), remove_dimensions(a_1, ..., a_n) -->
### Function: declare_dimensions (a_1, d_1, ..., a_n, d_n)

`declare_dimensions`は
*a_1*, ..., *a_n*を
それぞれ、次元*d_1*, ..., *d_n*を持つと
宣言します。


*a_k*それぞれはシンボルかシンボルのリストです。
もしリストなら、*a_k*内のすべてのシンボルは
次元 *d_k*を持つように宣言されます。


`remove_dimensions`は `declare_dimensions`の効果を戻します。


`load("ezunits")`はこれらの関数をロードします。


例:









```maxima
(%i1) load ("ezunits") $
(%i2) declare_dimensions ([x, y, z], length, [t, u], time);
(%o2)                         done
(%i3) dimensions (y^2/u);
                                   2
                             length
(%o3)                        -------
                              time
(%i4) fundamental_units (y^2/u);
0 errors, 0 warnings
                                2
                               m
(%o4)                          --
                               s
```

<!-- category: Units -->
<!-- keywords: declare_fundamental_dimensions, remove_fundamental_dimensions, fundamental_dimensions -->
<!-- signatures: declare_fundamental_dimensions(d_1, d_2, d_3, ...), remove_fundamental_dimensions(d_1, d_2, d_3, ...), fundamental_dimensions -->
### Function: declare_fundamental_dimensions (d_1, d_2, d_3, ...)

`declare_fundamental_dimensions`は基本次元を宣言します。
シンボル *d_1*, *d_2*, *d_3*, ... は、
もしそれらがまだリストの中にないなら、基本次元のリストに追加されます。


`remove_fundamental_dimensions`は
`declare_fundamental_dimensions`の効果を戻します。


`fundamental_dimensions`は基本次元のリストです。
デフォルトでは、リストはいくつかの物理次元から成ります。


`load("ezunits")`はこれらの関数をロードします。


例:











```maxima
(%i1) load ("ezunits") $
(%i2) fundamental_dimensions;
(%o2) [length, mass, time, current, temperature, quantity]
(%i3) declare_fundamental_dimensions (money, cattle, happiness);
(%o3)                         done
(%i4) fundamental_dimensions;
(%o4) [length, mass, time, current, temperature, quantity, 
                                        money, cattle, happiness]
(%i5) remove_fundamental_dimensions (cattle, happiness);
(%o5)                         done
(%i6) fundamental_dimensions;
(%o6) [length, mass, time, current, temperature, quantity, money]
```

<!-- category: Units -->
<!-- keywords: declare_fundamental_units, remove_fundamental_units -->
<!-- signatures: declare_fundamental_units(u_1, d_1, ..., u_n, d_n), remove_fundamental_units(u_1, ..., u_n) -->
### Function: declare_fundamental_units (u_1, d_1, ..., u_n, d_n)

`declare_fundamental_units`は
*u_1*, ..., *u_n*を
それぞれ、次元*d_1*, ..., *d_n*を持つように宣言します。
引数すべてはシンボルでなければいけません。


`declare_fundamental_units`をコールした後、
`dimensions(u_k)`は
引数*u_1*, ..., *u_n*それぞれに対して
*d_k*を返し、
`fundamental_units(d_k)`は
引数*d_1*, ..., *d_n*それぞれに対して
*u_k*を返します。



`remove_fundamental_units`は
`declare_fundamental_units`の効果を戻します。


`load("ezunits")`はこれらの関数をロードします。


例:











```maxima
(%i1) load ("ezunits") $
(%i2) declare_fundamental_dimensions (money, cattle, happiness);
(%o2)                         done
(%i3) declare_fundamental_units (dollar, money, goat, cattle, smile, happiness);
(%o3)                 [dollar, goat, smile]
(%i4) dimensions (100 ` dollar/goat/km^2);
                             money
(%o4)                    --------------
                                      2
                         cattle length
(%i5) dimensions (x ` smile/kg);
                            happiness
(%o5)                       ---------
                              mass
(%i6) fundamental_units (money*cattle/happiness);
0 errors, 0 warnings
                           dollar goat
(%o6)                      -----------
                              smile
```

<!-- category: Units -->
<!-- keywords: declare_unit_conversion -->
<!-- signatures: declare_unit_conversion(u=v, ...) -->
### Function: declare_unit_conversion (u=v, ...)

式 *u* = *v*, ... を
単位変換演算子 $``$が知っている単位変換のリストに追加します。
*u*と *v*はともにその中のいかなる変数も単位である乗法の項か、
文字通り次元式です。


現在、
それぞれの式の左辺が(乗法式でなく)ただの単位か、
1に等しい量とただの単位である単位の文字通り次元式であるような
変換を表現する必要があります。
この限定は将来のバージョンで緩和されるかもしれません。


`known_unit_conversions`は既知の単位変換のリストです。


`load("ezunits")`はこの関数をロードします。


例:


乗法項の等式で表現された単位変換。









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (nautical_mile = 1852 * m,
                               fortnight = 14 * day);
(%o2)                         done
(%i3) 100 ` nautical_mile / fortnight `` m/s;
Computing conversions to base units; may take a moment. 
                            463    m
(%o3)                       ---- ` -
                            3024   s
```


文字通り次元式の等式で表現された単位変換。









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (1 ` fluid_ounce = 2 ` tablespoon);
(%o2)                         done
(%i3) declare_unit_conversion (1 ` tablespoon = 3 ` teaspoon);
(%o3)                         done
(%i4) 15 ` fluid_ounce `` teaspoon;
Computing conversions to base units; may take a moment. 
(%o4)                     90 ` teaspoon
```

<!-- category: Units -->
<!-- keywords: dimensionless -->
<!-- signatures: dimensionless(L) -->
### Function: dimensionless (L)

次元量のリスト*L*から形成できる
無次元量の基底を返します。


`load("ezunits")`はこの関数をロードします。


例:







```maxima
(%i1) load ("ezunits") $
(%i2) dimensionless ([x ` m, y ` m/s, z ` s]);
0 errors, 0 warnings
0 errors, 0 warnings
                               y z
(%o2)                         [---]
                                x
```


Dimensionless quantities derived from fundamental physical quantities.
Note that the first element on the list
is proportional to the fine-structure constant.








```maxima
(%i1) load ("ezunits") $
(%i2) load ("physical_constants") $
(%i3) dimensionless([%h_bar, %m_e, %m_P, %%e, %c, %e_0]);
0 errors, 0 warnings
0 errors, 0 warnings
                              2
                           %%e        %m_e
(%o3)                [--------------, ----]
                      %c %e_0 %h_bar  %m_P
```

<!-- category: Units -->
<!-- keywords: fundamental_units -->
<!-- signatures: fundamental_units(x), fundamental_units() -->
### Function: fundamental_units (x)

`fundamental_units(x)`は
`dimensions(x)`が決定するように
*x*の基本次元に関連付けられた
単位を返します。


*x*は文字通り次元式$a ` b$か、
`declare_units`を介して宣言された単位を持つシンボルか
それらのいずれかもしくは両方を含む式かもしれません。


`fundamental_units()`は
`declare_fundamental_units`が宣言するように、
既知の基本単位すべてのリストを返します。



`load("ezunits")`はこの関数をロードします。


例:










```maxima
(%i1) load ("ezunits")$
(%i2) fundamental_units ();
(%o2)                 [m, kg, s, A, K, mol]
(%i3) fundamental_units (100 ` mile/hour);
                                m
(%o3)                           -
                                s
(%i4) declare_units (aa, g/foot^2);
                                g
(%o4)                         -----
                                  2
                              foot
(%i5) fundamental_units (aa);
                               kg
(%o5)                          --
                                2
                               m
```

<!-- category: Units -->
<!-- keywords: natural_unit -->
<!-- signatures: natural_unit(expr, [v_1, ..., v_n]) -->
### Function: natural_unit (expr, [v_1, ..., v_n])

`dimension(expr) = dimension(v_1^e_1 ... v_n^e_n)`であるような
指数*e_1*, ..., *e_n*を見つけます。


`load("ezunits")`はこの関数をロードします。


例:





```maxima

```

<!-- category: Units -->
<!-- keywords: qty, declare_qty -->
<!-- signatures: qty(x), declare_qty(a, x) -->
### Function: qty (x)

`qty`は次元量*x*の無次元パーツを返します。
もし *x*が無次元なら、*x*を返します。
*x*は文字通り次元式 $a ` b$かも知れませんし、
宣言された量のシンボルかもしれませんし、
それらの一方または両方を含む式かもしれません。


`declare_qty`は、
`qty(a)`は無次元量*x*を返さなければいけないことを宣言します。


`load("ezunits")`はこれらの関数をロードします。


例:


文字通り次元式に適用された`qty`。











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                       100 ` kg
(%i3) qty (foo);
(%o3)                          100
(%i4) bar : v ` m/s;
                                  m
(%o4)                         v ` -
                                  s
(%i5) foo * bar;
                                  kg m
(%o5)                     100 v ` ----
                                   s
(%i6) qty (foo * bar);
(%o6)                         100 v
```


宣言された量のシンボルへ適用された`qty`。











```maxima
(%i1) load ("ezunits")$
(%i2) declare_qty (aa, xx);
(%o2)                          xx
(%i3) qty (aa);
(%o3)                          xx
(%i4) qty (aa^2);
                                 2
(%o4)                          xx
(%i5) foo : 100 ` kg;
(%o5)                       100 ` kg
(%i6) qty (aa * foo);
(%o6)                        100 xx
```

<!-- category: Units -->
<!-- keywords: unitp -->
<!-- signatures: unitp(x) -->
### Function: unitp (x)

もし*x*が文字通り次元式か、
次元的と宣言されたシンボルか、
主演算子が次元的宣言された式なら、
`true`を返します。
それ以外なら、`unitp`は `false`を返します。


`load("ezunits")`はこの関数を返します。


例:


文字通り次元式へ適用された`unitp`。







```maxima
(%i1) load ("ezunits")$
(%i2) unitp (100 ` kg);
(%o2)                         true
```


次元的と宣言されたシンボルへ適用された`unitp`。









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (foo);
(%o2)                         false
(%i3) declare (foo, dimensional);
(%o3)                         done
(%i4) unitp (foo);
(%o4)                         true
```


主演算子が次元的と宣言された式に適用された`unitp`。









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (bar (x, y, z));
(%o2)                         false
(%i3) declare (bar, dimensional);
(%o3)                         done
(%i4) unitp (bar (x, y, z));
(%o4)                         true
```

<!-- category: Units -->
<!-- keywords: units, declare_units -->
<!-- signatures: units(x), declare_units(a, u) -->
### Function: units (x)

次元量*x*の単位を返します。
もし*x*が無次元なら、1を返します。


*x*は、文字通り次元式 $a ` b$かもしれませんし、
`declare_units`を介して宣言された単位を持つシンボルかもしれませんし、
それらの一方または両方を含む式かもしれません。


`declare_units`は、
`units(a)`は式*u*を返さなければいけないことを宣言します。


`load("ezunits")`はこれらの関数をロードします。


例:


文字通り次元式へ適用された`units`。













```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                       100 ` kg
(%i3) bar : x ` m/s;
                                  m
(%o3)                         x ` -
                                  s
(%i4) units (foo);
(%o4)                          kg
(%i5) units (bar);
                                m
(%o5)                           -
                                s
(%i6) units (foo * bar);
                              kg m
(%o6)                         ----
                               s
(%i7) units (foo / bar);
                              kg s
(%o7)                         ----
                               m
(%i8) units (foo^2);
                                 2
(%o8)                          kg
```


宣言された単位を持つシンボルに適用された`units`。












```maxima
(%i1) load ("ezunits")$
(%i2) units (aa);
(%o2)                           1
(%i3) declare_units (aa, J);
(%o3)                           J
(%i4) units (aa);
(%o4)                           J
(%i5) units (aa^2);
                                2
(%o5)                          J
(%i6) foo : 100 ` kg;
(%o6)                       100 ` kg
(%i7) units (aa * foo);
(%o7)                         kg J
```

