## Data Types and Structures

<!-- category: NumberTheory -->
<!-- keywords: bfloat -->
<!-- signatures: bfloat(expr) -->
### Function: bfloat (expr)

`bfloat` replaces integers, rationals, floating point numbers, and some symbolic constants
in *expr* with bigfloat (variable-precision floating point) numbers.


The constants `%e`, `%gamma`, `%phi`, and `%pi`
are replaced by a numerical approximation.
However, `%e` in `%e^x` is not replaced by a numeric value
unless `bfloat(x)` is a number.


`bfloat` also causes numerical evaluation of some built-in functions,
namely trigonometric functions, exponential functions, `abs`, and `log`.



The number of significant digits in the resulting bigfloats is specified by the
global variable `fpprec`.
Bigfloats already present in *expr* are replaced with values which have
precision specified by the current value of `fpprec`.


When `float2bf` is `false`, a warning message is printed when
a floating point number is replaced by a bigfloat number with less precision.


Examples:


`bfloat` replaces integers, rationals, floating point numbers, and some symbolic constants
in *expr* with bigfloat numbers.








```maxima
(%i1) bfloat([123, 17/29, 1.75]);
(%o1)        [1.23b2, 5.862068965517241b-1, 1.75b0]
(%i2) bfloat([%e, %gamma, %phi, %pi]);
(%o2) [2.718281828459045b0, 5.772156649015329b-1, 
                        1.618033988749895b0, 3.141592653589793b0]
(%i3) bfloat((f(123) + g(h(17/29)))/(x + %gamma));
         1.0b0 (g(h(5.862068965517241b-1)) + f(1.23b2))
(%o3)    ----------------------------------------------
                    x + 5.772156649015329b-1
```


`bfloat` also causes numerical evaluation of some built-in functions.









```maxima
(%i1) bfloat(sin(17/29));
(%o1)                 5.532051841609784b-1
(%i2) bfloat(exp(%pi));
(%o2)                  2.314069263277927b1
(%i3) bfloat(abs(-%gamma));
(%o3)                 5.772156649015329b-1
(%i4) bfloat(log(%phi));
(%o4)                 4.812118250596035b-1
```

See also: `fpprec`, `float2bf`.

<!-- category: NumberTheory -->
<!-- keywords: bfloatp -->
<!-- signatures: bfloatp(expr) -->
### Function: bfloatp (expr)

Returns `true` if *expr* is a bigfloat number, otherwise `false`.

<!-- category: NumberTheory -->
<!-- keywords: bftorat -->
<!-- signatures: bftorat -->
### Variable: bftorat

Default value: `false`


`bftorat` controls the conversion of bfloats to rational numbers.  When
`bftorat` is `false`, `ratepsilon` will be used to control the
conversion (this results in relatively small rational numbers).  When
`bftorat` is `true`, the rational number generated will accurately
represent the bfloat.


Note: `bftorat` has no effect on the transformation to rational numbers
with the function `rationalize`.


Example:








```maxima
(%i1) ratepsilon:1e-4;
(%o1)                         1.0e-4
(%i2) rat(bfloat(11111/111111)), bftorat:false;
`rat' replaced 9.99990999991B-2 by 1/10 = 1.0B-1
                               1
(%o2)/R/                       --
                               10
(%i3) rat(bfloat(11111/111111)), bftorat:true;
`rat' replaced 9.99990999991B-2 by 11111/111111 = 9.99990999991B-2
                             11111
(%o3)/R/                     ------
                             111111
```

See also: `ratepsilon`, `rationalize`.

<!-- category: NumberTheory -->
<!-- keywords: bftrunc -->
<!-- signatures: bftrunc -->
### Variable: bftrunc

Default value: `true`


`bftrunc` causes trailing zeroes in non-zero bigfloat numbers not to be
displayed.  Thus, if `bftrunc` is `false`, `bfloat (1)`
displays as `1.000000000000000B0`.  Otherwise, this is displayed as
`1.0B0`.

<!-- category: NumberTheory -->
<!-- keywords: bigfloat_bits -->
<!-- signatures: bigfloat_bits() -->
### Function: bigfloat_bits ()

Returns the number of bits of precision in a bigfloat number.  This
value depends, of course, on the value of `fpprec`. 









```maxima
(%i1) fpprec:16;
(%o1)                                 16
(%i2) bigfloat_bits();
(%o2)                                 56
(%i3) fpprec:32;
(%o3)                                 32
(%i4) bigfloat_bits();
(%o4)                                 109
```

