## trigtools

### Function: atan_contract (r)

The function atan_contract(r) contracts atan functions. We
assume: 
$|r| < {\pi\over 2}.$


`load("trigtools")` loads this function.



Examples:



1. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) atan_contract(atan(x)+atan(y));
(%o2)                   atan(y) + atan(x)

(%i3) assume(abs(atan(x)+atan(y))<%pi/2)$

(%i4) atan(x)+atan(y)=atan_contract(atan(x)+atan(y));
                                          y + x
(%o4)           atan(y) + atan(x) = atan(-------)
                                         1 - x y
```
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) atan(1/3)+atan(1/5)+atan(1/7)+atan(1/8)$ %=atan_contract(%);
                1         1         1         1    %pi
(%o3)      atan(-) + atan(-) + atan(-) + atan(-) = ---
                3         5         7         8     4
```
3. Machin’s formulae






```maxima
maxima
(%i1) load("trigtools")$

(%i2) 4*atan(1/5)-atan(1/239)=atan_contract(4*atan(1/5)-atan(1/239));
                          1          1     %pi
(%o2)              4 atan(-) - atan(---) = ---
                          5         239     4
```
4. see [https://en.wikipedia.org/wiki/Machin-like_formula]()







```maxima
maxima
(%i1) load("trigtools")$
(%i2) 12*atan(1/49)+32*atan(1/57)-5*atan(1/239)+12*atan(1/110443)$

(%i3) %=atan_contract(%);
              1             1             1
(%o3) 12 atan(--) + 32 atan(--) - 5 atan(---)
              49            57           239
                                                      1       %pi
                                          + 12 atan(------) = ---
                                                    110443     4
```

### Function: c2hyp (x)

The function c2hyp (convert to hyperbolic) convert expression with exp function
to expression with hyperbolic functions sinh, cosh.


`load("trigtools")` loads this function.


Examples:









```maxima
maxima
(%i1) load("trigtools")$

(%i2) c2hyp(exp(x));
(%o2)                   sinh(x) + cosh(x)


(%i3) c2hyp(exp(x)+exp(x^2)+1);
                 2          2
(%o3)      sinh(x ) + cosh(x ) + sinh(x) + cosh(x) + 1


(%i4) c2hyp(exp(x)/(2*exp(y)-3*exp(z)));
                        sinh(x) + cosh(x)
(%o4)     ---------------------------------------------
          2 (sinh(y) + cosh(y)) - 3 (sinh(z) + cosh(z))
```

### Function: c2sin (x)

The function c2sin converts the expression 
$a\cos x + b\sin x$
to
$r\sin(x+\phi).$


The function c2cos converts the expression 
$a\cos x + b\sin x$
to
$r\cos(x-\phi).$


`load("trigtools")` loads these functions.


Examples:













```maxima
maxima
(%i1) load("trigtools")$

(%i2) c2sin(3*sin(x)+4*cos(x));
                                      4
(%o2)                  5 sin(x + atan(-))
                                      3


(%i3) trigexpand(%),expand;
(%o3)                  3 sin(x) + 4 cos(x)


(%i4) c2cos(3*sin(x)-4*cos(x));
                                       3
(%o4)                 - 5 cos(x + atan(-))
                                       4


(%i5) trigexpand(%),expand;
(%o5)                  3 sin(x) - 4 cos(x)


(%i6) c2sin(sin(x)+cos(x));
                                      %pi
(%o6)                 sqrt(2) sin(x + ---)
                                       4


(%i7) trigexpand(%),expand;
(%o7)                    sin(x) + cos(x)


(%i8) c2cos(sin(x)+cos(x));
                                      %pi
(%o8)                 sqrt(2) cos(x - ---)
                                       4


(%i9) trigexpand(%),expand;
(%o9)                    sin(x) + cos(x)
```


Example. Solve trigonometric equation







```maxima
maxima

(%i1) eq:3*sin(x)+4*cos(x)=2;
(%o1)                3 sin(x) + 4 cos(x) = 2


(%i2) plot2d([3*sin(x)+4*cos(x),2],[x,-%pi,%pi]);
(%o2)                         false
```


figures/trigtools-15inplot1














```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:3*sin(x)+4*cos(x)=2$

(%i3) eq1:c2sin(lhs(eq))=2;
                                    4
(%o3)                5 sin(x + atan(-)) = 2
                                    3

(%i4) solvetrigwarn:false$

(%i5) solve(eq1)[1]$ x1:rhs(%);
                             2         4
(%o6)                   asin(-) - atan(-)
                             5         3


(%i7) float(%), numer;
(%o7)                 - 0.5157783719341241


(%i8) eq2:c2cos(lhs(eq))=2;
                                    3
(%o8)                5 cos(x - atan(-)) = 2
                                    4


(%i9) solve(eq2,x)[1]$ x2:rhs(%);
                             3         2
(%o10)                  atan(-) + acos(-)
                             4         5


(%i11) float(%), numer;
(%o11)                  1.802780589520693


(%i12) sol:[x1,x2];
                   2         4        3         2
(%o12)       [asin(-) - atan(-), atan(-) + acos(-)]
                   5         3        4         5
```



Answ.: 
$x = x_1 + 2\pi k,$
$x_1 = \sin^{-1}{2\over 5} - \tan^{-1}{4\over 3},$
or
$x_1 = \tan^{-1}{3\over 4} + \cos^{-1}{2\over 5},$
for $k$ any integer.

### Function: c2trig (x)

The function c2trig (convert to trigonometric) reduce expression with hyperbolic functions
sinh, cosh, tanh, coth to trigonometric expression with sin, cos, tan, cot.


`load("trigtools")` loads these functions.


Examples:



1. ```maxima
maxima
(%i1) load(trigtools)$

(%i2) sinh(x)=c2trig(sinh(x));
(%o2)               sinh(x) = - %i sin(%i x)


(%i3) cosh(x)=c2trig(cosh(x));
(%o3)                  cosh(x) = cos(%i x)


(%i4) tanh(x)=c2trig(tanh(x));
(%o4)               tanh(x) = - %i tan(%i x)


(%i5) coth(x)=c2trig(coth(x));
(%o5)                coth(x) = %i cot(%i x)
```
2. see [https://maxima.sourceforge.io/ext/list_archives/2013/msg03230.html]()








```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(p+q*%i);
(%o2)                     cos(%i q + p)


(%i3) trigexpand(%);
(%o3)          cos(p) cosh(q) - %i sin(p) sinh(q)


(%i4) c2trig(%);
(%o4)                     cos(%i q + p)
```
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(a+b*%i);
(%o2)                     sin(%i b + a)


(%i3) trigexpand(%);
(%o3)          %i cos(a) sinh(b) + sin(a) cosh(b)


(%i4) c2trig(%);
(%o4)                     sin(%i b + a)
```
4. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(a*%i+b*%i);
(%o2)                   cos(%i b + %i a)


(%i3) trigexpand(%);
(%o3)           sinh(a) sinh(b) + cosh(a) cosh(b)


(%i4) c2trig(%);
(%o4)                   cos(%i b + %i a)
```
5. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) tan(a+%i*b);
(%o2)                     tan(%i b + a)


(%i3) trigexpand(%);
                       %i tanh(b) + tan(a)
(%o3)                 ---------------------
                      1 - %i tan(a) tanh(b)


(%i4) c2trig(%);
(%o4)                     tan(%i b + a)
```
6. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cot(x+%i*y);
(%o2)                     cot(%i y + x)


(%i3) trigexpand(%);
                     - %i cot(x) coth(y) - 1
(%o3)                -----------------------
                       cot(x) - %i coth(y)


(%i4) c2trig(%);
(%o4)                     cot(%i y + x)
```

### Function: trigeval (x)

The function trigeval compute values of expressions with 
$\sin {m\pi\over n},$
$\cos {m\pi\over n},$
$\tan {m\pi\over n},$
and 
$\cot {m\pi\over n}$
in radicals.

### Function: trigfactor (x)

The function trigfactor factors expressions of
form 
$\pm \sin x \pm \cos y.$


`load("trigtools")` loads this function.


Examples:



1. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)+cos(x));
                                      %pi
