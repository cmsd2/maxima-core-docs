## graphs

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

### Function: add_vertices (v_list, gr)

Adds all vertices in the list *v_list* to the graph *gr*.
A vertex may be any integer,
and *v_list* may contain vertices in any order.

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

### Function: chromatic_index (gr)

Returns the chromatic index of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) chromatic_index(p);
(%o3)                           4
```

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

### Function: clebsch_graph ()

Returns the Clebsch graph.

### Function: complement_graph (g)

Returns the complement of the graph *g*.

### Function: complete_bipartite_graph (n, m)

Returns the complete bipartite graph on *n+m* vertices.

### Function: complete_graph (n)

Returns the complete graph on *n* vertices.

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

### Function: connected_components (gr)

Returns the (vertex sets of) connected components of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g: graph_union(cycle_graph(5), path_graph(4))$
(%i3) connected_components(g);
(%o3)            [[1, 2, 3, 4, 0], [8, 7, 6, 5]]
```

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

### Function: copy_graph (g)

Returns a copy of the graph *g*.

### Function: create_graph (create_graph, v_list, e_list, create_graph, n, e_list, create_graph, v_list, e_list, directed)

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

### Function: cube_graph (n)

Returns the *n*-dimensional cube.

### Function: cuboctahedron_graph (n)

Returns the cuboctahedron graph.

### Function: cycle_digraph (n)

Returns the directed cycle on *n* vertices.

### Function: cycle_graph (n)

Returns the cycle on *n* vertices.

### Function: degree_sequence (gr)

Returns the list of vertex degrees of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) degree_sequence(random_graph(10, 0.4));
(%o2)            [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

### Function: diameter (gr)

Returns the diameter of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) diameter(dodecahedron_graph());
(%o2)                           5
```

### Function: dimacs_export (dimacs_export, gr, fl, dimacs_export, gr, fl, comment1, ..., commentn)

Exports the graph into the file *fl* in the DIMACS format. Optional
comments will be added to the top of the file.

### Function: dimacs_import (fl)

Returns the graph from file *fl* in the DIMACS format.

### Function: dodecahedron_graph ()

Returns the dodecahedron graph.

### Function: draw_graph (draw_graph, graph, draw_graph, graph, option1, ..., optionk)

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

### Variable: draw_graph_program

Default value: *spring_embedding*


The default value for the program used to position vertices in
`draw_graph` program.

### Variable: edge_color

The color used for displaying edges.

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

### Function: edge_connectivity (gr)

Returns the edge-connectivity of the graph *gr*.


See also `min_edge_cut`.

See also: `min_edge_cut`.

### Variable: edge_partition

A partition `[[e1,e2,...],...,[ek,...,em]]` of edges of the
graph. The edges of each list in the partition will be drawn using a
different color.

### Variable: edge_type

Defines how edges are displayed. See the *line_type* option for the
`draw` package.

### Variable: edge_width

The width of edges.

### Function: edges (gr)

Returns the list of edges (arcs) in a (directed) graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) edges(complete_graph(4));
(%o2)   [[2, 3], [1, 3], [1, 2], [0, 3], [0, 2], [0, 1]]
```

### Function: empty_graph (n)

Returns the empty graph on *n* vertices.

### Variable: fixed_vertices

Specifies a list of vertices which will have positions fixed along a regular polygon.
Can be used when `program=spring_embedding`.

### Function: flower_snark (n)

Returns the flower graph on *4n* vertices.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) f5 : flower_snark(5)$
(%i3) chromatic_index(f5);
(%o3)                           4
```

### Function: from_adjacency_matrix (A)

Returns the graph represented by its adjacency matrix *A*.

### Function: frucht_graph ()

Returns the Frucht graph.

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

### Function: get_edge_weight (get_edge_weight, e, gr, get_edge_weight, e, gr, ifnot)

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

### Function: girth (gr)

Returns the length of the shortest cycle in *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : heawood_graph()$
(%i3) girth(g);
(%o3)                           6
```

### Function: graph6_decode (str)

Returns the graph encoded in the graph6 format in the string *str*.

### Function: graph6_encode (gr)

Returns a string which encodes the graph *gr* in the graph6 format.

### Function: graph6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
graph6 format.

### Function: graph6_import (fl)

