## numericalio

<!-- category: IO -->
<!-- keywords: assume_external_byte_order -->
<!-- signatures: assume_external_byte_order(byte_order_flag) -->
### Function: assume_external_byte_order (byte_order_flag)

`numericalio`に
バイナリデータを読み書きするためのバイトオーダーを知らせます。
*byte_order_flag*の2つの値が認識されます:
リトルエンディアンバイトオーダーとも呼ばれる最下位バイト優先を示す`lsb`;
と
ビッグエンディアンバイトオーダーとも呼ばれる最上位バイト優先を示す`msb`。


もし指定されないなら、
`numericalio`は外部のバイトオーダーは最上位バイト優先を仮定します。

<!-- category: IO -->
<!-- keywords: opena_binary -->
<!-- signatures: opena_binary(file_name) -->
### Function: opena_binary (file_name)

*file_name*という名前のファイルに追加するための
8ビット符号なしバイトの出力ストリームを返します。

<!-- category: IO -->
<!-- keywords: openr_binary -->
<!-- signatures: openr_binary(file_name) -->
### Function: openr_binary (file_name)

*file_name*という名前のファイルを読むための
8ビット符号なしバイトの入力ストリームを返します。

<!-- category: IO -->
<!-- keywords: openw_binary -->
<!-- signatures: openw_binary(file_name) -->
### Function: openw_binary (file_name)

*file_name*という名前のファイルに書き込むための
8ビット符号なしバイトの出力ストリームを返します。

<!-- category: IO -->
<!-- keywords: read_array -->
<!-- signatures: read_array(S, A), read_array(S, A, separator_flag) -->
### Function: read_array (S, A)

*A*が一杯になるか、ソースが尽きるまで、
ソース*S*を配列*A*に読み込みます。
入力データは列優先順に配列に読み込まれます;
入力は*A*の次元に一致する必要はありません。


ソース*S*はファイル名かストリームかもしれません。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

<!-- category: IO -->
<!-- keywords: read_binary_array -->
<!-- signatures: read_binary_array(S, A) -->
### Function: read_binary_array (S, A)

*A*が一杯になるかソースが尽きるまで、
ソース*S*から配列*A*にバイナリの8バイト浮動小数点数を読み込みます。
*M*の要素は行優先順で読み込まれます。


ソース*S*はファイル名かストリームかもしれません。


ソースの要素のバイトオーダーは
`assume_external_byte_order`で指定されます。

<!-- category: IO -->
<!-- keywords: read_binary_list -->
<!-- signatures: read_binary_list(S), read_binary_list(S, L) -->
### Function: read_binary_list (S)

`read_binary_list(S)`は
バイナリ8バイト浮動小数点数の数列として
ソース*S*の内容全体を読み込み、それをリストとして返します。
ソース*S*はファイル名かストリームかもしれません。


`read_binary_list(S, L)`は
リスト*L*が一杯になるかソースが尽きるまで、
ソース*S*から
バイナリ8バイト浮動小数点数を読み込みます。


ソースの要素のバイトオーダーは
`assume_external_byte_order`で指定されます。

<!-- category: IO -->
<!-- keywords: read_binary_matrix -->
<!-- signatures: read_binary_matrix(S, M) -->
### Function: read_binary_matrix (S, M)

*M*が一杯になるかソースが尽きるまで、
ソース*S*から行列*M*にバイナリの8バイト浮動小数点数を読み込みます。
*M*の要素は行優先順で読み込まれます。


ソース*S*はファイル名かストリームかもしれません。


ソースの要素のバイトオーダーは
`assume_external_byte_order`で指定されます。

<!-- category: IO -->
<!-- keywords: read_hashed_array -->
<!-- signatures: read_hashed_array(S, A), read_hashed_array(S, A, separator_flag) -->
### Function: read_hashed_array (S, A)

ソース*S*が読み込まれ、ハッシュ配列として内容全体が返されます。
ソース*S*はファイル名かストリームかもしれません。


`read_hashed_array`は、
それぞれの行の最初の項目をハッシュキーとして扱い、
行の残りを(リストとして)キーと結合します。
例えば、
行`567 12 17 32 55`は
`A[567]: [12, 17, 32, 55]$`と同値です。
行数は要素数と同じである必要はありません。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