(%o2)                 sqrt(2) cos(x - ---)
                                       4


(%i3) trigrat(%);
(%o3)                    sin(x) + cos(x)
```
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)+cos(y));
                     y   x   %pi      y   x   %pi
(%o2)          2 cos(- - - + ---) cos(- + - - ---)
                     2   2    4       2   2    4


(%i3) trigrat(%);
(%o3)                    cos(y) + sin(x)
```
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)-cos(3*y));
                   3 y   x   %pi      3 y   x   %pi
(%o2)        2 sin(--- - - + ---) sin(--- + - - ---)
                    2    2    4        2    2    4


(%i3) trigrat(%);
(%o3)                   sin(x) - cos(3 y)
```
4. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(-sin(5*x)-cos(3*y));
                  3 y   5 x   %pi      3 y   5 x   %pi
(%o2)     - 2 cos(--- - --- + ---) cos(--- + --- - ---)
                   2     2     4        2     2     4


(%i3) trigrat(%);
(%o3)                 - cos(3 y) - sin(5 x)
```
5. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(alpha)+sin(beta)=trigfactor(sin(alpha)+sin(beta));
                                     beta   alpha
(%o2) sin(beta) + sin(alpha) = 2 cos(---- - -----)
                                      2       2
                                                    beta   alpha
                                                sin(---- + -----)
                                                     2       2


