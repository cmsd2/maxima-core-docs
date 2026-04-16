## stringproc

### Function: adjust_external_format ()

Prints information about the current external format of the Lisp reader 
and in case the external format encoding differs from the encoding of the 
application which runs Maxima `adjust_external_format` tries to adjust 
the encoding or prints some help or instruction.
`adjust_external_format` returns `true` when the external format has 
been changed and `false` otherwise.


Functions like `cint`, `unicode`, `octets_005fto_005fstring` 
and `string_005fto_005foctets` need UTF-8 as the external format of the 
Lisp reader to work properly over the full range of Unicode characters. 


Examples (Maxima on Windows, March 2016): 
Using `adjust_external_format` when the default external format 
is not equal to the encoding provided by the application.


1. Command line Maxima


In case a terminal session is preferred it is recommended to use Maxima compiled 
with SBCL. Here Unicode support is provided by default and calls to 
`adjust_external_format` are unnecessary. 


If Maxima is compiled with CLISP or GCL it is recommended to change 
the terminal encoding from CP850 to CP1252. 
`adjust_external_format` prints some help. 


CCL reads UTF-8 while the terminal input is CP850 by default. 
CP1252 is not supported by CCL. `adjust_external_format` 
prints instructions for changing the terminal encoding and external format 
both to iso-8859-1.


2. wxMaxima


In wxMaxima SBCL reads CP1252 by default but the input from the application 
is UTF-8 encoded. Adjustment is needed. 


Calling `adjust_external_format` and restarting Maxima 
permanently changes the default external format to UTF-8.



```maxima
(%i1)adjust_external_format();
The line
(setf sb-impl::*default-external-format* :utf-8)
has been appended to the init file
C:/Users/Username/.sbclrc
Please restart Maxima to set the external format to UTF-8.
(%i1) false
```


Restarting Maxima.



```maxima
(%i1) adjust_external_format();
The external format is currently UTF-8
and has not been changed.
(%i1) false
```

See also: `cint`, `unicode`, `octets_to_string`, `string_to_octets`.

### Function: alphacharp (char)

Returns `true` if *char* is an alphabetic character. 


To identify a non-US-ASCII character as an alphabetic character 
the underlying Lisp must provide full Unicode support. 
E.g. a German umlaut is detected as an alphabetic character with SBCL in GNU/Linux 
but not with GCL. 
(In Windows Maxima, when compiled with SBCL, must be set to UTF-8. 
See `adjust_005fexternal_005fformat` for more.) 


Example: Examination of non-US-ASCII characters.


The underlying Lisp (SBCL, GNU/Linux) is able to convert the typed character 
into a Lisp character and to examine.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
```


In GCL this is not possible. An error break occurs.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
(%i2) alphacharp("u");

package stringproc: u cannot be converted into a Lisp character.
 -- an error.
```

See also: `adjust_external_format`.

### Function: alphanumericp (char)

Returns `true` if *char* is an alphabetic character or a digit 
(only corresponding US-ASCII characters are regarded as digits). 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: ascii (int)

Returns the US-ASCII character corresponding to the integer *int*
which has to be less than `128`.


See `unicode` for converting code points larger than `127`.


Examples:



```maxima
(%i1) for n from 0 thru 127 do ( 
        ch: ascii(n), 
        if alphacharp(ch) then sprint(ch),
        if n = 96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

See also: `unicode`.

### Function: cequal (char_1, char_2)

Returns `true` if *char_1* and *char_2* are the same character.

### Function: cequalignore (char_1, char_2)

Like `cequal` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: cgreaterp (char_1, char_2)

Returns `true` if the code point of *char_1* is greater than the 
code point of *char_2*.

### Function: cgreaterpignore (char_1, char_2)

Like `cgreaterp` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: charat (string, n)

Returns the *n*-th character of *string*.
The first character in *string* is returned with *n* = 1. 



```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
(%i2) charlist("Lisp")[1];
(%o2)                           L
```

### Function: charlist (string)

Returns the list of all characters in *string*. 



```maxima
(%i1) charlist("Lisp");
(%o1)                     [L, i, s, p]
```

### Function: charp (obj)

Returns `true` if *obj* is a Maxima-character.
See introduction for example.

### Function: cint (char)

Returns the Unicode code point of *char* which must be a 
Maxima character, i.e. a string of length `1`.


Examples: The hexadecimal code point of some characters 
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i1) obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
```


