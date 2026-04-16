## finance

### Function: amortization (rate, amount, num)

Amortization table determined by a specific rate.
*rate* is the interest rate, *amount* is the amount value,
and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) amortization(0.05,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     52481.777      2800.000      3518.223      6318.223  
     2.000     48787.643      2624.089      3694.134      6318.223  
     3.000     44908.802      2439.382      3878.841      6318.223  
     4.000     40836.019      2245.440      4072.783      6318.223  
     5.000     36559.597      2041.801      4276.422      6318.223  
     6.000     32069.354      1827.980      4490.243      6318.223  
     7.000     27354.599      1603.468      4714.755      6318.223  
     8.000     22404.106      1367.730      4950.493      6318.223  
     9.000     17206.088      1120.205      5198.018      6318.223  
    10.000     11748.170       860.304      5457.919      6318.223  
    11.000      6017.355       587.408      5730.814      6318.223  
    12.000         0.000       300.868      6017.355      6318.223
```

### Function: annuity_fv (rate, FV, num)

We can calculate the annuity knowing the desired value (future value),
it is a constant and periodic payment. *rate* is the interest rate,
*FV* is the future value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) annuity_fv(0.12,65000,10);
(%o2)                3703.970670389863
```

### Function: annuity_pv (rate, PV, num)

We can calculate the annuity knowing the present value (like an amount),
it is a constant and periodic payment. *rate* is the interest rate,
*PV* is the present value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) annuity_pv(0.12,5000,10);
(%o2)                884.9208207992202
```

### Function: arit_amortization (rate, increment, amount, num)

The amortization table determined by a specific rate and with growing payment
can be calculated by `arit_amortization`.
Notice that the payment is not constant, it presents
an arithmetic growing, increment is then the difference between two
consecutive rows in the "Payment" column.
*rate* is the interest rate, *increment* is the increment, *amount*
is the amount value, and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) arit_amortization(0.05,1000,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     57403.679      2800.000     -1403.679      1396.321  
     2.000     57877.541      2870.184      -473.863      2396.321  
     3.000     57375.097      2893.877       502.444      3396.321  
     4.000     55847.530      2868.755      1527.567      4396.321  
     5.000     53243.586      2792.377      2603.945      5396.321  
     6.000     49509.443      2662.179      3734.142      6396.321  
     7.000     44588.594      2475.472      4920.849      7396.321  
     8.000     38421.703      2229.430      6166.892      8396.321  
     9.000     30946.466      1921.085      7475.236      9396.321  
    10.000     22097.468      1547.323      8848.998     10396.321  
    11.000     11806.020      1104.873     10291.448     11396.321  
    12.000        -0.000       590.301     11806.020     12396.321
```

### Function: benefit_cost (rate, input, output)

Calculates the ratio Benefit/Cost. Benefit is the Net Present Value (NPV)
of the inputs, and Cost is the Net Present Value (NPV) of the outputs.
Notice that if there is not an input or output value in a specific period,
the input/output would be a zero for that period.
*rate* is the interest rate, *input* is a list of input values,
and *output* is a list of output values.


Example:



```maxima
(%i1) load("finance")$
(%i2) benefit_cost(0.24,[0,300,500,150],[100,320,0,180]);
(%o2)               1.427249324905784
```

### Function: days360 (year1, month1, day1, year2, month2, day2)

Calculates the distance between 2 dates, assuming 360 days years, 30 days months.


Example:



```maxima
(%i1) load("finance")$
(%i2) days360(2008,12,16,2007,3,25);
(%o2)                      - 621
```

### Function: fv (rate, PV, num)

