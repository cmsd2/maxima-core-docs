## graphs

<!-- category: Plotting -->
<!-- keywords: add_edge -->
<!-- signatures: add_edge(e, gr) -->
### Function: add_edge (e, gr)

Añade la arista *e* al grafo *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) p : path_graph(4)$
(%i3) neighbors(0, p);
(%o3)                                [1]
(%i4) add_edge([0,3], p);
(%o4)                               done
(%i5) neighbors(0, p);
(%o5)                              [3, 1]
```

<!-- category: Plotting -->
<!-- keywords: add_edges -->
<!-- signatures: add_edges(e_list, gr) -->
### Function: add_edges (e_list, gr)

Añade las aristas de la lista  *e_list* al grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : empty_graph(3)$
(%i3) add_edges([[0,1],[1,2]], g)$
(%i4) print_graph(g)$
Graph on 3 vertices with 2 edges.
Adjacencies:
  2 :  1
  1 :  2  0
  0 :  1
```

<!-- category: Plotting -->
<!-- keywords: add_vertex -->
<!-- signatures: add_vertex(v, gr) -->
### Function: add_vertex (v, gr)

Añade el vértice *v* al grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : path_graph(2)$
(%i3) add_vertex(2, g)$
(%i4) print_graph(g)$
Graph on 3 vertices with 1 edges.
Adjacencies:
  2 :
  1 :  0
  0 :  1
```

<!-- category: Plotting -->
<!-- keywords: add_vertices -->
<!-- signatures: add_vertices(v_list, gr) -->
### Function: add_vertices (v_list, gr)

Añade los vértices de la lista  *v_list* al grafo *gr*.

<!-- category: Plotting -->
<!-- keywords: adjacency_matrix -->
<!-- signatures: adjacency_matrix(gr) -->
### Function: adjacency_matrix (gr)

Devuelve la matriz de adyacencia del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(4)$
(%i3) adjacency_matrix(c5);
                                [ 0  1  0  1 ]
                                [            ]
                                [ 1  0  1  0 ]
(%o3)                           [            ]
                                [ 0  1  0  1 ]
                                [            ]
                                [ 1  0  1  0 ]
```

<!-- category: Plotting -->
<!-- keywords: average_degree -->
<!-- signatures: average_degree(gr) -->
### Function: average_degree (gr)

Devuelve el grado medio de los vértices del garfo *gr*.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) average_degree(grotzch_graph());
                                      40
(%o2)                                 --
                                      11
```

<!-- category: Plotting -->
<!-- keywords: biconnected_components -->
<!-- signatures: biconnected_components(gr) -->
### Function: biconnected_components (gr)

Devuelve los subconjuntos de vértices biconectados del grafo *gr*.


Ejemplo:













```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(
            [1,2,3,4,5,6,7],
            [
             [1,2],[2,3],[2,4],[3,4],
             [4,5],[5,6],[4,6],[6,7]
            ])$
(%i3) biconnected_components(g);
(%o3)               [[6, 7], [4, 5, 6], [1, 2], [2, 3, 4]]
```


(Figure graphs13, Grafo con vértices biconectados)

<!-- category: Plotting -->
<!-- keywords: bipartition -->
<!-- signatures: bipartition(gr) -->
### Function: bipartition (gr)

Devuelve una bipartición de los vértices del grafo *gr*, o una
lista vacía si *gr* no es bipartido.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) h : heawood_graph()$
(%i3) [A,B]:bipartition(h);
(%o3)         [[8, 12, 6, 10, 0, 2, 4], [13, 5, 11, 7, 9, 1, 3]]
(%i4) draw_graph(h, show_vertices=A, program=circular)$
```


(Figure graphs02, Bipartición de los vértices de un grafo de Heawood)

<!-- category: Plotting -->
<!-- keywords: chromatic_index -->
<!-- signatures: chromatic_index(gr) -->
### Function: chromatic_index (gr)

Devuelve el índice cromático del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) chromatic_index(p);
(%o3)                                  4
```

<!-- category: Plotting -->
<!-- keywords: chromatic_number -->
<!-- signatures: chromatic_number(gr) -->
### Function: chromatic_number (gr)

Devuelve el número cromático del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) chromatic_number(cycle_graph(5));
(%o2)                                  3
(%i3) chromatic_number(cycle_graph(6));
(%o3)                                  2
```

<!-- category: Plotting -->
<!-- keywords: circulant_graph -->
<!-- signatures: circulant_graph(n, d) -->
### Function: circulant_graph (n, d)

Devuelve un grafo cirlulante de parámetros *n* y *d*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : circulant_graph(10, [1,3])$
(%i3) print_graph(g)$
Graph on 10 vertices with 20 edges.
Adjacencies:
  9 :  2  6  0  8
  8 :  1  5  9  7
  7 :  0  4  8  6
  6 :  9  3  7  5
  5 :  8  2  6  4
  4 :  7  1  5  3
  3 :  6  0  4  2
  2 :  9  5  3  1
  1 :  8  4  2  0
  0 :  7  3  9  1
```

<!-- category: Plotting -->
<!-- keywords: clear_edge_weight -->
<!-- signatures: clear_edge_weight(e, gr) -->
### Function: clear_edge_weight (e, gr)

Elimina el peso del arco *e* del grafo *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(3, [[[0,1], 1.5], [[1,2], 1.3]])$
(%i3) get_edge_weight([0,1], g);
(%o3)                                 1.5
(%i4) clear_edge_weight([0,1], g)$
(%i5) get_edge_weight([0,1], g);
(%o5)                                  1
```

<!-- category: Plotting -->
<!-- keywords: clear_vertex_label -->
<!-- signatures: clear_vertex_label(v, gr) -->
### Function: clear_vertex_label (v, gr)

Elimina la etiqueta del vértice *v* del grafo *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[0,"Zero"], [1, "One"]], [[0,1]])$
(%i3) get_vertex_label(0, g);
(%o3)                               Zero
(%i4) clear_vertex_label(0, g);
(%o4)                               done
(%i5) get_vertex_label(0, g);
(%o5)                               false
```

<!-- category: Plotting -->
<!-- keywords: clebsch_graph -->
<!-- signatures: clebsch_graph() -->
### Function: clebsch_graph ()

Devuelve el grafo de Clebsch.

<!-- category: Plotting -->
<!-- keywords: complement_graph -->
<!-- signatures: complement_graph(g) -->
### Function: complement_graph (g)

Devuelve el complemento del grafo *g*.

<!-- category: Plotting -->
<!-- keywords: complete_bipartite_graph -->
<!-- signatures: complete_bipartite_graph(n, m) -->
### Function: complete_bipartite_graph (n, m)

Devuelve el grafo bipartido completo de *n+m* vértices.

<!-- category: Plotting -->
<!-- keywords: complete_graph -->
<!-- signatures: complete_graph(n) -->
### Function: complete_graph (n)

Devuelve el grafo completo de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: connect_vertices -->
<!-- signatures: connect_vertices(v_list, u_list, gr) -->
### Function: connect_vertices (v_list, u_list, gr)

Conecta todos los vértices de la lista *v_list* con los vértices
de la lista *u_list* del grafo *gr*.


*v_list* y *u_list* pueden ser vértices aislados o una lista de
vértices.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : empty_graph(4)$
(%i3) connect_vertices(0, [1,2,3], g)$
(%i4) print_graph(g)$
Graph on 4 vertices with 3 edges.
Adjacencies:
  3 :  0
  2 :  0
  1 :  0
  0 :  3  2  1
```

<!-- category: Plotting -->
<!-- keywords: connected_components -->
<!-- signatures: connected_components(gr) -->
### Function: connected_components (gr)

Devuelve las componentes conexas del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g: graph_union(cycle_graph(5), path_graph(4))$
(%i3) connected_components(g);
(%o3)                  [[1, 2, 3, 4, 0], [8, 7, 6, 5]]
```

<!-- category: Plotting -->
<!-- keywords: contract_edge -->
<!-- signatures: contract_edge(e, gr) -->
### Function: contract_edge (e, gr)

Contrae la arista *e* del *gr*.


Ejemplo:











```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph(
       8, [[0,3],[1,3],[2,3],[3,4],[4,5],[4,6],[4,7]])$
