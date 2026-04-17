## gentran

<!-- category: IO -->
<!-- keywords: ccurind -->
<!-- signatures: ccurind -->
### Variable: ccurind

Default: 0


Number of blank spaces printed at the beginning of each line of
generated’C’ code.

<!-- category: IO -->
<!-- keywords: clinelen -->
<!-- signatures: clinelen -->
### Variable: clinelen

Default: 80


Maximum number of characters printed on each line of generated ’C’ code.

<!-- category: IO -->
<!-- keywords: dblfloat -->
<!-- signatures: dblfloat -->
### Variable: dblfloat

Default: **false** If dblfloat is set to
true, floating point numbers in gentran output in implementations (such
as Windows Maxima under CLISP) in which float and double-float are the
same will be printed as *.d0. In implementations in which float and
double-float are different, floats will be coerced to double-float
before being printed.

<!-- category: IO -->
<!-- keywords: fortcurrind -->
<!-- signatures: fortcurrind -->
### Variable: fortcurrind

Default: 0


Number of blank spaces printed at the beginning of each line of
generated FORTRAN code (after column 6).

<!-- category: IO -->
<!-- keywords: fortlinelen -->
<!-- signatures: fortlinelen -->
### Variable: fortlinelen

default: 72


Maximum number of characters printed on each line of generated FORTRAN
code.

<!-- category: IO -->
<!-- keywords: gendecs -->
<!-- signatures: gendecs(name) -->
### Function: gendecs (name)

The gendecs command can be called any time the gendecs flag is switched
off to retrieve all type declarations from Gentran’s symbol table for
the given subprogram name (or the "current" subprogram if false is given
as its argument).

<!-- category: IO -->
<!-- keywords: genfloat -->
<!-- signatures: genfloat -->
### Variable: genfloat

Default: false


When set to true (or any non-false value), causes integers in generated
numerical code to be converted to floating point numbers, except in the
following places: array subscripts, exponents, and initial, final, and
step values in do-loops. An exception (for compatibility with Macsyma
2.4) is that numbers in exponentials (with base %e only) are
double-floated even when genfloat is false.

<!-- category: IO -->
<!-- keywords: genstmtincr -->
<!-- signatures: genstmtincr -->
### Variable: genstmtincr

Default: 1


number by which genstmtno is incremented each time a new statement
number is generated.

<!-- category: IO -->
<!-- keywords: genstmtno -->
<!-- signatures: genstmtno -->
### Variable: genstmtno

Default: 25000


Number used when a statement number must be generated. Note: it is the
user’s responsibility to make sure this number will not clash with
statement numbers in template files.

<!-- category: IO -->
<!-- keywords: gentran -->
<!-- signatures: gentran(stmt1, stmt2, ..., stmtn, [f1, f2, ... , fm]) -->
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

<!-- category: IO -->
<!-- keywords: gentran_off -->
<!-- signatures: gentran_off(sw) -->
### Function: gentran_off (sw)

Turns the given switch, *sw*, off.

<!-- category: IO -->
<!-- keywords: gentran_on -->
<!-- signatures: gentran_on(sw) -->
### Function: gentran_on (sw)

Turns on the mode switch *sw*.

<!-- category: IO -->
<!-- keywords: gentranin -->
<!-- signatures: gentranin(f1, f2, ..., fn, [f1, f2, ..., fm]) -->
### Function: gentranin (f1, f2, ..., fn, [f1, f2, ..., fm])

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

<!-- category: IO -->
<!-- keywords: gentraninshut -->
<!-- signatures: gentraninshut() -->
### Function: gentraninshut ()

A cleanup function to close input files in case where gentranin hung due
to error in template.

<!-- category: IO -->
<!-- keywords: gentranlang -->
<!-- signatures: gentranlang -->
### Variable: gentranlang

Default: fortran


Selects the target numerical language. Currently, gentranlang must be
fortran, ratfor, or c. Note that symbols entered in Maxima are
case-sensitive. gentranlang should not be set to FORTRAN, RATFOR or C.

<!-- category: IO -->
<!-- keywords: gentranopt -->
<!-- signatures: gentranopt -->
### Variable: gentranopt

Default: **false**


