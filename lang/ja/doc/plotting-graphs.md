## graphs

<!-- category: Plotting -->
<!-- keywords: add_edge -->
<!-- signatures: add_edge(e, gr) -->
### Function: add_edge (e, gr)

辺 *e*をグラフ *gr*に加えます。


例:









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

リスト *e_list*の中の辺すべてをグラフ *gr*に加えます。


例:








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

頂点 *v*をグラフ *gr*に加えます。


例:








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

リスト *v_list*の中の頂点すべてをグラフ *gr*に加えます。

<!-- category: Plotting -->
<!-- keywords: adjacency_matrix -->
<!-- signatures: adjacency_matrix(gr) -->
### Function: adjacency_matrix (gr)

グラフ *gr*の隣接行列を返します。


例:







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

グラフ *gr*に関する平均次数を返します。


例:






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

グラフ *gr*の2連結成分(の頂点集合)を返します


例:












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

<!-- category: Plotting -->
<!-- keywords: bipartition -->
<!-- signatures: bipartition(gr) -->
### Function: bipartition (gr)

グラフ *gr*の頂点の2分割か、もし *gr*が2部でないなら空のリストを返します。


例:









```maxima
(%i1) load ("graphs")$
(%i2) h : heawood_graph()$
(%i3) [A,B]:bipartition(h);
(%o3)  [[8, 12, 6, 10, 0, 2, 4], [13, 5, 11, 7, 9, 1, 3]]
(%i4) draw_graph(h, show_vertices=A, program=circular)$
```

<!-- category: Plotting -->
<!-- keywords: chromatic_index -->
<!-- signatures: chromatic_index(gr) -->
### Function: chromatic_index (gr)

グラフ *gr*の彩色指数を返します。


例:







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

グラフ *gr*の彩色数を返します。


例:







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

パラメータ *n*と *d*を持つ巡回グラフを返します。


例:







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

グラフ *gr*の辺  *e*の重みを削除します。


例:










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

グラフ *gr*の頂点 *v*のラベルを削除します。


例:









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

Clebschグラフを返します。

<!-- category: Plotting -->
<!-- keywords: complement_graph -->
<!-- signatures: complement_graph(g) -->
### Function: complement_graph (g)

グラフ *g*の補グラフを返します。

<!-- category: Plotting -->
<!-- keywords: complete_bipartite_graph -->
<!-- signatures: complete_bipartite_graph(n, m) -->
### Function: complete_bipartite_graph (n, m)

*n+m*この頂点上の完全2部グラフを返します。

<!-- category: Plotting -->
<!-- keywords: complete_graph -->
<!-- signatures: complete_graph(n) -->
### Function: complete_graph (n)

*n*この頂点上の完全グラフを返します。

<!-- category: Plotting -->
<!-- keywords: connect_vertices -->
<!-- signatures: connect_vertices(v_list, u_list, gr) -->
### Function: connect_vertices (v_list, u_list, gr)

グラフ *gr*に関して、
リスト *v_list*内の頂点すべてを
リスト *u_list*内の頂点に連結します。



*v_list*と *u_list*は1つの頂点か、頂点のリストを取り得ます。


例:








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

グラフ *gr*の連携成分(の頂点集合)を返します。


例:







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

グラフ *gr*の辺 *e*を縮約します。


例:










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

グラフ*g*のコピーを返します。

<!-- category: Plotting -->
<!-- keywords: create_graph -->
<!-- signatures: create_graph(v_list, e_list), create_graph(n, e_list), create_graph(v_list, e_list, directed) -->
### Function: create_graph (v_list, e_list)

頂点の集合*v_list*上に辺*e_list*を使って新しいグラフを生成します。


*v_list*は頂点のリスト(`[v1, v2,..., vn]`)もしくは
頂点ラベルを持つ頂点のリスト(`[[v1,l1], [v2,l2],..., [vn,ln]]`)です。


*n*は頂点の数です。
頂点は0からn-1までの整数で識別されます。
(訳注: 1から始まるMaximaのリストの添字の慣例とは異なることに注意してください。)


*e_list*は辺のリスト(`[e1, e2,..., em]`)もしくは
辺の重みを持つ辺のリスト(`[[e1, w1], ..., [em, wm]]`)です。


もし*directed*が`false`でないなら、
有向グラフが返されます。


例1: 頂点3つの循環を生成する。







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


例2: 辺の重みを持つ頂点3つの循環を生成する。








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


例3: 有向グラフを生成する:













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

*n*次元立方体を返します。

<!-- category: Plotting -->
<!-- keywords: cuboctahedron_graph -->
<!-- signatures: cuboctahedron_graph(n) -->
### Function: cuboctahedron_graph (n)