(%i3) print_graph(g)$
Graph on 8 vertices with 7 edges.
Adjacencies:
  7 :  4
  6 :  4
  5 :  4
  4 :  7  6  5  3
  3 :  4  2  1  0
  2 :  3
  1 :  3
  0 :  3
(%i4) contract_edge([3,4], g)$
(%i5) print_graph(g)$
Graph on 7 vertices with 6 edges.
Adjacencies:
  7 :  3
  6 :  3
  5 :  3
  3 :  5  6  7  2  1  0
  2 :  3
  1 :  3
  0 :  3
```

<!-- category: Plotting -->
<!-- keywords: copy_graph -->
<!-- signatures: copy_graph(g) -->
### Function: copy_graph (g)

Devuelve una copia del grafo *g*.

<!-- category: Plotting -->
<!-- keywords: create_graph -->
<!-- signatures: create_graph(v_list, e_list), create_graph(n, e_list), create_graph(v_list, e_list, directed) -->
### Function: create_graph (v_list, e_list)

Crea un nuevo grafo sobre el conjunto de vértices *v_list* con aristas
*e_list*.


*v_list* es una lista de vértices (`[v1, v2,..., vn]`) o una lista de
vértices junto con sus respectivas etiquetas (`[[v1,l1], [v2,l2],..., [vn,ln]]`).


*n* es el número de vértices, los cuales se identificarán desde
0 hasta n-1.


*e_list* es una lista de aristas (`[e1, e2,..., em]`) o una lista de
aristas con sus respectivas ponderaciones (`[[e1, w1], ..., [em, wm]]`).


Si *directed* is not `false`, se devolverá un grafo orientado.


Ejemplos:


Crea un ciclo de 3 vértices.








```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1,2,3], [[1,2], [2,3], [1,3]])$
(%i3) print_graph(g)$
Graph on 3 vertices with 3 edges.
Adjacencies:
  3 :  1  2
  2 :  3  1
  1 :  3  2
```


Crea un ciclo de 3 vértices y aristas ponderadas:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1,2,3], [[[1,2], 1.0], [[2,3], 2.0],
                                [[1,3], 3.0]])$
(%i3) print_graph(g)$
Graph on 3 vertices with 3 edges.
Adjacencies:
  3 :  1  2
  2 :  3  1
  1 :  3  2
```


Crea un grafo orientado:














```maxima
(%i1) load ("graphs")$
(%i2) d : create_graph(
       [1,2,3,4], 
       [
        [1,3], [1,4],
        [2,3], [2,4]
       ],
       'directed = true)$
(%i3) print_graph(d)$
Digraph on 4 vertices with 4 arcs.
Adjacencies:
  4 :
  3 :
  2 :  4  3
  1 :  4  3
```

<!-- category: Plotting -->
<!-- keywords: cube_graph -->
<!-- signatures: cube_graph(n) -->
### Function: cube_graph (n)

Devuelve el cubo de *n* dimensiones.

<!-- category: Plotting -->
<!-- keywords: cuboctahedron_graph -->
<!-- signatures: cuboctahedron_graph(n) -->
### Function: cuboctahedron_graph (n)

Devuelve el grafo cubooctaédrico.

<!-- category: Plotting -->
<!-- keywords: cycle_digraph -->
<!-- signatures: cycle_digraph(n) -->
### Function: cycle_digraph (n)

Devuelve el ciclo dirigido de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: cycle_graph -->
<!-- signatures: cycle_graph(n) -->
### Function: cycle_graph (n)

Devuelve el ciclo de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: degree_sequence -->
<!-- signatures: degree_sequence(gr) -->
### Function: degree_sequence (gr)

Devuelve una lista con los grados de los vértices del grafo *gr*.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) degree_sequence(random_graph(10, 0.4));
(%o2)            [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

<!-- category: Plotting -->
<!-- keywords: diameter -->
<!-- signatures: diameter(gr) -->
### Function: diameter (gr)

Devuelve el diámetro del grafo *gr*.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) diameter(dodecahedron_graph());
(%o2)                                 5
```

<!-- category: Plotting -->
<!-- keywords: dimacs_export -->
<!-- signatures: dimacs_export(gr, fl), dimacs_export(gr, fl, comment1, ..., commentn) -->
### Function: dimacs_export (gr, fl)

Exporta el grafo al fichero *fl* en formato DIMACS. Los comentarios
adicionales se anãdirán al comienzo del fichero.

<!-- category: Plotting -->
<!-- keywords: dimacs_import -->
<!-- signatures: dimacs_import(fl) -->
### Function: dimacs_import (fl)

Lee el grafo almacenado en el fichero *fl* en formato DIMACS.

<!-- category: Plotting -->
<!-- keywords: dodecahedron_graph -->
<!-- signatures: dodecahedron_graph() -->
### Function: dodecahedron_graph ()

Devuelve el grafo del dodecaedro.

<!-- category: Plotting -->
<!-- keywords: draw_graph -->
<!-- signatures: draw_graph(graph), draw_graph(graph, option1, ..., optionk) -->
### Function: draw_graph (graph)

Dibuja el grafo utilizando el paquete `draw`.


El algoritmo utilizado para posicionar los vértices se especifica con el argumento
opcional *program*, cuyo valor por defecto es `program=spring_embedding`.
*draw_graph* también puede utilizar los programas de graphviz para
posicionar los vértices, para lo cual deberá instalarse separadamente el programa graphviz.


Ejemplo 1:












```maxima
(%i1) load ("graphs")$
(%i2) g:grid_graph(10,10)$
(%i3) m:max_matching(g)$
(%i4) draw_graph(g,
   spring_embedding_depth=100,
   show_edges=m, edge_type=dots,
   vertex_size=0)$
```


(Figure graphs09, Ejemplo de uso de draw_graph para dibujar un grafo)


Ejemplo 2:






















```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(16,
    [
     [0,1],[1,3],[2,3],[0,2],[3,4],[2,4],
     [5,6],[6,4],[4,7],[6,7],[7,8],[7,10],[7,11],
     [8,10],[11,10],[8,9],[11,12],[9,15],[12,13],
     [10,14],[15,14],[13,14]
    ])$
(%i3) t:minimum_spanning_tree(g)$
(%i4) draw_graph(
    g,
    show_edges=edges(t),
    show_edge_width=4,
    show_edge_color=green,
    vertex_type=filled_square,
    vertex_size=2
    )$
```


(Figure graphs10, Ejemplo de uso de draw_graph para dibujar un grafo)


Ejemplo 3:

















```maxima
(%i1) load ("graphs")$
(%i2) mi : max_independent_set(g)$
(%i3) draw_graph(
    g,
    show_vertices=mi,
    show_vertex_type=filled_up_triangle,
    show_vertex_size=2,
    edge_color=cyan,
    edge_width=3,
    =true,
    text_color=brown
    )$
```


(Figure graphs11, Ejemplo de uso de draw_graph para dibujar un grafo)


Ejemplo 4:



























```maxima
(%i1) load ("graphs")$
(%i2) net : create_graph(
    [0,1,2,3,4,5],
    [
     [[0,1], 3], [[0,2], 2],
     [[1,3], 1], [[1,4], 3],
     [[2,3], 2], [[2,4], 2],
     [[4,5], 2], [[3,5], 2]
    ],
    directed=true
    )$
(%i3) draw_graph(
    net,
    show_weight=true,
    vertex_size=0,
    show_vertices=[0,5],
    show_vertex_type=filled_square,
    head_length=0.2,
    head_angle=10,
    edge_color="dark-green",
    text_color=blue
    )$
