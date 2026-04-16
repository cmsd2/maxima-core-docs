## IO

### Function: %coerce_bag (op, expr)

Attempts to coerce *expr* into an expression with *op* (one of
`=, #, <, <=, >, >=, [` or matrix) as the top-level operator. It
coerces the expression by swapping operands between layers but only if
adjacent layers are also lists, matrices or relations. This model
assumes that a list of equations, for example, can be viewed as an
equation whose sides are lists. Certain combinations, particularly those
involving inequalities may not be meaningful, however, so some caution
is advised.

### Variable: %edispflag

Default value: `false`


When `%edispflag` is `true`, Maxima displays `%e` to a negative
exponent as a quotient.  For example, `%e^-x` is displayed as
`1/%e^x`.  See also `exptdispflag`.


Example:








```maxima
maxima

(%i1) %e^-10;
                               - 10
(%o1)                        %e

(%i2) %edispflag:true$

(%i3) %e^-10;
                               1
(%o3)                         ----
                                10
                              %e
```

See also: `exptdispflag`.

### Function: %format_piece (piece, nth)

`lratsubst`’s `eqns` into expression and the result is formatted at the next layer.
Format a given piece of an expression, automatically accounting for
subtemplates and the remaining template chain. A specific subtemplate,
rather than the next one, can be selected by specifying *nth*.

### Variable: absboxchar

Default value: `!`


`absboxchar` is the character used to draw absolute value
signs around expressions which are more than one line tall.


`absboxchar` is only used when `display2d_unicode` is `false`.


Example:







```maxima
maxima
(%i1) display2d_unicode: false $

(%i2) abs((x^3+1));
                            | 3    |
(%o2)                       |x  + 1|
```

### Function: alt_display_output_type (form)

Determine the type of output to be printed. *Form* must be a lisp
form suitable for printing via Maxima’s built-in `displa`
function. At present, this function returns one of three values:
*text*, *label* or *unknown*.


An example where `alt_display_output_type` is used. In
`my_display`, a text form is printed between a pair of tags
TEXT;>> and <<TEXT; while a label form is printed between
a pair tags OUT;>> and <<OUT; in addition to the usual
output label.


The function `set_prompt` also ensures that input labels are
printed between matching PROMPT;>> and <<PROMPT; tags.


