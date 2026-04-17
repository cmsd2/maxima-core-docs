## Command Line

<!-- category: Programming -->
<!-- keywords: $ -->
<!-- signatures: $ -->
### Function: $

The dollar sign `$` terminates an input expression,
and the most recent output `%` and an output label, e.g. `%o1`,
are assigned the result, but the result is not displayed.


See also `_003b`.


Example:







```maxima
maxima
(%i1) 1 + 2 + 3 $

(%i2) %;
(%o2)                           6


(%i3) %o1;
(%o3)                           6
```

See also: `;`.

<!-- category: Programming -->
<!-- keywords: %, Previous output -->
<!-- signatures: % -->
### Variable: %

`%` is the output expression (e.g., `%o1`, `%o2`, `%o3`,
...) most recently computed by Maxima, whether or not it was displayed.


`%` is recognized by `batch` and `load`.  In a file processed
by `batch`, `%` has the same meaning as at the interactive prompt.
In a file processed by `load`, `%` is bound to the output expression
most recently computed at the interactive prompt or in a batch file; `%`
is not bound to output expressions in the file being processed.


See also `_`, `%%`, and `_0025th`.

See also: `batch`, `load`, `_`, `%%`, `%th`.

<!-- category: Programming -->
<!-- keywords: %%, Previous result in compound expression -->
<!-- signatures: %% -->
### Variable: %%

In compound statements, namely `block`, `lambda`, or
`(s_1, ..., s_n)`, `%%` is the value of the previous
statement.


At the first statement in a compound statement, or outside of a compound
statement, `%%` is undefined.


`%%` is recognized by `batch` and `load`, and it has the
same meaning as at the interactive prompt.


See also `_0025`.


Examples:


The following two examples yield the same result.








```maxima
maxima

(%i1) block (integrate (x^5, x), ev (%%, x=2) - ev (%%, x=1));
                               21
(%o1)                          --
                               2


(%i2) block ([prev], prev: integrate (x^5, x),
              ev (prev, x=2) - ev (prev, x=1));
                               21
(%o2)                          --
                               2
```


A compound statement may comprise other compound statements.  Whether a
statement be simple or compound, `%%` is the value of the previous
statement.






```maxima
maxima

(%i1) block (block (a^n, %%*42), %%/6);
                                 n
(%o1)                         7 a
```


Within a compound statement, the value of `%%` may be inspected at a break
prompt, which is opened by executing the `break` function.  For example,
entering `%%;` in the following example yields `42`.



```maxima
maxima
(%i4) block (a: 42, break ())$

Entering a Maxima break point. Type 'exit;' to resume.
_%%;
42
_
```

See also: `block`, `lambda`, `batch`, `load`, `%`, `break`.

<!-- category: Programming -->
<!-- keywords: %th -->
<!-- signatures: %th(i) -->
### Function: %th (i)

The value of the *i*’th previous output expression.  That is, if the next
expression to be computed is the *n*’th output, `%th (m)` is the
(*n* - *m*)’th output.


`%th` is recognized by `batch` and `load`.  In a file processed
by `batch`, `%th` has the same meaning as at the interactive prompt.
In a file processed by `load`, `%th` refers to output expressions most
recently computed at the interactive prompt or in a batch file; `%th` does
not refer to output expressions in the file being processed.


See also `%` and `_0025_0025`.


Example:


`%th` is useful in `batch` files or for referring to a group of
output expressions.  This example sets `s` to the sum of the last five
output expressions.







```maxima
maxima

(%i1) 1;2;3;4;5;
(%o1)                           1
(%o2)                           2
(%o3)                           3
(%o4)                           4
(%o5)                           5


(%i6) block (s: 0, for i:1 thru 5 do s: s + %th(i), s);
(%o6)                          15
```

See also: `batch`, `load`, `%`, `%%`.

<!-- category: Programming -->
<!-- keywords: ; -->
<!-- signatures: ; -->
### Function: ;

The semicolon `;` terminates an input expression,
and the resulting output is displayed.


See also `_0024`.


Example:





```maxima
maxima

(%i1) 1 + 2 + 3;
(%o1)                           6
```

See also: `$`.

<!-- category: Programming -->
<!-- keywords: ? -->
<!-- signatures: ? -->
### Function: ?

As prefix to a function or variable name, `?` signifies that the name is a
Lisp name, not a Maxima name.  For example, `?round` signifies the Lisp
function `ROUND`.  See `Lisp-and-Maxima` for more on this point.