```


(Figure graphs12, Ejemplo de uso de draw_graph para dibujar un grafo)


Ejemplo 5:








```maxima
(%i1) load("graphs")$
(%i2) g: petersen_graph(20, 2);
(%o2)                         GRAPH
(%i3) draw_graph(g, redraw=true, program=planar_embedding);
(%o3)                         done
```


(Figure graphs14, Ejemplo de uso de draw_graph para dibujar un grafo)


Ejemplo 6:









```maxima
(%i1) load("graphs")$
(%i2) t: tutte_graph();
(%o2)                         GRAPH
(%i3) draw_graph(t, redraw=true, 
                    fixed_vertices=[1,2,3,4,5,6,7,8,9]);
(%o3)                         done
```


(Figure graphs15, Ejemplo de uso de draw_graph para dibujar un grafo)

<!-- category: Plotting -->
<!-- keywords: draw_graph_program -->
<!-- signatures: draw_graph_program -->
### Variable: draw_graph_program

Valor por defecto: *spring_embedding*


Programa a utilizar por defecto para posicionar los vértices en la función `draw_graph`.

<!-- category: Plotting -->
<!-- keywords: edge_color -->
<!-- signatures: edge_color -->
### Variable: edge_color

Color a utilizar en las aristas.

<!-- category: Plotting -->
<!-- keywords: edge_coloring -->
<!-- signatures: edge_coloring(gr) -->
### Function: edge_coloring (gr)

Devuelve una coloración óptima de los arcos del grafo *gr*.


La función devuelve el índice cromático y una lista
que representa el coloreado de los arcos de *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) [ch_index, col] : edge_coloring(p);
(%o3) [4, [[[0, 5], 3], [[5, 7], 1], [[0, 1], 1], [[1, 6], 2], 
[[6, 8], 1], [[1, 2], 3], [[2, 7], 4], [[7, 9], 2], [[2, 3], 2], 
[[3, 8], 3], [[5, 8], 2], [[3, 4], 1], [[4, 9], 4], [[6, 9], 3], 
[[0, 4], 2]]]
(%i4) assoc([0,1], col);
(%o4)                           1
(%i5) assoc([0,5], col);
(%o5)                           3
```

<!-- category: Plotting -->
<!-- keywords: edge_connectivity -->
<!-- signatures: edge_connectivity(gr) -->
### Function: edge_connectivity (gr)

Devuelve la conectividad de las aristas del grafo *gr*.


Véase también `min_edge_cut`.

<!-- category: Plotting -->
<!-- keywords: edge_partition -->
<!-- signatures: edge_partition -->
### Variable: edge_partition

Una partición `[[e1,e2,...],...,[ek,...,em]]` de las aristas del grafo.
Las aristas de cada lista se dibujarán de diferente color.

<!-- category: Plotting -->
<!-- keywords: edge_type -->
<!-- signatures: edge_type -->
### Variable: edge_type

Establece cómo se dibujarán las aristas. Véase la opción
*line_type* del paquete `draw`.

<!-- category: Plotting -->
<!-- keywords: edge_width -->
<!-- signatures: edge_width -->
### Variable: edge_width

Ancho de las aristas.

<!-- category: Plotting -->
<!-- keywords: edges -->
<!-- signatures: edges(gr) -->
### Function: edges (gr)

Devuelve la lista de las aristas (arcos) del grafo (dirigido) *gr*.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) edges(complete_graph(4));
(%o2)         [[2, 3], [1, 3], [1, 2], [0, 3], [0, 2], [0, 1]]
```

<!-- category: Plotting -->
<!-- keywords: empty_graph -->
<!-- signatures: empty_graph(n) -->
### Function: empty_graph (n)

Devuelve el grafo vacío de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: fixed_vertices -->
<!-- signatures: fixed_vertices -->
### Variable: fixed_vertices

Especifica una lista de vértices con posiciones fijas en
un polígono regular. Se puede utilizar cuando `program=spring_embedding`.

<!-- category: Plotting -->
<!-- keywords: flower_snark -->
<!-- signatures: flower_snark(n) -->
### Function: flower_snark (n)

Devuelve el grafo de flor de *4n* vértices.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) f5 : flower_snark(5)$
(%i3) chromatic_index(f5);
(%o3)                                  4
```

<!-- category: Plotting -->
<!-- keywords: from_adjacency_matrix -->
<!-- signatures: from_adjacency_matrix(A) -->
### Function: from_adjacency_matrix (A)

Devuelve el grafo definido por la matriz de adyacencia *A*.

<!-- category: Plotting -->
<!-- keywords: frucht_graph -->
<!-- signatures: frucht_graph() -->
### Function: frucht_graph ()

Devuelve el grafo de Frucht.

<!-- category: Plotting -->
<!-- keywords: get_edge_weight -->
<!-- signatures: get_edge_weight(e, gr), get_edge_weight(e, gr, ifnot) -->
### Function: get_edge_weight (e, gr)

Devuelve el peso de la arista *e* del grafo *gr*.


Si la arista no tiene peso, la función devuelve 1. Si la arista no
pertenece al grafo, la función emite un mensaje de error o devuelve
el argumento opcional *ifnot*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(5)$
(%i3) get_edge_weight([1,2], c5);
(%o3)                                 1
(%i4) set_edge_weight([1,2], 2.0, c5);
(%o4)                               done
(%i5) get_edge_weight([1,2], c5);
(%o5)                                2.0
```

<!-- category: Plotting -->
<!-- keywords: get_vertex_label -->
<!-- signatures: get_vertex_label(v, gr) -->
### Function: get_vertex_label (v, gr)

Devuelve la etiqueta del vértice *v* del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[0,"Zero"], [1, "One"]], [[0,1]])$
(%i3) get_vertex_label(0, g);
(%o3)                               Zero
```

<!-- category: Plotting -->
<!-- keywords: girth -->
<!-- signatures: girth(gr) -->
### Function: girth (gr)

Devuelve la longitud del ciclo más corto del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : heawood_graph()$
(%i3) girth(g);
(%o3)                                 6
```

<!-- category: Plotting -->
<!-- keywords: graph6_decode -->
<!-- signatures: graph6_decode(str) -->
### Function: graph6_decode (str)

Devuelve el grafo codificado en formato graph6 en la cadena *str*.

<!-- category: Plotting -->
<!-- keywords: graph6_encode -->
<!-- signatures: graph6_encode(gr) -->
### Function: graph6_encode (gr)

Devuelve una cadena codificando el grafo *gr* en formato graph6.

<!-- category: Plotting -->
<!-- keywords: graph6_export -->
<!-- signatures: graph6_export(gr_list, fl) -->
### Function: graph6_export (gr_list, fl)

Exporta los grafos de la lista *gr_list* al fichero *fl* en formato graph6.

<!-- category: Plotting -->
<!-- keywords: graph6_import -->
<!-- signatures: graph6_import(fl) -->
### Function: graph6_import (fl)

Lee la lista de grafos almacenados en el fichero *fl* en formato graph6.

<!-- category: Plotting -->
<!-- keywords: graph_center -->
<!-- signatures: graph_center(gr) -->
### Function: graph_center (gr)

Devuelve el centro del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_center(g);
(%o3)                               [12]
```

<!-- category: Plotting -->
<!-- keywords: graph_charpoly -->
<!-- signatures: graph_charpoly(gr, x) -->
### Function: graph_charpoly (gr, x)

Devuelve el polinomio característico (de variable *x*)
del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_charpoly(p, x), factor;
                                         5        4
(%o3)                     (x - 3) (x - 1)  (x + 2)
```

<!-- category: Plotting -->
<!-- keywords: graph_eigenvalues -->
<!-- signatures: graph_eigenvalues(gr) -->
### Function: graph_eigenvalues (gr)

Devuelve los valores propios del grafo *gr*. La función
devuelve los valores propios en el mismo formato en el que lo 
hace la función `eigenvalue`.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_eigenvalues(p);
(%o3)                     [[3, - 2, 1], [1, 4, 5]]
```

<!-- category: Plotting -->
<!-- keywords: graph_order -->
<!-- signatures: graph_order(gr) -->
### Function: graph_order (gr)

Devuelve el número de vértices del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_order(p);
(%o3)                                10
```

<!-- category: Plotting -->
<!-- keywords: graph_periphery -->
<!-- signatures: graph_periphery(gr) -->
### Function: graph_periphery (gr)

Devuelve la periferia del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_periphery(g);
(%o3)                          [24, 20, 4, 0]
```

