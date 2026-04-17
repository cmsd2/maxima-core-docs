## graphs

<!-- category: Plotting -->
<!-- keywords: add_edge -->
<!-- signatures: add_edge(e, gr) -->
### Function: add_edge (e, gr)

Adds the edge *e* to the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) p : path_graph(4)$
(%i3) neighbors(0, p);
(%o3)                          [1]
(%i4) add_edge([0,3], p);
(%o4)                         done
(%i5) neighbors(0, p);
(%o5)                        [3, 1]
```

<!-- category: Plotting -->
<!-- keywords: add_edges -->
<!-- signatures: add_edges(e_list, gr) -->
### Function: add_edges (e_list, gr)

Adds all edges in the list *e_list* to the graph *gr*.


Example:








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

Adds the vertex *v* to the graph *gr*.


Example:








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

Adds all vertices in the list *v_list* to the graph *gr*.
A vertex may be any integer,
and *v_list* may contain vertices in any order.

<!-- category: Plotting -->
<!-- keywords: adjacency_matrix -->
<!-- signatures: adjacency_matrix(gr) -->
### Function: adjacency_matrix (gr)

Returns the adjacency matrix of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(4)$
(%i3) adjacency_matrix(c5);
                         [ 0  1  0  1 ]
                         [            ]
                         [ 1  0  1  0 ]
(%o3)                    [            ]
                         [ 0  1  0  1 ]
                         [            ]
                         [ 1  0  1  0 ]
```

<!-- category: Plotting -->
<!-- keywords: average_degree -->
<!-- signatures: average_degree(gr) -->
### Function: average_degree (gr)

Returns the average degree of vertices in the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) average_degree(grotzch_graph());
                               40
(%o2)                          --
                               11
```

<!-- category: Plotting -->
<!-- keywords: biconnected_components -->
<!-- signatures: biconnected_components(gr) -->
### Function: biconnected_components (gr)

Returns the (vertex sets of) 2-connected components of the graph
*gr*.


Example:












```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(
            [1,2,3,4,5,6,7],
            [
             [1,2],[2,3],[2,4],[3,4],
             [4,5],[5,6],[4,6],[6,7]
            ])$
(%i3) biconnected_components(g);
(%o3)        [[6, 7], [4, 5, 6], [1, 2], [2, 3, 4]]
```


(Figure graphs13, Graph with 2-connected vertices)

<!-- category: Plotting -->
<!-- keywords: bipartition -->
<!-- signatures: bipartition(gr) -->
### Function: bipartition (gr)

Returns a bipartition of the vertices of the graph *gr* or an empty
list if *gr* is not bipartite.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) h : heawood_graph()$
(%i3) [A,B]:bipartition(h);
(%o3)  [[8, 12, 6, 10, 0, 2, 4], [13, 5, 11, 7, 9, 1, 3]]
(%i4) draw_graph(h, show_vertices=A, program=circular)$
```


(Figure graphs02, Bipartition of the vertices in a Heawood graph)

<!-- category: Plotting -->
<!-- keywords: chromatic_index -->
<!-- signatures: chromatic_index(gr) -->
### Function: chromatic_index (gr)

Returns the chromatic index of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) chromatic_index(p);
(%o3)                           4
```

<!-- category: Plotting -->
<!-- keywords: chromatic_number -->
<!-- signatures: chromatic_number(gr) -->
### Function: chromatic_number (gr)

Returns the chromatic number of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) chromatic_number(cycle_graph(5));
(%o2)                           3
(%i3) chromatic_number(cycle_graph(6));
(%o3)                           2
```

<!-- category: Plotting -->
<!-- keywords: circulant_graph -->
<!-- signatures: circulant_graph(n, d) -->
### Function: circulant_graph (n, d)

Returns the circulant graph with parameters *n* and *d*.


Example:







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

Removes the weight of the edge  *e* in the graph *gr*.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(3, [[[0,1], 1.5], [[1,2], 1.3]])$
(%i3) get_edge_weight([0,1], g);
(%o3)                          1.5
(%i4) clear_edge_weight([0,1], g)$
(%i5) get_edge_weight([0,1], g);
(%o5)                           1
```

<!-- category: Plotting -->
<!-- keywords: clear_vertex_label -->
<!-- signatures: clear_vertex_label(v, gr) -->
### Function: clear_vertex_label (v, gr)

Removes the label of the vertex *v* in the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[0,"Zero"], [1, "One"]], [[0,1]])$
(%i3) get_vertex_label(0, g);
(%o3)                         Zero
(%i4) clear_vertex_label(0, g);
(%o4)                         done
(%i5) get_vertex_label(0, g);
(%o5)                         false
```

<!-- category: Plotting -->
<!-- keywords: clebsch_graph -->
<!-- signatures: clebsch_graph() -->
### Function: clebsch_graph ()

Returns the Clebsch graph.

<!-- category: Plotting -->
<!-- keywords: complement_graph -->
<!-- signatures: complement_graph(g) -->
### Function: complement_graph (g)

Returns the complement of the graph *g*.

<!-- category: Plotting -->
<!-- keywords: complete_bipartite_graph -->
<!-- signatures: complete_bipartite_graph(n, m) -->
### Function: complete_bipartite_graph (n, m)

Returns the complete bipartite graph on *n+m* vertices.

<!-- category: Plotting -->
<!-- keywords: complete_graph -->
<!-- signatures: complete_graph(n) -->
### Function: complete_graph (n)

Returns the complete graph on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: connect_vertices -->
<!-- signatures: connect_vertices(v_list, u_list, gr) -->
### Function: connect_vertices (v_list, u_list, gr)

Connects all vertices from the list *v_list* with the vertices in
the list *u_list* in the graph *gr*.


*v_list* and *u_list* can be single vertices or lists of
vertices.


Example:








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

