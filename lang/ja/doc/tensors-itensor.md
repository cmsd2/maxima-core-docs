## itensor

<!-- category: Tensors -->
<!-- keywords: allsym -->
<!-- signatures: allsym -->
### Variable: allsym

デフォルト: `false`。
もし`true`なら、すべての添字付きオブジェクトは共変、反変添字のすべてに関して対称と仮定されます。
もし`false`なら、これらの添字に関して、いかなる種類の対称性も仮定されません。
`iframe_flag`が`true`に設定されない限り、
微分添字はいつも対称と取られます。

<!-- category: Tensors -->
<!-- keywords: canform -->
<!-- signatures: canform(expr), canform(expr, rename) -->
### Function: canform (expr)

ダミー添字をリネームして、
それらに課せられた対称条件によって指令されたようにすべての添字を並べ替えることで、
*expr*を整理します。
もし`allsym`が`true`なら、
すべての添字は対称と仮定され、
そうでなければ、`decsym`宣言が提供する対称情報が使われます。
ダミー添字は`rename`関数に関するものと同じ方法でリネームされます。
`canform`が大きな式に適用される時、
計算にかなりの時間が費やされるかもしれません。
この時間は最初に式に対して`rename`をコールすることで短くできます。
`decsym`の下の例も参照してください。
注意: `canform`は
いつも数学的に正しい結果を返しますが、
式を最も簡単な形式に完全に整理できないかもしれません。


オプションの二番目のパラメータ*rename*は、
もし`false`に設定されたなら、リネームを抑制します。

<!-- category: Tensors -->
<!-- keywords: canten -->
<!-- signatures: canten(expr) -->
### Function: canten (expr)

名前を変えて(`rename`を参照してください)、ダミー添字を置換することで、
*expr*を整理します。
`rename`は
微分がないテンソル積の和に制限されます。
本当に限定されていて、
もし`canform`が要求された整理を実行する能力がない時だけ使われるはずです。


`canten`関数は、
引数が添字が完全に対称な式の時だけ数学的に正確な結果を返します。
この理由から、`canten`は、
もし`allsym`が`true`に設定されてないなら
エラーを返します。

<!-- category: Tensors -->
<!-- keywords: changename -->
<!-- signatures: changename(old, new, expr) -->
### Function: changename (old, new, expr)

*expr*の中の*old*と呼ばれるすべての添字付きオブジェクトの名前を*new*に変えます。
*old*はシンボルまたは形式`[name, m, n]`のリストであり得ます。
後者の場合、*m*個の共変添字と*n*個の反変添字を持つ
*name*と呼ばれるそれらの添字付きオブジェクトだけが*new*にリネームされます。

<!-- category: Tensors -->
<!-- keywords: components -->
<!-- signatures: components(tensor, expr) -->
### Function: components (tensor, expr)

*tensor*の成分の値を与える式*expr*に添字値を割り当てることを許します。
その添字のすべてとともに起こるときはいつでも、これらは自動的にテンソルに代入されます。
テンソルは、形式`t([...],[...])`でなければいけません。
ここで形式`t([...],[...])`の中のリストのいずれかは空であり得えます。
*expr*は、
*tensor*と同じ自由添字を持つ他のオブジェクトを含む任意の添字付き式であり得ます。
成分がダミー添字を含む計量テンソルへ値を割り当てるのに使われる時、
複数のダミー添字の生成を避けるようにこれらの添字を定義するように注意しなければいけません。
この割り当ての削除は関数`remcomps`に与えられます。


It is important to keep in mind that 
`components`はテンソル価についてだけ知る必要があり、特別な添字順序について知る必要がないことを覚えておくことは重要です。
このように、成分を、例えば、`x([i,-j],[])`, `x([-j,i],[])`または
`x([i],[j])`すべてに割り当てることは、同じ結果、
すなわち、
価`(1,1)`を持つ`x`と名付けられたテンソルに割り当てられた
成分を生成します。


成分を、4つの方法で添字付き式に割り当てることができます。
そのうちの2つは`components`コマンドの使用を含みます:


1) 添字付き式として。例えば:



```maxima
(%i2) components(g([],[i,j]),e([],[i])*p([],[j]))$
(%i3) ishow(g([],[i,j]))$
                                      i  j
(%t3)                                e  p
```


2) 行列として:



```maxima
(%i5) lg:-ident(4)$lg[1,1]:1$lg;

                            [ 1   0    0    0  ]
                            [                  ]
                            [ 0  - 1   0    0  ]
(%o5)                       [                  ]
                            [ 0   0   - 1   0  ]
                            [                  ]
                            [ 0   0    0   - 1 ]

(%i6) components(g([i,j],[]),lg);
(%o6)                                done
(%i7) ishow(g([i,j],[]))$
(%t7)                                g
                                      i j
(%i8) g([1,1],[]);
(%o8)                                  1
(%i9) g([4,4],[]);
(%o9)                                 - 1
```


3) 関数として。Maxima関数を使って、添字に基づいたテンソルの成分を指定することができます。
例えば、以下のコードは、
もし`h`が同じ数の共変添字と反変添字を持ち、微分添字を持たないなら、`kdelta`を`h`に割り当て、そうでなければ、`g`を割り当てます:



```maxima
(%i4) h(l1,l2,[l3]):=if length(l1)=length(l2) and length(l3)=0
  then kdelta(l1,l2) else apply(g,append([l1,l2], l3))$
(%i5) ishow(h([i],[j]))$
                                          j
(%t5)                               kdelta
                                          i
(%i6) ishow(h([i,j],[k],l))$
                                     k
(%t6)                               g
                                     i j,l
```


4) Maximaのパターンマッチング機能、特に`defrule`と`applyb1`コマンド
を使って:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) matchdeclare(l1,listp);
(%o2)                                done
(%i3) defrule(r1,m(l1,[]),(i1:idummy(),
      g([l1[1],l1[2]],[])*q([i1],[])*e([],[i1])))$

(%i4) defrule(r2,m([],l1),(i1:idummy(),
      w([],[l1[1],l1[2]])*e([i1],[])*q([],[i1])))$

(%i5) ishow(m([i,n],[])*m([],[i,m]))$

                                    i m
(%t5)                              m    m
                                         i n

(%i6) ishow(rename(applyb1(%,r1,r2)))$
                           %1  %2  %3 m
(%t6)                     e   q   w     q   e   g
                                         %1  %2  %3 n
```

<!-- category: Tensors -->
<!-- keywords: concan -->
<!-- signatures: concan(expr) -->
### Function: concan (expr)

`canten`に似ていますが、添字縮約も実行します。

<!-- category: Tensors -->
<!-- keywords: conmetderiv -->
<!-- signatures: conmetderiv(expr, tensor) -->
### Function: conmetderiv (expr, tensor)

計量テンソルの共変と反変形式両方(現在の制約)の常微分を含む式を整理します。
例えば、 以下に見られるように、
`conmetderiv`は
反変計量テンソルの微分をChristoffelシンボルに結びつけます:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(g([],[a,b],c))$
                                      a b
(%t2)                                g
                                      ,c
(%i3) ishow(conmetderiv(%,g))$
                         %1 b      a       %1 a      b
(%t3)                 - g     ichr2     - g     ichr2
                                   %1 c              %1 c
```