See also: `fpprec`.

<!-- category: NumberTheory -->
<!-- keywords: bigfloat_eps -->
<!-- signatures: bigfloat_eps() -->
### Function: bigfloat_eps ()

Returns the smallest bigfloat value, `eps`, such that
`1+eps` is not equal to 1.  The value depends on `fpprec`,
of course.









```maxima
(%i1) fpprec:16;
(%o1)                                 16
(%i2) bigfloat_eps();
(%o2)                        1.387778780781446b-17
(%i3) fpprec:32;
(%o3)                                 32
(%i4) bigfloat_eps();
(%o4)                1.5407439555097886824447823540679b-33
```

See also: `fpprec`.

<!-- category: NumberTheory -->
<!-- keywords: decode_float -->
<!-- signatures: decode_float(f) -->
### Function: decode_float (f)

`decode_float` takes a float *f* and returns a list of three
values that characterizes *f*, which must be either a `float`
or `bfloat`.  The first value has the same type as *f*, but
is a number in the range `[1, 2)`.  The second value is an
exponent.  The third value is a float of the same type as *f* and
has the value of 1 if *f* is greater than or equal to 0;
otherwise, -1.


If the returned list is `[mantissa, expo, sign]`, then
`scale_float(mantissa, exp)*sign` is identical to *f*.



```maxima
(%i1) decode_float(4e0);
(%o1)                            [1.0, 2, 1.0]
(%i2) decode_float(4b0);
(%o2)                          [1.0b0, 2, 1.0b0]
(%i3) decode_float(%pi);

decode_float is only defined for floats and bfloats: %pi
 -- an error. To debug this try: debugmode(true);
(%i4) decode_float(float(%pi));
(%o4)                     [1.570796326794897, 1, 1.0]
(%i5) decode_float(1.1e-5);
(%o5)                        [1.441792, - 17, 1.0]
(%i6) %[1]*2^%[2];
(%o6)                               1.1e-5
```


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htmdecode_float]().  However we return a signficand in the range
`[1,2)` instead of `[0.5, 1)`.  The former matches
IEEE-754.  Of course, this is extended to support bfloats.

<!-- category: NumberTheory -->
<!-- keywords: evenp -->
<!-- signatures: evenp(expr) -->
### Function: evenp (expr)

Returns `true` if *expr* is a literal even integer, otherwise
`false`.


`evenp` returns `false` if *expr* is a symbol, even if *expr*
is declared `even`.

<!-- category: NumberTheory -->
<!-- keywords: float -->
<!-- signatures: float(expr) -->
### Function: float (expr)

Converts integers, rational numbers and bigfloats in *expr* to floating
point numbers.  It is also an `evflag`, `float` causes
non-integral rational numbers and bigfloat numbers to be converted to floating
point.

See also: `evflag`.

<!-- category: NumberTheory -->
<!-- keywords: float2bf -->
<!-- signatures: float2bf -->
### Variable: float2bf

Default value: `true`

 

When `float2bf` is `false`, a warning message is printed when
a floating point number is replaced by a bigfloat number with less precision.

See also: `float2bf`.

<!-- category: NumberTheory -->
<!-- keywords: float_bits -->
<!-- signatures: float_bits() -->
### Function: float_bits ()

Returns the number of bits of precision of a floating-point number.

<!-- category: NumberTheory -->
<!-- keywords: float_eps -->
<!-- signatures: float_eps() -->
### Function: float_eps ()

Returns the smallest floating-point value, `eps`, such that
`1+eps` is not equal to 1.

<!-- category: NumberTheory -->
<!-- keywords: float_infinity_p -->
<!-- signatures: float_infinity_p(x) -->
### Function: float_infinity_p (x)

Returns `true` if *x* is floating point positive infinity or floating point negative infinity,
and returns `false` for all other arguments;
arguments which are not numbers are allowed,
and `float_infinity_p` returns `false` for all such arguments.


Positive and negative floating point infinity may be distinguished by `sign`,
which returns `pos` for positive infinity and `neg` for negative infinity.


`float_infinity_p` is defined whether or not the Lisp implementation supports float infinity.
When float infinity does not exist in the Lisp implementation’s number system,
`float_infinity_p` returns `false` for all arguments.


