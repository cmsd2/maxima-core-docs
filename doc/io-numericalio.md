## numericalio

<!-- category: IO -->
<!-- keywords: assume_external_byte_order -->
<!-- signatures: assume_external_byte_order(byte_order_flag) -->
### Function: assume_external_byte_order (byte_order_flag)

Tells `numericalio` the byte order for reading and writing binary data.
Two values of *byte_order_flag* are recognized:
`lsb` which indicates least-significant byte first, also called little-endian byte order;
and `msb` which indicates most-significant byte first, also called big-endian byte order.


If not specified, `numericalio` assumes the external byte order is most-significant byte first.

<!-- category: IO -->
<!-- keywords: opena_binary -->
<!-- signatures: opena_binary(file_name) -->
### Function: opena_binary (file_name)

Returns an output stream of 8-bit unsigned bytes to append the file named by *file_name*.

<!-- category: IO -->
<!-- keywords: openr_binary -->
<!-- signatures: openr_binary(file_name) -->
### Function: openr_binary (file_name)

Returns an input stream of 8-bit unsigned bytes to read the file named by *file_name*.


See also `openw_binary` and `openr`.

See also: `openw_binary`, `openr`.

<!-- category: IO -->
<!-- keywords: openw_binary -->
<!-- signatures: openw_binary(file_name) -->
### Function: openw_binary (file_name)

Returns an output stream of 8-bit unsigned bytes to write the file named by *file_name*.


See also `openr_binary`, `opena_binary` and `openw`.

See also: `openr_binary`, `opena_binary`, `openw`.

<!-- category: IO -->
<!-- keywords: read_array -->
<!-- signatures: read_array(S, A), read_array(S, A, separator_flag) -->
### Function: read_array (S, A)

Reads the source *S* into the array *A*,
until *A* is full or the source is exhausted.
Input data are read into the array in row-major order;
the input need not conform to the dimensions of *A*.


The source *S* may be a file name or a stream.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_hashed_array`,
`read_list`, `read_binary_array` and `read_005fnested_005flist`.

See also: `openr`, `read_matrix`, `read_hashed_array`, `read_list`, `read_binary_array`, `read_nested_list`.

<!-- category: IO -->
<!-- keywords: read_binary_array -->
<!-- signatures: read_binary_array(S, A) -->
### Function: read_binary_array (S, A)

Reads binary 8-byte floating point numbers from the source *S* into the array *A*
until *A* is full, or the source is exhausted.
*A* must be an array created by `array` or `make_array`.
Elements of *A* are read in row-major order.


The source *S* may be a file name or a stream.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005farray`.

See also: `read_array`.

<!-- category: IO -->
<!-- keywords: read_binary_list -->
<!-- signatures: read_binary_list(S), read_binary_list(S, L) -->
### Function: read_binary_list (S)

`read_binary_list(S)` reads the entire content of the source *S*
as a sequence of binary 8-byte floating point numbers, and returns it as a list.
The source *S* may be a file name or a stream.


`read_binary_list(S, L)` reads 8-byte binary floating point numbers
from the source *S* until the list *L* is full, or the source is exhausted.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005flist`.

See also: `read_list`.

<!-- category: IO -->
<!-- keywords: read_binary_matrix -->
<!-- signatures: read_binary_matrix(S, M) -->
### Function: read_binary_matrix (S, M)

Reads binary 8-byte floating point numbers from the source *S* into the matrix *M*
until *M* is full, or the source is exhausted.
Elements of *M* are read in row-major order.


The source *S* may be a file name or a stream.


The byte order in elements of the source is specified by `assume_external_byte_order`.


See also `read_005fmatrix`.

See also: `read_matrix`.

<!-- category: IO -->
<!-- keywords: read_hashed_array -->
<!-- signatures: read_hashed_array(S, A), read_hashed_array(S, A, separator_flag) -->
### Function: read_hashed_array (S, A)

Reads the source *S* and returns its entire content as a `hashed-array`.
The source *S* may be a file name or a stream.


`read_hashed_array` treats the first item on each line as a hash key,
and associates the remainder of the line (as a list) with the key.
For example,
the line `567 12 17 32 55` is equivalent to `A[567]: [12, 17, 32, 55]$`.
Lines need not have the same numbers of elements.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_list` and `read_005fnested_005flist`.

See also: `hashed-array`, `openr`, `read_matrix`, `read_array`, `read_list`, `read_nested_list`.

<!-- category: IO -->
<!-- keywords: read_list -->
<!-- signatures: read_list(S), read_list(S, L), read_list(S, separator_flag), read_list(S, L, separator_flag) -->
### Function: read_list (S)