<!-- category: Tensors -->
<!-- keywords: contract -->
<!-- signatures: contract(expr) -->
### Function: contract (expr)

和と積の任意の組み合わせであり得る
*expr*に関して
テンソル縮約を実行します。
この関数は
`defcon`関数に与えられた情報を使います。
最高の結果として、
`expr`は完全に展開されなければいけません。
もし項の分母の中に変数がないなら、
`ratexpand`は
和の積やべきを展開する
最速の方法です。
もしGCD消去が不要なら、
`gcd`スイッチは`false`でなければいけません。

<!-- category: Tensors -->
<!-- keywords: coord -->
<!-- signatures: coord(tensor_1, tensor_2, ...) -->
### Function: coord (tensor_1, tensor_2, ...)

*tensor_i*に、
その名前が*tensor_i*の1つである反変ベクトルの微分がKroneckerデルタをもたらす
座標微分プロパティを与えます。
例えば、
もし `coord(x)`が実行されたら、
`idiff(x([],[i]),j)`は `kdelta([i],[j])`を与えます。
`coord`はこのプロパティを持つ添字付きオブジェクトすべてのリストです。

<!-- category: Tensors -->
<!-- keywords: covdiff -->
<!-- signatures: covdiff(expr, v_1, v_2, ...) -->
### Function: covdiff (expr, v_1, v_2, ...)

第二種Christoffel記号(`ichr2`)を使って、
変数 *v_i*に対する
*expr*の共変微分をもたらします。
これらを評価するには、
`ev(expr,ichr2)`を使わなければ行けません。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the covariant indices: [i,j];
Enter a list of the contravariant indices: [k];
Enter a list of the derivative indices: [];
                                      k
(%t2)                                a
                                      i j
(%i3) ishow(covdiff(%,s))$
             k         %1     k         %1     k
(%t3)     - a     ichr2    - a     ichr2    + a
             i %1      j s    %1 j      i s    i j,s

             k     %1
      + ichr2     a
             %1 s  i j
(%i4) imetric:g;
(%o4)                                  g
(%i5) ishow(ev(%th(2),ichr2))$
         %1 %4  k
        g      a     (g       - g       + g      )
                i %1   s %4,j    j s,%4    j %4,s
(%t5) - ------------------------------------------
                            2

    %1 %3  k
   g      a     (g       - g       + g      )
           %1 j   s %3,i    i s,%3    i %3,s
 - ------------------------------------------
                       2
    k %2  %1
   g     a    (g        - g        + g       )
          i j   s %2,%1    %1 s,%2    %1 %2,s     k
 + ------------------------------------------- + a
                        2                         i j,s

(%i6)
```

<!-- category: Tensors -->
<!-- keywords: decsym -->
<!-- signatures: decsym(tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...]) -->
### Function: decsym (tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...])

*m*個の共変添字と*n*個の反変添字を持つ*tensor*に関する
対称プロパティを宣言します。
*cov_i*と*contr_i*は
それぞれ、共変添字と反変添字の間の対称関係を表す擬似関数です。
これらは
contravariant indices respectively.  These are of the form
形式`symoper(index_1, index_2,...)`を取ります。
ここで`symoper`は
`sym`, `anti`もしくは`cyc`のいずれかで、
 and the 
*index_i*は
*tensor*の添字の位置を示す整数です。
これは、*tensor*が*index_i*に関してそれぞれ対称、反対称、巡回であると宣言します。
`symoper(all)`も対称条件に従う添字すべてを示す有効な形式です。
例えば、
5つの共変添字を持つオブジェクト`b`が与えられたとして、
`decsym(b,5,3,[sym(1,2),anti(3,4)],[cyc(all)])`は、
`b`が一番目と二番目の共変添字に対して対称であり、三番目、四番目の共変添字に対して反対称であり、反変添字すべてに対して巡回的であると宣言します。
対称宣言のリストのどれかは空であり得ます。
式整理を実行する関数は
以下の例で示すように`canform`です。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:contract( expand( a([i1, j1, k1], [])
           *kdels([i, j, k], [i1, j1, k1])))$
(%i3) ishow(expr)$

(%t3)         a      + a      + a      + a      + a      + a
               k j i    k i j    j k i    j i k    i k j    i j k

(%i4) decsym(a,3,0,[sym(all)],[]);
(%o4)                                done
(%i5) ishow(canform(expr))$
(%t5)                              6 a
                                      i j k
(%i6) remsym(a,3,0);
(%o6)                                done
(%i7) decsym(a,3,0,[anti(all)],[]);
(%o7)                                done
(%i8) ishow(canform(expr))$
(%t8)                                  0
(%i9) remsym(a,3,0);
(%o9)                                done
(%i10) decsym(a,3,0,[cyc(all)],[]);
(%o10)                               done
(%i11) ishow(canform(expr))$
(%t11)                        3 a      + 3 a
                                 i k j      i j k
(%i12) dispsym(a,3,0);
(%o12)                     [[cyc, [[1, 2, 3]], []]]
```

<!-- category: Tensors -->
<!-- keywords: defcon -->
<!-- signatures: defcon(tensor_1), defcon(tensor_1, tensor_2, tensor_3) -->
### Function: defcon (tensor_1)

*tensor_1*に、
*tensor_1*と*tensor_2*の積の縮約が
適切な添字を持つ*tensor_3*に帰着するという
プロパティを与えます。
もし引数が*tensor_1*１つだけ与えれたなら、
, then the contraction of the product of 
適切な添字を持つ任意の添字付きオブジェクト(`my_tensor`とします)との*tensor_1*の積の縮約はその名前、すなわち、`my_tensor`と、実行された縮約を反映した添字の新しい集合を持つ添字付きオブジェクトをもたらします。
例えば、もし`imetric:g`なら、`defcon(g)`は
計量テンソルとの縮約を通して添字の上げ下げを実行します。
１つ以上の`defcon`を同じ添字付きオブジェクトに関して与えることができます;
特定の縮約に関して適用する最新のものが使われます。
`contractions`は、
`defcon`で縮約プロパティを与えられたそれら添字付きオブジェクトのリストです。

<!-- category: Tensors -->
<!-- keywords: dispcon -->
<!-- signatures: dispcon(tensor_1, tensor_2, ...), dispcon(all) -->
### Function: dispcon (tensor_1, tensor_2, ...)

`defcon`に与えられたような引数の縮約プロパティを表示します。
`dispcon (all)`は、定義された縮約プロパティすべてを表示します。

<!-- category: Tensors -->
<!-- keywords: entertensor -->
<!-- signatures: entertensor(name) -->
### Function: entertensor (name)

プロンプトによって、
任意の数のテンソル添字や微分添字を持つ*name*と呼ばれる添字付きオブジェクトを生成することを許す関数です。
単一添字または(nullもありえる)添字のリストが容認可能な入力です。
(`covdiff`の下の例を参照してください。)

<!-- category: Tensors -->
<!-- keywords: evundiff -->
<!-- signatures: evundiff(expr) -->
### Function: evundiff (expr)

`undiff`の実行と同値ですが、`ev`と `rediff`が続きます。


