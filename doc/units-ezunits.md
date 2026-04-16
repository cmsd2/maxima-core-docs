## ezunits

### Function: ` ()

The dimensional quantity operator.
An expression $a ` b$ represents a dimensional quantity,
with `a` indicating a nondimensional quantity and `b` indicating the dimensional units.
A symbol can be used as a unit without declaring it as such;
unit symbols need not have any special properties.
The quantity and unit of an expression $a ` b$ can
be extracted by the `qty` and `units` functions, respectively.


Arithmetic operations on dimensional quantities are carried out by
conventional rules for such operations.



- * 
$(x ` a) * (y ` b)$ is equal to $(x * y) ` (a * b)$.
- * 
$(x ` a) + (y ` a)$ is equal to $(x + y) ` a$.
- * 
$(x ` a)^y$ is equal to $x^y ` a^y$ when `y` is nondimensional.


`ezunits` does not require that units in a sum have the same dimensions;
such terms are not added together, and no error is reported.


`load ("ezunits")` enables this operator.


Examples:


SI (Systeme Internationale) units.










```maxima
(%i1) load ("ezunits")$
(%i2) foo : 10 ` m;
(%o2)                        10 ` m
(%i3) qty (foo);
(%o3)                          10
(%i4) units (foo);
(%o4)                           m
(%i5) dimensions (foo);
(%o5)                        length
```


"Customary" units.









```maxima
(%i1) load ("ezunits")$
(%i2) bar : x ` acre;
(%o2)                       x ` acre
(%i3) dimensions (bar);
                                   2
(%o3)                        length
(%i4) fundamental_units (bar);
                                2
(%o4)                          m
```


Units ad hoc.










```maxima
(%i1) load ("ezunits")$
(%i2) baz : 3 ` sheep + 8 ` goat + 1 ` horse;
(%o2)           8 ` goat + 3 ` sheep + 1 ` horse
(%i3) subst ([sheep = 3*goat, horse = 10*goat], baz);
(%o3)                       27 ` goat
(%i4) baz2 : 1000`gallon/fortnight;
                                gallon
(%o4)                   1000 ` ---------
                               fortnight
(%i5) subst (fortnight = 14*day, baz2);
                          500   gallon
(%o5)                     --- ` ------
                           7     day
```


Arithmetic operations on dimensional quantities.











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` kg + 200 ` kg;
(%o2)                       300 ` kg
(%i3) 100 ` m^3 - 100 ` m^3;
                                  3
(%o3)                        0 ` m
(%i4) (10 ` kg) * (17 ` m/s^2);
                                 kg m
(%o4)                      170 ` ----
                                   2
                                  s
(%i5) (x ` m) / (y ` s);
                              x   m
(%o5)                         - ` -
                              y   s
(%i6) (a ` m)^2;
                              2    2
(%o6)                        a  ` m
```

### Function: `` ()

The unit conversion operator.
An expression $a ` b `` c$ converts from unit `b` to unit `c`.
`ezunits` has built-in conversions for SI base units,
SI derived units, and some non-SI units.
Unit conversions not already known to `ezunits` can be declared.
The unit conversions known to `ezunits` are specified by the
global variable `known_unit_conversions`,
which comprises built-in and user-defined conversions.
Conversions for products, quotients, and powers of units are
derived from the set of known unit conversions.


There is no preferred system for display of units;
input units are not converted to other units
unless conversion is explicitly indicated.
`ezunits` does not attempt to simplify units by prefixes
(milli-, centi-, deci-, etc)
unless such conversion is explicitly indicated.


`load ("ezunits")` enables this operator.


Examples:


The set of known unit conversions.








```maxima
(%i1) load ("ezunits")$
(%i2) display2d : false$
(%i3) known_unit_conversions;
(%o3) {acre = 4840*yard^2,Btu = 1055*J,cfm = feet^3/minute,
       cm = m/100,day = 86400*s,feet = 381*m/1250,ft = feet,
       g = kg/1000,gallon = 757*l/200,GHz = 1000000000*Hz,
       GOhm = 1000000000*Ohm,GPa = 1000000000*Pa,
       GWb = 1000000000*Wb,Gg = 1000000*kg,Gm = 1000000000*m,
       Gmol = 1000000*mol,Gs = 1000000000*s,ha = hectare,
       hectare = 100*m^2,hour = 3600*s,Hz = 1/s,inch = feet/12,
       km = 1000*m,kmol = 1000*mol,ks = 1000*s,l = liter,
       lbf = pound_force,lbm = pound_mass,liter = m^3/1000,
       metric_ton = Mg,mg = kg/1000000,MHz = 1000000*Hz,
       microgram = kg/1000000000,micrometer = m/1000000,
       micron = micrometer,microsecond = s/1000000,
       mile = 5280*feet,minute = 60*s,mm = m/1000,
       mmol = mol/1000,month = 2629800*s,MOhm = 1000000*Ohm,
       MPa = 1000000*Pa,ms = s/1000,MWb = 1000000*Wb,
       Mg = 1000*kg,Mm = 1000000*m,Mmol = 1000000000*mol,
       Ms = 1000000*s,ns = s/1000000000,ounce = pound_mass/16,
       oz = ounce,Ohm = s*J/C^2,
       pound_force = 32*ft*pound_mass/s^2,
       pound_mass = 200*kg/441,psi = pound_force/inch^2,
       Pa = N/m^2,week = 604800*s,Wb = J/A,yard = 3*feet,
       year = 31557600*s,C = s*A,F = C^2/J,GA = 1000000000*A,
       GC = 1000000000*C,GF = 1000000000*F,GH = 1000000000*H,
       GJ = 1000000000*J,GK = 1000000000*K,GN = 1000000000*N,
       GS = 1000000000*S,GT = 1000000000*T,GV = 1000000000*V,
       GW = 1000000000*W,H = J/A^2,J = m*N,kA = 1000*A,
       kC = 1000*C,kF = 1000*F,kH = 1000*H,kHz = 1000*Hz,
       kJ = 1000*J,kK = 1000*K,kN = 1000*N,kOhm = 1000*Ohm,
       kPa = 1000*Pa,kS = 1000*S,kT = 1000*T,kV = 1000*V,
       kW = 1000*W,kWb = 1000*Wb,mA = A/1000,mC = C/1000,
       mF = F/1000,mH = H/1000,mHz = Hz/1000,mJ = J/1000,
       mK = K/1000,mN = N/1000,mOhm = Ohm/1000,mPa = Pa/1000,
       mS = S/1000,mT = T/1000,mV = V/1000,mW = W/1000,
       mWb = Wb/1000,MA = 1000000*A,MC = 1000000*C,
       MF = 1000000*F,MH = 1000000*H,MJ = 1000000*J,
       MK = 1000000*K,MN = 1000000*N,MS = 1000000*S,
       MT = 1000000*T,MV = 1000000*V,MW = 1000000*W,
       N = kg*m/s^2,R = 5*K/9,S = 1/Ohm,T = J/(m^2*A),V = J/C,
       W = J/s}
```


Elementary unit conversions.
















```maxima
(%i1) load ("ezunits")$
(%i2) 1 ` ft `` m;
Computing conversions to base units; may take a moment. 
                            381
(%o2)                       ---- ` m
                            1250
(%i3) %, numer;
(%o3)                      0.3048 ` m
(%i4) 1 ` kg `` lbm;
                            441
(%o4)                       --- ` lbm
                            200
(%i5) %, numer;
(%o5)                      2.205 ` lbm
(%i6) 1 ` W `` Btu/hour;
                           720   Btu
(%o6)                      --- ` ----
                           211   hour
(%i7) %, numer;
                                        Btu
(%o7)               3.412322274881517 ` ----
                                        hour
(%i8) 100 ` degC `` degF;
(%o8)                      212 ` degF
(%i9) -40 ` degF `` degC;
(%o9)                     (- 40) ` degC
(%i10) 1 ` acre*ft `` m^3;
                        60228605349    3
(%o10)                  ----------- ` m
                         48828125
(%i11) %, numer;
                                          3
(%o11)                1233.48183754752 ` m
```


Coercing quantities in feet and meters to one or the other.











```maxima
(%i1) load ("ezunits")$
(%i2) 100 ` m + 100 ` ft;
(%o2)                  100 ` m + 100 ` ft
(%i3) (100 ` m + 100 ` ft) `` ft;
Computing conversions to base units; may take a moment. 
                           163100
(%o3)                      ------ ` ft
                            381
(%i4) %, numer;
(%o4)                428.0839895013123 ` ft
(%i5) (100 ` m + 100 ` ft) `` m;
                            3262
(%o5)                       ---- ` m
                             25
(%i6) %, numer;
(%o6)                      130.48 ` m
```


Dimensional analysis to find fundamental dimensions and fundamental units.











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 1 ` acre * ft;
(%o2)                      1 ` acre ft
(%i3) dimensions (foo);
                                   3
(%o3)                        length
(%i4) fundamental_units (foo);
                                3
(%o4)                          m
(%i5) foo `` m^3;
Computing conversions to base units; may take a moment. 
                        60228605349    3
(%o5)                   ----------- ` m
                         48828125
(%i6) %, numer;
                                          3
(%o6)                 1233.48183754752 ` m
```


Declared unit conversions.











```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (MMBtu = 10^6*Btu, kW = 1000*W);
(%o2)                         done
(%i3) declare_unit_conversion (kWh = kW*hour, MWh = 1000*kWh,
                               bell = 1800*s);
(%o3)                         done
(%i4) 1 ` kW*s `` MWh;
Computing conversions to base units; may take a moment. 
                             1
(%o4)                     ------- ` MWh
                          3600000
(%i5) 1 ` kW/m^2 `` MMBtu/bell/ft^2;
                       1306449      MMBtu
(%o5)                 ---------- ` --------
                      8242187500          2
                                   bell ft
```

### Function: constvalue (x)

Shows the value and the units of one of the constants declared by package
`physical_constants`, which includes a list of physical constants, or
of a new constant declared in package `ezunits` (see
`declare_constvalue`).


Note that constant values as recognized by `constvalue`
are separate from values declared by `numerval` and
recognized by `constantp`.


Example:








```maxima
(%i1) load ("physical_constants")$
(%i2) constvalue (%G);
                                     3
                                    m
(%o2)                    6.67428 ` -----
                                       2
                                   kg s
(%i3) get ('%G, 'description);
(%o3)           Newtonian constant of gravitation
```

See also: `declare_constvalue`.

### Function: declare_constvalue (a, x)

Declares the value of a constant to be used in package `ezunits`. This
function should be loaded with `load ("ezunits")`. 


Example:









```maxima
(%i1) load ("ezunits")$
(%i2) declare_constvalue (FOO, 100 ` lbm / acre);
                                 lbm
(%o2)                      100 ` ----
                                 acre
(%i3) FOO * (50 ` acre);
(%o3)                     50 FOO ` acre
(%i4) constvalue (%);
(%o4)                      5000 ` lbm
```

### Function: declare_dimensions (a_1, d_1, ..., a_n, d_n)

Declares *a_1*, ..., *a_n* to have dimensions *d_1*, ...,
*d_n*, respectively.


Each *a_k* is a symbol or a list of symbols.
If it is a list, then every symbol in *a_k* is declared to have dimension *d_k*.


`load ("ezunits")` loads these functions.


Examples:









```maxima
(%i1) load ("ezunits") $
(%i2) declare_dimensions ([x, y, z], length, [t, u], time);
(%o2)                         done
(%i3) dimensions (y^2/u);
                                   2
                             length
(%o3)                        -------
                              time
(%i4) fundamental_units (y^2/u);
0 errors, 0 warnings
                                2
                               m
(%o4)                          --
                               s
```

### Function: declare_fundamental_dimensions (d_1, d_2, d_3, ...)

`declare_fundamental_dimensions` declares fundamental dimensions.
Symbols *d_1*, *d_2*, *d_3*, ... are appended to the list of
fundamental dimensions, if they are not already on the list.


`remove_fundamental_dimensions` reverts the effect of `declare_fundamental_dimensions`.


`fundamental_dimensions` is the list of fundamental dimensions.
By default, the list comprises several physical dimensions.


`load ("ezunits")` loads these functions.


Examples:











```maxima
(%i1) load ("ezunits") $
(%i2) fundamental_dimensions;
(%o2) [length, mass, time, current, temperature, quantity]
(%i3) declare_fundamental_dimensions (money, cattle, happiness);
(%o3)                         done
(%i4) fundamental_dimensions;
(%o4) [length, mass, time, current, temperature, quantity, 
                                        money, cattle, happiness]
(%i5) remove_fundamental_dimensions (cattle, happiness);
(%o5)                         done
(%i6) fundamental_dimensions;
(%o6) [length, mass, time, current, temperature, quantity, money]
```

### Function: declare_fundamental_units (u_1, d_1, ..., u_n, d_n)

`declare_fundamental_units` declares *u_1*, ..., *u_n*
to have dimensions *d_1*, ..., *d_n*, respectively.
All arguments must be symbols.


After calling `declare_fundamental_units`,
`dimensions(u_k)` returns *d_k* for each argument *u_1*, ..., *u_n*,
and `fundamental_units(d_k)` returns *u_k* for each argument *d_1*, ..., *d_n*.


`remove_fundamental_units` reverts the effect of `declare_fundamental_units`.


`load ("ezunits")` loads these functions.


Examples:












```maxima
(%i1) load ("ezunits") $
(%i2) declare_fundamental_dimensions (money, cattle, happiness);
(%o2)                         done
(%i3) declare_fundamental_units (dollar, money, goat, cattle,
                                 smile, happiness);
(%o3)                 [dollar, goat, smile]
(%i4) dimensions (100 ` dollar/goat/km^2);
                             money
(%o4)                    --------------
                                      2
                         cattle length
(%i5) dimensions (x ` smile/kg);
                            happiness
(%o5)                       ---------
                              mass
(%i6) fundamental_units (money*cattle/happiness);
0 errors, 0 warnings
                           dollar goat
(%o6)                      -----------
                              smile
```

### Function: declare_qty (a, x)

Declares that `qty` should return *x* for symbol *a*, where
*x* is a nondimensional quantity. This function should be loaded
with `load ("ezunits")`.


Example:











```maxima
(%i1) load ("ezunits")$
(%i2) declare_qty (aa, xx);
(%o2)                          xx
(%i3) qty (aa);
(%o3)                          xx
(%i4) qty (aa^2);
                                 2
(%o4)                          xx
(%i5) foo : 100 ` kg;
(%o5)                       100 ` kg
(%i6) qty (aa * foo);
(%o6)                        100 xx
```

See also: `qty`.

### Function: declare_unit_conversion (u, =, v, ...)

Appends equations *u* = *v*, ... to the list of unit conversions
known to the unit conversion operator $``$.
*u* and *v* are both multiplicative terms,
in which any variables are units,
or both literal dimensional expressions.


At present, it is necessary to express conversions such that
the left-hand side of each equation is a simple unit
(not a multiplicative expression)
or a literal dimensional expression with the quantity equal to 1
and the unit being a simple unit.
This limitation might be relaxed in future versions.


`known_unit_conversions` is the list of known unit conversions.


This function should be loaded with `load ("ezunits")`.


Examples:


Unit conversions expressed by equations of multiplicative terms.









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (nautical_mile = 1852 * m,
                               fortnight = 14 * day);
(%o2)                         done
(%i3) 100 ` nautical_mile / fortnight `` m/s;
Computing conversions to base units; may take a moment. 
                            463    m
(%o3)                       ---- ` -
                            3024   s
```


Unit conversions expressed by equations of literal dimensional expressions.









```maxima
(%i1) load ("ezunits")$
(%i2) declare_unit_conversion (1 ` fluid_ounce = 2 ` tablespoon);
(%o2)                         done
(%i3) declare_unit_conversion (1 ` tablespoon = 3 ` teaspoon);
(%o3)                         done
(%i4) 15 ` fluid_ounce `` teaspoon;
Computing conversions to base units; may take a moment. 
(%o4)                     90 ` teaspoon
```

### Function: declare_units (a, u)

Declares that `units` should return units *u* for *a*,
where *u* is an expression. This function should be loaded with
`load ("ezunits")`.


Example:












```maxima
(%i1) load ("ezunits")$
(%i2) units (aa);
(%o2)                           1
(%i3) declare_units (aa, J);
(%o3)                           J
(%i4) units (aa);
(%o4)                           J
(%i5) units (aa^2);
                                2
(%o5)                          J
(%i6) foo : 100 ` kg;
(%o6)                       100 ` kg
(%i7) units (aa * foo);
(%o7)                         kg J
```

See also: `units`.

### Function: dimensionless (L)

Returns a basis for the dimensionless quantities which can be formed
from a list *L* of dimensional quantities.


`load ("ezunits")` loads this function.


Examples:







```maxima
(%i1) load ("ezunits") $
(%i2) dimensionless ([x ` m, y ` m/s, z ` s]);
0 errors, 0 warnings
0 errors, 0 warnings
                               y z
