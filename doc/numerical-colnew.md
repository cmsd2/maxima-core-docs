## colnew

<!-- category: Numerical -->
<!-- keywords: colnew_appsln -->
<!-- signatures: colnew_appsln(x, zlen, fspace, ispace) -->
### Function: colnew_appsln (x, zlen, fspace, ispace)

Return a list of solution values from `colnew_expert` results.


The function arguments are:



**x** — List of x-coordinates to calculate solution.
**zlen** — *mstar*, the length of the solution list z
**fspace** — List *fspace* returned from `colnew_005fexpert`.
**ispace** — List *ispace* returned from `colnew_005fexpert`.

See also: `colnew_expert`.

<!-- category: Numerical -->
<!-- keywords: colnew_expert -->
<!-- signatures: colnew_expert(ncomp, m, aleft, aright, zeta, ipar, ltol, tol, fixpnt, ispace, fspace, iflag, fsub, dfsub, gsub, dgsub, guess) -->
### Function: colnew_expert (ncomp, m, aleft, aright, zeta, ipar, ltol, tol, fixpnt, ispace, fspace, iflag, fsub, dfsub, gsub, dgsub, guess)

*colnew_expert* solves mixed-order systems of boundary-value problems (BVPs) in ordinary
differential equations (ODEs) using a numerical collocation method.


*colnew_expert* returns the list [*iflag*, *fspace*, *ispace*].
*iflag* is an error flag.  Lists *fspace* and *ispace* contain the
state of the solution 
and can be: used by `colnew_appsln` to calculate solution values
at arbitrary points in the solution domain; and passed back to *colnew_expert* to restart the solution process
with different arguments. 


The function arguments are:



**ncomp** — Number of differential equations   (ncomp ≤ 20)
**m** — Integer list of length *ncomp*.  
$m_j$
is the order of the $j$-th
differential equation,
with 
$1 \le m_j \le 4$
and 
$m^* = \sum_j m_j \le 40.$
**aleft** — Left end of interval
**aright** — Right end of interval
**zeta** — *zeta* 
$(\zeta)$
is a real list of length 
$m^*.$
$\zeta_j$
is the 
$j$-th boundary or side condition point. The
list 
$\zeta$
must be ordered, 
with  
$\zeta_j \le \zeta_{j+1}.$
All side condition
points must be mesh points in all meshes used,
see description of ipar[11] and fixpnt below.
**ipar** — A integer list of length 11.  The parameters in ipar are:  - * 
*ipar[1]*
    
  - * 
0, if the problem is linear
  - * 
1, if the problem is nonlinear
- * 
*ipar[2]* ( = $k$ )
  Number of collocation points per subinterval , where
$\max_j m_j \le k \le 7.$
  If *ipar[2]*=0 then colnew sets 
$k = \max\left(\max_i m_i + 5, 5 - \max_i m_i\right).$
- * 
*ipar[3]*  ( = $n$ )
  Number of subintervals in the initial mesh.
  If *ipar[3]* = 0 then colnew arbitrarily sets $n = 5$.
- * 
*ipar[4]* ( = ntol )
  Number of solution and derivative tolerances.
  Require 
$0 < {\rm ntol} < m^*.$
- * 
*ipar[5]*  ( = ndimf )
  The length of list *fspace*. Its size provides a constraint on *nmax*.
  Choose ipar[5] according to the formula
${\rm ipar[5]} \ge {\rm nmax} \cdot {\rm nsizef}$
  where
${\rm nsizef} = 4 + 3m^* + (5 + {\rm kd})\times{\rm kdm} + (2m^* - {\rm nrec})\times 2 m^*.$
- * 
*ipar[6]* ( = ndimi )
  The length of list *ispace*. Its size provides a constraint on *nmax*, the maximum
  number of subintervals.  Choose *ipar[6]* according to the formula
${\rm ipar[6]} = {\rm nmax}\times {\rm nsizei}$
  where
${\rm nsizei} = 3 + {\rm kdm}$
  with
$$\eqalign{ {\rm kdm} &= {\rm kd} + m^* \cr {\rm kd} &= k + {\rm ncomp} \cr {\rm nrec} &= {\it number\, of\, right\, end\, boundary\, conditions} \cr }$$ $$\eqalign{
    {\rm kdm} &= {\rm kd} + m^* \cr
    {\rm kd} &= k + {\rm ncomp} \cr
    {\rm nrec} &= {\it number\, of\, right\, end\, boundary\, conditions} \cr
  }$$
.
- * 
*ipar[7]* ( = iprint )
  output control
  
  - * 
-1, for full diagnostic printout
  - * 
0, for selected printout
  - * 
1, for no printout
- * 
*ipar[8]* ( = iread )
    
  - * 