(%i3) trigrat(%);
(%o3)    sin(beta) + sin(alpha) = sin(beta) + sin(alpha)
```
6. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(alpha)-sin(beta)=trigfactor(sin(alpha)-sin(beta));
                                       beta   alpha
(%o2) sin(alpha) - sin(beta) = - 2 sin(---- - -----)
                                        2       2
                                                    beta   alpha
                                                cos(---- + -----)
                                                     2       2
```
7. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(alpha)+cos(beta)=trigfactor(cos(alpha)+cos(beta));
                                     beta   alpha
(%o2) cos(beta) + cos(alpha) = 2 cos(---- - -----)
                                      2       2
                                                    beta   alpha
                                                cos(---- + -----)
                                                     2       2
```
8. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(alpha)-cos(beta)=trigfactor(cos(alpha)-cos(beta));
                                     beta   alpha
(%o2) cos(alpha) - cos(beta) = 2 sin(---- - -----)
                                      2       2
                                                    beta   alpha
                                                sin(---- + -----)
                                                     2       2
```
9. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(3*sin(x)+7*cos(x));
(%o2)                  3 sin(x) + 7 cos(x)


(%i3) c2sin(%);
                                          7
(%o3)               sqrt(58) sin(x + atan(-))
                                          3


(%i4) trigexpand(%),expand;
(%o4)                  3 sin(x) + 7 cos(x)
```
10. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(2*x));
(%o2)                       sin(2 x)


(%i3) trigexpand(%);
(%o3)                    2 cos(x) sin(x)
```

### Function: trigsolve (x)

The function trigsolve find solutions of trigonometric equation from
interval 
$[a,b).$


`load("trigtools")` loads this function.



Examples:


1. ```maxima
maxima

(%i1) eq:eq:3*sin(x)+4*cos(x)=2;
(%o1)                3 sin(x) + 4 cos(x) = 2


(%i2) plot2d([3*sin(x)+4*cos(x),2],[x,-%pi,%pi]);
(%o2)                         false
```


figures/trigtools-25inplot2








```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:eq:3*sin(x)+4*cos(x)=2$

(%i3) sol:trigsolve(eq,-%pi,%pi);
            2 sqrt(21)   12              2 sqrt(21)   12
(%o3) {atan(---------- - --), %pi - atan(---------- + --)}
                5        5                   5        5


(%i4) float(%), numer;
(%o4)      {- 0.5157783719341241, 1.8027805895206928}
```