The notation `? word` (a question mark followed a word, separated by
whitespace) is equivalent to `describe("word")`.  The question mark must
occur at the beginning of an input line; otherwise it is not recognized as a
request for documentation.  See also `describe`.

See also: `Lisp-and-Maxima`, `describe`.

<!-- category: Programming -->
<!-- keywords: ?? -->
<!-- signatures: ?? -->
### Function: ??

The notation `?? word` (`??` followed a word, separated by whitespace)
is equivalent to `describe("word", inexact)`.  The question mark must occur
at the beginning of an input line; otherwise it is not recognized as a request
for documentation.  See also `describe`.

See also: `describe`.

<!-- category: Programming -->
<!-- keywords: _, Previous input -->
<!-- signatures: _ -->
### Variable: _

`_` is the most recent input expression (e.g., `%i1`, `%i2`,
`%i3`, ...).


`_` is assigned the input expression before the input is simplified or
evaluated.  However, the value of `_` is simplified (but not evaluated)
when it is displayed.


`_` is recognized by `batch` and `load`.  In a file processed
by `batch`, `_` has the same meaning as at the interactive prompt.
In a file processed by `load`, `_` is bound to the input expression
most recently evaluated at the interactive prompt or in a batch file; `_`
is not bound to the input expressions in the file being processed.


See also `__` and `_0025`.


Examples:


















```maxima
maxima

(%i1) 13 + 29;
(%o1)                          42


(%i2) :lisp $_
((MPLUS) 13 29)


(%i2) _;
(%o2)                          42


(%i3) sin (%pi/2);
(%o3)                           1


(%i4) :lisp $_
((%SIN) ((MQUOTIENT) $%PI 2))


(%i4) _;
(%o4)                           1

(%i5) a: 13$
(%i6) b: 29$

(%i7) a + b;
(%o7)                          42


(%i8) :lisp $_
((MPLUS) $A $B)


(%i8) _;
(%o8)                         b + a


(%i9) a + b;
(%o9)                          42


(%i10) ev (_);
(%o10)                         42
```

See also: `batch`, `load`, `__`, `%`.

<!-- category: Programming -->
<!-- keywords: __, Current input expression -->
<!-- signatures: __ -->
### Variable: __

`__` is the input expression currently being evaluated.  That is, while an
input expression *expr* is being evaluated, `__` is *expr*.


`__` is assigned the input expression before the input is simplified or
evaluated.  However, the value of `__` is simplified (but not evaluated)
when it is displayed.


`__` is recognized by `batch` and `load`.  In a file processed
by `batch`, `__` has the same meaning as at the interactive prompt.
In a file processed by `load`, `__` is bound to the input expression
most recently entered at the interactive prompt or in a batch file; `__`
is not bound to the input expressions in the file being processed.  In
particular, when `load (filename)` is called from the interactive
prompt, `__` is bound to `load (filename)` while the file is
being processed.


See also `_` and `_0025`.


Examples:










```maxima
maxima

(%i1) print ("I was called as", __);
I was called as print(I was called as, __) 
(%o1)              print(I was called as, __)


(%i2) foo (__);
(%o2)                     foo(foo(__))


(%i3) g (x) := (print ("Current input expression =", __), 0);
(%o3) g(x) := (print("Current input expression =", __), 0)


(%i4) [aa : 1, bb : 2, cc : 3];
(%o4)                       [1, 2, 3]


(%i5) (aa + bb + cc)/(dd + ee + g(x));
                            cc + bb + aa
Current input expression = -------------- 
                           g(x) + ee + dd
                                6
(%o5)                        -------
                             ee + dd
```

See also: `batch`, `load`, `_`, `%`.

<!-- category: Programming -->
<!-- keywords: eval_string_lisp -->
<!-- signatures: eval_string_lisp(str) -->
### Function: eval_string_lisp (str)

Sequentially read lisp forms from the string *str* and evaluate them.
Any values produced from the last form are returned as a Maxima list.


Examples:












```maxima
maxima

(%i1) eval_string_lisp ("");
(%o1)                          []


(%i2) eval_string_lisp ("(values)");
(%o2)                          []


(%i3) eval_string_lisp ("69");
(%o3)                         [69]


(%i4) eval_string_lisp ("1 2 3");
(%o4)                          [3]


(%i5) eval_string_lisp ("(values 1 2 3)");
(%o5)                       [1, 2, 3]


(%i6) eval_string_lisp ("(defun $foo (x) (* 2 x))");
(%o6)                         [foo]


(%i7) foo (5);
(%o7)                          10
```