Returns the (vertex sets of) connected components of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g: graph_union(cycle_graph(5), path_graph(4))$
(%i3) connected_components(g);
(%o3)            [[1, 2, 3, 4, 0], [8, 7, 6, 5]]
```

<!-- category: Plotting -->
<!-- keywords: contract_edge -->
<!-- signatures: contract_edge(e, gr) -->
### Function: contract_edge (e, gr)

Contracts the edge *e* in the graph *gr*.


Example:










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

Returns a copy of the graph *g*.

<!-- category: Plotting -->
<!-- keywords: create_graph -->
<!-- signatures: create_graph(v_list, e_list), create_graph(n, e_list), create_graph(v_list, e_list, directed) -->
### Function: create_graph (v_list, e_list)

Creates a new graph on the set of vertices *v_list* and with edges *e_list*.


*v_list* is a list of vertices `[v1, v2, ..., vn]` or a
list of vertices together with vertex labels `[[v1, l1], [v2 ,l2], ..., [vn, ln]]`.
A vertex may be any integer,
and *v_list* may contain vertices in any order.
A label may be any Maxima expression,
and two or more vertices may have the same label.


*n* is the number of vertices. Vertices will be identified by integers from 0 to n-1.


*e_list* is a list of edges `[e1, e2,..., em]` or a list of
edges together with edge-weights `[[e1, w1], ..., [em, wm]]`.


If *directed* is not `false`, a directed graph will be returned.


Example 1: create a cycle on 3 vertices:







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


Example 2: create a cycle on 3 vertices with edge weights:








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


Example 3: create a directed graph:













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

Returns the *n*-dimensional cube.

<!-- category: Plotting -->
<!-- keywords: cuboctahedron_graph -->
<!-- signatures: cuboctahedron_graph(n) -->
### Function: cuboctahedron_graph (n)

Returns the cuboctahedron graph.

<!-- category: Plotting -->
<!-- keywords: cycle_digraph -->
<!-- signatures: cycle_digraph(n) -->
### Function: cycle_digraph (n)

Returns the directed cycle on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: cycle_graph -->
<!-- signatures: cycle_graph(n) -->
### Function: cycle_graph (n)

Returns the cycle on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: degree_sequence -->
<!-- signatures: degree_sequence(gr) -->
### Function: degree_sequence (gr)

Returns the list of vertex degrees of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) degree_sequence(random_graph(10, 0.4));
(%o2)            [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

<!-- category: Plotting -->
<!-- keywords: diameter -->
<!-- signatures: diameter(gr) -->
### Function: diameter (gr)

Returns the diameter of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) diameter(dodecahedron_graph());
(%o2)                           5
```

<!-- category: Plotting -->
<!-- keywords: dimacs_export -->
<!-- signatures: dimacs_export(gr, fl), dimacs_export(gr, fl, comment1, ..., commentn) -->
### Function: dimacs_export (gr, fl)

Exports the graph into the file *fl* in the DIMACS format. Optional
comments will be added to the top of the file.

<!-- category: Plotting -->
<!-- keywords: dimacs_import -->
<!-- signatures: dimacs_import(fl) -->
### Function: dimacs_import (fl)

Returns the graph from file *fl* in the DIMACS format.

<!-- category: Plotting -->
<!-- keywords: dodecahedron_graph -->
<!-- signatures: dodecahedron_graph() -->
### Function: dodecahedron_graph ()

Returns the dodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: draw_graph -->
<!-- signatures: draw_graph(graph), draw_graph(graph, option1, ..., optionk) -->
### Function: draw_graph (graph)

Draws the graph using the `Package-draw` package.


The algorithm used to position vertices is specified by the optional
argument *program*. The default value is
`program=spring_embedding`. *draw_graph* can also use the
graphviz programs for positioning vertices, but graphviz must be
installed separately.


Example 1:












```maxima
(%i1) load ("graphs")$
(%i2) g:grid_graph(10,10)$
(%i3) m:max_matching(g)$
(%i4) draw_graph(g,
   spring_embedding_depth=100,
   show_edges=m, edge_type=dots,
   vertex_size=0)$
```


(Figure graphs09, Example of the use of draw_graph to draw a graph)


Example 2:






















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


(Figure graphs10, Example of the use of draw_graph to draw a graph)


Example 3:
























```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(16,
    [
     [0,1],[1,3],[2,3],[0,2],[3,4],[2,4],
     [5,6],[6,4],[4,7],[6,7],[7,8],[7,10],[7,11],
     [8,10],[11,10],[8,9],[11,12],[9,15],[12,13],
     [10,14],[15,14],[13,14]
    ])$
(%i3) mi : max_independent_set(g)$
(%i4) draw_graph(
    g,
    show_vertices=mi,
    show_vertex_type=filled_up_triangle,
    show_vertex_size=2,
    edge_color=cyan,
    edge_width=3,
    show_id=true,
    text_color=brown
    )$
```


(Figure graphs11, Example of the use of draw_graph to draw a graph)


Example 4:



























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


(Figure graphs12, Example of the use of draw_graph to draw a graph)


Example 5:








```maxima
(%i1) load("graphs")$
(%i2) g: petersen_graph(20, 2);
(%o2)                         GRAPH
(%i3) draw_graph(g, redraw=true, program=planar_embedding);
(%o3)                         done
```


(Figure graphs14, Example of the use of draw_graph to draw a graph)


Example 6:









```maxima
(%i1) load("graphs")$
(%i2) t: tutte_graph();
(%o2)                         GRAPH
(%i3) draw_graph(t, redraw=true, 
                    fixed_vertices=[1,2,3,4,5,6,7,8,9]);
(%o3)                         done
```


(Figure graphs15, Example of the use of draw_graph to draw a graph)

See also: `Package-draw`.

<!-- category: Plotting -->
<!-- keywords: draw_graph_program -->
<!-- signatures: draw_graph_program -->
### Variable: draw_graph_program

Default value: *spring_embedding*


The default value for the program used to position vertices in
`draw_graph` program.

<!-- category: Plotting -->
<!-- keywords: edge_color -->
<!-- signatures: edge_color -->
### Variable: edge_color

The color used for displaying edges.

<!-- category: Plotting -->
<!-- keywords: edge_coloring -->
<!-- signatures: edge_coloring(gr) -->
### Function: edge_coloring (gr)

Returns an optimal coloring of the edges of the graph *gr*.


The function returns the chromatic index and a list representing the
coloring of the edges of *gr*.


Example:









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

Returns the edge-connectivity of the graph *gr*.


See also `min_edge_cut`.

See also: `min_edge_cut`.

<!-- category: Plotting -->
<!-- keywords: edge_partition -->
<!-- signatures: edge_partition -->
### Variable: edge_partition

A partition `[[e1,e2,...],...,[ek,...,em]]` of edges of the
graph. The edges of each list in the partition will be drawn using a
different color.

<!-- category: Plotting -->
<!-- keywords: edge_type -->
<!-- signatures: edge_type -->
### Variable: edge_type

Defines how edges are displayed. See the *line_type* option for the
`draw` package.