A Lisp implementation may support more than one precision of floating point numbers.
`float_infinity_p` only recognizes double precision floating point infinity,
and not any other precision.

<!-- category: NumberTheory -->
<!-- keywords: float_nan_p -->
<!-- signatures: float_nan_p(x) -->
### Function: float_nan_p (x)

Returns `true` if *x* is a floating point not-a-number (NaN) value,
and returns `false` for all other arguments;
arguments which are not numbers are allowed,
and `float_nan_p` returns `false` for all such arguments.


`float_nan_p` is defined whether or not the Lisp implementation supports floating point not-a-number values.
When floating point not-a-number does not exist in the Lisp implementation’s number system,
`float_nan_p` returns `false` for all arguments.


A Lisp implementation may support more than one precision of floating point numbers.
`float_nan_p` only recognizes double precision floating point not-a-number,
and not any other precision.

<!-- category: NumberTheory -->
<!-- keywords: float_precision -->
<!-- signatures: float_precision(f) -->
### Function: float_precision (f)

Returns the number of bits of precision of a floating-point number,
which can be either a float or bigfloat.  This is basically the number
of bits used to represent the mantissa of a floating-point number.
For floats, this is 53 (for IEEE double-floats), but can be less when
denormal numbers occur.  For bigfloats, this is equal to
`fpprec`, when converted from digits to bits.

See also: `fpprec`.

<!-- category: NumberTheory -->
<!-- keywords: float_sign -->
<!-- signatures: float_sign(f) -->
### Function: float_sign (f)

Returns the sign of *f*.  It is $+1$ or $-1$ of the same
type as *f*.  It is an error if *f* is not a float or
bigfloat.  Note that some lisps do not support signed zeros for
floating-point numbers.  Bigfloats do not support signed zeroes.  The
examples below assume signed zeroes are supported.


```maxima
(%i1) float_sign(1.0);
(%o1)                                 1.0
(%i2) float_sign(-5.0);
(%o2)                                - 1.0
(%i3) float_sign(-0.0);
(%o3)                                - 1.0
(%i4) float_sign(1b0);
(%o4)                                1.0b0
(%i5) float_sign(-5b0);
(%o5)                               - 1.0b0
(%o6) float_sign(-0b0);
(%o6)                                1.0b0
(%i7) float_sign(%pi);

float_sign is only defined for floats and bfloats: %pi
 -- an error. To debug this try: debugmode(true);
```

<!-- category: NumberTheory -->
<!-- keywords: floatnump -->
<!-- signatures: floatnump(expr) -->
### Function: floatnump (expr)

Returns `true` if *expr* is a floating point number, otherwise
`false`.

<!-- category: NumberTheory -->
<!-- keywords: fpprec -->
<!-- signatures: fpprec -->
### Variable: fpprec

Default value: 16


`fpprec` is the number of significant digits for arithmetic on bigfloat
numbers.  `fpprec` does not affect computations on ordinary floating point
numbers.


See also `bfloat` and `fpprintprec`.

See also: `bfloat`, `fpprintprec`.

<!-- category: NumberTheory -->
<!-- keywords: fpprintprec -->
<!-- signatures: fpprintprec -->
### Variable: fpprintprec

Default value: 0


`fpprintprec` is the number of digits to print when printing an ordinary
float or bigfloat number.


For ordinary floating point numbers,
when `fpprintprec` has a value between 2 and 16 (inclusive),
the number of digits printed is equal to `fpprintprec`.
Otherwise, `fpprintprec` is 0, or greater than 16,
and the number is printed "readably":
that is, it is printed with sufficient digits to exactly reconstruct the number on input.


For bigfloat numbers,
when `fpprintprec` has a value between 2 and `fpprec` (inclusive),
the number of digits printed is equal to `fpprintprec`.
Otherwise, `fpprintprec` is 0, or greater than `fpprec`,
and the number of digits printed is equal to `fpprec`.


For both ordinary floats and bigfloats,
trailing zero digits are suppressed.
The actual number of digits printed is less than `fpprintprec`
if there are trailing zero digits.


`fpprintprec` cannot be 1.

<!-- category: NumberTheory -->
<!-- keywords: integer_decode_float -->
<!-- signatures: integer_decode_float(f) -->
### Function: integer_decode_float (f)

`integer_decode_float` takes a float *f* and returns a list of three
values that characterizes *f*, which must be either a `float`
or `bfloat`.  The first value is an integer.  The second value is an
exponent.  The third value is 1 if *f* is positive or zero;
otherwise, -1.


