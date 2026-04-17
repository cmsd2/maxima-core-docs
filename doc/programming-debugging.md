## Debugging

<!-- category: Programming -->
<!-- keywords: debugmode -->
<!-- signatures: debugmode -->
### Variable: debugmode

Default value: `false`


When `debugmode` is `true`, Maxima will start the Maxima debugger
when a Maxima error occurs.  At this point the user may enter commands to
examine the call stack, set breakpoints, step through Maxima code, and so on.
See `debugging` for a list of Maxima debugger commands.


When `debugmode` is `lisp`, Maxima will start the Lisp debugger
when a Maxima error occurs.


In either case, enabling `debugmode` will not catch Lisp errors.

<!-- category: Programming -->
<!-- keywords: refcheck -->
<!-- signatures: refcheck -->
### Variable: refcheck

Default value: `false`


When `refcheck` is `true`, Maxima prints a message
each time a bound variable is used for the first time in a
computation.

<!-- category: Programming -->
<!-- keywords: setcheck -->
<!-- signatures: setcheck -->
### Variable: setcheck

Default value: `false`


If `setcheck` is set to a list of variables (which can
be subscripted), 
Maxima prints a message whenever the variables, or
subscripted occurrences of them, are bound with the
ordinary assignment operator `:`, the `::` assignment
operator, or function argument binding,
but not the function assignment `:=` nor the macro assignment
`::=` operators.
The message comprises the name of the variable and the
value it is bound to.


`setcheck` may be set to `all` or `true` thereby
including all variables.


Each new assignment of `setcheck` establishes a new list of variables to
check, and any variables previously assigned to `setcheck` are forgotten.


The names assigned to `setcheck` must be quoted if they would otherwise
evaluate to something other than themselves.
For example, if `x`, `y`, and `z` are already bound, then enter



```maxima
setcheck: ['x, 'y, 'z]$
```


to put them on the list of variables to check.


No printout is generated when a
variable on the `setcheck` list is assigned to itself, e.g., `X: 'X`.

<!-- category: Programming -->
<!-- keywords: setcheckbreak -->
<!-- signatures: setcheckbreak -->
### Variable: setcheckbreak

Default value: `false`


When `setcheckbreak` is `true`,
Maxima will present a break prompt 
whenever a variable on the `setcheck` list is assigned a new value.
The break occurs before the assignment is carried out.
At this point, `setval` holds the value to which the variable is 
about to be assigned.
Hence, one may assign a different value by assigning to `setval`.


See also `setcheck` and `setval`.

See also: `setcheck`, `setval`.

<!-- category: Programming -->
<!-- keywords: setval -->
<!-- signatures: setval -->
### Variable: setval

Holds the value to which a variable is about to be set when
a `setcheckbreak` occurs.
Hence, one may assign a different value by assigning to `setval`.


See also `setcheck` and `setcheckbreak`.

See also: `setcheckbreak`, `setval`, `setcheck`.

<!-- category: Programming -->
<!-- keywords: timer -->
<!-- signatures: timer(f_1, ..., f_n), timer(all), timer() -->
### Function: timer (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*, `timer` puts each one on the
list of functions for which timing statistics are collected.
`timer(f)$ timer(g)$` puts `f` and then `g` onto the list;
the list accumulates from one call to the next.


`timer(all)` puts all user-defined functions (as named by the global
variable `functions`) on the list of timed functions.


With no arguments,  `timer` returns the list of timed functions.


Maxima records how much time is spent executing each function
on the list of timed functions.
`timer_info` returns the timing statistics, including the
average time elapsed per function call, the number of calls, and the
total time elapsed.
`untimer` removes functions from the list of timed functions.


`timer` quotes its arguments.
`f(x) := x^2$ g:f$ timer(g)$` does not put `f` on the timer list.


If `trace(f)` is in effect, then `timer(f)` has no effect;
`trace` and `timer` cannot both be in effect at the same time.


See also `timer_reset` and `timer_005fdevalue`.

See also: `timer_reset`, `timer_devalue`.

<!-- category: Programming -->
<!-- keywords: timer_devalue -->
<!-- signatures: timer_devalue -->
### Variable: timer_devalue