See also `eval_005fstring`.

See also: `eval_string`.

<!-- category: Programming -->
<!-- keywords: inchar -->
<!-- signatures: inchar -->
### Variable: inchar

Default value: `%i`


`inchar` is the prefix of the labels of expressions entered by the user.
Maxima automatically constructs a label for each input expression by 
concatenating `inchar` and `linenum`.


`inchar` may be assigned any string or symbol, not necessarily a single 
character.  A string is coerced to a symbol with the same printed
representation.  Because Maxima internally takes into account only the first char of
the prefix, the prefixes `inchar`, `outchar`, and
`linechar` should have a different first char.  Otherwise some commands
like `kill(inlabels)` do not work as expected.


See also `labels`.


Example:







```maxima
maxima

(%i1) inchar: "input";
(%o1)                         input


(input2) expand((a+b)^3);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
```

See also: `linenum`, `outchar`, `linechar`, `labels`.

<!-- category: Programming -->
<!-- keywords: infolists -->
<!-- signatures: infolists -->
### Variable: infolists

Default value: `[]`


`infolists` is a list of the names of all of the information
lists in Maxima.  These are:



**labels** — All bound `%i`, `%o`, and `%t` labels.
**values** — All bound atoms which are user variables, not Maxima options or switches,
created by `:` or `::` or functional binding.
**functions** — All user-defined functions, created by `:=` or `define`.
**arrays** — All arrays, `hashed arrays` and `memoizing functions`.
**macros** — All user-defined macro functions, created by `_003a_003a_003d`.
**myoptions** — All options ever reset by the user (whether or not they
are later reset to their default values).
**rules** — All user-defined pattern matching and simplification rules, created
by `tellsimp`, `tellsimpafter`, `defmatch`, or
`defrule`.
**aliases** — All atoms which have a user-defined alias, created by the `alias`,
`ordergreat`, `orderless` functions or by declaring the atom as a
`noun` with `declare`.
**dependencies** — All atoms which have functional dependencies, created by the
`depends`, `dependencies`, or `gradef` functions.
**gradefs** — All functions which have user-defined derivatives, created by the
`gradef` function.
**props** — All atoms which have any property other than those mentioned above, such as
properties established by `atvalue` or `matchdeclare`, etc.,
as well as properties established in the `declare` function.
**structures** — All structs defined using `defstruct`.
**let_rule_packages** — All user-defined `let` rule packages
plus the special package `default_005flet_005frule_005fpackage`.
(`default_let_rule_package` is the name of the rule package used when
one is not explicitly set by the user.)

See also: `:`, `::`, `:=`, `define`, `hashed-arrays`, `memoizing-functions`, `::=`, `tellsimp`, `tellsimpafter`, `defmatch`, `defrule`, `alias`, `ordergreat`, `orderless`, `noun`, `declare`, `depends`, `dependencies`, `gradef`, `atvalue`, `matchdeclare`, `defstruct`, `let`, `default_let_rule_package`.

<!-- category: Programming -->
<!-- keywords: kill -->
<!-- signatures: kill(a_1, ..., a_n), kill(labels), kill(inlabels, outlabels, linelabels), kill(n), kill([m, n]), kill(values, functions, arrays, ...), kill(all), kill(allbut(a_1, ..., a_n)) -->
### Function: kill (a_1, ..., a_n)

Removes all bindings (value, function, array, or rule) from the arguments
*a_1*, ..., *a_n*.  An argument *a_k* may be a symbol or a
single array element.  When *a_k* is a single array element, `kill`
unbinds that element without affecting any other elements of the array.


Several special arguments are recognized.  Different kinds of arguments
may be combined, e.g., `kill (inlabels, functions, allbut (foo, bar))`.


`kill (labels)` unbinds all input, output, and intermediate expression
labels created so far.  `kill (inlabels)` unbinds only input labels which
begin with the current value of `inchar`.  Likewise,
`kill (outlabels)` unbinds only output labels which begin with the current
value of `outchar`, and `kill (linelabels)` unbinds only
intermediate expression labels which begin with the current value of
`linechar`.


`kill (n)`, where *n* is an integer,
unbinds the *n* most recent input and output labels.


`kill ([m, n])` unbinds input and output labels *m* through
*n*.


`kill (infolist)`, where *infolist* is any item in
`infolists` (such as `values`, `functions`, or
`arrays`) unbinds all items in *infolist*.
See also `infolists`.