If the returned list is `[mantissa, expo, sign]`, then
`scale_float(fl(mantissa), expo)*sign` is identical to *f*.
Here, `fl` is either `float` or `bfloat` depending on
whether *f* is a `float` or a `bfloat`.



```maxima
(%i1) integer_decode_float(4.0);
(%o1)                     [4503599627370496, - 50, 1]
(%i2) integer_decode_float(4b0);
(%o2)                    [36028797018963968, - 53, 1]
(%i3) scale_float(float(%o1[1]), %o1[2]);
(%o3)                                 4.0
(%i4) scale_float(bfloat(%o2[1]), %o2[2]);
(%o4)                                4.0b0
(%i5) integer_decode_float(4);

decode_float is only defined for floats and bfloats: 4
 -- an error. To debug this try: debugmode(true);
(%i6) integer_decode_float(1e-7);
(%o6)                     [7555786372591432, - 76, 1]
(%i7) integer_decode_float(1b-7);
(%o7)                    [60446290980731459, - 79, 1]
(%i8) scale_float(float(%o6[1]), %o6[2]);
(%o8)                               1.0e-7
```


For lisps that support denormal numbers, we have the following results.


```maxima
(%i1) integer_decode_float(least_positive_float);
(%o1)                           [1, - 1074, 1]
(%i2) integer_decode_float(100*least_positive_float);
(%o2)                          [100, - 1074, 1]
(%i3) integer_decode_float(least_positive_normalized_float);
(%o3)                    [4503599627370496, - 1074, 1]
```

The number of bits in the integer part decreases as the denormal
number decreases.  Bfloat numbers do not have denormals because the
exponent is not bounded.


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htminteger_decode_float]().  However, the integer part can vary depending
on the Lisp implementation; we return the same value, independent of
the Lisp implementation.  Of course, this is extended to support bfloats.

<!-- category: NumberTheory -->
<!-- keywords: integerp -->
<!-- signatures: integerp(expr) -->
### Function: integerp (expr)

Returns `true` if *expr* is a literal numeric integer, otherwise
`false`.


`integerp` returns `false` if *expr* is a symbol, even if *expr*
is declared `integer`.


Examples:














```maxima
(%i1) integerp (0);
(%o1)                         true
(%i2) integerp (1);
(%o2)                         true
(%i3) integerp (-17);
(%o3)                         true
(%i4) integerp (0.0);
(%o4)                         false
(%i5) integerp (1.0);
(%o5)                         false
(%i6) integerp (%pi);
(%o6)                         false
(%i7) integerp (n);
(%o7)                         false
(%i8) declare (n, integer);
(%o8)                         done
(%i9) integerp (n);
(%o9)                         false
```

<!-- category: NumberTheory -->
<!-- keywords: is_power_of_two -->
<!-- signatures: is_power_of_two(n) -->
### Function: is_power_of_two (n)

`is_power_to_two` returns `true` if *n* is a power of
two and `false` otherwise.  *n* may be an integer, a
rational, a float, or a big float.


Some examples:


```maxima
(%i1) is_power_of_two(0);
(%o1)                                false
(%i2) is_power_of_two(4);
(%o2)                                true
(%i3) is_power_of_two(355/113);
(%o3)                                false
(%i4) is_power_of_two(1/32);
(%o4)                                true
(%i5) is_power_of_two(1048576);
(%o5)                                true
(%i6) is_power_of_two(1048575);
(%o6)                                false
(%i7) is_power_of_two(0.0);
(%o7)                                false
(%i8) is_power_of_two(1048576.0);
(%o8)                                true
(%i9) is_power_of_two(1048575.0);
(%o9)                                false
(%i10) is_power_of_two(1/256.0);
(%o10)                               true
(%i11) is_power_of_two(0b0);
(%o11)                               false
(%i12) is_power_of_two(1048576b0);
(%o12)                               true
(%i13) is_power_of_two(1048575b0);
(%o13)                               false
(%i14) is_power_of_two(1/256b0);
(%o14)                               true
```

<!-- category: NumberTheory -->
<!-- keywords: m1pbranch -->
<!-- signatures: m1pbranch -->
### Variable: m1pbranch

Default value: `false`


`m1pbranch` is the principal branch for `-1` to a power.
Quantities such as `(-1)^(1/3)` (that is, an "odd" rational exponent) and 
`(-1)^(1/4)` (that is, an "even" rational exponent) are handled as follows:




