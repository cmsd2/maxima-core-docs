## unit

### Variable: %unitexpand

Default value: `2`


This is the value supplied to `metricexpandall` during the initial loading
of *unit*.

### Function: convert (expr, list)

When resetting the global environment is overkill, there is the `convert`
command, which allows one time conversions.  It can accept either a single
argument or a list of units to use in conversion.  When a convert operation is
done, the normal global evaluation system is bypassed, in order to avoid the
desired result being converted again.  As a consequence, for inexact calculations
"rat" warnings will be visible if the global environment controlling this behavior
(`ratprint`) is true.  This is also useful for spot-checking the
accuracy of a global conversion.  Another feature is `convert` will allow a
user to do Base Dimension conversions even if the global environment is set to
simplify to a Derived Dimension.



```maxima
(%i2) kg*m/s^2;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) convert(kg*m/s^2,[g,km,s]);
                                     g km
(%o3)                                ----
                                       2
                                      s


(%i4) convert(kg*m/s^2,[g,inch,minute]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                              18000000000   %in g
(%o4)                        (-----------) (-----)
                                  127           2
                                            %min


(%i5) convert(kg*m/s^2,[N]);
(%o5)                                  N


(%i6) convert(kg*m^2/s^2,[N]);
(%o6)                                 m N


(%i7) setunits([N,J]);
(%o7)                                done


(%i8) convert(kg*m^2/s^2,[N]);
(%o8)                                 m N


(%i9) convert(kg*m^2/s^2,[N,inch]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                 5000
(%o9)                           (----) (%in N)
                                 127


(%i10) convert(kg*m^2/s^2,[J]);
(%o10)                                 J


(%i11) kg*m^2/s^2;
(%o11)                                 J


(%i12) setunits([g,inch,s]);
(%o12)                               done


(%i13) kg*m/s^2;
(%o13)                                 N


(%i14) uforget(N);
(%o14)                               false


(%i15) kg*m/s^2;
                                5000000   %in g
(%o15)                         (-------) (-----)
                                  127       2
                                           s


(%i16) convert(kg*m/s^2,[g,inch,s]);

`rat' replaced 39.37007874015748 by 5000/127 = 39.37007874015748
                                5000000   %in g
(%o16)                         (-------) (-----)
                                  127       2
                                           s
```


See also `setunits` and `uforget`. To use this function write first `load("unit")`.

See also: `setunits`, `uforget`.

### Function: metricexpandall (x)

Rebuilds global unit lists automatically creating all desired metric units.
*x* is a numerical argument which is used to specify how many metric
prefixes the user wishes defined.  The arguments are as follows, with each
higher number defining all lower numbers’ units:


```maxima
0 - none. Only base units
           1 - kilo, centi, milli
(default)  2 - giga, mega, kilo, hecto, deka, deci, centi, milli,
               micro, nano
           3 - peta, tera, giga, mega, kilo, hecto, deka, deci,
               centi, milli, micro, nano, pico, femto
           4 - all
```

Normally, Maxima will not define the full expansion since this results in a
very large number of units, but `metricexpandall` can be used to
rebuild the list in a more or less complete fashion. The relevant variable
in the *unit.mac* file is *%unitexpand*.

### Function: setunits (list)

By default, the *unit* package does not use any derived dimensions, but will
convert all units to the seven fundamental dimensions using MKS units.


```maxima
(%i2) N;
                                     kg m
(%o2)                                ----
                                       2
                                      s


(%i3) dyn;
                                   1      kg m
(%o3)                           (------) (----)
                                 100000     2
                                           s


(%i4) g;
                                    1
(%o4)                             (----) (kg)
                                   1000


(%i5) centigram*inch/minutes^2;
                                  127        kg m
(%o5)                       (-------------) (----)
                             1800000000000     2
                                              s
```


In some cases this is the desired behavior.  If the user wishes to use other
units, this is achieved with the `setunits` command:


```maxima
(%i6) setunits([centigram,inch,minute]);
(%o6)                                done


(%i7) N;
                            1800000000000   %in cg
(%o7)                      (-------------) (------)
                                 127            2
                                            %min


(%i8) dyn;
                               18000000   %in cg
(%o8)                         (--------) (------)
                                 127          2
                                          %min


(%i9) g;
(%o9)                             (100) (cg)


