## rk_adaptive

<!-- category: Numerical -->
<!-- keywords: rk_adaptive -->
<!-- signatures: rk_adaptive(expr, vars, vars_initval, var,  -->
### Function: rk_adaptive ((expr, vars, vars_initval, var,)

*startval*, *endval*, *params1...*)


Tries to solve the ODE whose derivates are defined by `expr` to the variables
`vars`, starting at their initial values `vars_initval`.
The independent variable (in physics: normally time) is `var`, being stepped from
`startval` to `endval`.


Sometimes it speeds up the calculation to use a floating-point number as
`startval`, as using floars will prevent all results from becoming endless rational
numbers.


The following optional parameters are accepted:



- * 
`maxstep=num`: The maximum step size to be used.
- * 
`minstep=num`: The minimum step size to be used.
- * 
`timestep_initial=num`: The initial guess for the optimum time step to start with.
- * 
`maxabserr=num`: The maximum absolute error of the resulting curves.
- * 
`maxrelerr=num`: The maximum relative error of the resulting curves as a
      fallback for variables with big values for which `maxabserr` might be too sensitive.


See also `rk`.


Example:





```maxima
maxima
(%i1) pnts:rk_adaptive(-1/10*x,x,1,t,0,100)  $
```

See also: `rk`.