0, causes colnew to generate a uniform initial mesh.
  - * 
1,
     if the initial mesh is provided by the user.  it
     is defined in fspace as follows:  the mesh
     aleft=x[1]<x[2]< ... <x[n]<x[n+1]=aright
     will occupy  fspace[1], ..., fspace[n+1]. the
     user needs to supply only the interior mesh
     points  fspace[j] = x[j], j = 2, ..., n.
  - * 
2,
     if the initial mesh is supplied by the user
     as with *ipar[8]*=1, and in addition no adaptive
     mesh selection is to be done.
- * 
*ipar[9]*  ( = iguess )
  
  - * 
0,
        if no initial guess for the solution is provided
  - * 
1,
        if an initial guess is provided by the user
        in subroutine guess.
  - * 
2,
        if an initial mesh and approximate solution
        coefficients are provided by the user in *fspace*.
        (the former and new mesh are the same).
  - * 
3,
        if a former mesh and approximate solution
        coefficients are provided by the user in *fspace*,
        and the new mesh is to be taken twice as coarse;
        i.e.,every second point from the former mesh.
  - * 
4,
        if in addition to a former initial mesh and
        approximate solution coefficients, a new mesh
        is provided in *fspace* as well.
       (see description of output for further details
        on iguess = 2, 3, and 4.)
- * 
*ipar[10]*
  
  - * 
0, if the problem is regular
  - * 
1, if the first relax factor is =rstart, and the
        nonlinear iteration does not rely on past convergence
        (use for an extra sensitive nonlinear problem only).
  - * 
2, if we are to return immediately upon  (a) two
        successive nonconvergences, or  (b) after obtaining
        error estimate for the first time.
- * 
*ipar[11]* ( = nfxpnt , the dimension of fixpnt)
    The number of fixed points in the mesh other than *aleft*
    and *aright*. 
    The code requires that all side condition points
    other than *aleft* and *aright* (see description of
    *zeta*) must be included as fixed points in *fixpnt*.
**ltol** — A list of length *ntol=ipar[4]*. *ltol[j]=k* specifies
that the j-th tolerance in *tol* controls the error
in the k-th component of z(u). 
The list *ltol* must be ordered with
$1 ≤ ltol[1] < ltol[2] < ... < ltol[ntol] ≤ mstar$.
**tol** — An list of length *ntol=ipar[4]*. *tol[j]* is the
error tolerance on the ltol[j]-th component
of z(u). 
Thus, the code attempts to satisfy
for j=1,...,ntol on each subinterval
$abs(z(v)-z(u))[k] ≤ tol(j)*abs(z(u))[k]+tol(j)$
if v(x) is the approximate solution vector.
**fixpnt** — An list of length *ipar[11]*. It contains the points, other than
*aleft* and *aright*, which are to be included in every mesh.
All side condition points other than *aleft* and *aright*
(see *zeta*) be included as fixed points in *fixpnt*.
**ispace** — An integer work list of length *ipar[6]*.
**fspace** — A real work list of length *ipar[5]*.
**fsub** — *fsub* is a function f(x,z1,...,z[mstar]) which realizes
the system of ODEs. 
It returns a list of *ncomp* values, one for each ODE.
Each value is the highest order
derivative in each ode in terms of of x,z1,...,z[mstar] .
**dfsub** — *dfsub* is a function df(x,z1,...,z[mstar]) for evaluating
the Jacobian of f.
**gsub** — Name of subroutine gsub(i,z1,z2,...,z[mstar]) for evaluating the i-th
component of the boundary value function g(z1,...,z[mstar]).
The independent variable x is not an argument of g.  The value
*x=zeta[i]* must be substituted in advance.
**dgsub** — Name of subroutine dgsub(i,z1,...,z[mstar]) for evaluating the
i-th row of the Jacobian of g(z1,...,z[mstar]).
**guess** — Name of subroutine to evaluate the initial
approximation for  (u(x)) and for dmval(u(x))= vector
of the mj-th derivatives of u(x).
This subroutine is needed only if using *ipar(9)* = 1.


The return value of *colnew_expert* is the list
*[iflag, fspace, ispace]*, where:



**iflag** — The mode of return from *colnew_expert*.
   - *
    
= 1 for normal return
- *
    
= 0 if the collocation matrix is singular.
- *
    
= -1 if the expected no. of subintervals exceeds storage specifications.
- *
    
= -2 if the nonlinear iteration has not converged.
- *
    
= -3 if there is an input data error.
**fspace** — A list of floats of length *ipar[5]*.
**ispace** — A list of integers of length *ipar[6]*.


`colnew_appsln` uses *fspace* and *ispace* to calculate solution values
at arbitrary points.  The lists can also be used to restart the solution process
with modified meshes and parameters.

See also: `colnew_appsln`.

