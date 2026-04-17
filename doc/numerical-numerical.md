## Numerical

<!-- category: Numerical -->
<!-- keywords: bf_fft -->
<!-- signatures: bf_fft(y) -->
### Function: bf_fft (y)

Computes the forward complex fast Fourier transform.  This is the
bigfloat version of `fft` that converts the input to
bigfloats and returns a bigfloat result.

See also: `fft`.

<!-- category: Numerical -->
<!-- keywords: bf_inverse_fft -->
<!-- signatures: bf_inverse_fft(y) -->
### Function: bf_inverse_fft (y)

Computes the inverse complex fast Fourier transform.  This is the
bigfloat version of `inverse_fft` that converts the input to
bigfloats and returns a bigfloat result.

See also: `inverse_fft`.

<!-- category: Numerical -->
<!-- keywords: bf_inverse_real_fft -->
<!-- signatures: bf_inverse_real_fft(y) -->
### Function: bf_inverse_real_fft (y)

Computes the inverse fast Fourier transform with a real-valued
bigfloat output.  This is the bigfloat version of `inverse_real_fft`.

<!-- category: Numerical -->
<!-- keywords: bf_real_fft -->
<!-- signatures: bf_real_fft(x) -->
### Function: bf_real_fft (x)

Computes the forward fast Fourier transform of a real-valued input
returning a bigfloat result.  This is the bigfloat version of
`real_fft`.

<!-- category: Numerical -->
<!-- keywords: fft -->
<!-- signatures: fft(x) -->
### Function: fft (x)

Computes the complex fast Fourier transform.
*x* is a list or array (named or unnamed) which contains the data to
transform.  The number of elements must be a power of 2.
The elements must be literal numbers (integers, rationals, floats, or bigfloats)
or symbolic constants,
or expressions `a + b*%i` where `a` and `b` are literal numbers
or symbolic constants.


`fft` returns a new object of the same type as *x*,
which is not modified.
Results are always computed as floats
or expressions `a + b*%i` where `a` and `b` are floats.
If bigfloat precision is needed the function `bf_fft` can be used
instead as a drop-in replacement of `fft` that is slower, but
supports bfloats. In addition if it is known that the input consists
of only real values (no imaginary parts), `real_fft` can be used
which is potentially faster.


The discrete Fourier transform is defined as follows.
Let $y$ be the output of the transform.
Then for $k$ from 0 through $n - 1$,



$$y[k] = {1\over n} \sum_{j=0}^{n-1} x[j] e^{+2i\pi j k / n}$$


$$y[k] = {1\over n} \sum_{j=0}^{n-1} x[j] e^{+2i\pi j k / n}$$



As there are various sign and normalization conventions possible,
this definition of the transform may differ from that used by other mathematical software.


When the data *x* are real,
real coefficients `a` and `b` can be computed such that



$$x[j] = \sum_{k=0}^{n/2} \left(a[k] \cos {2\pi j k\over n} + b[k] \sin {2\pi j k \over n}\right)$$


$$x[j] = \sum_{k=0}^{n/2} \left(a[k] \cos {2\pi j k\over n} + b[k]
\sin {2\pi j k \over n}\right)$$



with



$$\eqalign{ a[0] &= {\rm realpart}(y[0])\cr b[0] &= 0 }$$


$$\eqalign{
a[0] &= {\rm realpart}(y[0])\cr
b[0] &= 0
}$$



and, for $k$ from 1 through $n/2 - 1$,



$$\eqalign{ a[k] &= {\rm realpart}(y[k] + y[n-k]) \cr b[k] &= {\rm imagpart}(y[n-k] - y[k]) }$$


$$\eqalign{
a[k] &= {\rm realpart}(y[k] + y[n-k]) \cr
b[k] &= {\rm imagpart}(y[n-k] - y[k])
}$$



and



$$\eqalign{ a\left[{n\over 2}\right] &= {\rm realpart}\left(y\left[{n\over 2}\right]\right) \cr b\left[{n\over 2}\right] &= 0 }$$


$$\eqalign{
a\left[{n\over 2}\right] &= {\rm realpart}\left(y\left[{n\over 2}\right]\right) \cr
b\left[{n\over 2}\right] &= 0
}$$



`load("fft")` loads this function.