立方八面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: cycle_digraph -->
<!-- signatures: cycle_digraph(n) -->
### Function: cycle_digraph (n)

*n*個の頂点上の有向グラフを返します。

<!-- category: Plotting -->
<!-- keywords: cycle_graph -->
<!-- signatures: cycle_graph(n) -->
### Function: cycle_graph (n)

*n*この頂点上の閉路を返します。

<!-- category: Plotting -->
<!-- keywords: degree_sequence -->
<!-- signatures: degree_sequence(gr) -->
### Function: degree_sequence (gr)

グラフ *gr*の頂点次数のリストを返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) degree_sequence(random_graph(10, 0.4));
(%o2)            [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

<!-- category: Plotting -->
<!-- keywords: diameter -->
<!-- signatures: diameter(gr) -->
### Function: diameter (gr)

グラフ *gr*の直径を返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) diameter(dodecahedron_graph());
(%o2)                           5
```

<!-- category: Plotting -->
<!-- keywords: dimacs_export -->
<!-- signatures: dimacs_export(gr, fl), dimacs_export(gr, fl, comment1, ..., commentn) -->
### Function: dimacs_export (gr, fl)

グラフをファイル *fl*にDIMACSフォーマットでエクスポートします。
オプションのコメントはファイルの頭に加えられます。

<!-- category: Plotting -->
<!-- keywords: dimacs_import -->
<!-- signatures: dimacs_import(fl) -->
### Function: dimacs_import (fl)

DIMACSフォーマットのファイル *fl*からグラフを返します。

<!-- category: Plotting -->
<!-- keywords: dodecahedron_graph -->
<!-- signatures: dodecahedron_graph() -->
### Function: dodecahedron_graph ()

十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: draw_graph -->
<!-- signatures: draw_graph(graph), draw_graph(graph, option1, ..., optionk) -->
### Function: draw_graph (graph)

`draw`パッケージを使ってグラフを描画します。


頂点を配置するのに使われるアルゴリズムは
オプション引数 *program*で指定されます。
デフォルト値は `program=spring_embedding`です。
*draw_graph*は
頂点を配置するのにgraphvizプログラムも使うことができますが、
graphvizを別途インストールしなければいけません。


例 1:












```maxima
(%i1) load ("graphs")$
(%i2) g:grid_graph(10,10)$
(%i3) m:max_matching(g)$
(%i4) draw_graph(g,
   spring_embedding_depth=100,
   show_edges=m, edge_type=dots,
   vertex_size=0)$
```



例 2:






















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



例 3:
























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



例 4:



























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



例 5:








```maxima
(%i1) load("graphs")$
(%i2) g: petersen_graph(20, 2);
(%o2)                         GRAPH
(%i3) draw_graph(g, redraw=true, program=planar_embedding);
(%o3)                         done
```



例 6:









```maxima
(%i1) load("graphs")$
(%i2) t: tutte_graph();
(%o2)                         GRAPH
(%i3) draw_graph(t, redraw=true, 
                    fixed_vertices=[1,2,3,4,5,6,7,8,9]);
(%o3)                         done
```

<!-- category: Plotting -->
<!-- keywords: draw_graph_program -->
<!-- signatures: draw_graph_program -->
### Variable: draw_graph_program

デフォルト値: *spring_embedding*


頂点を配置するのに使われるプログラムのデフォルト値は
`draw_graph`プログラムです。

<!-- category: Plotting -->
<!-- keywords: edge_color -->
<!-- signatures: edge_color -->
### Variable: edge_color

辺を表示するのに使われる色。

<!-- category: Plotting -->
<!-- keywords: edge_coloring -->
<!-- signatures: edge_coloring(gr) -->
### Function: edge_coloring (gr)

グラフ *gr*の辺の最適色づけを返します。


関数は彩色指数と*gr*の辺の色付けを表すリストを返します。



例:









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

グラフ *gr*の辺連結性を返します。


`min_edge_cut`も参照してください。

<!-- category: Plotting -->
<!-- keywords: edge_partition -->
<!-- signatures: edge_partition -->
### Variable: edge_partition

グラフの辺の分割 `[[e1,e2,...],...,[ek,...,em]]`
分割内のそれぞれのリストの辺は異なる色を使って描画されます。

<!-- category: Plotting -->
<!-- keywords: edge_type -->
<!-- signatures: edge_type -->
### Variable: edge_type

辺をいかに表示するか定義します。
`draw`パッケージの*line_type*オプションを参照してください。

<!-- category: Plotting -->
<!-- keywords: edge_width -->
<!-- signatures: edge_width -->
### Variable: edge_width

辺の幅。

<!-- category: Plotting -->
<!-- keywords: edges -->
<!-- signatures: edges(gr) -->
### Function: edges (gr)

(有向)グラフ *gr*の辺(弧)のリストを返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) edges(complete_graph(4));
(%o2)   [[2, 3], [1, 3], [1, 2], [0, 3], [0, 2], [0, 1]]
```