この演算のポイントは
微分形式で直接評価できない式を簡単に評価することです。
例えば、以下はエラーをもたらします:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) icurvature([i,j,k],[l],m);
Maxima encountered a Lisp error:

 Error in $ICURVATURE [or a callee]:
 $ICURVATURE [or a callee] requires less than three arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```


しかし、もし `icurvature`は名詞形で入っているなら、
`evundiff`を使って評価できます:



```maxima
(%i3) ishow('icurvature([i,j,k],[l],m))$
                                         l
(%t3)                          icurvature
                                         i j k,m
(%i4) ishow(evundiff(%))$
             l              l         %1           l           %1
(%t4) - ichr2        - ichr2     ichr2      - ichr2       ichr2
             i k,j m        %1 j      i k,m        %1 j,m      i k

             l              l         %1           l           %1
      + ichr2        + ichr2     ichr2      + ichr2       ichr2
             i j,k m        %1 k      i j,m        %1 k,m      i j
```


注意: Maximaの以前のバージョンでは、
Christoffel記号の微分形式も評価できませんでした。
これは現在修正されています。
だから `evundiff`はもはやこのような式に関しては不要です:



```maxima
(%i5) imetric(g);
(%o5)                                done
(%i6) ishow(ichr2([i,j],[k],l))$
       k %3
      g     (g         - g         + g        )
              j %3,i l    i j,%3 l    i %3,j l
(%t6) -----------------------------------------
                          2

                         k %3
                        g     (g       - g       + g      )
                         ,l     j %3,i    i j,%3    i %3,j
                      + -----------------------------------
                                         2
```

<!-- category: Tensors -->
<!-- keywords: extdiff -->
<!-- signatures: extdiff(expr, i) -->
### Function: extdiff (expr, i)

添字 *i*に対する
*expr*の外積を計算します。
外微分は形式的に
偏微分演算子のウェッジ積で微分形式として定義されます。
そんなように、
演算子も
`igeowedge_flag`の設定で制御されます。
例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(extdiff(v([i]),j))$
                                  v    - v
                                   j,i    i,j
(%t2)                             -----------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(extdiff(a([i,j]),k))$
                           a      - a      + a
                            j k,i    i k,j    i j,k
(%t4)                      ------------------------
                                      3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(extdiff(v([i]),j))$
(%t6)                             v    - v
                                   j,i    i,j
(%i7) ishow(extdiff(a([i,j]),k))$
(%t7)                    - (a      - a      + a     )
                             k j,i    k i,j    j i,k
```

<!-- category: Tensors -->
<!-- keywords: flipflag -->
<!-- signatures: flipflag -->
### Variable: flipflag

デフォルト: `false`.
もし`false`なら反変添字の順に従って、
そうでなければ、共変添字の順に従って、
添字がリネームされます。


もし`flipflag`が`false`なら、
`rename`は
左から右に現れるよう反変添字のリストを形成します
(もし`true`なら共変添字について同様に)。
リストの最初のダミー添字は`%1`に、次は`%2`にというように、リネームされます。
そして、`rename`の後、並び替えが起こります。
(`rename`の下の例を参照してください。)

<!-- category: Tensors -->
<!-- keywords: flush -->
<!-- signatures: flush(expr, tensor_1, tensor_2, ...) -->
### Function: flush (expr, tensor_1, tensor_2, ...)

*expr*において、
微分添字を持たない *tensor_i*をすべて0にします。

<!-- category: Tensors -->
<!-- keywords: flush1deriv -->
<!-- signatures: flush1deriv(expr, tensor) -->
### Function: flush1deriv (expr, tensor)

*expr*において、
微分添字を1つだけ持つ *tensor*をすべて0にします。

<!-- category: Tensors -->
<!-- keywords: flushd -->
<!-- signatures: flushd(expr, tensor_1, tensor_2, ...) -->
### Function: flushd (expr, tensor_1, tensor_2, ...)

*expr*において、
微分添字を持つ *tensor_i*をすべて0にします。

<!-- category: Tensors -->
<!-- keywords: flushnd -->
<!-- signatures: flushnd(expr, tensor, n) -->
### Function: flushnd (expr, tensor, n)

以下の例で例示されるように、
*expr*において、
*n*以上の微分添字を持つ微分されたオブジェクト *tensor*をすべて0にします。


```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i],[J,r],k,r)+a([i],[j,r,s],k,r,s))$
                                J r      j r s
(%t2)                          a      + a
                                i,k r    i,k r s
(%i3) ishow(flushnd(%,a,3))$
                                     J r
(%t3)                               a
                                     i,k r
```

<!-- category: Tensors -->
<!-- keywords: hodge -->
<!-- signatures: hodge(expr) -->
### Function: hodge (expr)

*expr*のHodge双対を計算します。
例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                            done
(%i3) idim(4);
(%o3)                            done
(%i4) icounter:100;
(%o4)                             100
(%i5) decsym(A,3,0,[anti(all)],[])$

(%i6) ishow(A([i,j,k],[]))$
(%t6)                           A
                                 i j k
(%i7) ishow(canform(hodge(%)))$
                          %1 %2 %3 %4
               levi_civita            g        A
                                       %1 %102  %2 %3 %4
(%t7)          -----------------------------------------
                                   6
(%i8) ishow(canform(hodge(%)))$
                 %1 %2 %3 %8            %4 %5 %6 %7
(%t8) levi_civita            levi_civita            g       
                                                     %1 %106
                             g        g        g      A         /6
                              %2 %107  %3 %108  %4 %8  %5 %6 %7
(%i9) lc2kdt(%)$

(%i10) %,kdelta$

(%i11) ishow(canform(contract(expand(%))))$
(%t11)                     - A
                              %106 %107 %108
```

<!-- category: Tensors -->
<!-- keywords: ic_convert -->
<!-- signatures: ic_convert(eqn) -->
### Function: ic_convert (eqn)

`itensor`方程式 *eqn*を
`ctensor`割り当て文に変換します。
添字付きオブジェクトが配列に変換される一方で、
ダミー添字上の暗黙の和は明示的にされます。


(配列下付き添字は添字付きオブジェクトの反変添字が続く共変の順です。)
添字付きオブジェクトの微分は、
微分添字で下に添えられた `ct_coords`に対して取られる `diff`の名詞形に
置き換えられます。
Christoffel記号 `ichr1`と `ichr2`は
それぞれ、`lcs`と `mcs`に翻訳されます。
もし `metricconvert`が `true`なら、
2つの共変(反変)添字を持つ計量はすべて
`lg` (`ug`)にリネームされます。
更に、 自由添字すべての上で足される`do`ループが導入されます。
なので、
ただ `ev`するだけで
変換される割り当て分を評価することができます。
以下の例はこの関数の特長を例示します。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) eqn:ishow(t([i,j],[k])=f([],[])*g([l,m],[])*a([],[m],j)
      *b([i],[l,k]))$
                             k        m   l k
(%t2)                       t    = f a   b    g
                             i j      ,j  i    l m
(%i3) ic_convert(eqn);
(%o3) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 g    , l, 1, dim), m, 1, dim)))
  l, m
(%i4) imetric(g);
(%o4)                                done
(%i5) metricconvert:true;
(%o5)                                true
(%i6) ic_convert(eqn);
(%o6) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 lg    , l, 1, dim), m, 1, dim)))
   l, m
```

<!-- category: Tensors -->
<!-- keywords: icc1 -->
<!-- signatures: icc1 -->
### Variable: icc1

第一種接続係数。
`itensor`では、以下のように定義されます。



```maxima
icc1    = ichr1    - ikt1    - inmc1
    abc        abc       abc        abc
```


この式では、
もし `iframe_flag`が trueなら、
Christoffel記号 `ichr1`が
標構接続係数 `ifc1`に置き換えられます。
もし `itorsion_flag`が `false`なら、
 `ikt1`は省略されます。
もし標構基底が使われるなら、
ねじれが標構ブラケットの一部として既に計算されているので、
その時にも `ikt1`は省略されます。
最後に、
`inonmet_flag`が `false`なら、
`inmc1`は存在しません。

<!-- category: Tensors -->
<!-- keywords: icc2 -->
<!-- signatures: icc2 -->
### Variable: icc2

第二種接続係数。
`itensor`では、以下のように定義されます。



```maxima
c         c        c         c
icc2   = ichr2   - ikt2   - inmc2
    ab        ab       ab        ab
```


この式では、
もし `iframe_flag`が trueなら、
Christoffel記号 `ichr2`が
標構接続係数 `ifc2`に置き換えられます。
もし `itorsion_flag`が `false`なら、
 `ikt2`は省略されます。
もし標構基底が使われるなら、
ねじれが標構ブラケットの一部として既に計算されているので、
その時にも `ikt1`は省略されます。
最後に、
`inonmet_flag`が `false`なら、
`inmc1`は存在しません。

<!-- category: Tensors -->
<!-- keywords: ichr1 -->
<!-- signatures: ichr1([i, j, k]) -->
### Function: ichr1 ([i, j, k])

以下の定義を介して第一種Christoffel記号をもたらします。


```maxima
(g      + g      - g     )/2 .
         ik,j     jk,i     ij,k
```


特定の計量で Christoffel記号を評価するには、
`chr2`の下の例のように
変数 `imetric`が名前を割り当てられなければいけません。

<!-- category: Tensors -->
<!-- keywords: ichr2 -->
<!-- signatures: ichr2([i, j], [k]) -->
### Function: ichr2 ([i, j], [k])

以下の定義を介して第二種Christoffel記号をもたらします。


```maxima
ks
   ichr2([i,j],[k]) = g    (g      + g      - g     )/2
                             is,j     js,i     ij,s
```

<!-- category: Tensors -->
<!-- keywords: icounter -->
<!-- signatures: icounter -->
### Variable: icounter

デフォルト値: `1`


テンソルパッケージで次のダミー添字を生成する際使われる数値接尾を決定します。
接頭辞はオプション`idummy` (デフォルト: `%`)で決定されます。

<!-- category: Tensors -->
<!-- keywords: icurvature -->
<!-- signatures: icurvature([i, j, k], [h]) -->
### Function: icurvature ([i, j, k], [h])

第二種Christoffel記号(`ichr2`)を使った
Riemann曲率テンソルをもたらします。
以下の表記法が使われます:


```maxima
h             h            h         %1         h
  icurvature     = - ichr2      - ichr2     ichr2    + ichr2
            i j k         i k,j        %1 j      i k        i j,k
                            h          %1
                     + ichr2      ichr2
                            %1 k       i j
```

<!-- category: Tensors -->
<!-- keywords: idiff -->
<!-- signatures: idiff(expr, v_1, [n_1, [v_2, n_2]...]) -->
### Function: idiff (expr, v_1, [n_1, [v_2, n_2]...])

添字微分。
独立変数に関して微分する`diff`と異なり、
`idiff)`は座標に関して微分するのにつかうことができます。
添字付きオブジェクトに関して，
結果的に、これは
*v_i*を微分添字として追加することになります。
`iframe_flag`が `true`に設定されていない限り
続いて，微分添字が並び替えられます。


`idiff`は計量テンソルの行列式も微分することができます。
従って、もし `imetric`が
`G`にバインドされていたら、
`idiff(determinant(g),k)`は
ダミー添字 `%i`が適当に選ばれて
`2 * determinant(g) * ichr2([%i,k],[%i])`を返します。

<!-- category: Tensors -->
<!-- keywords: idim -->
<!-- signatures: idim(n) -->
### Function: idim (n)

計量の次元を設定します。
与えられた次元でLevi-Civita記号の反対称プロパティも初期化します。

<!-- category: Tensors -->
<!-- keywords: idummy -->
<!-- signatures: idummy() -->
### Function: idummy ()

Increments 
`icounter`を1つ増やし、
形式`%n`の添字を値として返します。ここでnは正の整数です。
これは式を形成する際必要なダミー添字が既に使用中の添字とぶつからないことを保証します。
(`indices`の下の例を参照してください。)

<!-- category: Tensors -->
<!-- keywords: idummyx -->
<!-- signatures: idummyx -->
### Variable: idummyx

デフォルト値: `%`


ダミー添字の接頭辞です。
(`indices`の下の例を参照してください。)

<!-- category: Tensors -->
<!-- keywords: ifb -->
<!-- signatures: ifb -->
### Variable: ifb

標構ブラケット(frame bracket)。
標構計量の接続係数への寄与が標構ブラケットを使って表されます:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                  2
```


標構ブラケット自身は
標枠と標構計量を使って定義されます。
`frame_bracket_form`の値に依存して
2つの代わりの計算方法が使われます。
もし true (デフォルト)か、もし `itorsion_flag`が `true`なら:



```maxima
d      e                                      f
ifb =  ifr    ifr   (ifri      - ifri      - ifri    itr   )
   abc    b      c       a d,e       a e,d       a f    d e
```


そうでないなら:



```maxima
e      d        d      e
ifb    = (ifr    ifr    - ifr    ifr   ) ifri
   abc       b      c,e      b,e    c        a d
```

<!-- category: Tensors -->
<!-- keywords: ifc1 -->
<!-- signatures: ifc1 -->
### Variable: ifc1

(Ricci回転係数としても知られている)第一種標構係数。
このテンソルは
標構計量の第一種接続係数への寄与を表します。
以下のように定義されます:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                   2
```

<!-- category: Tensors -->
<!-- keywords: ifc2 -->
<!-- signatures: ifc2 -->
### Variable: ifc2

第二種標構係数。
このテンソルは標構計量の第一種接続係数への寄与を表します。
必要に応じて、標構ブラケット (`ifb`)の、
適切な上付き、下付き添字での置換として定義されます:



```maxima
c       cd
ifc2   = ifg   ifc1
    ab             abd
```

<!-- category: Tensors -->
<!-- keywords: ifg -->
<!-- signatures: ifg -->
### Variable: ifg

標構計量。
`kdelta`のデフォルトですが、
`components`を使って変えることができます。

<!-- category: Tensors -->
<!-- keywords: ifgi -->
<!-- signatures: ifgi -->
### Variable: ifgi

逆標構計量。
標構計量 (`ifg`)を `kdelta`に縮約します。

<!-- category: Tensors -->
<!-- keywords: ifr -->
<!-- signatures: ifr -->
### Variable: ifr

標枠。
標構計量(`ifg`)を形成するために
逆標構場 (`ifri`)を
縮約します。

<!-- category: Tensors -->
<!-- keywords: iframe_bracket_form -->
<!-- signatures: iframe_bracket_form -->
### Variable: iframe_bracket_form

デフォルト値: `true`


標構ブラケット (`ifb`)が如何に計算されるか指定します。

<!-- category: Tensors -->
<!-- keywords: iframes -->
<!-- signatures: iframes() -->
### Function: iframes ()

Maximaのこのバージョン以来、
`ifr`と `ifri`に関する縮約恒等式がいつも定義されます。
as is the frame bracket (`ifb`), 
この関数は何もしません。

<!-- category: Tensors -->
<!-- keywords: ifri -->
<!-- signatures: ifri -->
### Variable: ifri

逆標構場。
(双対基底ベクトル)標構基底を指定します。
標構計量と一緒に、
標構に基づいた計算すべての基底を形成します。

<!-- category: Tensors -->
<!-- keywords: igeodesic_coords -->
<!-- signatures: igeodesic_coords(expr, name) -->
### Function: igeodesic_coords (expr, name)

*expr*内の、未微分 Christoffel記号と
計量テンソルの一階微分を消すようにします。
`igeodesic_coords`関数での *name*は
(もし *expr*)の中で現れるなら)
計量 *name*を参照します。
一方で、接続係数は
名前 `ichr1`か `ichr2`でコールされなければいけません。
以下の例は、
`igeodesic_coords`関数を使った、
Riemann曲率テンソルが満たす巡回恒等式の検証を例示します。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(icurvature([r,s,t],[u]))$
             u            u         %1         u     
