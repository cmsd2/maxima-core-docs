## lbfgs

### Function: lbfgs (lbfgs, FOM, X, X0, epsilon, iprint, lbfgs, FOM, grad, X, X0, epsilon, iprint)

Finds an approximate solution of the unconstrained minimization of the figure of merit *FOM*
over the list of variables *X*,
starting from initial estimates *X0*,
such that $norm(grad(FOM)) < epsilon*max(1, norm(X))$.


*grad*, if present, is the gradient of *FOM* with respect to the variables *X*.
*grad* may be a list or a function that returns a list, with one element for each element of *X*.
If not present, the gradient is computed automatically by symbolic differentiation.
If *FOM* is a function, the gradient *grad* must be supplied by the user.


The algorithm applied is a limited-memory quasi-Newton (BFGS) algorithm [1].
It is called a limited-memory method because a low-rank approximation of the
Hessian matrix inverse is stored instead of the entire Hessian inverse.
Each iteration of the algorithm is a line search, that is,
a search along a ray in the variables *X*,
with the search direction computed from the approximate Hessian inverse.
The FOM is always decreased by a successful line search.
Usually (but not always) the norm of the gradient of FOM also decreases.


*iprint* controls progress messages printed by `lbfgs`.



**iprint[1]** — `iprint[1]` controls the frequency of progress messages. 
**iprint[1] < 0** — No progress messages.
**iprint[1] = 0** — Messages at the first and last iterations.
**iprint[1] > 0** — Print a message every `iprint[1]` iterations.
**iprint[2]** — `iprint[2]` controls the verbosity of progress messages. 
**iprint[2] = 0** — Print out iteration count, number of evaluations of *FOM*, value of *FOM*,
norm of the gradient of *FOM*, and step length.
**iprint[2] = 1** — Same as `iprint[2] = 0`, plus *X0* and the gradient of *FOM* evaluated at *X0*.
**iprint[2] = 2** — Same as `iprint[2] = 1`, plus values of *X* at each iteration.
**iprint[2] = 3** — Same as `iprint[2] = 2`, plus the gradient of *FOM* at each iteration.


The columns printed by `lbfgs` are the following.



**I** — Number of iterations. It is incremented for each line search.
**NFN** — Number of evaluations of the figure of merit.
**FUNC** — Value of the figure of merit at the end of the most recent line search.
**GNORM** — Norm of the gradient of the figure of merit at the end of the most recent line search.
**STEPLENGTH** — An internal parameter of the search algorithm.


Additional information concerning details of the algorithm are found in the
comments of the original Fortran code [2].


See also `lbfgs_nfeval_max` and `lbfgs_005fncorrections`.


References:


[1] D. Liu and J. Nocedal. "On the limited memory BFGS method for large
scale optimization". *Mathematical Programming B* 45:503–528 (1989)


