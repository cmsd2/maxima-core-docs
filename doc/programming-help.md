## Help

### Function: apropos (name)

Searches for Maxima names which have *name* appearing anywhere
within them; *name* must be a string or symbol. Thus, `apropos (exp)` returns a list of all the flags and functions which have
`exp` as part of their names, such as `expand`, `exp`,
and `exponentialize`. So, if you can only remember part of the name
of a Maxima command or variable, you can use this command to find the
rest of the name. Similarly, you can type `apropos (tr_)` to find
a list of many of the switches relating to the translator, most of which
begin with `tr_`.


`apropos("")` returns a list with all Maxima names.


`apropos` returns the empty list `[]`, if no name is found.


Example:


Show all Maxima symbols which have `gamma` in the name:








```maxima
(%i1) apropos("gamma");
(%o1) [%gamma, Gamma, gamma_expand, gammalim, makegamma, 
prefer_gamma_incomplete, gamma, gamma-incomplete, gamma_incomplete, 
gamma_incomplete_generalized, gamma_incomplete_generalized_regularized, 
gamma_incomplete_lower, gamma_incomplete_regularized, log_gamma]


The same example, using the symbol gamma, rather than the string:

(%i2) apropos(gamma);
(%o2) [%gamma, Gamma, gamma_expand, gammalim, makegamma, 
prefer_gamma_incomplete, gamma, gamma-incomplete, gamma_incomplete, 
gamma_incomplete_generalized, gamma_incomplete_generalized_regularized, 
gamma_incomplete_lower, gamma_incomplete_regularized, log_gamma]


The number of symbols in the current Maxima session. This will vary.

(%i3) length(apropos(""));
(%o3)                                2338
```

### Variable: browser

This specifies the command to use to open an HTML file.  This is a
format string of the form `"browser_command"` that corresponds to a
valid command that when given a URL as argument, as in
`'browser_command URL'`, it will open up a browser to the given URL.


The default setting is `"start"` on Windows, `"xdg-open"` on
Linux/Unix, and `"open"` on MacOS, all of which will open the default Web
browser. In other systems, the default value of `browser` is set as
`"firefox"`, which will open the Firefox browser if it is
installed (if it is not installed, the user should change the value of
`browser` to some other valid browser).


You may replace the default value of `browser` with other valid browser
in your system, e.g. `"chrome"` or `"iexplore"`.


See also `output_format_for_help`, and `url_005fbase`.

See also: `output_format_for_help`, `url_base`.

### Function: demo (filename)

Evaluates Maxima expressions in *filename* and displays the results.
`demo` pauses after evaluating each expression and continues after the
user enters a carriage return.  (If running in Xmaxima, `demo` may need
to see a semicolon `;` followed by a carriage return.)


`demo` searches the list of directories `file_search_demo` to find
`filename`.  If the file has the suffix `dem`, the suffix may be
omitted.  See also `file_005fsearch`.


`demo` evaluates its argument.
`demo` returns the name of the demonstration file.


Example:



```maxima
(%i1) demo ("disol");

batching /home/wfs/maxima/share/simplification/disol.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i2)                      load("disol")

_
(%i3)           exp1 : a (e (g + f) + b (d + c))
(%o3)               a (e (g + f) + b (d + c))

_
(%i4)                disolate(exp1, a, b, e)
(%t4)                         d + c

(%t5)                         g + f

(%o5)                   a (%t5 e + %t4 b)

_
```

See also: `file_search_demo`, `file_search`.

### Function: describe (describe, string, describe, string, exact, describe, string, inexact)

`describe(string)` is equivalent to
`describe(string, exact)`.


`describe(string, exact)` finds an item with title equal
(case-insensitive) to *string*, if there is any such item.


`describe(string, inexact)` finds all documented items which contain
*string* in their titles.  If there is more than one such item, Maxima asks
the user to select an item or items to display.


At the interactive prompt, `? foo` (with a space between `?` and
`foo`) is equivalent to `describe("foo", exact)`, and `?? foo`
is equivalent to `describe("foo", inexact)`.


`describe("", inexact)` yields a list of all topics documented in the
on-line manual.


`describe` quotes its argument.  `describe` returns `true` if
some documentation is found, otherwise `false`.


To display the topics using a Web browser see `output_005fformat_005ffor_005fhelp`.
Also see `browser` and `url_base` to configure how to display
the HTML files.