(%t2) - ichr2      - ichr2     ichr2    + ichr2      
             r t,s        %1 s      r t        r s,t 

                                              u         %1
                                       + ichr2     ichr2
                                              %1 t      r s
(%i3) ishow(igeodesic_coords(%,ichr2))$
                                 u            u
(%t3)                       ichr2      - ichr2
                                 r s,t        r t,s
(%i4) ishow(igeodesic_coords(icurvature([r,s,t],[u]),ichr2)+
            igeodesic_coords(icurvature([s,t,r],[u]),ichr2)+
            igeodesic_coords(icurvature([t,r,s],[u]),ichr2))$
             u            u            u            u
(%t4) - ichr2      + ichr2      + ichr2      - ichr2
             t s,r        t r,s        s t,r        s r,t

                                             u            u
                                      - ichr2      + ichr2
                                             r t,s        r s,t
(%i5) canform(%);
(%o5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: igeowedge_flag -->
<!-- signatures: igeowedge_flag -->
### Variable: igeowedge_flag

デフォルト値: `false`


ウェッジ積と外微分の振る舞いを制御します。
`false` (デフォルト)に設定された時、
微分形式の概念は
完全反対称共変テンソル場のそれに対応します。
`true`に設定された時、
微分形式は容積要素の概念に一致します。

<!-- category: Tensors -->
<!-- keywords: ikt1 -->
<!-- signatures: ikt1 -->
### Variable: ikt1

(コントーションとしても知られる)ねじれテンソルの共変置換。
以下のように定義されます:



```maxima
d           d       d
          -g   itr  - g    itr   - itr   g
            ad    cb    bd    ca      ab  cd
ikt1    = ----------------------------------
    abc                   2
```


(もし標構計量を使うなら、`ifg`を `g`に代入します。)

<!-- category: Tensors -->
<!-- keywords: ikt2 -->
<!-- signatures: ikt2 -->
### Variable: ikt2

(コントーションとしても知られる)ねじれテンソルの共変置換。
以下のように定義されます:



```maxima
c     cd
ikt2   = g   ikt1
    ab           abd
```


(もし標構計量を使うなら、`ifg`を `g`に代入します。)

<!-- category: Tensors -->
<!-- keywords: imetric -->
<!-- signatures: imetric(g) -->
### Function: imetric (g)

変数 `imetric:g`を割り当てることで計量を指定します。
加えて、
コマンド `defcon(g),defcon(g, g, kdelta)`を実行することで
計量 *g*の縮約プロパティが設定されます。
(デフォルトではバインドされていない)変数 `imetric`は
`imetric(g)`コマンドが割り当てる計量にバインドされます。

<!-- category: Tensors -->
<!-- keywords: indexed_tensor -->
<!-- signatures: indexed_tensor(tensor) -->
### Function: indexed_tensor (tensor)

値に関する美しい姿が既に
`ichr1`, `ichr2`, `icurvature`とともにあるように存在する
*tensor*に成分を割り当てる前に実行されなければいけません。
`icurvature`の下の例を参照してください。

<!-- category: Tensors -->
<!-- keywords: indices -->
<!-- signatures: indices(expr) -->
### Function: indices (expr)

2つの要素のリストを返します。
以下の例が例示するように、
一番目は、*expr*の中の自由添字(一度だけ現れるもの)のリストです。
二番目は、*expr*の中のダミー添字(正確に二回現れるもの)のリストです。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i,j],[k,l],m,n)*b([k,o],[j,m,p],q,r))$
                                k l      j m p
