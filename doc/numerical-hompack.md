## hompack

### Function: hompack_polsys (eqnlist, varlist, iflg1, epsbig, epssml, numrr)

Finds the roots of the system of polynomials in the variables
*varlist* in the system of equations in *eqnlist*.  The number
of equations must match number of variables.  Each equation must be a
polynomial with variables in *varlist*.  The coefficients must be
real numbers.


The optional keyword arguments provide some control over the
algorithm.



**epsbig** — is the local error tolerance allowed by the
path tracker, defaulting to 1e-4.
**epssml** — is the accuracy
desired for the final solution, defaulting to 1d-14.
**numrr** — is the number of multiples of 1000 steps that will be tried
before abandoning a path, defaulting to 10.
**iflg1** — defaulting to 0, controls the algorithm as follows: 
**0** — If the problem is to be solved without calling `polsys`’ scaling
routine, `sclgnp`, and without using the projective
transformation.
**1** — If scaling but no projective transformation is to be used.
**10** — If no scaling but projective transformation is to be used.
**11** — If both scaling and projective transformation are to be used.


`hompack_polsys` returns a list.  The elements of the list are:


**retcode** — Indicates whether the solution is valid or not. 
**0** — Solution found without problems
**1** — Solution succeeded but `iflg2` indicates some issues with a
root. (That is, `iflg2` is not all ones.)
**-1** — `NN`, the declared dimension of the number of terms in the
polynomials,  is too small.  (This should not happen.)
**-2** — `MMAXT`, the declared dimension for the internal coefficient and
degree arrays, is too small.  (This should not happen.)
**-3** — `TTOTDG`, the total degree of the equations,  is too small.
(This should not happen.)
**-4** — `LENWK`, the length of the internal real work array, is too
small.  (This should not happen.)
**-5** — `LENIWK`, the length of the internal integer work array, is too
small.  (This should not happen.)
**-6** — *iflg1* is not 0 or 1, or 10 or 11.  (This should not happen; an
error should be thrown before `polsys` is called.)
**roots** — The roots of the system of equations.  This is in the same format as
`solve` would return.
**iflg2** — A list containing information on how the path for the m’th root terminated: 
**1** — Normal return
**2** — Specified error tolerance cannot be met.  Increase *epsbig* and
*epssml*  and rerun.
**3** — Maximum number of steps exceeded.  To track the path further, increase
*numrr* and rerun the path.  However, the path may be diverging, if the
lambda value is near 1 and the roots values are large.
**4** — Jacobian matrix does not have full rank.  The algorithm has failed
(the zero curve of the homotopy map cannot be followed any further).
**5** — The tracking algorithm has lost the zero curve of the homotopy map and
is not making progress.  The error tolerances *epsbig* and
*epssml* were too lenient.  The problem should be restarted with
smaller error tolerances.
**6** — The normal flow newton iteration in `stepnf` or `rootnf`
failed to converge.  The error tolerance *epsbig* may be too
stringent.
**7** — Illegal input parameters, a fatal error.
**lambda** — A list of the final lambda value for the m-th root, where lambda is the
continuation parameter.
**arclen** — A list of the arc length of the m-th root.
**nfe** — A list of the number of jacobian matrix evaluations required to track the m-th
root.


Here are some examples of using `hompack_polsys`.






```maxima
maxima
(%i1) load(hompack)$

(%i2) hompack_polsys([x1^2-1, x2^2-2],[x1,x2]);
(%o2) [0, [[x1 = 7.493410174972965e-17 %i - 1.0, 
x2 = - 2.1199276810167172e-16 %i - 1.4142135623730951], 
[x1 = 1.0 - 1.7812202259088373e-17 %i, 
x2 = - 9.892128000334418e-17 %i - 1.4142135623730951], 
[x1 = - 8.745710933584358e-17 %i - 1.0, 
x2 = 1.4142135623730951 - 3.1543521174128613e-17 %i], 
[x1 = 1.0 - 5.5487454344135625e-18 %i, 
x2 = 9.617653810456737e-17 %i + 1.4142135623730951]], 
[1, 1, 1, 1], [1.0, 1.0, 0.9999999999999999, 
0.9999999999999999], [4.6126237693413445, 4.6126230108601, 
4.612623872939582, 4.6126231144843475], [40, 40, 40, 40]]
```


The analytical solution can be obtained with solve:





```maxima
maxima

(%i1) solve([x1^2-1, x2^2-2],[x1,x2]);
(%o1) [[x1 = 1, x2 = - sqrt(2)], [x1 = 1, x2 = sqrt(2)], 
            [x1 = - 1, x2 = - sqrt(2)], [x1 = - 1, x2 = sqrt(2)]]
```

We see that `hompack_polsys` returned the correct answer except
that the roots are in a different order and there is a small imaginary
part.


Another example, with corresponding solution from solve:







```maxima
maxima
(%i1) load(hompack)$

(%i2) hompack_polsys([x1^2 + 2*x2^2 + x1*x2 - 5, 2*x1^2 + x2^2 + x2-4],[x1,x2]);
(%o2) [0, [[x1 = 1.2015573017007832 - 6.51849608628558e-16 %i, 
x2 = - 2.2667444298167825e-16 %i - 1.6672703634801431], 
[x1 = - 5.901956169878514e-17 %i - 1.4285291895653132, 
x2 = - 6.670215053038164e-17 %i - 0.9106199083334114], 
[x1 = 1.942890293094024e-16 %i + 0.5920619420732687, 
x2 = 1.383859154368197 - 1.942890293094024e-16 %i], 
[x1 = 0.08945540033671631 - 8.534583737796769e-16 %i, 
x2 = 2.415141536592239e-16 %i + 1.5576674810817213]], 
[1, 1, 1, 1], [1.0000000000000004, 1.0000000000000002, 1.0, 
0.9999999999999999], [6.205795654034981, 7.7222132593900525, 
7.228287079174324, 5.6114742835849105], [35, 41, 48, 40]]


(%i3) solve([x1^2+2*x2^2+x1*x2 - 5, 2*x1^2+x2^2+x2-4],[x1,x2]);
(%o3) [[x1 = 0.08945540336850383, x2 = 1.5576673866090713], 
[x1 = 0.5920619554695062, x2 = 1.3838592860838075], 
[x1 = 1.2015573525007488, x2 = - 1.66727025803531], 
[x1 = - 1.428529150636283, x2 = - 0.9106198942815954]]
```


Note that `hompack_polsys` can sometimes be very slow.  Perhaps
`solve` can be used.  Or perhaps `eliminate` can be used to
convert the system of polynomials into one polynomial for which
`allroots` can find all the roots.