`read_list(S)` reads the source *S* and returns its entire content as a flat list.


`read_list(S, L)` reads the source *S* into the list *L*,
until *L* is full or the source is exhausted.


The source *S* may be a file name or a stream.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_nested_list`, `read_binary_list` and `read_005fhashed_005farray`.

See also: `openr`, `read_matrix`, `read_array`, `read_nested_list`, `read_binary_list`, `read_hashed_array`.

<!-- category: IO -->
<!-- keywords: read_matrix -->
<!-- signatures: read_matrix(S), read_matrix(S, M), read_matrix(S, separator_flag), read_matrix(S, M, separator_flag) -->
### Function: read_matrix (S)

`read_matrix(S)` reads the source *S* and returns its entire content as a matrix.
The size of the matrix is inferred from the input data;
each line of the file becomes one row of the matrix.
If some lines have different lengths, `read_matrix` complains.


`read_matrix(S, M)` read the source *S* into the matrix *M*,
until *M* is full or the source is exhausted.
Input data are read into the matrix in row-major order;
the input need not have the same number of rows and columns as *M*.


The source *S* may be a file name or a stream which for example allows skipping
the very first line of a file (that may be useful, if you read CSV data, where the
first line often contains the description of the columns):


```maxima
s : openr("data.txt");
readline(s);  /* skip the first line */
M : read_matrix(s, 'comma);  /* read the following (comma-separated) lines into matrix M */
close(s);
```


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_array`, `read_hashed_array`,
`read_list`, `read_binary_matrix`, `write_data` and
`read_005fnested_005flist`.

See also: `openr`, `read_array`, `read_hashed_array`, `read_list`, `read_binary_matrix`, `write_data`, `read_nested_list`.

<!-- category: IO -->
<!-- keywords: read_nested_list -->
<!-- signatures: read_nested_list(S), read_nested_list(S, separator_flag) -->
### Function: read_nested_list (S)

Reads the source *S* and returns its entire content as a nested list.
The source *S* may be a file name or a stream.


`read_nested_list` returns a list which has a sublist for each
line of input. Lines need not have the same numbers of elements.
Empty lines are *not* ignored: an empty line yields an empty sublist.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, and `space`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openr`, `read_matrix`, `read_array`,
`read_list` and `read_005fhashed_005farray`.

See also: `openr`, `read_matrix`, `read_array`, `read_list`, `read_hashed_array`.

<!-- category: IO -->
<!-- keywords: write_binary_data -->
<!-- signatures: write_binary_data(X, D) -->
### Function: write_binary_data (X, D)

Writes the object *X*, comprising binary 8-byte IEEE 754 floating-point numbers,
to the destination *D*.
Other kinds of numbers are coerced to 8-byte floats.
`write_binary_data` cannot write non-numeric data.


The object *X* may be a list, a nested list, a matrix,
or an array created by `array` or `make_array`;
*X* cannot be a hashed array or any other type of object.
`write_binary_data` writes nested lists, matrices, and arrays in row-major order.


The destination *D* may be a file name or a stream.
When the destination is a file name,
the global variable `file_output_append` governs
whether the output file is appended or truncated.
When the destination is a stream,
no special action is taken by `write_binary_data` after all the data are written;
in particular, the stream remains open.


The byte order in elements of the destination
is specified by `assume_external_byte_order`.


See also `write_005fdata`.

See also: `write_data`.

<!-- category: IO -->
<!-- keywords: write_data -->
<!-- signatures: write_data(X, D), write_data(X, D, separator_flag) -->
### Function: write_data (X, D)

Writes the object *X* to the destination *D*.


`write_data` writes a matrix in row-major order,
with one line per row.


`write_data` writes an array created by `array` or `make_array`
in row-major order, with a new line at the end of every slab.
Higher-dimensional slabs are separated by additional new lines.


`write_data` writes a hashed array with each key followed by
its associated list on one line.


`write_data` writes a nested list with each sublist on one line.


`write_data` writes a flat list all on one line.


The destination *D* may be a file name or a stream.
When the destination is a file name,
the global variable `file_output_append` governs
whether the output file is appended or truncated.
When the destination is a stream,
no special action is taken by `write_data` after all the data are written;
in particular, the stream remains open.


The recognized values of *separator_flag* are
`comma`, `pipe`, `semicolon`, `space`, and `tab`.
Equivalently, the separator may be specified as a string of one character:
`","` (comma), `"|"` (pipe), `";"` (semicolon),
`" "` (space), or `" "` (tab).
If *separator_flag* is not specified, the file is assumed space-delimited.


See also `openw` and `read_005fmatrix`.

See also: `openw`, `read_matrix`.