```maxima
domain:real
                            
(-1)^(1/3):      -1         
(-1)^(1/4):   (-1)^(1/4)   

             domain:complex              
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```

<!-- category: NumberTheory -->
<!-- keywords: nonnegintegerp -->
<!-- signatures: nonnegintegerp(n) -->
### Function: nonnegintegerp (n)

Return `true` if and only if `n >= 0` and *n* is an integer.

<!-- category: NumberTheory -->
<!-- keywords: numberp -->
<!-- signatures: numberp(expr) -->
### Function: numberp (expr)

Returns `true` if *expr* is a literal integer, rational number, 
floating point number, or bigfloat, otherwise `false`.


`numberp` returns `false` if *expr* is a symbol, even if *expr*
is a symbolic number such as `%pi` or `%i`, or declared to be
`even`, `odd`, `integer`, `rational`, `irrational`,
`real`, `imaginary`, or `complex`.


Examples:













```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare (a, even, b, odd, c, integer, d, rational,
     e, irrational, f, real, g, imaginary, h, complex);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e, f, g, h]);
(%o7) [false, false, false, false, false, false, false, false]
```

<!-- category: NumberTheory -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

`numer` causes some mathematical functions (including exponentiation)
with numerical arguments to be evaluated in floating point.  It causes
variables in `expr` which have been given numerals to be replaced by
their values.  It also sets the `float` switch on.


See also `_0025enumer`.


Examples:







```maxima
(%i1) [sqrt(2), sin(1), 1/(1+sqrt(3))];
                                        1
(%o1)            [sqrt(2), sin(1), -----------]
                                   sqrt(3) + 1


(%i2) [sqrt(2), sin(1), 1/(1+sqrt(3))],numer;
(%o2) [1.414213562373095, 0.8414709848078965, 0.3660254037844387]
```

See also: `float`, `%enumer`.

<!-- category: NumberTheory -->
<!-- keywords: numer_pbranch -->
<!-- signatures: numer_pbranch -->
### Variable: numer_pbranch

Default value: `false`


The option variable `numer_pbranch` controls the numerical evaluation of 
the power of a negative integer, rational, or floating point number.  When
`numer_pbranch` is `true` and the exponent is a floating point number
or the option variable `numer` is `true` too, Maxima evaluates
the numerical result using the principal branch.  Otherwise a simplified, but
not an evaluated result is returned.


Examples:










```maxima
(%i1) (-2)^0.75;
                                 0.75
(%o1)                       (- 2)


(%i2) (-2)^0.75,numer_pbranch:true;
(%o2)       1.189207115002721 %i - 1.189207115002721


(%i3) (-2)^(3/4);
                               3/4  3/4
(%o3)                     (- 1)    2


(%i4) (-2)^(3/4),numer;
                                          0.75
(%o4)              1.681792830507429 (- 1)


(%i5) (-2)^(3/4),numer,numer_pbranch:true;
(%o5)       1.189207115002721 %i - 1.189207115002721
```

See also: `numer`.

<!-- category: NumberTheory -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, expr_1, ..., var_n, expr_n) -->
### Function: numerval (x_1, expr_1, ..., var_n, expr_n)

Declares the variables `x_1`, ..., *x_n* to have
numeric values equal to `expr_1`, ..., `expr_n`.
The numeric value is evaluated and substituted for the variable
in any expressions in which the variable occurs if the `numer` flag is
`true`.  See also `ev`.


The expressions `expr_1`, ..., `expr_n` can be any expressions,
not necessarily numeric.

See also: `ev`.

<!-- category: NumberTheory -->
<!-- keywords: oddp -->
<!-- signatures: oddp(expr) -->
### Function: oddp (expr)

Returns `true` if *expr* is a literal odd integer, otherwise
`false`.


`oddp` returns `false` if *expr* is a symbol, even if *expr*
is declared `odd`.

<!-- category: NumberTheory -->
<!-- keywords: ratepsilon -->
<!-- signatures: ratepsilon -->
### Variable: ratepsilon

Default value: `2.0e-15`


`ratepsilon` is the tolerance used in the conversion
of floating point numbers to rational numbers, when the option variable
`bftorat` has the value `false`.  See `bftorat` for an example.

See also: `bftorat`.

