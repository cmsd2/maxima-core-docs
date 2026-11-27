## Grafische Darstellung

<!-- category: Other -->
<!-- keywords: adapt_depth -->
<!-- signatures: adapt_depth[adapt_depth, integer] -->
### Variable: adapt_depth

Standardwert: `5`




Die maximale Zahl an Teilungen von Intervallen, die der adaptive Algorithmus 
fur das Zeichnen eines Graphen vornimmt.  Zusammen mit der Grafikoption
`nticks` hat diese Grafikoption Einfluss darauf, wie glatt der Graph
gezeichnet wird.

See also: `nticks`.

<!-- category: Other -->
<!-- keywords: axes -->
<!-- signatures: axes[axes, symbol] -->
### Variable: axes

Standardwert: `true`








`symbol` kann einen der Werte `true`, `false`, `x` oder
`y` annehmen.  Ist der Wert `false`, werden keine Achsen gezeichnet.  
Mit `x` oder `y` werden nur die x- oder nur die y-Achse gezeichnet.  
Mit `true` werden beide Achsen gezeichnet.  Diese Option wird nur von den
Funktionen `plot2d` und `implicit_plot` beachtet.

See also: `plot2d`, `implicit_plot`.

<!-- category: Other -->
<!-- keywords: azimuth -->
<!-- signatures: azimuth[azimuth, number] -->
### Variable: azimuth

Standardwert: `30`









Setzt den Wert des Azimutwinkels in Grad fur die Ansicht einer 
dreidimensionalen Grafik.  Siehe auch `elevation`.

See also: `elevation`.

<!-- category: Other -->
<!-- keywords: color -->
<!-- signatures: color[color, color_1, ..., color_n] -->
### Variable: color

Standardwert: `[blue, red, green, magenta, black, cyan]`








Wenn die Funktionen `plot2d` oder `implicit_plot` mehrere Graphen
zeichnen, definiert die Grafikoption `color` die Farben der einzelnen 
Graphen.  Fur einen 3D-Graphen mit der Funktion `plot3d` definiert die
Grafikoption `color` die Farbe der Flachen.










Gibt es mehr Kurven oder Flachen als Farben, werden die Farben wiederholt.
Im Grafikformat Gnuplot konnen nur die Farben `blue`, `red`, 
`green`, `magenta`, `black`, `cyan` verwendet werden.  Im 
Grafikformat Xmaxima konnen die Farben auch als eine Zeichenkette angegeben 
werden, die mit dem Zeichen # beginnt und auf dem sechs hexadezimale Zahlenwerte
folgen.  Je zwei Werte bezeichnen die rote, grune und blaue Komponente der 
Farbe.


Siehe auch `style`.

See also: `plot2d`, `implicit_plot`, `plot3d`, `style`.

<!-- category: Other -->
<!-- keywords: colorbox -->
<!-- signatures: colorbox[colorbox, symbol] -->
### Variable: colorbox

Standardwert: `false`








Hat die Grafikoption `colorbox` den Wert `true`, wird immer dann,
wenn das Grafikkommando `plot3d` eine Palette mit verschiedenen Farben
nutzt, um die z-Werte darzustellen, eine Legende mit den Farben und den
dazugehorenden z-Werten angezeigt.

See also: `plot3d`.

<!-- category: Other -->
<!-- keywords: contour_plot -->
<!-- signatures: contour_plot(expr, x_range, y_range, options, ...) -->
### Function: contour_plot (expr, x_range, y_range, options, ...)

Zeichnet einen Konturgraphen (die Isolinien einer Funktion) von *expr* im 
Bereich *x_range* und *y_range* mit den Optionen *options*. 
*expr* ist ein Ausdruck oder der Name einer Funktion `f(x,y)` mit zwei
Argumenten.  Alle weiteren Argumente entsprechen denen der Funktion 
`plot3d`.







Die Funktion steht nur fur die Grafikformate `gnuplot` und 
`gnuplot_pipes` zur Verfugung.  Das Paket `implicit_plot` enthalt
die Funktion `implicit_plot` mit der fur alle Grafikformate Konturgraphen
erstellt werden konnen.


Beispiele:






```maxima
(%i1) contour_plot(x^2 + y^2, [x, -4, 4], [y, -4, 4])$
```

![./figures/plotting1](./figures/plotting1.png)






Es kann jede Option genutzt werden, die von der Funktion `plot3d` 
akzeptiert wird.  Standardmaßig zeichnet Gnuplot den Graphen mit 3 
Isolinien.  Die Anzahl der Isolinien kann mit der Gnuplot-Option 
`gnuplot_preamble` erhoht werden.  In diesem Beispiel werden 12 Isolinien
gezeichnet und die Legende ist entfernt.








```maxima
(%i1) contour_plot (u^3 + v^2, [u, -4, 4], [v, -4, 4],
              [legend,false],
              [gnuplot_preamble, "set cntrparam levels 12"])$
```

![./figures/plotting2](./figures/plotting2.png)