(%o2)                         [---]
                                x
```


Dimensionless quantities derived from fundamental physical quantities.
Note that the first element on the list
is proportional to the fine-structure constant.








```maxima
(%i1) load ("ezunits") $
(%i2) load ("physical_constants") $
(%i3) dimensionless([%h_bar, %m_e, %m_P, %%e, %c, %e_0]);
0 errors, 0 warnings
0 errors, 0 warnings
                              2
                           %%e        %m_e
(%o3)                [--------------, ----]
                      %c %e_0 %h_bar  %m_P
```

### Function: fundamental_units (fundamental_units, x, fundamental_units)

`fundamental_units(x)` returns the units
associated with the fundamental dimensions of *x*.
as determined by `dimensions(x)`.


*x* may be a literal dimensional expression $a ` b$,
a symbol with declared units via `declare_units`, 
or an expression containing either or both of those.


`fundamental_units()` returns the list of all known fundamental units,
as declared by `declare_fundamental_units`.


`load ("ezunits")` loads this function.


Examples:










```maxima
(%i1) load ("ezunits")$
(%i2) fundamental_units ();
(%o2)                 [m, kg, s, A, K, mol]
(%i3) fundamental_units (100 ` mile/hour);
                                m
(%o3)                           -
                                s
(%i4) declare_units (aa, g/foot^2);
                                g
