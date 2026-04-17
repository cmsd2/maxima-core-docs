## ratpow

<!-- category: Polynomials -->
<!-- keywords: ratp_coeffs -->
<!-- signatures: ratp_coeffs(expr, x) -->
### Function: ratp_coeffs (expr, x)

Returns the powers and coefficients of *x* in `ratnumer(expr)` as a list of length-2 lists;
returned coefficients are in CRE form except for numbers.



`ratnumer(expr)`.






```maxima
(%i1) load("ratpow")$

(%i2) ratp_coeffs( 4*x^3 + x + sqrt(x), x);
(%o2)/R/         [[3, 4], [1, 1], [0, sqrt(x)]]
```

<!-- category: Polynomials -->
<!-- keywords: ratp_dense_coeffs -->
<!-- signatures: ratp_dense_coeffs(expr, x) -->
### Function: ratp_dense_coeffs (expr, x)

Returns the coefficients of powers of *x* in `ratnumer(expr)` from highest to lowest;
returned coefficients are in CRE form except for numbers.







```maxima
(%i1) load("ratpow")$

(%i2) ratp_dense_coeffs( 4*x^3 + x + sqrt(x), x);
(%o2)/R/               [4, 0, 1, sqrt(x)]
```

<!-- category: Polynomials -->
<!-- keywords: ratp_hipow -->
<!-- signatures: ratp_hipow(expr, x) -->
### Function: ratp_hipow (expr, x)

Returns the highest power of *x* in `ratnumer(expr)`








```maxima
(%i1) load("ratpow")$

(%i2) ratp_hipow( x^(5/2) + x^2 , x);
(%o2)                           2


(%i3) ratp_hipow( x^(5/2) + x^2 , sqrt(x));
(%o3)                           5
```

<!-- category: Polynomials -->
<!-- keywords: ratp_lopow -->
<!-- signatures: ratp_lopow(expr, x) -->
### Function: ratp_lopow (expr, x)

Returns the lowest power of *x* in `ratnumer(expr)`







```maxima
(%i1) load("ratpow")$

(%i2) ratp_lopow( x^5 + x^2 , x);
(%o2)                           2
```


The following example returns 0 since `1` equals `x^0`:






```maxima
(%i1) load("ratpow")$

(%i2) ratp_lopow( x^5 + x^2 + 1, x);
(%o2)                           0
```


The CRE form of the following equation contains `sqrt(x)` and
`x`. Since they are interpreted as independent variables,
`ratp_lopow` returns `0`:









```maxima
(%i1) load("ratpow")$

(%i2) g:sqrt(x)^5 + sqrt(x)^2;
                             5/2
(%o2)                       x    + x


(%i3) showratvars(g);
                              1/2
(%o3)                       [x   , x]


(%i4) ratp_lopow( g, x);
(%o4)                           0


(%i5) ratp_lopow( g, sqrt(x));
(%o5)                           0
```