<!-- category: Plotting -->
<!-- keywords: empty_graph -->
<!-- signatures: empty_graph(n) -->
### Function: empty_graph (n)

*n*個の頂点上の空グラフを返します。

<!-- category: Plotting -->
<!-- keywords: fixed_vertices -->
<!-- signatures: fixed_vertices -->
### Variable: fixed_vertices

正多角形沿いに固定された位置を持つ頂点のリストを指定します。
`program=spring_embedding`の時、使うことができます。

<!-- category: Plotting -->
<!-- keywords: flower_snark -->
<!-- signatures: flower_snark(n) -->
### Function: flower_snark (n)

*4n*個の頂点上の花グラフを返します。


例:







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

隣接行列 *A*で表現されるグラフを返します。

<!-- category: Plotting -->
<!-- keywords: frucht_graph -->
<!-- signatures: frucht_graph() -->
### Function: frucht_graph ()

Fruchtグラフを返します。

<!-- category: Plotting -->
<!-- keywords: get_edge_weight -->
<!-- signatures: get_edge_weight(e, gr), get_edge_weight(e, gr, ifnot) -->
### Function: get_edge_weight (e, gr)

グラフ *gr*の辺 *e*の重みを返します。


もし辺に割り当てられた重みがないなら、
関数は1を返します。
もし辺がグラフの中に存在しないなら、
関数はエラーをシグナルするか、オプション引数 *ifnot*を返します。


例:









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
<!-- keywords: get_vertex_label -->
<!-- signatures: get_vertex_label(v, gr) -->
### Function: get_vertex_label (v, gr)

グラフ *gr*の頂点 *v*のラベルを返します。


例:







```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[0,"Zero"], [1, "One"]], [[0,1]])$
(%i3) get_vertex_label(0, g);
(%o3)                         Zero
```

<!-- category: Plotting -->
<!-- keywords: girth -->
<!-- signatures: girth(gr) -->
### Function: girth (gr)

*gr*の最短閉路の長さを返します。


例:







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

文字列 *str*にgraph6フォーマットで符号化されたグラフを返します。

<!-- category: Plotting -->
<!-- keywords: graph6_encode -->
<!-- signatures: graph6_encode(gr) -->
### Function: graph6_encode (gr)

グラフ *gr*をgraph6フォーマットに符号化した文字列を返します。

<!-- category: Plotting -->
<!-- keywords: graph6_export -->
<!-- signatures: graph6_export(gr_list, fl) -->
### Function: graph6_export (gr_list, fl)

リスト *gr_list*内のグラフをファイル *fl*に
graph6フォーマットでエクスポートします。

<!-- category: Plotting -->
<!-- keywords: graph6_import -->
<!-- signatures: graph6_import(fl) -->
### Function: graph6_import (fl)

graph6フォーマットのファイル *fl*からグラフのリストを返します。

<!-- category: Plotting -->
<!-- keywords: graph_center -->
<!-- signatures: graph_center(gr) -->
### Function: graph_center (gr)

グラフ *gr*の中心を返します。


例:







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

グラフ *gr*の(変数 *x*に関する)特性多項式を返します。


例:







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

グラフ *gr*の固有値を返します。
関数は
maxima `eigenvalue`関数と同じフォーマットで固有値を返します。


例:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_eigenvalues(p);
(%o3)               [[3, - 2, 1], [1, 4, 5]]
```

<!-- category: Plotting -->
<!-- keywords: graph_order -->
<!-- signatures: graph_order(gr) -->
### Function: graph_order (gr)

グラフ *gr*の頂点の数を返します。


例:







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

グラフ *gr*の外周を返します。


例:







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

グラフ *g1*と *g2*の直積を返します。


例:







```maxima
(%i1) load ("graphs")$
(%i2) grid : graph_product(path_graph(3), path_graph(4))$
(%i3) draw_graph(grid)$
```

<!-- category: Plotting -->
<!-- keywords: graph_size -->
<!-- signatures: graph_size(gr) -->
### Function: graph_size (gr)

グラフ *gr*の辺の数を返します。


例:







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

グラフ*g1*と *g2*の和を返します。

<!-- category: Plotting -->
<!-- keywords: great_rhombicosidodecahedron_graph -->
<!-- signatures: great_rhombicosidodecahedron_graph() -->
### Function: great_rhombicosidodecahedron_graph ()

大菱形二十・十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: great_rhombicuboctahedron_graph -->
<!-- signatures: great_rhombicuboctahedron_graph() -->
### Function: great_rhombicuboctahedron_graph ()

大斜方立方八面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: grid_graph -->
<!-- signatures: grid_graph(n, m) -->
### Function: grid_graph (n, m)

*n x m*グリッドを返します。

<!-- category: Plotting -->
<!-- keywords: grotzch_graph -->
<!-- signatures: grotzch_graph() -->
### Function: grotzch_graph ()

Grotzchグラフを返します。

<!-- category: Plotting -->
<!-- keywords: hamilton_cycle -->
<!-- signatures: hamilton_cycle(gr) -->
### Function: hamilton_cycle (gr)

グラフ *gr*のHamilton閉路を返します。
もし *gr*がハミルトニアンでないなら、空のリストを返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) c : cube_graph(3)$
(%i3) hc : hamilton_cycle(c);
(%o3)              [7, 3, 2, 6, 4, 0, 1, 5, 7]
(%i4) draw_graph(c, show_edges=vertices_to_cycle(hc))$
```

<!-- category: Plotting -->
<!-- keywords: hamilton_path -->
<!-- signatures: hamilton_path(gr) -->
### Function: hamilton_path (gr)

グラフ *gr*のHamilton経路を返します。
もし *gr*がHamilton経路を持たないなら、空のリストを返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) hp : hamilton_path(p);
(%o3)            [0, 5, 7, 2, 1, 6, 8, 3, 4, 9]
(%i4) draw_graph(p, show_edges=vertices_to_path(hp))$
```

<!-- category: Plotting -->
<!-- keywords: heawood_graph -->
<!-- signatures: heawood_graph() -->
### Function: heawood_graph ()

Heawoodグラフを返します。

<!-- category: Plotting -->
<!-- keywords: icosahedron_graph -->
<!-- signatures: icosahedron_graph() -->
### Function: icosahedron_graph ()

二十面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: icosidodecahedron_graph -->
<!-- signatures: icosidodecahedron_graph() -->
### Function: icosidodecahedron_graph ()

二十・十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: in_neighbors -->
<!-- signatures: in_neighbors(v, gr) -->
### Function: in_neighbors (v, gr)

有向グラフ *gr*の頂点 *v*の内隣接点のリストを返します。


例:








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

グラフ *g*の頂点の部分集合 *V*上の誘導部分グラフを返します。


例:









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

もし *gr*が2連結なら `true`を、
そうでないなら、 `false`を返します。


例:







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

もし *gr*が2部(2彩色)なら `true`を、
そうでないなら、 `false`を返します。


例:







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

もしグラフ *gr*が連結なら `true`を、
そうでないなら `false`を返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) is_connected(graph_union(cycle_graph(4), path_graph(3)));
(%o2)                         false
```

<!-- category: Plotting -->
<!-- keywords: is_digraph -->
<!-- signatures: is_digraph(gr) -->
### Function: is_digraph (gr)

もし *gr*が有向グラフなら `true`を、
そうでないなら `false`を返します。


例:







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

もし *e*が(有向)グラフ *g*の辺(弧)なら `true`を、
そうでないなら `false`を返します。


例:










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

もし *gr*がグラフなら `true`を、
そうでないなら `false`を返します。


例:







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

もし *gr*がグラフか有向グラフなら `true`を、
そうでないなら `false`を返します。


例:







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

もし グラフ/有向グラフ *gr1*と *gr2*が同型なら `true`を、
そうでないなら `false`を返します。


`isomorphism`も参照してください。


例:







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

もし *gr*が平面グラフなら `true`を、
そうでないなら `false`を返します。


使われているアルゴリズムはDemoucronのアルゴリズムです。
これは二次時間アルゴリズムです。


例:








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

もし有向グラフ *gr*が強連結なら `true`を、
そうでないなら `false`を返します。


例:







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

もし *gr*が木なら `true`を、
そうでないなら `false`を返します。


例:







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

もし *v*がグラフ *g*の頂点なら `true`を、
そうでないなら `false`を返します。


例:








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

グラフ/有向グラフ *gr1*と *gr2*の間の同型写像を返します。
もし *gr1*と *gr2*が同型でないなら、空のリストを返します。


例:







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

グラフ *gr*のLaplace行列を返します。


例:






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

グラフ *g*の折れ線グラフを返します。

<!-- category: Plotting -->
<!-- keywords: make_graph -->
<!-- signatures: make_graph(vrt, f), make_graph(vrt, f, oriented) -->
### Function: make_graph (vrt, f)

述語論理関数 *f*を使ってグラフを生成します。