(%o4)                         -----
                                  2
                              foot
(%i5) fundamental_units (aa);
                               kg
(%o5)                          --
                                2
                               m
```

### Function: natural_unit (expr, v_1, ..., v_n)

Finds exponents *e_1*, ..., *e_n* such that
`dimension(expr) = dimension(v_1^e_1 ... v_n^e_n)`.


`load ("ezunits")` loads this function.


Examples:





```maxima

```

### Function: qty (x)

Returns the nondimensional part of a dimensional quantity *x*,
or returns *x* if *x* is nondimensional.
*x* may be a literal dimensional expression $a ` b$,
a symbol with declared quantity, 
or an expression containing either or both of those.


This function should be loaded with `load ("ezunits")`.


Example:











```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                       100 ` kg
(%i3) qty (foo);
(%o3)                          100
(%i4) bar : v ` m/s;
                                  m
(%o4)                         v ` -
                                  s
(%i5) foo * bar;
                                  kg m
(%o5)                     100 v ` ----
                                   s
(%i6) qty (foo * bar);
(%o6)                         100 v
```

### Function: remove_constvalue (a)

Reverts the effect of `declare_005fconstvalue`. This function should be
loaded with `load ("ezunits")`.

See also: `declare_constvalue`.

### Function: remove_dimensions (a_1, ..., a_n)