<!-- category: Plotting -->
<!-- keywords: graph_product -->
<!-- signatures: graph_product(g1, g1) -->
### Function: graph_product (g1, g1)

Devuelve el producto dirigido de los grafos *g1* y *g2*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) grid : graph_product(path_graph(3), path_graph(4))$
(%i3) draw_graph(grid)$
```


(Figure graphs01, Producto directo de dos grafos)

<!-- category: Plotting -->
<!-- keywords: graph_size -->
<!-- signatures: graph_size(gr) -->
### Function: graph_size (gr)

Devuelve el número de aristas del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_size(p);
(%o3)                                15
```

<!-- category: Plotting -->
<!-- keywords: graph_union -->
<!-- signatures: graph_union(g1, g1) -->
### Function: graph_union (g1, g1)

Devuelve la unión (suma) de los grafos *g1* y *g2*.

<!-- category: Plotting -->
<!-- keywords: great_rhombicosidodecahedron_graph -->
<!-- signatures: great_rhombicosidodecahedron_graph() -->
### Function: great_rhombicosidodecahedron_graph ()

Devuelve el grafo gran rombicosidodecaédrico.

<!-- category: Plotting -->
<!-- keywords: great_rhombicuboctahedron_graph -->
<!-- signatures: great_rhombicuboctahedron_graph() -->
### Function: great_rhombicuboctahedron_graph ()

Devuelve el grafo gran rombicocubicooctaédrico.

<!-- category: Plotting -->
<!-- keywords: grid_graph -->
<!-- signatures: grid_graph(n, m) -->
### Function: grid_graph (n, m)

Devuelve la rejilla *n x m*.

<!-- category: Plotting -->
<!-- keywords: grotzch_graph -->
<!-- signatures: grotzch_graph() -->
### Function: grotzch_graph ()

Devuelve el grafo de Grotzch.

<!-- category: Plotting -->
<!-- keywords: hamilton_cycle -->
<!-- signatures: hamilton_cycle(gr) -->
### Function: hamilton_cycle (gr)

Devuelve el ciclo de Hamilton del grafo *gr* o una lista vacía
si *gr* no es hamiltoniano.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) c : cube_graph(3)$
(%i3) hc : hamilton_cycle(c);
(%o3)              [7, 3, 2, 6, 4, 0, 1, 5, 7]
(%i4) draw_graph(c, show_edges=vertices_to_cycle(hc))$
```


(Figure graphs03, Ciclo de Hamilton de un grafo cúbico)

<!-- category: Plotting -->
<!-- keywords: hamilton_path -->
<!-- signatures: hamilton_path(gr) -->
### Function: hamilton_path (gr)

Devuelve el camino de Hamilton del grafo *gr* o una lista vacía
si *gr* no los tiene.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) hp : hamilton_path(p);
(%o3)                  [0, 5, 7, 2, 1, 6, 8, 3, 4, 9]
(%i4) draw_graph(p, show_edges=vertices_to_path(hp))$
```


(Figure graphs04, Camino de Hamilton de un grafo de Petersen)

<!-- category: Plotting -->
<!-- keywords: heawood_graph -->
<!-- signatures: heawood_graph() -->
### Function: heawood_graph ()

Devuelve el grafo de Heawood.

<!-- category: Plotting -->
<!-- keywords: icosahedron_graph -->
<!-- signatures: icosahedron_graph() -->
### Function: icosahedron_graph ()

Devuelve el grafo icosaédrico.

<!-- category: Plotting -->
<!-- keywords: icosidodecahedron_graph -->
<!-- signatures: icosidodecahedron_graph() -->
### Function: icosidodecahedron_graph ()

Devuelve el grafo icosidodecaédrico.

<!-- category: Plotting -->
<!-- keywords: in_neighbors -->
<!-- signatures: in_neighbors(v, gr) -->
### Function: in_neighbors (v, gr)

Devuelve la lista de los nodos hijos del vértice *v*
del grafo orientado *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                                 [1]
(%i4) out_neighbors(2, p);
(%o4)                                 []
```

<!-- category: Plotting -->
<!-- keywords: induced_subgraph -->
<!-- signatures: induced_subgraph(V, g) -->
### Function: induced_subgraph (V, g)

Devuelve el grafo inducido por el subconjunto *V* de vértices del grafo *g*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) V : [0,1,2,3,4]$
(%i4) g : induced_subgraph(V, p)$
(%i5) print_graph(g)$
Graph on 5 vertices with 5 edges.
Adjacencies:
  4 :  3  0
  3 :  2  4
  2 :  1  3
  1 :  0  2
  0 :  1  4
```

<!-- category: Plotting -->
<!-- keywords: is_biconnected -->
<!-- signatures: is_biconnected(gr) -->
### Function: is_biconnected (gr)

Devuelve `true` si *gr* está biconectado y `false`
en caso contrario.


Ejemplo:


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_biconnected(cycle_graph(5));
(%o2)                         true
(%i3) is_biconnected(path_graph(5));
(%o3)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_bipartite -->
<!-- signatures: is_bipartite(gr) -->
### Function: is_bipartite (gr)

Devuelve `true` si *gr* es bipartido (2-coloreable) y `false`
en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_bipartite(petersen_graph());
(%o2)                               false
(%i3) is_bipartite(heawood_graph());
(%o3)                               true
```

<!-- category: Plotting -->
<!-- keywords: is_connected -->
<!-- signatures: is_connected(gr) -->
### Function: is_connected (gr)

Devuelve `true` si el grafo *gr* es conexo y `false`
en caso contrario.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) is_connected(graph_union(cycle_graph(4), path_graph(3)));
(%o2)                               false
```

<!-- category: Plotting -->
<!-- keywords: is_digraph -->
<!-- signatures: is_digraph(gr) -->
### Function: is_digraph (gr)

Devuelve `true` si *gr* es un grafo orientado (digrafo) y
`false` en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_digraph(path_graph(5));
(%o2)                               false
(%i3) is_digraph(path_digraph(5));
(%o3)                               true
```

<!-- category: Plotting -->
<!-- keywords: is_edge_in_graph -->
<!-- signatures: is_edge_in_graph(e, gr) -->
### Function: is_edge_in_graph (e, gr)

Devuelve `true` si *e* es una arista (arco) del
grafo (digrafo) *g* y `false` en caso contrario.


Ejemplo:











```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_edge_in_graph([2,3], c4);
(%o3)                               true
(%i4) is_edge_in_graph([3,2], c4);
(%o4)                               true
(%i5) is_edge_in_graph([2,4], c4);
(%o5)                               false
(%i6) is_edge_in_graph([3,2], cycle_digraph(4));
(%o6)                               false
```

<!-- category: Plotting -->
<!-- keywords: is_graph -->
<!-- signatures: is_graph(gr) -->
### Function: is_graph (gr)

Devuelve `true` si *gr* es un grafo y `false` en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_graph(path_graph(5));
(%o2)                               true
(%i3) is_graph(path_digraph(5));
(%o3)                               false
```

<!-- category: Plotting -->
<!-- keywords: is_graph_or_digraph -->
<!-- signatures: is_graph_or_digraph(gr) -->
### Function: is_graph_or_digraph (gr)

Devuelve `true` si *gr* es una grafo, orientado o no,
y `false` en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_graph_or_digraph(path_graph(5));
(%o2)                               true
(%i3) is_graph_or_digraph(path_digraph(5));
(%o3)                               true
```

<!-- category: Plotting -->
<!-- keywords: is_isomorphic -->
<!-- signatures: is_isomorphic(gr1, gr2) -->
### Function: is_isomorphic (gr1, gr2)

Devuelve `true` si los grafos/digrafos *gr1* y *gr2* son
isomorfos y `false` en caso contrario.


Véase también `isomorphism`.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) clk5:complement_graph(line_graph(complete_graph(5)))$
(%i3) is_isomorphic(clk5, petersen_graph());
(%o3)                         true
```