Default value: `false`


When `timer_devalue` is `true`, Maxima subtracts from each timed
function the time spent in other timed functions.  Otherwise, the time reported
for each function includes the time spent in other functions.
Note that time spent in untimed functions is not subtracted from the
total time.


See also `timer` and `timer_005finfo`.

See also: `timer`, `timer_info`.

<!-- category: Programming -->
<!-- keywords: timer_info -->
<!-- signatures: timer_info(f_1, ..., f_n), timer_info() -->
### Function: timer_info (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*, `timer_info` returns a matrix
containing timing information for each function.
With no arguments, `timer_info` returns timing information for
all functions currently on the timer list.


The matrix returned by `timer_info` contains the function name,
time per function call, number of function calls, total time,
and `gctime`, which meant "garbage collection time" in the original Macsyma
but is now always zero.


The data from which `timer_info` constructs its return value
can also be obtained by the `get` function:



```maxima
get(f, 'calls);  get(f, 'runtime);  get(f, 'gctime);
```


See also `timer` and `timer_005freset`.

See also: `timer`, `timer_reset`.

<!-- category: Programming -->
<!-- keywords: timer_reset -->
<!-- signatures: timer_reset(f_1, ..., f_n), timer_reset() -->
### Function: timer_reset (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*,
`timer_reset` sets the accumulated elapsed time
for each function
to zero.


With no arguments,
`timer_reset` sets the accumulated elapsed time
for each function on the global timer list
to zero.

<!-- category: Programming -->
<!-- keywords: trace -->
<!-- signatures: trace(f_1, ..., f_n), trace(all), trace() -->
### Function: trace (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*, `trace` instructs Maxima to
print out debugging information whenever those functions are called.
`trace(f)$ trace(g)$` puts `f` and then `g` onto the list of
functions to be traced; the list accumulates from one call to the next.


`trace(all)` puts all user-defined functions (as named by the global
variable `functions`) on the list of functions to be traced.


With no arguments,
`trace` returns a list of all the functions currently being traced.


The `untrace` function disables tracing.
See also `trace_005foptions`.


`trace` quotes its arguments.  Thus,
`f(x) := x^2$ g:f$ trace(g)$` does not put `f` on the trace list.


When a function is redefined, it is removed from the timer list.
Thus after `timer(f)$ f(x) := x^2$`,
function `f` is no longer on the timer list.


If `timer (f)` is in effect, then `trace (f)` has no effect;
`trace` and `timer` can’t both be in effect for the same function.

See also: `trace_options`.

<!-- category: Programming -->
<!-- keywords: trace_break_arg -->
<!-- signatures: trace_break_arg -->
### Variable: trace_break_arg

When a traced function stops at a breakpoint,
`trace_break_arg` is bound to the value of function arguments when entering the function,
or the return value of the function, when exiting.


Breakpoints for traced functions are specified by the option keyword `break` of the function `trace_options`,
which see.

<!-- category: Programming -->
<!-- keywords: trace_options -->
<!-- signatures: trace_options(f, option_1, ..., option_n), trace_options(f) -->
### Function: trace_options (f, option_1, ..., option_n)

Sets the trace options for function *f*.
Any previous options are superseded.
`trace_options (f, ...)` has no effect unless `trace (f)`
is also called (either before or after `trace_options`).


`trace_options (f)` resets all options to their default values.


The following option keywords are recognized.
The presence of the option keyword alone enables the option unconditionally.
Specifying an option keyword with a predicate function *p* as its argument
makes the option conditional on the predicate.



- *
`noprint`, `noprint(p)`
Do not print a message at function entry and exit.
- *
`break`, `break(p)`
Stop execution before the function is entered, and after the function is exited.
See also `break`.
The arguments of the function and its return value are available as `trace_break_arg`
when entering and exiting the function, respectively.
- *
`lisp_print`, `lisp_print(p)`
Display arguments and return values as Lisp objects.
- *
`info`, `info(p)`
Display the return value of *p* at function entry and exit.
The function *p* may also have side effects,
such as displaying output or modifying global variables.
- *
`errorcatch`, `errorcatch(p)`
Catch errors, giving the option to signal an error,
retry the function call, or specify a return value.