<!-- category: Plotting -->
<!-- keywords: edge_width -->
<!-- signatures: edge_width -->
### Variable: edge_width

The width of edges.

<!-- category: Plotting -->
<!-- keywords: edges -->
<!-- signatures: edges(gr) -->
### Function: edges (gr)

Returns the list of edges (arcs) in a (directed) graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) edges(complete_graph(4));
(%o2)   [[2, 3], [1, 3], [1, 2], [0, 3], [0, 2], [0, 1]]
```

<!-- category: Plotting -->
<!-- keywords: empty_graph -->
<!-- signatures: empty_graph(n) -->
### Function: empty_graph (n)

Returns the empty graph on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: fixed_vertices -->
<!-- signatures: fixed_vertices -->
### Variable: fixed_vertices

Specifies a list of vertices which will have positions fixed along a regular polygon.
Can be used when `program=spring_embedding`.

<!-- category: Plotting -->
<!-- keywords: flower_snark -->
<!-- signatures: flower_snark(n) -->
### Function: flower_snark (n)

Returns the flower graph on *4n* vertices.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) f5 : flower_snark(5)$
(%i3) chromatic_index(f5);
(%o3)                           4
```

<!-- category: Plotting -->
<!-- keywords: from_adjacency_matrix -->
<!-- signatures: from_adjacency_matrix(A) -->
### Function: from_adjacency_matrix (A)

Returns the graph represented by its adjacency matrix *A*.

<!-- category: Plotting -->
<!-- keywords: frucht_graph -->
<!-- signatures: frucht_graph() -->
### Function: frucht_graph ()

Returns the Frucht graph.

<!-- category: Plotting -->
<!-- keywords: get_all_vertices_by_label -->
<!-- signatures: get_all_vertices_by_label(l, gr) -->
### Function: get_all_vertices_by_label (l, gr)

Returns all vertices, if any, which have the label *l* in graph *gr*.


If there are no such vertices,
`get_all_vertices_by_label` returns an empty list `[]`.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph ([[0, "Zero"], [1, "One"], [2, "Other"], [3, "Other"]], []) $
(%i3) get_all_vertices_by_label ("Zero", g);
(%o3)                          [0]
(%i4) get_all_vertices_by_label ("Two", g);
(%o4)                          []
(%i5) get_all_vertices_by_label ("Other", g);
(%o5)                        [2, 3]
```

<!-- category: Plotting -->
<!-- keywords: get_edge_weight -->
<!-- signatures: get_edge_weight(e, gr), get_edge_weight(e, gr, ifnot) -->
### Function: get_edge_weight (e, gr)

Returns the weight of the edge *e* in the graph *gr*.


If there is no weight assigned to the edge, the function returns 1. If
the edge is not present in the graph, the function signals an error or
returns the optional argument *ifnot*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(5)$
(%i3) get_edge_weight([1,2], c5);
(%o3)                           1
(%i4) set_edge_weight([1,2], 2.0, c5);
(%o4)                         done
(%i5) get_edge_weight([1,2], c5);
(%o5)                          2.0
```

<!-- category: Plotting -->
<!-- keywords: get_unique_vertex_by_label -->
<!-- signatures: get_unique_vertex_by_label(l, gr) -->
### Function: get_unique_vertex_by_label (l, gr)

Returns the unique vertex which has the label *l* in graph *gr*.


If there is no such vertex,
`get_unique_vertex_by_label` returns `false`.


If there are two or more vertices with label *l*,
`get_unique_vertex_by_label` reports an error.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph ([[0, "Zero"], [1, "One"], [2, "Other"], [3, "Other"]], []) $
(%i3) get_unique_vertex_by_label ("Zero", g);
(%o3)                           0
(%i4) get_unique_vertex_by_label ("Two", g);
(%o4)                         false
(%i5) errcatch (get_unique_vertex_by_label ("Other", g));
get_unique_vertex_by_label: two or more vertices have the same label "Other"
(%o5)                          []
```

<!-- category: Plotting -->
<!-- keywords: get_vertex_label -->
<!-- signatures: get_vertex_label(v, gr) -->
### Function: get_vertex_label (v, gr)

Returns the label of the vertex *v* in the graph *gr*.


If no label is assigned to vertex *v*,
`get_vertex_label` returns `false`.


Example:








```maxima
(%i1) load("graphs")$
(%i2) g: create_graph([[0, "Zero"], [1, "One"], 2, 3], [])$
(%i3) get_vertex_label(0, g);
(%o3)                         Zero
(%i4) get_vertex_label(2, g);
(%o4)                         false
```

<!-- category: Plotting -->
<!-- keywords: girth -->
<!-- signatures: girth(gr) -->
### Function: girth (gr)

Returns the length of the shortest cycle in *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : heawood_graph()$
(%i3) girth(g);
(%o3)                           6
```

<!-- category: Plotting -->
<!-- keywords: graph6_decode -->
<!-- signatures: graph6_decode(str) -->
### Function: graph6_decode (str)

Returns the graph encoded in the graph6 format in the string *str*.

<!-- category: Plotting -->
<!-- keywords: graph6_encode -->
<!-- signatures: graph6_encode(gr) -->
### Function: graph6_encode (gr)

Returns a string which encodes the graph *gr* in the graph6 format.

<!-- category: Plotting -->
<!-- keywords: graph6_export -->
<!-- signatures: graph6_export(gr_list, fl) -->
### Function: graph6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
graph6 format.

<!-- category: Plotting -->
<!-- keywords: graph6_import -->
<!-- signatures: graph6_import(fl) -->
### Function: graph6_import (fl)

Returns a list of graphs from the file *fl* in the graph6 format.

<!-- category: Plotting -->
<!-- keywords: graph_center -->
<!-- signatures: graph_center(gr) -->
### Function: graph_center (gr)

Returns the center of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_center(g);
(%o3)                         [12]
```

<!-- category: Plotting -->
<!-- keywords: graph_charpoly -->
<!-- signatures: graph_charpoly(gr, x) -->
### Function: graph_charpoly (gr, x)

Returns the characteristic polynomial (in variable *x*) of the graph
*gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_charpoly(p, x), factor;
                                   5        4
(%o3)               (x - 3) (x - 1)  (x + 2)
```

<!-- category: Plotting -->
<!-- keywords: graph_eigenvalues -->
<!-- signatures: graph_eigenvalues(gr) -->
### Function: graph_eigenvalues (gr)