<!-- category: Plotting -->
<!-- keywords: is_planar -->
<!-- signatures: is_planar(gr) -->
### Function: is_planar (gr)

Devuelve `true` si *gr* es un grafo planar y `false` en caso contrario.


El algoritmo utilizado es el de Demoucron, que es de tiempo cuadrático.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) is_planar(dodecahedron_graph());
(%o2)                                true
(%i3) is_planar(petersen_graph());
(%o3)                                false
(%i4) is_planar(petersen_graph(10,2));
(%o4)                                true
```

<!-- category: Plotting -->
<!-- keywords: is_sconnected -->
<!-- signatures: is_sconnected(gr) -->
### Function: is_sconnected (gr)

Devuelve `true` si el grafo orientado *gr* es fuertemente conexo,
devolviendo `false` en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_sconnected(cycle_digraph(5));
(%o2)                               true
(%i3) is_sconnected(path_digraph(5));
(%o3)                               false
```

<!-- category: Plotting -->
<!-- keywords: is_tree -->
<!-- signatures: is_tree(gr) -->
### Function: is_tree (gr)

Devuelve `true` si *gr* es un árbol y `false` en caso contrario.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) is_tree(random_tree(4));
(%o2)                               true
(%i3) is_tree(graph_union(random_tree(4), random_tree(5)));
(%o3)                               false
```

<!-- category: Plotting -->
<!-- keywords: is_vertex_in_graph -->
<!-- signatures: is_vertex_in_graph(v, gr) -->
### Function: is_vertex_in_graph (v, gr)

Devuelve `true` si *v* es un vértice del grafo *g*
y `false` en caso contrario.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_vertex_in_graph(0, c4);
(%o3)                               true
(%i4) is_vertex_in_graph(6, c4);
(%o4)                               false
```

<!-- category: Plotting -->
<!-- keywords: isomorphism -->
<!-- signatures: isomorphism(gr1, gr2) -->
### Function: isomorphism (gr1, gr2)

Devuelve un isomorfismo entre los grafos/digrafos *gr1* y *gr2*.
Si *gr1* y *gr2* no son isomorfos, devuelve una lista vacía.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) clk5:complement_graph(line_graph(complete_graph(5)))$
(%i3) isomorphism(clk5, petersen_graph());
(%o3) [9 -> 0, 2 -> 1, 6 -> 2, 5 -> 3, 0 -> 4, 1 -> 5, 3 -> 6, 
                                          4 -> 7, 7 -> 8, 8 -> 9]
```

<!-- category: Plotting -->
<!-- keywords: laplacian_matrix -->
<!-- signatures: laplacian_matrix(gr) -->
### Function: laplacian_matrix (gr)

Devuelve el laplaciano de la matriz del grafo *gr*.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) laplacian_matrix(cycle_graph(5));
                          [  2   - 1   0    0   - 1 ]
                          [                         ]
                          [ - 1   2   - 1   0    0  ]
                          [                         ]
(%o2)                     [  0   - 1   2   - 1   0  ]
                          [                         ]
                          [  0    0   - 1   2   - 1 ]
                          [                         ]
                          [ - 1   0    0   - 1   2  ]
```

<!-- category: Plotting -->
<!-- keywords: line_graph -->
<!-- signatures: line_graph(g) -->
### Function: line_graph (g)

Devuelve el grafo de línea del grafo *g*.

<!-- category: Plotting -->
<!-- keywords: make_graph -->
<!-- signatures: make_graph(vrt, f), make_graph(vrt, f, oriented) -->
### Function: make_graph (vrt, f)

Crea un grafo por medio de la función de predicado *f*.


*vrt* es una lista o conjunto de vértices o un simplemente un número entero.
Si *vrt* es un número entero, entonces los vértices del grafo serán los
enteros desde 1 hasta *vrt*.


*f* es una función de predicado. Dos vértices *a* y *b* se conectarán
si `f(a,b)=true`.


Si *directed* no es *false*, entonces en grafo será dirigido.


Ejemplo 1:








```maxima
(%i1) load("graphs")$
(%i2) g : make_graph(powerset({1,2,3,4,5}, 2), disjointp)$
(%i3) is_isomorphic(g, petersen_graph());
(%o3)                         true
(%i4) get_vertex_label(1, g);
(%o4)                        {1, 2}
```


Ejemplo 2:









```maxima
(%i1) load("graphs")$
(%i2) f(i, j) := is (mod(j, i)=0)$
(%i3) g : make_graph(20, f, directed=true)$
(%i4) out_neighbors(4, g);
(%o4)                    [8, 12, 16, 20]
(%i5) in_neighbors(18, g);
(%o5)                    [1, 2, 3, 6, 9]
```

<!-- category: Plotting -->
<!-- keywords: max_clique -->
<!-- signatures: max_clique(gr) -->
### Function: max_clique (gr)

Devuelve el clique máximo del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.5)$
(%i3) max_clique(g);
(%o3)       [6, 12, 31, 36, 52, 59, 62, 63, 80]
```

<!-- category: Plotting -->
<!-- keywords: max_degree -->
<!-- signatures: max_degree(gr) -->
### Function: max_degree (gr)

Devuelve el grado máximo de los vértices del grafo *gr* y un 
vértice de grado máximo.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.02)$
(%i3) max_degree(g);
(%o3)                        [6, 79]
(%i4) vertex_degree(95, g);
(%o4)                           3
```

<!-- category: Plotting -->
<!-- keywords: max_flow -->
<!-- signatures: max_flow(net, s, t) -->
### Function: max_flow (net, s, t)

Devuelve el flujo maximal de la red *net* con origen en
*s* y final en *t*.


La función devuelve el valor del flujo maximal y una lista con los
pesos de los arcos del flujo óptimo.


Ejemplo:


Example:





















```maxima
(%i1) load ("graphs")$
(%i2) net : create_graph(
  [1,2,3,4,5,6],
  [[[1,2], 1.0],
   [[1,3], 0.3],
   [[2,4], 0.2],
   [[2,5], 0.3],
   [[3,4], 0.1],
   [[3,5], 0.1],
   [[4,6], 1.0],
   [[5,6], 1.0]],
  directed=true)$
(%i3) [flow_value, flow] : max_flow(net, 1, 6);
(%o3) [0.7, [[[1, 2], 0.5], [[1, 3], 0.2], [[2, 4], 0.2],
[[2, 5], 0.3], [[3, 4], 0.1], [[3, 5], 0.1], [[4, 6], 0.3],
[[5, 6], 0.4]]]
(%i4) fl : 0$
(%i5) for u in out_neighbors(1, net) 
         do fl : fl + assoc([1, u], flow)$
(%i6) fl;
(%o6)                                 0.7
```

<!-- category: Plotting -->
<!-- keywords: max_independent_set -->
<!-- signatures: max_independent_set(gr) -->
### Function: max_independent_set (gr)

Devuelve un conjunto maximal independiente de vértices del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) mi : max_independent_set(d);
(%o3)             [0, 3, 5, 9, 10, 11, 18, 19]
(%i4) draw_graph(d, show_vertices=mi)$
```


(Figure graphs05, Conjunto maximal independiente de un grafo dodecaédrico)

<!-- category: Plotting -->
<!-- keywords: max_matching -->
<!-- signatures: max_matching(gr) -->
### Function: max_matching (gr)

Devuelve un conjunto maximal independiente de aristas del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) m : max_matching(d);
(%o3) [[5, 7], [8, 9], [6, 10], [14, 19], [13, 18], [12, 17], 
                               [11, 16], [0, 15], [3, 4], [1, 2]]
(%i4) draw_graph(d, show_edges=m)$
```


(Figure graphs06, Conjunto maximal independiente de aristas de un grafo dodecaédrico)

<!-- category: Plotting -->
<!-- keywords: min_degree -->
<!-- signatures: min_degree(gr) -->
### Function: min_degree (gr)

