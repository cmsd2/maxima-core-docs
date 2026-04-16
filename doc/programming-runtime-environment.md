## Runtime Environment

### Function: absolute_real_time ()

Returns the number of seconds since midnight, January 1, 1900 GMT.
The return value is an integer.


See also `elapsed_real_time` and `elapsed_005frun_005ftime`.


Example:







```maxima
(%i1) absolute_real_time ();
(%o1)                      3385045277
(%i2) 1900 + absolute_real_time () / (365.25 * 24 * 3600);
(%o2)                   2007.265612087104
```

See also: `elapsed_real_time`, `elapsed_run_time`.

### Function: decode_time (decode_time, T, tz_offset, decode_time, T)

Given the number of seconds (possibly including a fractional part)
since midnight, January 1, 1900 GMT,
returns the date and time as represented by a list comprising
the year, month, day of the month, hours, minutes, seconds, and time zone offset.


*tz_offset* measures the offset of the time zone, in hours,
east (positive) or west (negative) of GMT.
*tz_offset* must be an integer, rational, or float between -24 and 24, inclusive.
If *tz_offset* is not a multiple of 1/3600, 
it is rounded to the nearest multiple of 1/3600.


If *tz_offset* is not present, the offset of the local time zone is assumed.


See also `encode_005ftime`.


Examples:











```maxima
(%i1) decode_time (0, 0);
(%o1)               [1900, 1, 1, 0, 0, 0, 0]
(%i2) decode_time (0);
(%o2)             [1899, 12, 31, 16, 0, 0, - 8]
(%i3) decode_time (2208988800, 9.25);
                                          37
(%o3)              [1970, 1, 1, 9, 15, 0, --]
                                          4
(%i4) decode_time (2208988800);
(%o4)             [1969, 12, 31, 16, 0, 0, - 8]
(%i5) decode_time (2208988800 + 1729/1000, -6);
                                      1729
(%o5)           [1969, 12, 31, 18, 0, ----, - 6]
                                      1000
(%i6) decode_time (2208988800 + 1729/1000);
                                      1729
(%o6)           [1969, 12, 31, 16, 0, ----, - 8]
                                      1000
```

See also: `encode_time`.

### Function: elapsed_real_time ()

Returns the number of seconds (including fractions of a second)
since Maxima was most recently started or restarted.
The return value is a floating-point number.


See also `absolute_real_time` and `elapsed_005frun_005ftime`.


Example:








```maxima
(%i1) elapsed_real_time ();
(%o1)                       2.559324
(%i2) expand ((a + b)^500)$
(%i3) elapsed_real_time ();
(%o3)                       7.552087
```

See also: `absolute_real_time`, `elapsed_run_time`.

### Function: elapsed_run_time ()

Returns an estimate of the number of seconds (including fractions of a second)
which Maxima has spent in computations since Maxima was most recently started
or restarted.  The return value is a floating-point number.


See also `absolute_real_time` and `elapsed_005freal_005ftime`.


Example:








```maxima
(%i1) elapsed_run_time ();
(%o1)                         0.04
(%i2) expand ((a + b)^500)$
(%i3) elapsed_run_time ();
(%o3)                         1.26
```

See also: `absolute_real_time`, `elapsed_real_time`.

### Function: encode_time (encode_time, year, month, day, hours, minutes, seconds, tz_offset, encode_time, year, month, day, hours, minutes, seconds)

Given a time and date specified by
*year*, *month*, *day*, *hours*, *minutes*, and *seconds*,
`encode_time` returns the number of seconds (possibly including a fractional part)
since midnight, January 1, 1900 GMT.


*year* must be an integer greater than or equal to 1899.
However, 1899 is allowed only if the resulting encoded time is greater than or equal to 0.


*month* must be an integer from 1 to 12, inclusive.


*day* must be an integer from 1 to *n*, inclusive,
where *n* is the number of days in the month specified by *month*.


*hours* must be an integer from 0 to 23, inclusive.


*minutes* must be an integer from 0 to 59, inclusive.