Returns the eigenvalues of the graph *gr*. The function returns
eigenvalues in the same format as maxima `eigenvalues` function.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_eigenvalues(p);
(%o3)               [[3, - 2, 1], [1, 4, 5]]
```

See also: `eigenvalues`.

<!-- category: Plotting -->
<!-- keywords: graph_order -->
<!-- signatures: graph_order(gr) -->
### Function: graph_order (gr)

Returns the number of vertices in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_order(p);
(%o3)                          10
```

<!-- category: Plotting -->
<!-- keywords: graph_periphery -->
<!-- signatures: graph_periphery(gr) -->
### Function: graph_periphery (gr)

Returns the periphery of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_periphery(g);
(%o3)                    [24, 20, 4, 0]
```

<!-- category: Plotting -->
<!-- keywords: graph_product -->
<!-- signatures: graph_product(g1, g1) -->
### Function: graph_product (g1, g1)

Returns the direct product of graphs *g1* and *g2*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) grid : graph_product(path_graph(3), path_graph(4))$
(%i3) draw_graph(grid)$
```


(Figure graphs01, Direct product of two graphs)

<!-- category: Plotting -->
<!-- keywords: graph_size -->
<!-- signatures: graph_size(gr) -->
### Function: graph_size (gr)

Returns the number of edges in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_size(p);
(%o3)                          15
```

<!-- category: Plotting -->
<!-- keywords: graph_union -->
<!-- signatures: graph_union(g1, g1) -->
### Function: graph_union (g1, g1)

Returns the union (sum) of graphs *g1* and *g2*.

<!-- category: Plotting -->
<!-- keywords: great_rhombicosidodecahedron_graph -->
<!-- signatures: great_rhombicosidodecahedron_graph() -->
### Function: great_rhombicosidodecahedron_graph ()

Returns the great rhombicosidodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: great_rhombicuboctahedron_graph -->
<!-- signatures: great_rhombicuboctahedron_graph() -->
### Function: great_rhombicuboctahedron_graph ()

Returns the great rhombicuboctahedron graph.

<!-- category: Plotting -->
<!-- keywords: grid_graph -->
<!-- signatures: grid_graph(n, m) -->
### Function: grid_graph (n, m)

Returns the *n x m* grid.

<!-- category: Plotting -->
<!-- keywords: grotzch_graph -->
<!-- signatures: grotzch_graph() -->
### Function: grotzch_graph ()

Returns the Grotzch graph.

<!-- category: Plotting -->
<!-- keywords: hamilton_cycle -->
<!-- signatures: hamilton_cycle(gr) -->
### Function: hamilton_cycle (gr)

Returns the Hamilton cycle of the graph *gr* or an empty list if
*gr* is not hamiltonian.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) c : cube_graph(3)$
(%i3) hc : hamilton_cycle(c);
(%o3)              [7, 3, 2, 6, 4, 0, 1, 5, 7]
(%i4) draw_graph(c, show_edges=vertices_to_cycle(hc))$
```


(Figure graphs03, Hamilton cycle of a cubic graph)

<!-- category: Plotting -->
<!-- keywords: hamilton_path -->
<!-- signatures: hamilton_path(gr) -->
### Function: hamilton_path (gr)

Returns the Hamilton path of the graph *gr* or an empty list if
*gr* does not have a Hamilton path.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) hp : hamilton_path(p);
(%o3)            [0, 5, 7, 2, 1, 6, 8, 3, 4, 9]
(%i4) draw_graph(p, show_edges=vertices_to_path(hp))$
```


(Figure graphs04, Hamilton path of a Petersen graph)

<!-- category: Plotting -->
<!-- keywords: heawood_graph -->
<!-- signatures: heawood_graph() -->
### Function: heawood_graph ()

Returns the Heawood graph.

<!-- category: Plotting -->
<!-- keywords: icosahedron_graph -->
<!-- signatures: icosahedron_graph() -->
### Function: icosahedron_graph ()

Returns the icosahedron graph.

<!-- category: Plotting -->
<!-- keywords: icosidodecahedron_graph -->
<!-- signatures: icosidodecahedron_graph() -->
### Function: icosidodecahedron_graph ()

Returns the icosidodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: in_neighbors -->
<!-- signatures: in_neighbors(v, gr) -->
### Function: in_neighbors (v, gr)

Returns the list of in-neighbors of the vertex *v* in the directed
graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                          [1]
(%i4) out_neighbors(2, p);
(%o4)                          []
```

<!-- category: Plotting -->
<!-- keywords: induced_subgraph -->
<!-- signatures: induced_subgraph(V, g) -->
### Function: induced_subgraph (V, g)

Returns the graph induced on the subset *V* of vertices of the graph
*g*.


Example:









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

Returns `true` if *gr* is 2-connected and `false` otherwise.


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

Returns `true` if *gr* is bipartite (2-colorable) and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_bipartite(petersen_graph());
(%o2)                         false
(%i3) is_bipartite(heawood_graph());
(%o3)                         true
```

<!-- category: Plotting -->
<!-- keywords: is_connected -->
<!-- signatures: is_connected(gr) -->
### Function: is_connected (gr)

Returns `true` if the graph *gr* is connected and `false` otherwise.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) is_connected(graph_union(cycle_graph(4), path_graph(3)));
(%o2)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_digraph -->
<!-- signatures: is_digraph(gr) -->
### Function: is_digraph (gr)

Returns `true` if *gr* is a directed graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_digraph(path_graph(5));
(%o2)                         false
(%i3) is_digraph(path_digraph(5));
(%o3)                         true
```

<!-- category: Plotting -->
<!-- keywords: is_edge_in_graph -->
<!-- signatures: is_edge_in_graph(e, gr) -->
### Function: is_edge_in_graph (e, gr)

Returns `true` if *e* is an edge (arc) in the (directed) graph *g*
and `false` otherwise.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_edge_in_graph([2,3], c4);
(%o3)                         true
(%i4) is_edge_in_graph([3,2], c4);
(%o4)                         true
(%i5) is_edge_in_graph([2,4], c4);
(%o5)                         false
(%i6) is_edge_in_graph([3,2], cycle_digraph(4));
(%o6)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_graph -->
<!-- signatures: is_graph(gr) -->
### Function: is_graph (gr)

Returns `true` if *gr* is a graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_graph(path_graph(5));
(%o2)                         true
(%i3) is_graph(path_digraph(5));
(%o3)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_graph_or_digraph -->
<!-- signatures: is_graph_or_digraph(gr) -->
### Function: is_graph_or_digraph (gr)