Devuelve el grado mínimo de los vértices del grafo *gr* y un 
vértice de grado mínimo.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.1)$
(%i3) min_degree(g);
(%o3)                              [3, 49]
(%i4) vertex_degree(21, g);
(%o4)                                 9
```

<!-- category: Plotting -->
<!-- keywords: min_edge_cut -->
<!-- signatures: min_edge_cut(gr) -->
### Function: min_edge_cut (gr)

Devuelve el mínimo *edge cut* del grafo *gr*. Un *edge cut* es
un conjunto de aristas cuya eliminación aumenta el número de componentes del grafo.


Véase también `edge_connectivity`.

<!-- category: Plotting -->
<!-- keywords: min_vertex_cover -->
<!-- signatures: min_vertex_cover(gr) -->
### Function: min_vertex_cover (gr)

Devuelve el mínimo nodo *covering* del grafo *gr*.

<!-- category: Plotting -->
<!-- keywords: min_vertex_cut -->
<!-- signatures: min_vertex_cut(gr) -->
### Function: min_vertex_cut (gr)

Devuelve el mínimo *vertex cut* del grafo *gr*.


Véase también `vertex_connectivity`.

<!-- category: Plotting -->
<!-- keywords: minimum_spanning_tree -->
<!-- signatures: minimum_spanning_tree(gr) -->
### Function: minimum_spanning_tree (gr)

Devuelve el grafo de expansión mínimo del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(path_graph(10), path_graph(10))$
(%i3) t : minimum_spanning_tree(g)$
(%i4) draw_graph(g, show_edges=edges(t))$
```


(Figure graphs07, Grafo de expansión mínimo de un grafo rectangular)

<!-- category: Plotting -->
<!-- keywords: mycielski_graph -->
<!-- signatures: mycielski_graph(g) -->
### Function: mycielski_graph (g)

Devuelve el grafo de Mycielski del grafo *g*.

<!-- category: Plotting -->
<!-- keywords: neighbors -->
<!-- signatures: neighbors(v, gr) -->
### Function: neighbors (v, gr)

Devuelve la lista de los vecinos del vértice *v* del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) neighbors(3, p);
(%o3)                             [4, 8, 2]
```

<!-- category: Plotting -->
<!-- keywords: new_graph -->
<!-- signatures: new_graph() -->
### Function: new_graph ()

Devuelve el grafo sin vértices ni aristas.

<!-- category: Plotting -->
<!-- keywords: odd_girth -->
<!-- signatures: odd_girth(gr) -->
### Function: odd_girth (gr)

Devuelve la longitud del ciclo impar más corto del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(cycle_graph(4), cycle_graph(7))$
(%i3) girth(g);
(%o3)                                 4
(%i4) odd_girth(g);
(%o4)                                 7
```

<!-- category: Plotting -->
<!-- keywords: out_neighbors -->
<!-- signatures: out_neighbors(v, gr) -->
### Function: out_neighbors (v, gr)

Devuelve la lista de los nodos padres del vértice *v* del grafo
orientado *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                                 [1]
(%i4) out_neighbors(2, p);
(%o4)                                 []
```

<!-- category: Plotting -->
<!-- keywords: path_digraph -->
<!-- signatures: path_digraph(n) -->
### Function: path_digraph (n)

Devuelve el camino dirigido de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: path_graph -->
<!-- signatures: path_graph(n) -->
### Function: path_graph (n)

Devuelve el camino de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: petersen_graph -->
<!-- signatures: petersen_graph(), petersen_graph(n, d) -->
### Function: petersen_graph ()

Devuelve el grafo de Petersen *P_{n,d}*. Los valores por
defecto para *n* y *d* son `n=5` y `d=2`.

<!-- category: Plotting -->
<!-- keywords: planar_embedding -->
<!-- signatures: planar_embedding(gr) -->
### Function: planar_embedding (gr)

Devuelve la lista de caminos faciales en una proyección planar de *gr*,
o `false` si *gr* no es un grafo planar.


El grafo *gr* debe estar biconectado.


El algoritmo utilizado es el de Demoucron, que es de tiempo cuadrático.


Ejemplo:







```maxima
(%i1) load ("graphs")$
(%i2) planar_embedding(grid_graph(3,3));
(%o2) [[3, 6, 7, 8, 5, 2, 1, 0], [4, 3, 0, 1], [3, 4, 7, 6], 
                                      [8, 7, 4, 5], [1, 2, 5, 4]]
```

<!-- category: Plotting -->
<!-- keywords: print_graph -->
<!-- signatures: print_graph(gr) -->
### Function: print_graph (gr)

Muestra alguna información sobre el grafo *gr*.


Ejemplo:











```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(5)$
(%i3) print_graph(c5)$
Graph on 5 vertices with 5 edges.
Adjacencies:
  4 :  0  3
  3 :  4  2
  2 :  3  1
  1 :  2  0
  0 :  4  1
(%i4) dc5 : cycle_digraph(5)$
(%i5) print_graph(dc5)$
Digraph on 5 vertices with 5 arcs.
Adjacencies:
  4 :  0
  3 :  4
  2 :  3
  1 :  2
  0 :  1
(%i6) out_neighbors(0, dc5);
(%o6)                                [1]
```

<!-- category: Plotting -->
<!-- keywords: program -->
<!-- signatures: program -->
### Variable: program

establece el programa para posicionado de vértices del grafo. Puede ser
cualquiera de los programas graphviz (dot, neato, twopi, circ, fdp), *circular* o
*spring_embedding* o *planar_embedding*; *planar_embedding* slo está
disponible para grafos planares 2-conectados. Si `program=spring_embedding`,
se puede especificar un conjunto de vértices de posición fija con la opción 
*fixed_vertices*.

<!-- category: Plotting -->
<!-- keywords: random_bipartite_graph -->
<!-- signatures: random_bipartite_graph(a, b, p) -->
### Function: random_bipartite_graph (a, b, p)

Devuelve un grafo aleatorio bipartido a partir de los vértices `a+b`. Cada
arista se genera con probabilidad *p*.

<!-- category: Plotting -->
<!-- keywords: random_digraph -->
<!-- signatures: random_digraph(n, p) -->
### Function: random_digraph (n, p)

Devuelve un grafo aleatorio dirigido de *n* vértices. Cada arco se presenta
con una probabilidad *p*.

<!-- category: Plotting -->
<!-- keywords: random_graph -->
<!-- signatures: random_graph(n, p) -->
### Function: random_graph (n, p)

Devuelve un grafo aleatorio de *n* vértices. Cada arco se presenta
con una probabilidad *p*.

<!-- category: Plotting -->
<!-- keywords: random_graph1 -->
<!-- signatures: random_graph1(n, m) -->
### Function: random_graph1 (n, m)

Devuelve un grafo aleatorio de *n* vértices y *m* arcos aleatorios.

<!-- category: Plotting -->
<!-- keywords: random_network -->
<!-- signatures: random_network(n, p, w) -->
### Function: random_network (n, p, w)

Devuelve una red aleatoria de *n* vértices. Cada arco se presenta 
con probabilidad *p* y tiene un peso dentro del rango `[0,w]`.
La función devuelve una lista `[network, source, sink]`.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) [net, s, t] : random_network(50, 0.2, 10.0);
(%o2)                         [DIGRAPH, 50, 51]
(%i3) max_flow(net, s, t)$
(%i4) first(%);
(%o4)                   27.65981397932507
```

<!-- category: Plotting -->
<!-- keywords: random_regular_graph -->
<!-- signatures: random_regular_graph(n), random_regular_graph(n, d) -->
### Function: random_regular_graph (n)

Devuelve un grafo aleatorio *d*-regular de *n* vértices. El valor
por defecto para *d* es `d=3`.

<!-- category: Plotting -->
<!-- keywords: random_tournament -->
<!-- signatures: random_tournament(n) -->
### Function: random_tournament (n)

Devuelve un torneo aleatorio de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: random_tree -->
<!-- signatures: random_tree(n) -->
### Function: random_tree (n)

Devuelve un árbol aleatorio de *n* vértices.

<!-- category: Plotting -->
<!-- keywords: redraw -->
<!-- signatures: redraw -->
### Variable: redraw

