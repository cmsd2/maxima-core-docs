## Eingabe und Ausgabe

<!-- category: IO -->
<!-- keywords: fortindent -->
<!-- signatures: fortindent -->
### Variable: fortindent

Default value: `0`


`fortindent` controls the left margin indentation of
expressions printed out by the `fortran` command.  `0` gives normal
printout (i.e., 6 spaces), and positive values will causes the
expressions to be printed farther to the right.

See also: `fortran`.

<!-- category: IO -->
<!-- keywords: fortran -->
<!-- signatures: fortran(expr) -->
### Function: fortran (expr)

Prints *expr* as a Fortran statement.
The output line is indented with spaces.
If the line is too long, `fortran` prints continuation lines.
`fortran` prints the exponentiation operator `^` as `**`,
and prints a complex number `a + b %i` in the form `(a,b)`.


*expr* may be an equation. If so, `fortran` prints an assignment
statement, assigning the right-hand side of the equation to the left-hand side.
In particular, if the right-hand side of *expr* is the name of a matrix,
then `fortran` prints an assignment statement for each element of the
matrix.


If *expr* is not something recognized by `fortran`,
the expression is printed in `grind` format without complaint.
`fortran` does not know about lists, arrays, or functions.


`fortindent` controls the left margin of the printed lines.
`0` is the normal margin (i.e., indented 6 spaces). Increasing
`fortindent` causes expressions to be printed further to the right.


When `fortspaces` is `true`, `fortran` fills out
each printed line with spaces to 80 columns.


`fortran` evaluates its arguments;
quoting an argument defeats evaluation.
`fortran` always returns `done`.


See also the function `function_f90` for printing one or more
expressions as a Fortran 90 program.


Examples:



(%i1) expr: (a + b)^12$
(%i2) fortran (expr);
      (b+a)**12                                                                 
(%o2)                         done
(%i3) fortran ('x=expr);
      x = (b+a)**12                                                             
(%o3)                         done
(%i4) fortran ('x=expand (expr));
      x = b**12+12*a*b**11+66*a**2*b**10+220*a**3*b**9+495*a**4*b**8+792
     1   *a**5*b**7+924*a**6*b**6+792*a**7*b**5+495*a**8*b**4+220*a**9*b
     2   **3+66*a**10*b**2+12*a**11*b+a**12
(%o4)                         done
(%i5) fortran ('x=7+5*%i);
      x = (7,5)                                                                 
(%o5)                         done
(%i6) fortran ('x=[1,2,3,4]);
      x = [1,2,3,4]                                                             
(%o6)                         done
(%i7) f(x) := x^2$
(%i8) fortran (f);
      f                                                                         
(%o8)                         done

See also: `grind`, `fortspaces`, `function_f90`.

<!-- category: IO -->
<!-- keywords: fortspaces -->
<!-- signatures: fortspaces -->
### Variable: fortspaces

Default value: `false`


When `fortspaces` is `true`, `fortran` fills out
each printed line with spaces to 80 columns.