See also `Documentation`.


Example:



```maxima
(%i1) ?? integ
 0: Functions and Variables for Elliptic Integrals
 1: Functions and Variables for Integration
 2: Introduction to Elliptic Functions and Integrals
 3: Introduction to Integration
 4: askinteger  (Functions and Variables for Simplification)
 5: integerp  (Functions and Variables for Miscellaneous Options)
 6: integer_partitions  (Functions and Variables for Sets)
 7: integrate  (Functions and Variables for Integration)
 8: integrate_use_rootsof  (Functions and Variables for
    Integration)
 9: integration_constant_counter  (Functions and Variables for
    Integration)
 10: nonnegintegerp  (Functions and Variables for linearalgebra)
Enter space-separated numbers, `all' or `none': 7 8

 -- Function: integrate (<expr>, <x>)
 -- Function: integrate (<expr>, <x>, <a>, <b>)
     Attempts to symbolically compute the integral of <expr> with
     respect to <x>.  `integrate (<expr>, <x>)' is an indefinite
     integral, while `integrate (<expr>, <x>, <a>, <b>)' is a
     definite integral, [...]
     
 -- Option variable: integrate_use_rootsof
     Default value: `false'

     When `integrate_use_rootsof' is `true' and the denominator of
     a rational function cannot be factored, `integrate' returns
     the integral in a form which is a sum over the roots (not yet
     known) of the denominator.
     [...]
```


In this example, items 7 and 8 were selected (output is shortened as indicated
by `[...]`).  All or none of the items could have been selected by entering
`all` or `none`, which can be abbreviated `a` or `n`,
respectively.

See also: `output_format_for_help`, `browser`, `url_base`, `Documentation`.

### Function: example (example, topic, example)

`example (topic)` displays some examples of *topic*, which is a
symbol or a string.  To get examples for operators like `if`, `do`,
or `lambda` the argument must be a string, e.g. `example ("do")`.
`example` is not case sensitive.  Most topics are function names.


`example ()` returns the list of all recognized topics.


The name of the file containing the examples is given by the global option 
variable `manual_demo`, which defaults to `"manual.demo"`.


`example` quotes its argument.  `example` returns `done` unless
no examples are found or there is no argument, in which case `example`
returns the list of all recognized topics.


Examples:







```maxima
(%i1) example(append);
(%i2) append([y+x,0,-3.2],[2.5e+20,x])
(%o2)             [y + x, 0, - 3.2, 2.5e+20, x]
(%o2)                         done

(%i3) example("lambda");
(%i4) lambda([x,y,z],x^2+y^2+z^2)
                                    2    2    2
(%o4)            lambda([x, y, z], x  + y  + z )
(%i5) %(1,2,a)
                              2
(%o5)                        a  + 5
(%i6) 1+2+a
(%o6)                         a + 3
(%o6)                         done
```

See also: `manual_demo`.

### Variable: manual_demo

Default value: `"manual.demo"`


`manual_demo` specifies the name of the file containing the examples for 
the function `example`.  See `example`.

See also: `example`.

### Variable: output_format_for_help

Default value: `text`


`output_format_for_help` controls how `describe` displays
help.


`output_format_for_help` can be set to one of the following
values:


**text** — Help is displayed as plain text sent to a terminal.  This is the default.
**html** — Help is displayed using a Web browser to display the HTML version of the
manual.
**frontend** — When Maxima is being run from a graphical interface (for example,
wxMaxima or xmaxima), lets that program decide how to display the help
results. If no frontend is running then an error is signaled.


Any other value is a error.



See also `browser`, and `url_005fbase`.

See also: `browser`, `url_base`.

### Variable: url_base

When displaying help using a browser, `url_base` defines the URL to
use.  It defaults to a `file://` path pointing to the directory
containing the html files for documentation; something such as,
`file:///home/user/.local/share/maxima/5.48.1/doc/html"`. However,
you could change the value of `url_base` to any valid URL that has
the HTML help files of the manual. For instance to see the official
manual in Maxima’s website instead of the local copy in your disk, set
`url_base` to `"https://maxima.sourceforge.io/docs/manual"`.


But keep in mind that the URL to where `url_base` points must have
exactly the same HTML files as in the Maxima version that you are using,
otherwise the help topics you are searching might not be found.


See also `output_005fformat_005ffor_005fhelp` and `browser`.

See also: `output_format_for_help`, `browser`.

