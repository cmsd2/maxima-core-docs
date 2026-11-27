## Grafische Darstellung

<!-- category: Plotting -->
<!-- keywords: gnuplot_close -->
<!-- signatures: gnuplot_close() -->
### Function: gnuplot_close ()

Schließt die Pipe, die im Grafikformat `gnuplot_pipes` fur den 
Austausch der Daten genutzt wird.

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_styles -->
<!-- signatures: gnuplot_curve_styles -->
### Variable: gnuplot_curve_styles

Dies ist eine veraltete Option, die von der Grafikoption `style`
ersetzt wurde.

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_titles -->
<!-- signatures: gnuplot_curve_titles -->
### Variable: gnuplot_curve_titles

Dies ist eine veraltete Option, die von der Grafikoption `legend` ersetzt
wurde.

<!-- category: Plotting -->
<!-- keywords: gnuplot_default_term_command -->
<!-- signatures: gnuplot_default_term_command -->
### Variable: gnuplot_default_term_command

Das Gnuplot-Kommando, um den Standardtyp eines Terminals zu setzen.
Der Standardwert ist `set term pop`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_dumb_term_command -->
<!-- signatures: gnuplot_dumb_term_command -->
### Variable: gnuplot_dumb_term_command

Das Gnuplot-Kommando, um die Breite und Hohe des Terminaltyps `dumb` zu
setzen.  Der Standardwert ist `"set term dumb 79 22"`.  Die Ausgabe hat 
eine Breite von 79 Zeichen und eine Hohe von 22 Zeichen.

<!-- category: Plotting -->
<!-- keywords: gnuplot_out_file -->
<!-- signatures: gnuplot_out_file -->
### Variable: gnuplot_out_file

Zusammen mit der Option `gnuplot_term`, kann die Ausgabe in dem angegebenen
Gnuplot-Format in eine Datei geschrieben werden.  Eine Postscript-Datei kann 
auch mit der Grafikoption `psfile` angegeben werden.  Die Grafikoption 
`psfile` funktioniert auch mit dem Grafikformat `xmaxima`.



```maxima
[gnuplot_term, png], [gnuplot_out_file, "graph3.png"]
```

<!-- category: Plotting -->
<!-- keywords: gnuplot_pm3d -->
<!-- signatures: gnuplot_pm3d -->
### Variable: gnuplot_pm3d

Hat die Grafikoption `gnuplot_pm3d` den Wert `false`, wird der
PM3D-Modus ausgeschaltet.  Dieser Modus ist standardmaßig eingeschaltet.

<!-- category: Plotting -->
<!-- keywords: gnuplot_preamble -->
<!-- signatures: gnuplot_preamble -->
### Variable: gnuplot_preamble

Fugt Gnuplot-Kommandos ein, die vor dem Zeichnen der Grafik ausgefuhrt 
werden.  Jedes gultige Gnuplot-Kommando kann verwendet werden.  Mehrere 
Kommandos sollten mit einem Semikolon voneinander getrennt werden.  Der 
Standardwert der Option `gnuplot_preamble` ist eine leere Zeichenkette 
`""`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_ps_term_command -->
<!-- signatures: gnuplot_ps_term_command -->
### Variable: gnuplot_ps_term_command

Das Gnuplot-Kommando, um die Parameter fur eine Postscript-Terminal zu
setzen.  Ein Postscript-Terminal hat die Standardwerte `"set size 1.5, 1.5; set term postscript eps enhanced color solid 24"`.  Das Terminal wird auf den 
1,5 fachen Wert des Standardwertes und die Schriftgroße auf 24 gesetzt.  
Siehe die Gnuplot-Dokumentation fur eine Beschreibung weiterer Parameter, die 
fur ein Postscript-Terminal gesetzt werden konnen.

<!-- category: Plotting -->
<!-- keywords: gnuplot_replot -->
<!-- signatures: gnuplot_replot(), gnuplot_replot(string) -->
### Function: gnuplot_replot ()

Aktualisiert die Ausgabe von Gnuplot.  Wird `gnuplot_replot` mit einer
Zeichenkette *string* aufgerufen, die Gnuplot-Kommandos enthalt, dann 
werden die Kommandos vor der Aktualisierung an Gnuplot gesendet.

<!-- category: Plotting -->
<!-- keywords: gnuplot_reset -->
<!-- signatures: gnuplot_reset() -->
### Function: gnuplot_reset ()

Im Grafikformat `gnuplot_pipes` wird Gnuplot zuruckgesetzt.  Um die 
Anzeige zu aktualisieren, kann das Kommando `gnuplot_replot` nach dem 
Kommando `gnuplot_reset` ausgefuhrt werden.

<!-- category: Plotting -->
<!-- keywords: gnuplot_restart -->
<!-- signatures: gnuplot_restart() -->
### Function: gnuplot_restart ()

Schließt die Pipe, die im Grafikformat `gnuplot_pipes` fur den 
Austausch der Daten genutzt wird, und offnet eine neue Pipe.

<!-- category: Plotting -->
<!-- keywords: gnuplot_start -->
<!-- signatures: gnuplot_start() -->
### Function: gnuplot_start ()

Offnet eine Pipe, die im Grafikformat `gnuplot_pipes` fur den Austausch
der Daten genutzt wird.

<!-- category: Plotting -->
<!-- keywords: gnuplot_term -->
<!-- signatures: gnuplot_term -->
### Variable: gnuplot_term

Setzt den Terminaltyp fur das Grafikformat Gnuplot.



- * 
**default** (Standardwert)

Die Ausgabe von Gnuplot wird in einem separatem Fenster angezeigt.
- * 
**dumb**

Die Ausgabe von Gnuplot wird in der Maxima Konsole mit Ascii-Zeichen angezeigt.
- * 
**ps**

Gnuplot generiert PostScript-Kommandos.  Mit der Grafikoption 
`gnuplot_out_file` werden die PostScript-Kommandos in eine Datei
*filename* geschrieben.  Ansonsten werden die Kommandos in die Datei
`maxplot.ps` geschrieben.
- * 
Jede andere gultige Gnuplot Spezifikation














Gnuplot kann Ausgaben in verschiedenen Formaten wie zum Beispiel PNG, JPEG, SVG
generieren.  Die verschiedenen Formate werden mit der Option `gnuplot_term`
angegeben.  Weiterhin kann jedes gultige Kommando als Zeichenkette ubergeben
werden.  Zum Beispiel generiert `[gnuplot_term, png]` eine Grafik im 
PNG-Format.  Das Kommando `[gnuplot_term, "png size 1000, 1000"]` generiert
eine Grafik im PNG-Format mit dem Format 1000x1000 Punkte.  Erhalt die 
Grafikoption `gnuplot_out_file` den Wert *filename*, wird die Ausgabe 
in die Datei *filename* geschrieben.  Ansonsten werden die Kommandos in die 
Datei `maxplot.term` geschrieben, wobei *term* das verwendete 
Grafikformat ist.