Returns a list of graphs from the file *fl* in the graph6 format.

### Function: graph_center (gr)

Returns the center of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_center(g);
(%o3)                         [12]
```

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

### Function: graph_order (gr)

Returns the number of vertices in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_order(p);
(%o3)                          10
```

### Function: graph_periphery (gr)

Returns the periphery of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_periphery(g);
(%o3)                    [24, 20, 4, 0]
```

### Function: graph_product (g1, g1)

Returns the direct product of graphs *g1* and *g2*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) grid : graph_product(path_graph(3), path_graph(4))$
(%i3) draw_graph(grid)$
```


(Figure graphs01, Direct product of two graphs)

### Function: graph_size (gr)

Returns the number of edges in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_size(p);
(%o3)                          15
```

### Function: graph_union (g1, g1)

Returns the union (sum) of graphs *g1* and *g2*.

### Function: great_rhombicosidodecahedron_graph ()

Returns the great rhombicosidodecahedron graph.

### Function: great_rhombicuboctahedron_graph ()

Returns the great rhombicuboctahedron graph.

### Function: grid_graph (n, m)

Returns the *n x m* grid.

### Function: grotzch_graph ()

Returns the Grotzch graph.

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

### Function: heawood_graph ()

Returns the Heawood graph.

### Function: icosahedron_graph ()

Returns the icosahedron graph.

### Function: icosidodecahedron_graph ()

Returns the icosidodecahedron graph.

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

### Function: is_connected (gr)

Returns `true` if the graph *gr* is connected and `false` otherwise.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) is_connected(graph_union(cycle_graph(4), path_graph(3)));
(%o2)                         false
```

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

### Function: line_graph (g)

Returns the line graph of the graph *g*.

### Function: make_graph (make_graph, vrt, f, make_graph, vrt, f, oriented)

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

### Function: max_clique (gr)

Returns a maximum clique of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.5)$
(%i3) max_clique(g);
(%o3)          [6, 12, 31, 36, 52, 59, 62, 63, 80]
```

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

### Function: min_edge_cut (gr)

Returns the minimum edge cut in the graph *gr*.


See also `edge_005fconnectivity`.

See also: `edge_connectivity`.

### Function: min_vertex_cover (gr)

Returns the minimum vertex cover of the graph *gr*.

### Function: min_vertex_cut (gr)

Returns the minimum vertex cut in the graph *gr*.


See also `vertex_005fconnectivity`.

See also: `vertex_connectivity`.

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

### Function: mycielski_graph (g)

Returns the mycielskian graph of the graph *g*.

### Function: neighbors (v, gr)

Returns the list of neighbors of the vertex *v* in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) neighbors(3, p);
(%o3)                       [4, 8, 2]
```

### Function: new_graph ()

Returns the graph with no vertices and no edges.

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

### Function: path_digraph (n)

Returns the directed path on *n* vertices.

### Function: path_graph (n)

Returns the path on *n* vertices.

### Function: petersen_graph (petersen_graph, petersen_graph, n, d)

Returns the petersen graph *P_{n,d}*. The default values for
*n* and *d* are `n=5` and `d=2`.

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

### Variable: program

Defines the program used for positioning vertices of the graph. Can be
one of the graphviz programs (dot, neato, twopi, circ, fdp),
*circular*, *spring_embedding* or
*planar_embedding*. *planar_embedding* is only available for
2-connected planar graphs. When `program=spring_embedding`, a set
of vertices with fixed position can be specified with the
*fixed_vertices* option.

### Function: random_bipartite_graph (a, b, p)

Returns a random bipartite graph on `a+b` vertices. Each edge is
present with probability *p*.

### Function: random_digraph (n, p)

Returns a random directed graph on *n* vertices. Each arc is present
with probability *p*.

### Function: random_graph (n, p)

Returns a random graph on *n* vertices. Each edge is present with
probability *p*.

### Function: random_graph1 (n, m)

Returns a random graph on *n* vertices and random *m* edges.

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

### Function: random_regular_graph (random_regular_graph, n, random_regular_graph, n, d)

Returns a random *d*-regular graph on *n* vertices. The default
value for *d* is `d=3`.

### Function: random_tournament (n)

Returns a random tournament on *n* vertices.

### Function: random_tree (n)