`kill (all)` unbinds all items on all infolists.  `kill (all)` does
not reset global variables to their default values; see `reset` on this
point.


`kill (allbut (a_1, ..., a_n))` unbinds all items on all
infolists except for *a_1*, ..., *a_n*.
`kill (allbut (infolist))` unbinds all items except for the ones on
*infolist*, where *infolist* is `values`,
`functions`, `arrays`, etc.


The memory taken up by a bound property is not released until all symbols are
unbound from it.  In particular, to release the memory taken up by the value of
a symbol, one unbinds the output label which shows the bound value, as well as
unbinding the symbol itself.


`kill` quotes its arguments.  The quote-quote operator `''`
defeats quotation.


`kill (symbol)` unbinds all properties of *symbol*.  In contrast,
the functions `remvalue`, `remfunction`,
`remarray`, and `remrule` unbind a specific property.
Note that facts declared by `assume` don’t require a symbol they apply to,
therefore aren’t stored as properties of symbols and therefore aren’t affected
by `kill`.


`kill` always returns `done`, even if an argument has no binding.

See also: `inchar`, `outchar`, `linechar`, `values`, `functions`, `arrays`, `infolists`, `reset`, `remvalue`, `remfunction`, `remarray`, `remrule`, `assume`.

<!-- category: Programming -->
<!-- keywords: labels -->
<!-- signatures: labels(symbol) -->
### Function: labels (symbol)

Returns the list of input, output, or intermediate expression labels which begin
with *symbol*.  Typically *symbol* is the value of
`inchar`, `outchar`, or `linechar`.
If no labels begin with *symbol*, `labels` returns an empty list.


By default, Maxima displays the result of each user input expression, giving the
result an output label.  The output display is suppressed by terminating the
input with `$` (dollar sign) instead of `;` (semicolon).  An output
label is constructed and bound to the result, but not displayed, and the label
may be referenced in the same way as displayed output labels.  See also
`%`, `%%`, and `_0025th`.


Intermediate expression labels can be generated by some functions.  The option
variable `programmode` controls whether `solve` and some other
functions generate intermediate expression labels instead of returning a list of
expressions.  Some other functions, such as `ldisplay`, always generate
intermediate expression labels.


See also `inchar`, `outchar`, `linechar`, and
`infolists`.

See also: `inchar`, `outchar`, `linechar`, `%`, `%%`, `%th`, `programmode`, `solve`, `ldisplay`, `infolists`.

<!-- category: Programming -->
<!-- keywords: linechar -->
<!-- signatures: linechar -->
### Variable: linechar

Default value: `%t`


`linechar` is the prefix of the labels of intermediate expressions 
generated by Maxima.  Maxima constructs a label for each intermediate expression 
(if displayed) by concatenating `linechar` and `linenum`.


`linechar` may be assigned any string or symbol, not necessarily a single 
character.  A string is coerced to a symbol with the same printed
representation.  Because Maxima internally takes into account only the first char of
the prefix, the prefixes `inchar`, `outchar`, and
`linechar` should have a different first char.  Otherwise some commands
like `kill(inlabels)` do not work as expected.


Intermediate expressions might or might not be displayed.
See `programmode` and `labels`.

See also: `linenum`, `inchar`, `outchar`, `programmode`, `labels`.

<!-- category: Programming -->
<!-- keywords: linenum -->
<!-- signatures: linenum -->
### Variable: linenum

The line number of the current pair of input and output expressions.

<!-- category: Programming -->
<!-- keywords: myoptions -->
<!-- signatures: myoptions -->
### Variable: myoptions

Default value: `[]`


`myoptions` is the list of all options ever reset by the user,
whether or not they get reset to their default value.

<!-- category: Programming -->
<!-- keywords: nolabels -->
<!-- signatures: nolabels -->
### Variable: nolabels

Default value: `false`


When `nolabels` is `true`, input and output result labels (`%i`
and `%o`, respectively) are displayed, but the labels are not bound to
results, and the labels are not appended to the `labels` list.  Since
labels are not bound to results, garbage collection can recover the memory taken
up by the results.


Otherwise input and output result labels are bound to results, and the labels
are appended to the `labels` list.


Intermediate expression labels (`%t`) are not affected by `nolabels`;
whether `nolabels` is `true` or `false`, intermediate expression
labels are bound and appended to the `labels` list.


See also `batch`, `load`, and `labels`.