See also: `plot3d`, `implicit_plot`, `gnuplot_preamble`.

<!-- category: Other -->
<!-- keywords: elevation -->
<!-- signatures: elevation[elevation, number] -->
### Variable: elevation

Standardwert: `60`









Setzt den Wert des Elevationswinkels in Grad fur die Ansicht einer 
dreidimensionalen Grafik.  Siehe auch `azimuth`.

See also: `azimuth`.

<!-- category: Other -->
<!-- keywords: get_plot_option -->
<!-- signatures: get_plot_option(keyword, index) -->
### Function: get_plot_option (keyword, index)

Gibt die Werte der Parameter der Option mit dem Namen *keyword* zuruck. 
Die Optionen und ihre Parameter sind in der Variablen `plot_options` 
gespeichert.  Hat *index* den Wert 1 wird der Name der Option *keyword*
zuruckgeben.  Der Wert 2 fur *index* gibt den Wert des ersten Parameters
zuruck, und so weiter.





Siehe auch `plot_options`, `set_plot_option` und das Kapitel
Grafikoptionen.


Beispiel:








```maxima
(%i1) get_plot_option(color,1);
(%o1)                         color
(%i2) get_plot_option(color,2);
(%o2)                         blue
(%i3) get_plot_option(color,3);
(%o3)                          red
```

See also: `plot_options`, `set_plot_option`.

<!-- category: Other -->
<!-- keywords: grid -->
<!-- signatures: grid[grid, integer, integer] -->
### Variable: grid

Standardwert: `[30, 30]`





Setzt die Anzahl der Gitterlinen fur die x- und y-Achsen einer 
dreidimensionalen Grafik.

<!-- category: Other -->
<!-- keywords: implicit_plot -->
<!-- signatures: implicit_plot(expr, x_range, y_range), implicit_plot([expr_1, ..., expr_n], x_range, y_range) -->
### Function: implicit_plot (expr, x_range, y_range)

Zeichnet den Graphen eines oder mehrerer Ausdrucke, die implizit gegeben sind.
*expr* ist der Ausdruck der gezeichnet werden soll, *x_range* ist der
Wertebereich der x-Achse und *y_range* der Wertebereich der y-Achse.  Die
Funktion `implicit_plot` beachtet die Werte der Parameter der 
Grafikoptionen, die in der Systemvariablen `plot_options` enthalten sind.
Grafikoptionen konnen auch als Argumente ubergeben werden.






Der Algorithmus von `implicit_plot` stellt Vorzeichenwechsel der Funktion
in den Bereichen *x_range* und *y_range* fest.  Fur komplizierte
Flachen kann der Algorithmus versagen.




Die Funktion wird mit dem Kommando `load("implicit_plot")` geladen.


Beispiel:







```maxima
(%i1) load("implicit_plot")$
(%i2) implicit_plot (x^2 = y^3 - 3*y + 1, [x, -4, 4], [y, -4, 4])$
```


![./figures/plotting3](./figures/plotting3.png)

<!-- category: Other -->
<!-- keywords: legend -->
<!-- signatures: legend[legend, string_1, ..., string_n], legend[legend, false] -->
### Variable: legend

Definiert die Eintrage einer Legende, wenn mehrere Graphen gezeichnet 
werden.  Sind mehr Graphen als Eintrage vorhanden, werden die Eintrage 
wiederholt.  Hat die Grafikoption `legend` den Wert `false`, wird 
keine Legende gezeichnet.  Standardmaßig werden die Ausdrucke oder Namen
der Funktionen als Eintrage verwendet.  Fur diskrete Grafiken werden die 
Eintrage mit discrete1, discrete2, ... bezeichnet.  Diese Grafikoption 
kann nicht mit der Funktion `set_plot_option` gesetzt werden.

<!-- category: Other -->
<!-- keywords: logx -->
<!-- signatures: logx[logx] -->
### Variable: logx

Bewirkt, dass die horizontale Achse logarithmisch skaliert wird.  Diese 
Grafikoption kann nicht mit der Funktion `set_plot_option` gesetzt werden.
Siehe auch `logy`.

See also: `logy`.

<!-- category: Other -->
<!-- keywords: logy -->
<!-- signatures: logy[logy] -->
### Variable: logy

Bewirkt, dass die vertikale Achse logarithmisch skaliert wird.  Diese 
Grafikoption kann nicht mit der Funktion `set_plot_option` gesetzt werden.
Siehe auch `logx`.

See also: `logx`.

<!-- category: Other -->
<!-- keywords: make_transform -->
<!-- signatures: make_transform([var1, var2, var3], fx, fy, fz) -->
### Function: make_transform ([var1, var2, var3], fx, fy, fz)

Gibt eine Funktion zuruck, die als Parameter fur die Grafikoption 
`transform_xy` geeignet ist.  Die zwei Argumente *var1* und *var2* 
reprasentieren die zwei unabhangigen Variablen der Funktion `plot3d`.  
Das dritte Argument *var3* ist die Funktion, die von den zwei Variablen 
abhangt.  Die drei Funktionen *fx*, *fy* und *fz* mussen von 
den drei Argumenten *var1*, *var2* und *var3* abhangen und die 
Argumente der Funktion `plot3d` in kartesische Koordinaten fur die 
Ausgabe des Graphen transformieren. 