*vrt*は頂点か整数のリスト/集合です。
もし *vrt*が整数なら、
グラフの頂点は1から *vrt*までの整数です。


*f*は述語論理関数です。
2つの頂点 *a*と *b*は
もし `f(a,b)=true`なら結合されます。


もし *directed*が *false*でないなら、
グラフは有向です。


例 1:








```maxima
(%i1) load("graphs")$
(%i2) g : make_graph(powerset({1,2,3,4,5}, 2), disjointp)$
(%i3) is_isomorphic(g, petersen_graph());
(%o3)                         true
(%i4) get_vertex_label(1, g);
(%o4)                        {1, 2}
```


例 2:









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

グラフ *gr*の最大クリークを返します。


例:







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

グラフ *gr*の頂点の最大次数と最大次数の頂点を返します。


例:








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

ソース *s*とシンク *t*を持ち
ネットワーク *net*を通る最大フローを返します。


関数は最大フローの値と
最適フローで弧の重みを表現するリストを返します。


例:





















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

グラフ *gr*の最大独立集合を返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) mi : max_independent_set(d);
(%o3)             [0, 3, 5, 9, 10, 11, 18, 19]
(%i4) draw_graph(d, show_vertices=mi)$
```

<!-- category: Plotting -->
<!-- keywords: max_matching -->
<!-- signatures: max_matching(gr) -->
### Function: max_matching (gr)

グラフ *gr*の最大マッチングを返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) m : max_matching(d);
(%o3) [[5, 7], [8, 9], [6, 10], [14, 19], [13, 18], [12, 17], 
                               [11, 16], [0, 15], [3, 4], [1, 2]]
(%i4) draw_graph(d, show_edges=m)$
```

<!-- category: Plotting -->
<!-- keywords: min_degree -->
<!-- signatures: min_degree(gr) -->
### Function: min_degree (gr)

グラフ *gr*の頂点の最小次数と最小次数の頂点を返します。


例:








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

グラフ *gr*の最小切断辺を返します。


`edge_connectivity`も参照してください。

<!-- category: Plotting -->
<!-- keywords: min_vertex_cover -->
<!-- signatures: min_vertex_cover(gr) -->
### Function: min_vertex_cover (gr)

グラフ *gr*の最小頂点被覆を返します。

<!-- category: Plotting -->
<!-- keywords: min_vertex_cut -->
<!-- signatures: min_vertex_cut(gr) -->
### Function: min_vertex_cut (gr)

Returns the minimum vertex cut in the graph
グラフ *gr*の最小頂点切断を返します。


`vertex_connectivity`も参照してください。

<!-- category: Plotting -->
<!-- keywords: minimum_spanning_tree -->
<!-- signatures: minimum_spanning_tree(gr) -->
### Function: minimum_spanning_tree (gr)

グラフ *gr*の最小全域木を返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(path_graph(10), path_graph(10))$
(%i3) t : minimum_spanning_tree(g)$
(%i4) draw_graph(g, show_edges=edges(t))$
```

<!-- category: Plotting -->
<!-- keywords: mycielski_graph -->
<!-- signatures: mycielski_graph(g) -->
### Function: mycielski_graph (g)

グラフ *g*のMycielskiグラフを返します。

<!-- category: Plotting -->
<!-- keywords: neighbors -->
<!-- signatures: neighbors(v, gr) -->
### Function: neighbors (v, gr)

グラフ *gr*の頂点 *v*の隣接点のリストを返します。


例:







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

頂点も辺も持たないグラフを返します。

<!-- category: Plotting -->
<!-- keywords: odd_girth -->
<!-- signatures: odd_girth(gr) -->
### Function: odd_girth (gr)

グラフ *gr*の最短奇閉路の長さを返します。


例:








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

有向グラフ *gr*の頂点 *v*の外隣接点のリストを返します。


例:








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

*n*個の頂点上の有向道を返します。

<!-- category: Plotting -->
<!-- keywords: path_graph -->
<!-- signatures: path_graph(n) -->
### Function: path_graph (n)

*n*個の頂点上の道を返します。

<!-- category: Plotting -->
<!-- keywords: petersen_graph -->
<!-- signatures: petersen_graph(), petersen_graph(n, d) -->
### Function: petersen_graph ()

Petersenグラフ *P_{n,d}*を返します。
*n*と *d*のデフォルト値は
`n=5`と `d=2`です。

<!-- category: Plotting -->
<!-- keywords: planar_embedding -->
<!-- signatures: planar_embedding(gr) -->
### Function: planar_embedding (gr)

*gr*の平面埋め込みでのfacial walkのリストを返します。
もし *gr*が平面グラフでないなら `false`を返します。


グラフ *gr*は2連結でなければいけません。


使われるアルゴリズムはDemoucronのアルゴリズムです。
これは二次時間アルゴリズムです。


例:






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

グラフ *gr*についてのある情報を印字します。


例:










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

グラフの頂点を配置するのに使われるプログラムを定義します。
graphvizプログラム (dot, neato, twopi, circ, fdp)の1つ,
*circular*, *spring_embedding*, *planar_embedding*を取り得ます。
2連結平面グラフでは *planar_embedding*だけが利用可能です。
`program=spring_embedding`の時、
固定位置の頂点の集合が *fixed_vertices*オプションで指定可能です。

<!-- category: Plotting -->
<!-- keywords: radius -->
<!-- signatures: radius(gr) -->
### Function: radius (gr)

グラフ *gr*の半径を返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) radius(dodecahedron_graph());
(%o2)                           5
```

