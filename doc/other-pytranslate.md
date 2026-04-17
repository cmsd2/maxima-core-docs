## pytranslate

<!-- category: Other -->
<!-- keywords: pytranslate -->
<!-- signatures: pytranslate(expr, [print-ir]) -->
### Function: pytranslate (expr, [print-ir])

Translates the expression *expr* to equivalent python3 statements. Output is printed in the stdout.


Example:






```maxima
(%i1) load ("pytranslate")$

(%i2) pytranslate('(for i:8 step -1 unless i<3 do (print(i))));
(%o2) 
v["i"] = 8
while not((v["i"] < 3)):
    m["print"](v["i"])
    v["i"] = (v["i"] + -1)
del v["i"]
```


*expr* is evaluated, and the return value is used for translation. Hence, for statements like assignment, it might be useful to quote the statement:







```maxima
(%i1) load ("pytranslate")$

(%i2) pytranslate(x:20);
(%o2) 
20


(%i3) pytranslate('(x:20));
(%o3) 
v["x"] = 20
```


Passing the optional parameter (*print-ir*) to `pytranslate` as t, will print the internal IR representation of `expr` and return the translated python3 code.








```maxima
(%i1) load("pytranslate");
(%o1) pytranslate


(%i2) pytranslate('(plot3d(lambda([x, y], x^2+y^(-1)), [x, 1, 10],
                   [y, 1, 10])), t);
(body
 (funcall (element-array "m" (string "plot3d"))
          (lambda
              ((symbol "x") (symbol "y")
               (op-no-bracket
                =
                (symbol "v")
                (funcall (symbol "stack") (dictionary) (symbol "v"))))
            (op +
                (funcall (element-array (symbol "m") (string "pow"))
                         (symbol "x") (num 2 0))
                (funcall (element-array (symbol "m") (string "pow"))
                         (symbol "y") (unary-op - (num 1 0)))))
          (struct-list (string "x") (num 1 0) (num 10 0))
          (struct-list (string "y") (num 1 0) (num 10 0))))
(%o2) 
m["plot3d"](lambda x, y, v = Stack({}, v): (m["pow"](x, 2) + m["\
pow"](y, (-1))), ["x", 1, 10], ["y", 1, 10])
```

<!-- category: Other -->
<!-- keywords: show_form -->
<!-- signatures: show_form(expr) -->
### Function: show_form (expr)

Displays the internal maxima form of `expr`


```maxima
(%i4) show_form(a^b);
((mexpt) $a $b) 
(%o4) a^b
```