Die Transformationen `polar_to_xy` fur die Transformation von 
Polarkoordinaten und `spherical_to_xyz` fur die Transformation von 
Kugelkoordinaten in kartesische Koordinaten sind bereits definiert.


Beispiel:


Definition der Transformation von Zylinderkoordinaten nach kartesischen 
Koordinaten.  Die Definition ist identisch mit der fur `polar_to_xy`.
Der Graph zeigt einen Kegel.











```maxima
(%i1) cylinder_to_xy:make_transform([r,phi,z],r*cos(phi),
                                              r*sin(phi),z)$
(%i2) plot3d(-r,[r,0,3],[phi,0,2*%pi],
                        [transform_xy, cylinder_to_xy])$
```

See also: `polar_to_xy`, `spherical_to_xyz`.

<!-- category: Other -->
<!-- keywords: mesh_lines_color -->
<!-- signatures: mesh_lines_color[mesh_lines_color, color] -->
### Variable: mesh_lines_color

Standardwert: `black`







Setzt die Farbe, die von der Funktion `plot3d` genutzt wird, um die
Gitterlinien zu zeichnen.  Es konnen dieselben Farben verwendet werden wie 
fur die Grafikoption `color`. Hat `mesh_lines_color` Wert 
`false`, werden keine Gitterlinien gezeichnet.

See also: `color`.

<!-- category: Other -->
<!-- keywords: nticks -->
<!-- signatures: nticks[nticks, integer] -->
### Variable: nticks

Standardwert: `29`







Wird eine Grafik mit der Funktion `plot2d` gezeichnet, gibt `nticks`
die Anzahl der Anfangspunkte fur das Zeichnen der Grafik an.  Werden 
parametrische Kurven mit den Funktionen `plot2d` oder `plot3d`
gezeichnet, ist `nticks` die Anzahl der Punkte, fur die der Graph
gezeichnet wird.


Zusammen mit der Grafikoption `adapt_depth` hat diese Grafikoption Einfluss
darauf, wie glatt der Graph gezeichnet wird.

See also: `adapt_depth`.

<!-- category: Other -->
<!-- keywords: palette -->
<!-- signatures: palette[palette, [palette_1], ..., [palette_n]], palette[palette, false] -->
### Variable: palette

Standardwert: `[hue, 0.25, 0.7, 0.8, 0.5], [hue, 0.65, 0.8, 0.9, 0.55], [hue, 0.55, 0.8, 0.9, 0.4], [hue, 0.95, 0.7, 0.8, 0.5]`













Eine Palette kann aus einer oder einer Liste mit mehreren Paletten bestehen.  
Jede Palette beginnt mit einem Schlusselwort, worauf 4 Zahlen folgen.  Die 
ersten drei Zahlen haben Werte zwischen 0 und 1.  Diese definieren den Farbton 
`hue`, die Sattigung `saturation` und die Grundfarbe `value`, 
die der kleinste z-Wert erhalt.  Die Schlusselworte `hue`, 
`saturation` und `value` spezifizieren, welches der drei Attribute mit
dem Wert von z geandert werden.  Der letzte Wert der Liste, spezifiziert, 
welcher Wert zum großten z-Wert gehort.  Dieser großte Wert kann
großer als 1 und auch negativ sein.  Die Werte der modifizierten 
Attribute werden Modulo 1 gerundet.







Gnuplot verwendet nur die erste Palette in einer Liste mit Paletten.  Xmaxima 
nutzt alle Paletten nacheinander, wenn mehrere Flachen gezeichnet werden.  
Sind nicht genugend Paletten vorhanden, werden die Paletten wiederholt.








Die Farbe der Gitterlinien wird mit der Option `mesh_lines_color`
angegeben.  Hat `palette` den Wert `false`, werden die Flachen nicht
gefarbt, sondern als ein Gitternetz gezeichnet.  Die Farbe der Gitterlinien
wird in diesem Fall mit der Grafikoption `color` festgelegt.

See also: `mesh_lines_color`, `color`.

<!-- category: Other -->
<!-- keywords: plot2d -->
<!-- signatures: plot2d(plot, x_range, ..., options, ...), plot2d([plot_1, ..., plot_n], ..., options, ...), plot2d([plot_1, ..., plot_n], x_range, ..., options, ...) -->
### Function: plot2d (plot, x_range, ..., options, ...)

*plot*, *plot_1*, ..., *plot_n* sind Ausdrucke, Namen von 
Funktionen oder Listen, mit denen diskrete Punkte oder Funktionen in einer
parametrischen Darstellung angegeben werden.  Diskrete Punkte konnen als
`[discrete, [x1, ..., xn], [y1, ..., yn]]` oder als 
`[discrete, [[x1, y1], ..., [xn, ..., yn]]`
angegeben werden.  Eine parametrische Darstellung hat die Form
`[parametric, x_expr, y_expr, t_range]`.