<!-- category: Plotting -->
<!-- keywords: random_bipartite_graph -->
<!-- signatures: random_bipartite_graph(a, b, p) -->
### Function: random_bipartite_graph (a, b, p)

`a+b`個の頂点上のランダムな2部グラフを返します。
辺それぞれは確率 *p*で存在します。

<!-- category: Plotting -->
<!-- keywords: random_digraph -->
<!-- signatures: random_digraph(n, p) -->
### Function: random_digraph (n, p)

`n`個の頂点上のランダムな有向グラフを返します。
弧それぞれは確率 *p*で存在します。

<!-- category: Plotting -->
<!-- keywords: random_graph -->
<!-- signatures: random_graph(n, p) -->
### Function: random_graph (n, p)

*n*個の頂点上のランダムグラフを返します。
辺それぞれは確率 *p*で存在します。

<!-- category: Plotting -->
<!-- keywords: random_graph1 -->
<!-- signatures: random_graph1(n, m) -->
### Function: random_graph1 (n, m)

*n*個の頂点とランダムな *m*個の辺上のランダムグラフを返します。

<!-- category: Plotting -->
<!-- keywords: random_network -->
<!-- signatures: random_network(n, p, w) -->
### Function: random_network (n, p, w)

*n*個の頂点上のランダムネットワークを返します。
弧それぞれは確率 *p*で存在し、
範囲 `[0,w]`の中に重みを持ちます。
関数はリスト `[network, source, sink]`を返します。


例:








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

*n*個の頂点上の
ランダムな*d*正則グラフを返します。
*d*のデフォルト値は `d=3`です。

<!-- category: Plotting -->
<!-- keywords: random_tournament -->
<!-- signatures: random_tournament(n) -->
### Function: random_tournament (n)

*n*個の頂点上のランダムなトーナメントを返します。

<!-- category: Plotting -->
<!-- keywords: random_tree -->
<!-- signatures: random_tree(n) -->
### Function: random_tree (n)

*n*個の頂点上のランダムな木を返します。

<!-- category: Plotting -->
<!-- keywords: redraw -->
<!-- signatures: redraw -->
### Variable: redraw

デフォルト値: *false*


もし `true`なら、
たとえ位置がグラフの以前の描画から保存されていても頂点位置が再計算されます。

<!-- category: Plotting -->
<!-- keywords: remove_edge -->
<!-- signatures: remove_edge(e, gr) -->
### Function: remove_edge (e, gr)

グラフ *gr*から辺 *e*を削除します。


例:








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

グラフ *gr*から頂点 *v*を削除します。

<!-- category: Plotting -->
<!-- keywords: set_edge_weight -->
<!-- signatures: set_edge_weight(e, w, gr) -->
### Function: set_edge_weight (e, w, gr)

グラフ *gr*の辺 *e*に重み *w*を割り当てます。


例:









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

グラフ *gr*の頂点 *v*にラベル *l*を割り当てます。



例:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[1, "One"], [2, "Two"]], [[1,2]])$
(%i3) get_vertex_label(1, g);
(%o3)                          One
(%i4) set_vertex_label(1, "oNE", g);
(%o4)                         done
(%i5) get_vertex_label(1, g);
(%o5)                          oNE
```

<!-- category: Plotting -->
<!-- keywords: shortest_path -->
<!-- signatures: shortest_path(u, v, gr) -->
### Function: shortest_path (u, v, gr)

グラフ *gr*の *u*から *v*までの最短経路を返します。


例:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) path : shortest_path(0, 7, d);
(%o3)                   [0, 1, 19, 13, 7]
(%i4) draw_graph(d, show_edges=vertices_to_path(path))$
```

<!-- category: Plotting -->
<!-- keywords: shortest_weighted_path -->
<!-- signatures: shortest_weighted_path(u, v, gr) -->
### Function: shortest_weighted_path (u, v, gr)