Returns `true` if *gr* is a graph or a directed graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_graph_or_digraph(path_graph(5));
(%o2)                         true
(%i3) is_graph_or_digraph(path_digraph(5));
(%o3)                         true
```

<!-- category: Plotting -->
<!-- keywords: is_isomorphic -->
<!-- signatures: is_isomorphic(gr1, gr2) -->
### Function: is_isomorphic (gr1, gr2)

Returns `true` if graphs/digraphs *gr1* and *gr2* are isomorphic
and `false` otherwise.


See also `isomorphism`.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) clk5:complement_graph(line_graph(complete_graph(5)))$
(%i3) is_isomorphic(clk5, petersen_graph());
(%o3)                         true
```

See also: `isomorphism`.

<!-- category: Plotting -->
<!-- keywords: is_planar -->
<!-- signatures: is_planar(gr) -->
### Function: is_planar (gr)

Returns `true` if *gr* is a planar graph and `false` otherwise.


The algorithm used is the Demoucron’s algorithm, which is a quadratic time
algorithm.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) is_planar(dodecahedron_graph());
(%o2)                         true
(%i3) is_planar(petersen_graph());
(%o3)                         false
(%i4) is_planar(petersen_graph(10,2));
(%o4)                         true
```

<!-- category: Plotting -->
<!-- keywords: is_sconnected -->
<!-- signatures: is_sconnected(gr) -->
### Function: is_sconnected (gr)

Returns `true` if the directed graph *gr* is strongly connected and
`false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_sconnected(cycle_digraph(5));
(%o2)                         true
(%i3) is_sconnected(path_digraph(5));
(%o3)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_tree -->
<!-- signatures: is_tree(gr) -->
### Function: is_tree (gr)

Returns `true` if *gr* is a tree and `false`  otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_tree(random_tree(4));
(%o2)                         true
(%i3) is_tree(graph_union(random_tree(4), random_tree(5)));
(%o3)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_vertex_in_graph -->
<!-- signatures: is_vertex_in_graph(v, gr) -->
### Function: is_vertex_in_graph (v, gr)

Returns `true` if *v* is a vertex in the graph *g* and `false`  otherwise.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_vertex_in_graph(0, c4);
(%o3)                         true
(%i4) is_vertex_in_graph(6, c4);
(%o4)                         false
```

<!-- category: Plotting -->
<!-- keywords: isomorphism -->
<!-- signatures: isomorphism(gr1, gr2) -->
### Function: isomorphism (gr1, gr2)

Returns a an isomorphism between graphs/digraphs *gr1* and
*gr2*. If *gr1* and *gr2* are not isomorphic, it returns
an empty list.


Example:







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

Returns the laplacian matrix of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) laplacian_matrix(cycle_graph(5));
                   [  2   - 1   0    0   - 1 ]
                   [                         ]
                   [ - 1   2   - 1   0    0  ]
                   [                         ]
(%o2)              [  0   - 1   2   - 1   0  ]
                   [                         ]
                   [  0    0   - 1   2   - 1 ]
                   [                         ]
                   [ - 1   0    0   - 1   2  ]
```

<!-- category: Plotting -->
<!-- keywords: line_graph -->
<!-- signatures: line_graph(g) -->
### Function: line_graph (g)

Returns the line graph of the graph *g*.

<!-- category: Plotting -->
<!-- keywords: make_graph -->
<!-- signatures: make_graph(vrt, f), make_graph(vrt, f, oriented) -->
### Function: make_graph (vrt, f)

Creates a graph using a predicate function *f*.


*vrt* is a list or set of vertices, or an integer.


When *vrt* is a list or set,
its elements may be any integers,
and, if a list, may be listed in any order.


When *vrt* is an integer,
vertices of the graph will be integers from 1 to *vrt*.


*f* is a predicate function. Two vertices *a* and *b* will
be connected if `f(a,b)=true`.


If *directed* is not *false*, then the graph will be directed.


Example 1:








```maxima
(%i1) load("graphs")$
(%i2) g : make_graph(powerset({1,2,3,4,5}, 2), disjointp)$
(%i3) is_isomorphic(g, petersen_graph());
(%o3)                         true
(%i4) get_vertex_label(1, g);
(%o4)                        {1, 2}
```


Example 2:









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

Returns a maximum clique of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.5)$
(%i3) max_clique(g);
(%o3)          [6, 12, 31, 36, 52, 59, 62, 63, 80]
```

<!-- category: Plotting -->
<!-- keywords: max_degree -->
<!-- signatures: max_degree(gr) -->
### Function: max_degree (gr)

Returns the maximal degree of vertices of the graph *gr* and a
vertex of maximal degree.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.02)$
(%i3) max_degree(g);
(%o3)                        [6, 79]
(%i4) vertex_degree(95, g);
(%o4)                           2
```

<!-- category: Plotting -->
<!-- keywords: max_flow -->
<!-- signatures: max_flow(net, s, t) -->
### Function: max_flow (net, s, t)

Returns a maximum flow through the network *net* with the source
*s* and the sink *t*.


The function returns the value of the maximal flow and a list
representing the weights of the arcs in the optimal flow.


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
(%o6)                          0.7
```

<!-- category: Plotting -->
<!-- keywords: max_independent_set -->
<!-- signatures: max_independent_set(gr) -->
### Function: max_independent_set (gr)

Returns a maximum independent set of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) mi : max_independent_set(d);
(%o3)             [0, 3, 5, 9, 10, 11, 18, 19]
(%i4) draw_graph(d, show_vertices=mi)$
```


(Figure graphs05, Maximum independent set of a dodecahedral graph)

<!-- category: Plotting -->
<!-- keywords: max_matching -->
<!-- signatures: max_matching(gr) -->
### Function: max_matching (gr)

Returns a maximum matching of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) m : max_matching(d);
(%o3) [[5, 7], [8, 9], [6, 10], [14, 19], [13, 18], [12, 17], 
                               [11, 16], [0, 15], [3, 4], [1, 2]]
(%i4) draw_graph(d, show_edges=m)$
```


(Figure graphs06, Maximum matching of a dodecahedral graph)

<!-- category: Plotting -->
<!-- keywords: min_degree -->
<!-- signatures: min_degree(gr) -->
### Function: min_degree (gr)

Returns the minimum degree of vertices of the graph *gr* and a
vertex of minimum degree.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.1)$
(%i3) min_degree(g);
(%o3)                        [3, 49]
(%i4) vertex_degree(21, g);
(%o4)                           9
```

