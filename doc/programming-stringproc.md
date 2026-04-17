## stringproc

<!-- category: Programming -->
<!-- keywords: regex_compile -->
<!-- signatures: regex_compile(pattern) -->
### Function: regex_compile (pattern)

Compile regex string in *pattern* to an internal form that is
easier for the regex engine to process.  This is not required,
however.  All the regex functions accept this compiled regex or a
string.  If the pattern is used many times, compiling the pattern
will speed up matching.






```maxima
(%i1) regex_compile("c.r");
(%o1)         Structure [COMPILED-REGEX for "c.r"]
```

<!-- category: Programming -->
<!-- keywords: regex_match -->
<!-- signatures: regex_match(regex, str), regex_match(regex, str, start), regex_match(regex, str, start, end) -->
### Function: regex_match (regex, str)

`regex_match` is very similar to `regex_match_pos` except
that it returns the matching substrings instead of the indices of the
match.  If no match is found, returns `false`.







```maxima
(%i1) regex_match("ne{2}dle", "hay needle stack");
(%o1)                       [needle]


(%i2) regex_match("ne{2}dle", "hay needle stack", 10);
(%o2)                         false
```


Here is examples using POSIX character classes.  `[:alpha:]`
matches any letter.  The pattern matches any letter or underscore:







```maxima
(%i1) regex_match("[[:alpha:]_]", "--x--");
(%o1)                          [x]


(%i2) regex_match("[[:alpha:]_]", "--_--");
(%o2)                          [_]


(%i3) regex_match("[[:alpha:]_]", "--:--");
(%o3)                         false
```