グラフ *gr*の *u*から *v*までの最短重み付き経路とその長さを返します。


重み付き経路の長さは経路内の辺の辺重みの和です。
もし辺に重みがないなら、辺はデフォルト重み1を持ちます。


例:









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

*show_edges*リスト内の辺を表示するのに使う色。

<!-- category: Plotting -->
<!-- keywords: show_edge_type -->
<!-- signatures: show_edge_type -->
### Variable: show_edge_type

*show_edges*内の辺を以下に表示するかを定義します。
`draw`パッケージの*line_type*オプションを参照してください。

<!-- category: Plotting -->
<!-- keywords: show_edge_width -->
<!-- signatures: show_edge_width -->
### Variable: show_edge_width

*show_edges*内の辺の幅。

<!-- category: Plotting -->
<!-- keywords: show_edges -->
<!-- signatures: show_edges -->
### Variable: show_edges

異なる色を使ってリスト *e_list*内で指定された辺を表示する。

<!-- category: Plotting -->
<!-- keywords: show_id -->
<!-- signatures: show_id -->
### Variable: show_id

デフォルト値: *false*


もし *true*なら頂点のidが表示されます。

<!-- category: Plotting -->
<!-- keywords: show_label -->
<!-- signatures: show_label -->
### Variable: show_label

デフォルト値: *false*


もし *true*なら頂点のラベルが表示されます。

<!-- category: Plotting -->
<!-- keywords: show_vertex_color -->
<!-- signatures: show_vertex_color -->
### Variable: show_vertex_color

*show_vertices*リスト内の頂点を表示するのに使う色。

<!-- category: Plotting -->
<!-- keywords: show_vertex_size -->
<!-- signatures: show_vertex_size -->
### Variable: show_vertex_size

*show_vertices*内の頂点のサイズ

<!-- category: Plotting -->
<!-- keywords: show_vertex_type -->
<!-- signatures: show_vertex_type -->
### Variable: show_vertex_type

*show_vertices*で指定された頂点をいかに表示するか定義します。
可能な値については、
`draw`パッケージの *point_type*オプションを参照してください。

<!-- category: Plotting -->
<!-- keywords: show_vertices -->
<!-- signatures: show_vertices -->
### Variable: show_vertices

デフォルト値: []


選択された頂点を異なる色を使って表示。

<!-- category: Plotting -->
<!-- keywords: show_weight -->
<!-- signatures: show_weight -->
### Variable: show_weight

デフォルト値: *false*


もし *true*なら辺の重みを表示します。

<!-- category: Plotting -->
<!-- keywords: small_rhombicosidodecahedron_graph -->
<!-- signatures: small_rhombicosidodecahedron_graph() -->
### Function: small_rhombicosidodecahedron_graph ()

斜方二十・十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: small_rhombicuboctahedron_graph -->
<!-- signatures: small_rhombicuboctahedron_graph() -->
### Function: small_rhombicuboctahedron_graph ()

斜方立方八面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: snub_cube_graph -->
<!-- signatures: snub_cube_graph() -->
### Function: snub_cube_graph ()

変形立方体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: snub_dodecahedron_graph -->
<!-- signatures: snub_dodecahedron_graph() -->
### Function: snub_dodecahedron_graph ()

変形十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: sparse6_decode -->
<!-- signatures: sparse6_decode(str) -->
### Function: sparse6_decode (str)

文字列 *str*にsparse6フォーマットで符号化されたグラフを返します。

<!-- category: Plotting -->
<!-- keywords: sparse6_encode -->
<!-- signatures: sparse6_encode(gr) -->
### Function: sparse6_encode (gr)

グラフ *gr*をsparse6フォーマットに符号化した文字列を返します。

<!-- category: Plotting -->
<!-- keywords: sparse6_export -->
<!-- signatures: sparse6_export(gr_list, fl) -->
### Function: sparse6_export (gr_list, fl)

リスト *gr_list*内のグラフを
ファイル *fl*にsparse6フォーマットでエクスポートします。

<!-- category: Plotting -->
<!-- keywords: sparse6_import -->
<!-- signatures: sparse6_import(fl) -->
### Function: sparse6_import (fl)

sparse6フォーマットのファイル *fl*からグラフのリストを返します。

<!-- category: Plotting -->
<!-- keywords: spring_embedding_depth -->
<!-- signatures: spring_embedding_depth -->
### Variable: spring_embedding_depth

デフォルト値: 50


バネ埋め込みグラフ描画アルゴリズムでの繰り返し回数