<!-- category: IO -->
<!-- keywords: read_list -->
<!-- signatures: read_list(S), read_list(S, L), read_list(S, separator_flag), read_list(S, L, separator_flag) -->
### Function: read_list (S)

`read_list(S)`は、
ソース*S*を読み込み、
フラットなリストとして内容全体を返します。


`read_list(S, L)`は、
*L*が一杯になるかソースが尽きるまで、
ソース*S*を
リスト*L*に読み込みます。


ソース*S*はファイル名かストリームかもしれません。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

<!-- category: IO -->
<!-- keywords: read_matrix -->
<!-- signatures: read_matrix(S), read_matrix(S, M), read_matrix(S, separator_flag), read_matrix(S, M, separator_flag) -->
### Function: read_matrix (S)

`read_matrix(S)`は、
ソース*S*を読み込み、行列として内容全体を返します。
行列のサイズは入力データから推論されます;
ファイルの行それぞれは行列の1行になります。
もし複数の行が異なる長さを持つなら、
`read_matrix`はエラーを出力します。


`read_matrix(S, M)`は、
*M*が一杯になるか、ソースが尽きるまで、
ソース*S*を行列*M*に読み込みます。
入力データは行優先順に行列に読み込まれます;
入力は*M*と同じ行数と列数を持つ必要はありません。


ソース*S*はファイル名かストリームかもしれません。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

<!-- category: IO -->
<!-- keywords: read_nested_list -->
<!-- signatures: read_nested_list(S), read_nested_list(S, separator_flag) -->
### Function: read_nested_list (S)

ソース*S*を読み込み、
入れ子のリストとして内容全体を返します。
ソース*S*はファイル名かストリームかもしれません。


`read_nested_list`は
入力のそれぞれの行について部分リストを持つリストを返します。
行数は要素数と同じである必要はありません。
空の行は無視され*ません*: 空の行は空の部分リストをもたらします。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

<!-- category: IO -->
<!-- keywords: write_binary_data -->
<!-- signatures: write_binary_data(X, D) -->
### Function: write_binary_data (X, D)

Writes the object 
バイナリ8バイトIEEE 754浮動小数点数で構成される
オブジェクト*X*を
ディスティネーション*D*に書き込みます。
他の種類の数は8バイト浮動小数点に強制変換されます。
`write_binary_data`は非数データを書くことはできません。


The object 
オブジェクト*X*はリストか、入れ子のリスト、行列、
もしくは、`array`か`make_array`で生成された配列であり得ます;
*X*は未宣言配列や他のいかなる種類のオブジェクトもありえません。
`write_binary_data`は
入れ子のリスト、行列、配列を行優先順に書き込みます。


デスティネーション*D*はファイル名かストリームかもしれません。
デスティネーションがファイル名の時、
グローバル変数`file_output_append`が
出力ファイルに追加されるか上書きされるか決めます。
デスティネーションがストリームの時、
データすべてが書かれた後`write_binary_data`は特別な動作は何もしません;
特に、ストリームは開かれたままです。


デスティネーションの要素のバイトオーダーは
`assume_external_byte_order`で指定されます。

<!-- category: IO -->
<!-- keywords: write_data -->
<!-- signatures: write_data(X, D), write_data(X, D, separator_flag) -->
### Function: write_data (X, D)

オブジェクト*X*をデスティネーション*D*に書き出します。


`write_data`は行列を
行につき一行で行優先順に書き出します。


`write_data`は
`array`や`make_array`で生成された配列を
行優先順でスラブ毎に改行して書き出します。
高次元スラブは更に改行で分割されます。


`write_data`はハッシュ配列を
1行に、キーそれぞれに結合したリストが続くように書き出します。


`write_data`は入れ子のリストを
それぞれの部分リストを1行に書き出します。


`write_data`はフラットなリストすべてを1行に書き出します。


デスティネーション*D*はファイル名かストリームかもしれません。
デスティネーションがファイル名の時、
グローバル変数`file_output_append`は
出力ファイルに追加されるか上書きされるか決定します。
デスティネーションがストリームの時、
`write_data`は
データすべてが書かれた後、特殊なアクションを取ります;
特にストリームは開いたままとなります。


*separator_flag*の認識される値は
`comma`, `pipe`, `semicolon`, `space`です。
もし*separator_flag*が指定されないなら、ファイルは空白で区切られていると仮定されます。

