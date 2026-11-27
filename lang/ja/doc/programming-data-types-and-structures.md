## Data Types and Structures

<!-- category: Programming -->
<!-- keywords: %e -->
<!-- signatures: %e -->
### Variable: %e

`%e`はEuler数としても知られる自然対数の基数を表します。
`%e`の数値は倍精度浮動小数点数2.718281828459045d0です。

<!-- category: Programming -->
<!-- keywords: %gamma -->
<!-- signatures: %gamma -->
### Variable: %gamma

Euler-Macheroni定数0.5772156649015329 ....

<!-- category: Programming -->
<!-- keywords: %i -->
<!-- signatures: %i -->
### Variable: %i

`%i`は虚数単位$sqrt(- 1)$を表します。

<!-- category: Programming -->
<!-- keywords: %phi -->
<!-- signatures: %phi -->
### Variable: %phi

`%phi`は*黄金比*と呼ばれる$(1 + sqrt(5))/2$を表します。
`%phi`の数値は倍精度浮動小数点数1.618033988749895d0です。


`fibtophi`は、`%phi`を使って
フィボナッチ数`fib(n)`を表現します。


デフォルトでは、Maximaは
`%phi`の代数的プロパティを知りません。
`tellrat(%phi^2 - %phi - 1)`と`algebraic: true`を評価した後、
`ratsimp`は `%phi`を含むいくつかの式を整理できます。


例:


`fibtophi`は、`%phi`を使って
フィボナッチ数`fib(n)`を表現します。









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```


デフォルトでは、Maximaは
`%phi`の代数的プロパティを知りません。
`tellrat(%phi^2 - %phi - 1)`と`algebraic: true`を評価した後、
`ratsimp`は `%phi`を含むいくつかの式を整理できます。










```maxima
(%i1) e : expand ((%phi^2 - %phi - 1) * (A + 1));
                 2                      2
(%o1)        %phi  A - %phi A - A + %phi  - %phi - 1
(%i2) ratsimp (e);
                  2                     2
(%o2)        (%phi  - %phi - 1) A + %phi  - %phi - 1
(%i3) tellrat (%phi^2 - %phi - 1);
                            2
(%o3)                  [%phi  - %phi - 1]
(%i4) algebraic : true;
(%o4)                         true
(%i5) ratsimp (e);
(%o5)                           0
```

See also: `fibtophi`, `ratsimp`.

<!-- category: Programming -->
<!-- keywords: %pi -->
<!-- signatures: %pi -->
### Variable: %pi

`%pi`は直径に体する円周の比を表します。
`%pi`の数値は倍精度浮動小数点数3.141592653589793d0です。

<!-- category: Programming -->
<!-- keywords: @ -->
<!-- signatures: @ -->
### Function: @

`@`構造体フィールドアクセス演算子です。
式`x@ a`は
構造体インスタンス*x*のフィールド*a*の値を参照します。
フィールド名は評価されません。


もし*x*のフィールド*a*が値を割り当てられていないなら、
`x@ a`はそれ自身に評価されます。


`kill(x@ a)`は
*x*のフィールド値*a*を値を取り除きます。


例:













```maxima
(%i1) defstruct (foo (x, y, z));
(%o1)                    [foo(x, y, z)]
(%i2) u : new (foo (123, a - b, %pi));
(%o2)           foo(x = 123, y = a - b, z = %pi)
(%i3) u@z;
(%o3)                          %pi
(%i4) u@z : %e;
(%o4)                          %e
(%i5) u;
(%o5)            foo(x = 123, y = a - b, z = %e)
(%i6) kill (u@z);
(%o6)                         done
(%i7) u;
(%o7)              foo(x = 123, y = a - b, z)
(%i8) u@z;
(%o8)                          u@z
```


フィールド名は評価されません。













```maxima
(%i1) defstruct (bar (g, h));
(%o1)                      [bar(g, h)]
(%i2) x : new (bar);
(%o2)                       bar(g, h)
(%i3) x@h : 42;
(%o3)                          42
(%i4) h : 123;
(%o4)                          123
(%i5) x@h;
(%o5)                          42
(%i6) x@h : 19;
(%o6)                          19
(%i7) x;
(%o7)                    bar(g, h = 19)
(%i8) h;
(%o8)                          123
```

<!-- category: Programming -->
<!-- keywords: [, ] -->
<!-- signatures: ] -->
### Variable: [

先頭が`[`で終わりが`]`のマークはリストです。


`[`と`]`は、リスト、配列、ハッシュ配列、配列関数の添字もくくります。


例:



```maxima
(%i1) x: [a, b, c];
(%o1)                       [a, b, c]
(%i2) x[3];
(%o2)                           c
(%i3) array (y, fixnum, 3);
(%o3)                           y
(%i4) y[2]: %pi;
(%o4)                          %pi
(%i5) y[2];
(%o5)                          %pi
(%i6) z['foo]: 'bar;
(%o6)                          bar
(%i7) z['foo];
(%o7)                          bar
(%i8) g[k] := 1/(k^2+1);
                                  1
(%o8)                     g  := ------
                           k     2
                                k  + 1
(%i9) g[10];
                                1
(%o9)                          ---
                               101
```

<!-- category: Programming -->
<!-- keywords: append -->
<!-- signatures: append(list_1, ..., list_n) -->
### Function: append (list_1, ..., list_n)

*list_1*の要素のあとに
*list_2*の要素が続き、...
という１つのリストを返します。
`append`は一般式上でも機能します。
例えば、 `append (f(a,b), f(c,d,e));`は
`f(a,b,c,d,e)`をもたらします。


例を見るには、 `example(append);`を実行してください。

<!-- category: Programming -->
<!-- keywords: array -->
<!-- signatures: array(name, dim_1, ..., dim_n), array(name, type, dim_1, ..., dim_n), array([name_1, ..., name_m], dim_1, ..., dim_n) -->
### Function: array (name, dim_1, ..., dim_n)

$n$次元の配列を生成します。
$n$は5以下を取り得ます。
$i$番目の次元のための添字は0から*dim_i*まで動く整数です。


`array (name, dim_1, ..., dim_n)`は
一般的な配列を生成します。


`array (name, type, dim_1, ..., dim_n)`は
指定されたタイプの要素を持つ配列を生成します。
*type*には
制限されたサイズの整数には`fixnum`が使え、
また、浮動小数点には`flonum`が使えます。


`array ([name_1, ..., name_m], dim_1, ..., dim_n)`
は同じ次元の$m$個の配列を生成します。




もしユーザーが対応する配列を宣言する前に添字付き変数に割り当てたら、
未宣言配列が生成されます。
(ハッシュコーディングが添字上でされるので)別名ハッシュド配列と知られる未宣言配列は、
宣言配列よりもっと一般的です。
ユーザーは最大サイズを宣言せず、さらなる要素が値に割り当てられる時、ハッシュすることで
それらは動的に成長します。
未宣言配列の添字は数である必要すらありません。
しかしながら、
配列がむしろ疎でないなら、
未宣言のまま放っておくより、可能な時に宣言した方がおそらく効率的です。
`array`関数は未宣言配列を宣言配列に変換するのに使うことができます。

<!-- category: Programming -->
<!-- keywords: arrayapply -->
<!-- signatures: arrayapply(A, [i_1, ...i_n]) -->
### Function: arrayapply (A, [i_1, ...i_n])

`A [i_1, ..., i_n]`を評価します。
ここで、*A*は配列、*i_1*, ..., *i_n*は整数です。


これは、最初の引数が関数の代わりに配列だということを除いて、
`apply`を連想させます。

See also: `apply`.

<!-- category: Programming -->
<!-- keywords: arrayinfo -->
<!-- signatures: arrayinfo(A) -->
### Function: arrayinfo (A)

配列*A*に関する情報を返します。
引数*A*は、宣言配列、未宣言(ハッシュド)配列、配列関数、または添字付き関数を取り得ます。


宣言配列では、
`arrayinfo`は、
アトム`declared`と、次元数、それぞれの次元のサイズを含むリストを返します。
配列の要素は、バインドされたものもそうでないものも、`listarray`で返されます。


未宣言配列(ハッシュド配列)では、
`arrayinfo`は、
アトム`hashed`と、添字の数、値を持つすべての要素の添字を含むリストを返します。
値は `listarray`で返されます。


配列関数では、
`arrayinfo`は、
アトム`hashed`と、添字の数、
記憶された関数値がある添字の値すべてを含むリストを返します。
記憶された関数値は、`listarray`で返されます。


添字付き関数では、、
`arrayinfo`は、
 returns a list comprising the 
アトム`hashed`と、添字の数、
ラムダ式がある添字の値すべてを含むリストを返します。
ラムダ式は `listarray`で返されます。


`listarray`も参照してください。


例:


宣言配列に適用された`arrayinfo`と`listarray`。










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa


(%i2) aa [2, 3] : %pi;
(%o2)                          %pi


(%i3) aa [1, 2] : %e;
(%o3)                          %e


(%i4) arrayinfo (aa);
(%o4)                 [declared, 2, [2, 3]]


(%i5) listarray (aa);
(%o5) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
```


未宣言(ハッシュド)配列に適用された`arrayinfo`と`listarray`。









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) arrayinfo (bb);
(%o3)               [hashed, 1, [BAR], [FOO]]


(%i4) listarray (bb);
                              3         2
(%o4)                 [(c - d) , (b + a) ]
```


配列関数に適用された`arrayinfo`と`listarray`。










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) arrayinfo (cc);
(%o4)              [hashed, 2, [4, z], [u, v]]


(%i5) listarray (cc);
                              z  v
(%o5)                        [-, -]
                              4  u
```


添字付き関数に適用された`arrayinfo`と`listarray`。










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) arrayinfo (dd);
(%o4)             [hashed, 1, [b + a], [v - u]]