*seconds* must be an integer, rational, or float
greater than or equal to 0 and less than 60.
When *seconds* is not an integer,
`encode_time` returns a rational,
such that the fractional part of the return value is equal to the fractional part of *seconds*.
Otherwise, *seconds* is an integer, and the return value is likewise an integer.


*tz_offset* measures the offset of the time zone, in hours,
east (positive) or west (negative) of GMT.
*tz_offset* must be an integer, rational, or float between -24 and 24, inclusive.
If *tz_offset* is not a multiple of 1/3600, 
it is rounded to the nearest multiple of 1/3600.


If *tz_offset* is not present, the offset of the local time zone is assumed.


See also `decode_005ftime`.


Examples:











```maxima
(%i1) encode_time (1900, 1, 1, 0, 0, 0, 0);
(%o1)                           0
(%i2) encode_time (1970, 1, 1, 0, 0, 0, 0);
(%o2)                      2208988800
(%i3) encode_time (1970, 1, 1, 8, 30, 0, 8.5);
(%o3)                      2208988800
(%i4) encode_time (1969, 12, 31, 16, 0, 0, -8);
(%o4)                      2208988800
(%i5) encode_time (1969, 12, 31, 16, 0, 1/1000, -8);
                          2208988800001
(%o5)                     -------------
                              1000
(%i6) % - 2208988800;
                               1
(%o6)                         ----
                              1000
```

See also: `decode_time`.

### Variable: maxima_tempdir

`maxima_tempdir` names the directory in which Maxima creates some temporary
files.  In particular, temporary files for plotting are created in
`maxima_tempdir`.


The initial value of `maxima_tempdir` is the user’s home directory, if
Maxima can locate it; otherwise Maxima makes a guess about a suitable directory.


`maxima_tempdir` may be assigned a string which names a directory.

### Variable: maxima_userdir

`maxima_userdir` names a directory which Maxima searches to find Maxima and
Lisp files.  (Maxima searches some other directories as well;
`file_search_maxima` and `file_search_lisp` are the complete lists.)


The initial value of `maxima_userdir` is a subdirectory of the user’s home
directory, if Maxima can locate it; otherwise Maxima makes a guess about a
suitable directory.


`maxima_userdir` may be assigned a string which names a directory.
However, assigning to `maxima_userdir` does not automatically change
`file_search_maxima` and `file_search_lisp`;
those variables must be changed separately.

### Function: parse_timedate (parse_timedate, S)

Parses a string *S* representing a date or date and time of day
and returns the number of seconds since midnight, January 1, 1900 GMT.
If there is a nonzero fractional part, the value returned is a rational number,
otherwise, it is an integer.
`parse_timedate` returns `false`
if it cannot parse *S* according to any of the allowed formats.


The string *S* must have one of the following formats,
optionally followed by a timezone designation:



- *
`YYYY-MM-DD[ T]hh:mm:ss[,.]nnn`
- *
`YYYY-MM-DD[ T]hh:mm:ss`
- *
`YYYY-MM-DD`


where the fields are year, month, day, hours, minutes, seconds, and fraction of a second,
and square brackets indicate acceptable alternatives.
The fraction may contain one or more digits.


Except for the fraction of a second,
each field must have exactly the number of digits indicated:
four digits for the year, and two for the month, day of the month, hours, minutes, and seconds.


A timezone designation must have one of the following forms:



- *
`[+-]hh:mm`
- *
`[+-]hhmm`
- *
`[+-]hh`
- *
`Z`


where `hh` and `mm` indicate hours and minutes east (`+`) or west (`-`) of GMT.
The timezone may be from +24 hours (inclusive) to -24 hours (inclusive).


A literal character `Z` is equivalent to `+00:00` and its variants,
indicating GMT.


If no timezone is indicated,
the time is assumed to be in the local time zone.


Any leading or trailing whitespace (space, tab, newline, and carriage return) is ignored,
but any other leading or trailing characters cause `parse_timedate` to fail and return `false`.


See also `timedate` and `absolute_005freal_005ftime`.


Examples:


