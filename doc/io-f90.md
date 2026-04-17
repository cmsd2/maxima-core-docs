## f90

<!-- category: IO -->
<!-- keywords: f90 -->
<!-- signatures: f90(expr_1, ..., expr_n) -->
### Function: f90 (expr_1, ..., expr_n)

Prints one or more expressions *expr_1*, ..., *expr_n*
as a Fortran 90 program.
Output is printed to the standard output.


`f90` prints output in the so-called "free form" input format for
Fortran 90: there is no special attention to column positions.
Long lines are split at a fixed width with the ampersand `&` continuation
character;
the number of output characters per line, not including ampersands,
is specified by `f90_output_line_length_max`.
`f90` outputs an ampersand at the end of a split line
and another at the beginning of the next line.


`load("f90")` loads this function.  See also the function `fortran`.


Examples:








```maxima
(%i1) load ("f90")$
(%i2) foo : expand ((xxx + yyy + 7)^4);
         4            3         3        2    2             2
(%o2) yyy  + 4 xxx yyy  + 28 yyy  + 6 xxx  yyy  + 84 xxx yyy
          2        3             2
 + 294 yyy  + 4 xxx  yyy + 84 xxx  yyy + 588 xxx yyy + 1372 yyy
      4         3          2
 + xxx  + 28 xxx  + 294 xxx  + 1372 xxx + 2401
(%i3) f90 ('foo = foo);
foo = yyy**4+4*xxx*yyy**3+28*yyy**3+6*xxx**2*yyy**2+84*xxx*yyy**2&
&+294*yyy**2+4*xxx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372*yyy+xxx**&
&4+28*xxx**3+294*xxx**2+1372*xxx+2401
(%o3)                         false
```


Multiple expressions.
Capture standard output into a file via the `with_stdout` function.









```maxima
(%i1) load ("f90")$
(%i2) foo : sin (3*x + 1) - cos (7*x - 2);
(%o2)              sin(3 x + 1) - cos(7 x - 2)
(%i3) with_stdout ("foo.f90",
                   f90 (x=0.25, y=0.625, 'foo=foo, 'stop, 'end));
(%o3)                         false
(%i4) printfile ("foo.f90");
x = 0.25
y = 0.625
foo = sin(3*x+1)-cos(7*x-2)
stop
end
(%o4)                        foo.f90
```

See also: `fortran`, `with_stdout`.

<!-- category: IO -->
<!-- keywords: f90_output_line_length_max -->
<!-- signatures: f90_output_line_length_max -->
### Variable: f90_output_line_length_max

Default value: 65


`f90_output_line_length_max` is the maximum number of characters of Fortran code
which are output by `f90` per line.
Longer lines of code are divided, and printed with an ampersand `&` at the end of an output line
and an ampersand at the beginning of the following line.


`f90_output_line_length_max` must be a positive integer.


Example:











```maxima
(%i1) load ("f90")$
(%i2) foo : expand ((xxx + yyy + 7)^4);
         4            3         3        2    2             2
(%o2) yyy  + 4 xxx yyy  + 28 yyy  + 6 xxx  yyy  + 84 xxx yyy
          2        3             2
 + 294 yyy  + 4 xxx  yyy + 84 xxx  yyy + 588 xxx yyy + 1372 yyy
      4         3          2
 + xxx  + 28 xxx  + 294 xxx  + 1372 xxx + 2401
(%i3) f90_output_line_length_max;
(%o3)                          65
(%i4) f90 ('foo = foo);
foo = yyy**4+4*xxx*yyy**3+28*yyy**3+6*xxx**2*yyy**2+84*xxx*yyy**2&
&+294*yyy**2+4*xxx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372*yyy+xxx**&
&4+28*xxx**3+294*xxx**2+1372*xxx+2401
(%o4)                         false
(%i5) f90_output_line_length_max : 40 $
(%i6) f90 ('foo = foo);
foo = yyy**4+4*xxx*yyy**3+28*yyy**3+6*xx&
&x**2*yyy**2+84*xxx*yyy**2+294*yyy**2+4*x&
&xx**3*yyy+84*xxx**2*yyy+588*xxx*yyy+1372&
&*yyy+xxx**4+28*xxx**3+294*xxx**2+1372*xx&
&x+2401
(%o6)                         false
```