Valor por defecto: *false*


Si *redraw* vale `true`, las posiciones de los vértices se recalculan
incluso si las posiciones están almacenadas de un dibujo previo del grafo.

<!-- category: Plotting -->
<!-- keywords: remove_edge -->
<!-- signatures: remove_edge(e, gr) -->
### Function: remove_edge (e, gr)

Elimina la arista *e* del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) c3 : cycle_graph(3)$
(%i3) remove_edge([0,1], c3)$
(%i4) print_graph(c3)$
Graph on 3 vertices with 2 edges.
Adjacencies:
  2 :  0  1
  1 :  2
  0 :  2
```

<!-- category: Plotting -->
<!-- keywords: remove_vertex -->
<!-- signatures: remove_vertex(v, gr) -->
### Function: remove_vertex (v, gr)

Elimina el vértice *v* del grafo *gr*.

<!-- category: Plotting -->
<!-- keywords: set_edge_weight -->
<!-- signatures: set_edge_weight(e, w, gr) -->
### Function: set_edge_weight (e, w, gr)

Asigna el peso *w* a la arista *e* del grafo *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1, 2], [[[1,2], 1.2]])$
(%i3) get_edge_weight([1,2], g);
(%o3)                                1.2
(%i4) set_edge_weight([1,2], 2.1, g);
(%o4)                               done
(%i5) get_edge_weight([1,2], g);
(%o5)                                2.1
```

<!-- category: Plotting -->
<!-- keywords: set_vertex_label -->
<!-- signatures: set_vertex_label(v, l, gr) -->
### Function: set_vertex_label (v, l, gr)

Asigna la etiqueta *l* al vértice *v* del grafo *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[1, "One"], [2, "Two"]], [[1,2]])$
(%i3) get_vertex_label(1, g);
(%o3)                                One
(%i4) set_vertex_label(1, "oNE", g);
(%o4)                               done
(%i5) get_vertex_label(1, g);
(%o5)                                oNE
```

<!-- category: Plotting -->
<!-- keywords: shortest_path -->
<!-- signatures: shortest_path(u, v, gr) -->
### Function: shortest_path (u, v, gr)

Devuelve el camino más corto desde *u* hasta *v* del grafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) path : shortest_path(0, 7, d);
(%o3)                          [0, 1, 19, 13, 7]
(%i4) draw_graph(d, show_edges=vertices_to_path(path))$
```


(Figure graphs08, Camino más corto entre dos vértices de un grafo dodecaédrico)

<!-- category: Plotting -->
<!-- keywords: shortest_weighted_path -->
<!-- signatures: shortest_weighted_path(u, v, gr) -->
### Function: shortest_weighted_path (u, v, gr)

Devuelve la longitud del camino más corto ponderado y el propio camino
más corto ponderado desde *u* hasta *v* en el grafo *gr*.


La longitud del camino ponderado es la suma de los pesos de las aristas
del camino. Si una arista no tiene peso asignado, su valor por defecto
es la unidad.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) g: petersen_graph(20, 2)$
(%i3) for e in edges(g) do set_edge_weight(e, random(1.0), g)$
(%i4) shortest_weighted_path(0, 10, g);
(%o4) [2.575143920268482, [0, 20, 38, 36, 34, 32, 30, 10]]
```

<!-- category: Plotting -->
<!-- keywords: show_edge_color -->
<!-- signatures: show_edge_color -->
### Variable: show_edge_color

Color a utilizar en las aristas de la lista *show_edges*.

<!-- category: Plotting -->
<!-- keywords: show_edge_type -->
<!-- signatures: show_edge_type -->
### Variable: show_edge_type

Establece cómo se dibujarán las aristas de *show_edges*.
Véase la opción *line_type* del paquete `draw`.

<!-- category: Plotting -->
<!-- keywords: show_edge_width -->
<!-- signatures: show_edge_width -->
### Variable: show_edge_width

Anchos de las aristas de *show_edges*.

<!-- category: Plotting -->
<!-- keywords: show_edges -->
<!-- signatures: show_edges -->
### Variable: show_edges

Dibuja las aristas de la lista *e_list* con colores diferentes.

<!-- category: Plotting -->
<!-- keywords: show_id -->
<!-- signatures: show_id -->
### Variable: show_id

Valor por defecto: *false*


Si *show_id* vale *true* entonces se muestran los
números identificadores de los vértices.

<!-- category: Plotting -->
<!-- keywords: show_label -->
<!-- signatures: show_label -->
### Variable: show_label

Valor por defecto: *false*


Si *show_label* vale *true* entonces se muestran las
etiquetas de los vértices.

<!-- category: Plotting -->
<!-- keywords: show_vertex_color -->
<!-- signatures: show_vertex_color -->
### Variable: show_vertex_color

Color a utilizar en los vértices de la lista *show_vertices*.

<!-- category: Plotting -->
<!-- keywords: show_vertex_size -->
<!-- signatures: show_vertex_size -->
### Variable: show_vertex_size

Tamanõs de los vértices de *show_vertices*.

<!-- category: Plotting -->
<!-- keywords: show_vertex_type -->
<!-- signatures: show_vertex_type -->
### Variable: show_vertex_type

Establece cómo se mostrarán los vértices de
*show_vertices*. Véase la opción *point_type* del paquete `draw`.

<!-- category: Plotting -->
<!-- keywords: show_vertices -->
<!-- signatures: show_vertices -->
### Variable: show_vertices

Valor por defecto: []


Dibuja los vértices seleccionados en la lista con colores diferentes.

<!-- category: Plotting -->
<!-- keywords: show_weight -->
<!-- signatures: show_weight -->
### Variable: show_weight

Valor por defecto: *false*


si *show_weight* vale *true* entonces se mostrarán 
los pesos de las aristas.

<!-- category: Plotting -->
<!-- keywords: small_rhombicosidodecahedron_graph -->
<!-- signatures: small_rhombicosidodecahedron_graph() -->
### Function: small_rhombicosidodecahedron_graph ()

Devuelve el grafo pequeño rombicosidodecaédrico.

<!-- category: Plotting -->
<!-- keywords: small_rhombicuboctahedron_graph -->
<!-- signatures: small_rhombicuboctahedron_graph() -->
### Function: small_rhombicuboctahedron_graph ()

Devuelve el grafo pequeño rombicocubicooctaédrico.

<!-- category: Plotting -->
<!-- keywords: snub_cube_graph -->
<!-- signatures: snub_cube_graph() -->
### Function: snub_cube_graph ()

Devuelve el grafo cúbico volteado.

<!-- category: Plotting -->
<!-- keywords: snub_dodecahedron_graph -->
<!-- signatures: snub_dodecahedron_graph() -->
### Function: snub_dodecahedron_graph ()

Devuelve el grafo dodecaédrico volteado.

<!-- category: Plotting -->
<!-- keywords: sparse6_decode -->
<!-- signatures: sparse6_decode(str) -->
### Function: sparse6_decode (str)

Devuelve el grafo codificado en formato sparse6 en la cadena *str*.

<!-- category: Plotting -->
<!-- keywords: sparse6_encode -->
<!-- signatures: sparse6_encode(gr) -->
### Function: sparse6_encode (gr)

Devuelve una cadena codificando el grafo *gr* en formato sparse6.

<!-- category: Plotting -->
<!-- keywords: sparse6_export -->
<!-- signatures: sparse6_export(gr_list, fl) -->
### Function: sparse6_export (gr_list, fl)

Exporta los grafos de la lista *gr_list* al fichero *fl* en formato sparse6.

<!-- category: Plotting -->
<!-- keywords: sparse6_import -->
<!-- signatures: sparse6_import(fl) -->
### Function: sparse6_import (fl)

Lee la lista de grafos almacenados en el fichero *fl* en formato sparse6.

<!-- category: Plotting -->
<!-- keywords: spring_embedding_depth -->
<!-- signatures: spring_embedding_depth -->
### Variable: spring_embedding_depth

Valor por defecto: 50


Número de iteraciones del algoritmo de dibujo de grafos.

<!-- category: Plotting -->
<!-- keywords: strong_components -->
<!-- signatures: strong_components(gr) -->
### Function: strong_components (gr)

Devuelve las componentes fuertes del grafo orientado *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) t : random_tournament(4)$
(%i3) strong_components(t);
(%o3)                         [[1], [0], [2], [3]]
(%i4) vertex_out_degree(3, t);
(%o4)                                 3
```