Reverts the effect of `declare_dimensions`. This function should be
loaded with `load ("ezunits")`.

### Function: unitp (x)

Returns `true` if *x* is a literal dimensional expression,
a symbol declared dimensional,
or an expression in which the main operator is declared dimensional.
`unitp` returns `false` otherwise.


`load ("ezunits")` loads this function.


Examples:


`unitp` applied to a literal dimensional expression.







```maxima
(%i1) load ("ezunits")$
(%i2) unitp (100 ` kg);
(%o2)                         true
```


`unitp` applied to a symbol declared dimensional.









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (foo);
(%o2)                         false
(%i3) declare (foo, dimensional);
(%o3)                         done
(%i4) unitp (foo);
(%o4)                         true
```


`unitp` applied to an expression in which the main operator is declared dimensional.









```maxima
(%i1) load ("ezunits")$
(%i2) unitp (bar (x, y, z));
(%o2)                         false
(%i3) declare (bar, dimensional);
(%o3)                         done
(%i4) unitp (bar (x, y, z));
(%o4)                         true
```

### Function: units (x)

Returns the units of a dimensional quantity *x*,
or returns 1 if *x* is nondimensional.


*x* may be a literal dimensional expression $a ` b$,
a symbol with declared units via `declare_units`, 
or an expression containing either or both of those.


This function should be loaded with `load ("ezunits")`.


Example:













```maxima
(%i1) load ("ezunits")$
(%i2) foo : 100 ` kg;
(%o2)                       100 ` kg
(%i3) bar : x ` m/s;
                                  m
(%o3)                         x ` -
                                  s
(%i4) units (foo);
(%o4)                          kg
(%i5) units (bar);
                                m
(%o5)                           -
                                s
(%i6) units (foo * bar);
                              kg m
(%o6)                         ----
                               s
(%i7) units (foo / bar);
                              kg s
(%o7)                         ----
                               m
(%i8) units (foo^2);
                                 2
(%o8)                          kg
```

