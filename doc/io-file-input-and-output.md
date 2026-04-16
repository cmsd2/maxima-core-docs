## File Input and Output

### Function: appendfile (filename)

Appends a console transcript to *filename*.  `appendfile` is the same
as `writefile`, except that the transcript file, if it exists, is
always appended.


`closefile` closes the transcript file opened by `appendfile` or
`writefile`.

See also: `writefile`, `closefile`.

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

### Function: closefile ()

Closes the transcript file opened by `writefile` or `appendfile`.

See also: `writefile`, `appendfile`.

### Function: directory (path)

Returns a list of the files and directories found in *path*
in the file system.


*path* may contain wildcard characters (i.e., characters which represent
unspecified parts of the path),
which include at least the asterisk on most systems,
and possibly other characters, depending on the system.


`directory` relies on the Lisp function DIRECTORY,
which may have implementation-specific behavior.

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

### Variable: fortindent

Default value: `0`


`fortindent` controls the left margin indentation of
expressions printed out by the `fortran` command.  `0` gives normal
printout (i.e., 6 spaces), and positive values will causes the
expressions to be printed farther to the right.

See also: `fortran`.

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