<!-- category: Plotting -->
<!-- keywords: min_edge_cut -->
<!-- signatures: min_edge_cut(gr) -->
### Function: min_edge_cut (gr)

Returns the minimum edge cut in the graph *gr*.


See also `edge_005fconnectivity`.

See also: `edge_connectivity`.

<!-- category: Plotting -->
<!-- keywords: min_vertex_cover -->
<!-- signatures: min_vertex_cover(gr) -->
### Function: min_vertex_cover (gr)

Returns the minimum vertex cover of the graph *gr*.

<!-- category: Plotting -->
<!-- keywords: min_vertex_cut -->
<!-- signatures: min_vertex_cut(gr) -->
### Function: min_vertex_cut (gr)

Returns the minimum vertex cut in the graph *gr*.


See also `vertex_005fconnectivity`.

See also: `vertex_connectivity`.

<!-- category: Plotting -->
<!-- keywords: minimum_spanning_tree -->
<!-- signatures: minimum_spanning_tree(gr) -->
### Function: minimum_spanning_tree (gr)

Returns the minimum spanning tree of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(path_graph(10), path_graph(10))$
(%i3) t : minimum_spanning_tree(g)$
(%i4) draw_graph(g, show_edges=edges(t))$
```


(Figure graphs07, Minimum spanning of rectangular graph)

<!-- category: Plotting -->
<!-- keywords: mycielski_graph -->
<!-- signatures: mycielski_graph(g) -->
### Function: mycielski_graph (g)

Returns the mycielskian graph of the graph *g*.

<!-- category: Plotting -->
<!-- keywords: neighbors -->
<!-- signatures: neighbors(v, gr) -->
### Function: neighbors (v, gr)

Returns the list of neighbors of the vertex *v* in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) neighbors(3, p);
(%o3)                       [4, 8, 2]
```

<!-- category: Plotting -->
<!-- keywords: new_graph -->
<!-- signatures: new_graph() -->
### Function: new_graph ()

Returns the graph with no vertices and no edges.

<!-- category: Plotting -->
<!-- keywords: odd_girth -->
<!-- signatures: odd_girth(gr) -->
### Function: odd_girth (gr)

Returns the length of the shortest odd cycle in the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(cycle_graph(4), cycle_graph(7))$
(%i3) girth(g);
(%o3)                           4
(%i4) odd_girth(g);
(%o4)                           7
```

<!-- category: Plotting -->
<!-- keywords: out_neighbors -->
<!-- signatures: out_neighbors(v, gr) -->
### Function: out_neighbors (v, gr)

Returns the list of out-neighbors of the vertex *v* in the directed
graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                          [1]
(%i4) out_neighbors(2, p);
(%o4)                          []
```

<!-- category: Plotting -->
<!-- keywords: path_digraph -->
<!-- signatures: path_digraph(n) -->
### Function: path_digraph (n)

Returns the directed path on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: path_graph -->
<!-- signatures: path_graph(n) -->
### Function: path_graph (n)

Returns the path on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: petersen_graph -->
<!-- signatures: petersen_graph(), petersen_graph(n, d) -->
### Function: petersen_graph ()

Returns the petersen graph *P_{n,d}*. The default values for
*n* and *d* are `n=5` and `d=2`.

<!-- category: Plotting -->
<!-- keywords: planar_embedding -->
<!-- signatures: planar_embedding(gr) -->
### Function: planar_embedding (gr)

Returns the list of facial walks in a planar embedding of *gr* and
`false` if *gr* is not a planar graph.


The graph *gr* must be biconnected.


The algorithm used is the Demoucron’s algorithm, which is a quadratic time
algorithm.


Example:






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

Prints some information about the graph *gr*.


Example:










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
(%o6)                          [1]
```

<!-- category: Plotting -->
<!-- keywords: program -->
<!-- signatures: program -->
### Variable: program

Defines the program used for positioning vertices of the graph. Can be
one of the graphviz programs (dot, neato, twopi, circ, fdp),
*circular*, *spring_embedding* or
*planar_embedding*. *planar_embedding* is only available for
2-connected planar graphs. When `program=spring_embedding`, a set
of vertices with fixed position can be specified with the
*fixed_vertices* option.

<!-- category: Plotting -->
<!-- keywords: random_bipartite_graph -->
<!-- signatures: random_bipartite_graph(a, b, p) -->
### Function: random_bipartite_graph (a, b, p)

Returns a random bipartite graph on `a+b` vertices. Each edge is
present with probability *p*.

<!-- category: Plotting -->
<!-- keywords: random_digraph -->
<!-- signatures: random_digraph(n, p) -->
### Function: random_digraph (n, p)

Returns a random directed graph on *n* vertices. Each arc is present
with probability *p*.

<!-- category: Plotting -->
<!-- keywords: random_graph -->
<!-- signatures: random_graph(n, p) -->
### Function: random_graph (n, p)

Returns a random graph on *n* vertices. Each edge is present with
probability *p*.

<!-- category: Plotting -->
<!-- keywords: random_graph1 -->
<!-- signatures: random_graph1(n, m) -->
### Function: random_graph1 (n, m)

Returns a random graph on *n* vertices and random *m* edges.

<!-- category: Plotting -->
<!-- keywords: random_network -->
<!-- signatures: random_network(n, p, w) -->
### Function: random_network (n, p, w)

Returns a random network on *n* vertices. Each arc is present with
probability *p* and has a weight in the range `[0,w]`. The
function returns a list `[network, source, sink]`.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) [net, s, t] : random_network(50, 0.2, 10.0);
(%o2)                   [DIGRAPH, 50, 51]
(%i3) max_flow(net, s, t)$
(%i4) first(%);
(%o4)                   27.65981397932507
```

<!-- category: Plotting -->
<!-- keywords: random_regular_graph -->
<!-- signatures: random_regular_graph(n), random_regular_graph(n, d) -->
### Function: random_regular_graph (n)

Returns a random *d*-regular graph on *n* vertices. The default
value for *d* is `d=3`.

<!-- category: Plotting -->
<!-- keywords: random_tournament -->
<!-- signatures: random_tournament(n) -->
### Function: random_tournament (n)

Returns a random tournament on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: random_tree -->
<!-- signatures: random_tree(n) -->
### Function: random_tree (n)

Returns a random tree on *n* vertices.

