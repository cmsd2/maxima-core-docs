## augmented_lagrangian

<!-- category: Other -->
<!-- keywords: augmented_lagrangian_method -->
<!-- signatures: augmented_lagrangian_method(FOM, xx, C, yy), augmented_lagrangian_method(FOM, xx, C, yy, optional_args), augmented_lagrangian_method([FOM, grad], xx, C, yy), augmented_lagrangian_method([FOM, grad], xx, C, yy, optional_args) -->
### Function: augmented_lagrangian_method (FOM, xx, C, yy)

ゼロに等しい制約*C*を保ちながら、
式*FOM*の変数*xx*に関する近似最小を返します。
*yy*は
*xx*の初期推量のリストです。
利用した方法は拡張Lagrange法です。(文献[1]と[2]を参照してください。)


もしあるなら、*grad*は
*FOM*の*xx*に関するグラディエントであり、
*xx*の変数それぞれに関する式のリストとして表されます。
もしないなら、グラディエントは自動的に構成されます。


*FOM*と、もしあるなら*grad*の要素それぞれは、
関数名やラムダ式ではなく、通常の式でなければいけません。


`optional_args`は、
`symbol = value`として指定される、
追加の引数を表します。
認識されるオプション引数は以下の通りです:



**niter** — 拡張Lagrangeアルゴリズムの繰り返しの回数
**lbfgs_tolerance** — LBFGSに供給される許容誤差
**iprint** — LBFGSに供給される
IPRINTパラメータ(メッセージ出力を制御する２つの整数のリスト)
**%lambda** — 拡張Lagrangeを計算するために使われる
`%lambda`の初期値


この実装は
擬似Newtonアルゴリズムであるメモリ制限付きBFGS (LBFGS)アルゴリズムを適用することで
拡張Lagraneを最小化します。


`load("augmented_lagrangian")`はこの関数をロードします。


`lbfgs`も参照してください。


参考文献:


[1] [http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/continuous/constrained/nonlinearcon/auglag.html]()


[2] [http://www.cs.ubc.ca/spider/ascher/542/chap10.pdf]()


例:












```maxima
(%i1) load ("lbfgs");
(%o1)     /maxima/share/lbfgs/lbfgs.mac
(%i2) load ("augmented_lagrangian");
(%o2) 
   /maxima/share/contrib/augmented_lagrangian.mac
(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x
(%i4) xx: [x, y];
(%o4)                        [x, y]
(%i5) C: [x + y - 1];
(%o5)                      [y + x - 1]
(%i6) yy: [1, 1];
(%o6)                        [1, 1]
(%i7) augmented_lagrangian_method(FOM, xx, C, yy, iprint=[-1,0]);
(%o7) [[x = 0.66665984108002, y = 0.33334027245545],
                                 %lambda = [- 1.333337940892525]]
```


前と同じ例ですが、今回は
グラディエントが引数として供給されます。














```maxima
(%i1) load ("lbfgs")$
(%i2) load ("augmented_lagrangian")$
(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x
(%i4) FOM: x^2 + 2*y^2;
                               2    2
(%o4)                       2 y  + x
(%i5) xx: [x, y];
(%o5)                        [x, y]
(%i6) grad : [2*x, 4*y];
(%o6)                      [2 x, 4 y]
(%i7) C: [x + y - 1];
(%o7)                      [y + x - 1]
(%i8) yy: [1, 1];
(%o8)                        [1, 1]
(%i9) augmented_lagrangian_method ([FOM, grad], xx, C, yy,
                                   iprint = [-1, 0]);
(%o9) [[x = 0.666659841080025, y = .3333402724554462], 
                                 %lambda = [- 1.333337940892543]]
```