Answ. : 
$x = \tan^{-1}\left({2\sqrt{21}\over 5} - {12\over 5}\right) + 2\pi k$
;
$x = \pi - \tan^{-1}\left({2\sqrt{21}\over 5} + {12\over 5}\right) + 2\pi k,$
$k$ – any integer.
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x));
(%o2)    cos(3 x) - sin(x) = sqrt(3) (cos(x) - sin(3 x))

(%i3) plot2d([lhs(eq)-rhs(eq)], [x,0,2*%pi])$
```


figures/trigtools-35inplot3

We have 6 solutions from [0, 2*pi].







```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$
(%i3) plot2d([lhs(eq)-rhs(eq)], [x,0.2,0.5])$
```


figures/trigtools-45inplot4








```maxima
maxima
(%i1) load("trigtools")$
(%i2) load("trigtools")$
(%i3) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$
(%i4) plot2d([lhs(eq)-rhs(eq)], [x,3.3,3.6])$
```


figures/trigtools-55inplot4








```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$

(%i3) trigfactor(lhs(eq))=map(trigfactor,rhs(eq));
                  %pi            %pi
(%o3) - 2 sin(x + ---) sin(2 x - ---) = 
                   4              4
                                              %pi            %pi
                            2 sqrt(3) sin(x - ---) sin(2 x - ---)
                                               4              4


(%i4) factor(lhs(%)-rhs(%));
               4 x + %pi                4 x - %pi
(%o4) - 2 (sin(---------) + sqrt(3) sin(---------))
                   4                        4
                                                       8 x - %pi
                                                   sin(---------)
                                                           4
```


Equation is equivalent to














```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$

(%i3) trigfactor(lhs(eq))=map(trigfactor,rhs(eq));
                  %pi            %pi
(%o3) - 2 sin(x + ---) sin(2 x - ---) = 
                   4              4
                                              %pi            %pi
                            2 sqrt(3) sin(x - ---) sin(2 x - ---)
                                               4              4


(%i4) L:factor(rhs(%)-lhs(%));
             4 x + %pi                4 x - %pi       8 x - %pi
(%o4) 2 (sin(---------) + sqrt(3) sin(---------)) sin(---------)
                 4                        4               4


(%i5) eq1:part(L,2)=0;
               4 x + %pi                4 x - %pi
(%o5)      sin(---------) + sqrt(3) sin(---------) = 0
                   4                        4


(%i6) eq2:part(L,3)=0;
                           8 x - %pi
(%o6)                  sin(---------) = 0
                               4


(%i7) S1:trigsolve(eq1,0,2*%pi);
                           %pi  13 %pi
(%o7)                     {---, ------}
                           12     12


(%i8) S2:trigsolve(eq2,0,2*%pi);
                    %pi  5 %pi  9 %pi  13 %pi
(%o8)              {---, -----, -----, ------}
                     8     8      8      8


(%i9) S:listify(union(S1,S2));
             %pi  %pi  5 %pi  13 %pi  9 %pi  13 %pi
(%o9)       [---, ---, -----, ------, -----, ------]
             12    8     8      12      8      8


(%i10) float(%), numer;
(%o10) [0.2617993877991494, 0.39269908169872414, 
1.9634954084936207, 3.4033920413889422, 3.5342917352885173, 
5.105088062083414]
```


Answer: 
$x = a + 2\pi k,$
where $a$ any from $S$, $k$ any integer.
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0;
(%o2)          8 cos(x) cos(4 x) cos(5 x) - 1 = 0


(%i3) trigrat(%);
(%o3)     2 cos(10 x) + 2 cos(8 x) + 2 cos(2 x) + 1 = 0
```


Left side is periodic with period 
$T=\pi.$


We have 10 solutions from [0, pi].







```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) plot2d([lhs(eq),rhs(eq)],[x,0,%pi]);
(%o3)                         false
```