(%i10) centigram*inch/minutes^2;
                                    %in cg
(%o10)                              ------
                                        2
                                    %min
```


The setting of units is quite flexible.  For example, if we want to
get back to kilograms, meters, and seconds as defaults for those
dimensions we can do:


```maxima
(%i11) setunits([kg,m,s]);
(%o11)                               done


(%i12) centigram*inch/minutes^2;
                                  127        kg m
(%o12)                      (-------------) (----)
                             1800000000000     2
                                              s
```


Derived units are also handled by this command:


```maxima
(%i17) setunits(N);
(%o17)                               done


(%i18) N;
(%o18)                                 N


(%i19) dyn;
                                    1
(%o19)                           (------) (N)
                                  100000


(%i20) kg*m/s^2;
(%o20)                                 N


(%i21) centigram*inch/minutes^2;
                                    127
(%o21)                        (-------------) (N)
                               1800000000000
```


Notice that the *unit* package recognized the non MKS combination
of mass, length, and inverse time squared as a force, and converted it
to Newtons.  This is how Maxima works in general.  If, for example, we
prefer dyne to Newtons, we simply do the following:


```maxima
(%i22) setunits(dyn);
(%o22)                               done


(%i23) kg*m/s^2;
(%o23)                          (100000) (dyn)


(%i24) centigram*inch/minutes^2;
                                  127
(%o24)                         (--------) (dyn)
                                18000000
```


To discontinue simplifying to any force, we use the uforget command:


```maxima
(%i26) uforget(dyn);
(%o26)                               false


(%i27) kg*m/s^2;
                                     kg m
(%o27)                               ----
                                       2
                                      s


(%i28) centigram*inch/minutes^2;
                                  127        kg m
(%o28)                      (-------------) (----)
                             1800000000000     2
                                              s
```

This would have worked equally well with `uforget(N)` or
`uforget(%force)`.


See also `uforget`. To use this function write first `load("unit")`.

See also: `uforget`.

### Function: uforget (list)

By default, the *unit* package converts all units to the
seven fundamental dimensions using MKS units. This behavior can
be changed with the `setunits` command. After that, the
user can restore the default behavior for a particular dimension
by means of the `uforget` command:


```maxima
(%i13) setunits([centigram,inch,minute]);
(%o13)                               done


(%i14) centigram*inch/minutes^2;
                                    %in cg
(%o14)                              ------
                                        2
                                    %min


(%i15) uforget([cg,%in,%min]);
(%o15)                      [false, false, false]


(%i16) centigram*inch/minutes^2;
                                  127        kg m
(%o16)                      (-------------) (----)
                             1800000000000     2
                                              s
```


`uforget` operates on dimensions,
not units, so any unit of a particular dimension will work.  The
dimension itself is also a legal argument.


See also `setunits`. To use this function write first `load("unit")`.

See also: `setunits`.

### Variable: usersetunits

Default value: none


If a user wishes to have a default unit behavior other than that described,
they can make use of *maxima-init.mac* and the *usersetunits*
variable.  The *unit* package will check on startup to see if this variable
has been assigned a list.  If it has, it will use setunits on that list and take
the units from that list to be defaults.  `uforget` will revert to the behavior
defined by usersetunits over its own defaults.  For example, if we have a
*maxima-init.mac* file containing:


```maxima
usersetunits : [N,J];
```

we would see the following behavior:


```maxima
(%i1) load("unit")$
*******************************************************************
*                       Units version 0.50                        *
*          Definitions based on the NIST Reference on             *
*              Constants, Units, and Uncertainty                  *
*       Conversion factors from various sources including         *
*                   NIST and the GNU units package                *
*******************************************************************

Redefining necessary functions...
WARNING: DEFUN/DEFMACRO: redefining function
 TOPLEVEL-MACSYMA-EVAL ...
WARNING: DEFUN/DEFMACRO: redefining function MSETCHK ...
WARNING: DEFUN/DEFMACRO: redefining function KILL1 ...
WARNING: DEFUN/DEFMACRO: redefining function NFORMAT ...
Initializing unit arrays...
Done.
User defaults found...
User defaults initialized.


(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) kg*m^3/s^2;
(%o4)                                 J m


(%i5) kg*m*km/s^2;
(%o5)                             (1000) (J)