Warning: It is not possible to enter characters corresponding to code points 
larger than 16 bit in wxMaxima with SBCL on Windows when the external format 
has not been set to UTF-8. See `adjust_005fexternal_005fformat`.








CMUCL doesn’t process these characters as one character. 
`cint` then returns `false`. 

Converting a character to a code point via UTF-8-octets may serve as a workaround: 


`utf8_to_unicode(string_to_octets(character));`








See `utf8_005fto_005funicode`, `string_005fto_005foctets`.

See also: `adjust_external_format`, `utf8_to_unicode`, `string_to_octets`.

### Function: clessp (char_1, char_2)

Returns `true` if the code point of *char_1* is less than the 
code point of *char_2*.

### Function: clesspignore (char_1, char_2)

Like `clessp` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: close (stream)

Closes *stream* and returns `true` if *stream* had been open.

### Function: constituent (char)

Returns `true` if *char* is a graphic character but not a space character.
A graphic character is a character one can see, plus the space character.
(`constituent` is defined by Paul Graham. 
See Paul Graham, ANSI Common Lisp, 1996, page 67.)



```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if constituent(tmp) then sprint(tmp) )$
! " #  %  ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c
d e f g h i j k l m n o p q r s t u v w x y z { | } ~
```

### Function: digitcharp (char)

Returns `true` if *char* is a digit where only the corresponding 
US-ASCII-character is regarded as a digit.

### Function: eval_string (str)

Parse the string *str* as a Maxima expression and evaluate it.
The string *str* may or may not have a terminator (dollar sign `$` or semicolon `;`).
Only the first expression is parsed and evaluated, if there is more than one.


Complain if *str* is not a string.


Examples:



```maxima
(%i1) eval_string ("foo: 42; bar: foo^2 + baz");
(%o1)                       42
(%i2) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o2)                   baz + 1764
```


See also `parse_005fstring` and `eval_005fstring_005flisp`.

See also: `parse_string`, `eval_string_lisp`.

### Function: flength (stream)

*stream* has to be an open stream from or to a file. 
`flength` then returns the number of bytes which are currently present in this file.


Example: See `writebyte` .

See also: `writebyte`.

### Function: flush_output (stream)

Flushes *stream* where *stream* has to be an output stream to a file. 


Example: See `writebyte` .

See also: `writebyte`.

### Function: fposition (fposition, stream, fposition, stream, pos)

Returns the current position in *stream*, if *pos* is not used. 
If *pos* is used, `fposition` sets the position in *stream*.
*stream* has to be a stream from or to a file and 
*pos* has to be a positive number.


Positions in data streams are like in strings or lists 1-indexed, 
i.e. the first element in *stream* is in position 1.

### Function: freshline (freshline, freshline, stream)

Writes a new line to the standard output stream 
if the position is not at the beginning of a line and returns `true`.
Using the optional argument *stream* the new line is written to that stream. 
There are some cases, where `freshline()` does not work as expected. 


See also `newline`.

See also: `newline`.

### Function: get_output_stream_string (stream)

Returns a string containing all the characters currently present in 
*stream* which must be an open string-output stream. 
The returned characters are removed from *stream*.


Example: See `make_005fstring_005foutput_005fstream` .

See also: `make_string_output_stream`.

### Function: lowercasep (char)

Returns `true` if *char* is a lowercase character. 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: make_string_input_stream (make_string_input_stream, string, make_string_input_stream, string, start, make_string_input_stream, string, start, end)

Returns an input stream which contains parts of *string* and an end of file. 
Without optional arguments the stream contains the entire string 
and is positioned in front of the first character. 
*start* and *end* define the substring contained in the stream. 
The first character is available at position 1.

 