<!-- category: NumberTheory -->
<!-- keywords: rationalize -->
<!-- signatures: rationalize(expr) -->
### Function: rationalize (expr)

Convert all double floats and big floats in the Maxima expression *expr* to
their exact rational equivalents.  If you are not familiar with the binary
representation of floating point numbers, you might be surprised that
`rationalize (0.1)` does not equal 1/10.  This behavior isn’t special to
Maxima – the number 1/10 has a repeating, not a terminating, binary
representation.












```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2


(%i2) rationalize (0.1);
                        3602879701896397
(%o2)                   -----------------
                        36028797018963968

(%i3) fpprec : 5$

(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152

(%i5) fpprec : 20$

(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848


(%i7) rationalize (sin (0.1*x + 5.6));
               3602879701896397 x   3152519739159347
(%o7)      sin(------------------ + ----------------)
               36028797018963968    562949953421312
```

<!-- category: NumberTheory -->
<!-- keywords: ratnump -->
<!-- signatures: ratnump(expr) -->
### Function: ratnump (expr)

Returns `true` if *expr* is a literal integer or ratio of literal
integers, otherwise `false`.

<!-- category: NumberTheory -->
<!-- keywords: scale_float -->
<!-- signatures: scale_float(f, n) -->
### Function: scale_float (f, n)

`scale_float` scales the float *f* by the value
`2^n`.  This is done carefully so that no round-off every
occurs.  If *f* is a float, then it is possible to underflow to 0
or overflow, depending on the value of *f* and *n*.  Bigfloats
cannot underflow or overflow.



```maxima
(%i1) scale_float(2d0, 2);
(%o1)                                 8.0
(%i2) scale_float(2d0, -2);
(%o2)                                 0.5
(%i3) scale_float(-2d0, -10);
(%o3)                            - 0.001953125
(%i4) scale_float(1d0, -2000);
(%o4)                                 0.0
(%i5) scale_float(2b0, 2);
(%o5)                                8.0b0
(%i6) scale_float(1b0, -2000);
(%o6)                       8.709809816217217b-603
(%i7) scale_float(1, 5);

scale_float: first arg must be a float or bfloat: 1
 -- an error. To debug this try: debugmode(true);
(%i8) scale_float(1.0, n);

scale_float: second arg must be an integer: n
 -- an error. To debug this try: debugmode(true);
```


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htmscale_float]().  Of course, this is extended to support bfloats.

<!-- category: NumberTheory -->
<!-- keywords: unit_in_last_place -->
<!-- signatures: unit_in_last_place(n) -->
### Function: unit_in_last_place (n)

`unit_in_last_place` returns a value that is the gap between
*n* and the nearest other number.  See, for example,
[https://people.eecs.berkeley.edu/~wkahan/LOG10HAF.TXTKahan, FOOTNOTE 1]().  `unit_in_last_place` supports rational numbers,
floating-point numbers and bigfloat numbers.  For integer, the result
is always 1, and for rational numbers the result is always 0.


The examples below assume
[https://en.wikipedia.org/wiki/IEEE_754IEEE-754]() arithmetic that
supports
[https://en.wikipedia.org/wiki/IEEE_754-1985#Denormalized_numbersdenormal]()
numbers.  Some lisps like [https://clisp.sourceforge.io/Clisp]()
do not have denormal numbers.



```maxima
(%i1) unit_in_last_place(0);
(%o1)                                  1
(%i2) unit_in_last_place(-123);
(%o2)                                  1
(%i3) unit_in_last_place(2/3);
(%o3)                                  0
(%i4) unit_in_last_place(355/113);
(%o4)                                  0
(%i5) unit_in_last_place(0b0);
(%o5)                                0.0b0
(%i6) unit_in_last_place(0.0);
(%o6)                       4.940656458412465e-324
(%i7) unit_in_last_place(1.0);
(%o7)                        1.110223024625157e-16
(%i8) unit_in_last_place(1b0);
(%o8)                        1.387778780781446b-17
(%i9) unit_in_last_place(100.0);
(%o9)                         1.4210854715202e-14
(%i10) unit_in_last_place(100b0);
(%o10)                       1.77635683940025b-15
(%i11) fpprec:32;
(%o11)                                32
(%i12) unit_in_last_place(1b0);
(%o12)               1.5407439555097886824447823540679b-33
(%i13) unit_in_last_place(100b0);
(%o13)               1.972152263052529513529321413207b-31
```