figures/trigtools-65inplot6









```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) x4:find_root(eq, x, 1.3, 1.32);
(%o3)                  1.3089969389957472


(%i4) x5:find_root(eq, x, 1.32, 1.35);
(%o4)                  1.3463968515384828


(%i5) plot2d([lhs(eq),0], [x,1.3,1.35], [gnuplot_preamble, "set grid;"]);
(%o5)                         false
```


figures/trigtools-75inplot7

Equation we multiply by 
$2\sin x\cos 2x:$













```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) eq*2*sin(x)*cos(2*x);
(%o3) 2 sin(x) cos(2 x) (8 cos(x) cos(4 x) cos(5 x) - 1) = 0


(%i4) eq1:trigreduce(%),expand;
(%o4)                sin(13 x) + sin(x) = 0


(%i5) trigfactor(lhs(eq1))=0;
(%o5)                2 cos(6 x) sin(7 x) = 0


(%i6) S1:trigsolve(cos(6*x),0,%pi);
              %pi  %pi  5 %pi  7 %pi  3 %pi  11 %pi
(%o6)        {---, ---, -----, -----, -----, ------}
              12    4    12     12      4      12


(%i7) S2:trigsolve(sin(7*x),0,%pi);
               %pi  2 %pi  3 %pi  4 %pi  5 %pi  6 %pi
(%o7)      {0, ---, -----, -----, -----, -----, -----}
                7     7      7      7      7      7
```


We remove solutions of 
$\sin x = 0$
and
$\cos 2x = 0.$










```maxima
maxima
(%i1) load("trigtools")$
(%i2) S1:trigsolve(cos(6*x),0,%pi)$
(%i3) S2:trigsolve(sin(7*x),0,%pi)$

(%i4) S3:trigsolve(sin(x),0,%pi);
(%o4)                          {0}


(%i5) S4:trigsolve(cos(2*x),0,%pi);
                           %pi  3 %pi
(%o5)                     {---, -----}
                            4     4
```


We find 10 solutions from 
$[0, \pi]:$














```maxima
maxima
(%i1) load("trigtools")$
(%i2) S1:trigsolve(cos(6*x),0,%pi)$
(%i3) S2:trigsolve(sin(7*x),0,%pi)$
(%i4) S3:trigsolve(sin(x),0,%pi)$
(%i5) S4:trigsolve(cos(2*x),0,%pi)$

(%i6) union(S1,S2)$ setdifference(%,S3)$ setdifference(%,S4);
       %pi  %pi  2 %pi  5 %pi  3 %pi  4 %pi  7 %pi  5 %pi
(%o8) {---, ---, -----, -----, -----, -----, -----, -----, 
       12    7     7     12      7      7     12      7
                                                   6 %pi  11 %pi
                                                   -----, ------}
                                                     7      12


(%i9) S:listify(%);
       %pi  %pi  2 %pi  5 %pi  3 %pi  4 %pi  7 %pi  5 %pi
(%o9) [---, ---, -----, -----, -----, -----, -----, -----, 
       12    7     7     12      7      7     12      7
                                                   6 %pi  11 %pi
                                                   -----, ------]
                                                     7      12


(%i10) length(S);
(%o10)                         10


(%i11) float(S), numer;
(%o11) [0.2617993877991494, 0.4487989505128276, 
0.8975979010256552, 1.3089969389957472, 1.3463968515384828, 
1.7951958020513104, 1.8325957145940461, 2.243994752564138, 
2.6927937030769655, 2.8797932657906435]
```

Answer: 
$x = a + 2\pi k,$
where $a$ any from $S$, $k$ any integer.

### Function: trigvalue (x)

The function trigvalue compute values of 
$\sin {m\pi\over n},$
$\cos {m\pi\over n},$
$\tan {m\pi\over n},$
and 
$\cot {m\pi\over n}$
in radicals.


`trigvalue` is essentially an internal function.
Use function `trigeval` in preference.


`load("trigtools")` loads this function.

See also: `trigeval`.