Die Funktion `plot2d` zeichnet einen zweidimensionalen Graphen einer oder 
mehrerer Ausdrucke als Funktion einer Variablen oder eines Parameters.  Mit 
der Grafikoption *x_range* wird der Name der unabhangigen Variablen und 
deren Bereich angegeben.  Die Syntax der Grafikoption *x_range* ist: 
`[variable, min, max]`.












Ein diskreter Graph wird durch eine Liste definiert, die mit dem
Schlusselwort *disrecte* beginnt.  Es folgen ein oder zwei Listen mit 
den Werten.  Werden zwei Listen ubergeben, mussen diese dieselbe Lange 
haben.  Die Daten der ersten Listen werden als die x-Koordinaten der Punkte und 
die der zweiten als die y-Koordinaten der Punkte interpretiert.  Wird nur eine 
Liste ubergeben, sind die Elemente Listen mit je zwei Elementen, die die x- 
und y-Koordinaten der Punkte reprasentieren.










Ein parametrischer Graph wird durch eine Liste definiert, die mit dem
Schlusselwort *parametric* beginnt.  Es folgen zwei Ausdrucke oder 
Namen von Funktionen und ein Parameter.  Der Bereich fur den Parameter muss 
eine Liste sein, die den Namen des Parameters, seinen großten und seinen 
kleinsten Wert enthalt: `[parameter, min, max]`.  Der 
Graph ist der Weg fur die zwei Ausdrucke oder Namen von Funktionen, wenn 
der Parameter *parameter* von *min* nach *max* zunimmt.










Als optionales Argument kann ein Wertebereich fur die vertikale 
Koordinatenachse mit der Grafikoption `y` angegeben werden: 
`[y, min, max]`.  Die vertikale Achse wird immer mit dem 
Schlusselwort `y` bezeichnet.  Wird kein Wertebereich `y` angegeben, 
wird dieser durch den großten und kleinsten `y`-Wert des zu 
zeichnenden Graphen festgelegt.





Auch alle anderen Grafikoptionen werden als Listen angegeben, die mit einem 
Schlusselwort beginnen, auf das die Parameter der Grafikoption folgen.  Siehe 
`plot_options`.








Werden mehrere Graphen gezeichnet, wird eine Legende hinzugefugt, die die 
einzelnen Graphen unterscheidet.  Mit der Grafikoption *legend* konnen die
Bezeichnungen fur die Legende festgelegt werden.  Wird diese Option nicht 
genutzt, generiert Maxima die Bezeichnungen der Legende aus den Ausdrucken 
oder Namen der Funktionen, die als Argument ubergeben wurden.




Siehe auch das Kapitel `Grafikoptionen`.


Beispiele:




Graph einer einfachen Funktion.






```maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


![./figures/plotting6](./figures/plotting6.png)




Wachst die Funktion sehr schnell, kann es notwendig sein, die Werte auf der
vertikalen Achse mit der Grafikoption `y` zu begrenzen.






```maxima
(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
```


![./figures/plotting7](./figures/plotting7.png)





Die Ansicht eines Graphen kann sich fur verschiedene Grafikprogramme
unterscheiden.  In Xmaxima bewirkt die Grafikoption `[box, false]`, das die
Koordinatenachsen mit Pfeilen dargestellt werden.









```maxima
(%i1) plot2d ( x^2 - 1, [x, -3, 3], [box, false], grid2d,
      [yx_ratio, 1], [axes, solid], [xtics, -2, 4, 2],
      [ytics, 2, 2, 6], [label, ["x", 2.9, -0.3],
      ["x^2-1", 0.1, 8]], [title, "A parabola"])$
```


![./figures/plotting8](./figures/plotting8.png)



Ein Graph mit einer logarithmischen Skala:






```maxima
(%i1) plot2d (exp(3*s), [s, -2, 2], logy)$
```


![./figures/plotting9](./figures/plotting9.png)



Graphen von Funktionen, deren Namen als Argumente ubergeben werden.









```maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


![./figures/plotting10](./figures/plotting10.png)



Graph einer parametrisch definierten Schmetterlingskurve.







```maxima
(%i1) r: (exp(cos(t))-2*cos(4*t)-sin(t/12)^5)$
(%i2) plot2d([parametric, r*sin(t), r*cos(t), [t, -8*%pi, 8*%pi]])$
```


![./figures/plotting11](./figures/plotting11.png)





Graph der Funktion `abs(x)` und eines parametrischen Kreises.  Das 
Seitenverhaltnis der Grafik wurde mit den Grafikoptionen `same_xy`.







```maxima
(%i1) plot2d([[parametric, cos(t), sin(t), [t,0,2*%pi]], -abs(x)],
         [x, -sqrt(2), sqrt(2)], same_xy)$
```


![./figures/plotting12](./figures/plotting12.png)



Graph fur diskrete Punkte.  Die Punkte sind in zwei separaten Listen jeweils 
fur die x- und y-Koordinaten angegeben.  Standardmaßig werden die Punkte
mit einer Linie verbunden.







```maxima
(%i1) plot2d ([discrete, makelist(i*%pi, i, 1, 5),
                            [0.6, 0.9, 0.2, 1.3, 1]])$
```


![./figures/plotting14](./figures/plotting14.png)





In diesem Beispiel wird eine Tabelle mit drei Spalten in eine Datei 
`data.txt` gespeichert.  Die Datei wird gelesen und die zweite und dritte
Spalte werden gezeichnet.










```maxima
(%i1) with_stdout ("data.txt", for x:0 thru 10 do
                             print (x, x^2, x^3))$

(%i2) data: read_matrix ("data.txt")$

(%i3) plot2d ([discrete, transpose(data)[2], transpose(data)[3]],
  [style,points], [point_type,diamond], [color,red])$
```


![./figures/plotting15](./figures/plotting15.png)




Graph von experimentellen Datenpunkten zusammen mit einer theoretischen 
Funktion, die die Daten beschreibt.












```maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$

(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


![./figures/plotting16](./figures/plotting16.png)

See also: `plot_options`, `Grafikoptionen`.

<!-- category: Other -->
<!-- keywords: plot3d -->
<!-- signatures: plot3d(expr, x_range, y_range, ..., options, ...), plot3d([expr_1, ..., expr_n], x_range, y_range, ..., options, ...) -->
### Function: plot3d (expr, x_range, y_range, ..., options, ...)

Zeichnet einen Graph mit einer oder mehreren Flachen, die als eine Funktion
von zwei Variablen oder in parametrischer Form definiert sind.







Die zu zeichnenden Funktionen werden als Ausdrucke oder mit ihrem Namen als 
Argumente ubergeben.  Mit der Maus kann der Graph rotiert werden, 
um die Flache aus verschiedenen Blickwinkeln zu betrachten.




Siehe auch das Kapitel Grafikoptionen.


Beispiele:




Graph einer einfachen Funktion.







```maxima
(%i1) plot3d (u^2 - v^2, [u, -2, 2], [v, -3, 3], [grid, 100, 100],
        [mesh_lines_color,false])$
```


![./figures/plotting17](./figures/plotting17.png)





Mit der Grafikoption `z` wird der Wertebereich der z-Achse begrenzt. 
Dieses Beispiel zeigt den Graph ohne Farbung der Flache.







```maxima
(%i1) plot3d ( log ( x^2*y^2 ), [x, -2, 2], [y, -2, 2], [z, -8, 4],
               [palette, false], [color, magenta, blue])$
```


![./figures/plotting18](./figures/plotting18.png)






Unendlich große Werte der z-Koordinate konnen auch durch Wahl eines 
Gitters vermieden werden, das nicht mit einer der Asymptoten zusammenfallt. 
Das Beispiel zeigt zudem die Nutzung einer Palette.









```maxima
(%i1) plot3d (log (x^2*y^2), [x, -2, 2], [y, -2, 2],[grid, 29, 29],
       [palette, [gradient, red, orange, yellow, green]],
       color_bar, [xtics, 1], [ytics, 1], [ztics, 4],
       [color_bar_tics, 4])$
```


![./figures/plotting19](./figures/plotting19.png)








Graph mit zwei Flachen mit verschiedenen Wertebereichen.








```maxima
(%i1) plot3d ([[-3*x - y, [x, -2, 2], [y, -2, 2]],
   4*sin(3*(x^2 + y^2))/(x^2 + y^2), [x, -3, 3], [y, -3, 3]],
   [x, -4, 4], [y, -4, 4])$
```


![./figures/plotting20](./figures/plotting20.png)



Graph der kleinschen Flasche, die parametrisch definiert ist.










```maxima
(%i1) expr_1: 5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)-10$
(%i2) expr_2: -5*sin(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y)+cos(x/2)*sin(2*y))$

(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 50, 50])$
```


![./figures/plotting21](./figures/plotting21.png)





Graph einer Kugelfunktion, die vordefinierte Koordinatentransformation
`spherical_to_xyz` wird verwendet, um von Kugelkoordinaten in ein 
kartesisches Koordinatensystem zu transformieren.









```maxima
(%i1) plot3d (sin(2*theta)*cos(phi), [theta, 0, %pi],
        [phi, 0, 2*%pi],
        [transform_xy, spherical_to_xyz], [grid,30,60],
   [legend,false])$
```


![./figures/plotting22](./figures/plotting22.png)






Gebrauch der vordefinierten Funktion `polar_to_xy`, um von
zylindrischen Koordinaten in ein kartesisches Koordinatensystem zu 
transformieren.  Siehe auch `polar_to_xy`. Dieses Beispiel zeigt auch 
wie der Rahmen und die Legende entfernt werden konnen.







```maxima
(%i1) plot3d (r^.33*cos(th/3), [r,0,1], [th,0,6*%pi], [box, false],
   [grid, 12, 80], [transform_xy, polar_to_xy], [legend, false])$
