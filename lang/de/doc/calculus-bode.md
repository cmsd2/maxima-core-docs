## bode

<!-- category: Calculus -->
<!-- keywords: bode_gain -->
<!-- signatures: bode_gain(H, range, ...plot_opts...) -->
### Function: bode_gain (H, range, ...plot_opts...)

Function to draw Bode gain plots. To use this function write first
`load("bode")`. See also `bode_phase`.


Examples:


Examples (1 through 7 from
[http://www.swarthmore.edu/NatSci/echeeve1/Ref/Bode/BodeHow.html](),

$$
\texttt{http://www.swarthmore.edu/\-NatSci/\-echeeve1/\-Ref/\-Bode/\-BodeHow.html},
$$

8 from Ron Crummett):



```maxima
(%i1) load("bode")$
(%i2) H1 (s) := 100 * (1 + s) / ((s + 10) * (s + 100))$
(%i3) bode_gain (H1 (s), [w, 1/1000, 1000])$
```

![./figures/bodegain1](./figures/bodegain1.png)


```maxima
(%i4) H2 (s) := 1 / (1 + s/omega0)$
(%i5) bode_gain (H2 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodegain2](./figures/bodegain2.png)


```maxima
(%i6) H3 (s) := 1 / (1 + s/omega0)^2$
(%i7) bode_gain (H3 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodegain3](./figures/bodegain3.png)


```maxima
(%i8) H4 (s) := 1 + s/omega0$
(%i9) bode_gain (H4 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodegain4](./figures/bodegain4.png)


```maxima
(%i10) H5 (s) := 1/s$
(%i11) bode_gain (H5 (s), [w, 1/1000, 1000])$
```

![./figures/bodegain5](./figures/bodegain5.png)


```maxima
(%i12) H6 (s) := 1/((s/omega0)^2 + 2 * zeta * (s/omega0) + 1)$
(%i13) bode_gain (H6 (s), [w, 1/1000, 1000]), 
                          omega0 = 10, zeta = 1/10$
```

![./figures/bodegain6](./figures/bodegain6.png)


```maxima
(%i14) H7 (s) := (s/omega0)^2 + 2 * zeta * (s/omega0) + 1$
(%i15) bode_gain (H7 (s), [w, 1/1000, 1000]),
                          omega0 = 10, zeta = 1/10$
```

![./figures/bodegain7](./figures/bodegain7.png)


```maxima
(%i16) H8 (s) := 0.5 / (0.0001 * s^3 + 0.002 * s^2 + 0.01 * s)$
(%i17) bode_gain (H8 (s), [w, 1/1000, 1000])$
```

![./figures/bodegain8](./figures/bodegain8.png)

See also: `bode_phase`.

<!-- category: Calculus -->
<!-- keywords: bode_phase -->
<!-- signatures: bode_phase(H, range, ...plot_opts...) -->
### Function: bode_phase (H, range, ...plot_opts...)

Function to draw Bode phase plots. To use this function write first 
`load("bode")`. See also `bode_gain`.


Examples:


Examples (1 through 7 from
[http://www.swarthmore.edu/NatSci/echeeve1/Ref/Bode/BodeHow.html](),

$$
\texttt{http://www.swarthmore.edu/\-NatSci/\-echeeve1/\-Ref/\-Bode/\-BodeHow.html},
$$

8 from Ron Crummett):



```maxima
(%i1) load("bode")$
(%i2) H1 (s) := 100 * (1 + s) / ((s + 10) * (s + 100))$
(%i3) bode_phase (H1 (s), [w, 1/1000, 1000])$
```

![./figures/bodephase1](./figures/bodephase1.png)


```maxima
(%i4) H2 (s) := 1 / (1 + s/omega0)$
(%i5) bode_phase (H2 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodephase2](./figures/bodephase2.png)


```maxima
(%i6) H3 (s) := 1 / (1 + s/omega0)^2$
(%i7) bode_phase (H3 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodephase3](./figures/bodephase3.png)


```maxima
(%i8) H4 (s) := 1 + s/omega0$
(%i9) bode_phase (H4 (s), [w, 1/1000, 1000]), omega0 = 10$
```

![./figures/bodephase4](./figures/bodephase4.png)


```maxima
(%i10) H5 (s) := 1/s$
(%i11) bode_phase (H5 (s), [w, 1/1000, 1000])$
```

![./figures/bodephase5](./figures/bodephase5.png)


```maxima
(%i12) H6 (s) := 1/((s/omega0)^2 + 2 * zeta * (s/omega0) + 1)$
(%i13) bode_phase (H6 (s), [w, 1/1000, 1000]), 
                   omega0 = 10, zeta = 1/10$
```

![./figures/bodephase6](./figures/bodephase6.png)


```maxima
(%i14) H7 (s) := (s/omega0)^2 + 2 * zeta * (s/omega0) + 1$
(%i15) bode_phase (H7 (s), [w, 1/1000, 1000]), 
                   omega0 = 10, zeta = 1/10$
```

![./figures/bodephase7](./figures/bodephase7.png)


```maxima
(%i16) H8 (s) := 0.5 / (0.0001 * s^3 + 0.002 * s^2 + 0.01 * s)$
(%i17) bode_phase (H8 (s), [w, 1/1000, 1000])$
```

![./figures/bodephase8](./figures/bodephase8.png)







```maxima
(%i18) block ([bode_phase_unwrap : true], 
              bode_phase (H8 (s), [w, 1/1000, 1000]));
```

![./figures/bodephase9](./figures/bodephase9.png)

See also: `bode_gain`.

