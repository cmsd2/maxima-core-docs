## odepack

### Function: dlsode_init (fex, vars, method)

This must be called before running the solver.  This function returns
a state object for use in the solver.  The user must not modify the
state.


The ODE to be solved is given in *fex*, which is a list of the
equations.  *vars* is a list of independent variable and the
dependent variables.  The list of dependent variables must be in the
same order as the equations if *fex*.  Finally, *method*
indicates the method to be used by the solver:


> **10** — Nonstiff (Adams) method, no Jacobian used.
> **21** — Stiff (BDF) method, user-supplied full Jacobian.
> **22** — Stiff method, internally generated full Jacobian.



The returned state object is a list of lists.  The sublist is a list
of two elements:

> **f** — The compiled function for the ODE.
> **vars** — The list independent and dependent variables (*vars*).
> **mf** — The method to be used (*method*).
> **neq** — The number of equations.
> **lrw** — Length of the work vector for real values.
> **liw** — Length of the work vector for integer values.
> **rwork** — Lisp array holding the real-valued work vector.
> **iwork** — Lisp array holding the integer-valued work vector.
> **fjac** — Compiled analytical Jacobian of the equations



See also `dlsode_005fstep`.  `Getting-Started-with-ODEPACK` for
an example of usage.

See also: `dlsode_step`, `Getting-Started-with-ODEPACK`.

### Function: dlsode_step (inity, t, tout, rtol, atol, istate, state)

Performs one step of the solver, returning the values of the
independent and dependent variables, a success or error code.


The parameters for `dlsode_step` are:


> **inity** — For the first call (when istate = 1), the initial values
> **t** — Current value of the independent value
> **tout** — Next point where output is desired which must not be equal to *t*.
> **rtol** — relative tolerance parameter
> **atol** — Absolute tolerance parameter, scalar of vector.  If
> scalar, it applies to all dependent variables.
> Otherwise it must be the tolerance for each dependent
> variable. 
> Use *rtol* = 0 for pure absolute error and use *atol* = 0
> for pure relative error.
> **istate** — 1 for the first call to dlsode, 2 for subsequent calls.
> **state** — state returned by dlsode_init.



The output is a list of the following items:

> **t** — independent variable value
> **y** — list of values of the dependent variables at time t.
> **istate** — Integration status: > **1** — no work because tout = tt
> > **2** — successful result
> > **-1** — Excess work done on this call
> > **-2** — Excess accuracy requested
> > **-3** — Illegal input detected
> > **-4** — Repeated error test failures
> > **-5** — Repeated convergence failures (perhaps bad Jacobian or wrong choice of
> > mf or tolerances)
> > **-6** — Error weight because zero during problem (solution component is
> > vanished and atol(i) = 0.
> **info** — association list of various bits of information: > **n_steps** — total steps taken thus far
> > **n_f_eval** — total number of function evals
> > **n_j_eval** — total number of Jacobian evals
> > **method_order** — method order
> > **len_rwork** — Actual length used for real work array
> > **len_iwork** — Actual length used for integer work array



See also `dlsode_005finit`.  `Getting-Started-with-ODEPACK` for
an example of usage.

See also: `dlsode_init`, `Getting-Started-with-ODEPACK`.