<!-- category: Plotting -->
<!-- keywords: redraw -->
<!-- signatures: redraw -->
### Variable: redraw

Default value: *false*


If `true`, vertex positions are recomputed even if the positions
have been saved from a previous drawing of the graph.

<!-- category: Plotting -->
<!-- keywords: remove_edge -->
<!-- signatures: remove_edge(e, gr) -->
### Function: remove_edge (e, gr)

Removes the edge *e* from the graph *gr*.


Example:








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

Removes the vertex *v* from the graph *gr*.

<!-- category: Plotting -->
<!-- keywords: set_edge_weight -->
<!-- signatures: set_edge_weight(e, w, gr) -->
### Function: set_edge_weight (e, w, gr)

Assigns the weight *w* to the edge *e* in the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1, 2], [[[1,2], 1.2]])$
(%i3) get_edge_weight([1,2], g);
(%o3)                          1.2
(%i4) set_edge_weight([1,2], 2.1, g);
(%o4)                         done
(%i5) get_edge_weight([1,2], g);
(%o5)                          2.1
```

<!-- category: Plotting -->
<!-- keywords: set_vertex_label -->
<!-- signatures: set_vertex_label(v, l, gr) -->
### Function: set_vertex_label (v, l, gr)

Assigns the label *l* to the vertex *v* in the graph *gr*.


A label may be any Maxima expression,
and two or more vertices may have the same label.


Example:











```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[1, "One"], [2, "Two"]], [[1, 2]])$
(%i3) get_vertex_label(1, g);
(%o3)                          One
(%i4) set_vertex_label(1, "oNE", g);
(%o4)                         done
(%i5) get_vertex_label(1, g);
(%o5)                          oNE
(%i6) h : create_graph([[11, x], [22, y], [33, x + y]], [[11, 33], [22, 33]]) $
(%i7) get_vertex_label (33, h);
(%o7)                         y + x
```

<!-- category: Plotting -->
<!-- keywords: shortest_path -->
<!-- signatures: shortest_path(u, v, gr) -->
### Function: shortest_path (u, v, gr)

Returns the shortest path from *u* to *v* in the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) path : shortest_path(0, 7, d);
(%o3)                   [0, 1, 19, 13, 7]
(%i4) draw_graph(d, show_edges=vertices_to_path(path))$
```


(Figure graphs08, Shortest path between two vertices in a dodecahedral graph)

<!-- category: Plotting -->
<!-- keywords: shortest_weighted_path -->
<!-- signatures: shortest_weighted_path(u, v, gr) -->
### Function: shortest_weighted_path (u, v, gr)

Returns the length of the shortest weighted path and the shortest
weighted path from *u* to *v* in the graph *gr*.


The length of a weighted path is the sum of edge weights of edges in the
path. If an edge has no weight, then it has a default weight 1.


Example:









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

The color used for displaying edges in the *show_edges* list.

<!-- category: Plotting -->
<!-- keywords: show_edge_type -->
<!-- signatures: show_edge_type -->
### Variable: show_edge_type

Defines how edges in *show_edges* are displayed. See the
*line_type* option for the `draw` package.

<!-- category: Plotting -->
<!-- keywords: show_edge_width -->
<!-- signatures: show_edge_width -->
### Variable: show_edge_width

The width of edges in *show_edges*.

<!-- category: Plotting -->
<!-- keywords: show_edges -->
<!-- signatures: show_edges -->
### Variable: show_edges

Display edges specified in the list *e_list* using a different
color.

<!-- category: Plotting -->
<!-- keywords: show_id -->
<!-- signatures: show_id -->
### Variable: show_id

Default value: *false*


If *true* then ids of the vertices are displayed.

<!-- category: Plotting -->
<!-- keywords: show_label -->
<!-- signatures: show_label -->
### Variable: show_label

Default value: *false*


If *true* then labels of the vertices are displayed.

<!-- category: Plotting -->
<!-- keywords: show_vertex_color -->
<!-- signatures: show_vertex_color -->
### Variable: show_vertex_color

The color used for displaying vertices in the *show_vertices* list.

<!-- category: Plotting -->
<!-- keywords: show_vertex_size -->
<!-- signatures: show_vertex_size -->
### Variable: show_vertex_size

The size of vertices in *show_vertices*.

<!-- category: Plotting -->
<!-- keywords: show_vertex_type -->
<!-- signatures: show_vertex_type -->
### Variable: show_vertex_type

Defines how vertices specified in *show_vertices* are displayed.
See the *point_type* option for the `draw` package for possible
values.

<!-- category: Plotting -->
<!-- keywords: show_vertices -->
<!-- signatures: show_vertices -->
### Variable: show_vertices

Default value: []


Display selected vertices in the using a different color.

<!-- category: Plotting -->
<!-- keywords: show_weight -->
<!-- signatures: show_weight -->
### Variable: show_weight

Default value: *false*


If *true* then weights of the edges are displayed.

<!-- category: Plotting -->
<!-- keywords: small_rhombicosidodecahedron_graph -->
<!-- signatures: small_rhombicosidodecahedron_graph() -->
### Function: small_rhombicosidodecahedron_graph ()

Returns the small rhombicosidodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: small_rhombicuboctahedron_graph -->
<!-- signatures: small_rhombicuboctahedron_graph() -->
### Function: small_rhombicuboctahedron_graph ()

Returns the small rhombicuboctahedron graph.

<!-- category: Plotting -->
<!-- keywords: snub_cube_graph -->
<!-- signatures: snub_cube_graph() -->
### Function: snub_cube_graph ()

Returns the snub cube graph.

<!-- category: Plotting -->
<!-- keywords: snub_dodecahedron_graph -->
<!-- signatures: snub_dodecahedron_graph() -->
### Function: snub_dodecahedron_graph ()

Returns the snub dodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: sparse6_decode -->
<!-- signatures: sparse6_decode(str) -->
### Function: sparse6_decode (str)

Returns the graph encoded in the sparse6 format in the string *str*.

<!-- category: Plotting -->
<!-- keywords: sparse6_encode -->
<!-- signatures: sparse6_encode(gr) -->
### Function: sparse6_encode (gr)

Returns a string which encodes the graph *gr* in the sparse6 format.

<!-- category: Plotting -->
<!-- keywords: sparse6_export -->
<!-- signatures: sparse6_export(gr_list, fl) -->
### Function: sparse6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
sparse6 format.