```maxima
(%i1) istream : make_string_input_stream("text", 1, 4);
(%o1)              #<string-input stream from "text">
(%i2) (while (c : readchar(istream)) # false do sprint(c), newline())$
t e x 
(%i3) close(istream)$
```

### Function: make_string_output_stream ()

Returns an output stream that accepts characters. Characters currently present 
in this stream can be retrieved by `get_005foutput_005fstream_005fstring`.

 

```maxima
(%i1) ostream : make_string_output_stream();
(%o1)               #<string-output stream 09622ea0>
(%i2) printf(ostream, "foo")$

(%i3) printf(ostream, "bar")$

(%i4) string : get_output_stream_string(ostream);
(%o4)                            foobar
(%i5) printf(ostream, "baz")$

(%i6) string : get_output_stream_string(ostream);
(%o6)                              baz
(%i7) close(ostream)$
```

See also: `get_output_stream_string`.

### Function: newline (newline, newline, stream)

Writes a new line to the standard output stream. 
Using the optional argument *stream* the new line is written to that stream. 
There are some cases, where `newline()` does not work as expected. 


See `sprint` for an example of using `newline()`.

See also: `sprint`.

### Function: opena (file)

Returns a character output stream to *file*.
If an existing file is opened, `opena` appends elements at the end of *file*.


For binary output see `Functions-and-Variables-for-binary-input-and-output` .

See also: `Functions-and-Variables-for-binary-input-and-output`.

### Function: openr (openr, file, openr, file, encoding)

