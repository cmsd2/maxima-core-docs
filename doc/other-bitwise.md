## bitwise

### Function: bit_and (int1, ...)

This function calculates a bitwise `and` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_and(i,i);
(%o2)                           i


(%i3) bit_and(i,i,i);
(%o3)                           i


(%i4) bit_and(1,3);
(%o4)                           1


(%i5) bit_and(-7,7);
(%o5)                           1
```


If it is known if one of the parameters to `bit_and` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_and(1,e);
(%o3)                           0


(%i4) bit_and(1,o);
(%o4)                           1
```

### Function: bit_length (int)

determines how many bits a variable needs to be long in order to store the
number `int`. This function only operates on positive numbers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_length(0);
(%o2)                           0


(%i3) bit_length(1);
(%o3)                           1


(%i4) bit_length(7);
(%o4)                           3


(%i5) bit_length(8);
(%o5)                           4
```

### Function: bit_lsh (int, nBits)

This function shifts all bits of the signed integer `int` to the left by
`nBits` bits. The width of the integer is extended by `nBits` for
this process. The result of `bit_lsh` therefore is `int * 2`.












```maxima
(%i1) load("bitwise")$

(%i2) bit_lsh(0,1);
(%o2)                           0


(%i3) bit_lsh(1,0);
(%o3)                           1


(%i4) bit_lsh(1,1);
(%o4)                           2


(%i5) bit_lsh(1,i);
(%o5)                     bit_lsh(1, i)


(%i6) bit_lsh(-3,1);
(%o6)                          - 6


(%i7) bit_lsh(-2,1);
(%o7)                          - 4
```

### Function: bit_not (int)

Inverts all bits of a signed integer. The result of this action reads
`-int - 1`.











```maxima
(%i1) load("bitwise")$

(%i2) bit_not(i);
(%o2)                      bit_not(i)


(%i3) bit_not(bit_not(i));
(%o3)                           i


(%i4) bit_not(3);
(%o4)                          - 4


(%i5) bit_not(100);
(%o5)                         - 101


(%i6) bit_not(-101);
(%o6)                          100
```

### Function: bit_onep (int, nBit)

determines if bits `nBit` is set in the signed integer `int`.












```maxima
(%i1) load("bitwise")$

(%i2) bit_onep(85,0);
(%o2)                         true


(%i3) bit_onep(85,1);
(%o3)                         false


(%i4) bit_onep(85,2);
(%o4)                         true


(%i5) bit_onep(85,3);
(%o5)                         false


(%i6) bit_onep(85,100);
(%o6)                         false


(%i7) bit_onep(i,100);
(%o7)                   bit_onep(i, 100)
```


For signed numbers the sign bit is interpreted to be more than `nBit` to the
left of the leftmost bit of `int` that reads `1`.










```maxima
(%i1) load("bitwise")$

(%i2) bit_onep(-2,0);
(%o2)                         false


(%i3) bit_onep(-2,1);
(%o3)                         true


(%i4) bit_onep(-2,2);
(%o4)                         true


(%i5) bit_onep(-2,3);
(%o5)                         true


(%i6) bit_onep(-2,4);
(%o6)                         true
```



If it is known if the number to be tested is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_onep(e,0);
(%o3)                         false


(%i4) bit_onep(o,0);
(%o4)                         true
```

### Function: bit_or (int1, ...)

This function calculates a bitwise `or` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_or(i,i);
(%o2)                           i


(%i3) bit_or(i,i,i);
(%o3)                           i


(%i4) bit_or(1,3);
(%o4)                           3


(%i5) bit_or(-7,7);
(%o5)                          - 1
```


If it is known if one of the parameters to `bit_or` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_or(1,e);
(%o3)                         e + 1


(%i4) bit_or(1,o);
(%o4)                           o
```

### Function: bit_rsh (int, nBits)

This function shifts all bits of the signed integer `int` to the right by
`nBits` bits. The width of the integer is reduced by `nBits` for
this process.













```maxima
(%i1) load("bitwise")$

(%i2) bit_rsh(0,1);
(%o2)                           0


(%i3) bit_rsh(2,0);
(%o3)                           2


(%i4) bit_rsh(2,1);
(%o4)                           1


(%i5) bit_rsh(2,2);
(%o5)                           0


(%i6) bit_rsh(-3,1);
(%o6)                          - 2


(%i7) bit_rsh(-2,1);
(%o7)                          - 1


(%i8) bit_rsh(-2,2);
(%o8)                          - 1
```

### Function: bit_xor (int1, ...)

This function calculates a bitwise `or` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_xor(i,i);
(%o2)                           0


(%i3) bit_xor(i,i,i);
(%o3)                           i


(%i4) bit_xor(1,3);
(%o4)                           2


(%i5) bit_xor(-7,7);
(%o5)                          - 2
```


If it is known if one of the parameters to `bit_xor` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_xor(1,e);
(%o3)                         e + 1


(%i4) bit_xor(1,o);
(%o4)                         o - 1
```