Returns a random tree on *n* vertices.

### Variable: redraw

Default value: *false*


If `true`, vertex positions are recomputed even if the positions
have been saved from a previous drawing of the graph.

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

### Function: remove_vertex (v, gr)

Removes the vertex *v* from the graph *gr*.

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

### Variable: show_edge_color

The color used for displaying edges in the *show_edges* list.

### Variable: show_edge_type

Defines how edges in *show_edges* are displayed. See the
*line_type* option for the `draw` package.

### Variable: show_edge_width

The width of edges in *show_edges*.

### Variable: show_edges

Display edges specified in the list *e_list* using a different
color.

### Variable: show_id

Default value: *false*


If *true* then ids of the vertices are displayed.

### Variable: show_label

Default value: *false*


If *true* then labels of the vertices are displayed.

### Variable: show_vertex_color

The color used for displaying vertices in the *show_vertices* list.

### Variable: show_vertex_size

The size of vertices in *show_vertices*.

### Variable: show_vertex_type

Defines how vertices specified in *show_vertices* are displayed.
See the *point_type* option for the `draw` package for possible
values.

### Variable: show_vertices

Default value: []


Display selected vertices in the using a different color.

### Variable: show_weight

Default value: *false*


If *true* then weights of the edges are displayed.

### Function: small_rhombicosidodecahedron_graph ()

Returns the small rhombicosidodecahedron graph.

### Function: small_rhombicuboctahedron_graph ()

Returns the small rhombicuboctahedron graph.

### Function: snub_cube_graph ()

Returns the snub cube graph.

### Function: snub_dodecahedron_graph ()

Returns the snub dodecahedron graph.

### Function: sparse6_decode (str)

Returns the graph encoded in the sparse6 format in the string *str*.

### Function: sparse6_encode (gr)

Returns a string which encodes the graph *gr* in the sparse6 format.

### Function: sparse6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
sparse6 format.

### Function: sparse6_import (fl)

Returns a list of graphs from the file *fl* in the sparse6 format.

### Variable: spring_embedding_depth

Default value: 50


The number of iterations in the spring embedding graph drawing
algorithm.

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

### Function: truncated_cube_graph ()

Returns the truncated cube graph.

### Function: truncated_dodecahedron_graph ()

Returns the truncated dodecahedron graph.

### Function: truncated_icosahedron_graph ()

Returns the truncated icosahedron graph.

### Function: truncated_tetrahedron_graph ()

Returns the truncated tetrahedron graph.

### Function: tutte_graph ()

Returns the Tutte graph.

### Function: underlying_graph (g)

Returns the underlying graph of the directed graph *g*.

### Variable: vertex_color

The color used for displaying vertices.

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

### Function: vertex_connectivity (g)

Returns the vertex connectivity of the graph *g*.


See also `min_005fvertex_005fcut`.

See also: `min_vertex_cut`.

### Function: vertex_degree (v, gr)

Returns the degree of the vertex *v* in the graph *gr*.

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

### Function: vertex_eccentricity (v, gr)

Returns the eccentricity of the vertex *v* in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g:cycle_graph(7)$
(%i3) vertex_eccentricity(0, g);
(%o3)                           3
```

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

### Variable: vertex_partition

Default value: []


A partition `[[v1,v2,...],...,[vk,...,vn]]` of the vertices of the
graph. The vertices of each list in the partition will be drawn in a
different color.

### Variable: vertex_size

The size of vertices.

### Variable: vertex_type

Default value: *circle*


Defines how vertices are displayed. See the *point_type* option for
the `draw` package for possible values.

### Function: vertices (gr)

Returns the list of vertices in the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) vertices(complete_graph(4));
(%o2)                     [3, 2, 1, 0]
```

### Function: vertices_to_cycle (v_list)

Converts a list *v_list* of vertices to a list of edges of the cycle
defined by *v_list*.

### Function: vertices_to_path (v_list)

Converts a list *v_list* of vertices to a list of edges of the path
defined by *v_list*.

### Function: wheel_graph (n)

Returns the wheel graph on *n+1* vertices.

### Function: wiener_index (gr)

Returns the Wiener index of the graph *gr*.


Example:






```maxima
(%i2) wiener_index(dodecahedron_graph());
(%o2)                          500
```