(%t2)                          a        b
                                i j,m n  k o,q r
(%i3) indices(%);
(%o3)                 [[l, p, i, n, o, q, r], [k, j, m]]
```


同じ添字を二回以上含むテンソル積は構文的に認められていません。
`indices`は、これらの式を合理的な方法で扱おうとします;
しかしながら、そんな非合法な式上で動くようにコールされた時、その振る舞いは未定義と考えなければいけません。

<!-- category: Tensors -->
<!-- keywords: inm -->
<!-- signatures: inm -->
### Variable: inm

非計量性ベクトル。
共形非計量性は計量テンソルの共変微分を通して定義されます。
`inonmet_flag`が `true`に設定されている時
通常零の計量テンソルの共変微分は以下のように評価されます:



```maxima
g     =- g  inm
 ij;k     ij   k
```

<!-- category: Tensors -->
<!-- keywords: inmc1 -->
<!-- signatures: inmc1 -->
### Variable: inmc1

非計量ベクトル成分の共変置換。
以下のように定義されます:



```maxima
g   inm  - inm  g   - g   inm
            ab    c      a  bc    ac    b
inmc1    = ------------------------------
     abc                 2
```


(もし標構計量を使うなら、`ifg`を `g`に代入します。)

<!-- category: Tensors -->
<!-- keywords: inmc2 -->
<!-- signatures: inmc2 -->
### Variable: inmc2

非計量ベクトル成分の反変置換。
もし `inonmet_flag`が `true`なら
接続係数で使われます。
以下のように定義されます:



```maxima
c         c         cd
          -inm  kdelta  - kdelta  inm  + g   inm  g
     c        a       b         a    b          d  ab
inmc2   = -------------------------------------------
     ab                        2
