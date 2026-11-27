## Gráficos

<!-- category: Plotting -->
<!-- keywords: gnuplot_close -->
<!-- signatures: gnuplot_close() -->
### Function: gnuplot_close ()

Cierra la tubería hacia Gnuplot que haya sido 
utilizada para hacer gráficos.

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_styles -->
<!-- signatures: gnuplot_curve_styles -->
### Variable: gnuplot_curve_styles

Opción obsoleta que ha sido sustituida por `style`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_titles -->
<!-- signatures: gnuplot_curve_titles -->
### Variable: gnuplot_curve_titles

Opción obsoleta que ha sido sustituida por `legend`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_default_term_command -->
<!-- signatures: gnuplot_default_term_command -->
### Variable: gnuplot_default_term_command

Comando de Gnuplot para establecer el tipo de terminal por defecto.
El valor por defecto es `set term pop`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_dumb_term_command -->
<!-- signatures: gnuplot_dumb_term_command -->
### Variable: gnuplot_dumb_term_command

Comando de Gnuplot para establecer el tipo de terminal para
el terminal oculto. El valor por defecto es `"set term dumb 79 22"`,
que da una salida de texto de 79 por 22 caracteres.

<!-- category: Plotting -->
<!-- keywords: gnuplot_out_file -->
<!-- signatures: gnuplot_out_file -->
### Variable: gnuplot_out_file

Cuando se utiliza conjuntamente con la opción `gnuplot_term`,
puede utilizarse para almacenar el gráfico en un fichero en uno
de los formatos aceptados por Gnuplot. Si se quiere crear un fichero
Postscript se puede utilizar la opción `psfile`, que también 
funciona con Openmath.



```maxima
[gnuplot_term, png], [gnuplot_out_file, "graph3.png"]
```

<!-- category: Plotting -->
<!-- keywords: gnuplot_pm3d -->
<!-- signatures: gnuplot_pm3d -->
### Variable: gnuplot_pm3d

Controla la utilización del modo PM3D, que tiene capacidades avanzadas
para gráficos tridimensionales. PM3D sólo está disponible en versiones 
de Gnuplot posteriores a la 3.7. El valor por defecto de `gnuplot_pm3d` es `false`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_preamble -->
<!-- signatures: gnuplot_preamble -->
### Variable: gnuplot_preamble

Introduce instrucciones de Gnuplot antes de que se haga el gráfico.
Puede utilizarse cualquier comando válido de Gnuplot. Si interesa 
introducir varios comandos se separarán con punto y coma. El valor 
por defecto de `gnuplot_preamble` es la cadena vacía `""`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_ps_term_command -->
<!-- signatures: gnuplot_ps_term_command -->
### Variable: gnuplot_ps_term_command

Comando de Gnuplot para establecer el tipo de terminal para
el terminal PostScript. El valor por defecto es
`"set size 1.5, 1.5;set term postscript eps enhanced color solid 24"`,
que establece un tamaño de 1.5 veces el valor por defecto de gnuplot,
junto con un tamaño de fuente de 24, entre otras cosas. Consúltese
la documentación de gnuplot para más información sobre `set term postscript`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_replot -->
<!-- signatures: gnuplot_replot(), gnuplot_replot(s) -->
### Function: gnuplot_replot ()

Actualiza la ventana de Gnuplot. Si `gnuplot_replot` es invocada
con un comando de Gnuplot en la cadena *s*, entonces *s* es 
enviada a Gnuplot antes de redibujar la ventana.

<!-- category: Plotting -->
<!-- keywords: gnuplot_reset -->
<!-- signatures: gnuplot_reset() -->
### Function: gnuplot_reset ()

Resetea Gnuplot cuando se utiliza el formato `gnuplot_pipes`.
Para actualizar la ventana de Gnuplot invóquese a `gnuplot_replot`
después de `gnuplot_reset`.

<!-- category: Plotting -->
<!-- keywords: gnuplot_restart -->
<!-- signatures: gnuplot_restart() -->
### Function: gnuplot_restart ()

Cierra la tubería hacia Gnuplot que haya sido 
utilizada para hacer gráficos e inicializa una nueva.

<!-- category: Plotting -->
<!-- keywords: gnuplot_start -->
<!-- signatures: gnuplot_start() -->
### Function: gnuplot_start ()

Inicializa una tubería hacia Gnuplot, con el fin
de ser utilizada para utilizar el formato `gnuplot_pipes`.
No es necesario inicializarla manualmente antes de hacer gráficos.

<!-- category: Plotting -->
<!-- keywords: gnuplot_term -->
<!-- signatures: gnuplot_term -->
### Variable: gnuplot_term

Establece el terminal de salida para Gnuplot.



- *
**default** (valor por defecto)

Gnuplot muestra el gráfico en una ventana gráfica.
- *
**dumb**

Gnuplot muestra el gráfico en la consola de Maxima
en estilo ASCII artístico.
- *
**ps**

Gnuplot genera código en lenguaje PostScript.
Si a la opción `gnuplot_out_file` se le da el
valor *filename*, Gnuplot escribe el código PostScript
en *filename*. En caso contrario, se guarda en el archivo `maxplot.ps`.
- *
Cualquier otro terminal admitido por Gnuplot.

Gnuplot puede generar gráficos en otros muchos formatos, tales como
png, jpeg, svg etc. Para crear gráficos en cualquera de estos formatos,
a la opción `gnuplot_term` se le puede asignar cualquiera de los
terminales admitidos por Gnuplot, bien por su nombre (símbolo)
bien con la especificación completa del terminal (cadena). Por ejemplo,
`[gnuplot_term,png]` guarda el gráfico en formato PNG (Portable
Network Graphics), mientras que `[gnuplot_term,"png size 1000,1000"]`
lo hace con dimensiones 1000x1000 píxeles.
Si a la opción `gnuplot_out_file` se le da el
valor *filename*, Gnuplot escribe el código PostScript
en *filename*. En caso contrario, se guarda en el archivo 
`maxplot.term`, siendo *term* el nombre del terminal.

