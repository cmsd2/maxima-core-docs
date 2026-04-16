## stringproc

### Function: base64 (arg)

Returns the base64-representation of *arg* as a string. 
The argument *arg* may be a string, a non-negative integer or a list of octets.


Examples:



```maxima
(%i1) base64: base64("foo bar baz");
(%o1)                          Zm9vIGJhciBiYXo=
(%i2) string: base64_decode(base64);
(%o2)                            foo bar baz
(%i3) obase: 16.$
(%i4) integer: base64_decode(base64, 'number);
(%o4)                       666f6f206261722062617a
(%i5) octets: base64_decode(base64, 'list);
(%o5)            [66, 6F, 6F, 20, 62, 61, 72, 20, 62, 61, 7A]
(%i6) ibase: 16.$
(%i7) base64(octets);
(%o7)                          Zm9vIGJhciBiYXo=
```


Note that if *arg* contains umlauts (resp. octets larger than 127) 
the resulting base64-string is platform dependent.
However the decoded string will be equal to the original.

### Function: base64_decode (base64_decode, base64-string, base64_decode, base64-string, return-type)

By default `base64_decode` decodes the *base64-string* back to the original string. 


The optional argument *return-type* allows `base64_decode` to 
alternatively return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example: See `base64`.

See also: `base64`.

### Function: crc24sum (crc24sum, octets, crc24sum, octets, return-type)

By default `crc24sum` returns the `CRC24` checksum of an octet-list 
as a string.


The optional argument *return-type* allows `crc24sum` to 
alternatively return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example:



```maxima
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2.0.22 (GNU/Linux)

iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM
wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi
rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe
vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam
/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH
WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=
=WmeC
-----END PGP SIGNATURE-----
```



```maxima
(%i1) ibase : obase : 16.$
(%i2) sig64 : sconcat(
 "iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM",
 "wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi",
 "rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe",
 "vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam",
 "/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH",
 "WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=" )$
(%i3) octets: base64_decode(sig64, 'list)$
(%i4) crc24: crc24sum(octets, 'list);
(%o4)                          [5A, 67, 82]
(%i5) base64(crc24);
(%o5)                              WmeC
```

### Function: md5sum (md5sum, arg, md5sum, arg, return-type)

Returns the `MD5` checksum of a string, non-negative integer,
list of octets, or binary (not character) input stream.
A file for which an input stream is opened may be an ordinary text file;
it is the stream which needs to be binary, not the file itself.


When the argument is an input stream,
`md5sum` reads the entire content of the stream,
but does not close the stream.


The default return value is a string containing 32 hex characters.
The optional argument *return-type* allows `md5sum` to alternatively 
return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `MD5` checksum is platform dependent.