```


![./figures/plotting23](./figures/plotting23.png)




Graph einer Kugel, wobei die Koordinatentransformation von Kugelkoordinaten in
ein kartesisches Koordinatensystem genutzt wird. 








```maxima
(%i1) plot3d ( 5, [theta, 0, %pi], [phi, 0, 2*%pi], same_xyz,
  [transform_xy, spherical_to_xyz], [mesh_lines_color,blue],
  [palette,[gradient,"#1b1b4e", "#8c8cf8"]], [legend, false])$
```


![./figures/plotting24](./figures/plotting24.png)





Definition einer Funktion mit zwei Variablen als eine Matrix.  Der 
Quote-Operator `'` in der Definition der Funktion verhindert,
das `plot3d` fehlschlagt, wenn die Argumente keine ganze Zahlen sind.








```maxima
(%i1) M: matrix([1,2,3,4], [1,2,3,2], [1,2,3,4], [1,2,3,3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$

(%i3) plot3d (f(x,y), [x,1,4],[y,1,4],[grid,3,3],[legend,false])$
```


![./figures/plotting25](./figures/plotting25.png)




Wird die Hohenangabe `elevation` auf Null gesetzt, kann die Flache als
eine Karte betrachtet werden.  Jede Farbe reprasentiert einen anderen Wert der
Flache.








```maxima
(%i1) plot3d (cos (-x^2 + y^3/4), [x,-4,4], [y,-4,4], [zlabel,""],
       [mesh_lines_color,false], [elevation,0], [azimuth,0],
       color_bar, [grid,80,80], [ztics,false], [color_bar_tics,1])$
```


![./figures/plotting26](./figures/plotting26.png)

See also: `spherical_to_xyz`, `polar_to_xy`.

<!-- category: Other -->
<!-- keywords: plot_format -->
<!-- signatures: plot_format[plot_format, format] -->
### Variable: plot_format

Standardwert: `gnuplot_pipes`






Setzt das Grafikformat fur die Ausgabe einer Grafik.  `format` kann die 
Werte `gnuplot`, `xmaxima`, `mgnuplot` oder `gnuplot_pipes`
annehmen.  Siehe das Kapitel Grafikformate.

<!-- category: Other -->
<!-- keywords: plot_options -->
<!-- signatures: plot_options -->
### Variable: plot_options

Die Elemente dieser Liste definieren die Standardwerte fur die Ausgabe von
Graphen.  Ist einer der Werte ein Argument der Funktionen `plot2d` oder
`plot3d`, wird der Standardwert uberschrieben.  Die Standardwerte
konnen mit der Funktion `set_plot_option` gesetzt werden.  Einige
Grafikoptionen sind nicht in der Liste `plot_options` enthalten.







Jedes Element der Liste `plot_options` ist eine Liste mit zwei oder
mehr Eintragen.  Der erste Eintrag ist der Name der Grafikoption.  Die 
weiteren Eintrage sind die Parameter der Option.  In einigen Fallen kann 
der Parameter einer Option wiederum eine Liste sein.





Siehe auch `set_plot_option`, `get_plot_option` und das 
Kapitel Grafikoptionen.

See also: `set_plot_option`, `get_plot_option`.

<!-- category: Other -->
<!-- keywords: plot_realpart -->
<!-- signatures: plot_realpart[plot_realpart, symbol] -->
### Variable: plot_realpart

Standardwert: `false`












Hat `plot_realpart` den Wert `true`, werden Funktionen als komplex
angenommen und der Realteil wird gezeichnet.  Das entspricht dem Aufruf der
Grafikfunktion mit dem Ausdruck `realpart(function)`.  Hat
`plot_realpart` den Wert `false`, wird keine Grafik gezeichnet, wenn
die Funktion keinen Realteil hat.  Zum Beispiel ist `log(x)` komplex, wenn
*x* negativ ist.  Hat `plot_realpart` den Wert `true`, wird der
Wert `log(-5)` als `log(5)` gezeichnet.  Hat `plot_realpart`
den Wert `false` wird kein Wert gezeichnet.

<!-- category: Other -->
<!-- keywords: point_type -->
<!-- signatures: point_type[point_type, type_1, ..., type_n] -->
### Variable: point_type

Standardwert: `[bullet, circle, plus, times, asterisk, box, square, triangle, delta, wedge, nabla, diamond, lozenge]`










Werden im Grafikformat Gnuplot Punkte mit den Stilen `points` oder
`linespoints` gezeichnet, werden die Symbole fur die einzelnen 
Datensatze nacheinander der Liste `point_type` entnommen.  Gibt es
mehr Datensatze als Symbole, werden diese wiederholt.  Siehe auch 
`style`.

See also: `style`.

<!-- category: Other -->
<!-- keywords: polar_to_xy -->
<!-- signatures: polar_to_xy -->
### Function: polar_to_xy