See also: `labels`, `batch`, `load`.

<!-- category: Programming -->
<!-- keywords: optionset -->
<!-- signatures: optionset -->
### Variable: optionset

Default value: `false`


When `optionset` is `true`, Maxima prints out a message whenever a
Maxima option is reset.  This is useful if the user is doubtful of the spelling
of some option and wants to make sure that the variable he assigned a value to
was truly an option variable.


Example:







```maxima
maxima

(%i1) optionset:true;
(%o1)                         true


(%i2) gamma_expand:true;
assignment: assigning to option gamma_expand
(%o2)                         true
```

<!-- category: Programming -->
<!-- keywords: outchar -->
<!-- signatures: outchar -->
### Variable: outchar

Default value: `%o`


`outchar` is the prefix of the labels of expressions computed by Maxima.
Maxima automatically constructs a label for each computed expression by 
concatenating `outchar` and `linenum`.


`outchar` may be assigned any string or symbol, not necessarily a single 
character.  A string is coerced to a symbol with the same printed
representation.  Because Maxima internally takes into account only the first char of
the prefix, the prefixes `inchar`, `outchar` and
`linechar` should have a different first char.  Otherwise some commands
like `kill(inlabels)` do not work as expected.


See also `labels`.


Example:







```maxima
maxima

(%i1) outchar: "output";
(output1)                    output


(%i2) expand((a+b)^3);
                     3        2      2      3
(output2)           b  + 3 a b  + 3 a  b + a
```

See also: `linenum`, `inchar`, `linechar`, `labels`.

<!-- category: Programming -->
<!-- keywords: playback -->
<!-- signatures: playback(), playback(n), playback([m, n]), playback([m]), playback(input), playback(slow), playback(time), playback(grind) -->
### Function: playback ()

Displays input, output, and intermediate expressions, without recomputing them.
`playback` only displays the expressions bound to labels; any other output
(such as text printed by `print` or `describe`, or error messages)
is not displayed.  See also `labels`.


`playback` quotes its arguments.  The quote-quote operator `''`
defeats quotation.  `playback` always returns `done`.


`playback ()` (with no arguments) displays all input, output, and
intermediate expressions generated so far.  An output expression is displayed
even if it was suppressed by the `$` terminator when it was originally
computed.


`playback (n)` displays the most recent *n* expressions.
Each input, output, and intermediate expression counts as one.


`playback ([m, n])` displays input, output, and intermediate
expressions with numbers from *m* through *n*, inclusive.


`playback ([m])` is equivalent to
`playback ([m, m])`; this usually prints one pair of input and
output expressions.


`playback (input)` displays all input expressions generated so far.


`playback (slow)` pauses between expressions and waits for the user to
press `enter`.  This behavior is similar to `demo`.

`playback (slow)` is useful in conjunction with `save` or
`stringout` when creating a secondary-storage file in order to pick out
useful expressions.


`playback (time)` displays the computation time for each expression.




`playback (grind)` displays input expressions in the same format as the
`grind` function.  Output expressions are not affected by the `grind`
option.  See `grind`.


Arguments may be combined, e.g., `playback ([5, 10], grind, time, slow)`.

See also: `print`, `describe`, `labels`, `demo`, `stringout`, `grind`.

<!-- category: Programming -->
<!-- keywords: prompt -->
<!-- signatures: prompt -->
### Variable: prompt

Default value: `_`


`prompt` is the prompt symbol of the `demo` function,
`playback (slow)` mode, and the Maxima break loop (as invoked by
`break`).

See also: `demo`, `break`.

<!-- category: Programming -->
<!-- keywords: quit -->
<!-- signatures: quit([exit-code]) -->
### Function: quit ([exit-code])

Terminates the Maxima session.  Note that the function must be invoked as
`quit();` or `quit()$`, not `quit` by itself.
`quit` supports returning an exit code to the shell for Lisps and
OSes that support exit codes.  The default exit code is 0 (usually
indicating no errors encountered).  Thus `quit(1)` indicates to the
shell that maxima exited with some kind of failure.  This is useful in
scripts where maxima can indicate to the shell that maxima failed to
compute something or some other bad thing happened.


To stop a lengthy computation, type `control-C`.  The default action is to
return to the Maxima prompt.  If `*debugger-hook*` is `nil`,
`control-C` opens the Lisp debugger.  See also `Debugging`.

See also: `Debugging`.

<!-- category: Programming -->
<!-- keywords: read -->
<!-- signatures: read(expr_1, ..., expr_n) -->
### Function: read (expr_1, ..., expr_n)