We can calculate the future value of a Present one given a certain interest rate.
*rate* is the interest rate, *PV* is the present value and *num* is
the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) fv(0.12,1000,3);
(%o2)                     1404.928
```

### Function: geo_amortization (rate, growing_rate, amount, num)

The amortization table determined by rate, amount,
and number of periods can be found by `geo_amortization`.
Notice that the payment is not constant, it presents
a geometric growing, *growing_rate* is then the quotient between two
consecutive rows in the "Payment" column.
*rate* is the interest rate, *amount*
is the amount value, and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_amortization(0.05,0.03,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     53365.296      2800.000      2634.704      5434.704  
     2.000     50435.816      2668.265      2929.480      5597.745  
     3.000     47191.930      2521.791      3243.886      5765.677  
     4.000     43612.879      2359.596      3579.051      5938.648  
     5.000     39676.716      2180.644      3936.163      6116.807  
     6.000     35360.240      1983.836      4316.475      6300.311  
     7.000     30638.932      1768.012      4721.309      6489.321  
     8.000     25486.878      1531.947      5152.054      6684.000  
     9.000     19876.702      1274.344      5610.176      6884.520  
    10.000     13779.481       993.835      6097.221      7091.056  
    11.000      7164.668       688.974      6614.813      7303.787  
    12.000         0.000       358.233      7164.668      7522.901
```

### Function: geo_annuity_fv (rate, growing_rate, FV, num)

We can calculate the annuity knowing the desired value (future value),
in a growing periodic payment. *rate* is the interest rate, *growing_rate*
is the growing rate, *FV* is the future value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_annuity_fv(0.14,0.05,5000,10);
(%o2)                216.5203395312695
```

### Function: geo_annuity_pv (rate, growing_rate, PV, num)

We can calculate the annuity knowing the present value (like an amount),
in a growing periodic payment. *rate* is the interest rate, *growing_rate*
is the growing rate, *PV* is the present value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_annuity_pv(0.14,0.05,5000,10);
(%o2)                802.6888176505123
```

### Function: graph_flow (val)

Plots the money flow in a time line, the positive values are in blue
and upside; the negative ones are in red and downside.
The direction of the flow is given by the sign of the value.
*val* is a list of flow values.


Example:



```maxima
(%i1) load("finance")$
(%i2) graph_flow([-5000,-3000,800,1300,1500,2000])$
```

### Function: irr (val, IO)

IRR (Internal Rate of Return) is the value of rate which makes Net Present Value
zero.
*flowValues* is a list of varying cash flows,
*I0* is the initial investment.


Example:



```maxima
(%i1) load("finance")$
(%i2) res:irr([-5000,0,800,1300,1500,2000],0)$
(%i3) rhs(res[1][1]);
(%o3)                .03009250374237132
```

### Function: npv (rate, val)

Calculates the present value of a value series to evaluate the viability in a
project.
*val* is a list of varying cash flows.


Example:



```maxima
(%i1) load("finance")$
(%i2) npv(0.25,[100,500,323,124,300]);
(%o2)                714.4703999999999
```

### Function: pv (rate, FV, num)

We can calculate the present value of a Future one given a certain interest rate.
*rate* is the interest rate, *FV* is the future value and *num* is
the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) pv(0.12,1000,3);
(%o2)                711.7802478134108
```

### Function: saving (rate, amount, num)

The table that represents the values in a constant and periodic
saving can be found by `saving`.
*amount* represents the desired quantity and num the number
of periods to save.


Example:



```maxima
(%i1) load("finance")$
(%i2) saving(0.15,12000,15)$
      "n"    "Balance"     "Interest"   "Payment"      
     0.000         0.000         0.000         0.000  
     1.000       252.205         0.000       252.205  
     2.000       542.240        37.831       252.205  
     3.000       875.781        81.336       252.205  
     4.000      1259.352       131.367       252.205  
     5.000      1700.460       188.903       252.205  
     6.000      2207.733       255.069       252.205  
     7.000      2791.098       331.160       252.205  
     8.000      3461.967       418.665       252.205  
     9.000      4233.467       519.295       252.205  
    10.000      5120.692       635.020       252.205  
    11.000      6141.000       768.104       252.205  
    12.000      7314.355       921.150       252.205  
    13.000      8663.713      1097.153       252.205  
    14.000     10215.474      1299.557       252.205  
    15.000     12000.000      1532.321       252.205
```