Kann als Parameter der Grafikoption `transform_xy` der Funktion 
`plot3d` ubergeben werden.  Der Parameter `polar_to_xy` bewirkt, 
dass die zwei unabhangigen Variablen der Funktion `plot3d` von 
Polarkoordinaten in kartesische Koordinaten transformiert werden.


Fur ein Beispiele siehe `make_transform`.

See also: `make_transform`.

<!-- category: Other -->
<!-- keywords: psfile -->
<!-- signatures: psfile[psfile, filename] -->
### Variable: psfile

Speichert die Grafik in eine Postscript-Datei mit den Namen *filename*.  Die
Grafik wird nicht auf dem Bildschirm ausgegeben.  Standardmaßig wird die 
Datei in dem Ordner abgespeichert, dessen Namen in der Optionsvariablen
`maxima_tempdir` enthalten ist.

<!-- category: Other -->
<!-- keywords: run_viewer -->
<!-- signatures: run_viewer[run_viewer, symbol] -->
### Variable: run_viewer

Standardwert: `true`





Kontrolliert, ob die Bildschirmausgabe des Grafikformats gestartet wird.

<!-- category: Other -->
<!-- keywords: set_plot_option -->
<!-- signatures: set_plot_option(option) -->
### Function: set_plot_option (option)

Akzeptiert die meisten der Optionen, die im Kapitel Grafikoptionen aufgelistet
sind und speichert diese in der globalen Variable `plot_options`.
`set_plot_options` wertet die Argumente aus und gibt die vollstandige
Liste `plot_optons` zuruck.





Siehe auch `plot_options`, `get_plot_option` und das Kapitel
Grafikoptionen.


Beispiele:




Setze einen neue Werte fur die Grafikoption `grid`.






```maxima
(%i1) set_plot_option ([grid, 30, 40]);

(%o1) [[t, - 3, 3], [grid, 30, 40], [transform_xy, false], 
[run_viewer, true], [axes, true], [plot_format, gnuplot_pipes], 
[color, blue, red, green, magenta, black, cyan], 
[point_type, bullet, circle, plus, times, asterisk, box, square, 
triangle, delta, wedge, nabla, diamond, lozenge], 
[palette, [hue, 0.25, 0.7, 0.8, 0.5], 
[hue, 0.65, 0.8, 0.9, 0.55], [hue, 0.55, 0.8, 0.9, 0.4], 
[hue, 0.95, 0.7, 0.8, 0.5]], [gnuplot_term, default], 
[gnuplot_out_file, false], [nticks, 29], [adapt_depth, 5], 
[gnuplot_preamble, ], [gnuplot_default_term_command, 
set term pop], [gnuplot_dumb_term_command, set term dumb 79 22], 
[gnuplot_ps_term_command, set size 1.5, 1.5;set term postscript \
eps enhanced color solid 24], [plot_realpart, false]]
```

See also: `plot_options`, `get_plot_option`.

<!-- category: Other -->
<!-- keywords: spherical_to_xyz -->
<!-- signatures: spherical_to_xyz -->
### Function: spherical_to_xyz

Kann als Parameter fur die Option `transform_xy` der Funktion 
`plot3d` ubergeben werden.  Der Parameter `spherical_to_xyz` 
bewirkt, dass die zwei unabhangigen Variablen und die Funktion beim Aufruf 
von `plot3d` von Kugelkoordinaten in kartesische Koordinaten umgerechnet 
werden.

<!-- category: Other -->
<!-- keywords: style -->
<!-- signatures: style[style, type_1, ..., type1_n], style[style, [style_1], ..., [style_n]] -->
### Variable: style

Standardwert: `lines`










Bestimmt den Stil fur das Zeichnen von Funktionen oder Datensatzen mit der
Funktion `plot2d`.  Werden mehr Graphen gezeichnet, als Stile vorhanden
sind, werden diese wiederholt.  Die moglichen Stile sind `lines` fur 
Linien, `points` fur einzelne Punkte, `linespoints` fur Linien mit
Punkten oder `dots` fur kleine Punkte.  Das Grafikformat Gnuplot 
akzeptiert zusatzlich den Stil `impulses`.











Jeder Stil kann weitere Parameter erhalten, die zusammen mit dem Stil als eine
Liste angegeben werden.  Der Stil `lines` akzeptiert zwei Zahlen, die die
Breite der Linie und deren Farbe angegeben.  Die Standardfarben haben die
Zahlenwerte: 1: `blue`, 2: `red`, 3: `magenta`, 4: `orange`,
5: `brown`, 6: `lime` und 7: `aqua`.  Im Grafikformat Gnuplot 
kann die Kodierung der Farben fur verschiedene Terminals abweichend sein.  
Wird zum Beispiel das Terminal [*gnuplot_term*,*ps*] verwendet, 
entspricht dem Zahlenwert 4 die Farbe `black`.