Thanks to
[https://sourceforge.net/p/maxima/mailman/maxima-discuss/thread/7792c096-7e07-842d-0c3a-b2f039ef1f15%40gmail.com/#msg37235035Eric Stemmler]().



(%i1) (load("mactex-utilities"), load("alt-display.mac")) $

(%i2) define_alt_display(my_display(form),
block([type,txttmplt,labtmplt], 
txttmplt:"~%TEXT;>>~%~a~%<<TEXT;~%",
labtmplt:"~%OUT;>>~%(~a) ~a~a~a~%<<OUT;~%",
type:alt_display_output_type(form),
if type='text then 
   printf(true,txttmplt,first(form))
else if type='label then 
     printf(true,labtmplt,first(form),"$$",tex1(second(form)),"$$")
else 
     block([alt_display1d:false, alt_display2d:false], displa(form)))) $

(%i3) (set_prompt('prefix, "PROMPT;>>",'suffix, "<<PROMPT;"), 
      set_alt_display(1,my_display)) $

PROMPT;>>(%i4) <<PROMPT;integrate(x^n,x);
PROMPT;>>
TEXT;>>
Is n equal to -1?
<<TEXT;
<<PROMPT;
n;

OUT;>>
(%o4) $$\frac{x^{n+1}}{n+1}$$
<<OUT;
PROMPT;>>(%i5) <<PROMPT;

See also: `set_prompt`.

### Function: appendfile (filename)

Appends a console transcript to *filename*.  `appendfile` is the same
as `writefile`, except that the transcript file, if it exists, is
always appended.


`closefile` closes the transcript file opened by `appendfile` or
`writefile`.

See also: `writefile`, `closefile`.

### Function: assume_external_byte_order (byte_order_flag)

Tells `numericalio` the byte order for reading and writing binary data.
Two values of *byte_order_flag* are recognized:
`lsb` which indicates least-significant byte first, also called little-endian byte order;
and `msb` which indicates most-significant byte first, also called big-endian byte order.


If not specified, `numericalio` assumes the external byte order is most-significant byte first.

### Function: batch (batch, filename, batch, filename, option, batch, S, batch, S, option)

`batch(filename)` reads Maxima expressions from *filename* and 
evaluates them.  `batch` searches for *filename* in the list 
`file_005fsearch_005fmaxima`.  See also `file_005fsearch`.


`batch(S)` reads Maxima expressions from the input stream *S*
as created by `openr`.
The behavior of `batch` in this case is the same as if the input
were a file name, and in the remainder of this description,
what is said about input files applies to input streams as well,
except that the comments about searching for files do not apply to streams.


`batch(filename, demo)` is like `demo(filename)`.
In this case `batch` searches for *filename* in the list
`file_005fsearch_005fdemo`.  See `demo`.


`batch(filename, test)` is like `run_testsuite` with the
option `display_all=true`.  For this case `batch` searches 
*filename* in the list `file_search_maxima` and not in the list
`file_search_tests` like `run_testsuite`.  Furthermore,
`run_testsuite` runs tests which are in the list
`testsuite_005ffiles`.  With `batch` it is possible to run any file in
a test mode, which can be found in the list `file_search_maxima`.  This is
useful, when writing a test file.


*filename* comprises a sequence of Maxima expressions, each terminated with
`;` or `$`.  The special variable `%` and the function
`%th` refer to previous results within the file.  The file may include
`:lisp` constructs.  Spaces, tabs, and newlines in the file are ignored.
A suitable input file may be created by a text editor or by the
`stringout` function.


`batch` reads each input expression from *filename*, displays
the input to the console, computes the corresponding output expression,
and displays the output expression. Input labels are assigned to the
input expressions and output labels are assigned to the output
expressions. `batch` evaluates every input expression in the file
unless there is an error. If user input is requested (by `asksign`
or `askinteger`, for example) `batch` pauses to collect
the requisite input and then continue; if `batch_answers_from_file`
is `true`, the input is read from the file itself. See also
`batch_005fanswers_005ffrom_005ffile`.




It may be possible to halt `batch` by typing `control-C` at the
console.  The effect of `control-C` depends on the underlying Lisp
implementation.


`batch` has several uses, such as to provide a reservoir for working
command lines, to give error-free demonstrations, or to help organize one’s
thinking in solving complex problems.


`batch` evaluates its arguments.


When called with no second argument or with the option `demo`,
`batch` returns the path of *filename*,
if the argument is a file name,
or the path of the file for which the input stream was opened,
if the argument is a file input stream.
If the argument is a string input stream,
a representation of the input stream is returned.


When called with the option `test`, the return value
is a an empty list `[]` or a list with *filename* and the numbers of
the tests which have failed.


See also `load`, `batchload`,
`batch_answers_from_file`, and `demo`.

See also: `file_search_maxima`, `file_search`, `openr`, `file_search_demo`, `demo`, `run_testsuite`, `file_search_tests`, `testsuite_files`, `%`, `%th`, `stringout`, `asksign`, `askinteger`, `batch_answers_from_file`, `load`, `batchload`.

### Variable: batch_answers_from_file

Default value: `false`


If `true`, then `batch` reads answers to interactive questions
from its input file or stream.


Example: Maxima’s interactive testsuite includes something like
following.



```maxima
maxima
[asksign (foo), sign (foo), sign (foo)];
p;
[pos, pos, pos];
```


The first line makes Maxima ask a question; when
`batch_answers_from_file` is `true`, the second line is read
as the answer to the question; and the third line provides the expected
result.


The command-line option `--batch-string` binds
`batch_answers_from_file` to `true`. The `run_testsuite`
function, as a default, also binds `batch_answers_from_file` to
`true`. See also `command_line_options` and `run_005ftestsuite`.

See also: `command_line_options`, `run_testsuite`.

### Function: batchload (batchload, filename, batchload, S)

Reads Maxima expressions from input file *filename* or input stream *S*
and evaluates them,
without displaying the input or output expressions and without assigning labels to
output expressions.  Printed output (such as produced by `print` or
`describe`) is displayed, however.


The special variable `%` and the function `%th` refer to previous
results from the interactive interpreter, not results within the file.
The file cannot include `:lisp` constructs.


`batchload` evaluates its argument.


`batchload` returns the path of *filename*,
if the argument is a file name,
or the path of the file for which the input stream was opened,
if the argument is a file input stream.
If the argument is a string input stream,
a representation of the input stream is returned.


See also `batch`, and `load`.

See also: `print`, `describe`, `%`, `%th`, `batch`, `load`.

### Variable: ccurind

Default: 0


Number of blank spaces printed at the beginning of each line of
generated’C’ code.

### Function: charat (string, n)

Returns the *n*-th character of *string*.
The first character in *string* is returned with *n* = 1. 



```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
(%i2) charlist("Lisp")[1];
(%o2)                           L
```

### Function: charlist (string)

Returns the list of all characters in *string*. 



```maxima
(%i1) charlist("Lisp");
(%o1)                     [L, i, s, p]
```

### Variable: clinelen

Default: 80


Maximum number of characters printed on each line of generated ’C’ code.

### Function: close (stream)

Closes *stream* and returns `true` if *stream* had been open.

### Function: closefile ()

Closes the transcript file opened by `writefile` or `appendfile`.

See also: `writefile`, `appendfile`.

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

### Function: copy_file (file1, file2)

copies file *file1* to *file2*

### Variable: dblfloat

Default: **false** If dblfloat is set to
true, floating point numbers in gentran output in implementations (such
as Windows Maxima under CLISP) in which float and double-float are the
same will be printed as *.d0. In implementations in which float and
double-float are different, floats will be coerced to double-float
before being printed.

### Function: declare_index_properties (declare_index_properties, a, p_1, p_2, p_3, ..., declare_index_properties, a, b, c, ..., p_1, p_2, p_3, ...)

Declares the properties of indices applied to the symbol *a*
or each of the of symbols *a*, *b*, *c*, ....
If multiple symbols are given,
the whole list of properties applies to each symbol.


Given a symbol with indices, `a[i_1, i_2, i_3, ...]`,
the `k`-th property *p_k* applies to the `k`-th index *i_k*.
There may be any number of index properties, in any order. 


Each property *p_k* must one of these four recognized properties:
`postsubscript`, `postsuperscript`, `presuperscript`, or `presubscript`,
to denote indices which are displayed, respectively,
to the right and below, to the right and above, to the left and above, or to the left and below.


Index properties apply only to the 2-dimensional display of indexed variables
(i.e., when `display2d` is `true`)
and TeX output via `tex`.
Otherwise, index properties are ignored.
Index properties do not change the input of indexed variables,
do not change the algebraic properties of indexed variables,
and do not change the 1-dimensional display of indexed variables.


`declare_index_properties` quotes (does not evaluate) its arguments.


`remove_index_properties` removes index properties.
`kill` also removes index properties (and all other properties).


`get_index_properties` retrieves index properties.


Examples:


Given a symbol with indices, `a[i_1, i_2, i_3, ...]`,
the `k`-th property *p_k* applies to the `k`-th index *i_k*.
There may be any number of index properties, in any order. 













```maxima
maxima

(%i1) declare_index_properties (A, [presubscript, postsubscript]);
(%o1)                         done


(%i2) declare_index_properties (B, [postsuperscript, postsuperscript,
 presuperscript]);
(%o2)                         done


(%i3) declare_index_properties (C, [postsuperscript, presubscript,
 presubscript, presuperscript]);
(%o3)                         done


(%i4) A[w, x];
(%o4)                           A
                               w x


(%i5) B[w, x, y];
                             y w, x
(%o5)                         B


(%i6) C[w, x, y, z];
                                z w
(%o6)                            C
                             x, y
```


Index properties apply only to the 2-dimensional display of indexed variables and TeX output.
Otherwise, index properties are ignored.














```maxima
maxima

(%i1) declare_index_properties (A, [presubscript, postsubscript]);
(%o1)                         done


(%i2) A[w, x];
(%o2)                           A
                               w x


(%i3) tex (A[w, x]);
$${}_{w}A_{x}$$
(%o3)                         false

(%i4) display2d: false $

(%i5) A[w, x];
(%o5) A[w,x]

(%i6) display2d: true $

(%i7) grind (A[w, x]);
A[w,x]$
(%o7)                         done

(%i8) stringdisp: true $

(%i9) string (A[w, x]);
(%o9)                       "A[w,x]"
```

See also: `display2d`.

### Function: define_alt_display (function, input, expr)

This function is similar to `define`: it evaluates its arguments
and expands into a function definition. The *function* is a
function of a single input *input*. For convenience, a substitution
is applied to *expr* after evaluation, to provide easy access to
Lisp variable names.


Set a time-stamp on each prompt:


```maxima
(%i1) load("alt-display.mac")$

(%i2) display2d: false$

(%i3) define_alt_display(time_stamp(x),
                block([alt_display1d:false,alt_display2d:false],
                      prompt_prefix:printf(false,"~a~%",timedate()),
                      displa(x)));

(%o3) time_stamp(x):=block(
                 [\*alt\-display1d\*:false,
                  \*alt\-display2d\*:false],
                 \*prompt\-prefix\*
                  :printf(false,"~a~%",timedate()),displa(x))
(%i4) set_alt_display(1,time_stamp);

(%o4) done
2017-11-27 16:15:58-06:00
(%i5)
```


The input line `%i3` defines `time_stamp` using
`define_alt_display`. The output line `%o3` shows that the
Maxima variable names `alt_display1d`, `alt_display2d` and
`prompt_prefix` have been replaced by their Lisp translations, as
has `displa` been replaced by `?displa` (the display
function).


The display variables `alt_display1d` and `alt_display2d` are
both bound to `false` in the body of `time_stamp` to prevent
an infinite recursion in `displa`.

### Function: delete_file (file1)

deletes file *file1*

### Function: directory (path)

Returns a list of the files and directories found in *path*
in the file system.


*path* may contain wildcard characters (i.e., characters which represent
unspecified parts of the path),
which include at least the asterisk on most systems,
and possibly other characters, depending on the system.


`directory` relies on the Lisp function DIRECTORY,
which may have implementation-specific behavior.

### Function: disp (expr_1, expr_2, ...)

is like `display` but only the value of the arguments are displayed rather
than equations.  This is useful for complicated arguments which don’t have names 
or where only the value of the argument is of interest and not the name.


See also `ldisp` and `print`.


Example:








```maxima
maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$

(%i3) disp(x, b[1,2], sin(1.0));
                               123

                                  2
                             x - x

                       0.8414709848078965

(%o3)                         done
```

See also: `display`, `ldisp`, `print`.

### Function: display (expr_1, expr_2, ...)

Displays equations whose left side is *expr_i* unevaluated, and whose right
side is the value of the expression centered on the line.  This function is 
useful in blocks and `for` statements in order to have intermediate results
displayed.  The arguments to `display` are usually atoms, subscripted 
variables, or function calls.


See also `ldisplay`, `disp`, and `ldisp`.


Example:








```maxima
maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$

(%i3) display(x, b[1,2], sin(1.0));
                             x = 123

                                      2
                         b     = x - x
                          1, 2

                  sin(1.0) = 0.8414709848078965

(%o3)                         done
```

See also: `for`, `ldisplay`, `disp`, `ldisp`.

### Variable: display2d

Default value: `true`


When `display2d` is `true`,
the console display is an attempt to present mathematical expressions
as they might appear in books and articles,
using only letters, numbers, and some punctuation characters.
This display is sometimes called the "pretty printer" display.


When `display2d` is `true`,
Maxima attempts to honor the global variable for line length, `linel`.
When an atom (symbol, number, or string) would otherwise cause a line to exceed `linel`,
the atom may be printed in pieces on successive lines,
with a continuation character (backslash, `\`) at the end of the leading piece;
however, in some cases, such atoms are printed without a line break,
and the length of the line is greater than `linel`.


When `display2d` is `false`,
the console display is a 1-dimensional or linear form
which is the same as the output produced by `grind`.


When `display2d` is `false`,
the value of `stringdisp` is ignored,
and strings are always displayed with quote marks.


When `display2d` is `false`,
Maxima attempts to honor `linel`,
but atoms are not broken across lines,
and the actual length of an output line may exceed `linel`.


See also `leftjust` to switch between a left justified and a centered
display of equations.


Example:








```maxima
maxima

(%i1) x/(x^2+1);
                               x
(%o1)                        ------
                              2
                             x  + 1

(%i2) display2d:false$

(%i3) x/(x^2+1);
(%o3) x/(x^2+1)
```

See also: `stringdisp`, `leftjust`.

### Variable: display2d_unicode

Default value: `true`


When `display2d_unicode` is `true`,
the 2-d pretty printer (enabled by the global flag `display2d`) uses Unicode drawing characters [1] to display
integrals, summations, products, matrices, ratios, derivatives,
`box` expressions, `at` expressions, and absolute value expressions.


Otherwise, the pretty printer uses only ASCII characters to display every kind of expression.


In addition to displaying expressions in console interaction (as `%o` labeled expressions),
the 2-d pretty printer is invoked to display expressions for `print`,
and `printf` with the `~m` format specifier.


Examples:


Expressions displayed by 2-d pretty printer using Unicode drawing characters
(`display2d_unicode` equal to `true`),
shown as an image:


(Figure maxima-unicode-display-variety-1)


Same expressions, displayed using only ASCII characters
(`display2d_unicode` equal to `false`),
shown as an image:


(Figure maxima-unicode-display-variety-1-ascii)



Footnotes:


[1] [https://en.wikipedia.org/wiki/Box-drawing_character]()

### Variable: display_format_internal

Default value: `false`


When `display_format_internal` is `true`, expressions are displayed
without being transformed in ways that hide the internal mathematical
representation.  The display then corresponds to what `inpart` returns
rather than `part`.


Examples:



```maxima
User     part       inpart
a-b;      a - b     a + (- 1) b

           a            - 1
a/b;       -         a b
           b
                       1/2
sqrt(x);   sqrt(x)    x

          4 X        4
X*4/3;    ---        - X
           3         3
```

See also: `inpart`, `part`.

### Variable: display_index_separator

When a symbol *A* has index display properties declared via `declare_index_properties`,
the value of the property `display_index_separator`
is the string or other expression which is displayed between indices.


The value of `display_index_separator`
is assigned by `put(A, S, display_index_separator)`,
where *S* is a string or other expression.
The assigned value is retrieved by `get(A, display_index_separator)`.


The display index separator *S* can be a string, including an empty string,
or `false`, indicating the default separator, or any expression.
If not a string and not `false`, the property value is coerced to a string via `string`.


If no display index separator is assigned, the default separator is used.
The default separator is a comma.
There is no way to change the default separator.


Each symbol has its own value of `display_index_separator`.


See also `put`, `get`, and `declare_005findex_005fproperties`.


Examples:

    

When a symbol *A* has index display properties,
the value of the property `display_index_separator`
is the string or other expression which is displayed between indices.
The value is assigned by `put(A, S, display_index_separator)`,









```maxima
maxima

(%i1) declare_index_properties (A, [postsuperscript, postsuperscript,
 presubscript, presubscript]);
(%o1)                         done


(%i2) put (A, ";", display_index_separator);
(%o2)                           ;


(%i3) A[w, x, y, z];
                                 w;x
(%o3)                           A
                             y;z
```


The assigned value is retrieved by `get(A, display_index_separator)`.









```maxima
maxima

(%i1) declare_index_properties (A, [postsuperscript, postsuperscript,
 presubscript, presubscript]);
(%o1)                         done


(%i2) put (A, ";", display_index_separator);
(%o2)                           ;


(%i3) get (A, display_index_separator);
(%o3)                           ;
```


The display index separator *S* can be a string, including an empty string,
or `false`, indicating the default separator, or any expression.


















```maxima
maxima

(%i1) declare_index_properties (A, [postsuperscript, postsuperscript,
 presubscript, presubscript]);
(%o1)                         done


(%i2) A[w, x, y, z];
                                 w, x
(%o2)                           A
                            y, z


(%i3) put (A, "-", display_index_separator);
(%o3)                           -


(%i4) A[w, x, y, z];
                                 w-x
(%o4)                           A
                             y-z


(%i5) put (A, " ", display_index_separator);
(%o5)                            


(%i6) A[w, x, y, z];
                                 w x
(%o6)                           A
                             y z


(%i7) put (A, "", display_index_separator);
(%o7) 


(%i8) A[w, x, y, z];
                                 wx
(%o8)                           A
                              yz


(%i9) put (A, false, display_index_separator);
(%o9)                         false


(%i10) A[w, x, y, z];
                                 w, x
(%o10)                          A
                            y, z


(%i11) put (A, 'foo, display_index_separator);
(%o11)                         foo


(%i12) A[w, x, y, z];
                                 wfoox
(%o12)                          A
                           yfooz
```


If no display index separator is assigned, the default separator is used.
The default separator is a comma.








```maxima
maxima

(%i1) declare_index_properties (A, [postsuperscript, postsuperscript,
 presubscript, presubscript]);
(%o1)                         done


(%i2) A[w, x, y, z];
                                 w, x
(%o2)                           A
                            y, z
```


Each symbol has its own value of `display_index_separator`.












```maxima
maxima

(%i1) declare_index_properties (A, [postsuperscript, postsuperscript,
 presubscript, presubscript]);
(%o1)                         done


(%i2) put (A, " ", display_index_separator);
(%o2)                            


(%i3) declare_index_properties (B, [presuperscript, presuperscript,
 postsubscript, postsubscript]);
(%o3)                         done


(%i4) put (B, ";", display_index_separator);
(%o4)                           ;


(%i5) A[w, x, y, z] + B[w, x, y, z];
                        w;x           w x
(%o5)                      B    +    A
                            y;z   y z
```

See also: `put`, `get`, `declare_index_properties`.

### Function: dispterms (expr)

Displays *expr* in parts one below the other.  That is, first the operator
of *expr* is displayed, then each term in a sum, or factor in a product, or
part of a more general expression is displayed separately.  This is useful if
*expr* is too large to be otherwise displayed.  For example if `P1`,
`P2`, ...  are very large expressions then the display program may run
out of storage space in trying to display `P1 + P2 + ...`  all at once.
However, `dispterms (P1 + P2 + ...)` displays `P1`, then below it
`P2`, etc.  When not using `dispterms`, if an exponential expression
is too wide to be displayed as `A^B` it appears as `expt (A, B)` (or
as `ncexpt (A, B)` in the case of `A^^B`).


Example:






```maxima
maxima

(%i1) dispterms(2*a*sin(x)+%e^x);
+

2 a sin(x)


  x
%e


(%o1)                         done
```

### Variable: engineering_format_floats

Default value: `true` 



This variable allows to temporarily switch off engineering-format.








```maxima
(%i1) load("engineering-format");
(%o1) /home/gunter/src/maxima-code/share/contrib/engineering-for\
mat.lisp


(%i2) float(sin(10)/10000);
(%o2)                - 54.40211108893698e-6

(%i3) engineering_format_floats:false$

(%i4) float(sin(10)/10000);
(%o4)                - 5.440211108893698e-5
```


See also `fpprintprec` and `float`.

See also: `fpprintprec`, `float`.

### Variable: engineering_format_max

Default value: `0.0` 


The maximum absolute value that isn’t automatically converted to the engineering format.
See also `engineering_format_min` and `engineering_005fformat_005ffloats`.

See also: `engineering_format_min`, `engineering_format_floats`.

### Variable: engineering_format_min

Default value: `0.0` 


The minimum absolute value that isn’t automatically converted to the engineering format.
See also `engineering_format_max` and `engineering_005fformat_005ffloats`.











```maxima
(%i1) lst: float([.05,.5,5,500,5000,500000]);
(%o1)       [0.05, 0.5, 5.0, 500.0, 5000.0, 500000.0]


(%i2) load("engineering-format");
(%o2) /home/gunter/src/maxima-code/share/contrib/engineering-for\
mat.lisp


(%i3) lst;
(%o3) [50.0e-3, 500.0e-3, 5.0e+0, 500.0e+0, 5.0e+3, 500.0e+3]

(%i4) engineering_format_min:.1$
(%i5) engineering_format_max:1000$

(%i6) lst;
(%o6)     [50.0e-3, 0.5, 5.0, 500.0, 5.0e+3, 500.0e+3]
```

See also: `engineering_format_max`, `engineering_format_floats`.

### Function: eval_string (str)

Parse the string *str* as a Maxima expression and evaluate it.
The string *str* may or may not have a terminator (dollar sign `$` or semicolon `;`).
Only the first expression is parsed and evaluated, if there is more than one.


Complain if *str* is not a string.


Examples:



```maxima
(%i1) eval_string ("foo: 42; bar: foo^2 + baz");
(%o1)                       42
(%i2) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o2)                   baz + 1764
```


See also `parse_005fstring` and `eval_005fstring_005flisp`.

See also: `parse_string`, `eval_string_lisp`.

### Function: expt (a, b)

If an exponential expression is too wide to be displayed as
`a^b` it appears as `expt (a, b)` (or as
`ncexpt (a, b)` in the case of `a^^b`).





`expt` and `ncexpt` are not recognized in input.

### Variable: exptdispflag

Default value: `true`


When `exptdispflag` is `true`, Maxima displays expressions
with negative exponents using quotients.  See also `_0025edispflag`.


Example:









```maxima
maxima

(%i1) exptdispflag:true;
(%o1)                         true


(%i2) 10^-x;
                                1
(%o2)                          ---
                                 x
                               10


(%i3) exptdispflag:false;
(%o3)                         false


(%i4) 10^-x;
                                - x
(%o4)                         10
```

See also: `%edispflag`.

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

### Variable: file_output_append

Default value: `false`


`file_output_append` governs whether file output functions append or
truncate their output file.  When `file_output_append` is `true`, such
functions append to their output file.  Otherwise, the output file is truncated.


`save`, `stringout`, and `with_stdout` respect
`file_output_append`.  Other functions which write output files do not
respect `file_output_append`.  In particular, plotting and translation
functions always truncate their output file, and `tex` and
`appendfile` always append.

See also: `save`, `stringout`, `with_stdout`, `tex`, `appendfile`.

### Function: file_search (file_search, filename, file_search, filename, pathlist)

`file_search` searches for the file *filename* and returns the path to
the file (as a string) if it can be found; otherwise `file_search` returns
`false`.  `file_search (filename)` searches in the default
search directories, which are specified by the
`file_search_maxima`, `file_search_lisp`, and
`file_search_demo` variables.


`file_search` first checks if the actual name passed exists,
before attempting to match it to “wildcard” file search patterns.
See `file_search_maxima` concerning file search patterns.


The argument *filename* can be a path and file name, or just a file name,
or, if a file search directory includes a file search pattern, just the base of
the file name (without an extension).  For example,



```maxima
maxima
file_search ("/home/wfs/special/zeta.mac");
file_search ("zeta.mac");
file_search ("zeta");
```


all find the same file, assuming the file exists and 
`/home/wfs/special/###.mac` is in `file_search_maxima`.


`file_search (filename, pathlist)` searches only in the
directories specified by *pathlist*, which is a list of strings.  The
argument *pathlist* supersedes the default search directories, so if the
path list is given, `file_search` searches only the ones specified, and not
any of the default search directories.  Even if there is only one directory in
*pathlist*, it must still be given as an one-element list.


The user may modify the default search directories.
See `file_005fsearch_005fmaxima`.


`file_search` is invoked by `load` with `file_search_maxima` and
`file_search_lisp` as the search directories.


See also `file_005fsearch_005fcache`.

See also: `file_search_maxima`, `file_search_lisp`, `file_search_demo`, `load`, `file_search_cache`.

### Variable: file_search_cache

Default value: `auto`


`file_search_cache` controls the use of a cache by `file_search` in
order to speed up the search.  Currently, it can only speed up searches where
the filename part does not contain wildcards (but the directory part may).


When `file_search_cache` is `auto` (the default value), the cache
will be activated if a one-time check determines that the system (Lisp
implementation, file system) fulfills the requirements.  This can be overridden
by setting `file_search_cache` to `true`, which is not recommended.
The value `false` prevents the use of the cache.


See also `file_005fsearch`.

See also: `file_search`.

### Variable: file_search_maxima

These variables specify lists of directories to be searched by
`load`, `demo`, and some other Maxima functions.  The default
values of these variables name various directories in the Maxima installation.


The user can modify these variables, either to replace the default values or to
append additional directories.  For example,



```maxima
maxima
file_search_maxima: ["/usr/local/foo/*.mac",
    "/usr/local/bar/*.mac"]$
```


replaces the default value of `file_search_maxima`, while



```maxima
maxima
file_search_maxima: append (file_search_maxima,
    ["/usr/local/foo/*.mac", "/usr/local/bar/*.mac"])$
```


appends two additional directories.  It may be convenient to put such an
expression in the file `maxima-init.mac` so that the file search path is
assigned automatically when Maxima starts.
See also `Introduction-for-Runtime-Environment`.


Each element of the search list is a Common Lisp wildcard pathname.
Briefly, a wildcard filename looks like `"*.lisp"`, which matches
any filename with an extension of `"lisp"`.  A directory
component of `*` matches any directory in the current directory,
and `**` matches any directory and subdirectories in the current
directory.


So, `file_search_maxima` includes
`"/home/username/.maxima/**/*.mac"`.  This means look in all
subdirectories of `"/home/username/.maxima/"` for files with
extension `"mac"`.  This includes subdirectories of
subdirectories.  Thus, `load("file")` will find
`"/home/username/.maxima/dir1/subdir1/file.mac"`.


To only search for a single level of subdirectories, use
`"/home/username/.maxima/*/*.mac"`.  This means Maxima will not
find the file `"/home/username/.maxima/dir1/subdir1/file.mac"`
when Maxima tries to, say, `load("file")`.


Further information about Common Lisp pathnames maybe be found in
[http://www.lispworks.com/documentation/HyperSpec/Body/19_b.htmCLHS Section 19.2: Pathnames]().

See also: `load`, `demo`, `Introduction-for-Runtime-Environment`.

### Function: file_type (filename)

Returns a guess about the content of *filename*, based on the filename 
extension.  *filename* need not refer to an actual file; no attempt is made 
to open the file and inspect the content.


The return value is a symbol, either `object`, `lisp`, or
`maxima`.  If the extension is matches one of the values in
`file_type_maxima`, `file_type` returns `maxima`.  If the
extension matches one of the values in `file_type_lisp`, `file_type`
returns `lisp`.  If none of the above, `file_type` returns
`object`.


See also `pathname_005ftype`.


See `file_type_maxima` and `file_type_lisp` for the default values.


Examples:







```maxima
maxima

(%i1) map('file_type,
    ["test.lisp", "test.mac", "test.dem", "test.txt"]);
(%o1)            [lisp, maxima, maxima, object]
```

See also: `pathname_type`, `file_type_maxima`, `file_type_lisp`.

### Variable: file_type_lisp

Default value:  `[l, lsp, lisp]`


`file_type_lisp` is a list of file extensions that maxima recognizes
as denoting a Lisp source file.


See also `file_005ftype`.

See also: `file_type`.

### Variable: file_type_maxima

Default value:  `[mac, mc, demo, dem, dm1, dm2, dm3, dmt, wxm]`


`file_type_maxima` is a list of file extensions that maxima recognizes
as denoting a Maxima source file.


See also `file_005ftype`.

See also: `file_type`.

### Function: filename_merge (path, filename)

Constructs a modified path from *path* and *filename*.  If the final
component of *path* is of the form `###.something`, the component
is replaced with `filename.something`.  Otherwise, the final
component is simply replaced by *filename*.


The result is a Lisp pathname object.

### Function: flength (stream)

*stream* has to be an open stream from or to a file. 
`flength` then returns the number of bytes which are currently present in this file.


Example: See `writebyte` .

See also: `writebyte`.

### Function: flush_output (stream)

Flushes *stream* where *stream* has to be an output stream to a file. 


Example: See `writebyte` .

See also: `writebyte`.

### Function: format (expr, template1, ...)

Each `template` indicates the desired form for an expression;
either the expected form or that into which it will be transformed. At
the same time, the indicated form implies a set of *pieces*; the
next template in the chain applies to those pieces. For example,
`%poly(x)` specifies the transformation into a polynomial in
`x`, with the pieces being the coefficients. The passive
`%frac` treats the expression as a fraction; the pieces are the
numerator and denominator.  Whereas the next template formats all pieces
of the previous layer, positional *subtemplates* may be used to
specify formats for each piece individually. This is most useful when
the pieces have unique roles and need to be treated differently, such as
a fraction’s numerator and denominator.

### Variable: fortcurrind

Default: 0


Number of blank spaces printed at the beginning of each line of
generated FORTRAN code (after column 6).

### Variable: fortindent

Default value: `0`


`fortindent` controls the left margin indentation of
expressions printed out by the `fortran` command.  `0` gives normal
printout (i.e., 6 spaces), and positive values will causes the
expressions to be printed farther to the right.

See also: `fortran`.

### Variable: fortlinelen

default: 72


Maximum number of characters printed on each line of generated FORTRAN
code.

### Function: fortran (expr)

Prints *expr* as a Fortran statement.
The output line is indented with spaces.
If the line is too long, `fortran` prints continuation lines.
`fortran` prints the exponentiation operator `^` as `**`,
and prints a complex number `a + b %i` in the form `(a,b)`.


*expr* may be an equation.  If so, `fortran` prints an assignment
statement, assigning the right-hand side of the equation to the left-hand side.
In particular, if the right-hand side of *expr* is the name of a matrix,
then `fortran` prints an assignment statement for each element of the
matrix.


If *expr* is not something recognized by `fortran`,
the expression is printed in `grind` format without complaint.
`fortran` does not know about lists, arrays, or functions.


`fortindent` controls the left margin of the printed lines.
`0` is the normal margin (i.e., indented 6 spaces).  Increasing
`fortindent` causes expressions to be printed further to the right.


When `fortspaces` is `true`, `fortran` fills out
each printed line with spaces to 80 columns.


`fortran` evaluates its arguments; quoting an argument defeats evaluation.
`fortran` always returns `done`.


See also the function `function_005ff90` for printing one or more
expressions as a Fortran 90 program.


Examples:













```maxima
maxima
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
      x(1) = 1
      x(2) = 2
      x(3) = 3
      x(4) = 4
(%o6)                         done

(%i7) f(x) := x^2$

(%i8) fortran (f);
      f
(%o8)                         done
```

See also: `grind`, `fortindent`, `fortspaces`, `function_f90`.

### Variable: fortspaces

Default value: `false`


When `fortspaces` is `true`, `fortran` fills out
each printed line with spaces to 80 columns.

### Function: fposition (fposition, stream, fposition, stream, pos)

Returns the current position in *stream*, if *pos* is not used. 
If *pos* is used, `fposition` sets the position in *stream*.
*stream* has to be a stream from or to a file and 
*pos* has to be a positive number.


Positions in data streams are like in strings or lists 1-indexed, 
i.e. the first element in *stream* is in position 1.

### Function: freshline (freshline, freshline, stream)

Writes a new line to the standard output stream 
if the position is not at the beginning of a line and returns `true`.
Using the optional argument *stream* the new line is written to that stream. 
There are some cases, where `freshline()` does not work as expected. 


See also `newline`.

See also: `newline`.

### Function: function_arguments (expr, functions, ...)

Returns a list of all argument lists for calls to *functions* in *expr*.

### Function: function_calls (expr, functions, ...)

Returns a list of all calls in *expr* involving any of *functions*.

### Function: gendecs (name)

The gendecs command can be called any time the gendecs flag is switched
off to retrieve all type declarations from Gentran’s symbol table for
the given subprogram name (or the "current" subprogram if false is given
as its argument).

### Variable: genfloat

Default: false


When set to true (or any non-false value), causes integers in generated
numerical code to be converted to floating point numbers, except in the
following places: array subscripts, exponents, and initial, final, and
step values in do-loops. An exception (for compatibility with Macsyma
2.4) is that numbers in exponentials (with base %e only) are
double-floated even when genfloat is false.

### Variable: genstmtincr

Default: 1


number by which genstmtno is incremented each time a new statement
number is generated.

### Variable: genstmtno

Default: 25000


Number used when a statement number must be generated. Note: it is the
user’s responsibility to make sure this number will not clash with
statement numbers in template files.

### Function: gentran (stmt1, stmt2, ..., stmtn, [f1, f2, ... , fm])

Translates each stmt into formatted code in the target language. A
substantial subset of expressions and statements in the Maxima
programming language can be translated directly into numerical code. The
**gentran** command translates Maxima statements or procedure
definitions into code in the target language (**gentranlang:**
fortran, c, or ratfor). Expressions may optionally be given to Maxima
for evaluation prior to translation.


*stmt1, stmt2, ... , stmtn* is a sequence of one or more
statements, each of which is any Maxima user level expression, (simple,
group, or block) statement, or procedure definition that can be
translated into the target language.


*[f1, f2, ... , fm]* is an optional list of output files to which
translated output will be written. They can be any of the following:


***string*** = the name of an output file in quotes


**true** (no quotes) = the terminal


**false** = the current output file(s)


**all** = all files currently open for output by gentran


If the files are not open they will be opened; if they are open, output
will be appended to them. Filenames are given as quoted strings. If the
optional variable **genoutpath** (string, including the final /)
default **false** is set, it will be prepended to the output file
names. If the output file list is omitted, output will be written to the
current output, generally the terminal. **gentran** returns (a list
of) the name(s) of file(s) to which code was written.

### Function: gentran_off (sw)

Turns the given switch, *sw*, off.

### Function: gentran_on (sw)

Turns on the mode switch *sw*.

### Function: gentranin (f1, f2, ..., fn, f1, f2, ..., fm)

gentranin processes mixed-language template files consisting of active
parts (delimited by <<...>>) containing Maxima statements, including
calls to gentran, and passive parts, assumed to contain statements in
the target language (including comments), which are transcribed
verbatim. Input files are processed sequentially and the results
appended to the output. The presence of >> in passive parts of the file
(except for in comments) is interpreted as an end-of-file and terminates
processing of that file. The optional list of output files *[f1,f2,
... , fm]* each receive a copy of the entire output. All filespecs are
quoted strings. Input files may be given as (quoted string) filenames,
which will be located by Maxima **file_search**. The optional
variable **geninpath** (default **false** ) must be a
*list* of quoted strings describing the paths to be searched for
the input files. If it is set, that list replaces the standard Maxima
search paths.


Active parts may contain any number of Maxima expressions and
statements. They are not copied directly to the output. Instead, they
are given to Maxima for evaluation. All output generated by each
evaluation is sent to the output file(s). Returned values are only
printed on the terminal. Active parts will most likely contain calls to
gentran to generate code. This means that the result of processing a
template file will be the original template file with all active parts
replaced by generated code. If *[f1, f2, ... , fm]* is not
supplied, then generated code is simply written to the current output
file(s). However, if it is given, then the current output file is
temporarily overridden. Generated code is written to each file
represented by *f1, f2, ... , fn* for this command only. Files which
were open prior to the call to gentranin will remain open after the
call, and files which did not exist prior to the call will be created,
opened, written to, and closed. The output file stack will be exactly
the same both before and after the call. gentranin returns (to the
terminal) the name(s) of (all) file(s) written to by this command.

### Function: gentraninshut ()

A cleanup function to close input files in case where gentranin hung due
to error in template.

### Variable: gentranlang

Default: fortran


Selects the target numerical language. Currently, gentranlang must be
fortran, ratfor, or c. Note that symbols entered in Maxima are
case-sensitive. gentranlang should not be set to FORTRAN, RATFOR or C.

### Variable: gentranopt

Default: **false**


When set to true (or any non-false value), causes Gentran to replace
each block of straightline code by an optimized sequence of assignments
obtained from the Maxima optimize command. (The optimize command takes
an expression and replaces common subexpressions by temporary variable
names. It returns the resulting assignment statement, preceded by
common-subexpression-to-temporary-variable assignments.

### Function: gentranout (f1, f2, ..., fn)

Gentran maintains a list of files currently open for output by gentran
commands only. gentranout inserts each file name represented by
*f1, f2,... , fn* into that list and opens each one for output. It
also resets the current output file(s) to include all files in
*f1, f2, ... , fn*. gentranout returns the list of files represented by
*f1, f2, ... , fn*; i.e., the current output file(s) after the
command has been executed.

### Variable: gentranparser

Default: **false**


If gentranparser is set to **true** Maxima forms input to gentran
will be parsed and an error will be produced if an expression cannot be
translated. Otherwise, untranslatable expressions may generate anomalous
output, sometimes containing explicit calls to Maxima functions.

### Function: gentranpop (f1, f2, ..., fn)

gentranpop deletes the top-most occurrence of the single element
containing the file name(s) represented by *f1, f2, ... , fn* from
the output stack. Files whose names have been completely removed from
the output stack are closed. The current output file is reset to the
(new) element on the top of the output stack. gentranpop returns the
current output file(s) after this command has been executed.

### Function: gentranpush (f1, f2, ..., fn)

gentranpush pushes the file list onto the output stack. Each file in the
list that is not already open for output is opened at this time. The
current output file is reset to this new element on the top of the
stack.

### Variable: gentranseg

Default: **true**

### Function: gentranshut (f1, f2, ..., fn)

gentranshut creates a list of file names from *f1, f2, ... , fn*,
deletes each from the output file list, and closes the corresponding
files. If (all of) the current output file(s) are closed, then the
current output file is reset to the terminal. gentranshut returns (a
list of) the current output file(s) after the command has been executed.
**gentranshut**(**all**) will close all gentran output files.

### Function: get_coef (clist, k1, ...)

Gets the coefficient from the coefficient list *clist* corresponding
to the keys *ki*. The keys are matched to variable powers when
*clist* is a `%poly`, `%series` or `%Taylor` form. If
*clist* is a `%trig` then *k1* should be `sin`
or `cos` and the remaining keys are matched to multipliers.

### Function: get_index_properties (a)

Returns the properties for *a* established by `declare_index_properties`.


See also `remove_005findex_005fproperties`.

See also: `remove_index_properties`.

### Function: get_output_stream_string (stream)

Returns a string containing all the characters currently present in 
*stream* which must be an open string-output stream. 
The returned characters are removed from *stream*.


Example: See `make_005fstring_005foutput_005fstream` .

See also: `make_string_output_stream`.

### Function: get_tex_environment (op)

Customize the TeX environment output by `tex`.
As maintained by these functions, the TeX environment comprises two strings:
one is printed before any other TeX output, and the other is printed after.


Only the TeX environment of the top-level operator in an expression
is output; TeX environments associated with other operators are ignored.


`get_tex_environment` returns the TeX environment which is applied
to the operator *op*; returns the default if no other environment
has been assigned.


`set_tex_environment` assigns the TeX environment for the operator
*op*.


Examples:









```maxima
maxima

(%i1) get_tex_environment (":=");
(%o1) [
\begin{verbatim}
, ;
\end{verbatim}
]


(%i2) tex (f (x) := 1 - x);
\begin{verbatim}
f(x):=1-x;
\end{verbatim}

(%o2)                         false


(%i3) set_tex_environment (":=", "$$", "$$");
(%o3)                       [$$, $$]


(%i4) tex (f (x) := 1 - x);
$$f(x):=1-x$$
(%o4)                         false
```

### Function: get_tex_environment_default ()

Customize the TeX environment output by `tex`.
As maintained by these functions, the TeX environment comprises two strings:
one is printed before any other TeX output, and the other is printed after.


`get_tex_environment_default` returns the TeX environment which is
applied to expressions for which the top-level operator has no
specific TeX environment (as assigned by `set_tex_environment`).


`set_tex_environment_default` assigns the default TeX environment.


Examples:











```maxima
maxima

(%i1) get_tex_environment_default ();
(%o1)                       [$$, $$]


(%i2) tex (f(x) + g(x));
$$g\left(x\right)+f\left(x\right)$$
(%o2)                         false


(%i3) set_tex_environment_default ("\\begin{equation}
(%o3) [\begin{equation}
, 
\end{equation}]


(%i4) ", "
\begin{equation}
g\left(x\right)+f\left(x\right)
\end{equation}
(%o4)                         false

(%i5) \\end{equation}");
```

### Function: grind (expr)

The function `grind` prints *expr* to the console in a form suitable
for input to Maxima.  `grind` always returns `done`.


When *expr* is the name of a function or macro, `grind` prints the
function or macro definition instead of just the name.


See also `string`, which returns a string instead of printing its
output.  `grind` attempts to print the expression in a manner which makes
it slightly easier to read than the output of `string`.


`grind` evaluates its argument.


Examples:



























```maxima
maxima

(%i1) aa + 1729;
(%o1)                       aa + 1729


(%i2) grind (%);
aa+1729$
(%o2)                         done


(%i3) [aa, 1729, aa + 1729];
(%o3)                 [aa, 1729, aa + 1729]


(%i4) grind (%);
[aa,1729,aa+1729]$
(%o4)                         done


(%i5) matrix ([aa, 17], [29, bb]);
                           [ aa  17 ]
(%o5)                      [        ]
                           [ 29  bb ]


(%i6) grind (%);
matrix([aa,17],[29,bb])$
(%o6)                         done


(%i7) set (aa, 17, 29, bb);
(%o7)                   {17, 29, aa, bb}


(%i8) grind (%);
{17,29,aa,bb}$
(%o8)                         done


(%i9) exp (aa / (bb + 17)^29);
                                aa
                            -----------
                                     29
                            (bb + 17)
(%o9)                     %e


(%i10) grind (%);
%e^(aa/(bb+17)^29)$
(%o10)                        done


(%i11) expr: expand ((aa + bb)^10);
         10           9        2   8         3   7         4   6
(%o11) bb   + 10 aa bb  + 45 aa  bb  + 120 aa  bb  + 210 aa  bb
         5   5         6   4         7   3        8   2
 + 252 aa  bb  + 210 aa  bb  + 120 aa  bb  + 45 aa  bb
        9        10
 + 10 aa  bb + aa


(%i12) grind (expr);
bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6
     +252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2
     +10*aa^9*bb+aa^10$
(%o12)                        done


(%i13) string (expr);
(%o13) bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6\
+252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2+10*aa^9*\
bb+aa^10


(%i14) cholesky (A):= block ([n : length (A), L : copymatrix (A),
  p : makelist (0, i, 1, length (A))],
  for i thru n do for j : i thru n do
  (x : L[i, j], x : x - sum (L[j, k] * L[i, k], k, 1, i - 1),
  if i = j then p[i] : 1 / sqrt(x) else L[j, i] : x * p[i]),
  for i thru n do L[i, i] : 1 / p[i],
  for i thru n do for j : i + 1 thru n do L[i, j] : 0, L)$
define: warning: redefining the built-in operator cholesky


(%i15) grind (cholesky);
cholesky(A):=block(
         [n:length(A),L:copymatrix(A),
          p:makelist(0,i,1,length(A))],
         for i thru n do
             (for j from i thru n do
                  (x:L[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),
                   if i = j then p[i]:1/sqrt(x)
                       else L[j,i]:x*p[i])),
         for i thru n do L[i,i]:1/p[i],
         for i thru n do (for j from i+1 thru n do L[i,j]:0),L)$
(%o15)                        done


(%i16) string (fundef (cholesky));
(%o16) cholesky(A):=block([n:length(A),L:copymatrix(A),p:makelis\
t(0,i,1,length(A))],for i thru n do (for j from i thru n do (x:L\
[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),if i = j then p[i]:1/sqrt(x\
) else L[j,i]:x*p[i])),for i thru n do L[i,i]:1/p[i],for i thru \
n do (for j from i+1 thru n do L[i,j]:0),L)
```

See also: `string`.

### Variable: ibase

Default value: `10`


`ibase` is the base for integers read by Maxima.


`ibase` may be assigned any integer between 2 and 36 (decimal), inclusive.
When `ibase` is greater than 10,
the numerals comprise the decimal numerals 0 through 9
plus letters of the alphabet `A`, `B`, `C`, ...,
as needed to make `ibase` digits in all.
Letters are interpreted as digits only if the first digit is 0 through 9.


Uppercase and lowercase letters are not distinguished.
The numerals for base 36, the largest acceptable base,
comprise 0 through 9 and `A` through `Z`.


Whatever the value of `ibase`,
when an integer is terminated by a decimal point,
it is interpreted in base 10.


See also `obase`.


Examples:


`ibase` less than 10 (for example binary numbers).








```maxima
maxima
(%i1) ibase : 2 $

(%i2) obase;
(%o2)                          10


(%i3) 1111111111111111;
(%o3)                         65535
```


`ibase` greater than 10.
Letters are interpreted as digits only if the first digit is 0
through 9 which means that hexadecimal numbers might need to
be prepended by a 0.












```maxima
maxima
(%i1) ibase : 16 $

(%i2) obase;
(%o2)                          10


(%i3) 1000;
(%o3)                         4096


(%i4) abcd;
(%o4)                         abcd


(%i5) symbolp (abcd);
(%o5)                         true


(%i6) 0abcd;
(%o6)                         43981


(%i7) symbolp (0abcd);
(%o7)                         false
```


When an integer is terminated by a decimal point,
it is interpreted in base 10.









```maxima
maxima
(%i1) ibase : 36 $

(%i2) obase;
(%o2)                          10


(%i3) 1234;
(%o3)                         49360


(%i4) 1234.;
(%o4)                         1234
```

See also: `obase`.

### Function: info_display (form)

This is an alias for the default 1-d display function. It may be used as
an alternative 1-d or 2-d display function.



```maxima
(%i1) load("alt-display.mac")$

(%i2) set_alt_display(2,info_display);

(%o2) done
(%i3) x/y;

(%o3) x/y
```

### Function: ldisp (expr_1, ..., expr_n)

Displays expressions *expr_1*, ..., *expr_n* to the console as
printed output.  `ldisp` assigns an intermediate expression label to each
argument and returns the list of labels.


See also `disp`, `display`, and `ldisplay`.


Examples:










```maxima
maxima

(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)


(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a


(%i3) ldisp (e, f);
                                   3
(%t3)                       (b + a)

                     3        2      2      3
(%t4)               b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]


(%i5) %t3;
                                   3
(%o5)                       (b + a)


(%i6) %t4;
                     3        2      2      3
(%o6)               b  + 3 a b  + 3 a  b + a
```

See also: `disp`, `display`, `ldisplay`.

### Function: ldisplay (expr_1, ..., expr_n)

Displays expressions *expr_1*, ..., *expr_n* to the console as
printed output.  Each expression is printed as an equation of the form
`lhs = rhs` in which `lhs` is one of the arguments of `ldisplay`
and `rhs` is its value.  Typically each argument is a variable.
`ldisp` assigns an intermediate expression label to each equation and
returns the list of labels.


See also `display`, `disp`, and `ldisp`.


Examples:










```maxima
maxima

(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)


(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a


(%i3) ldisplay (e, f);
                                     3
(%t3)                     e = (b + a)

                       3        2      2      3
(%t4)             f = b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]


(%i5) %t3;
                                     3
(%o5)                     e = (b + a)


(%i6) %t4;
                       3        2      2      3
(%o6)             f = b  + 3 a b  + 3 a  b + a
```

See also: `ldisp`, `display`, `disp`.

### Variable: leftjust

Default value: `false`


When `leftjust` is `true`, equations in 2D-display are drawn left
justified rather than centered.


See also `display2d` to switch between 1D- and 2D-display.


Example:








```maxima
maxima

(%i1) expand((x+1)^3);
                        3      2
(%o1)                  x  + 3 x  + 3 x + 1

(%i2) leftjust:true$

(%i3) expand((x+1)^3);
       3      2
(%o3) x  + 3 x  + 3 x + 1
```

See also: `display2d`.

### Variable: linel

Default value: `79`


`linel` is the assumed width (in characters) of the console display for the
purpose of displaying expressions.  `linel` may be assigned any value by
the user, although very small or very large values may be impractical.  Text
printed by built-in Maxima functions, such as error messages and the output of
`describe`, is not affected by `linel`.

See also: `describe`.

### Variable: lispdisp

Default value: `false`


When `lispdisp` is `true`, Lisp symbols are displayed with a leading
question mark `?`.  Otherwise, Lisp symbols are displayed with no leading
mark. This has the same effect for 1-d and 2-d display.


Examples:









```maxima
maxima
(%i1) lispdisp: false$

(%i2) ?foo + ?bar;
(%o2)                       foo + bar

(%i3) lispdisp: true$

(%i4) ?foo + ?bar;
(%o4)                      ?foo + ?bar
```

### Function: literal (arg1, arg2, ... , argn)

where arg1, arg2, ... , argn is an argument list containing one or more
arg’s, each of which either is, or evaluates to, an atom. The atoms
*tab* and *cr* have special meanings. arg’s are not evaluated
unless given as arguments to eval. This function call is replaced by the
character sequence resulting from concatenation of the given atoms.
Double quotes are stripped from all string type arg’s, and each
occurrence of the reserved atom *tab* or *cr* is replaced by a
tab to the current level of indentation, or an end-of-line character.

### Function: load (filename)

Evaluates expressions in *filename*, thus bringing variables, functions, and
other objects into Maxima.  The binding of any existing object is clobbered by
the binding recovered from *filename*.


*filename* must be a string, symbol,
or Lisp pathname (as created by `filename_merge`).
To find the file, `load` calls
`file_search` with `file_search_maxima` and
`file_search_lisp` as the search directories.  If `load` succeeds, it
returns the name of the file.  Otherwise `load` prints an error message.


`load` works equally well for Lisp code and Maxima code.  Files created by
`save`, `translate_file`, and `compile_file`, which
create Lisp code, and `stringout`, which creates Maxima code, can all
be processed by `load`.  `load` calls `loadfile` to load Lisp
files and `batchload` to load Maxima files.


`load` does not recognize `:lisp` constructs in Maxima files, and
while processing *filename*, the global variables `_`, `__`,
`%`, and `%th` have whatever bindings they had when `load` was
called.


Note also that structures will only be read back as structures if
they have been defined by `defstruct` before the `load` command
is called.


See also `loadfile`, for Lisp files; and `batch`, `batchload`, and
`demo`. for Maxima files.


See `file_search` for more detail about the file search mechanism.
The `numericalio` chapter describes many functions
for loading csv and other data files.


During Maxima file loading, the variable `load_pathname` is bound to the pathname of the file
being loaded.


`load` evaluates its argument.

See also: `filename_merge`, `file_search`, `file_search_maxima`, `file_search_lisp`, `save`, `translate_file`, `compile_file`, `stringout`, `loadfile`, `batchload`, `batch`, `demo`, `numericalio`, `load_pathname`.

### Variable: load_pathname

Default value: `false`


When a file is loaded with the functions `load`, `loadfile` or
`batchload` the system variable `load_pathname` is bound to the
pathname of the file which is processed.


The variable `load_pathname` can be accessed from the file during the
loading.


Example:


Suppose we have a batchfile `test.mac` in the directory


`"/home/dieter/workspace/mymaxima/temp/"` with the following commands




```maxima
maxima
print("The value of load_pathname is: ", load_pathname)$
print("End of batchfile")$
```


then we get the following output



```maxima
maxima
(%i1) load("/home/dieter/workspace/mymaxima/temp/test.mac")$
The value of load_pathname is:  
                   /home/dieter/workspace/mymaxima/temp/test.mac 
End of batchfile
```

See also: `load`, `loadfile`, `batchload`.

### Function: loadfile (filename)

Evaluates Lisp expressions in *filename*.  `loadfile` does not invoke
`file_search`, so `filename` must include the file extension and
as much of the path as needed to find the file.


`loadfile` can process files created by `save`,
`translate_file`, and `compile_005ffile`.  The user may find it
more convenient to use `load` instead of `loadfile`.

See also: `file_search`, `save`, `translate_file`, `compile_file`, `load`.

### Variable: loadprint

Default value: `true`


`loadprint` tells whether to print a message when a file is loaded.



- *
When `loadprint` is `true`, always print a message.
- *
When `loadprint` is `'loadfile`, print a message only if
a file is loaded by the function `loadfile`.
- *
When `loadprint` is `'autoload`,
print a message only if a file is automatically loaded.
See `setup_005fautoload`.
- *
When `loadprint` is `false`, never print a message.

See also: `setup_autoload`.

### Function: lrsetq (var, exp)

Where *var* is any Maxima matrix or array element with indices
which, after evaluation by Maxima, will result in expressions that can
be translated by Gentran; and *exp* is any user level expression
which, after evaluation, will result in an expression that can be
translated by Gentran into the target language. This is equivalent to
`var[eval(s1), eval(s2), ...]: eval(exp);`.

### Function: lsetq (var, exp)

Where *var* is any Maxima user level matrix or array element with
indices which, after evaluation by Maxima, will result in expressions
that can be translated by Gentran, and *exp* is any Maxima user
level expression that can be translated into the target language. This
is equivalent to `var[eval(s1), eval(s2), ...]: exp` where *s1*, *s2*, ...
are indices.

### Function: make_string_input_stream (make_string_input_stream, string, make_string_input_stream, string, start, make_string_input_stream, string, start, end)

Returns an input stream which contains parts of *string* and an end of file. 
Without optional arguments the stream contains the entire string 
and is positioned in front of the first character. 
*start* and *end* define the substring contained in the stream. 
The first character is available at position 1.

 

```maxima
(%i1) istream : make_string_input_stream("text", 1, 4);
(%o1)              #<string-input stream from "text">
(%i2) (while (c : readchar(istream)) # false do sprint(c), newline())$
t e x 
(%i3) close(istream)$
```

### Function: make_string_output_stream ()

Returns an output stream that accepts characters. Characters currently present 
in this stream can be retrieved by `get_005foutput_005fstream_005fstring`.

 

```maxima
(%i1) ostream : make_string_output_stream();
(%o1)               #<string-output stream 09622ea0>
(%i2) printf(ostream, "foo")$

(%i3) printf(ostream, "bar")$

(%i4) string : get_output_stream_string(ostream);
(%o4)                            foobar
(%i5) printf(ostream, "baz")$

(%i6) string : get_output_stream_string(ostream);
(%o6)                              baz
(%i7) close(ostream)$
```

See also: `get_output_stream_string`.

### Function: markedvarp (vname)

markedvarp tests whether the variable name *vname* is currently
marked.

### Function: markvar (vname)

markvar "marks" variable name *vname* to indicate that it currently
holds a significant value.

### Function: matching_parts (expr, predicate, args, ...)

Returns a list of all subexpressions of *expr* for which the application
`predicate(piece,args ... )` returns `true`.

### Function: mathml_display (form)

Produces MathML output.



```maxima
(%i1) load("alt-display.mac")$

(%i2) set_alt_display(2,mathml_display);
<math xmlns="http://www.w3.org/1998/Math/MathML"> <mi>mlabel</mi> 
 <mfenced separators=""><msub><mi>%o</mi> <mn>2</mn></msub> 
 <mo>,</mo><mi>done</mi> </mfenced> </math>
```

### Variable: maxexpprintlen

Default: 800


When **gentranseg** is true (or any non-false value), causes
Gentran to "segment" large expressions into subexpressions of manageable
size. The segmentation facility generates a sequence of assignment
statements, each of which assigns a subexpression to an automatically
generated temporary variable name. This sequence is generated in such a
way that temporary variables are re-used as soon as possible, thereby
keeping the number of automatically generated variables to a minimum.
The maximum allowable expression size can be controlled by setting the
**maxexpprintlen** variable to the maximum number of characters
allowed in an expression printed in the target numerical language
(excluding spaces and other whitespace characters automatically printed
by the formatter). When the segmentation routine generates temporary
variables, it places type declarations in the symbol table for those
variables if possible. It uses the following rules to determine their
type:


1. If the type of the variable to which the large expression is being
assigned is already known (i.e., has been declared by the user via a
TYPE form), then the temporary variables will be declared to be of that
same type. 2. If the global variable **tempvartype** has a
non-false value, then the temporary variables are declared to be of that
type. 3. Otherwise, the variables are not declared unless
**implicit** has been set to **true**.

### Variable: minclinelen

Default: 40


Minimum number of characters printed on each line of generated ’C’ code.

### Variable: minfortlinelen

Default: 40


Minimum number of characters printed on each line of generated FORTRAN
code.

### Function: multi_display_for_texinfo (form)

Produces Texinfo output using all three display functions.



```maxima
(%i2) set_alt_display(2,multi_display_for_texinfo)$

(%i3) x/(x^2+y^2);

@iftex
@tex
\mbox{\tt\red({\it \%o_3}) \black}$${{x}\over{y^2+x^2}}$$
@end tex
@end iftex
@ifhtml
@html

   <math xmlns="http://www.w3.org/1998/Math/MathML"> <mi>mlabel</mi> 
   <mfenced separators=""><msub><mi>%o</mi> <mn>3</mn></msub> 
   <mo>,</mo><mfrac><mrow><mi>x</mi> </mrow> <mrow><msup><mrow>
   <mi>y</mi> </mrow> <mn>2</mn> </msup> <mo>+</mo> <msup><mrow>
   <mi>x</mi> </mrow> <mn>2</mn> </msup> </mrow></mfrac> </mfenced> </math>
@end html
@end ifhtml
@ifinfo
@example
(%o3) x/(y^2+x^2)
@end example
@end ifinfo
```

### Variable: negsumdispflag

Default value: `true`


When `negsumdispflag` is `true`, `x - y` displays as `x - y`
instead of as `- y + x`.  Setting it to `false` causes the special
check in display for the difference of two expressions to not be done.  One
application is that thus `a + %i*b` and `a - %i*b` may both be
displayed the same way.

### Function: newline (newline, newline, stream)

Writes a new line to the standard output stream. 
Using the optional argument *stream* the new line is written to that stream. 
There are some cases, where `newline()` does not work as expected. 


See `sprint` for an example of using `newline()`.

See also: `sprint`.

### Variable: obase

Default value: `10`


`obase` is the base for integers displayed by Maxima.


`obase` may be assigned any integer between 2 and 36 (decimal), inclusive.
When `obase` is greater than 10,
the numerals comprise the decimal numerals 0 through 9
plus capital letters of the alphabet A, B, C, ..., as needed.
A leading 0 digit is displayed if the leading digit is otherwise a letter.
The numerals for base 36, the largest acceptable base,
comprise 0 through 9, and A through Z.


See also `ibase`.


Examples:













```maxima
maxima

(%i1) obase : 2;
(%o1)                          10


(%i2) 2^8 - 1;
(%o2)                       11111111


(%i3) obase : 8;
(%o3)                          10


(%i4) 8^8 - 1;
(%o4)                       77777777


(%i5) obase : 16;
(%o5)                          10


(%i6) 16^8 - 1;
(%o6)                       0FFFFFFFF


(%i7) obase : 36;
(%o7)                          10


(%i8) 36^8 - 1;
(%o8)                       0ZZZZZZZZ
```

See also: `ibase`.

### Function: opena (file)

Returns a character output stream to *file*.
If an existing file is opened, `opena` appends elements at the end of *file*.


For binary output see `Functions-and-Variables-for-binary-input-and-output` .

See also: `Functions-and-Variables-for-binary-input-and-output`.

### Function: opena_binary (file_name)

Returns an output stream of 8-bit unsigned bytes to append the file named by *file_name*.

### Function: openr (openr, file, openr, file, encoding)

Returns a character input stream to *file*.
`openr` assumes that *file* already exists.
If reading the file results in a lisp error about its encoding
passing the correct string as the argument *encoding* might help.
The available encodings and their names depend on the lisp being used.
For sbcl a list of suitable strings can be found at
[http://www.sbcl.org/manual/#External-Formats]().


For binary input see `Functions-and-Variables-for-binary-input-and-output` .
See also `close` and `openw`.



```maxima
(%i1) istream : openr("data.txt","EUC-JP");
(%o1)     #<FD-STREAM for "file /home/gunter/data.txt" {10099A3AE3}>
(%i2) close(istream);
(%o2)                                true
```

See also: `Functions-and-Variables-for-binary-input-and-output`, `close`, `openw`.

### Function: openr_binary (file_name)

Returns an input stream of 8-bit unsigned bytes to read the file named by *file_name*.


See also `openw_binary` and `openr`.

See also: `openw_binary`, `openr`.

### Function: openw (file)

Returns a character output stream to *file*.
If *file* does not exist, it will be created.
If an existing file is opened, `openw` destructively modifies *file*.


For binary output see `Functions-and-Variables-for-binary-input-and-output` .


See also `close` and `openr`.

See also: `Functions-and-Variables-for-binary-input-and-output`, `close`, `openr`.

### Function: openw_binary (file_name)

Returns an output stream of 8-bit unsigned bytes to write the file named by *file_name*.


See also `openr_binary`, `opena_binary` and `openw`.

See also: `openr_binary`, `opena_binary`, `openw`.

### Variable: optimvarname

default: **’u**


is the preface used
to generate temporary file names produced by the optimizer when
**gentranopt** is **true**. When both gentranseg and
gentranopt are true, the optimizer generates temporary file names using
**optimvarname** while the segmentation routine uses
**tempvarname** preventing conflict.

### Function: parse_string (str)

Parse the string *str* as a Maxima expression (do not evaluate it).
The string *str* may or may not have a terminator (dollar sign `$` or semicolon `;`).
Only the first expression is parsed, if there is more than one.


Complain if *str* is not a string.


Examples:



```maxima
(%i1) parse_string ("foo: 42; bar: foo^2 + baz");
(%o1)                    foo : 42
(%i2) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o2)          (foo : 42, bar : foo  + baz)
```


See also `eval_005fstring`.

See also: `eval_string`.

### Function: partition_poly (expr, test, v1, ...)

Partitions *expr* into two polynomials; the first is made of those
monomials for which the function test returns true and the second is the
remainder. The test function is called on the powers of the *vi*.

### Function: partition_series (expr, test, v, O)

### Function: partition_Taylor (expr, test, v, O)

Analog to `partition_poly` for series.

### Function: partition_trig (expr, sintest, costest, v1, ...)

Trigonometric analog to partition poly; The functions *sintest* and
*costest* select sine and cosine terms, respectively; each are called on
the multipliers of the *vi*.

### Function: pathname_directory (pathname)

These functions return the components of *pathname*.


Examples:








```maxima
maxima

(%i1) pathname_directory("/home/dieter/maxima/changelog.txt");
(%o1)                 /home/dieter/maxima/


(%i2) pathname_name("/home/dieter/maxima/changelog.txt");
(%o2)                       changelog


(%i3) pathname_type("/home/dieter/maxima/changelog.txt");
(%o3)                          txt
```

### Variable: pfeformat

Default value: `false`


When `pfeformat` is `true`, a ratio of integers is displayed with the
solidus (forward slash) character, and an integer denominator `n` is
displayed as a leading multiplicative term `1/n`.


Examples:











```maxima
maxima
(%i1) pfeformat: false$

(%i2) 2^16/7^3;
                              65536
(%o2)                         -----
                               343


(%i3) (a+b)/8;
                              b + a
(%o3)                         -----
                                8

(%i4) pfeformat: true$

(%i5) 2^16/7^3;
(%o5)                       65536/343


(%i6) (a+b)/8;
(%o6)                     (1/8) (b + a)
```

### Variable: powerdisp

Default value: `false`


When `powerdisp` is `true`,
a sum is displayed with its terms in order of increasing power.
Thus a polynomial is displayed as a truncated power series,
with the constant term first and the highest power last.


By default, terms of a sum are displayed in order of decreasing power.


Example:









```maxima
maxima

(%i1) powerdisp:true;
(%o1)                         true


(%i2) x^2+x^3+x^4;
                           2    3    4
(%o2)                     x  + x  + x


(%i3) powerdisp:false;
(%o3)                         false


(%i4) x^2+x^3+x^4;
                           4    3    2
(%o4)                     x  + x  + x
```

### Function: print (expr_1, ..., expr_n)

Evaluates and displays *expr_1*, ..., *expr_n* one after another,
from left to right, starting at the left edge of the console display.


The value returned by `print` is the value of its last argument.
`print` does not generate intermediate expression labels.


See also `display`, `disp`, `ldisplay`, and
`ldisp`.  Those functions display one expression per line, while
`print` attempts to display two or more expressions per line.


To display the contents of a file, see `printfile`.


Examples:








```maxima
maxima

(%i1) r: print ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is", radcan (log (a^10/b)))$
            3        2      2      3
(a+b)^3 is b  + 3 a b  + 3 a  b + a  log (a^10/b) is 
                                              10 log(a) - log(b) 


(%i2) r;
(%o2)                  10 log(a) - log(b)


(%i3) disp ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is", radcan (log (a^10/b)))$
                           (a+b)^3 is

                     3        2      2      3
                    b  + 3 a b  + 3 a  b + a

                         log (a^10/b) is

                       10 log(a) - log(b)
```

See also: `display`, `disp`, `ldisplay`, `ldisp`, `printfile`.

### Function: printf (printf, dest, string, printf, dest, string, expr_1, ..., expr_n)

Produces formatted output by outputting the characters of control-string 
*string* and observing that a tilde introduces a directive.
The character after the tilde, possibly preceded by prefix parameters 
and modifiers, specifies what kind of formatting is desired.
Most directives use one or more elements of the arguments 
*expr_1*, ..., *expr_n* to create their output.


If *dest* is a stream or `true`, then `printf` returns `false`.
Otherwise, `printf` returns a string containing the output.
By default the streams *stdin*, *stdout* and *stderr* are defined.
If Maxima is running as a network client (which is the normal case if Maxima is communicating
with a graphical user interface, which must be the server) `setup-client`
will define *old_stdout* and *old_stderr*, too.


`printf` provides the Common Lisp function `format` in Maxima. 
The following example illustrates the general relation between these two 
functions.



```maxima
(%i1) printf(true, "R~dD~d~%", 2, 2);
R2D2
(%o1)                                false
(%i2) :lisp (format t "R~dD~d~%" 2 2)
R2D2
NIL
```


The following description is limited to a rough sketch of the possibilities of 
`printf`.
The Lisp function `format` is described in detail in many reference books. 
Of good help is e.g. the free available online-manual 
"Common Lisp the Language" by Guy L. Steele. See chapter 22.3.3 there. 


In addition, `printf` recognizes two format directives which are not known to Lisp `format`.
The format directive `~m` indicates Maxima pretty printer output.
The format directive `~h` indicates a bigfloat number.



```maxima
~%       new line
   ~&       fresh line
   ~t       tab
   ~$       monetary
   ~d       decimal integer
   ~b       binary integer
   ~o       octal integer
   ~x       hexadecimal integer
   ~br      base-b integer
   ~r       spell an integer
   ~p       plural
   ~f       floating point
   ~e       scientific notation
   ~g       ~f or ~e, depending upon magnitude
   ~h       bigfloat
   ~a       uses Maxima function string
   ~m       Maxima pretty printer output
   ~s       like ~a, but output enclosed in "double quotes"
   ~~       ~
   ~<       justification, ~> terminates
   ~(       case conversion, ~) terminates 
   ~[       selection, ~] terminates 
   ~{       iteration, ~} terminates
```


Note that the directive ~* is not supported.


If *dest* is a stream or `true`, then `printf` returns `false`.
Otherwise, `printf` returns a string containing the output.



```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf(true,"~{~{~9,1f ~}~%~}",mat ),
          mat = args(matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]))$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false,control, n,n,if n=1 then 1 else 2 ), n=2;
(%o5)                    Two birds are singing.
```


The directive ~h has been introduced to handle bigfloats. 



```maxima
~w,d,e,x,o,p@H
 w : width
 d : decimal digits behind floating point
 e : minimal exponent digits
 x : preferred exponent
 o : overflow character
 p : padding character
 @ : display sign for positive numbers
```



```maxima
(%i1) fpprec : 1000$
(%i2) printf(true, "|~h|~%", 2.b0^-64)$
|0.0000000000000000000542101086242752217003726400434970855712890625|
(%i3) fpprec : 26$
(%i4) printf(true, "|~h|~%", sqrt(2))$
|1.4142135623730950488016887|
(%i5) fpprec : 24$
(%i6) printf(true, "|~h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i7) printf(true, "|~28h|~%", sqrt(2))$
|   1.41421356237309504880169|
(%i8) printf(true, "|~28,,,,,'*h|~%", sqrt(2))$
|***1.41421356237309504880169|
(%i9) printf(true, "|~,18h|~%", sqrt(2))$
|1.414213562373095049|
(%i10) printf(true, "|~,,,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-3|
(%i11) printf(true, "|~,,2,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-03|
(%i12) printf(true, "|~20h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i13) printf(true, "|~20,,,,'+h|~%", sqrt(2))$
|++++++++++++++++++++|
```


For conversion of objects to strings also see `concat`, `sconcat`,
`string` and `simplode`.

See also: `concat`, `sconcat`, `string`, `simplode`.

### Function: printfile (path)

Prints the file named by *path* to the console.  *path* may be a string
or a symbol; if it is a symbol, it is converted to a string.


If *path* names a file which is accessible from the current working
directory, that file is printed to the console.  Otherwise, `printfile`
attempts to locate the file by appending *path* to each of the elements of
`file_search_usage` via `filename_005fmerge`.


`printfile` returns *path* if it names an existing file,
or otherwise the result of a successful filename merge.

See also: `file_search_usage`, `filename_merge`.

### Variable: ratlinelen

Default: 80


Maximum number of characters printed on each line of generated Ratfor
code.

### Function: read_array (read_array, S, A, read_array, S, A, separator_flag)

Reads the source *S* into the array *A*,
until *A* is full or the source is exhausted.
Input data are read into the array in row-major order;
the input need not conform to the dimensions of *A*.


The source *S* may be a file name or a stream.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_hashed_array`,
`read_list`, `read_binary_array` and `read_005fnested_005flist`.

See also: `openr`, `read_matrix`, `read_hashed_array`, `read_list`, `read_binary_array`, `read_nested_list`.

### Function: read_binary_array (S, A)

Reads binary 8-byte floating point numbers from the source *S* into the array *A*
until *A* is full, or the source is exhausted.
*A* must be an array created by `array` or `make_array`.
Elements of *A* are read in row-major order.


The source *S* may be a file name or a stream.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005farray`.

See also: `read_array`.

### Function: read_binary_list (read_binary_list, S, read_binary_list, S, L)

`read_binary_list(S)` reads the entire content of the source *S*
as a sequence of binary 8-byte floating point numbers, and returns it as a list.
The source *S* may be a file name or a stream.


`read_binary_list(S, L)` reads 8-byte binary floating point numbers
from the source *S* until the list *L* is full, or the source is exhausted.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005flist`.

See also: `read_list`.

### Function: read_binary_matrix (S, M)

Reads binary 8-byte floating point numbers from the source *S* into the matrix *M*
until *M* is full, or the source is exhausted.
Elements of *M* are read in row-major order.


The source *S* may be a file name or a stream.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005fmatrix`.

See also: `read_matrix`.

### Function: read_hashed_array (read_hashed_array, S, A, read_hashed_array, S, A, separator_flag)

Reads the source *S* and returns its entire content as a `hashed-array`.
The source *S* may be a file name or a stream.


`read_hashed_array` treats the first item on each line as a hash key,
and associates the remainder of the line (as a list) with the key.
For example,
the line `567 12 17 32 55` is equivalent to `A[567]: [12, 17, 32, 55]$`.
Lines need not have the same numbers of elements.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_list` and `read_005fnested_005flist`.

See also: `hashed-array`, `openr`, `read_matrix`, `read_array`, `read_list`, `read_nested_list`.

### Function: read_list (read_list, S, read_list, S, L, read_list, S, separator_flag, read_list, S, L, separator_flag)

`read_list(S)` reads the source *S* and returns its entire content as a flat list.


`read_list(S, L)` reads the source *S* into the list *L*,
until *L* is full or the source is exhausted.


The source *S* may be a file name or a stream.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_nested_list`, `read_binary_list` and `read_005fhashed_005farray`.

See also: `openr`, `read_matrix`, `read_array`, `read_nested_list`, `read_binary_list`, `read_hashed_array`.

### Function: read_matrix (read_matrix, S, read_matrix, S, M, read_matrix, S, separator_flag, read_matrix, S, M, separator_flag)

`read_matrix(S)` reads the source *S* and returns its entire content as a matrix.
The size of the matrix is inferred from the input data;
each line of the file becomes one row of the matrix.
If some lines have different lengths, `read_matrix` complains.


`read_matrix(S, M)` read the source *S* into the matrix *M*,
until *M* is full or the source is exhausted.
Input data are read into the matrix in row-major order;
the input need not have the same number of rows and columns as *M*.


The source *S* may be a file name or a stream which for example allows skipping
the very first line of a file (that may be useful, if you read CSV data, where the
first line often contains the description of the columns):


```maxima
s : openr("data.txt");
readline(s);  /* skip the first line */
M : read_matrix(s, 'comma);  /* read the following (comma-separated) lines into matrix M */
close(s);
```


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_array`, `read_hashed_array`,
`read_list`, `read_binary_matrix`, `write_data` and
`read_005fnested_005flist`.

See also: `openr`, `read_array`, `read_hashed_array`, `read_list`, `read_binary_matrix`, `write_data`, `read_nested_list`.

### Function: read_nested_list (read_nested_list, S, read_nested_list, S, separator_flag)

Reads the source *S* and returns its entire content as a nested list.
The source *S* may be a file name or a stream.


`read_nested_list` returns a list which has a sublist for each
line of input. Lines need not have the same numbers of elements.
Empty lines are *not* ignored: an empty line yields an empty sublist.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_list` and `read_005fhashed_005farray`.

See also: `openr`, `read_matrix`, `read_array`, `read_list`, `read_hashed_array`.

### Function: readbyte (stream)

Removes and returns the first byte in *stream* which must be a binary input stream. 
If the end of file is encountered `readbyte` returns `false`.


Example: Read the first 16 bytes from a file encrypted with AES in OpenSSL. 



```maxima
(%i1) ibase: obase: 16.$

(%i2) in: openr_binary("msg.bin");
(%o2)                       #<input stream msg.bin>
(%i3) (L:[],  thru 16. do push(readbyte(in), L),  L:reverse(L));
(%o3) [53, 61, 6C, 74, 65, 64, 5F, 5F, 88, 56, 0DE, 8A, 74, 0FD,
       0AD, 0F0]
(%i4) close(in);
(%o4)                                true
(%i5) map(ascii, rest(L,-8));
(%o5)                      [S, a, l, t, e, d, _, _]
(%i6) salt: octets_to_number(rest(L,8));
(%o6)                          8856de8a74fdadf0
```

### Function: readchar (stream)

Removes and returns the first character in *stream*. 
If the end of file is encountered `readchar` returns `false`.


Example: See `make_005fstring_005finput_005fstream`.

See also: `make_string_input_stream`.

### Function: readline (stream)

Returns a string containing all characters starting at the current position 
in *stream* up to the end of the line or `false` 
if the end of the file is encountered.

### Function: remove_index_properties (a, b, c, ...)

Removes the properties established by `declare_index_properties`.
All index properties are removed from each symbol *a*, *b*, *c*, ....


`remove_index_properties` quotes (does not evaluate) its arguments.

### Function: rename_file (file1, file2)

renames file *file1* to *file2*

### Function: reset_displays ()

Resets the prompt prefix and suffix to the empty string, and sets both
1-d and 2-d display functions to the default.

### Function: rsetq (var, exp)

Where *var* is any Maxima variable, matrix or array element, and
*exp* is any Maxima expression which, after evaluation by Maxima
results in an expression that can be translated by Gentran into the
target language. This is equivalent to VAR : EVAL(EXP) ;

### Function: save (save, filename, name_1, name_2, name_3, ..., save, filename, values, functions, labels, ..., save, filename, m, n, save, filename, name_1, =, expr_1, ..., save, filename, all, save, filename, name_1, =, expr_1, name_2, =, expr_2, ...)

Stores the current values of *name_1*, *name_2*, *name_3*, ...,
in *filename*.  The arguments are the names of variables, functions, or
other objects.  If a name has no value or function associated with it, it is
ignored.  `save` returns *filename*.


`save` stores data in the form of Lisp expressions.
If *filename* ends in `.lisp` the
data stored by `save` may be recovered by `load (filename)`.
See `load`.


The global flag `file_output_append` governs whether `save` appends or
truncates the output file.  When `file_output_append` is `true`,
`save` appends to the output file.  Otherwise, `save` truncates the
output file.  In either case, `save` creates the file if it does not yet
exist.


The special form `save (filename, values, functions, labels, ...)`
stores the items named by `values`, `functions`,
`labels`, etc.  The names may be any specified by the variable
`infolists`.  `values` comprises all user-defined variables.


The special form `save (filename, [m, n])` stores the
values of input and output labels *m* through *n*.  Note that *m*
and *n* must be literal integers.  Input and output labels may also be
stored one by one, e.g., `save ("foo.1", %i42, %o42)`.
`save (filename, labels)` stores all input and output labels.
When the stored labels are recovered, they clobber existing labels.


The special form `save (filename, name_1=expr_1, name_2=expr_2, ...)` stores the values of *expr_1*,
*expr_2*, ..., with names *name_1*, *name_2*, ...
It is useful to apply this form to input and output labels, e.g.,
`save ("foo.1", aa=%o88)`.  The right-hand side of the equality in this
form may be any expression, which is evaluated.  This form does not introduce
the new names into the current Maxima environment, but only stores them in
*filename*.


These special forms and the general form of `save` may be mixed at will.
For example, `save (filename, aa, bb, cc=42, functions, [11, 17])`.


The special form `save (filename, all)` stores the current state of
Maxima.  This includes all user-defined variables, functions, arrays, etc., as
well as some automatically defined items.  The saved items include system
variables, such as `file_search_maxima` or `showtime`, if they
have been assigned new values by the user; see `myoptions`.


`save` evaluates *filename* and quotes all other arguments.

See also: `load`, `file_output_append`, `values`, `functions`, `labels`, `infolists`, `file_search_maxima`, `showtime`, `myoptions`.

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

### Function: scopy (string)

Returns a copy of *string* as a new string.

### Function: sdowncase (sdowncase, string, sdowncase, string, start, sdowncase, string, start, end)

Like `supcase` but uppercase characters are converted to lowercase.

See also: `supcase`.

### Function: sequal (string_1, string_2)

Returns `true` if *string_1* and *string_2* contain the same 
sequence of characters.

### Function: sequalignore (string_1, string_2)

Like `sequal` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: set_alt_display (num, display-function)

The input *num* is the display to set; it may be either 1 or 2. The
second input *display-function* is the display function to use. The
display function may be either a Maxima function or a `lambda`
expression.


Here is an example where the display function is a `lambda`
expression; it just displays the result as TeX.


```maxima
(%i1) load("alt-display.mac")$

(%i2) set_alt_display(2, lambda([form], tex(?caddr(form))))$

(%i3) integrate(exp(-t^2),t,0,inf);
$${{\sqrt{\pi}}\over{2}}$$
```


A user-defined display function should take care that it *prints*
its output. A display function that returns a string will appear to
display nothing, nor cause any errors.

### Function: set_prompt (fix, expr)

Set the prompt prefix or suffix to *expr*. The input *fix* must
evaluate to one of `prefix`, `suffix`, `general`,
`prolog` or `epilog`. The input *expr* must evaluate to
either a string or `false`; if `false`, the *fix* is reset
to the default value.



```maxima
(%i1) load("alt-display.mac")$
(%i2) set_prompt('prefix,printf(false,"It is now: ~a~%",timedate()))$

It is now: 2014-01-07 15:23:23-05:00
(%i3)
```


The following example shows the effect of each option, except
`prolog`. Note that the `epilog` prompt is printed as Maxima
closes down. The `general` is printed between the end of input and
the output, unless the input line ends in `$`.


Here is an example to show where the prompt strings are placed.



```maxima
(%i1) load("alt-display.mac")$

(%i2) set_prompt(prefix, "<<prefix>> ", suffix, "<<suffix>> ",
                 general, printf(false,"<<general>>~%"),
                 epilog, printf(false,"<<epilog>>~%"));

(%o2)                                done
<<prefix>> (%i3) <<suffix>> x/y;
<<general>>
                                       x
(%o3)                                  -
                                       y
<<prefix>> (%i4) <<suffix>> quit();
<<general>>
<<epilog>>
```


Here is an example that shows how to colorize the input and output when
Maxima is running in a terminal or terminal emulator like
Emacs

Readers using the `info` reader in `Emacs` will
see the actual prompt strings; other readers will see the colorized
output
.


(Figure color_terminal)


Each prompt string starts with the ASCII escape character (27) followed
by an open square bracket (91); each string ends with a lower-case m
(109). The webpages
[https://misc.flogisoft.com/bash/tip_colors_and_formatting]() and
[https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html]() provide
information on how to use control strings to set the terminal colors.

### Function: sexplode (string)

`sexplode` is an alias for function `charlist`.

### Function: simplode (simplode, list, simplode, list, delim)

`simplode` takes a list of expressions and concatenates them into a string.
If no delimiter *delim* is specified, `simplode` uses no delimiter.
*delim* can be any string.


See also `concat`, `sconcat`, `string` and `printf`.


Examples:



```maxima
(%i1) simplode(["xx[",3,"]:",expand((x+y)^3)]);
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) simplode( sexplode("stars")," * " );
(%o2)                   s * t * a * r * s
(%i3) simplode( ["One","more","coffee."]," " );
(%o3)                   One more coffee.
```

See also: `concat`, `sconcat`, `string`, `printf`.

### Function: sinsert (seq, string, pos)

Returns a string that is a concatenation of `substring(string, 1, pos-1)`,
the string *seq* and `substring (string, pos)`.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) s: "A submarine."$
(%i2) concat( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

### Function: sinvertcase (sinvertcase, string, sinvertcase, string, start, sinvertcase, string, start, end)

Returns *string* except that each character from position *start* to *end* is inverted.
If *end* is not given,
all characters from *start* to the end of *string* are replaced.


Examples:



```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

### Function: slength (string)

Returns the number of characters in *string*.

### Function: smake (num, char)

Returns a new string with a number of *num* characters *char*. 


Example:



```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

### Function: smismatch (smismatch, string_1, string_2, smismatch, string_1, string_2, test)

Returns the position of the first character of *string_1* at which *string_1* and *string_2* differ or `false`.
Default test function for matching is `sequal`.
If `smismatch` should ignore case, use `sequalignore` as test.


Example:



```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

### Function: split (split, string, split, string, delim, split, string, delim, multiple)

Returns the list of all tokens in *string*.
Each token is an unparsed string.
`split` uses *delim* as delimiter.
If *delim* is not given, the space character is the default delimiter.
*multiple* is a boolean variable with `true` by default.
Multiple delimiters are read as one.
This is useful if tabs are saved as multiple space characters.
If *multiple* is set to `false`, each delimiter is noted.


Examples:



```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

### Function: sposition (char, string)

Returns the position of the first character in *string* which matches *char*.
The first character in *string* is in position 1.
For matching characters ignoring case see `ssearch`.

See also: `ssearch`.

### Function: sprint (expr_1, ..., expr_n)

Evaluates and displays its arguments one after the other ‘on a line’ starting at
the leftmost position.  The expressions are printed with a space character right next 
to the number, and it disregards line length.  
`newline()` might be used for line breaking.


Example: Sequential printing with `sprint`. 
Creating a new line with `newline()`.



```maxima
(%i1) for n:0 thru 19 do sprint(fib(n))$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), 
         if mod(n,10) = 9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

### Variable: sqrtdispflag

Default value: `true`


When `sqrtdispflag` is `false`, causes `sqrt` to display with
exponent 1/2.

### Function: sremove (sremove, seq, string, sremove, seq, string, test, sremove, seq, string, test, start, sremove, seq, string, test, start, end)

Returns a string like *string* but without all substrings matching *seq*.
Default test function for matching is `sequal`.
If `sremove` should ignore case while searching for *seq*, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

### Function: sremovefirst (sremovefirst, seq, string, sremovefirst, seq, string, test, sremovefirst, seq, string, test, start, sremovefirst, seq, string, test, start, end)

Like `sremove` except that only the first substring that matches *seq* is removed.

### Function: sreverse (string)

Returns a string with all the characters of *string* in reverse order. 


See also `reverse`.

See also: `reverse`.

### Function: ssearch (ssearch, seq, string, ssearch, seq, string, test, ssearch, seq, string, test, start, ssearch, seq, string, test, start, end)

Returns the position of the first substring of *string* that matches the string *seq*.
Default test function for matching is `sequal`.
If `ssearch` should ignore case, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Example:



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

### Function: ssort (ssort, string, ssort, string, test)

Returns a string that contains all characters from *string* in an order such there are no two successive characters *c* and *d* such that `test (c, d)` is `false` and `test (d, c)` is `true`.
Default test function for sorting is *clessp*.
The set of test functions is `{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`.


Examples:



```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

### Function: ssubst (ssubst, new, old, string, ssubst, new, old, string, test, ssubst, new, old, string, test, start, ssubst, new, old, string, test, start, end)

Returns a string like *string* except that all substrings matching *old* are replaced by *new*.
*old* and *new* need not to be of the same length.
Default test function for matching is `sequal`.
If `ssubst` should ignore case while searching for old, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

### Function: ssubstfirst (ssubstfirst, new, old, string, ssubstfirst, new, old, string, test, ssubstfirst, new, old, string, test, start, ssubstfirst, new, old, string, test, start, end)

Like `subst` except that only the first substring that matches *old* is replaced.

### Variable: stardisp

Default value: `false`


When `stardisp` is `true`, multiplication is
displayed with an asterisk `*` between operands.

### Function: strim (seq, string)

Returns a string like *string*,
but with all characters that appear in *seq* removed from both ends. 


Examples:



```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

### Function: striml (seq, string)

Like `strim` except that only the left end of *string* is trimmed.

### Function: strimr (seq, string)

Like `strim` except that only the right end of *string* is trimmed.

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

### Function: stringout (stringout, filename, expr_1, expr_2, expr_3, ..., stringout, filename, m, n, stringout, filename, input, stringout, filename, functions, stringout, filename, values)

`stringout` writes expressions to a file in the same form the expressions
would be typed for input.  The file can then be used as input for the
`batch` or `demo` commands, and it may be edited for any purpose.
`stringout` can be executed while `writefile` is in progress.


The global flag `file_output_append` governs whether `stringout`
appends or truncates the output file.  When `file_output_append` is
`true`, `stringout` appends to the output file.  Otherwise,
`stringout` truncates the output file.  In either case, `stringout`
creates the file if it does not yet exist.


The general form of `stringout` writes the values of one or more 
expressions to the output file.  Note that if an expression is a
variable, only the value of the variable is written and not the name
of the variable.  As a useful special case, the expressions may be
input labels (`%i1`, `%i2`, `%i3`, ...) or output labels
(`%o1`, `%o2`, `%o3`, ...).


If `grind` is `true`, `stringout` formats the output using the
`grind` format.  Otherwise the `string` format is used.  See
`grind` and `string`.


The special form `stringout (filename, [m, n])` writes
the values of input labels m through n, inclusive.


The special form `stringout (filename, input)` writes all
input labels to the file.


The special form `stringout (filename, functions)` writes all
user-defined functions (named by the global list `functions`) to the
file.


The special form `stringout (filename, values)` writes all
user-assigned variables (named by the global list `values`) to the file.
Each variable is printed as an assignment statement, with the name of the
variable, a colon, and its value.  Note that the general form of
`stringout` does not print variables as assignment statements.

See also: `batch`, `demo`, `writefile`, `file_output_append`, `grind`, `functions`, `values`.

### Function: stringp (obj)

Returns `true` if *obj* is a string.
See introduction for example.

### Function: substring (substring, string, start, substring, string, start, end)

Returns the substring of *string* beginning at position *start* and ending at position *end*.
The character at position *end* is not included.
If *end* is not given, the substring contains the rest of the string.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

### Function: supcase (supcase, string, supcase, string, start, supcase, string, start, end)

Returns *string* except that lowercase characters from position *start* to *end* are replaced by the corresponding uppercase ones.
If *end* is not given,
all lowercase characters from *start* to the end of *string* are replaced.


Example:



```maxima
(%i1) supcase("english",1,2);
(%o1)                        English
```

### Variable: tablen

Default: 4


Number of blank spaces printed for each new level of indentation.
(Automatic indentation can be turned off by setting this variable to 0.)

### Function: tempvar (type)

Generates temporary variable names by concatenating **tempvarname**
(default **’t**) with sequence numbers. If *type* is
non-false, *e.g.* "real*8" the corresponding type is assigned to
the variable in the gentran symbol table, which may be used to generate
declarations depending on the setting of the **gendecs** flag. It
is the users responsibility to make sure temporary variable names do not
conflict with the main program.

### Variable: tempvarname

Default: **’t**


Name used as the prefix when generating temporary variable names.

### Variable: tempvarnum

Default: 0


Number appended onto tempvarname to create a temporary variable name. If
the temporary variable name resulting from appending tempvarnum onto the
end of tempvarname has already been generated and still holds a useful
value or has a different type than requested, then the number is
incremented until one is found that was not previously generated or does
not still hold a significant value or a different type.

### Variable: tempvartype

Default: **false**


Target language variable type (e.g., INTEGER, REAL*8, FLOAT, etc.) used
as a default for automatically generated variables whose type cannot be
determined otherwise. If tempvartype is false, then generated temporary
variables whose type cannot be determined are not automatically
declared.

### Function: tex (tex, expr, tex, expr, destination, tex, expr, false, tex, label, tex, label, destination, tex, label, false)

Prints a representation of an expression suitable for the TeX document
preparation system.  The result is a fragment of a document, which can be copied
into a larger document but not processed by itself.


`tex (expr)` prints a TeX representation of *expr* on the
console.


`tex (label)` prints a TeX representation of the expression named by
*label* and assigns it an equation label (to be displayed to the left of the
expression).  The TeX equation label is the same as the Maxima label.


*destination* may be an output stream or file name.  When *destination*
is a file name, `tex` appends its output to the file.  The functions
`openw` and `opena` create output streams.


`tex (expr, false)` and `tex (label, false)`
return their TeX output as a string.


`tex` evaluates its first argument after testing it to see if it is a
label.  Quote-quote `''` forces evaluation of the argument, thereby
defeating the test and preventing the label.


See also `tex1` and `texput`.


Examples:









```maxima
maxima

(%i1) integrate (1/(1+x^3), x);
                                  2 x - 1
                2            atan(-------)
           log(x  - x + 1)        sqrt(3)    log(x + 1)
(%o1)    - --------------- + ------------- + ----------
                  6             sqrt(3)          3


(%i2) tex (%o1);
$$-\left({{\log \left(x^2-x+1\right)}\over{6}}\right)+{{\arctan 
 \left({{2\,x-1}\over{\sqrt{3}}}\right)}\over{\sqrt{3}}}+{{\log 
 \left(x+1\right)}\over{3}}\leqno{\tt (\%o1)}$$
(%o2)                        (\%o1)


(%i3) tex (integrate (sin(x), x));
$$-\cos x$$
(%o3)                         false


(%i4) tex (%o1, "foo.tex");
(%o4)                        (\%o1)
```


`tex (expr, false)` returns its TeX output as a string.







```maxima
maxima

(%i1) S : tex (x * y * z, false);
(%o1) $$x\,y\,z$$


(%i2) S;
(%o2) $$x\,y\,z$$
```

See also: `tex1`, `texput`.

### Function: tex1 (e)

Returns a string which represents the TeX output for the expressions *e*.
The TeX output is not enclosed in delimiters for an equation or any other
environment.


See also `tex` and `texput`.


Examples:






```maxima
maxima

(%i1) tex1 (sin(x) + cos(x));
(%o1)                     \sin x+\cos x
```

See also: `tex`, `texput`.

### Function: tex_display (form)

Produces TeX output.



```maxima
(%i2) set_alt_display(2,tex_display);
\mbox{\tt\red({\it \%o_2}) \black}$$\mathbf{done}$$
(%i3) x/(x^2+y^2);
\mbox{\tt\red({\it \%o_3}) \black}$${{x}\over{y^2+x^2}}$$
```

### Function: texput (texput, a, s, texput, a, f, texput, a, s, operator_type, texput, a, s_1, s_2, matchfix, texput, a, s_1, s_2, s_3, matchfix)

Assign the TeX output for the atom *a*, which can be a symbol or the name
of an operator.


`texput (a, s)` causes the `tex` function to interpolate
the string *s* into the TeX output in place of *a*.


`texput (a, f)` causes the `tex` function to call the
function *f* to generate TeX output.  *f* must accept one argument,
which is an expression which has operator *a*,
and must return either a string (the TeX output) or `false`,
indicating that the TeX function in effect when `texput` is called
should handle the expression.
*f* may call `tex1` to generate TeX output for the
arguments of the input expression.


`texput (a, s, operator_type)`, where *operator_type*
is `prefix`, `infix`, `postfix`, `nary`, or `nofix`,
causes the `tex` function to interpolate *s* into the TeX output in
place of *a*, and to place the interpolated text in the appropriate
position.


`texput (a, [s_1, s_2], matchfix)` causes the `tex`
function to interpolate *s_1* and *s_2* into the TeX output on either
side of the arguments of *a*.  The arguments (if more than one) are
separated by commas.


`texput (a, [s_1, s_2, s_3], matchfix)` causes the
`tex` function to interpolate *s_1* and *s_2* into the TeX output
on either side of the arguments of *a*, with *s_3* separating the
arguments.


See also `tex` and `tex1`.


Examples:


Assign TeX output for a variable.







```maxima
maxima

(%i1) texput (me,"\\mu_e");
(%o1)                         \mu_e


(%i2) tex (me);
$$\mu_e$$
(%o2)                         false
```


Assign TeX output for an ordinary function (not an operator).







```maxima
maxima

(%i1) texput (lcm, "\\mathrm{lcm}");
(%o1)                     \mathrm{lcm}


(%i2) tex (lcm (a, b));
$$\mathrm{lcm}\left(a , b\right)$$
(%o2)                         false
```


Call a function to generate TeX output.









```maxima
maxima

(%i1) texfoo (e) := block ([a, b], [a, b] : args (e),
  concat ("\\left[\\stackrel{",tex1(b),"}{",tex1(a),"}\\right]"))$


(%i2) texput (foo, texfoo);
(%o2)                        texfoo


(%i3) tex (foo (2^x, %pi));
$$\left[\stackrel{\pi}{2^{x}}\right]$$
(%o3)                         false
```


Assign TeX output for a prefix operator.








```maxima
maxima

(%i1) prefix ("grad");
(%o1)                         grad


(%i2) texput ("grad", " \\nabla ", prefix);
(%o2)                        \nabla 


(%i3) tex (grad f);
$$ \nabla f$$
(%o3)                         false
```


Assign TeX output for an infix operator.








```maxima
maxima

(%i1) infix ("~");
(%o1)                           ~


(%i2) texput ("~", " \\times ", infix);
(%o2)                        \times 


(%i3) tex (a ~ b);
$$a \times b$$
(%o3)                         false
```


Assign TeX output for a postfix operator.








```maxima
maxima

(%i1) postfix ("##");
(%o1)                          ##


(%i2) texput ("##", "!!", postfix);
(%o2)                          !!


(%i3) tex (x ##);
$$x!!$$
(%o3)                         false
```


Assign TeX output for a nary operator.








```maxima
maxima

(%i1) nary ("@@");
(%o1)                          @@


(%i2) texput ("@@", " \\circ ", nary);
(%o2)                         \circ 


(%i3) tex (a @@ b @@ c @@ d);
$$a \circ b \circ c \circ d$$
(%o3)                         false
```


Assign TeX output for a nofix operator.








```maxima
maxima

(%i1) nofix ("foo");
(%o1)                          foo


(%i2) texput ("foo", "\\mathsc{foo}", nofix);
(%o2)                     \mathsc{foo}


(%i3) tex (foo);
$$\mathsc{foo}$$
(%o3)                         false
```


Assign TeX output for a matchfix operator.













```maxima
maxima

(%i1) matchfix ("<<", ">>");
(%o1)                          <<


(%i2) texput ("<<", [" \\langle ", " \\rangle "], matchfix);
(%o2)                [ \langle ,  \rangle ]


(%i3) tex (<<a>>);
$$ \langle a \rangle $$
(%o3)                         false


(%i4) tex (<<a, b>>);
$$ \langle a , b \rangle $$
(%o4)                         false


(%i5) texput ("<<", [" \\langle ", " \\rangle ", " \\, | \\,"],
      matchfix);
(%o5)           [ \langle ,  \rangle ,  \, | \,]


(%i6) tex (<<a>>);
$$ \langle a \rangle $$
(%o6)                         false


(%i7) tex (<<a, b>>);
$$ \langle a \, | \,b \rangle $$
(%o7)                         false
```

See also: `tex`, `tex1`.

### Function: tokens (tokens, string, tokens, string, test)

Returns a list of tokens, which have been extracted from *string*.
The tokens are substrings whose characters satisfy a certain test function.
If test is not given, *constituent* is used as the default test.
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}` is the set of test functions. 
(The Lisp-version of `tokens` is written by Paul Graham. ANSI Common Lisp, 1996, page 67.)


Examples:



```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parse_string,%);
(%o3)                      [5, 10, 24]
```

### Variable: ttyoff

Default value: `false`


When `ttyoff` is `true`, output expressions are not displayed.
Output expressions are still computed and assigned labels.  See `labels`.


Text printed by built-in Maxima functions, such as error messages and the output
of `describe`, is not affected by `ttyoff`.

See also: `labels`, `describe`.

### Function: type (type,v1...vn)

Places information in the gentran symbol table to assign *type* to
variables *v1...vn*. This may result in type declarations
printed by gentran depending on the setting of gendecs. **type**
must be called from within gentran and does not evaluate its arguments
unless **eval**() is used.

### Function: uncoef (clist)

Reconstructs the expression from a coefficient list *clist*. The
coefficient list can be any of the coefficient list forms.

### Function: unmarkvar (vname)

unmarkvar "unmarks" variable name *vname* to indicate that it no
longer holds a significant value.

### Variable: usefortcomplex

Default: **false**


If usefortcomplex is true, real numbers in expressions declared to be
complex by *type(complex,...)* will be printed in Fortran
complex number format *(realpart,0.0)*. This is a purely syntactic
device and does not carry out any complex calculations.

### Function: with_default_2d_display (expr)

While maxima by default realizes 2d Output using ASCII-Art some frontend
change that to TeX, MathML or a specific XML dialect that better suits
the needs for this specific frontend. `with_default_2d_display`
temporarily switches maxima to the default 2D ASCII Art formatter for
outputting the result of `expr`.


See also `set_alt_display` and `display2d`.

See also: `set_alt_display`, `display2d`.

### Function: with_stdout (with_stdout, f, expr_1, expr_2, expr_3, ..., with_stdout, s, expr_1, expr_2, expr_3, ...)

Evaluates *expr_1*, *expr_2*, *expr_3*, ... and writes any
output thus generated to a file *f* or output stream *s*.  The evaluated
expressions are not written to the output.  Output may be generated by
`print`, `display`, `grind`, among other functions.


The global flag `file_output_append` governs whether `with_stdout`
appends or truncates the output file *f*.  When `file_output_append`
is `true`, `with_stdout` appends to the output file.  Otherwise,
`with_stdout` truncates the output file.  In either case,
`with_stdout` creates the file if it does not yet exist.


`with_stdout` returns the value of its final argument.


See also `writefile` and `display2d`.








```maxima
(%i1) with_stdout ("tmp.out", for i:5 thru 10 do
      print (i, "! yields", i!))$
(%i2) printfile ("tmp.out")$
5 ! yields 120 
6 ! yields 720 
7 ! yields 5040 
8 ! yields 40320 
9 ! yields 362880 
10 ! yields 3628800
```

See also: `print`, `display`, `grind`, `file_output_append`, `writefile`, `display2d`.

### Function: write_binary_data (X, D)

Writes the object *X*, comprising binary 8-byte IEEE 754 floating-point numbers,
to the destination *D*.
Other kinds of numbers are coerced to 8-byte floats.
`write_binary_data` cannot write non-numeric data.


The object *X* may be a list, a nested list, a matrix,
or an array created by `array` or `make_array`;
*X* cannot be a hashed array or any other type of object.
`write_binary_data` writes nested lists, matrices, and arrays in row-major order.


The destination *D* may be a file name or a stream.
When the destination is a file name,
the global variable `file_output_append` governs
whether the output file is appended or truncated.
When the destination is a stream,
no special action is taken by `write_binary_data` after all the data are written;
in particular, the stream remains open.


The byte order in elements of the destination
is specified by `assume_external_byte_order`.


See also `write_005fdata`.

See also: `write_data`.

### Function: write_data (write_data, X, D, write_data, X, D, separator_flag)

Writes the object *X* to the destination *D*.


`write_data` writes a matrix in row-major order,
with one line per row.


`write_data` writes an array created by `array` or `make_array`
in row-major order, with a new line at the end of every slab.
Higher-dimensional slabs are separated by additional new lines.


`write_data` writes a hashed array with each key followed by
its associated list on one line.


`write_data` writes a nested list with each sublist on one line.


`write_data` writes a flat list all on one line.


The destination *D* may be a file name or a stream.
When the destination is a file name,
the global variable `file_output_append` governs
whether the output file is appended or truncated.
When the destination is a stream,
no special action is taken by `write_data` after all the data are written;
in particular, the stream remains open.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, `space`, and `tab`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openw` and `read_005fmatrix`.

See also: `openw`, `read_matrix`.

### Function: writebyte (byte, stream)

Writes *byte* to *stream* which must be a binary output stream. 
`writebyte` returns `byte`.


Example: Write some bytes to a binary file output stream. 
In this example all bytes correspond to printable characters and are printed 
by `printfile`. 
The bytes remain in the stream until `flush_output` or `close` have been called.



```maxima
(%i1) ibase: obase: 16.$

(%i2) bytes: map(cint, charlist("GNU/Linux"));
(%o2)                [47, 4E, 55, 2F, 4C, 69, 6E, 75, 78]
(%i3) out: openw_binary("test.bin");
(%o3)                      #<output stream test.bin>
(%i4) for i thru 3 do writebyte(bytes[i], out);
(%o4)                                done
(%i5) printfile("test.bin")$

(%i6) flength(out);
(%o6)                                  0
(%i7) flush_output(out);
(%o7)                                true
(%i8) flength(out);
(%o8)                                  3
(%i9) printfile("test.bin")$
GNU
(%i0A) for b in rest(bytes,3) do writebyte(b, out);
(%o0A)                               done
(%i0B) close(out);
(%o0B)                               true
(%i0C) printfile("test.bin")$
GNU/Linux
```

### Function: writefile (filename)

Begins writing a transcript of the Maxima session to *filename*.
All interaction between the user and Maxima is then recorded in this file,

just as it appears on the console.


As the transcript is printed in the console output format, it cannot be reloaded
into Maxima.  To make a file containing expressions which can be reloaded,
see `save` and `stringout`.  `save` stores expressions in Lisp
form, while `stringout` stores expressions in Maxima form.


The effect of executing `writefile` when *filename* already exists
depends on the underlying Lisp implementation; the transcript file may be
clobbered, or the file may be appended.  `appendfile` always appends to
the transcript file.


It may be convenient to execute `playback` after `writefile` to save
the display of previous interactions.  As `playback` displays only the
input and output variables (`%i1`, `%o1`, etc.), any output generated
by a print statement in a function (as opposed to a return value) is not
displayed by `playback`.


`closefile` closes the transcript file opened by `writefile` or
`appendfile`.

See also: `save`, `stringout`, `appendfile`, `playback`, `closefile`.