`sregex` supports *clusters* (see
[https://ds26gte.github.io/pregexp/index.html#TAG:__tex2page_toc_TAG:__tex2page_sec_3.4pregexp clusters]()) which are subpatterns denoted
by being enclosed within parentheses.  These cause the matcher to
return the submatch along with the overall match.


Here we are looking for any number of letters followed by a space, any
number of digits, a comma and space, then any number of digits.





```maxima
(%i1) regex_match("([a-z]+) ([0-9]+), ([0-9]+)", "jan 1, 1970");
(%o1)              [jan 1, 1970, jan, 1, 1970]
```

The result is a list of strings.  The first element is the full match.
The second matches `"([a-z]+)"`, which is a cluster of any number
of letters.  Hence, `"jan"` matches this cluster.  Likewise for
the other clusters.


A more complicated example illustrates how a subpattern fails to
match, but the overall pattern matches.  In this case, `false`
represents to failed match.


The regex pattern matches “month year” or “month day, year”.  The
subpattern matches the day, if present.







```maxima
(%i1) date_re : regex_compile("([a-z]+) +([0-9]+,)? *([0-9]+)");
(%o1) 
  Structure [COMPILED-REGEX for "([a-z]+) +([0-9]+,)? *([0-9]+)"]


(%i2) regex_match(date_re, "jan 1, 1970");
(%o2)             [jan 1, 1970, jan, 1,, 1970]


(%i3) regex_match(date_re, "jan 1970");
(%o3)             [jan 1970, jan, false, 1970]
```


You can also do case-insensitive matches by using a *cloister*
(see
[https://ds26gte.github.io/pregexp/index.html#TAG:__tex2page_toc_TAG:__tex2page_sec_3.4.3pregexp cloisters]())
with the `i` modifier:







```maxima
(%i1) regex_match("hearth", "HeartH");
(%o1)                         false


(%i2) regex_match("(?i:hearth)", "HeartH");
(%o2)                       [HeartH]
```


Alternate subpatterns can be separated by `|`.





```maxima
(%i1) regex_match("f(ee|i|o|um)", "a small, final fee");
(%o1)                        [fi, i]
```

The first element is the full match `"fi"`; the second shows
that we matched `"i"` for the cluster.

<!-- category: Programming -->
<!-- keywords: regex_match_pos -->
<!-- signatures: regex_match_pos(regex, str), regex_match_pos(regex, str, start), regex_match_pos(regex, str, start, end) -->
### Function: regex_match_pos (regex, str)

Return a list consisting of a list of the start and end positions of
*str* where the first match of *regex* occurred.  If no match
is found, returns `false`.


If a third argument, *start*, is supplied, it is the starting index
of the text string *str*.  The fourth argument, *end*, is the
ending index of text string *str*.










```maxima
(%i1) str : "his hay needle stack -- my hay needle stack -- her hay needle stack"$
(%i2) regex : regex_compile("ne{2}dle")$

(%i3) regex_match_pos(regex, str);
(%o3)                       [[9, 15]]


(%i4) regex_match_pos("ne{2}dle", str);
(%o4)                       [[9, 15]]


(%i5) regex_match_pos("ne{2}dle", str, 25, 44);
(%o5)                      [[32, 38]]
```


Here is an example where `regex_match_pos` returns a list of more
than one element:







```maxima
(%i1) str : "jan 1, 1970";
(%o1)                      jan 1, 1970


(%i2) match: regex_match_pos("([a-z]+) ([0-9]+), ([0-9]+)", "jan 1, 1970");
(%o2)          [[1, 12], [1, 4], [5, 6], [8, 12]]


(%i3) map(lambda([posn], substring(str, posn[1], posn[2])), match);
(%o3)              [jan 1, 1970, jan, 1, 1970]
```


The first element is for the full match.  Each subsequent element of
the list is the substring that matches the *cluster* enclosed in
parenthesis in the given regular expression.

<!-- category: Programming -->
<!-- keywords: regex_split -->
<!-- signatures: regex_split(regex, str) -->
### Function: regex_split (regex, str)

Returns a list of strings where *str* has been split into
substrings where the *regex* identifies the delimiters to use for
separating the substrings.






```maxima
(%i1) regex_split("[,;]+", "split,pea;;;soup");
(%o1)                  [split, pea, soup]
```

<!-- category: Programming -->
<!-- keywords: regex_subst -->
<!-- signatures: regex_subst(replacement, pattern, str) -->
### Function: regex_subst (replacement, pattern, str)

Returns a string where every occurrence of *pattern* has been
replaced by *replacement* in the string *str*.






```maxima
(%i1) regex_subst("ty", "t.\\b", "liberte egalite fraternite");
(%o1)              liberty egality fraternity
```

<!-- category: Programming -->
<!-- keywords: regex_subst_first -->
<!-- signatures: regex_subst_first(replacement, pattern, str) -->
### Function: regex_subst_first (replacement, pattern, str)

Returns a string where the first occurrence of *pattern* in
*str* with *replacement*.






```maxima
(%i1) regex_subst_first("ty", "t.", "liberte egalite fraternite");
(%o1)              liberty egalite fraternite
```


This example shows how to use back references.  The replacement
specifies that the first submatch is used as the replacement text.






```maxima
(%i1) regex_match("_(.+?)_", "the _nina_, the _pinta_, and the _santa maria_");
(%o1)                    [_nina_, nina]


(%i2) regex_subst_first("*\\1*", "_(.+?)_", "the _nina_, the _pinta_, and the _santa maria_");
(%o2)    the *nina*, the _pinta_, and the _santa maria_
```

<!-- category: Programming -->
<!-- keywords: string_to_regex -->
<!-- signatures: string_to_regex(str) -->
### Function: string_to_regex (str)

Returns a regex string where any special reqex characters in *str*
are quoted to remove the specialness of the character.









```maxima
(%i1) re : string_to_regex(". :");
(%o1)                         \. :


(%i2) regex_match(re, "z :");
(%o2)                         false


(%i3) regex_match(re, ". :");
(%o3)                         [. :]


(%i4) regex_match(". :", "z :");
(%o4)                         [z :]
```


In this example, the regex will only match a substring consisting of a
period, followed by a space and a colon.  Without the quoting, the
`"."` would match any single character.