<!-- category: Plotting -->
<!-- keywords: sparse6_import -->
<!-- signatures: sparse6_import(fl) -->
### Function: sparse6_import (fl)

Returns a list of graphs from the file *fl* in the sparse6 format.

<!-- category: Plotting -->
<!-- keywords: spring_embedding_depth -->
<!-- signatures: spring_embedding_depth -->
### Variable: spring_embedding_depth

Default value: 50


The number of iterations in the spring embedding graph drawing
algorithm.

<!-- category: Plotting -->
<!-- keywords: strong_components -->
<!-- signatures: strong_components(gr) -->
### Function: strong_components (gr)

Returns the strong components of a directed graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) t : random_tournament(4)$
(%i3) strong_components(t);
(%o3)                 [[1], [0], [2], [3]]
(%i4) vertex_out_degree(3, t);
(%o4)                           3
```

<!-- category: Plotting -->
<!-- keywords: topological_sort -->
<!-- signatures: topological_sort(dag) -->
### Function: topological_sort (dag)

Returns a topological sorting of the vertices of a directed graph
*dag* or an empty list if *dag* is not a directed acyclic graph.


Example:













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
(%o3)                    [1, 2, 5, 3, 4]
```

<!-- category: Plotting -->
<!-- keywords: truncated_cube_graph -->
<!-- signatures: truncated_cube_graph() -->
### Function: truncated_cube_graph ()

Returns the truncated cube graph.

<!-- category: Plotting -->
<!-- keywords: truncated_dodecahedron_graph -->
<!-- signatures: truncated_dodecahedron_graph() -->
### Function: truncated_dodecahedron_graph ()

Returns the truncated dodecahedron graph.

<!-- category: Plotting -->
<!-- keywords: truncated_icosahedron_graph -->
<!-- signatures: truncated_icosahedron_graph() -->
### Function: truncated_icosahedron_graph ()

Returns the truncated icosahedron graph.

<!-- category: Plotting -->
<!-- keywords: truncated_tetrahedron_graph -->
<!-- signatures: truncated_tetrahedron_graph() -->
### Function: truncated_tetrahedron_graph ()

Returns the truncated tetrahedron graph.

<!-- category: Plotting -->
<!-- keywords: tutte_graph -->
<!-- signatures: tutte_graph() -->
### Function: tutte_graph ()

Returns the Tutte graph.

<!-- category: Plotting -->
<!-- keywords: underlying_graph -->
<!-- signatures: underlying_graph(g) -->
### Function: underlying_graph (g)

Returns the underlying graph of the directed graph *g*.

<!-- category: Plotting -->
<!-- keywords: vertex_color -->
<!-- signatures: vertex_color -->
### Variable: vertex_color

The color used for displaying vertices.

<!-- category: Plotting -->
<!-- keywords: vertex_coloring -->
<!-- signatures: vertex_coloring(gr) -->
### Function: vertex_coloring (gr)

Returns an optimal coloring of the vertices of the graph *gr*.


The function returns the chromatic number and a list representing the
coloring of the vertices of *gr*.


Example:







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

Returns the vertex connectivity of the graph *g*.


See also `min_005fvertex_005fcut`.

See also: `min_vertex_cut`.

<!-- category: Plotting -->
<!-- keywords: vertex_degree -->
<!-- signatures: vertex_degree(v, gr) -->
### Function: vertex_degree (v, gr)

Returns the degree of the vertex *v* in the graph *gr*.

<!-- category: Plotting -->
<!-- keywords: vertex_distance -->
<!-- signatures: vertex_distance(u, v, gr) -->
### Function: vertex_distance (u, v, gr)

Returns the length of the shortest path between *u* and *v* in
the (directed) graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) vertex_distance(0, 7, d);
(%o3)                           4
(%i4) shortest_path(0, 7, d);
(%o4)                   [0, 1, 19, 13, 7]
```

<!-- category: Plotting -->
<!-- keywords: vertex_eccentricity -->
<!-- signatures: vertex_eccentricity(v, gr) -->
### Function: vertex_eccentricity (v, gr)

Returns the eccentricity of the vertex *v* in the graph *gr*.


Example:







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

Returns the in-degree of the vertex *v* in the directed graph *gr*.


Example:









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
(%o4)                           1
(%i5) in_neighbors(4, p5);
(%o5)                          [3]
```

<!-- category: Plotting -->
<!-- keywords: vertex_out_degree -->
<!-- signatures: vertex_out_degree(v, gr) -->
### Function: vertex_out_degree (v, gr)

Returns the out-degree of the vertex *v* in the directed graph *gr*.


Example:








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

Default value: []


A partition `[[v1,v2,...],...,[vk,...,vn]]` of the vertices of the
graph. The vertices of each list in the partition will be drawn in a
different color.

<!-- category: Plotting -->
<!-- keywords: vertex_size -->
<!-- signatures: vertex_size -->
### Variable: vertex_size

The size of vertices.

<!-- category: Plotting -->
<!-- keywords: vertex_type -->
<!-- signatures: vertex_type -->
### Variable: vertex_type

Default value: *circle*


Defines how vertices are displayed. See the *point_type* option for
the `draw` package for possible values.

<!-- category: Plotting -->
<!-- keywords: vertices -->
<!-- signatures: vertices(gr) -->
### Function: vertices (gr)

Returns the list of vertices in the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) vertices(complete_graph(4));
(%o2)                     [3, 2, 1, 0]
```

<!-- category: Plotting -->
<!-- keywords: vertices_to_cycle -->
<!-- signatures: vertices_to_cycle(v_list) -->
### Function: vertices_to_cycle (v_list)

Converts a list *v_list* of vertices to a list of edges of the cycle
defined by *v_list*.

<!-- category: Plotting -->
<!-- keywords: vertices_to_path -->
<!-- signatures: vertices_to_path(v_list) -->
### Function: vertices_to_path (v_list)

Converts a list *v_list* of vertices to a list of edges of the path
defined by *v_list*.

<!-- category: Plotting -->
<!-- keywords: wheel_graph -->
<!-- signatures: wheel_graph(n) -->
### Function: wheel_graph (n)

Returns the wheel graph on *n+1* vertices.

<!-- category: Plotting -->
<!-- keywords: wiener_index -->
<!-- signatures: wiener_index(gr) -->
### Function: wiener_index (gr)

Returns the Wiener index of the graph *gr*.


Example:






```maxima
(%i2) wiener_index(dodecahedron_graph());
(%o2)                          500
```