The predicate function, if supplied, is called with four arguments.



- *
The recursion level for the function, an integer.
- *
Whether the function is being entered or exited, indicated by a symbol, either `enter` or `exit`, respectively.
- *
The name of the function, a symbol.
- *
The arguments of the traced function (on entering) or the function return value (on exiting).


If the predicate function returns `false`,
the corresponding trace option is disabled;
if any value other than `false` value is returned, the trace option is enabled.


`trace_options` quotes (does not evaluate) its arguments.


Examples:


The presence of the option keyword alone enables the option unconditionally.








```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1);
(%o1)    ff(n) := if equal(n, 0) then 1 else n ff(n - 1)
(%i2) trace (ff);
(%o2)                         [ff]
(%i3) trace_options (ff, lisp_print, break);
(%o3)                  [lisp_print, break]
(%i4) ff(3);
Trace entering ff level 1 

Entering a Maxima break point. Type 'exit;' to resume.
_trace_break_arg;
[3]
_exit;
(1 ENTER $FF (3))
Trace entering ff level 2 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
 (2 ENTER $FF (2))
Trace entering ff level 3 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
  (3 ENTER $FF (1))
Trace entering ff level 4 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
   (4 ENTER $FF (0))
Trace exiting ff level 4 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
   (4 EXIT $FF 1)
Trace exiting ff level 3 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
  (3 EXIT $FF 1)
Trace exiting ff level 2 

Entering a Maxima break point. Type 'exit;' to resume.
_exit;
 (2 EXIT $FF 2)
Trace exiting ff level 1 

Entering a Maxima break point. Type 'exit;' to resume.
_trace_break_arg;
6
_exit;
(1 EXIT $FF 6)
(%o4)                           6
```


Specifying an option keyword with a predicate function *p* as its argument
makes the option conditional on the predicate.









```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1);
(%o1)    ff(n) := if equal(n, 0) then 1 else n ff(n - 1)
(%i2) trace (ff);
(%o2)                         [ff]
(%i3) trace_options (ff, break(pp));
(%o3)                      [break(pp)]
(%i4) pp (level, direction, fnname, item) := (print (item), fnname = 'ff and level = 3 and direction = 'exit);
(%o4) pp(level, direction, fnname, item) := 
(print(item), (fnname = 'ff) and (level = 3)
 and (direction = 'exit))
(%i5) ff(6);
[6] 
1 Enter ff [6]
[5] 
 2 Enter ff [5]
[4] 
  3 Enter ff [4]
[3] 
   4 Enter ff [3]
[2] 
    5 Enter ff [2]
[1] 
     6 Enter ff [1]
[0] 
      7 Enter ff [0]
1 
      7 Exit  ff 1
1 
     6 Exit  ff 1
2 
    5 Exit  ff 2
6 
   4 Exit  ff 6
24 
Trace exiting ff level 3 

Entering a Maxima break point. Type 'exit;' to resume.
_trace_break_arg;
24
_exit;
  3 Exit  ff 24
120 
 2 Exit  ff 120
720 
1 Exit  ff 720
(%o5)                          720
```

<!-- category: Programming -->
<!-- keywords: untimer -->
<!-- signatures: untimer(f_1, ..., f_n), untimer() -->
### Function: untimer (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*,
`untimer` removes each function from the timer list.


With no arguments, `untimer` removes all functions currently on the timer
list.


After `untimer (f)` is executed, `timer_info (f)` still returns
previously collected timing statistics,
although `timer_info()` (with no arguments) does not
return information about any function not currently on the timer list.
`timer (f)` resets all timing statistics to zero
and puts `f` on the timer list again.

<!-- category: Programming -->
<!-- keywords: untrace -->
<!-- signatures: untrace(f_1, ..., f_n), untrace() -->
### Function: untrace (f_1, ..., f_n)

Given functions *f_1*, ..., *f_n*,
`untrace` disables tracing enabled by the `trace` function.
With no arguments, `untrace` disables tracing for all functions.


`untrace` returns a list of the functions for which 
it disabled tracing.