Returns a character input stream to *file*.
`openr` assumes that *file* already exists.
If reading the file results in a lisp error about its encoding
passing the correct string as the argument *encoding* might help.
The available encodings and their names depend on the lisp being used.
For sbcl a list of suitable strings can be found at
[http://www.sbcl.org/manual/#External-Formats]().


For binary input see `Functions-and-Variables-for-binary-input-and-output` .
See also `close` and `openw`.



```maxima
(%i1) istream : openr("data.txt","EUC-JP");
(%o1)     #<FD-STREAM for "file /home/gunter/data.txt" {10099A3AE3}>
(%i2) close(istream);
(%o2)                                true
```

See also: `Functions-and-Variables-for-binary-input-and-output`, `close`, `openw`.

### Function: openw (file)

Returns a character output stream to *file*.
If *file* does not exist, it will be created.
If an existing file is opened, `openw` destructively modifies *file*.


For binary output see `Functions-and-Variables-for-binary-input-and-output` .


See also `close` and `openr`.

See also: `Functions-and-Variables-for-binary-input-and-output`, `close`, `openr`.

### Function: parse_string (str)

Parse the string *str* as a Maxima expression (do not evaluate it).
The string *str* may or may not have a terminator (dollar sign `$` or semicolon `;`).
Only the first expression is parsed, if there is more than one.


Complain if *str* is not a string.


Examples:



```maxima
(%i1) parse_string ("foo: 42; bar: foo^2 + baz");
(%o1)                    foo : 42
(%i2) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o2)          (foo : 42, bar : foo  + baz)
```


See also `eval_005fstring`.

See also: `eval_string`.

### Function: printf (printf, dest, string, printf, dest, string, expr_1, ..., expr_n)

Produces formatted output by outputting the characters of control-string 
*string* and observing that a tilde introduces a directive.
The character after the tilde, possibly preceded by prefix parameters 
and modifiers, specifies what kind of formatting is desired.
Most directives use one or more elements of the arguments 
*expr_1*, ..., *expr_n* to create their output.


If *dest* is a stream or `true`, then `printf` returns `false`.
Otherwise, `printf` returns a string containing the output.
By default the streams *stdin*, *stdout* and *stderr* are defined.
If Maxima is running as a network client (which is the normal case if Maxima is communicating
with a graphical user interface, which must be the server) `setup-client`
will define *old_stdout* and *old_stderr*, too.


`printf` provides the Common Lisp function `format` in Maxima. 
The following example illustrates the general relation between these two 
functions.



```maxima
(%i1) printf(true, "R~dD~d~%", 2, 2);
R2D2
(%o1)                                false
(%i2) :lisp (format t "R~dD~d~%" 2 2)
R2D2
NIL
```


The following description is limited to a rough sketch of the possibilities of 
`printf`.
The Lisp function `format` is described in detail in many reference books. 
Of good help is e.g. the free available online-manual 
"Common Lisp the Language" by Guy L. Steele. See chapter 22.3.3 there. 


In addition, `printf` recognizes two format directives which are not known to Lisp `format`.
The format directive `~m` indicates Maxima pretty printer output.
The format directive `~h` indicates a bigfloat number.



```maxima
~%       new line
   ~&       fresh line
   ~t       tab
   ~$       monetary
   ~d       decimal integer
   ~b       binary integer
   ~o       octal integer
   ~x       hexadecimal integer
   ~br      base-b integer
   ~r       spell an integer
   ~p       plural
   ~f       floating point
   ~e       scientific notation
   ~g       ~f or ~e, depending upon magnitude
   ~h       bigfloat
   ~a       uses Maxima function string
   ~m       Maxima pretty printer output
   ~s       like ~a, but output enclosed in "double quotes"
   ~~       ~
   ~<       justification, ~> terminates
   ~(       case conversion, ~) terminates 
   ~[       selection, ~] terminates 
   ~{       iteration, ~} terminates
```


Note that the directive ~* is not supported.


If *dest* is a stream or `true`, then `printf` returns `false`.
Otherwise, `printf` returns a string containing the output.



```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf(true,"~{~{~9,1f ~}~%~}",mat ),
          mat = args(matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]))$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false,control, n,n,if n=1 then 1 else 2 ), n=2;
(%o5)                    Two birds are singing.
```


The directive ~h has been introduced to handle bigfloats. 



```maxima
~w,d,e,x,o,p@H
 w : width
 d : decimal digits behind floating point
 e : minimal exponent digits
 x : preferred exponent
 o : overflow character
 p : padding character
 @ : display sign for positive numbers
```



```maxima
(%i1) fpprec : 1000$
(%i2) printf(true, "|~h|~%", 2.b0^-64)$
|0.0000000000000000000542101086242752217003726400434970855712890625|
(%i3) fpprec : 26$
(%i4) printf(true, "|~h|~%", sqrt(2))$
|1.4142135623730950488016887|
(%i5) fpprec : 24$
(%i6) printf(true, "|~h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i7) printf(true, "|~28h|~%", sqrt(2))$
|   1.41421356237309504880169|
(%i8) printf(true, "|~28,,,,,'*h|~%", sqrt(2))$
|***1.41421356237309504880169|
(%i9) printf(true, "|~,18h|~%", sqrt(2))$
|1.414213562373095049|
(%i10) printf(true, "|~,,,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-3|
(%i11) printf(true, "|~,,2,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-03|
(%i12) printf(true, "|~20h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i13) printf(true, "|~20,,,,'+h|~%", sqrt(2))$
|++++++++++++++++++++|
```


For conversion of objects to strings also see `concat`, `sconcat`,
`string` and `simplode`.

See also: `concat`, `sconcat`, `string`, `simplode`.

### Function: readbyte (stream)

Removes and returns the first byte in *stream* which must be a binary input stream. 
If the end of file is encountered `readbyte` returns `false`.


Example: Read the first 16 bytes from a file encrypted with AES in OpenSSL. 



```maxima
(%i1) ibase: obase: 16.$

(%i2) in: openr_binary("msg.bin");
(%o2)                       #<input stream msg.bin>
(%i3) (L:[],  thru 16. do push(readbyte(in), L),  L:reverse(L));
(%o3) [53, 61, 6C, 74, 65, 64, 5F, 5F, 88, 56, 0DE, 8A, 74, 0FD,
       0AD, 0F0]
(%i4) close(in);
(%o4)                                true
(%i5) map(ascii, rest(L,-8));
(%o5)                      [S, a, l, t, e, d, _, _]
(%i6) salt: octets_to_number(rest(L,8));
(%o6)                          8856de8a74fdadf0
```

### Function: readchar (stream)

Removes and returns the first character in *stream*. 
If the end of file is encountered `readchar` returns `false`.


Example: See `make_005fstring_005finput_005fstream`.

See also: `make_string_input_stream`.

### Function: readline (stream)

Returns a string containing all characters starting at the current position 
in *stream* up to the end of the line or `false` 
if the end of the file is encountered.

### Function: scopy (string)

Returns a copy of *string* as a new string.

### Function: sdowncase (sdowncase, string, sdowncase, string, start, sdowncase, string, start, end)

Like `supcase` but uppercase characters are converted to lowercase.

See also: `supcase`.

### Function: sequal (string_1, string_2)

Returns `true` if *string_1* and *string_2* contain the same 
sequence of characters.

### Function: sequalignore (string_1, string_2)

Like `sequal` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: sexplode (string)

`sexplode` is an alias for function `charlist`.

### Function: simplode (simplode, list, simplode, list, delim)

`simplode` takes a list of expressions and concatenates them into a string.
If no delimiter *delim* is specified, `simplode` uses no delimiter.
*delim* can be any string.


See also `concat`, `sconcat`, `string` and `printf`.


Examples:



```maxima
(%i1) simplode(["xx[",3,"]:",expand((x+y)^3)]);
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) simplode( sexplode("stars")," * " );
(%o2)                   s * t * a * r * s
(%i3) simplode( ["One","more","coffee."]," " );
(%o3)                   One more coffee.
```

See also: `concat`, `sconcat`, `string`, `printf`.

### Function: sinsert (seq, string, pos)

Returns a string that is a concatenation of `substring(string, 1, pos-1)`,
the string *seq* and `substring (string, pos)`.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) s: "A submarine."$
(%i2) concat( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

### Function: sinvertcase (sinvertcase, string, sinvertcase, string, start, sinvertcase, string, start, end)

Returns *string* except that each character from position *start* to *end* is inverted.
If *end* is not given,
all characters from *start* to the end of *string* are replaced.


Examples:



```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

### Function: slength (string)

Returns the number of characters in *string*.

### Function: smake (num, char)

Returns a new string with a number of *num* characters *char*. 


Example:



```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

### Function: smismatch (smismatch, string_1, string_2, smismatch, string_1, string_2, test)

Returns the position of the first character of *string_1* at which *string_1* and *string_2* differ or `false`.
Default test function for matching is `sequal`.
If `smismatch` should ignore case, use `sequalignore` as test.


Example:



```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

### Variable: space

The space character.

### Function: split (split, string, split, string, delim, split, string, delim, multiple)

Returns the list of all tokens in *string*.
Each token is an unparsed string.
`split` uses *delim* as delimiter.
If *delim* is not given, the space character is the default delimiter.
*multiple* is a boolean variable with `true` by default.
Multiple delimiters are read as one.
This is useful if tabs are saved as multiple space characters.
If *multiple* is set to `false`, each delimiter is noted.


Examples:



```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

### Function: sposition (char, string)

Returns the position of the first character in *string* which matches *char*.
The first character in *string* is in position 1.
For matching characters ignoring case see `ssearch`.

See also: `ssearch`.

### Function: sprint (expr_1, ..., expr_n)

Evaluates and displays its arguments one after the other ‘on a line’ starting at
the leftmost position.  The expressions are printed with a space character right next 
to the number, and it disregards line length.  
`newline()` might be used for line breaking.


Example: Sequential printing with `sprint`. 
Creating a new line with `newline()`.



```maxima
(%i1) for n:0 thru 19 do sprint(fib(n))$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), 
         if mod(n,10) = 9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

### Function: sremove (sremove, seq, string, sremove, seq, string, test, sremove, seq, string, test, start, sremove, seq, string, test, start, end)

Returns a string like *string* but without all substrings matching *seq*.
Default test function for matching is `sequal`.
If `sremove` should ignore case while searching for *seq*, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

### Function: sremovefirst (sremovefirst, seq, string, sremovefirst, seq, string, test, sremovefirst, seq, string, test, start, sremovefirst, seq, string, test, start, end)

Like `sremove` except that only the first substring that matches *seq* is removed.

### Function: sreverse (string)

Returns a string with all the characters of *string* in reverse order. 


See also `reverse`.

See also: `reverse`.

### Function: ssearch (ssearch, seq, string, ssearch, seq, string, test, ssearch, seq, string, test, start, ssearch, seq, string, test, start, end)

Returns the position of the first substring of *string* that matches the string *seq*.
Default test function for matching is `sequal`.
If `ssearch` should ignore case, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Example:



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

### Function: ssort (ssort, string, ssort, string, test)

Returns a string that contains all characters from *string* in an order such there are no two successive characters *c* and *d* such that `test (c, d)` is `false` and `test (d, c)` is `true`.
Default test function for sorting is *clessp*.
The set of test functions is `{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`.


Examples:



```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

### Function: ssubst (ssubst, new, old, string, ssubst, new, old, string, test, ssubst, new, old, string, test, start, ssubst, new, old, string, test, start, end)

Returns a string like *string* except that all substrings matching *old* are replaced by *new*.
*old* and *new* need not to be of the same length.
Default test function for matching is `sequal`.
If `ssubst` should ignore case while searching for old, use `sequalignore` as test.
Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

### Function: ssubstfirst (ssubstfirst, new, old, string, ssubstfirst, new, old, string, test, ssubstfirst, new, old, string, test, start, ssubstfirst, new, old, string, test, start, end)

Like `subst` except that only the first substring that matches *old* is replaced.

### Function: strim (seq, string)

Returns a string like *string*,
but with all characters that appear in *seq* removed from both ends. 


Examples:



```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

### Function: striml (seq, string)

Like `strim` except that only the left end of *string* is trimmed.

### Function: strimr (seq, string)

Like `strim` except that only the right end of *string* is trimmed.

### Function: stringp (obj)

Returns `true` if *obj* is a string.
See introduction for example.

### Function: substring (substring, string, start, substring, string, start, end)

Returns the substring of *string* beginning at position *start* and ending at position *end*.
The character at position *end* is not included.
If *end* is not given, the substring contains the rest of the string.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

### Function: supcase (supcase, string, supcase, string, start, supcase, string, start, end)

Returns *string* except that lowercase characters from position *start* to *end* are replaced by the corresponding uppercase ones.
If *end* is not given,
all lowercase characters from *start* to the end of *string* are replaced.


Example:



```maxima
(%i1) supcase("english",1,2);
(%o1)                        English
```

### Variable: tab

The tab character.

### Function: tokens (tokens, string, tokens, string, test)

Returns a list of tokens, which have been extracted from *string*.
The tokens are substrings whose characters satisfy a certain test function.
If test is not given, *constituent* is used as the default test.
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}` is the set of test functions. 
(The Lisp-version of `tokens` is written by Paul Graham. ANSI Common Lisp, 1996, page 67.)


Examples:



```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parse_string,%);
(%o3)                      [5, 10, 24]
```

### Function: unicode (arg)

Returns the character defined by *arg* which might be a Unicode code point 
or a name string if the underlying Lisp provides full Unicode support. 


Example: Characters defined by hexadecimal code points
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i1) ibase: 16.$
(%i2) map(unicode, [24, 0A3, 20AC]);
(%o2)                            [$, GBP, EUR]
```


Warning: In wxMaxima with SBCL on Windows it is not possible to convert 
code points larger than 16 bit to characters when the external format 
has not been set to UTF-8. See `adjust_005fexternal_005fformat` for more information.








CMUCL doesn’t process code points larger than 16 bit. 
In these cases `unicode` returns `false`. 

Converting a code point to a character via UTF-8 octets may serve as a workaround: 


`octets_to_string(unicode_to_utf8(code_point));`








See `octets_005fto_005fstring`, `unicode_005fto_005futf8`.


In case the underlying Lisp provides full Unicode support the character might be 
specified by its name. The following is possible in ECL, CLISP and SBCL, 
where in SBCL on Windows the external format has to be set to UTF-8.
`unicode(name)` is supported by CMUCL too but again limited to 16 bit 
characters. 


The string argument to `unicode` is basically the same string returned by 
`printf` using the "~@c" specifier. 
But as shown below the prefix "#\" must be omitted. 
Underlines might be replaced by spaces and uppercase letters by lowercase ones.


Example (continued): Characters defined by names 
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i3) printf(false, "~@c", unicode(0DF));
(%o3)                    #\LATIN_SMALL_LETTER_SHARP_S
(%i4) unicode("LATIN_SMALL_LETTER_SHARP_S");
(%o4)                                  ß
(%i5) unicode("Latin small letter sharp s");
(%o5)                                  ß
```

See also: `adjust_external_format`, `octets_to_string`, `unicode_to_utf8`.

### Function: unicode_to_utf8 (code_point)

Returns a list containing the UTF-8 code corresponding to the Unicode *code_point*.


Examples: Converting Unicode code points to UTF-8 and vice versa. 



```maxima
(%i1) ibase: obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
(%i3) map(unicode_to_utf8, %);
(%o3)                 [[24], [0C2, 0A3], [0E2, 82, 0AC]]
(%i4) map(utf8_to_unicode, %);
(%o4)                           [24, 0A3, 20AC]
```

### Function: uppercasep (char)

Returns `true` if *char* is an uppercase character. 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Variable: us_ascii_only

This option variable affects Maxima when the character encoding 
provided by the application which runs Maxima is UTF-8 but the 
external format of the Lisp reader is not equal to UTF-8. 


On GNU/Linux this is true when Maxima is built with GCL 
and on Windows in wxMaxima with GCL- and SBCL-builds. 
With SBCL it is recommended to change the external format to UTF-8. 
Setting `us_ascii_only` is unnecessary then. 
See `adjust_005fexternal_005fformat` for details. 


`us_ascii_only` is `false` by default. 
Maxima itself then (i.e. in the above described situation) parses the UTF-8 encoding.


When `us_ascii_only` is set to `true` it is assumed that all strings 
used as arguments to string processing functions do not contain Non-US-ASCII characters. 
Given that promise, Maxima avoids parsing UTF-8 and strings can be processed more efficiently.

See also: `adjust_external_format`.

### Function: utf8_to_unicode (list)

Returns a Unicode code point corresponding to the *list* which must contain 
the UTF-8 encoding of a single character.


Examples: See `unicode_005fto_005futf8`.

See also: `unicode_to_utf8`.

### Function: writebyte (byte, stream)

Writes *byte* to *stream* which must be a binary output stream. 
`writebyte` returns `byte`.


Example: Write some bytes to a binary file output stream. 
In this example all bytes correspond to printable characters and are printed 
by `printfile`. 
The bytes remain in the stream until `flush_output` or `close` have been called.



```maxima
(%i1) ibase: obase: 16.$

(%i2) bytes: map(cint, charlist("GNU/Linux"));
(%o2)                [47, 4E, 55, 2F, 4C, 69, 6E, 75, 78]
(%i3) out: openw_binary("test.bin");
(%o3)                      #<output stream test.bin>
(%i4) for i thru 3 do writebyte(bytes[i], out);
(%o4)                                done
(%i5) printfile("test.bin")$

(%i6) flength(out);
(%o6)                                  0
(%i7) flush_output(out);
(%o7)                                true
(%i8) flength(out);
(%o8)                                  3
(%i9) printfile("test.bin")$
GNU
(%i0A) for b in rest(bytes,3) do writebyte(b, out);
(%o0A)                               done
(%i0B) close(out);
(%o0B)                               true
(%i0C) printfile("test.bin")$
GNU/Linux
```

