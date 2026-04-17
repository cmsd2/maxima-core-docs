## quantum_computing

<!-- category: Other -->
<!-- keywords: binlist -->
<!-- signatures: binlist(k), binlist(k, n) -->
### Function: binlist (k)

`binlist`(*k*), where *k* must be a natural number,
returns a list of binary digits 0 or 1 corresponding to the digits of
*k* in binary representation. `binlist`(*k*, *n*) does
the same but returns a list of length *n*, with leading zeros as
necessary. Notice that for the result to represent a possible state of
*m* qubits, *n* should be equal to 2^*m* and *k* should
be between 0 and 2^*m*-1.

<!-- category: Other -->
<!-- keywords: binlist2dec -->
<!-- signatures: binlist2dec(lst) -->
### Function: binlist2dec (lst)

Given a list *lst* with *n* binary digits, it returns the decimal
number it represents.

<!-- category: Other -->
<!-- keywords: CNOT -->
<!-- signatures: CNOT(q, i, j) -->
### Function: CNOT (q, i, j)

Changes the value of the *j*’th qubit, in a state *q* of *m*
qubits, when the value of the *i*’th qubit equals 1. It modifies the
list *q* and returns its modified value.

<!-- category: Other -->
<!-- keywords: controlled -->
<!-- signatures: controlled(U, q, c, i) -->
### Function: controlled (U, q, c, i)

Applies a matrix *U*, acting on *m* qubits, on qubits *i*
through *i*+*m*-1 of the state *q* of *n* qubits
(*n* > *m*), when the value of the *c*’th qubit in *q*
equals 1. *i* should be an integer between 1 and *n*+1-*m*
and *c* should be an integer between 1 and *n*, excluding the
qubits to be modified (*i* through *i*+*m*-1).


*U* can be one of the indices of the array of common matrices
*qmatrix* (see `qmatrix`). The state *q* is modified and
shown in the output.

See also: `qmatrix`.

<!-- category: Other -->
<!-- keywords: gate -->
<!-- signatures: gate(U, q), gate(U, q, i), gate(U, q, i1, ..., im) -->
### Function: gate (U, q)

*U* must be a matrix acting on states of *m* qubits; *q* a
list corresponding to a state of *n* qubits (*n* >= *m*);
*i* and the *m* numbers *i1*, ..., *im* must be
different integers between 1 and *n*.


`gate`(*U*, *q*) applies matrix *U* to each qubit of
*q*, when *m* equals 1, or to the first *m* qubits of
*q* when *m* is bigger than 1.


`gate`(*U*, *q*, *i*) applies matrix *U* to the
qubits *i* through *i*+*m*-1 of *q*.


`gate`(*U*, *q*, *i1*, ..., *in*) applies
matrix *U* to the in the positions *i1*, ..., *im*.


*U* can be one of the indices of the array of common matrices
*qmatrix* (see `qmatrix`). The state *q* is modified and
shown in the output.

See also: `qmatrix`.

<!-- category: Other -->
<!-- keywords: gate_matrix -->
<!-- signatures: gate_matrix(U, n), gate_matrix(U, n, i1, ..., im) -->
### Function: gate_matrix (U, n)

*U* must be a 2 by 2 matrix or one of the indices of the array of
common matrices *qmatrix* (see `qmatrix`).
`gate_matrix`(*U*, *n*) returns the matrix corresponding to
the action of *U* on each qubit in a state of *n* qubits.


`gate_matrix` (*U*, *n*, *i1*, ..., *im*)
returns the matrix corresponding to the action of *U* on qubits
*i1*, ..., *im* of a state of *n* qubits, where
*i1*, ..., *im* are different integers between 1 and
*n*.

See also: `qmatrix`.

<!-- category: Other -->
<!-- keywords: linsert -->
<!-- signatures: linsert(e, lst, p) -->
### Function: linsert (e, lst, p)

Inserts the expression or list *e* into the list *lst* at position
*p*. The list can be empty and *p* must be an integer between 1 and
the length of *lst* plus 1.

