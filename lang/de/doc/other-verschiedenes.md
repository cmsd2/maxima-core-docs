## Verschiedenes

<!-- category: Other -->
<!-- keywords: askexp -->
<!-- signatures: askexp -->
### Variable: askexp

Wenn `asksign` aufgerufen wird, enthalt `askexp` den Ausdruck, der 
von `asksign` getestet wird.





Es war einmal moglich, die Variable `askexp` nach einer Unterbrechnung 
mit Control-A zu inspezieren.

<!-- category: Other -->
<!-- keywords: gensym -->
<!-- signatures: gensym(), gensym(x) -->
### Function: gensym ()

`gensym()` creates and returns a fresh symbol.


The name of the new-symbol is the concatenation of a prefix, which defaults to 
"g", and a suffix, which is the decimal representation of a number that defaults
to the value of a Lisp internal counter.


If *x* is supplied, and is a string, then that string is used as a prefix 
instead of "g" for this call to gensym only.


If *x* is supplied, and is an integer, then that integer, instead of the 
value of the internal Lisp integer, is used as the suffix for this call to 
gensym only.


If and only if no explicit suffix is supplied, the Lisp internal integer is 
incremented after it is used.


Examples:



```maxima
(%i1) gensym();
(%o1)                         g887
(%i2) gensym("new");
(%o2)                        new888
(%i3) gensym(123);
(%o3)                         g123
```

<!-- category: Other -->
<!-- keywords: packagefile -->
<!-- signatures: packagefile -->
### Variable: packagefile

Default value: `false`


Package designers who use `save` or `translate` to create packages
(files) for others to use may want to set `packagefile: true` to prevent
information from being added to Maxima’s information-lists (e.g.
`values`, `functions`) except where necessary when the file is
loaded in.  In this way, the contents of the package will not get in the user’s
way when he adds his own data.  Note that this will not solve the problem of
possible name conflicts.  Also note that the flag simply affects what is output
to the package file.  Setting the flag to `true` is also useful for
creating Maxima init files.

See also: `save`, `translate`, `values`, `functions`.

<!-- category: Other -->
<!-- keywords: remvalue -->
<!-- signatures: remvalue(name_1, ..., name_n), remvalue(all) -->
### Function: remvalue (name_1, ..., name_n)

Entfernt die Werte von nutzerdefinierten Variablen *name_1*, ..., 
*name_n*.  Die Variablen konnen indiziert sein.
`remvalue(all)` entfernt die Werte aller Variablen, die in der 
Informationsliste `values` enthalten sind.


Siehe auch `values`.

See also: `values`.

<!-- category: Other -->
<!-- keywords: rncombine -->
<!-- signatures: rncombine(expr) -->
### Function: rncombine (expr)

Transformiert den Ausdruck *expr* so, dass alle Terme mit identischem Nenner
oder Nennern, die sich nur um einen numerischen Faktor voneinander 
unterscheiden, uber einen Nenner zusammengefasst werden. Die Funktion
`combine` fasst ebenfalls Ausdrucke uber einen Nenner zusammen, 
betrachtet aber Nenner als verschieden, die sich um einen Zahlenfaktor 
voneinander unterscheiden.


Die Funktion wird mit dem Kommando `rncomb` geladen.

<!-- category: Other -->
<!-- keywords: setup_autoload -->
<!-- signatures: setup_autoload(filename, function_1, ..., function_n) -->
### Function: setup_autoload (filename, function_1, ..., function_n)

Die Funktionen *function_1*, ..., *function_n* erhalten die 
Eigenschaft, dass die Datei *filename* automatisch geladen wird, wenn die 
Funktion zum ersten Mal genutzt werden soll.  *filename* wird mit der 
Funktion `load` geladen und enthalt ublicherweise den Code fur die 
Definition der zu ladenden Funktion.


`setup_autoload` funktioniert nicht fur Array-Funktionen.
`setup_autoload` wertet die Argumente nicht aus.


Beispiele:










```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma function ultraspherical
Warning - you are redefining the Macsyma function legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);

                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