[2] [https://www.netlib.org/opt/lbfgs_um.shar]()


Examples:


The same FOM as computed by FGCOMPUTE in the program sdrive.f in the LBFGS package from Netlib.
Note that the variables in question are subscripted variables.
The FOM has an exact minimum equal to zero at $u[k] = 1$ for $k = 1, ..., 8$.












```maxima
(%i1) load ("lbfgs")$
(%i2) t1[j] := 1 - u[j];
(%o2)                     t1  := 1 - u
                            j         j
(%i3) t2[j] := 10*(u[j + 1] - u[j]^2);
                                          2
(%o3)                t2  := 10 (u      - u )
                       j         j + 1    j
(%i4) n : 8;
(%o4)                           8
(%i5) FOM : sum (t1[2*j - 1]^2 + t2[2*j - 1]^2, j, 1, n/2);
                 2 2           2              2 2           2
(%o5) 100 (u  - u )  + (1 - u )  + 100 (u  - u )  + (1 - u )
            8    7           7           6    5           5
                     2 2           2              2 2           2
        + 100 (u  - u )  + (1 - u )  + 100 (u  - u )  + (1 - u )
                4    3           3           2    1           1
(%i6) lbfgs (FOM, '[u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8]],
       [-1.2, 1, -1.2, 1, -1.2, 1, -1.2, 1], 1e-3, [1, 0]);
*************************************************
  N=    8   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  9.680000000000000D+01   GNORM=  4.657353755084533D+02
*************************************************
```


```maxima
I NFN   FUNC                    GNORM                   STEPLENGTH

 1   3   1.651479526340304D+01   4.324359291335977D+00   7.926153934390631D-04
 2   4   1.650209316638371D+01   3.575788161060007D+00   1.000000000000000D+00
 3   5   1.645461701312851D+01   6.230869903601577D+00   1.000000000000000D+00
 4   6   1.636867301275588D+01   1.177589920974980D+01   1.000000000000000D+00
 5   7   1.612153014409201D+01   2.292797147151288D+01   1.000000000000000D+00
 6   8   1.569118407390628D+01   3.687447158775571D+01   1.000000000000000D+00
 7   9   1.510361958398942D+01   4.501931728123679D+01   1.000000000000000D+00
 8  10   1.391077875774293D+01   4.526061463810630D+01   1.000000000000000D+00
 9  11   1.165625686278198D+01   2.748348965356907D+01   1.000000000000000D+00
10  12   9.859422687859144D+00   2.111494974231706D+01   1.000000000000000D+00
11  13   7.815442521732282D+00   6.110762325764183D+00   1.000000000000000D+00
12  15   7.346380905773044D+00   2.165281166715009D+01   1.285316401779678D-01
13  16   6.330460634066464D+00   1.401220851761508D+01   1.000000000000000D+00
14  17   5.238763939854303D+00   1.702473787619218D+01   1.000000000000000D+00
15  18   3.754016790406625D+00   7.981845727632704D+00   1.000000000000000D+00
16  20   3.001238402313225D+00   3.925482944745832D+00   2.333129631316462D-01
17  22   2.794390709722064D+00   8.243329982586480D+00   2.503577283802312D-01
18  23   2.563783562920545D+00   1.035413426522664D+01   1.000000000000000D+00
19  24   2.019429976373283D+00   1.065187312340952D+01   1.000000000000000D+00
20  25   1.428003167668592D+00   2.475962450735100D+00   1.000000000000000D+00
21  27   1.197874264859232D+00   8.441707983339661D+00   4.303451060697367D-01
22  28   9.023848942003913D-01   1.113189216665625D+01   1.000000000000000D+00
23  29   5.508226405855795D-01   2.380830599637816D+00   1.000000000000000D+00
24  31   3.902893258879521D-01   5.625595817143044D+00   4.834988416747262D-01
25  32   3.207542206881058D-01   1.149444645298493D+01   1.000000000000000D+00
26  33   1.874468266118200D-01   3.632482152347445D+00   1.000000000000000D+00
27  34   9.575763380282112D-02   4.816497449000391D+00   1.000000000000000D+00
28  35   4.085145106760390D-02   2.087009347116811D+00   1.000000000000000D+00
29  36   1.931106005512628D-02   3.886818624052740D+00   1.000000000000000D+00
30  37   6.894000636920714D-03   3.198505769992936D+00   1.000000000000000D+00
31  38   1.443296008850287D-03   1.590265460381961D+00   1.000000000000000D+00
32  39   1.571766574930155D-04   3.098257002223532D-01   1.000000000000000D+00
33  40   1.288011779655132D-05   1.207784334505595D-02   1.000000000000000D+00
34  41   1.806140190993455D-06   4.587890258846915D-02   1.000000000000000D+00
35  42   1.769004612050548D-07   1.790537363138099D-02   1.000000000000000D+00
36  43   3.312164244118216D-10   6.782068546986653D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
 1& 3& 1.651479526340304D+01& 4.324359291335977D+00& 7.926153934390631D-04\cr
 2& 4& 1.650209316638371D+01& 3.575788161060007D+00& 1.000000000000000D+00\cr
 3& 5& 1.645461701312851D+01& 6.230869903601577D+00& 1.000000000000000D+00\cr
 4& 6& 1.636867301275588D+01& 1.177589920974980D+01& 1.000000000000000D+00\cr
 5& 7& 1.612153014409201D+01& 2.292797147151288D+01& 1.000000000000000D+00\cr
 6& 8& 1.569118407390628D+01& 3.687447158775571D+01& 1.000000000000000D+00\cr
 7& 9& 1.510361958398942D+01& 4.501931728123680D+01& 1.000000000000000D+00\cr
 8&10& 1.391077875774294D+01& 4.526061463810632D+01& 1.000000000000000D+00\cr
 9&11& 1.165625686278198D+01& 2.748348965356917D+01& 1.000000000000000D+00\cr
10&12& 9.859422687859137D+00& 2.111494974231644D+01& 1.000000000000000D+00\cr
11&13& 7.815442521732281D+00& 6.110762325766556D+00& 1.000000000000000D+00\cr
12&15& 7.346380905773160D+00& 2.165281166714631D+01& 1.285316401779533D-01\cr
13&16& 6.330460634066370D+00& 1.401220851762050D+01& 1.000000000000000D+00\cr
14&17& 5.238763939851439D+00& 1.702473787613255D+01& 1.000000000000000D+00\cr
15&18& 3.754016790406701D+00& 7.981845727704576D+00& 1.000000000000000D+00\cr
16&20& 3.001238402309352D+00& 3.925482944716691D+00& 2.333129631296807D-01\cr
17&22& 2.794390709718290D+00& 8.243329982546473D+00& 2.503577283782332D-01\cr
18&23& 2.563783562918759D+00& 1.035413426521790D+01& 1.000000000000000D+00\cr
19&24& 2.019429976377856D+00& 1.065187312346769D+01& 1.000000000000000D+00\cr
20&25& 1.428003167670903D+00& 2.475962450826961D+00& 1.000000000000000D+00\cr
21&27& 1.197874264861340D+00& 8.441707983493810D+00& 4.303451060808756D-01\cr
22&28& 9.023848941942773D-01& 1.113189216635162D+01& 1.000000000000000D+00\cr
23&29& 5.508226405863770D-01& 2.380830600326308D+00& 1.000000000000000D+00\cr
24&31& 3.902893258815567D-01& 5.625595816584421D+00& 4.834988416524465D-01\cr
25&32& 3.207542206990315D-01& 1.149444645416472D+01& 1.000000000000000D+00\cr
26&33& 1.874468266362791D-01& 3.632482152880997D+00& 1.000000000000000D+00\cr
27&34& 9.575763380706598D-02& 4.816497446154354D+00& 1.000000000000000D+00\cr
28&35& 4.085145107543406D-02& 2.087009350166495D+00& 1.000000000000000D+00\cr
29&36& 1.931106001379290D-02& 3.886818608498966D+00& 1.000000000000000D+00\cr
30&37& 6.894000721499670D-03& 3.198505796342214D+00& 1.000000000000000D+00\cr
31&38& 1.443296033051864D-03& 1.590265471025043D+00& 1.000000000000000D+00\cr
32&39& 1.571766603154336D-04& 3.098257063980634D-01& 1.000000000000000D+00\cr
33&40& 1.288011776581970D-05& 1.207784183577257D-02& 1.000000000000000D+00\cr
34&41& 1.806140173752971D-06& 4.587890233385193D-02& 1.000000000000000D+00\cr
35&42& 1.769004645459358D-07& 1.790537375052208D-02& 1.000000000000000D+00\cr
36&43& 3.312164100763217D-10& 6.782068426119681D-04& 1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o6) [u  = 1.000005339816132, u  = 1.000009942840108, 
        1                       2
u  = 1.000005339816132, u  = 1.000009942840108, 
 3                       4
u  = 1.000005339816132, u  = 1.000009942840108, 
 5                       6
u  = 1.000005339816132, u  = 1.000009942840108]
 7                       8
```


A regression problem.
The FOM is the mean square difference between the predicted value $F(X[i])$
and the observed value $Y[i]$.
The function $F$ is a bounded monotone function (a so-called "sigmoidal" function).
In this example, `lbfgs` computes approximate values for the parameters of $F$
and `plot2d` displays a comparison of $F$ with the observed data.














```maxima
(%i1) load ("lbfgs")$
(%i2) FOM : '((1/length(X))*sum((F(X[i]) - Y[i])^2, i, 1,
                                                length(X)));
                               2
               sum((F(X ) - Y ) , i, 1, length(X))
                       i     i
(%o2)          -----------------------------------
                            length(X)
(%i3) X : [1, 2, 3, 4, 5];
(%o3)                    [1, 2, 3, 4, 5]
(%i4) Y : [0, 0.5, 1, 1.25, 1.5];
(%o4)                [0, 0.5, 1, 1.25, 1.5]
(%i5) F(x) := A/(1 + exp(-B*(x - C)));
                                   A
(%o5)            F(x) := ----------------------
                         1 + exp((- B) (x - C))
(%i6) ''FOM;
                A               2            A                2
(%o6) ((----------------- - 1.5)  + (----------------- - 1.25)
          - B (5 - C)                  - B (4 - C)
        %e            + 1            %e            + 1
            A             2            A               2
 + (----------------- - 1)  + (----------------- - 0.5)
      - B (3 - C)                - B (2 - C)
    %e            + 1          %e            + 1
             2
            A
 + --------------------)/5
      - B (1 - C)     2
   (%e            + 1)
(%i7) estimates : lbfgs (FOM, '[A, B, C], [1, 1, 1], 1e-4, [1, 0]);
*************************************************
  N=    3   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  1.348738534246918D-01   GNORM=  2.000215531936760D-01
*************************************************
```


```maxima
I  NFN  FUNC                    GNORM                   STEPLENGTH
1    3  1.177820636622582D-01   9.893138394953992D-02   8.554435968992371D-01  
2    6  2.302653892214013D-02   1.180098521565904D-01   2.100000000000000D+01  
3    8  1.496348495303004D-02   9.611201567691624D-02   5.257340567840710D-01  
4    9  7.900460841091138D-03   1.325041647391314D-02   1.000000000000000D+00  
5   10  7.314495451266914D-03   1.510670810312226D-02   1.000000000000000D+00  
6   11  6.750147275936668D-03   1.914964958023037D-02   1.000000000000000D+00  
7   12  5.850716021108202D-03   1.028089194579382D-02   1.000000000000000D+00  
8   13  5.778664230657800D-03   3.676866074532179D-04   1.000000000000000D+00  
9   14  5.777818823650780D-03   3.010740179797108D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
1&  3&1.177820636622582D-01& 9.893138394953992D-02& 8.554435968992371D-01\cr
2&  6&2.302653892214013D-02& 1.180098521565904D-01& 2.100000000000000D+01\cr
3&  8&1.496348495303004D-02& 9.611201567691624D-02& 5.257340567840710D-01\cr
4&  9&7.900460841091138D-03& 1.325041647391314D-02& 1.000000000000000D+00\cr
5& 10&7.314495451266914D-03& 1.510670810312226D-02& 1.000000000000000D+00\cr
6& 11&6.750147275936668D-03& 1.914964958023037D-02& 1.000000000000000D+00\cr
7& 12&5.850716021108202D-03& 1.028089194579382D-02& 1.000000000000000D+00\cr
8& 13&5.778664230657800D-03& 3.676866074532179D-04& 1.000000000000000D+00\cr
9& 14&5.777818823650780D-03& 3.010740179797108D-04& 1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o7) [A = 1.461933911464101, B = 1.601593973254801, 
                                           C = 2.528933072164855]
(%i8) plot2d ([F(x), [discrete, X, Y]], [x, -1, 6]), ''estimates;
(%o8)
```


Gradient of FOM is specified (instead of computing it automatically).
Both the FOM and its gradient are passed as functions to `lbfgs`.











```maxima
(%i1) load ("lbfgs")$
(%i2) F(a, b, c) := (a - 5)^2 + (b - 3)^4 + (c - 2)^6$
(%i3) define(F_grad(a, b, c),
             map (lambda ([x], diff (F(a, b, c), x)), [a, b, c]))$
(%i4) estimates : lbfgs ([F, F_grad],
                   [a, b, c], [0, 0, 0], 1e-4, [1, 0]);
*************************************************
  N=    3   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  1.700000000000000D+02   GNORM=  2.205175729958953D+02
*************************************************
```


```maxima
I  NFN     FUNC                    GNORM                   STEPLENGTH

   1    2     6.632967565917637D+01   6.498411132518770D+01   4.534785987412505D-03  
   2    3     4.368890936228036D+01   3.784147651974131D+01   1.000000000000000D+00  
   3    4     2.685298972775191D+01   1.640262125898520D+01   1.000000000000000D+00  
   4    5     1.909064767659852D+01   9.733664001790506D+00   1.000000000000000D+00  
   5    6     1.006493272061515D+01   6.344808151880209D+00   1.000000000000000D+00  
   6    7     1.215263596054292D+00   2.204727876126877D+00   1.000000000000000D+00  
   7    8     1.080252896385329D-02   1.431637116951845D-01   1.000000000000000D+00  
   8    9     8.407195124830860D-03   1.126344579730008D-01   1.000000000000000D+00  
   9   10     5.022091686198525D-03   7.750731829225275D-02   1.000000000000000D+00  
  10   11     2.277152808939775D-03   5.032810859286796D-02   1.000000000000000D+00  
  11   12     6.489384688303218D-04   1.932007150271009D-02   1.000000000000000D+00  
  12   13     2.075791943844547D-04   6.964319310814365D-03   1.000000000000000D+00  
  13   14     7.349472666162258D-05   4.017449067849554D-03   1.000000000000000D+00  
  14   15     2.293617477985238D-05   1.334590390856715D-03   1.000000000000000D+00  
  15   16     7.683645404048675D-06   6.011057038099202D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
   1&   2&    6.632967565917637D+01&  6.498411132518770D+01&  4.534785987412505D-03\cr
   2&   3&    4.368890936228036D+01&  3.784147651974131D+01&  1.000000000000000D+00\cr
   3&   4&    2.685298972775191D+01&  1.640262125898520D+01&  1.000000000000000D+00\cr
   4&   5&    1.909064767659852D+01&  9.733664001790506D+00&  1.000000000000000D+00\cr
   5&   6&    1.006493272061515D+01&  6.344808151880209D+00&  1.000000000000000D+00\cr
   6&   7&    1.215263596054292D+00&  2.204727876126877D+00&  1.000000000000000D+00\cr
   7&   8&    1.080252896385329D-02&  1.431637116951845D-01&  1.000000000000000D+00\cr
   8&   9&    8.407195124830860D-03&  1.126344579730008D-01&  1.000000000000000D+00\cr
   9&  10&    5.022091686198525D-03&  7.750731829225275D-02&  1.000000000000000D+00\cr
  10&  11&    2.277152808939775D-03&  5.032810859286796D-02&  1.000000000000000D+00\cr
  11&  12&    6.489384688303218D-04&  1.932007150271009D-02&  1.000000000000000D+00\cr
  12&  13&    2.075791943844547D-04&  6.964319310814365D-03&  1.000000000000000D+00\cr
  13&  14&    7.349472666162258D-05&  4.017449067849554D-03&  1.000000000000000D+00\cr
  14&  15&    2.293617477985238D-05&  1.334590390856715D-03&  1.000000000000000D+00\cr
  15&  16&    7.683645404048675D-06&  6.011057038099202D-04&  1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o4) [a = 5.000086823042934, b = 3.052395429705181, 
                                           c = 1.927980629919583]
```

See also: `lbfgs_nfeval_max`, `lbfgs_ncorrections`.

### Variable: lbfgs_ncorrections

Default value: 25


`lbfgs_ncorrections` is the number of corrections applied
to the approximate inverse Hessian matrix which is maintained by `lbfgs`.

### Variable: lbfgs_nfeval_max

Default value: 100


`lbfgs_nfeval_max` is the maximum number of evaluations of the figure of merit (FOM) in `lbfgs`.
When `lbfgs_nfeval_max` is reached,
`lbfgs` returns the result of the last successful line search.