Examples:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: md5sum(msg);
(%o3)                  ab07acbb1e496801937adfa772424bf7
(%i4) integer: md5sum(msg, 'number);
(%o4)                 0ab07acbb1e496801937adfa772424bf7
(%i5) octets: md5sum(msg, 'list);
(%o5)        [0AB,7,0AC,0BB,1E,49,68,1,93,7A,0DF,0A7,72,42,4B,0F7]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)           ab:07:ac:bb:1e:49:68:01:93:7a:df:a7:72:42:4b:f7
```


The argument may be a binary input stream.



```maxima
(%i1) S: openr_binary (file_search ("md5.lisp"));
(%o1) #<INPUT BUFFERED FILE-STREAM (UNSIGNED-BYTE 8)
  /home/robert/maxima/maxima-code/share/stringproc/md5.lisp>
(%i2) md5sum (S);
(%o2)           31a512ed53daf5b99495c9d05559355f
(%i3) close (S);
(%o3)                         true
```

### Function: mgf1_sha1 (mgf1_sha1, seed, len, mgf1_sha1, seed, len, return-type)

Returns a pseudo random number of variable length. 
By default the returned value is a number with a length of *len* octets.


The optional argument *return-type* allows `mgf1_sha1` to alternatively 
return the corresponding list of *len* octets.
*return-type* may be `number` or `list`.


The computation of the returned value is described in `RFC 3447`, 
appendix `B.2.1 MGF1`. 
`SHA1` is used as hash function, i.e. the randomness of the computed number
relies on the randomness of `SHA1` hashes.


Example:



```maxima
(%i1) ibase: obase: 16.$
(%i2) number: mgf1_sha1(4711., 8);
(%o2)                        0e0252e5a2a42fea1
(%i3) octets: mgf1_sha1(4711., 8, 'list);
(%o3)                  [0E0,25,2E,5A,2A,42,0FE,0A1]
```

### Function: number_to_octets (number)

Returns an octet-representation of *number* as a list of octets.
The *number* must be a non-negative integer.


Example:



```maxima
(%i1) ibase : obase : 16.$
(%i2) octets: [0ca,0fe,0ba,0be]$
(%i3) number: octets_to_number(octets);
(%o3)                            0cafebabe
(%i4) number_to_octets(number);
(%o4)                      [0CA, 0FE, 0BA, 0BE]
```

### Function: octets_to_number (octets)

Returns a number by concatenating the octets in the list of *octets*.


Example: See `number_005fto_005foctets`.

See also: `number_to_octets`.

### Function: octets_to_oid (octets)

Computes an object identifier (OID) from the list of *octets*.


Example: RSA encryption OID



```maxima
(%i1) ibase : obase : 16.$
(%i2) oid: octets_to_oid([2A,86,48,86,0F7,0D,1,1,1]);
(%o2)                      1.2.840.113549.1.1.1
(%i3) oid_to_octets(oid);
(%o3)               [2A, 86, 48, 86, 0F7, 0D, 1, 1, 1]
```

### Function: octets_to_string (octets_to_string, octets, octets_to_string, octets, encoding)

Decodes the list of *octets* into a string according to current system defaults. 
When decoding octets corresponding to Non-US-ASCII characters 
the result depends on the platform, application and underlying Lisp.


Example: Using system defaults 
(Maxima compiled with GCL, which uses no format definition and 
simply passes through the UTF-8-octets encoded by the GNU/Linux terminal).



```maxima
(%i1) octets: string_to_octets("abc");
(%o1)                            [61, 62, 63]
(%i2) octets_to_string(octets);
(%o2)                                 abc
(%i3) ibase: obase: 16.$
(%i4) unicode(20AC);
(%o4)                                  EUR
(%i5) octets: string_to_octets(%);
(%o5)                           [0E2, 82, 0AC]
(%i6) octets_to_string(octets);
(%o6)                                  EUR
(%i7) utf8_to_unicode(octets);
(%o7)                                20AC
```


In case the external format of the Lisp reader is equal to UTF-8 the optional 
argument *encoding* allows to set the encoding for the octet to string conversion. 
If necessary see `adjust_005fexternal_005fformat` for changing the external format. 


Some names of supported encodings (see corresponding Lisp manual for more): 

CCL, CLISP, SBCL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, cp1252, cp850` 

CMUCL: `utf-8, utf-16-be, utf-32-be, iso8859-1, cp1252` 

ECL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, windows-cp1252, dos-cp850` 

   

Example (continued): Using the optional encoding argument 
(Maxima compiled with SBCL, GNU/Linux terminal).



```maxima
(%i8) string_to_octets("EUR", "ucs-2be");
(%o8)                              [20, 0AC]
```

See also: `adjust_external_format`.

### Function: oid_to_octets (oid-string)

Converts an object identifier (OID) to a list of *octets*.


Example: See `octets_005fto_005foid`.

See also: `octets_to_oid`.

### Function: sha1sum (sha1sum, arg, sha1sum, arg, return-type)

Returns the `SHA1` fingerprint of a string, a non-negative integer or 
a list of octets. The default return value is a string containing 40 hex characters.


The optional argument *return-type* allows `sha1sum` to alternatively 
return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: sha1sum(msg);
(%o3)              c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i4) integer: sha1sum(msg, 'number);
(%o4)             0c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i5) octets: sha1sum(msg, 'list);
(%o5)  [0C7,56,7E,8B,39,0E2,42,8E,38,0BF,9C,92,26,0AC,68,0DE,4C,67,0DC,39]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)     c7:56:7e:8b:39:e2:42:8e:38:bf:9c:92:26:ac:68:de:4c:67:dc:39
```


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `SHA1` fingerprint is platform dependent.

### Function: sha256sum (sha256sum, arg, sha256sum, arg, return-type)

Returns the `SHA256` fingerprint of a string, a non-negative integer or 
a list of octets. The default return value is a string containing 64 hex characters.


The optional argument *return-type* allows `sha256sum` to alternatively 
return the corresponding number or list of octets (see `sha1sum`).


Example:



```maxima
(%i1) string: sha256sum("foo bar baz");
(%o1)  dbd318c1c462aee872f41109a4dfd3048871a03dedd0fe0e757ced57dad6f2d7
```


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `SHA256` fingerprint is platform dependent.

See also: `sha1sum`.

### Function: string_to_octets (string_to_octets, string, string_to_octets, string, encoding)

Encodes a *string* into a list of octets according to current system defaults. 
When encoding strings containing Non-US-ASCII characters 
the result depends on the platform, application and underlying Lisp.


In case the external format of the Lisp reader is equal to UTF-8 the optional 
argument *encoding* allows to set the encoding for the string to octet conversion. 
If necessary see `adjust_005fexternal_005fformat` for changing the external format. 


See `octets_005fto_005fstring` for examples and some more information.

See also: `adjust_external_format`, `octets_to_string`.