See also `inverse_fft` (inverse transform),
`recttopolar`, and `polartorect`.. See `real_fft`
for FFTs of a real-valued input, and `bf_fft` and
`bf_real_fft` for operations on bigfloat values.  Finally, for
transforms of any size (but limited to float values), see
`fftpack5_fft` and `fftpack5_real_fft`.


Examples:


Real data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $

(%i4) L1 : fft (L);
(%o4) [0.0, 1.811 %i - 0.1036, 0.0, 0.3107 %i + 0.6036, 0.0, 
                    0.6036 - 0.3107 %i, 0.0, - 1.811 %i - 0.1036]


(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 4.441e-16 %i + 2.0, 3.0, 4.0 - 4.441e-16 %i, - 1.0, 
                 - 4.441e-16 %i - 2.0, - 3.0, 4.441e-16 %i - 4.0]


(%i6) lmax (abs (L2 - L));
(%o6)                       4.441e-16
```


Complex data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $

(%i4) L1 : fft (L);
(%o4) [0.5, 0.5, 0.25 %i - 0.25, - 0.3536 %i - 0.3536, 0.0, 0.5, 
                            - 0.25 %i - 0.25, 0.3536 %i + 0.3536]


(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, - 1.0, - 1.0, 
                                 1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0]


(%i6) lmax (abs (L2 - L));
(%o6)                          0.0
```


Computation of sine and cosine coefficients.

























```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, 5, 6, 7, 8] $
(%i4) n : length (L) $
(%i5) x : make_array (any, n) $
(%i6) fillarray (x, L) $
(%i7) y : fft (x) $
(%i8) a : make_array (any, n/2 + 1) $
(%i9) b : make_array (any, n/2 + 1) $
(%i10) a[0] : realpart (y[0]) $
(%i11) b[0] : 0 $

(%i12) for k : 1 thru n/2 - 1 do
   (a[k] : realpart (y[k] + y[n - k]),
    b[k] : imagpart (y[n - k] - y[k]));
(%o12)                        done

(%i13) a[n/2] : y[n/2] $
(%i14) b[n/2] : 0 $

(%i15) listarray (a);
(%o15)          [4.5, - 1.0, - 1.0, - 1.0, - 0.5]


(%i16) listarray (b);
(%o16)             [0, 2.414, 1.0, 0.4142, 0]

(%i17) f(j) := sum (a[k] * cos (2*%pi*j*k / n) + b[k] * sin (2*%pi*j*k / n), k, 0, n/2) $

(%i18) makelist (float (f (j)), j, 0, n - 1);
(%o18)      [1.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0]
```

See also: `bf_fft`, `real_fft`, `inverse_fft`, `recttopolar`, `polartorect`, `bf_real_fft`, `fftpack5_fft`, `fftpack5_real_fft`.

<!-- category: Numerical -->
<!-- keywords: fftpack5_fft -->
<!-- signatures: fftpack5_fft(x) -->
### Function: fftpack5_fft (x)

Like `fft` (`fft`), this computes the fast Fourier transform
of a complex sequence.  However, the length of *x* is not limited
to a power of 2.  


`load("fftpack5")` loads this function.


Examples:


Real data.



```maxima
(%i1) load("fftpack5") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2 ,-3, -4] $
(%i4) L1 : fftpack5_fft(L);
(%o4) [0.0, 1.811 %i - 0.1036, 0.0, 0.3107 %i + 0.6036, 0.0, 
                                0.6036 - 0.3107 %i, 0.0, (- 1.811 %i) - 0.1036]
(%i5) L2 : fftpack5_inverse_fft(L1);
(%o5) [1.0, 4.441e-16 %i + 2.0, 1.837e-16 %i + 3.0, 4.0 - 4.441e-16 %i, 
     - 1.0, (- 4.441e-16 %i) - 2.0, (- 1.837e-16 %i) - 3.0, 4.441e-16
       %i - 4.0]
(%i6) lmax (abs (L2-L));
(%o6)                       4.441e-16
(%i7) L : [1, 2, 3, 4, 5, 6]$
(%i8) L1 : fftpack5_fft(L);
(%o8) [3.5, (- 0.866 %i) - 0.5, (- 0.2887 %i) - 0.5, (- 1.48e-16 %i) - 0.5, 
                                               0.2887 %i - 0.5, 0.866
                                                      %%i - 0.5]
(%i9) L2 : fftpack5_inverse_fft (L1);
(%o9) [1.0 - 1.48e-16 %i, 3.701e-17 %i + 2.0, 3.0 - 1.48e-16 %i, 
                     4.0 - 1.811e-16 %i, 5.0 - 1.48e-16 %i, 5.881e-16
                           %i + 6.0]
(%i10) lmax (abs (L2-L));
(%o10)                             9.064e-16
```


