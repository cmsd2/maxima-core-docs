## Miscellaneous Options

### Variable: askexp

When `asksign` is called,
`askexp` is the expression `asksign` is testing.


At one time, it was possible for a user to inspect `askexp`
by entering a Maxima break with control-A.

### Variable: genindex

Default value: `i`


`genindex` is the alphabetic prefix used to generate the
next variable of summation when necessary.

### Variable: gensumnum

Default value: 0


`gensumnum` is the numeric suffix used to generate the next variable
of summation.  If it is set to `false` then the index will consist only
of `genindex` with no numeric suffix.

### Function: gensym (gensym, gensym, x)

`gensym()` creates and returns a fresh symbol.


The name of the new symbol is the concatenation of a prefix, which defaults to
"g", and a suffix, which is an integer that defaults to the value of an internal
counter.


If *x* is supplied, and is a string, then that string is used as a prefix 
instead of "g" for this call to gensym only.


If *x* is supplied, and is a nonnegative integer, then that integer, instead
of the value of the internal counter, is used as the suffix for this call to
gensym only.


If and only if no explicit suffix is supplied, the internal counter is
incremented after it is used.


Examples:








```maxima
(%i1) gensym();
(%o1)                         g887
(%i2) gensym("new");
(%o2)                        new888
(%i3) gensym(123);
(%o3)                         g123
```

### Variable: packagefile

Default value: `false`


Package designers who use `save` or `translate` to create packages
(files) for others to use may want to set `packagefile: true` to prevent
information from being added to Maxima’s information-lists (e.g.
`values`, `functions`) except where necessary when the file is
loaded in.  In this way, the contents of the package will not get in the user’s
way when he adds his own data.  Note that this will not solve the problem of
possible name conflicts.  Also note that the flag simply affects what is output
to the package file.  Setting the flag to `true` is also useful for
creating Maxima init files.

See also: `save`, `translate`, `values`, `functions`.

### Function: remvalue (remvalue, name_1, ..., name_n, remvalue, all)

Removes the values of user variables *name_1*, ..., *name_n*
(which can be subscripted) from the system.


`remvalue (all)` removes the values of all variables in `values`,
the list of all variables given names by the user
(as opposed to those which are automatically assigned by Maxima).


See also `values`.

See also: `values`.

### Function: rncombine (expr)

Transforms *expr* by combining all terms of *expr* that have
identical denominators or denominators that differ from each other by
numerical factors only.  This is slightly different from the behavior
of `combine`, which collects terms that have identical denominators.


Setting `pfeformat: true` and using `combine` yields results similar
to those that can be obtained with `rncombine`, but `rncombine` takes
the additional step of cross-multiplying numerical denominator factors.
This results in neater forms, and the possibility of recognizing some
cancellations.


`load("rncomb")` loads this function.

See also: `combine`.

### Function: setup_autoload (filename, function_1, ..., function_n)

Specifies that if any of *function_1*, ..., *function_n* are
referenced and not yet defined, *filename* is loaded via `load`.
*filename* usually contains definitions for the functions specified,
although that is not enforced.


`setup_autoload` does not work for `memoizing-functions`.


`setup_autoload` quotes its arguments.


Example:









```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma function ultraspherical
Warning - you are redefining the Macsyma function legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);
                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

See also: `memoizing-functions`.

### Function: tcl_output (tcl_output, list, i0, skip, tcl_output, list, i0, tcl_output, list_1, ..., list_n, i)

Prints elements of a list enclosed by curly braces `{ }`,
suitable as part of a program in the Tcl/Tk language.


`tcl_output (list, i0, skip)`
prints *list*, beginning with element *i0* and printing elements
`i0 + skip`, `i0 + 2 skip`, etc.


`tcl_output (list, i0)`
is equivalent to `tcl_output (list, i0, 2)`.


`tcl_output ([list_1, ..., list_n], i)`
prints the *i*’th elements of *list_1*, ..., *list_n*.


Examples:













```maxima
(%i1) tcl_output ([1, 2, 3, 4, 5, 6], 1, 3)$

 {1.000000000     4.000000000     
 }
(%i2) tcl_output ([1, 2, 3, 4, 5, 6], 2, 3)$

 {2.000000000     5.000000000     
 }
(%i3) tcl_output ([3/7, 5/9, 11/13, 13/17], 1)$

 {((RAT SIMP) 3 7) ((RAT SIMP) 11 13) 
 }
(%i4) tcl_output ([x1, y1, x2, y2, x3, y3], 2)$

 {$Y1 $Y2 $Y3 
 }
(%i5) tcl_output ([[1, 2, 3], [11, 22, 33]], 1)$

 {SIMP 1.000000000     11.00000000     
 }
```