```


(もし標構計量を使うなら、`ifg`を `g`に代入します。)

<!-- category: Tensors -->
<!-- keywords: ishow -->
<!-- signatures: ishow(expr) -->
### Function: ishow (expr)

下付き添字としての共変添字と上付き添字としての反変添字を持つように
添字付きオブジェクトを持つ形で*expr*を表示します。
微分添字は、共変添字からコンマで区切られた下付き添字として表示されます。
(このドキュメント至る所の例を参照してください。)

<!-- category: Tensors -->
<!-- keywords: itr -->
<!-- signatures: itr -->
### Variable: itr

ねじれテンソル。
以下の例で例示されるように、
ねじれを伴う計量に関してスカラー関数上の繰り返される共変微分は計算されません:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric:g;
(%o2)                                  g
(%i3) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i4) ishow(%)$
                                   %4              %2
(%t4)                    f    ichr2    - f    ichr2
                          ,%4      j i    ,%2      i j
(%i5) canform(%);
(%o5)                                  0
(%i6) itorsion_flag:true;
(%o6)                                true
(%i7) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i8) ishow(%)$
                           %8             %6
(%t8)             f    icc2    - f    icc2    - f     + f
                   ,%8     j i    ,%6     i j    ,j i    ,i j
(%i9) ishow(canform(%))$
                                   %1             %1
(%t9)                     f    icc2    - f    icc2
                           ,%1     j i    ,%1     i j
(%i10) ishow(canform(ev(%,icc2)))$
                                   %1             %1
(%t10)                    f    ikt2    - f    ikt2
                           ,%1     i j    ,%1     j i
(%i11) ishow(canform(ev(%,ikt2)))$
                      %2 %1                    %2 %1
(%t11)          f    g      ikt1       - f    g      ikt1
                 ,%2            i j %1    ,%2            j i %1
(%i12) ishow(factor(canform(rename(expand(ev(%,ikt1))))))$
                           %3 %2            %1       %1
                     f    g      g      (itr    - itr   )
                      ,%3         %2 %1     j i      i j
(%t12)               ------------------------------------
                                      2
(%i13) decsym(itr,2,1,[anti(all)],[]);
(%o13)                               done
(%i14) defcon(g,g,kdelta);
(%o14)                               done
(%i15) subst(g,nounify(g),%th(3))$
(%i16) ishow(canform(contract(%)))$
                                           %1
(%t16)                           - f    itr
                                    ,%1    i j
```

<!-- category: Tensors -->
<!-- keywords: kdels -->
<!-- signatures: kdels(L1, L2) -->
### Function: kdels (L1, L2)

