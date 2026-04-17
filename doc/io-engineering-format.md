## engineering-format

<!-- category: IO -->
<!-- keywords: engineering_format_floats -->
<!-- signatures: engineering_format_floats -->
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

<!-- category: IO -->
<!-- keywords: engineering_format_max -->
<!-- signatures: engineering_format_max -->
### Variable: engineering_format_max

Default value: `0.0` 


The maximum absolute value that isn’t automatically converted to the engineering format.
See also `engineering_format_min` and `engineering_005fformat_005ffloats`.

See also: `engineering_format_min`, `engineering_format_floats`.

<!-- category: IO -->
<!-- keywords: engineering_format_min -->
<!-- signatures: engineering_format_min -->
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