Der Stil `points` akzeptiert zwei oder drei Parameter.  Der erste Parameter
ist der Radius des Punktes.  Der zweite Parameter ist eine Zahl, der wie
fur den Stil `lines` eine Farbe angibt.  Der dritte Parameter ist eine 
Zahl, mit der im Grafikformat Gnuplot die folgenden Zeichen fur die 
Darstellung der Punkte ausgewahlt werden konnen: 1: `bullet`, 
2: `circle`, 3: `plus`, 4: `times`, 5: `asterisk`, 
6: `box`, 7: `square`, 8: `triangle`, 9: `delta`, 
10: `wedge`, 11: `nabla`, 12: `diamond`, 13: `lozenge`.





Der Stil `linesdots` akzeptiert bis zu vier Parameter: die Breite der 
Linie, den Radius der Punkte, die Farbe und das Symbol fur das Zeichnen der
Punkte.




Siehe auch die Grafikoptionen `color` und `point_type`.

See also: `color`, `point_type`.

<!-- category: Other -->
<!-- keywords: t -->
<!-- signatures: t[t, min, max] -->
### Variable: t

Bestimmt den Wertebereich fur das Zeichnen einer parametrischen Kurve mit der
Funktion `plot2d`.  Die Variable einer parametrischen Kurve muss mit
`t` bezeichnet werden.

See also: `plot2d`.

<!-- category: Other -->
<!-- keywords: transform_xy -->
<!-- signatures: transform_xy[transform_xy, symbol] -->
### Variable: transform_xy

Standardwert: `false`






*symbol* hat entweder den Wert `false` oder ist das Ergebnis der 
Funktion `make_transform`.  Wenn verschieden von `false`, wird die
Funktion genutzt, um die drei Koordinaten einer dreidimensionalen Grafik zu
transformieren.


Siehe auch `polar_to_xy` und `spherical_to_xyz`. fur bereits
vordefinierte Koordinatentransformationen.

See also: `make_transform`, `polar_to_xy`, `spherical_to_xyz`.

<!-- category: Other -->
<!-- keywords: x -->
<!-- signatures: x[x, min, max] -->
### Variable: x

Die erste Grafikoption der Funktionen `plot2d` oder `plot3d` 
bezeichnet die un­ab­hang­ige Variable.  Die unabhangige Variable muss 
nicht mit `x` bezeichnet werden, sondern kann ein beliebiges von `x` 
verschiedenes Symbol sein.  Die Werte *min* und *max* geben in diesem
Fall den Wertebereich der unabhangigen Variablen an.  Die Grafikoption 
`x` kann ein zweites Mal angegeben werden, um den Bereich fur die x-Achse
festzulegen.

<!-- category: Other -->
<!-- keywords: xlabel -->
<!-- signatures: xlabel[xlabel, string] -->
### Variable: xlabel

Standardwert: `"x"`









Legt die Zeichenkette *string* fest, mit der die x-Achse der Grafik 
bezeichnet wird.  Der Standardwert ist `"x"` oder der Name der ersten
unabhangigen Variablen.  Diese Grafikoption kann nicht mit dem Kommando 
`set_plot_option` gesetzt werden.

<!-- category: Other -->
<!-- keywords: y -->
<!-- signatures: y[y, min, max] -->
### Variable: y

Fur einen dreidimensionalen Graphen legt diese Grafikoption die zweite 
unabhangige Variable fest.  Die unabhangige Variable muss nicht mit `y` 
bezeichnet werden, sondern kann ein beliebiges von `y` verschiedenes Symbol
sein.  Die Werte *min* und *max* geben in diesem Fall den Wertebereich 
der Variablen an.  Wird die Grafikoption fur einen zweidimensionalen Graphen 
verwendet oder fur einen dreidimensionalen Graphen ein zweites Mal eingesetzt, 
dann wird der Bereich fur die y-Achse festgelegt.

<!-- category: Other -->
<!-- keywords: ylabel -->
<!-- signatures: ylabel[ylabel, string] -->
### Variable: ylabel

Standardwert: `"y"`









Legt die Zeichenkette *string* fest, mit der die y-Achse der Grafik 
bezeichnet wird.  Der Standardwert ist `"y"` oder fur den Fall einer
dreidimensionalen Grafik der Name der zweiten unabhangigen Variablen.  Diese 
Grafikoption kann nicht mit dem Kommando `set_plot_option` gesetzt werden.

<!-- category: Other -->
<!-- keywords: z -->
<!-- signatures: z[z, min, max] -->
### Variable: z

Legt fur eine dreidimensionalen Grafik den Bereich fur die z-Achse fest.

<!-- category: Other -->
<!-- keywords: zlabel -->
<!-- signatures: zlabel[zlabel, string] -->
### Variable: zlabel

Standardwert: `"z"`








Legt die Zeichenkette *string* fest, mit der die z-Achse der Grafik 
bezeichnet wird.  Der Standardwert ist `"z"`.  Diese Grafikoption kann 
nicht mit dem Kommando `set_plot_option` gesetzt werden und wird von den
Funktionen `plot2d` sowie `implicit_plot` ignoriert.