When set to true (or any non-false value), causes Gentran to replace
each block of straightline code by an optimized sequence of assignments
obtained from the Maxima optimize command. (The optimize command takes
an expression and replaces common subexpressions by temporary variable
names. It returns the resulting assignment statement, preceded by
common-subexpression-to-temporary-variable assignments.

<!-- category: IO -->
<!-- keywords: gentranout -->
<!-- signatures: gentranout(f1, f2, ..., fn) -->
### Function: gentranout (f1, f2, ..., fn)

Gentran maintains a list of files currently open for output by gentran
commands only. gentranout inserts each file name represented by
*f1, f2,... , fn* into that list and opens each one for output. It
also resets the current output file(s) to include all files in
*f1, f2, ... , fn*. gentranout returns the list of files represented by
*f1, f2, ... , fn*; i.e., the current output file(s) after the
command has been executed.

<!-- category: IO -->
<!-- keywords: gentranparser -->
<!-- signatures: gentranparser -->
### Variable: gentranparser

Default: **false**


If gentranparser is set to **true** Maxima forms input to gentran
will be parsed and an error will be produced if an expression cannot be
translated. Otherwise, untranslatable expressions may generate anomalous
output, sometimes containing explicit calls to Maxima functions.

<!-- category: IO -->
<!-- keywords: gentranpop -->
<!-- signatures: gentranpop(f1, f2, ..., fn) -->
### Function: gentranpop (f1, f2, ..., fn)

gentranpop deletes the top-most occurrence of the single element
containing the file name(s) represented by *f1, f2, ... , fn* from
the output stack. Files whose names have been completely removed from
the output stack are closed. The current output file is reset to the
(new) element on the top of the output stack. gentranpop returns the
current output file(s) after this command has been executed.

<!-- category: IO -->
<!-- keywords: gentranpush -->
<!-- signatures: gentranpush(f1, f2, ..., fn) -->
### Function: gentranpush (f1, f2, ..., fn)

gentranpush pushes the file list onto the output stack. Each file in the
list that is not already open for output is opened at this time. The
current output file is reset to this new element on the top of the
stack.

<!-- category: IO -->
<!-- keywords: gentranseg -->
<!-- signatures: gentranseg -->
### Variable: gentranseg

Default: **true**

<!-- category: IO -->
<!-- keywords: gentranshut -->
<!-- signatures: gentranshut(f1, f2, ..., fn) -->
### Function: gentranshut (f1, f2, ..., fn)

gentranshut creates a list of file names from *f1, f2, ... , fn*,
deletes each from the output file list, and closes the corresponding
files. If (all of) the current output file(s) are closed, then the
current output file is reset to the terminal. gentranshut returns (a
list of) the current output file(s) after the command has been executed.
**gentranshut**(**all**) will close all gentran output files.

<!-- category: IO -->
<!-- keywords: literal -->
<!-- signatures: literal(arg1, arg2, ... , argn) -->
### Function: literal (arg1, arg2, ... , argn)

where arg1, arg2, ... , argn is an argument list containing one or more
arg’s, each of which either is, or evaluates to, an atom. The atoms
*tab* and *cr* have special meanings. arg’s are not evaluated
unless given as arguments to eval. This function call is replaced by the
character sequence resulting from concatenation of the given atoms.
Double quotes are stripped from all string type arg’s, and each
occurrence of the reserved atom *tab* or *cr* is replaced by a
tab to the current level of indentation, or an end-of-line character.

<!-- category: IO -->
<!-- keywords: lrsetq -->
<!-- signatures: lrsetq(var, exp) -->
### Function: lrsetq (var, exp)

Where *var* is any Maxima matrix or array element with indices
which, after evaluation by Maxima, will result in expressions that can
be translated by Gentran; and *exp* is any user level expression
which, after evaluation, will result in an expression that can be
translated by Gentran into the target language. This is equivalent to
`var[eval(s1), eval(s2), ...]: eval(exp);`.

<!-- category: IO -->
<!-- keywords: lsetq -->
<!-- signatures: lsetq(var, exp) -->
### Function: lsetq (var, exp)

Where *var* is any Maxima user level matrix or array element with
indices which, after evaluation by Maxima, will result in expressions
that can be translated by Gentran, and *exp* is any Maxima user
level expression that can be translated into the target language. This
is equivalent to `var[eval(s1), eval(s2), ...]: exp` where *s1*, *s2*, ...
are indices.

<!-- category: IO -->
<!-- keywords: markedvarp -->
<!-- signatures: markedvarp(vname) -->
### Function: markedvarp (vname)

markedvarp tests whether the variable name *vname* is currently
marked.

<!-- category: IO -->
<!-- keywords: markvar -->
<!-- signatures: markvar(vname) -->
### Function: markvar (vname)

markvar "marks" variable name *vname* to indicate that it currently
holds a significant value.

<!-- category: IO -->
<!-- keywords: maxexpprintlen -->
<!-- signatures: maxexpprintlen -->
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

<!-- category: IO -->
<!-- keywords: minclinelen -->
<!-- signatures: minclinelen -->
### Variable: minclinelen

Default: 40


Minimum number of characters printed on each line of generated ’C’ code.

<!-- category: IO -->
<!-- keywords: minfortlinelen -->
<!-- signatures: minfortlinelen -->
### Variable: minfortlinelen

Default: 40


Minimum number of characters printed on each line of generated FORTRAN
code.

<!-- category: IO -->
<!-- keywords: optimvarname -->
<!-- signatures: optimvarname -->
### Variable: optimvarname

default: **’u**


is the preface used
to generate temporary file names produced by the optimizer when
**gentranopt** is **true**. When both gentranseg and
gentranopt are true, the optimizer generates temporary file names using
**optimvarname** while the segmentation routine uses
**tempvarname** preventing conflict.

<!-- category: IO -->
<!-- keywords: ratlinelen -->
<!-- signatures: ratlinelen -->
### Variable: ratlinelen

Default: 80


Maximum number of characters printed on each line of generated Ratfor
code.

<!-- category: IO -->
<!-- keywords: rsetq -->
<!-- signatures: rsetq(var, exp) -->
### Function: rsetq (var, exp)

Where *var* is any Maxima variable, matrix or array element, and
*exp* is any Maxima expression which, after evaluation by Maxima
results in an expression that can be translated by Gentran into the
target language. This is equivalent to VAR : EVAL(EXP) ;

<!-- category: IO -->
<!-- keywords: tablen -->
<!-- signatures: tablen -->
### Variable: tablen

Default: 4


Number of blank spaces printed for each new level of indentation.
(Automatic indentation can be turned off by setting this variable to 0.)

<!-- category: IO -->
<!-- keywords: tempvar -->
<!-- signatures: tempvar(type) -->
### Function: tempvar (type)

Generates temporary variable names by concatenating **tempvarname**
(default **’t**) with sequence numbers. If *type* is
non-false, *e.g.* "real*8" the corresponding type is assigned to
the variable in the gentran symbol table, which may be used to generate
declarations depending on the setting of the **gendecs** flag. It
is the users responsibility to make sure temporary variable names do not
conflict with the main program.

<!-- category: IO -->
<!-- keywords: tempvarname -->
<!-- signatures: tempvarname -->
### Variable: tempvarname

Default: **’t**


Name used as the prefix when generating temporary variable names.

<!-- category: IO -->
<!-- keywords: tempvarnum -->
<!-- signatures: tempvarnum -->
### Variable: tempvarnum

Default: 0


Number appended onto tempvarname to create a temporary variable name. If
the temporary variable name resulting from appending tempvarnum onto the
end of tempvarname has already been generated and still holds a useful
value or has a different type than requested, then the number is
incremented until one is found that was not previously generated or does
not still hold a significant value or a different type.

<!-- category: IO -->
<!-- keywords: tempvartype -->
<!-- signatures: tempvartype -->
### Variable: tempvartype

Default: **false**


Target language variable type (e.g., INTEGER, REAL*8, FLOAT, etc.) used
as a default for automatically generated variables whose type cannot be
determined otherwise. If tempvartype is false, then generated temporary
variables whose type cannot be determined are not automatically
declared.

<!-- category: IO -->
<!-- keywords: type -->
<!-- signatures: type(type,v1...vn) -->
### Function: type (type,v1...vn)

Places information in the gentran symbol table to assign *type* to
variables *v1...vn*. This may result in type declarations
printed by gentran depending on the setting of gendecs. **type**
must be called from within gentran and does not evaluate its arguments
unless **eval**() is used.

<!-- category: IO -->
<!-- keywords: unmarkvar -->
<!-- signatures: unmarkvar(vname) -->
### Function: unmarkvar (vname)

unmarkvar "unmarks" variable name *vname* to indicate that it no
longer holds a significant value.

<!-- category: IO -->
<!-- keywords: usefortcomplex -->
<!-- signatures: usefortcomplex -->
### Variable: usefortcomplex

Default: **false**


If usefortcomplex is true, real numbers in expressions declared to be
complex by *type(complex,...)* will be printed in Fortran
complex number format *(realpart,0.0)*. This is a purely syntactic
device and does not carry out any complex calculations.