<!-- category: Plotting -->
<!-- keywords: strong_components -->
<!-- signatures: strong_components(gr) -->
### Function: strong_components (gr)

有向グラフ *gr*の強成分を返します。


例:








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
有向グラフ *dag*の頂点のトポロジカルソートを返します。
もし *dag*が有向無閉路グラフなら空のリストを返します。


例:













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

切頂六面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: truncated_dodecahedron_graph -->
<!-- signatures: truncated_dodecahedron_graph() -->
### Function: truncated_dodecahedron_graph ()

切頂十二面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: truncated_icosahedron_graph -->
<!-- signatures: truncated_icosahedron_graph() -->
### Function: truncated_icosahedron_graph ()

切頂二十面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: truncated_tetrahedron_graph -->
<!-- signatures: truncated_tetrahedron_graph() -->
### Function: truncated_tetrahedron_graph ()

切頂四面体グラフを返します。

<!-- category: Plotting -->
<!-- keywords: tutte_graph -->
<!-- signatures: tutte_graph() -->
### Function: tutte_graph ()

Tutteグラフを返します。

<!-- category: Plotting -->
<!-- keywords: underlying_graph -->
<!-- signatures: underlying_graph(g) -->
### Function: underlying_graph (g)

有向グラフ *g*の台グラフを返します。

<!-- category: Plotting -->
<!-- keywords: vertex_color -->
<!-- signatures: vertex_color -->
### Variable: vertex_color

頂点を表示するのに使う色。

<!-- category: Plotting -->
<!-- keywords: vertex_coloring -->
<!-- signatures: vertex_coloring(gr) -->
### Function: vertex_coloring (gr)

グラフ *gr*の頂点の最適色付けを返します。


関数は、彩色数と *gr*の頂点の色付けを表すリストを返します。


例:







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

グラフ *g*の頂点連結性を返します。


`min_vertex_cut`も参照してください。

<!-- category: Plotting -->
<!-- keywords: vertex_degree -->
<!-- signatures: vertex_degree(v, gr) -->
### Function: vertex_degree (v, gr)

グラフ *gr*の頂点 *v*の次数を返します。

<!-- category: Plotting -->
<!-- keywords: vertex_distance -->
<!-- signatures: vertex_distance(u, v, gr) -->
### Function: vertex_distance (u, v, gr)

(有向)グラフ *gr*の *u*と *v*の間の最短経路の長さを返します。


例:








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

グラフ *gr*の頂点 *v*の離心率を返します。


例:







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

有向グラフ *gr*の頂点 *v*の内次数を返します。


例:









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

有向グラフ *gr*の頂点 *v*の外次数を返します。


例:








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

デフォルト値: []


グラフの頂点の分割 `[[v1,v2,...],...,[vk,...,vn]]`
分割内のそれぞれのリストの頂点は異なる色で描画されます。

<!-- category: Plotting -->
<!-- keywords: vertex_size -->
<!-- signatures: vertex_size -->
### Variable: vertex_size

頂点のサイズ。

<!-- category: Plotting -->
<!-- keywords: vertex_type -->
<!-- signatures: vertex_type -->
### Variable: vertex_type

デフォルト値: *circle*


頂点をいかに表示するか定義します。
可能な値に関しては、
`draw`パッケージの *point_type*オプションを参照してください。

<!-- category: Plotting -->
<!-- keywords: vertices -->
<!-- signatures: vertices(gr) -->
### Function: vertices (gr)

グラフ *gr*の頂点のリストを返します。


例:






```maxima
(%i1) load ("graphs")$
(%i2) vertices(complete_graph(4));
(%o2)                     [3, 2, 1, 0]
```

<!-- category: Plotting -->
<!-- keywords: vertices_to_cycle -->
<!-- signatures: vertices_to_cycle(v_list) -->
### Function: vertices_to_cycle (v_list)

頂点のリスト *v_list*を
*v_list*で定義された閉路の辺のリストに変換します。

<!-- category: Plotting -->
<!-- keywords: vertices_to_path -->
<!-- signatures: vertices_to_path(v_list) -->
### Function: vertices_to_path (v_list)

頂点のリスト *v_list*を
*v_list*で定義された経路の辺のリストに変換します。

<!-- category: Plotting -->
<!-- keywords: wheel_graph -->
<!-- signatures: wheel_graph(n) -->
### Function: wheel_graph (n)

*n+1*個の頂点上の車輪グラフを返します。

<!-- category: Plotting -->
<!-- keywords: wiener_index -->
<!-- signatures: wiener_index(gr) -->
### Function: wiener_index (gr)

グラフ *gr*のWiener指数を返します。


例:






```maxima
(%i2) wiener_index(dodecahedron_graph());
(%o2)                          500
```