Complex data.



```maxima
(%i1) load("fftpack5") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : fftpack5_inverse_fft (L);
(%o4) [4.0, 2.828 %i + 2.828, (- 2.0 %i) - 2.0, 4.0, 0.0, 
                                       (- 2.828 %i) - 2.828, 2.0 %i - 2.0, 4.0]
(%i5) L2 : fftpack5_fft(L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, (- 2.776e-17 %i) - 1.0, - 1.0, 
                                1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0 -
                                          %2.776e-17 %i]
(%i6) lmax(abs(L2-L));
(%o6)                              1.11e-16
```

See also: `fft`.

<!-- category: Numerical -->
<!-- keywords: fftpack5_inverse_fft -->
<!-- signatures: fftpack5_inverse_fft(y) -->
### Function: fftpack5_inverse_fft (y)

Computes the inverse complex Fourier transform, like
`inverse_fft`, but is not constrained to be a power of two.

<!-- category: Numerical -->
<!-- keywords: fftpack5_inverse_real_fft -->
<!-- signatures: fftpack5_inverse_real_fft(y, n) -->
### Function: fftpack5_inverse_real_fft (y, n)

Computes the inverse Fourier transform of *y*, which must have a
length of `floor(n/2) + 1`.  The length of sequence produced by the
inverse transform must be specified by *n*.  This is required
because the length of *y* does not uniquely determine *n*.
The last element of *y* is always real if *n* is even, but it
can be complex when *n* is odd.

<!-- category: Numerical -->
<!-- keywords: fftpack5_real_fft -->
<!-- signatures: fftpack5_real_fft(x) -->
### Function: fftpack5_real_fft (x)

Computes the fast Fourier transform of a real-valued sequence *x*,
just like `real_fft`, except the length is not constrained to be
a power of two.


Examples:



```maxima
(%i1) fpprintprec : 4 $
(%i2) L : [1, 2, 3, 4, 5, 6] $
(%i3) L1 : fftpack5_real_fft(L);
(%o3)       [3.5, (- 0.866 %i) - 0.5, (- 0.2887 %i) - 0.5, - 0.5]
(%i4) L2 : fftpack5_inverse_real_fft(L1, 6);
(%o4)                  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
(%i5) lmax(abs(L2-L));
(%o5)                            1.332e-15
(%i6) fftpack5_inverse_real_fft(L1, 7);
(%o6)            [0.5, 2.083, 2.562, 3.7, 4.3, 5.438, 5.917]
```


The last example shows how important it to set the length correctly
for `fftpack5_inverse_real_fft`.

<!-- category: Numerical -->
<!-- keywords: inverse_fft -->
<!-- signatures: inverse_fft(y) -->
### Function: inverse_fft (y)

Computes the inverse complex fast Fourier transform.
*y* is a list or array (named or unnamed) which contains the data to
transform.  The number of elements must be a power of 2.
The elements must be literal numbers (integers, rationals, floats, or bigfloats)
or symbolic constants,
or expressions $a + bi$ where $a$ and $b$ are literal numbers
or symbolic constants.


`inverse_fft` returns a new object of the same type as $y$,
which is not modified.
Results are always computed as floats
or expressions `a + b*%i` where `a` and `b` are floats.
If bigfloat precision is needed the function `bf_inverse_fft` can
be used instead as a drop-in replacement of `inverse_fft` that is
slower, but supports bfloats. 


The inverse discrete Fourier transform is defined as follows.
Let $x$ be the output of the inverse transform.
Then for $j$ from 0 through $n - 1$,



$$x[j] = \sum_{k=0}^{n-1} y[k] e^{-2i\pi j k/n}$$


$$x[j] = \sum_{k=0}^{n-1} y[k] e^{-2i\pi j k/n}$$



As there are various sign and normalization conventions possible,
this definition of the transform may differ from that used by other mathematical software.


`load("fft")` loads this function.


