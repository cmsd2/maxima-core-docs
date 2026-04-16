## Data Types and Structures

### Function: concat (arg_1, arg_2, ...)

Concatenates its arguments.  The arguments must evaluate to atoms.  The return
value is a symbol if the first argument is a symbol and a string otherwise.


`concat` evaluates its arguments.  The single quote `'` prevents
evaluation.


See also `sconcat`, that works on non-atoms, too, `simplode`,
`string` and `eval_005fstring`.
For complex string conversions see also `printf`.









```maxima
(%i1) y: 7$
(%i2) z: 88$
(%i3) concat (y, z/2);
(%o3)                          744
(%i4) concat ('y, z/2);
(%o4)                          y44
```


A symbol constructed by `concat` may be assigned a value and appear in
expressions.  The `::` (double colon) assignment operator evaluates its
left-hand side.










```maxima
(%i5) a: concat ('y, z/2);
(%o5)                          y44
(%i6) a:: 123;
(%o6)                          123
(%i7) y44;
(%o7)                          123
(%i8) b^a;
                               y44
(%o8)                         b
(%i9) %, numer;
                               123
(%o9)                         b
```


Note that although `concat (1, 2)` looks like a number, it is a string.






```maxima
(%i10) concat (1, 2) + 3;
(%o10)                       12 + 3
```

See also: `sconcat`, `simplode`, `string`, `eval_string`, `printf`, `::`.

### Function: sconcat (arg_1, arg_2, ...)

Concatenates its arguments into a string.  Unlike `concat`, the
arguments do *not* need to be atoms.


See also `concat`, `simplode`, `string` and `eval_005fstring`.
For complex string conversions see also `printf`.






```maxima
(%i1) sconcat ("xx[", 3, "]:", expand ((x+y)^3));
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
```


Another purpose for `sconcat` is to convert arbitrary objects to strings. 






```maxima
(%i1) sconcat (x);
(%o1)                           x


(%i2) stringp(%);
(%o2)                         true
```

See also: `concat`, `simplode`, `string`, `eval_string`, `printf`.

### Function: string (expr)

Converts `expr` to Maxima’s linear notation just as if it had been typed
in.


The return value of `string` is a string, and thus it cannot be used in a
computation.


See also `concat`, `sconcat`, `simplode` and
`eval_005fstring`.

See also: `concat`, `sconcat`, `simplode`, `eval_string`.

### Variable: stringdisp

Default value: `false`


When `stringdisp` is `true`, strings are displayed enclosed in double
quote marks.  Otherwise, quote marks are not displayed.


`stringdisp` is always `true` when displaying a function definition.


Examples:











```maxima
(%i1) stringdisp: false$

(%i2) "This is an example string.";
(%o2)              This is an example string.


(%i3) foo () :=
      print ("This is a string in a function definition.");
(%o3) foo() := 
              print("This is a string in a function definition.")

(%i4) stringdisp: true$

(%i5) "This is an example string.";
(%o5)             "This is an example string."
```