いくつかの計算で使われる、対称化されたKroneckerデルタ。
例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) kdelta([1,2],[2,1]);
(%o2)                                 - 1
(%i3) kdels([1,2],[2,1]);
(%o3)                                  1
(%i4) ishow(kdelta([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  - kdelta  kdelta
                             a       b         a       b
(%i4) ishow(kdels([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  + kdelta  kdelta
                             a       b         a       b
```

<!-- category: Tensors -->
<!-- keywords: kdelta -->
<!-- signatures: kdelta(L1, L2) -->
### Function: kdelta (L1, L2)

共変添字のリスト*L1*と反変添字のリスト*L2*を使って
`itensor`パッケージで定義された
一般化されたKroneckerのデルタ関数です。
`kdelta([i],[j])`は通常のKroneckerデルタを返します。
コマンド`ev(expr,kdelta)`は
`kdelta([],[])`を多様体の次元に含む
式の評価をもたらします。


この表記法の乱用となることですが、
`itensor`は
`kdelta`が2つの共変添字だけ、または、2つの反変添字だけを持つことも許し、
事実上、共(反)変「単位行列」を供給します。
これは厳密にはプログラミング目的としてみなされ、
`kdelta([i,j],[])`が有効なテンソルオブジェクトだということを意味するつもりではありません。

<!-- category: Tensors -->
<!-- keywords: lc2kdt -->
<!-- signatures: lc2kdt(expr) -->
### Function: lc2kdt (expr)

Levi-Civitaシンボルを含む式を整理し、可能ならこれらをKroneckerデルタ式に変換します。
この関数と単にLevi-Civitaシンボルを評価することの主な違いは、
直接評価はしばしば数値添字を含むKronecker式に帰着することです。
これは、更なる整理を妨げるので、しばしば望ましくないことです。
`lc2kdt`関数はこの問題を避けて、
`rename`や`contract`を使って更に容易に整理される式をもたらします。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([k,l],[])*a([j],[k]))$
                                  i j  k
(%t2)                  levi_civita    a  levi_civita
                                       j            k l
(%i3) ishow(ev(expr,levi_civita))$
                                  i j  k       1 2
(%t3)                       kdelta    a  kdelta
                                  1 2  j       k l
(%i4) ishow(ev(%,kdelta))$
             i       j         j       i   k
(%t4) (kdelta  kdelta  - kdelta  kdelta ) a
             1       2         1       2   j

                               1       2         2       1
                        (kdelta  kdelta  - kdelta  kdelta )
                               k       l         k       l
(%i5) ishow(lc2kdt(expr))$
                     k       i       j    k       j       i
(%t5)               a  kdelta  kdelta  - a  kdelta  kdelta
                     j       k       l    j       k       l
(%i6) ishow(contract(expand(%)))$
                                 i           i
(%t6)                           a  - a kdelta
                                 l           l
```


`lc2kdt`関数は時々計量テンソルを利用します。
もし前もって計量テンソルが`imetric`で定義されていなかったなら、
これはエラーになります。



```maxima
(%i7) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([],[k,l])*a([j,k],[]))$

                                 i j            k l
(%t7)                 levi_civita    levi_civita    a
                                                     j k

(%i8) ishow(lc2kdt(expr))$
Maxima encountered a Lisp error:

 Error in $IMETRIC [or a callee]:
 $IMETRIC [or a callee] requires less than two arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i9) imetric(g);
(%o9)                                done
(%i10) ishow(lc2kdt(expr))$
         %3 i       k   %4 j       l     %3 i       l   %4 j
(%t10) (g     kdelta   g     kdelta   - g     kdelta   g    
                    %3             %4               %3
              k
        kdelta  ) a
              %4   j k
(%i11) ishow(contract(expand(%)))$
                                  l i    l i  j
(%t11)                           a    - g    a
                                              j
```

<!-- category: Tensors -->
<!-- keywords: lc_l -->
<!-- signatures: lc_l -->
### Function: lc_l

未評価のLevi-Civitaシンボル(`levi_civita`)を含む式のために使われる整理ルール。
`lc_u`と組み合わせて、
たくさんの式を、`levi_civita`の評価より、より効率的に整理するのに使うことができます。


例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) el1:ishow('levi_civita([i,j,k],[])*a([],[i])*a([],[j]))$
                             i  j
(%t2)                       a  a  levi_civita
                                             i j k
(%i3) el2:ishow('levi_civita([],[i,j,k])*a([i])*a([j]))$
                                       i j k
(%t3)                       levi_civita      a  a
                                              i  j
(%i4) canform(contract(expand(applyb1(el1,lc_l,lc_u))));
(%t4)                                  0
(%i5) canform(contract(expand(applyb1(el2,lc_l,lc_u))));
(%t5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: lc_u -->
<!-- signatures: lc_u -->
### Function: lc_u

未評価のLevi-Civitaシンボル(`levi_civita`)を含む式のために使われる整理ルール。
`lc_l`と組み合わせて、
たくさんの式を、`levi_civita`の評価より、より効率的に整理するのに使うことができます。
詳しくは、`lc_l`を参照してください。

<!-- category: Tensors -->
<!-- keywords: levi_civita -->
<!-- signatures: levi_civita(L) -->
### Function: levi_civita (L)

もしリスト*L*が整数の偶置換から成るなら1を返し、
*L*が奇置換なら成るなら-1を返し、
*L*のいくつかの添字が繰り返しなら0を返す
置換(別名Levi-Civita)テンソルです。

<!-- category: Tensors -->
<!-- keywords: liediff -->
<!-- signatures: liediff(v, ten) -->
### Function: liediff (v, ten)

ベクトル場 *v*に対してテンソル式 *ten*のLie微分を計算します。
*ten*は任意の添字付きテンソル式でなければいけません;
*v*はベクトル場の(添字なしの)名前でなければいけません。
例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(liediff(v,a([i,j],[])*b([],[k],l)))$
       k    %2            %2          %2
(%t2) b   (v   a       + v   a     + v   a    )
       ,l       i j,%2    ,j  i %2    ,i  %2 j

                          %1  k        %1  k      %1  k
                      + (v   b      - b   v    + v   b   ) a
                              ,%1 l    ,l  ,%1    ,l  ,%1   i j
```

<!-- category: Tensors -->
<!-- keywords: listoftens -->
<!-- signatures: listoftens -->
### Function: listoftens

テンソル式の中のすべてのテンソルを添字が完備した形でリストします。
例えば、



```maxima
(%i6) ishow(a([i,j],[k])*b([u],[],v)+c([x,y],[])*d([],[])*e)$
                                         k
(%t6)                        d e c    + a    b
                                  x y    i j  u,v
(%i7) ishow(listoftens(%))$
                               k
(%t7)                        [a   , b   , c   , d]
                               i j   u,v   x y
```

<!-- category: Tensors -->
<!-- keywords: lorentz_gauge -->
<!-- signatures: lorentz_gauge(expr) -->
### Function: lorentz_gauge (expr)

反変添字と同一の微分添字を持つ *expr*の中で
添字付きオブジェクトすべてに0を代入することで、
Lorentz条件を課します。

<!-- category: Tensors -->
<!-- keywords: makebox -->
<!-- signatures: makebox(expr) -->
### Function: makebox (expr)

`show`と同じように *expr*を表示します;
しかし、
*expr*に現れるテンソル d’Alembert演算子はすべて記号 `[]`を使って示されます。
例えば、 `[]p([m],[n])`は
`g([],[i,j])*p([m],[n],i,j)`を表します。

<!-- category: Tensors -->
<!-- keywords: rediff -->
<!-- signatures: rediff(ten) -->
### Function: rediff (ten)

テンソル式 *ten*の中の`idiff`コマンドすべてを評価します。

<!-- category: Tensors -->
<!-- keywords: remcomps -->
<!-- signatures: remcomps(tensor) -->
### Function: remcomps (tensor)

`components`関数で割り当てられたすべての値を
*tensor*からアンバインドします。

<!-- category: Tensors -->
<!-- keywords: remcon -->
<!-- signatures: remcon(tensor_1, ..., tensor_n), remcon(all) -->
### Function: remcon (tensor_1, ..., tensor_n)

*tensor_1*, ..., *tensor_n*からすべての縮約プロパティを取り除きます。
`remcon(all)`は、すべての添字付きオブジェクトから
すべての縮約プロパティを取り除きます。

<!-- category: Tensors -->
<!-- keywords: remcoord -->
<!-- signatures: remcoord(tensor_1, tensor_2, ...), remcoord(all) -->
### Function: remcoord (tensor_1, tensor_2, ...)

`tensor_i`から
関数 `coord`がもたらした座標微分プロパティを削除します。
`remcoord(all)`は添字付きオブジェクトすべてからこのプロパティを削除します。

<!-- category: Tensors -->
<!-- keywords: remsym -->
<!-- signatures: remsym(tensor, m, n) -->
### Function: remsym (tensor, m, n)

*m*個の共変添字と*n*個の反変添字を持つ*tensor*から
すべての対称プロパティを取り除きます。

<!-- category: Tensors -->
<!-- keywords: rename -->
<!-- signatures: rename(expr), rename(expr, count) -->
### Function: rename (expr)

もしオプションの二番目の引数が省略されたら、
*expr*と同値な、
しかし、各項に対して、集合`[%1, %2,...]`から選ばれたダミー添字を持つ式を返します。
そうでなければ、ダミー添字は*count*の値で始まるようインデックスされます。
積の中のそれぞれのダミー添字は異なります。
和に関しては、`rename`は各項毎にカウンタが再設定されるように和の中の各項上で作用します。
この方法で、`rename`はテンソル整理器として利用できます。
加えて、
(もし`allsym`が`true`なら、)
添字は、
`flipflag`の値に依存して共変または反変添字に関して、
英数字順に並び替えられます。
もし`flipflag`が`false`なら、
添字は反変添字の順に従ってリネームされます。
もし`flipflag`が`true`なら、
リネームは共変添字の順に従って起こるでしょう。
２つのリネームの組み合わせた効果が、それ自身によって、
どちらか１つよりも更に式を簡単にすることがしばしば起こります。



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) allsym:true;
(%o2)                                true
(%i3) g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%4],[%3])*
ichr2([%2,%3],[u])*ichr2([%5,%6],[%1])*ichr2([%7,r],[%2])-
g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%2],[u])*
ichr2([%3,%5],[%1])*ichr2([%4,%6],[%3])*ichr2([%7,r],[%2]),noeval$
(%i4) expr:ishow(%)$

       %4 %5  %6 %7      %3         u          %1         %2
(%t4) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %4      %2 %3      %5 %6      %7 r

        %4 %5  %6 %7      u          %1         %3         %2
     - g      g      ichr2      ichr2      ichr2      ichr2
                          %1 %2      %3 %5      %4 %6      %7 r

(%i5) flipflag:true;
(%o5)                                true
(%i6) ishow(rename(expr))$
       %2 %5  %6 %7      %4         u          %1         %3
(%t6) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %2      %3 %4      %5 %6      %7 r

        %4 %5  %6 %7      u          %1         %3         %2
     - g      g      ichr2      ichr2      ichr2      ichr2
                          %1 %2      %3 %4      %5 %6      %7 r
(%i7) flipflag:false;
(%o7)                                false
(%i8) rename(%th(2));
(%o8)                                  0
(%i9) ishow(rename(expr))$
       %1 %2  %3 %4      %5         %6         %7        u
(%t9) g      g      ichr2      ichr2      ichr2     ichr2
                         %1 %6      %2 %3      %4 r      %5 %7

        %1 %2  %3 %4      %6         %5         %7        u
     - g      g      ichr2      ichr2      ichr2     ichr2
                          %1 %3      %2 %6      %4 r      %5 %7
```

<!-- category: Tensors -->
<!-- keywords: show -->
<!-- signatures: show(expr) -->
### Function: show (expr)

下付き添字として共変インデックス、上付き添字として反変インデックスを持つよう、
インデックスされたオブジェクトと一緒に`expr`を表示します。
微分インデックスは下付き添字として表示され、
コンマによって共変インデックスと区別されます。

<!-- category: Tensors -->
<!-- keywords: showcomps -->
<!-- signatures: showcomps(tensor) -->
### Function: showcomps (tensor)

`components`コマンドを使って作られたように
テンソルの成分割り当てを表示します。
以下の例で明示されるように、
行列が、`components`を使って
添字テンソルに割り当てられている時、
この関数は特に役に立ちます:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) load("itensor");
(%o2)      /share/tensor/itensor.lisp
(%i3) lg:matrix([sqrt(r/(r-2*m)),0,0,0],[0,r,0,0],
                [0,0,sin(theta)*r,0],[0,0,0,sqrt((r-2*m)/r)]);
               [         r                                     ]
               [ sqrt(-------)  0       0              0       ]
               [      r - 2 m                                  ]
               [                                               ]
               [       0        r       0              0       ]
(%o3)          [                                               ]
               [       0        0  r sin(theta)        0       ]
               [                                               ]
               [                                      r - 2 m  ]
               [       0        0       0        sqrt(-------) ]
               [                                         r     ]
(%i4) components(g([i,j],[]),lg);
(%o4)                                done
(%i5) showcomps(g([i,j],[]));
                  [         r                                     ]
                  [ sqrt(-------)  0       0              0       ]
                  [      r - 2 m                                  ]
                  [                                               ]
                  [       0        r       0              0       ]
(%t5)      g    = [                                               ]
            i j   [       0        0  r sin(theta)        0       ]
                  [                                               ]
                  [                                      r - 2 m  ]
                  [       0        0       0        sqrt(-------) ]
                  [                                         r     ]
(%o5)                                false
```


`showcomps`コマンドは
2よりも高い階数のテンソルの成分も表示することができます。

<!-- category: Tensors -->
<!-- keywords: simpmetderiv -->
<!-- signatures: simpmetderiv(expr), simpmetderiv(expr[, stop]) -->
### Function: simpmetderiv (expr)

計量テンソルの微分の積を含む式を整理します。
特に、 `simpmetderiv`は2つの恒等式を知っています:



```maxima
ab        ab           ab                 a
  g   g   + g   g     = (g   g  )   = (kdelta )   = 0
   ,d  bc        bc,d         bc ,d          c ,d
```


従って、



```maxima
ab          ab
  g   g   = - g   g
   ,d  bc          bc,d
```


と



```maxima
ab          ab
 g   g     = g   g
  ,j  ab,i    ,i  ab,j
```


これはChristoffel記号の対称性の結果です。


`simpmetderiv`関数はオプションパラメータを1つ取ります。
それは、与えられた時、
積式の中の最初にうまくいった代入の後、関数が停止するようにします。
`simpmetderiv`関数は
“正準”順序を積添字に適用する方法を決めるグローバル変数 *flipflag*も利用します。


まとめると、
これらの機能は
そうでなければ遂行困難か不可能な強力な式整理を達成するのに使うことができます。
これは、
縮約式を得るために`simpmetderiv`の部分的な整理の特長を明示的に使う
以下の例を通じて例示されます:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                                done
(%i3) ishow(g([],[a,b])*g([],[b,c])*g([a,b],[],d)*g([b,c],[],e))$
                             a b  b c
(%t3)                       g    g    g      g
                                       a b,d  b c,e
(%i4) ishow(canform(%))$

errexp1 has improper indices
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) ishow(simpmetderiv(%))$
                             a b  b c
(%t5)                       g    g    g      g
                                       a b,d  b c,e
(%i6) flipflag:not flipflag;
(%o6)                                true
(%i7) ishow(simpmetderiv(%th(2)))$
                               a b  b c
(%t7)                         g    g    g    g
                               ,d   ,e   a b  b c
(%i8) flipflag:not flipflag;
(%o8)                                false
(%i9) ishow(simpmetderiv(%th(2),stop))$
                               a b  b c
(%t9)                       - g    g    g      g
                                    ,e   a b,d  b c
(%i10) ishow(contract(%))$
                                    b c
(%t10)                           - g    g
                                    ,e   c b,d
```


Weylテンソルの縮約を整理するために
`simpmetderiv`と `conmetderiv`を一緒に使う例として、
`weyl.dem`も参照してください。

<!-- category: Tensors -->
<!-- keywords: tentex -->
<!-- signatures: tentex(expr) -->
### Function: tentex (expr)

以下の例のように、
`tentex`関数を使うには、
最初に`tentex`をロードしなければいけません:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) load("tentex");
(%o2)       /share/tensor/tentex.lisp
(%i3) idummyx:m;
(%o3)                                  m
(%i4) ishow(icurvature([j,k,l],[i]))$
            m1       i           m1       i           i
(%t4)  ichr2    ichr2     - ichr2    ichr2     - ichr2
            j k      m1 l        j l      m1 k        j l,k

                                                      i
                                               + ichr2
                                                      j k,l
(%i5) tentex(%)$
$$\Gamma_{j\,k}^{m_1}\,\Gamma_{l\,m_1}^{i}-\Gamma_{j\,l}^{m_1}\,
 \Gamma_{k\,m_1}^{i}-\Gamma_{j\,l,k}^{i}+\Gamma_{j\,k,l}^{i}$$
```


コンパイルエラーに導かれるTeX式でのパーセント符号の出現を避けるための、
`idummyx`割り当ての使用に注意してください。


注意せよ: このバージョンの`tentex`関数は幾分実験的です。

<!-- category: Tensors -->
<!-- keywords: undiff -->
<!-- signatures: undiff(expr) -->
### Function: undiff (expr)

*expr*と同値な、
添字付きオブジェクトの微分すべてが`idiff`関数の名詞形で置き換えられた
式を返します。
引数はもし微分が実行されていたらその添字付きオブジェクトをもたらします。
微分された添字付きオブジェクトを
*expr*を生じるある関数定義で置き換えて、
`ev(expr, idiff)`で微分を実行したい時、
これは役に立ちます。

<!-- category: Tensors -->
<!-- keywords: | -->
<!-- signatures: | -->
### Variable: |

縦線 `|`は
"ベクトルの縮約"二項演算子を示します。
完全反対称共変テンソルが反変ベクトルと縮約される時、
結果は、どの添字が縮約に使われるかに関わらず同じです。
このように、
添字に無関係な方法で縮約演算子を定義することが可能です。


`itensor`パッケージでは、
ベクトルとの縮約は常に
文字通りの並べ順で最初の添字に対して実行されます。
これは
`|`演算子を含む式のより良い整理を保証します。
例えば:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) decsym(a,2,0,[anti(all)],[]);
(%o2)                                done
(%i3) ishow(a([i,j],[])|v)$
                                    %1
(%t3)                              v   a
                                        %1 j
(%i4) ishow(a([j,i],[])|v)$
                                     %1
(%t4)                             - v   a
                                         %1 j
```


`|`演算子で使われるテンソルは
は共変添字に対して完全反対称と宣言されなければいけないことが
本質的であることに注意してください。
そうでないなら、結果は正しくありません。

<!-- category: Tensors -->
<!-- keywords: ~ -->
<!-- signatures: ~ -->
### Variable: ~

ウェッジ積演算子は
ティルデ `~`で示されれます。
これは二項演算子です。
引数は、
スカラ、階数1の共変テンソル、
共変添字すべてに関して反対称と宣言された階数 `l`の共変テンソルを含む式
でなければいけません。


以下の例のように、
ウェッジ積演算子の振る舞いは
`igeowedge_flag`
フラグで制御されます:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i])~b([j]))$
                                 a  b  - b  a
                                  i  j    i  j
(%t2)                            -------------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(a([i,j])~b([k]))$
                          a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
(%t4)                     ---------------------------
                                       3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(a([i])~b([j]))$
(%t6)                            a  b  - b  a
                                  i  j    i  j
(%i7) ishow(a([i,j])~b([k]))$
(%t7)                     a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
```