Midnight, January 1, 1900, in the local time zone, in each acceptable format.
The result is the number of seconds the local time zone
is ahead (negative result) or behind (positive result) GMT.
In this example, the local time zone is 8 hours behind GMT.












```maxima
(%i1) parse_timedate ("1900-01-01 00:00:00,000");
(%o1)                         28800
(%i2) parse_timedate ("1900-01-01 00:00:00.000");
(%o2)                         28800
(%i3) parse_timedate ("1900-01-01T00:00:00,000");
(%o3)                         28800
(%i4) parse_timedate ("1900-01-01T00:00:00.000");
(%o4)                         28800
(%i5) parse_timedate ("1900-01-01 00:00:00");
(%o5)                         28800
(%i6) parse_timedate ("1900-01-01T00:00:00");
(%o6)                         28800
(%i7) parse_timedate ("1900-01-01");
(%o7)                         28800
```


Midnight, January 1, 1900, GMT, in different indicated time zones.












```maxima
(%i1) parse_timedate ("1900-01-01 19:00:00+19:00");
(%o1)                           0
(%i2) parse_timedate ("1900-01-01 07:00:00+07:00");
(%o2)                           0
(%i3) parse_timedate ("1900-01-01 01:00:00+01:00");
(%o3)                           0
(%i4) parse_timedate ("1900-01-01Z");
(%o4)                           0
(%i5) parse_timedate ("1899-12-31 21:00:00-03:00");
(%o5)                           0
(%i6) parse_timedate ("1899-12-31 13:00:00-11:00");
(%o6)                           0
(%i7) parse_timedate ("1899-12-31 08:00:00-16:00");
(%o7)                           0
```

See also: `timedate`, `absolute_real_time`.

### Function: room (room, room, true, room, false)

Prints out a description of the state of storage and
stack management in Maxima.  `room` calls the Lisp function of 
the same name.



- *
`room ()` prints out a moderate description.
- *
`room (true)` prints out a verbose description.
- *
`room (false)` prints out a terse description.

### Function: sstatus (keyword, item)

When *keyword* is the symbol `feature`, *item* is put on the list
of system features.  After `sstatus (keyword, item)` is executed,
`status (feature, item)` returns `true`.  If *keyword* is the
symbol `nofeature`, *item* is deleted from the list of system features.
This can be useful for package writers, to keep track of what features they have
loaded in.


See also `status`.

See also: `status`.

### Function: status (status, feature, status, feature, item)

Returns information about the presence or absence of certain system-dependent 
features.



- *
`status (feature)` returns a list of system features. These include Lisp 
version, operating system type, etc. The list may vary from one Lisp type to 
another.
- * 
`status (feature, item)` returns `true` if *item* is on the
list of items returned by `status (feature)` and `false` otherwise.
`status` quotes the argument *item*. The quote-quote operator 
`''` defeats quotation. A feature whose name contains a special 
character, such as a hyphen, must be given as a string argument. For example,
`status (feature, "ansi-cl")`.


See also `sstatus`.


The variable `features` contains a list of features which apply to 
mathematical expressions. See `features` and `featurep` for more 
information.

See also: `sstatus`.

### Function: system (system, command, arg_1, ..., arg_n, system, command)

Executes *command* as a separate process.
The command is passed to the default shell for execution.


`system` is implemented by a command execution function
in the Lisp implementation which compiled Maxima,
and therefore the behavior of `system`
varies with the operating system and Lisp implementation.
`system` is known to work on Windows and Linux systems,
and might also work on other systems.


All combinations of Lisp implementation and operating system
allow command arguments as *arg_1*, ..., *arg_n*,
and some allow command arguments as part of *command*.
SBCL on Windows and Clozure CL on Windows are known to require
command arguments to be specified as *arg_1*, ..., *arg_n*.


`system` does not attempt to quote or escape spaces or other characters
in *command* or in *arg_1*, ..., *arg_n*;
all arguments are supplied verbatim to the command execution function of the Lisp implementation.


Standard output from *command* is displayed on the Maxima console by default,
and may be captured by `with_stdout`.