(%i6) setunits([dyn,eV]);
(%o6)                                done


(%i7) kg*m/s^2;
(%o7)                           (100000) (dyn)


(%i8) kg*m^2/s^2;
(%o8)                     (6241509596477042688) (eV)


(%i9) kg*m^3/s^2;
(%o9)                    (6241509596477042688) (eV m)


(%i10) kg*m*km/s^2;
(%o10)                   (6241509596477042688000) (eV)


(%i11) uforget([dyn,eV]);
(%o11)                           [false, false]


(%i12) kg*m/s^2;
(%o12)                                 N


(%i13) kg*m^2/s^2;
(%o13)                                 J


(%i14) kg*m^3/s^2;
(%o14)                                J m


(%i15) kg*m*km/s^2;
(%o15)                            (1000) (J)
```

Without `usersetunits`, the initial inputs would have been converted
to MKS, and uforget would have resulted in a return to MKS rules.  Instead,
the user preferences are respected in both cases.  Notice these can still
be overridden if desired.  To completely eliminate this simplification - i.e.
to have the user defaults reset to factory defaults - the `dontusedimension`
command can be used.  `uforget` can restore user settings again, but
only if `usedimension` frees it for use.  Alternately,
`kill(usersetunits)` will completely remove all knowledge of the user defaults
from the session.  Here are some examples of how these various options work.


```maxima
(%i2) kg*m/s^2;
(%o2)                                  N


(%i3) kg*m^2/s^2;
(%o3)                                  J


(%i4) setunits([dyn,eV]);
(%o4)                                done


(%i5) kg*m/s^2;
(%o5)                           (100000) (dyn)


(%i6) kg*m^2/s^2;
(%o6)                     (6241509596477042688) (eV)


(%i7) uforget([dyn,eV]);
(%o7)                          [false, false]


(%i8) kg*m/s^2;
(%o8)                                  N


(%i9) kg*m^2/s^2;
(%o9)                                  J


(%i10) dontusedimension(N);
(%o10)                             [%force]


(%i11) dontusedimension(J);
(%o11)                         [%energy, %force]


(%i12) kg*m/s^2;
                                     kg m
(%o12)                               ----
                                       2
                                      s


(%i13) kg*m^2/s^2;
                                         2
                                     kg m
(%o13)                               -----
                                       2
                                      s


(%i14) setunits([dyn,eV]);
(%o14)                               done


(%i15) kg*m/s^2;
                                     kg m
(%o15)                               ----
                                       2
                                      s


(%i16) kg*m^2/s^2;
                                         2
                                     kg m
(%o16)                               -----
                                       2
                                      s


(%i17) uforget([dyn,eV]);
(%o17)                         [false, false]


(%i18) kg*m/s^2;
                                     kg m
(%o18)                               ----
                                       2
                                      s


(%i19) kg*m^2/s^2;
                                         2
                                     kg m
(%o19)                               -----
                                       2
                                      s


(%i20) usedimension(N);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o20)                               true


(%i21) usedimension(J);
Done.  To have Maxima simplify to this dimension, use
setunits([unit]) to select a unit.
(%o21)                               true


(%i22) kg*m/s^2;
                                     kg m
(%o22)                               ----
                                       2
                                      s


(%i23) kg*m^2/s^2;
                                         2
                                     kg m
(%o23)                               -----
                                       2
                                      s


(%i24) setunits([dyn,eV]);
(%o24)                               done


(%i25) kg*m/s^2;
(%o25)                          (100000) (dyn)


(%i26) kg*m^2/s^2;
(%o26)                    (6241509596477042688) (eV)


(%i27) uforget([dyn,eV]);
(%o27)                           [false, false]


(%i28) kg*m/s^2;
(%o28)                                 N


(%i29) kg*m^2/s^2;
(%o29)                                 J


(%i30) kill(usersetunits);
(%o30)                               done


(%i31) uforget([dyn,eV]);
(%o31)                          [false, false]


(%i32) kg*m/s^2;
                                     kg m
(%o32)                               ----
                                       2
                                      s


(%i33) kg*m^2/s^2;
                                         2
                                     kg m
(%o33)                               -----
                                       2
                                      s
```

Unfortunately this wide variety of options is a little confusing at first,
but once the user grows used to them they should find they have very full
control over their working environment.