Prints *expr_1*, ..., *expr_n*, then reads one expression from the
console and returns the evaluated expression.  The expression is terminated with
a semicolon `;` or dollar sign `$`.


See also `readonly`


Example:



```maxima
maxima
(%i1) foo: 42$ 
(%i2) foo: read ("foo is", foo, " -- enter new value.")$
foo is 42  -- enter new value. 
(a+b)^3;
(%i3) foo;
                                     3
(%o3)                         (b + a)
```

See also: `readonly`.

<!-- category: Programming -->
<!-- keywords: readonly -->
<!-- signatures: readonly(expr_1, ..., expr_n) -->
### Function: readonly (expr_1, ..., expr_n)

Prints *expr_1*, ..., *expr_n*, then reads one expression from the
console and returns the expression (without evaluation).  The expression is
terminated with a `;` (semicolon) or `$` (dollar sign).


See also `read`.


Examples:



```maxima
maxima
(%i1) aa: 7$
(%i2) foo: readonly ("Enter an expression:");
Enter an expression: 
2^aa;
                                  aa
(%o2)                            2
(%i3) foo: read ("Enter an expression:");
Enter an expression: 
2^aa;
(%o3)                            128
```

See also: `read`.

<!-- category: Programming -->
<!-- keywords: reset -->
<!-- signatures: reset() -->
### Function: reset ()

Resets many global variables and options, and some other variables, to their
default values.


`reset` processes the variables on the Lisp list
`*variable-initial-values*`.  The Lisp macro `defmvar` puts variables
on this list (among other actions).  Many, but not all, global variables and
options are defined by `defmvar`, and some variables defined by
`defmvar` are not global variables or options.

<!-- category: Programming -->
<!-- keywords: showtime -->
<!-- signatures: showtime -->
### Variable: showtime

Default value: `false`


When `showtime` is `true`, the computation time and elapsed time is
printed with each output expression.


The computation time is always recorded, so `time` and `playback` can
display the computation time even when `showtime` is `false`.


See also `timer`.

See also: `time`, `playback`, `timer`.

<!-- category: Programming -->
<!-- keywords: to_lisp -->
<!-- signatures: to_lisp() -->
### Function: to_lisp ()

Enters the Lisp system under Maxima.  `(to-maxima)` returns to Maxima.


Example:


Define a function and enter the Lisp system under Maxima.  The definition is
inspected on the property list, then the function definition is extracted,
factored and stored in the variable `$result`.  The variable can be used in Maxima
after returning to Maxima.



```maxima
maxima
(%i1) f(x):=x^2+x;
                                  2
(%o1)                    f(x) := x  + x
(%i2) to_lisp();
Type (to-maxima) to restart, ($quit) to quit Maxima.
MAXIMA> (symbol-plist '$f)
(MPROPS (NIL MEXPR ((LAMBDA) ((MLIST) $X) 
                             ((MPLUS) ((MEXPT) $X 2) $X))))
MAXIMA> (setq $result ($factor (caddr (mget '$f 'mexpr))))
((MTIMES SIMP FACTORED) $X ((MPLUS SIMP IRREDUCIBLE) 1 $X))
MAXIMA> (to-maxima)
Returning to Maxima
(%o2)                         true
(%i3) result;
(%o3)                       x (x + 1)
```

<!-- category: Programming -->
<!-- keywords: values -->
<!-- signatures: values -->
### Variable: values

Initial value: `[]`


`values` is a list of all bound user variables (not Maxima options or
switches).  The list comprises symbols bound by `:`, or `_003a_003a`.


If the value of a variable is removed with the commands `kill`, 
`remove`, or `remvalue` the variable is deleted from
`values`.


See `functions` for a list of user defined functions.


Examples:


First, `values` shows the symbols `a`, `b`, and `c`, but 
not `d`, it is not bound to a value, and not the user function `f`.
The values are removed from the variables.  `values` is the empty list.









```maxima
maxima

(%i1) [a:99, b:: a-90, c:a-b, d, f(x):=x^2];
                                           2
(%o1)              [99, 9, 90, d, f(x) := x ]


(%i2) values;
(%o2)                       [a, b, c]


(%i3) [kill(a), remove(b,value), remvalue(c)];
(%o3)                   [done, done, [c]]


(%i4) values;
(%o4)                          []
```

See also: `:`, `::`, `remove`, `remvalue`, `functions`.