(%i5) listarray (dd);
                         b + a                v - u
(%o5)      [lambda([y], y     ), lambda([y], y     )]
```

See also: `listarray`.

<!-- category: Programming -->
<!-- keywords: arraymake -->
<!-- signatures: arraymake(A, [i_1, ..., i_n]) -->
### Function: arraymake (A, [i_1, ..., i_n])

式`A[i_1, ..., i_n]`を返します。
結果は未評価の配列参照です。


`arraymake`は、
戻り値は、未評価関数コールの代わりに未評価の配列参照だということを除いて、
`funmake`を連想させます。


例:


















```maxima
(%i1) arraymake (A, [1]);
(%o1)                          A
                                1


(%i2) arraymake (A, [k]);
(%o2)                          A
                                k


(%i3) arraymake (A, [i, j, 3]);
(%o3)                       A
                             i, j, 3


(%i4) array (A, fixnum, 10);
(%o4)                           A


(%i5) fillarray (A, makelist (i^2, i, 1, 11));
(%o5)                           A


(%i6) arraymake (A, [5]);
(%o6)                          A
                                5


(%i7) ''%;
(%o7)                          36


(%i8) L : [a, b, c, d, e];
(%o8)                    [a, b, c, d, e]


(%i9) arraymake ('L, [n]);
(%o9)                          L
                                n


(%i10) ''%, n = 3;
(%o10)                          c


(%i11) A2 : make_array (fixnum, 10);
(%o11)          {Array:  #(0 0 0 0 0 0 0 0 0 0)}


(%i12) fillarray (A2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o12)          {Array:  #(1 2 3 4 5 6 7 8 9 10)}


(%i13) arraymake ('A2, [8]);
(%o13)                         A2
                                 8


(%i14) ''%;
(%o14)                          9
```

See also: `funmake`.

<!-- category: Programming -->
<!-- keywords: arrays -->
<!-- signatures: arrays -->
### Variable: arrays

デフォルト値: `[]`


`arrays`は割り当てられた配列のリストです。
これらは、`array`で宣言された配列、
(なにかw配列要素に割り当てられた)陰の定義で構成されたハッシュド配列、
`:=`と`define`で定義された配列関数を含みます。
`make_array`で定義された配列は含まれません。


`array`, `arrayapply`, `arrayinfo`, `arraymake`, 
`fillarray`, `listarray`, `rearray`も参照してください。



例:










```maxima
(%i1) array (aa, 5, 7);
(%o1)                          aa


(%i2) bb [FOO] : (a + b)^2;
                                   2
(%o2)                       (b + a)


(%i3) cc [x] := x/100;
                                   x
(%o3)                      cc  := ---
                             x    100


(%i4) dd : make_array ('any, 7);
(%o4)       {Array:  #(NIL NIL NIL NIL NIL NIL NIL)}


(%i5) arrays;
(%o5)                     [aa, bb, cc]
```

See also: `make_array`, `array`, `arrayapply`, `arrayinfo`, `arraymake`, `fillarray`, `listarray`, `rearray`.

<!-- category: Programming -->
<!-- keywords: assoc -->
<!-- signatures: assoc(key, list, default), assoc(key, list) -->
### Function: assoc (key, list, default)

この関数は
形式 `[x,y,z,...]`の入力 *list*の左辺の中で *key*を探します。
ここで *list*の要素のそれぞれは二項演算子と２つの要素の式です。
例えば、 `x=1`, `2^3`, `[a,b]`など。
最初のオペランドに対して *key*がチェックされます。
もし `key`が見つかったら、
`assoc`は二番目のオペランドを返します。
もし `key`が見つからなかったら、
*default*値を返します。
*default*はオプションで、省略すると `false`に設定されます。

<!-- category: Programming -->
<!-- keywords: cons -->
<!-- signatures: cons(expr, list) -->
### Function: cons (expr, list)

最初の要素として要素 *expr*で構成され、
*list*の要素が続く新しいリストを返します。
`cons`は他の式上でも機能します。
例えば、 `cons(x, f(a,b,c));`  ->  `f(x,a,b,c)`。

<!-- category: Programming -->
<!-- keywords: copylist -->
<!-- signatures: copylist(list) -->
### Function: copylist (list)

リスト *list*のコピーを返します。

<!-- category: Programming -->
<!-- keywords: create_list -->
<!-- signatures: create_list(form, x_1, list_1, ..., x_n, list_n) -->
### Function: create_list (form, x_1, list_1, ..., x_n, list_n)

*list_1*の要素それぞれにバインドされた *x_1*で、
また、それぞれのバインドに対して、
*x_2*を *list_2*の要素それぞれにバインドして、...
それらのバインドを使って *form*を評価することによって
リストを生成します。
結果の要素の数はそれぞれのリストの要素の数の積です。
それぞれの変数 *x_i*は実際に、シンボルでなければいけません。ーそれは評価されません。
リスト引数は繰り返しの始めに一度だけ評価されます。



```maxima
(%i1) create_list(x^i,i,[1,3,7]);
                 3   7
(%o1)       [x, x , x ]
```



二重の繰り返しで:



```maxima
(%i1) create_list([i,j],i,[a,b],j,[e,f,h]);
(%o1) [[a, e], [a, f], [a, h], [b, e], [b, f], [b, h]]
```


*list_i*の代わりに、
それぞれが数に評価される２つの引数を供給することもできます。
これらは繰り返しの下限と上限になります。



```maxima
(%i1) create_list([i,j],i,[1,2,3],j,1,i);
(%o1) [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
```


`j`変数の範囲やリストは `i`の現在値に依存することができることに注意してください。

<!-- category: Programming -->
<!-- keywords: defstruct -->
<!-- signatures: defstruct(S(a_1, ..., a_n)), defstruct(S(a_1=v_1, ..., a_n=v_n)) -->
### Function: defstruct (S(a_1, ..., a_n))

構造体を定義します。
構造体はシンボル*S*と関連付けられた名前フィールドのリスト*a_1*, ..., *a_n*です。


構造体のインスタンスは演算子*S*と正確に`n`個の引数を持つただの式です。
`new(S)`は構造体*S*の新しいインスタンスを生成します。


ただのシンボル*a*である引数はフィールド名を指定します。
等式`a = v`である引数は
フィールド名*a*とデフォルト値*v*を指定します。
デフォルト値は任意の式を取り得ます。


`defstruct`は
ユーザー定義の構造体のリスト`structures`上に*S*を入れます。


`kill(S)`は
ユーザー定義の構造体のリストから*S*を取り除き、構造体定義を取り除きます。


例:













```maxima
(%i1) defstruct (foo (a, b, c));
(%o1)                    [foo(a, b, c)]
(%i2) structures;
(%o2)                    [foo(a, b, c)]
(%i3) new (foo);
(%o3)                     foo(a, b, c)
(%i4) defstruct (bar (v, w, x = 123, y = %pi));
(%o4)             [bar(v, w, x = 123, y = %pi)]
(%i5) structures;
(%o5)      [foo(a, b, c), bar(v, w, x = 123, y = %pi)]
(%i6) new (bar);
(%o6)              bar(v, w, x = 123, y = %pi)
(%i7) kill (foo);
(%o7)                         done
(%i8) structures;
(%o8)             [bar(v, w, x = 123, y = %pi)]
```

<!-- category: Programming -->
<!-- keywords: delete -->
<!-- signatures: delete(expr_1, expr_2), delete(expr_1, expr_2, n) -->
### Function: delete (expr_1, expr_2)

`delete(expr_1, expr_2)`は、
*expr_2*から
そのトップレベル演算子の引数のうち、
*expr_1*と("="で決定される意味で)同じ引数を取り除きます。
"="は、同値ではなく、形式的な同一をテストすることに注意してください。
部分式の引数には影響しないことにも注意してください。


*expr_1*はアトムか、非アトムの式を取り得ます。
*expr_2*は任意の非アトムの式を取り得ます。
`delete`は新しい式を返します;
*expr_2*を変更しません。


`delete(expr_1, expr_2, n)`は、


*expr_2*から
そのトップレベル演算子の引数のうち、
*expr_1*と同じ最初の
*n*個の引数を取り除きます。
もしそんな引数が *n*個より少ないなら、
該当するすべての引数が取り除かれます。


例:


リストから要素を削除。






```maxima
(%i1) delete (y, [w, x, y, z, z, y, x, w]);
(%o1)                  [w, x, z, z, x, w]
```


和から項を削除。






```maxima
(%i1) delete (sin(x), x + sin(x) + y);
(%o1)                         y + x
```


積から因子を削除。






```maxima
(%i1) delete (u - x, (u - w)*(u - x)*(u - y)*(u - z));
(%o1)                (u - w) (u - y) (u - z)
```


任意の式から引数を削除。






```maxima
(%i1) delete (a, foo (a, b, c, d, a));
(%o1)                     foo(b, c, d)
```


削除する引数の数を制限。






```maxima
(%i1) delete (a, foo (a, b, a, c, d, a), 2);
(%o1)                    foo(b, c, d, a)
```


引数が *expr_1*と同じかどうかは"="で決定されます。
`equal`ですが、"="でない引数は取り除かれません。











```maxima
(%i1) [is(equal(0, 0)), is(equal(0, 0.0)), is(equal(0, 0b0))];

`rat' replaced 0.0 by 0/1 = 0.0
`rat' replaced 0.0B0 by 0/1 = 0.0B0
(%o1)                  [true, true, true]
(%i2) [is (0 = 0), is (0 = 0.0), is (0 = 0b0)];
(%o2)                 [true, false, false]
(%i3) delete (0, [0, 0.0, 0b0]);
(%o3)                     [0.0, 0.0b0]
(%i4) is (equal ((x + y)*(x - y), x^2 - y^2));
(%o4)                         true
(%i5) is ((x + y)*(x - y) = x^2 - y^2);
(%o5)                         false
(%i6) delete ((x + y)*(x - y), [(x + y)*(x - y), x^2 - y^2]);
                              2    2
(%o6)                       [x  - y ]
```

<!-- category: Programming -->
<!-- keywords: eighth -->
<!-- signatures: eighth(expr) -->
### Function: eighth (expr)

式またはリスト *expr*の8番目の項を返します。
詳細は `first`を参照してください。

<!-- category: Programming -->
<!-- keywords: endcons -->
<!-- signatures: endcons(expr, list) -->
### Function: endcons (expr, list)

*expr*が続く `list`の要素から成る新しいリストを返します。
`endcons`は一般式上でも機能します。
例えば、
`endcons(x, f(a,b,c));`  ->  `f(a,b,c,x)`。

<!-- category: Programming -->
<!-- keywords: false -->
<!-- signatures: false -->
### Variable: false

`false`は同じ名前のブーリアン定数を表します。
Maximaは、Lispの値`NIL`で`false`を実装しています。

<!-- category: Programming -->
<!-- keywords: fifth -->
<!-- signatures: fifth(expr) -->
### Function: fifth (expr)

式またはリスト *expr*の5番目の項を返します。
詳細は `first`を参照してください。

See also: `first`.

<!-- category: Programming -->
<!-- keywords: fillarray -->
<!-- signatures: fillarray(A, B) -->
### Function: fillarray (A, B)

配列*A*を*B*から埋めます。
ここで、*B*はリストか配列です。


もし生成時に特定のタイプが*A*のために宣言されたら、
その同じタイプの要素でだけ埋めることができます;
もし違ったタイプの要素をコピーする試みがなされたらエラーです。


もし配列*A*と*B*の次元が違ったら、
*A*は行優先順で埋められます。
もし*B*の中の要素が十分でないなら、
*A*の残りを埋めるのに最後の要素が使われます。
もし多すぎるなら、残りは無視されます。


`fillarray`は最初の引数を返します。


例:


9個の要素の配列を生成し、リストから埋めます。








```maxima
(%i1) array (a1, fixnum, 8);
(%o1)                          a1


(%i2) listarray (a1);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]


(%i3) fillarray (a1, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
(%o3)                          a1


(%i4) listarray (a1);
(%o4)              [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


配列を埋めるのに要素が足らない時、
最後の要素が繰り返されます。
要素が多すぎる時、余分の要素は無視されます。








```maxima
(%i1) a2 : make_array (fixnum, 8);
(%o1)             {Array:  #(0 0 0 0 0 0 0 0)}


(%i2) fillarray (a2, [1, 2, 3, 4, 5]);
(%o2)             {Array:  #(1 2 3 4 5 5 5 5)}


(%i3) fillarray (a2, [4]);
(%o3)             {Array:  #(4 4 4 4 4 4 4 4)}


(%i4) fillarray (a2, makelist (i, i, 1, 100));
(%o4)             {Array:  #(1 2 3 4 5 6 7 8)}
```


多次元配列は行優先順に埋められます。









```maxima
(%i1) a3 : make_array (fixnum, 2, 5);
(%o1)        {Array:  #2A((0 0 0 0 0) (0 0 0 0 0))}


(%i2) fillarray (a3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o2)        {Array:  #2A((1 2 3 4 5) (6 7 8 9 10))}


(%i3) a4 : make_array (fixnum, 5, 2);
(%o3)     {Array:  #2A((0 0) (0 0) (0 0) (0 0) (0 0))}


(%i4) fillarray (a4, a3);
(%o4)     {Array:  #2A((1 2) (3 4) (5 6) (7 8) (9 10))}
```

<!-- category: Programming -->
<!-- keywords: first -->
<!-- signatures: first(expr) -->
### Function: first (expr)

リストの最初の要素、行列の最初の行、和の最初の項などに帰着する、
*expr*の最初の部分を返します。
`first`とその関連関数 `rest`と `last`は、
入力時にタイプした形式ではなく、 *expr*の表示形式上で機能することに注意してください。
しかしながら、もし変数 `inflag`が `true`に設定されているなら、
これらの関数は *expr*の内部形式を見ます。
整理器は式を再配置することに注意してください。
例えば、
`first(x+y)`は、
もし `inflag`が `true`なら `x`で、
もし `inflag`が `false`なら `y` です。
 (`first(y+x)`は同じ結果を与えます。)
関数 `second` .. `tenth`は
入力引数の二番目から十番目の部分をもたらします。

<!-- category: Programming -->
<!-- keywords: fourth -->
<!-- signatures: fourth(expr) -->
### Function: fourth (expr)

式またはリスト *expr*の4番目の項を返します。
詳細は `first`を参照してください。

See also: `first`.

<!-- category: Programming -->
<!-- keywords: ind -->
<!-- signatures: ind -->
### Variable: ind

`ind`は有界で不定の結果を表します。


`limit`も参照してください。


例:






```maxima
(%i1) limit (sin(1/x), x, 0);
(%o1)                          ind
```

See also: `limit`.

<!-- category: Programming -->
<!-- keywords: inf -->
<!-- signatures: inf -->
### Variable: inf

`inf`は実数の正の無限大を表します。

<!-- category: Programming -->
<!-- keywords: infinity -->
<!-- signatures: infinity -->
### Variable: infinity

`infinity`は複素数の無限大を表します。

<!-- category: Programming -->
<!-- keywords: join -->
<!-- signatures: join(l, m) -->
### Function: join (l, m)

リスト*l*と*m*の要素を交互に含む新しいリストを生成します。
結果は、要素 `[l[1], m[1], l[2], m[2], ...]`を持ちます。
リスト *l*と *m*は、任意のタイプの要素を含めます。


もしリストの長さが違ったら、
`join`は長いリストの要素を無視します。


もし *l*か *m*がリストでなかったら、
Maximaは文句を言います。


例:








```maxima
(%i1) L1: [a, sin(b), c!, d - 1];
(%o1)                [a, sin(b), c!, d - 1]
(%i2) join (L1, [1, 2, 3, 4]);
(%o2)          [a, 1, sin(b), 2, c!, 3, d - 1, 4]
(%i3) join (L1, [aa, bb, cc, dd, ee, ff]);
(%o3)        [a, aa, sin(b), bb, c!, cc, d - 1, dd]
```

<!-- category: Programming -->
<!-- keywords: last -->
<!-- signatures: last(expr) -->
### Function: last (expr)

*expr*最後の(項、行、要素など）部分を返します。

<!-- category: Programming -->
<!-- keywords: length -->
<!-- signatures: length(expr) -->
### Function: length (expr)

(デフォルトでは) *expr*の外部(表示)形式の部分の数を返します。
リストに関しては、これは要素の数を返し、
行列に関しては行数であり、
和に関しては項数です。
(`dispform`を参照してください。)


`length`コマンドは `inflag`スイッチに影響されます。
だから例えば、 `length(a/(b*c));`は、
 (`exptdispflag`が `true`と仮定して)
もし `inflag`が `false`なら2を与えますが、
もし `inflag`が `true`なら3を与えます。
 (内部表現は本質的には `a*b^-1*c^-1`です。)

See also: `dispform`, `inflag`, `exptdispflag`.

<!-- category: Programming -->
<!-- keywords: listarith -->
<!-- signatures: listarith -->
### Variable: listarith

デフォルト値: `true` - もし `false`なら、
リストを伴う任意の算術演算が抑制されるようになります;
`true`の時、リスト-行列演算では、
リストが行列に変換されるようになり、いつも行列の結果をもたらすよう連鎖します。
しかしながら、リスト-リスト演算はリストを返します。

<!-- category: Programming -->
<!-- keywords: listarray -->
<!-- signatures: listarray(A) -->
### Function: listarray (A)

配列*A*の要素のリストを返します。
引数*A*は、宣言配列、未宣言(ハッシュド)配列、配列関数、添字付き関数を取り得ます。


要素は行優先順にリストされます。
すなわち、要素は、最初のインデックスに従って振り分けられ、次に二番目のインデックスに従って、などなど。
インデックス値の振り分け順は、
`orderless`が確立する順と同じです。


未宣言配列や、配列関数、添字付き関数では、
要素は`arrayinfo`が返すインデックス値に対応します。


宣言された一般配列のバインドされていない要素(すなわち、`fixnum`でも`flonum`でもない要素)は、 `#####`として返されます。
宣言された`fixnum`配列または`flonum`配列のバイドされていない要素は、
それぞれ0または0.0として返されます。
未宣言配列、配列関数、添字付き関数のバインドされていない要素は返されません。


例:


宣言配列に適用された`listarray`と`arrayinfo`。










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa


(%i2) aa [2, 3] : %pi;
(%o2)                          %pi


(%i3) aa [1, 2] : %e;
(%o3)                          %e


(%i4) listarray (aa);
(%o4) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]


(%i5) arrayinfo (aa);
(%o5)                 [declared, 2, [2, 3]]
```


未宣言(ハッシュド)配列に適用された`listarray`と`arrayinfo`。









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) listarray (bb);
                              3         2
(%o3)                 [(c - d) , (b + a) ]


(%i4) arrayinfo (bb);
(%o4)               [hashed, 1, [BAR], [FOO]]
```


配列関数に適用された`listarray`と`arrayinfo`。










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) listarray (cc);
                              z  v
(%o4)                        [-, -]
                              4  u


(%i5) arrayinfo (cc);
(%o5)              [hashed, 2, [4, z], [u, v]]
```


添字付き関数に適用された`listarray`と`arrayinfo`。










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) listarray (dd);
                         b + a                v - u
(%o4)      [lambda([y], y     ), lambda([y], y     )]


(%i5) arrayinfo (dd);
(%o5)             [hashed, 1, [b + a], [v - u]]
```

See also: `orderless`, `arrayinfo`.

<!-- category: Programming -->
<!-- keywords: listp -->
<!-- signatures: listp(expr) -->
### Function: listp (expr)

もし *expr*がリストなら `true`、
そうでなければ `false`を返します。

<!-- category: Programming -->
<!-- keywords: make_array -->
<!-- signatures: make_array(type, dim_1, ..., dim_n) -->
### Function: make_array (type, dim_1, ..., dim_n)

Lisp配列を生成し、返します。
*type*は、`any`, `flonum`, `fixnum`, `hashed`, 
`functional`を取り得ます。
$n$個のインデックスがあり、
$i$番目のインデックスは0から$dim_i - 1$まで動きます。


`make_array`の`array`に対する利点は、
戻り値が名前を持たないことであり、
一旦、それへのポインタが消えると、それも消えます。
例えば、もし`y: make_array (...)`なら、
`y`は領域を取るオブジェクトを指しますが、
`y: false`の後、`y`はそのオブジェクトをもはや指さないので、
オブジェクトはガーベッジコレクトされることができます。











例:

















```maxima
(%i1) A1 : make_array (fixnum, 10);
(%o1)           {Array:  #(0 0 0 0 0 0 0 0 0 0)}


(%i2) A1 [8] : 1729;
(%o2)                         1729


(%i3) A1;
(%o3)          {Array:  #(0 0 0 0 0 0 0 0 1729 0)}


(%i4) A2 : make_array (flonum, 10);
(%o4) {Array:  #(0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i5) A2 [2] : 2.718281828;
(%o5)                      2.718281828


(%i6) A2;
(%o6) 
     {Array:  #(0.0 0.0 2.718281828 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i7) A3 : make_array (any, 10);
(%o7) {Array:  #(NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL)}


(%i8) A3 [4] : x - y - z;
(%o8)                      - z - y + x


(%i9) A3;
(%o9) {Array:  #(NIL NIL NIL NIL ((MPLUS SIMP) $X ((MTIMES SIMP)\
 -1 $Y) ((MTIMES SIMP) -1 $Z))
  NIL NIL NIL NIL NIL)}


(%i10) A4 : make_array (fixnum, 2, 3, 5);
(%o10) {Array:  #3A(((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0)) ((0 0 \
0 0 0) (0 0 0 0 0) (0 0 0 0 0)))}


(%i11) fillarray (A4, makelist (i, i, 1, 2*3*5));
(%o11) {Array:  #3A(((1 2 3 4 5) (6 7 8 9 10) (11 12 13 14 15))
    ((16 17 18 19 20) (21 22 23 24 25) (26 27 28 29 30)))}


(%i12) A4 [0, 2, 1];
(%o12)                         12
```

See also: `array`.

<!-- category: Programming -->
<!-- keywords: makelist -->
<!-- signatures: makelist(expr, i, i_0, i_1), makelist(expr, x, list) -->
### Function: makelist (expr, i, i_0, i_1)

要素それぞれが *expr*から生成されたリストを構成し、返します。


`makelist (expr, i, i_0, i_1)`は、
*i_0*から *i_1*に等しい `j`に対して
`j`番目の要素が `ev (expr, i=j)`に等しい
リストを返します。


`makelist (expr, x, list)`は、
1から `length (list)`に等しい `j`に対して、
`j`番目の要素が `ev (expr, x=list[j])`に等しい
リストを返します。


例:







```maxima
(%i1) makelist(concat(x,i),i,1,6);
(%o1)               [x1, x2, x3, x4, x5, x6]
(%i2) makelist(x=y,y,[a,b,c]);
(%o2)                 [x = a, x = b, x = c]
```

<!-- category: Programming -->
<!-- keywords: member -->
<!-- signatures: member(expr_1, expr_2) -->
### Function: member (expr_1, expr_2)

もし
`args(expr_2)`の中のある要素*a*に対して
`is(expr_1 = a)`なら
`true`を返し、
そうでなければ `false`を返します。


`expr_2`は通常リストです。
その場合、 `args(expr_2) = expr_2`かつ
`expr_2`の中のある要素 *a*に対して、
`is(expr_1 = a)`であることがテストです。


`member`は
`expr_2`の引数の部分を検査しません。
だから、
たとえ `expr_1`が `expr_2`のある引数の部分であっても
`false`を返すかもしれません。


`elementp`も参照してください。


例:













```maxima
(%i1) member (8, [8, 8.0, 8b0]);
(%o1)                         true
(%i2) member (8, [8.0, 8b0]);
(%o2)                         false
(%i3) member (b, [a, b, c]);
(%o3)                         true
(%i4) member (b, [[a, b], [b, c]]);
(%o4)                         false
(%i5) member ([b, c], [[a, b], [b, c]]);
(%o5)                         true
(%i6) F (1, 1/2, 1/4, 1/8);
                               1  1  1
(%o6)                     F(1, -, -, -)
                               2  4  8
(%i7) member (1/8, %);
(%o7)                         true
(%i8) member ("ab", ["aa", "ab", sin(1), a + b]);
(%o8)                         true
```

See also: `elementp`.

<!-- category: Programming -->
<!-- keywords: minf -->
<!-- signatures: minf -->
### Variable: minf

`minf`は実数のマイナスの（すなわち負の）無限大を表します。

<!-- category: Programming -->
<!-- keywords: new -->
<!-- signatures: new(S), new(S(v_1, ..., v_n)) -->
### Function: new (S)

`new`は構造体の新しいインスタンスを生成します。


`new(S)`は
構造体*S*の新しいインスタンスを生成します。
それぞれのフィールドは、もしデフォルト値があればデフォルト値を割り当てられ、
もしデフォルト値が構造体定義で指定されなかったなら、割り当てなしになります。


`new(S(v_1, ..., v_n))`は
フィールドが値*v_1*, ..., *v_n*に割り当てられた
構造体*S*の新しいインスタンスを生成します。


例:








```maxima
(%i1) defstruct (foo (w, x = %e, y = 42, z));
(%o1)              [foo(w, x = %e, y = 42, z)]
(%i2) new (foo);
(%o2)               foo(w, x = %e, y = 42, z)
(%i3) new (foo (1, 2, 4, 8));
(%o3)            foo(w = 1, x = 2, y = 4, z = 8)
```

<!-- category: Programming -->
<!-- keywords: ninth -->
<!-- signatures: ninth(expr) -->
### Function: ninth (expr)

式またはリスト *expr*の9番目の項を返します。
詳細は `first`を参照してください。

<!-- category: Programming -->
<!-- keywords: pop -->
<!-- signatures: pop(list) -->
### Function: pop (list)

`pop`は、リスト *list*から最初の要素を取り除き、この要素を返します。
*list*はリストそのものではなく、リストにバインドされたシンボルでなければいけません。


もし引数 *list*がリストにバインドされていないかリストが空なら、
Maximaはエラーメッセージを生成します。


例には `push`も参照してください。


`load("basic")`はこの関数をロードします。

See also: `push`.

<!-- category: Programming -->
<!-- keywords: push -->
<!-- signatures: push(item, list) -->
### Function: push (item, list)

`push`は項目 *item*をリスト *list*の先頭に追加し、
新しいリストのコピーを返します。
*list*はリストそのものではなく、リストにバインドされたシンボルでなければいけません。
*item*は任意のMaximaシンボルや式が使えます。


もし引数 *list*がリストにバインドされていないかリストが空なら、
Maximaはエラーメッセージを生成します。


リストから最初の項目を取り除くには `pop`も参照してください。


`load("basic")`はこの関数をロードします。


例:














```maxima
(%i1) ll:[];
(%o1)                          []
(%i2) push(x,ll);
(%o2)                          [x]
(%i3) push(x^2+y,ll);
                                 2
(%o3)                      [y + x , x]
(%i4) a:push("string",ll);
                                     2
(%o4)                  [string, y + x , x]
(%i5) pop(ll);
(%o5)                        string
(%i6) pop(ll);
                                  2
(%o6)                        y + x
(%i7) pop(ll);
(%o7)                           x
(%i8) ll;
(%o8)                          []
(%i9) a;
                                     2
(%o9)                  [string, y + x , x]
```

See also: `pop`.

<!-- category: Programming -->
<!-- keywords: rearray -->
<!-- signatures: rearray(A, dim_1, ..., dim_n) -->
### Function: rearray (A, dim_1, ..., dim_n)

配列の次元を変えます。
新しい配列は
行優先順に古いものの配列で埋められます。
もし古い配列が小さすぎるなら、
残りの要素は、
配列のタイプに依って、
`false`, `0.0`または`0`で埋められます。
配列のタイプは変えられません。

<!-- category: Programming -->
<!-- keywords: remarray -->
<!-- signatures: remarray(A_1, ..., A_n), remarray(all) -->
### Function: remarray (A_1, ..., A_n)

配列と関数に関連づけられた配列を削除し、占められた領域を開放します。
引数は、宣言配列、未宣言(ハッシュド)配列、配列関数、添字付き関数を取り得ます。


`remarray (all)`は、
グローバルリスト`arrays`の中の項目すべてを削除します。



もしハッシュド配列の中の値を再定義することが望ましいなら、この関数を使うことが必要になるかもしれません。


`remarray`は削除された配列のリストを返します。


`remarray`はクォートします。

See also: `arrays`.

<!-- category: Programming -->
<!-- keywords: rest -->
<!-- signatures: rest(expr, n), rest(expr) -->
### Function: rest (expr, n)

もし *n*が正なら、
頭の *n*個の要素を取り除いた
*expr*を返し、
もし *n*が負なら、
お尻の `- n`個の要素を取り除いた
*expr*を返します。
もし *n*が1なら、省略できます。
*expr*は、リスト、行列、他の式を取り得ます。

<!-- category: Programming -->
<!-- keywords: reverse -->
<!-- signatures: reverse(list) -->
### Function: reverse (list)

*list* のメンバーの順序を逆にします。
(メンバー自身は変えません。)
 `reverse`は、一般式でも機能します。
例えば、 `reverse(a=b);`は `b=a`を与えます。

<!-- category: Programming -->
<!-- keywords: second -->
<!-- signatures: second(expr) -->
### Function: second (expr)

式またはリスト *expr*の二番目の項を返します。
詳細は `first`を参照してください。

See also: `first`.

<!-- category: Programming -->
<!-- keywords: seventh -->
<!-- signatures: seventh(expr) -->
### Function: seventh (expr)

式またはリスト *expr*の7番目の項を返します。
詳細は `first`を参照してください。

See also: `first`.

<!-- category: Programming -->
<!-- keywords: sixth -->
<!-- signatures: sixth(expr) -->
### Function: sixth (expr)

式またはリスト *expr*の6番目の項を返します。
詳細は `first`を参照してください。

See also: `first`.

<!-- category: Programming -->
<!-- keywords: sort -->
<!-- signatures: sort(L, P), sort(L) -->
### Function: sort (L, P)

任意の隣り合う要素について`P (L[k], L[k + 1])`が`true`
になるように
２つの引数の述語論理`P`に従ってリスト*L*をソートします。
述語論理は関数や２値中値演算子の名前として、`lambda`式として指定されるかもしれません。
もし演算子名として指定されたなら、名前は「ダブルクォート」でくくられます。


ソートされたリストは新しいオブジェクトとして返されます;
*L*は変更されません。
戻り値を構成するために、
`sort`は、*L*の要素の浅いコピーを実行します。




もし述語論理*P*が*L*の要素の総順序でなければ、
`sort`は、エラーなしに実行を完了するかもしれませんが、結果は未定義です。
もし述語論理が`true`もしくは`false`以外の何かに評価されるなら、
`sort`はエラーを出力します。


`sort (L)`は `sort (L, orderlessp)`と同値です。
すなわち、デフォルトソート順序は昇順です。`orderlessp`で決められているように。


述語論理`ordergreatp`はリストを降順にソートします。
述語論理`ordermagnitudep`はMaxima数や数値を持つ定数シンボル、
定数に評価されることができる式を大きさによってソートします。
リスト*L*の他のすべての要素は`orderlessp`によってソートされます。
述語論理`"<"`も大きさによる順序付けを許しますが、
もしリスト*L*の要素が`"<"`の下で比較可能でないなら完全には並べません。


例:















```maxima
(%i1) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9 * c,
      19 - 3 * x]);
               5
(%o1) [- 17, - -, 3, 7.55, 11, 2.9b1, b + a, 9 c, 19 - 3 x]
               2
(%i2) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9*c, 19 - 3*x],
      ordergreatp);
                                                   5
(%o2) [19 - 3 x, 9 c, b + a, 2.9b1, 11, 7.55, 3, - -, - 17]
                                                   2
(%i3) sort ([%pi, 3, 4, %e, %gamma]);
(%o3)                [3, 4, %e, %gamma, %pi]
(%i4) sort ([%pi, 3, 4, %e, %gamma], "<");
(%o4)                [%gamma, %e, 3, %pi, 4]
(%i5) my_list: [[aa,hh,uu], [ee,cc], [zz,xx,mm,cc], [%pi,%e]];
(%o5) [[aa, hh, uu], [ee, cc], [zz, xx, mm, cc], [%pi, %e]]
(%i6) sort (my_list);
(%o6) [[%pi, %e], [aa, hh, uu], [ee, cc], [zz, xx, mm, cc]]

(%i7) sort (my_list, lambda ([a, b], orderlessp (reverse (a),
      reverse (b))));

(%o7) [[%pi, %e], [ee, cc], [zz, xx, mm, cc], [aa, hh, uu]]
```


Maxima数と定数、定数式を大きさ順に並べ、他のすべての要素を降順で並べます:







```maxima
(%i8) sort([%i,1+%i,2*x,minf,inf,%e,sin(1),0,1,2,3,1.0,1.0b0],
      ordermagnitudep);
(%o8)  [minf, 0, sin(1), 1, 1.0, 1.0b0, 2, %e, 3, inf, %i, 
                                                      %i + 1, 2 x]
```

See also: `orderlessp`.

<!-- category: Programming -->
<!-- keywords: structures -->
<!-- signatures: structures -->
### Variable: structures

`structures`は
`defstruct`で定義されたユーザー定義の構造体のリストです。

<!-- category: Programming -->
<!-- keywords: sublist -->
<!-- signatures: sublist(list, p) -->
### Function: sublist (list, p)

述語論理`p`が`true`を返す*list*の要素のリストを返します。


例:







```maxima
(%i1) L: [1, 2, 3, 4, 5, 6];
(%o1)                  [1, 2, 3, 4, 5, 6]
(%i2) sublist (L, evenp);
(%o2)                       [2, 4, 6]
```

<!-- category: Programming -->
<!-- keywords: sublist_indices -->
<!-- signatures: sublist_indices(L, P) -->
### Function: sublist_indices (L, P)

述語論理 `maybe(P(x))`が `true`を返す、
リスト *L*の要素 `x`のインデックスを返します;
これは `false`はもちろん `unknown`も除外します。
*P*は関数名かラムダ式を取り得ます。
*L*はリストリテラルでなければいけません。


例:













```maxima
(%i1) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b],
                       lambda ([x], x='b));
(%o1)                     [2, 3, 7, 9]
(%i2) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], symbolp);
(%o2)                  [1, 2, 3, 4, 7, 9]
(%i3) sublist_indices ([1 > 0, 1 < 0, 2 < 1, 2 > 1, 2 > 0],
                       identity);
(%o3)                       [1, 4, 5]
(%i4) assume (x < -1);
(%o4)                       [x < - 1]
(%i5) map (maybe, [x > 0, x < 0, x < -2]);
(%o5)                [false, true, unknown]
(%i6) sublist_indices ([x > 0, x < 0, x < -2], identity);
(%o6)                          [2]
```

<!-- category: Programming -->
<!-- keywords: subvar -->
<!-- signatures: subvar(x, i) -->
### Function: subvar (x, i)

添字付き式`x[i]`を評価します。


`subvar`は引数を評価します。


`arraymake (x, [i]`は
式`x[i]`を構成しますが、
それを評価はしません。


例:












```maxima
(%i1) x : foo $
(%i2) i : 3 $

(%i3) subvar (x, i);
(%o3)                         foo
                                 3

(%i4) foo : [aa, bb, cc, dd, ee]$

(%i5) subvar (x, i);
(%o5)                          cc


(%i6) arraymake (x, [i]);
(%o6)                         foo
                                 3


(%i7) ''%;
(%o7)                          cc
```

<!-- category: Programming -->
<!-- keywords: subvarp -->
<!-- signatures: subvarp(expr) -->
### Function: subvarp (expr)

もし*expr*が例えば`a[i]`のように添字された変数なら、`true`を返します。

<!-- category: Programming -->
<!-- keywords: tenth -->
<!-- signatures: tenth(expr) -->
### Function: tenth (expr)

式またはリスト *expr*の10番目の項を返します。
詳細は `first`を参照してください。

<!-- category: Programming -->
<!-- keywords: third -->
<!-- signatures: third(expr) -->
### Function: third (expr)

式またはリスト *expr*の三番目の項を返します。
詳細は `first`を参照してください。

<!-- category: Programming -->
<!-- keywords: true -->
<!-- signatures: true -->
### Variable: true

`true`は同じ名前のブーリアン定数を表します。
MaximaはLispの値`T`で`true`を実装しています。

<!-- category: Programming -->
<!-- keywords: und -->
<!-- signatures: und -->
### Variable: und

`und`は未定義の結果を表します。


`limit`も参照してください。


例:






```maxima
(%i1) limit (x*sin(x), x, inf);
(%o1)                          und
```

See also: `limit`.

<!-- category: Programming -->
<!-- keywords: unique -->
<!-- signatures: unique(L) -->
### Function: unique (L)

リスト *L*の重複しない要素を返します。


*L*の要素すべてが重複しない時、
`unique`は、
*L*自身ではなく、
*L*の浅いコピーを返します。


もし *L*がリストでないなら、
`unique`は*L*を返します。


例:






```maxima
(%i1) unique ([1, %pi, a + b, 2, 1, %e, %pi, a + b, [1]]);
(%o1)              [1, 2, %e, %pi, [1], b + a]
```

<!-- category: Programming -->
<!-- keywords: use_fast_arrays -->
<!-- signatures: use_fast_arrays -->
### Variable: use_fast_arrays

もし`true`なら、配列の２つのタイプだけが認識されます:



1. 整数でインデックスされたいくつかの次元を持つができ、
情報入力としてLispまたはMaximaオブジェクトを保てるart-q配列(Common Lispでのt)。
そんな配列を構成するには、
`a:make_array(any,3,4);`を入力してください。
`a`は、12個の枠を持つ配列を値として持ち、インデックスはゼロベースです
2. もし`b[x+1]:y^2`を実行したら、生成された配列のデフォルト値でハッシュテーブル配列
(`b`はまだ配列でもリストでも行列でもありません –
もしこれらの１つなら、`x+1`は、art-q配列やリスト、行列の有効な添字ではないので
、エラーが起こります。)
(キーとしても知られている)インデックスは、任意のオブジェクトを取り得ます。
一度の１つのキーだけを取ります((`b[x+1,u]:y`は`u`を無視します。)。
参照は、`b[x+1] ==> y^2`によってされます。
もちろん、キーは、例えば、
`b[[x+1,u]]:y`が有効なように
リストを取り得ます。
これは古いMaximaハッシュ配列と非互換ですが、コンシングを保ちます。


配列をシンボルの値として記憶することの利点は、
関数のローカル変数についての普通の慣例が配列にも適用することです。
ハッシュテーブルタイプは、
Maximaハッシャの古いタイプよりも
少ないコンシングを使い、もっと効率的です。
翻訳され、コンパイルされたコードに関する一貫した振る舞いを得るためには、
`translate_fast_arrays`を`true`に設定してください。

<!-- category: Programming -->
<!-- keywords: zeroa -->
<!-- signatures: zeroa -->
### Variable: zeroa

`zeroa`はゼロの上の無限小を表します。
`zeroa`は式の中で使うことができます。
`limit`は無限小を含む式を整理します。


`zerob`と`limit`も参照してください。


例:


`limit`は無限小を含む式を整理します:







```maxima
(%i1) limit(zeroa);
(%o1)                           0
(%i2) limit(x+zeroa);
(%o2)                           x
```

See also: `zerob`, `limit`.

<!-- category: Programming -->
<!-- keywords: zerob -->
<!-- signatures: zerob -->
### Variable: zerob

`zerob`はゼロの下の無限小を表します。
`zerob`は式の中で使うことができます。
`limit`は無限小を含む式を整理します。


`zeroa`と`limit`も参照してください。

See also: `zeroa`, `limit`.