<!-- category: Other -->
<!-- keywords: lreplace -->
<!-- signatures: lreplace(e, lst, p) -->
### Function: lreplace (e, lst, p)

If *e* is a list of length *n*, the elements in the positions
*p*, *p*+1, ..., *p*+*n*-1 of the list *lst* are
replaced by *e*, or the first elements of *e* if the end of
*lst* is reached.  If *e* is an expression, the element in
position *p* of list *lst* is replaced by that expression.
*p* must be an integer between 1 and the length of *lst*.

<!-- category: Other -->
<!-- keywords: normalize -->
<!-- signatures: normalize(q) -->
### Function: normalize (q)

Returns the normalized version of a quantum state given as a list *q*.

<!-- category: Other -->
<!-- keywords: qdisplay -->
<!-- signatures: qdisplay(q) -->
### Function: qdisplay (q)

Represents the state *q* of a system of *n* qubits as a linear
combination of the computational states with *n* binary digits.  It
returns an expression including strings and symbols.

<!-- category: Other -->
<!-- keywords: qmatrix -->
<!-- signatures: qmatrix -->
### Variable: qmatrix

This variable is a predefined hash array of two by two matrices with the
standard matrices: identity, Pauli matrices, Hadamard matrix and the
phase matrix. The six possible indices are I, X, Y, Z, H,
S. *qmatrix*[I] is the identity matrix, *qmatrix*[X] the Pauli x
matrix, *qmatrix*[Y] the Pauli y matrix, *qmatrix*[Z] the Pauli
z matrix, *qmatrix*[H] the Hadamard matrix and *qmatrix*[S] the
phase matrix.

<!-- category: Other -->
<!-- keywords: qmeasure -->
<!-- signatures: qmeasure(q), qmeasure(q, i1, ..., im) -->
### Function: qmeasure (q)

Measures the value of one or more qubits in a system of *n* qubits
with state *q*. The *m* positive integers *i1*, ...,
*im* are the positions of the qubits to be measured It requires 1 or
more arguments. The first argument must be the state q. If the only
argument given is *q*, all the n qubits will be measured.


It returns a list with the values of the qubits measured (either 0 or
1), in the same order they were requested or in ascending order if the
only argument given was *q*. It modifies the list *q*,
reflecting the collapse of the quantum state after the measurement.

<!-- category: Other -->
<!-- keywords: qswap -->
<!-- signatures: qswap(q, i, j) -->
### Function: qswap (q, i, j)

Interchanges the states of qubits *i* and *j* in the state
*q* of a system of several qubits.  It modifies the list *q* and
returns its modified value.

<!-- category: Other -->
<!-- keywords: qubits -->
<!-- signatures: qubits(n), qubits(i1, ..., in) -->
### Function: qubits (n)

`qubits`(*n*) returns a list representing the ground state of a
system of *n* qubits.


`qubits`(*i1*, ..., *in*) returns a list with
representing the state of *n* qubits with values *i1*, ...,
*in*.

<!-- category: Other -->
<!-- keywords: Rx -->
<!-- signatures: Rx(a) -->
### Function: Rx (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the x axis.

<!-- category: Other -->
<!-- keywords: Ry -->
<!-- signatures: Ry(a) -->
### Function: Ry (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the y axis.

<!-- category: Other -->
<!-- keywords: Rz -->
<!-- signatures: Rz(a) -->
### Function: Rz (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the z axis.

<!-- category: Other -->
<!-- keywords: toffoli -->
<!-- signatures: toffoli(q, (i, (j, (k) -->
### Function: toffoli (q, (i, (j, (k)

Changes the value of the *k*’th qubit, in the state *q* of
*n* qubits, if the values of the *i*’th anf *j*’th qubits
are equal to 1. It modifies the list *q* and returns its new value.

<!-- category: Other -->
<!-- keywords: tprod -->
<!-- signatures: tprod(o1, ..., on) -->
### Function: tprod (o1, ..., on)

Returns the tensor product of the *n* matrices or lists *o1*,
..., *on*.