For most Lisp implementations,
the call to `system` returns after *command* has completed.
Job control operations,
such as executing a command asynchronously with respect to Maxima,
are not known to have the expected effect.


Examples:




`system` executes *command* as a separate process.
The output of the command `dir` varies from one system to another.





```maxima
(%i1) system ("dir", maxima_tempdir);
config-err-UsLLQM
gnome-software-0TNK22
MozillaUpdateLock-6939C585ADF59520
snap-private-tmp
systemd-private-169e359ab2d94b208622fa96dd88c05e-colord.service-ZP9Xn7
(%o1)                           0
```


All combinations of Lisp implementation and operating system
allow command arguments as *arg_1*, ..., *arg_n*.





```maxima
(%i1) system ("echo", "Hello", "world", "glad", "to", "meet", "you");
Hello world glad to meet you
(%o1)                           0
```


Standard output from *command* is displayed on the Maxima console by default,
and may be captured by `with_stdout`.










```maxima
(%i1) my_output: sconcat (maxima_tempdir, "/tmp.out");
(%o1)                     /tmp/tmp.out
(%i2) with_stdout (my_output, system ("dir"));
(%o2)                           0
(%i3) S: openr (my_output);
(%o3)               #<FILE-STREAM {7B500975}>
(%i4) readline (S);
(%o4)                      aclocal.m4
(%i5) readline (S);
(%o5)                         admin
(%i6) readline (S);
(%o6)                        archive
```


For most Lisp implementations,
the call to `system` returns after *command* has completed.
`xfontsel` is a utility to inspect fonts for the X Windows system;
`system` returns after the user clicks the "quit" button.





```maxima
(%i1) system ("xfontsel");
(%o1)                           0
```

### Function: time (%o1, %o2, %o3, ...)

Returns a list of the times, in seconds, taken to compute the output lines
`%o1`, `%o2`, `%o3`, ... The time returned is Maxima’s
estimate of the internal computation time, not the elapsed time.  `time`
can only be applied to output line variables; for any other variables,
`time` returns `unknown`.


Set `showtime: true` to make Maxima print out the computation time 
and elapsed time with each output line.

### Function: timedate (timedate, T, tz_offset, timedate, T, timedate)

`timedate(T, tz_offset)` returns a string
representing the time *T* in the time zone *tz_offset*.
The string format is `YYYY-MM-DD HH:MM:SS.NNN[+|-]ZZ:ZZ`
(using as many digits as necessary to represent the fractional part)
if *T* has a nonzero fractional part,
or `YYYY-MM-DD HH:MM:SS[+|-]ZZ:ZZ` if its fractional part is zero.


*T* measures time, in seconds, since midnight, January 1, 1900,
in the GMT time zone.


*tz_offset* measures the offset of the time zone, in hours,
east (positive) or west (negative) of GMT.
*tz_offset* must be an integer, rational, or float between -24 and 24, inclusive.
If *tz_offset* is not a multiple of 1/60, 
it is rounded to the nearest multiple of 1/60.


`timedate(T)` is equivalent to `timedate(T, tz_offset)`
with *tz_offset* equal to the offset of the local time zone.


`timedate()` is equivalent to `timedate(absolute_real_time())`.
That is, it returns the current time in the local time zone.


Example:


`timedate` with no argument returns a string representing the current time and date.







```maxima
(%i1) d : timedate ();
(%o1)                      2010-06-08 04:08:09+01:00
(%i2) print ("timedate reports current time", d) $
timedate reports current time 2010-06-08 04:08:09+01:00
```


`timedate` with an argument returns a string representing the argument.







```maxima
(%i1) timedate (0);
(%o1)                      1900-01-01 01:00:00+01:00
(%i2) timedate (absolute_real_time () - 7*24*3600);
(%o2)                      2010-06-01 04:19:51+01:00
```


`timedate` with optional timezone offset.






```maxima
(%i1) timedate (1000000000, -9.5);
(%o1)               1931-09-09 16:16:40-09:30
```

