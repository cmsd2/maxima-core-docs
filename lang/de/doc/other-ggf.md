## ggf

<!-- category: Other -->
<!-- keywords: ggf -->
<!-- signatures: ggf(l) -->
### Function: ggf (l)

Compute the generating function (if it is a fraction of two
polynomials) of a sequence, its first terms being given. *l*
is a list of numbers.


The solution is returned as a fraction of two polynomials.
If no solution has been found, it returns with `done`.


This function is controlled by global variables *GGFINFINITY* and 
*GGFCFMAX*. See also *GGFINFINITY* and *GGFCFMAX*.


To use this function write first `load("ggf")`.

<!-- category: Other -->
<!-- keywords: GGFCFMAX -->
<!-- signatures: GGFCFMAX -->
### Variable: GGFCFMAX

Default value: 3


This is an option variable for function `ggf`.


When computing the continued fraction of the
generating function, if no good result has been found (see
the *GGFINFINITY* flag) after having computed *GGFCFMAX* partial
quotients, the generating function will be considered as
not being a fraction of two polynomials and the function will
exit. Put freely a greater value for more complicated
generating functions.


See also `ggf`.

<!-- category: Other -->
<!-- keywords: GGFINFINITY -->
<!-- signatures: GGFINFINITY -->
### Variable: GGFINFINITY

Default value: 3


This is an option variable for function `ggf`.


When computing the continued fraction of the
generating function, a partial quotient having a degree
(strictly) greater than *GGFINFINITY* will be discarded and
the current convergent will be considered as the exact value
of the generating function; most often the degree of all
partial quotients will be 0 or 1; if you use a greater value,
then you should give enough terms in order to make the
computation accurate enough.



See also `ggf`.