<!-- category: Plotting -->
<!-- keywords: topological_sort -->
<!-- signatures: topological_sort(dag) -->
### Function: topological_sort (dag)

Devuelve el orden topológico de los vértices del grafo orientado *dag*
o una lista vacía si *dag* no es un grafo orientado
acíclico.


Ejemplo:














```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(
         [1,2,3,4,5],
         [
          [1,2], [2,5], [5,3],
          [5,4], [3,4], [1,3]
         ],
         directed=true)$
(%i3) topological_sort(g);
(%o3)                           [1, 2, 5, 3, 4]
```

<!-- category: Plotting -->
<!-- keywords: truncated_cube_graph -->
<!-- signatures: truncated_cube_graph() -->
### Function: truncated_cube_graph ()

Devuelve el grafo cúbico truncado.

<!-- category: Plotting -->
<!-- keywords: truncated_dodecahedron_graph -->
<!-- signatures: truncated_dodecahedron_graph() -->
### Function: truncated_dodecahedron_graph ()

Devuelve el grafo dodecaédrico truncado.

<!-- category: Plotting -->
<!-- keywords: truncated_icosahedron_graph -->
<!-- signatures: truncated_icosahedron_graph() -->
### Function: truncated_icosahedron_graph ()

Devuelve el grafo icosaédrico truncado.

<!-- category: Plotting -->
<!-- keywords: truncated_tetrahedron_graph -->
<!-- signatures: truncated_tetrahedron_graph() -->
### Function: truncated_tetrahedron_graph ()

Devuelve el grafo del tetraedro truncado.

<!-- category: Plotting -->
<!-- keywords: tutte_graph -->
<!-- signatures: tutte_graph() -->
### Function: tutte_graph ()

Devuelve el grafo de Tutte.

<!-- category: Plotting -->
<!-- keywords: underlying_graph -->
<!-- signatures: underlying_graph(g) -->
### Function: underlying_graph (g)

Devuelve el grafo asociado al grafo orientado *g*.

<!-- category: Plotting -->
<!-- keywords: vertex_color -->
<!-- signatures: vertex_color -->
### Variable: vertex_color

Color a utilizar en los vértices.

<!-- category: Plotting -->
<!-- keywords: vertex_coloring -->
<!-- signatures: vertex_coloring(gr) -->
### Function: vertex_coloring (gr)

Devuelve un coloreado óptimo de los vértices del grafo *gr*.


La función devuelve el número cromático y una lista 
representando el coloreado de los vértices de *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) p:petersen_graph()$
(%i3) vertex_coloring(p);
(%o3) [3, [[0, 2], [1, 3], [2, 2], [3, 3], [4, 1], [5, 3], 
                                 [6, 1], [7, 1], [8, 2], [9, 2]]]
```

<!-- category: Plotting -->
<!-- keywords: vertex_connectivity -->
<!-- signatures: vertex_connectivity(g) -->
### Function: vertex_connectivity (g)

Devuelve la conectividad de los vértices del grafo *g*.


Véase también `min_vertex_cut`.

<!-- category: Plotting -->
<!-- keywords: vertex_degree -->
<!-- signatures: vertex_degree(v, gr) -->
### Function: vertex_degree (v, gr)

Devuelve el grado del vértice *v* del grafo *gr*.

<!-- category: Plotting -->
<!-- keywords: vertex_distance -->
<!-- signatures: vertex_distance(u, v, gr) -->
### Function: vertex_distance (u, v, gr)

Devuelve la longitud del camino más corto entre *u* y *v*
del grafo o digrafo *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) vertex_distance(0, 7, d);
(%o3)                                 4
(%i4) shortest_path(0, 7, d);
(%o4)                         [0, 1, 19, 13, 7]
```

<!-- category: Plotting -->
<!-- keywords: vertex_eccentricity -->
<!-- signatures: vertex_eccentricity(v, gr) -->
### Function: vertex_eccentricity (v, gr)

Devuelve la excentricidad del vértice *v* del grafo *gr*.


Ejemplo:








```maxima
(%i1) load ("graphs")$
(%i2) g:cycle_graph(7)$
(%i3) vertex_eccentricity(0, g);
(%o3)                           3
```

<!-- category: Plotting -->
<!-- keywords: vertex_in_degree -->
<!-- signatures: vertex_in_degree(v, gr) -->
### Function: vertex_in_degree (v, gr)

Devuelve el grado de entrada del vértice *v* del grafo 
orientado *gr*.


Ejemplo:










```maxima
(%i1) load ("graphs")$
(%i2) p5 : path_digraph(5)$
(%i3) print_graph(p5)$
Digraph on 5 vertices with 4 arcs.
Adjacencies:
  4 :
  3 :  4
  2 :  3
  1 :  2
  0 :  1
(%i4) vertex_in_degree(4, p5);
(%o4)                                 1
(%i5) in_neighbors(4, p5);
(%o5)                                [3]
```

<!-- category: Plotting -->
<!-- keywords: vertex_out_degree -->
<!-- signatures: vertex_out_degree(v, gr) -->
### Function: vertex_out_degree (v, gr)

Devuelve el grado de salida del vértice *v* del grafo
orientado *gr*.


Ejemplo:









```maxima
(%i1) load ("graphs")$
(%i2) t : random_tournament(10)$
(%i3) vertex_out_degree(0, t);
(%o3)                           2
(%i4) out_neighbors(0, t);
(%o4)                        [7, 1]
```

<!-- category: Plotting -->
<!-- keywords: vertex_partition -->
<!-- signatures: vertex_partition -->
### Variable: vertex_partition

Valor por defecto: []


Una partición `[[v1,v2,...],...,[vk,...,vn]]` de los vértices del grafo. Los 
vértices de cada lista se dibujarán de diferente color.

<!-- category: Plotting -->
<!-- keywords: vertex_size -->
<!-- signatures: vertex_size -->
### Variable: vertex_size

Tamanõ de los vértices.

<!-- category: Plotting -->
<!-- keywords: vertex_type -->
<!-- signatures: vertex_type -->
### Variable: vertex_type

Valor por defecto: *circle*


Establece cómo se mostrarán los vértices. Véase la
opción *point_type* del paquete `draw`.

<!-- category: Plotting -->
<!-- keywords: vertices -->
<!-- signatures: vertices(gr) -->
### Function: vertices (gr)

Devuelve la lista de vértices del grafo *gr*.


Example







```maxima
(%i1) load ("graphs")$
(%i2) vertices(complete_graph(4));
(%o2)                           [3, 2, 1, 0]
```

<!-- category: Plotting -->
<!-- keywords: vertices_to_cycle -->
<!-- signatures: vertices_to_cycle(v_list) -->
### Function: vertices_to_cycle (v_list)

Convierte una lista *v_list* de vértices en la lista de aristas del ciclo
definido por la propia *v_list*.

<!-- category: Plotting -->
<!-- keywords: vertices_to_path -->
<!-- signatures: vertices_to_path(v_list) -->
### Function: vertices_to_path (v_list)

Convierte una lista *v_list* de vértices en la lista de aristas del camino
definido por la propia *v_list*.

<!-- category: Plotting -->
<!-- keywords: wheel_graph -->
<!-- signatures: wheel_graph(n) -->
### Function: wheel_graph (n)

Devuelve el grafo de rueda de *n+1* vértices.

<!-- category: Plotting -->
<!-- keywords: wiener_index -->
<!-- signatures: wiener_index(gr) -->
### Function: wiener_index (gr)

Devuelve el índice de Wiener del grafo *gr*.


Ejemplo:







```maxima
(%i1) wiener_index(dodecahedron_graph());
(%o1)                          500
```