See also `fft` (forward transform), `recttopolar`, and
`polartorect`.


Examples:


Real data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $

(%i4) L1 : inverse_fft (L);
(%o4) [0.0, - 14.49 %i - 0.8284, 0.0, 4.828 - 2.485 %i, 0.0, 
                        2.485 %i + 4.828, 0.0, 14.49 %i - 0.8284]


(%i5) L2 : fft (L1);
(%o5) [1.0, 2.0 - 4.441e-16 %i, 3.0, 4.441e-16 %i + 4.0, - 1.0, 
                 4.441e-16 %i - 2.0, - 3.0, - 4.441e-16 %i - 4.0]


(%i6) lmax (abs (L2 - L));
(%o6)                       4.441e-16
```


Complex data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $

(%i4) L1 : inverse_fft (L);
(%o4) [4.0, 2.828 %i + 2.828, - 2.0 %i - 2.0, 4.0, 0.0, 
                           - 2.828 %i - 2.828, 2.0 %i - 2.0, 4.0]


(%i5) L2 : fft (L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, - 1.0, - 1.0, 
                                 1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0]


(%i6) lmax (abs (L2 - L));
(%o6)                          0.0
```

See also: `bf_inverse_fft`, `fft`, `recttopolar`, `polartorect`.

<!-- category: Numerical -->
<!-- keywords: inverse_real_fft -->
<!-- signatures: inverse_real_fft(y) -->
### Function: inverse_real_fft (y)

Computes the inverse Fourier transform of *y*, which must have a
length of `N/2+1` where `N` is a power of two.  That is, the
input *x* is expected to be the output of `real_fft`.


No check is made to ensure that the input has the correct format.
(The first and last elements must be purely real.)

<!-- category: Numerical -->
<!-- keywords: polartorect -->
<!-- signatures: polartorect(r, t) -->
### Function: polartorect (r, t)

Translates complex values of the form $r e^{i t}$ to the form
$a + b i$, where $r$ is the magnitude and $t$ is the phase.
$r$ and $t$ are 1-dimensional arrays of the same size.
The array size need not be a power of 2.


The original values of the input arrays are
replaced by the real and imaginary parts, $a$ and $b$, on return.
The outputs are calculated as



$$\eqalign{ a &= r \cos t \cr b &= r \sin t }$$


$$\eqalign{
a &= r \cos t \cr
b &= r \sin t
}$$



`polartorect` is the inverse function of `recttopolar`.


`load("fft")` loads this function.  See also `fft`.

See also: `polartorect`, `recttopolar`, `fft`.

<!-- category: Numerical -->
<!-- keywords: real_fft -->
<!-- signatures: real_fft(x) -->
### Function: real_fft (x)

Computes the fast Fourier transform of a real-valued sequence
*x*.  This is equivalent to performing `fft(x)`, except that
only the first `N/2+1` results are returned, where `N` is
the length of *x*.  `N` must be power of two.


No check is made that *x* contains only real values.


The symmetry properties of the Fourier transform of real sequences to
reduce he complexity.  In particular the first and last output values
of `real_fft` are purely real.  For larger sequences, `real_fft`
may be computed more quickly than `fft`.


Since the output length is short, the normal `inverse_fft` cannot
be directly used.  Use `inverse_real_fft` to compute the inverse.

See also: `inverse_fft`, `inverse_real_fft`.

<!-- category: Numerical -->
<!-- keywords: recttopolar -->
<!-- signatures: recttopolar(a, b) -->
### Function: recttopolar (a, b)

Translates complex values of the form $a + b i$ to the form
$r e^{i t}$, where $a$ is the real part and $b$ is the imaginary
part.  $a$ and $b$ are 1-dimensional arrays of the same size.
The array size need not be a power of 2.


The original values of the input arrays are
replaced by the magnitude and angle, $r$ and $t$, on return.
The outputs are calculated as



$$\eqalign{ r &= \sqrt{a^2+b^2} \cr t &= {\rm atan2}(b, a) }$$


$$\eqalign{
r &= \sqrt{a^2+b^2} \cr
t &= {\rm atan2}(b, a)
}$$



The computed angle is in the range
$-\pi$
to
$\pi.$


`recttopolar` is the inverse function of `polartorect`.


`load("fft")` loads this function.  See also `fft`.

See also: `polartorect`, `fft`.

