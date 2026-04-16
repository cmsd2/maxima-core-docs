## Bug Detection and Reporting

### Function: bug_report ()

Prints out Maxima and Lisp version numbers, and gives a link
to the Maxima project [https://sourceforge.net/p/maxima/bugsbug report web page]().
The version information is the same as reported by `build_005finfo`.


When a bug is reported, it is helpful to copy the Maxima
and Lisp version information into the bug report.


`bug_report` returns an empty string `""`.

See also: `build_info`.

### Function: build_info ()

Returns a summary of the parameters of the Maxima build,
as a Maxima structure (defined by `defstruct`).
When the pretty-printer is enabled (via `display2d`),
the structure is displayed as a short table.


The fields of the structure are:



- * 
version Maxima version
- * 
timestamp Time at which Maxima was compiled
- * 
host Type of system Maxima is running on
- * 
lisp_name Name of the Lisp implementation
- * 
lisp_version Version of the Lisp implementation
- * 
maxima_userdir User directory (value of `maxima_userdir`)
- * 
maxima_tempdir Directory for temporary files (value of `maxima_tempdir`)
- * 
maxima_objdir Directory for compiled files of share packages (value of `maxima_objdir`)
- * 
maxima_frontend Name of user interface, if any (value of `maxima_frontend`)
- * 
maxima_frontend_version User interface version when `maxima_frontend` is present (value of `maxima_frontend_version`)


See also `bug_005freport`.


Examples:













```maxima
(%i1) build_info ();
(%o1) 
Maxima-version: "5.48.1"
Maxima build date: "2025-08-23 10:39:15"
Host type: "x86_64-pc-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)"
User dir: "/home/dodier/.maxima"
Temp dir: "/tmp"
Object dir: "/home/dodier/.maxima/binary/5_48_1/clisp/2_49_93___2024_07_04___built_3935171094___memory_3964959574_"
Frontend: false


(%i2) x : build_info ()$
(%i3) x@version;
(%o3)                               5.48.1


(%i4) x@timestamp;
(%o4)                         2025-08-23 10:39:15


(%i5) x@host;
(%o5)                         x86_64-pc-linux-gnu


(%i6) x@lisp_name;
(%o6)                                CLISP


(%i7) x@lisp_version;
(%o7)        2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)


(%i8) x;
(%o8) 
Maxima-version: "5.48.1"
Maxima build date: "2025-08-23 10:39:15"
Host type: "x86_64-pc-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)"
User dir: "/home/dodier/.maxima"
Temp dir: "/tmp"
Object dir: "/home/dodier/.maxima/binary/5_48_1/clisp/2_49_93___2024_07_04___built_3935171094___memory_3964959574_"
Frontend: false
```


The Maxima version string (here 5.48.1) can look very different:



```maxima
(%i1) build_info();
(%o1) 
Maxima version: "branch_5_37_base_331_g8322940_dirty"
Maxima build date: "2016-01-01 15:37:35"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49 (2010-07-07) (built 3605577779) (memory 3660647857)"
```





In that case, Maxima was not build from a released sourcecode, 
but directly from the Git checkout of the source code.
In the example, the checkout is 331 commits after the latest Git tag
(usually a Maxima release, 5.37 in our example) and the 
abbreviated commit hash of the last commit was "8322940".


User interfaces for maxima can add information about currently being used
by setting the variables `maxima_frontend` and
`maxima_frontend_version` accordingly.

See also: `display2d`, `bug_report`.

### Function: run_testsuite (options)

Run the Maxima test suite.  Tests producing the desired answer are
considered “passes,” as are tests that do not produce the desired
answer, but are marked as known bugs.


`run_testsuite` takes the following optional keyword arguments



**display_all** — Display all tests.  Normally, the tests are not displayed, unless the test
fails.  (Defaults to `false`).
**display_known_bugs** — Displays tests that are marked as known bugs.  (Default is `false`).
**tests** — This is a single test or a list of tests that should be run.  Each test can be specified by
either a string or a symbol.  By default, all tests are run.  The complete set
of tests is specified by `testsuite_005ffiles`.
**time** — Display time information.  If `true`, the time taken for each
test file is displayed.  If `all`, the time for each individual
test is shown if `display_all` is `true`.  The default is
`false`, so no timing information is shown.
**share_tests** — Load additional tests for the `share` directory.  If `true`,
these additional tests are run as a part of the testsuite.  If
`false`, no tests from the `share` directory are run.  If
`only`, only the tests from the `share` directory are run.
Of course, the actual set of test that are run can be controlled by
the `tests` option. The default is `false`.
**answers_from_file** — Read answers to interactive questions from the source file. May only be
`false` or `true` (default). See also
`batch_005fanswers_005ffrom_005ffile`.


For example `run_testsuite(display_known_bugs = true, tests=[rtest5])`
runs just test `rtest5` and displays the test that are marked as
known bugs.


`run_testsuite(display_all = true, tests=["rtest1", rtest1a])` will
run tests `rtest1` and `rtest2`, and displays each test.


`run_testsuite` changes the Maxima environment.
Typically a test script executes `kill` to establish a known environment
(namely one without user-defined functions and variables)
and then defines functions and variables appropriate to the test.


`run_testsuite` returns `done`.

See also: `testsuite_files`, `batch_answers_from_file`, `kill`.

### Variable: share_testsuite_files

`share_testsuite_files` is the set of tests from the `share`
directory that is run as a part of the test suite by
`run_005ftestsuite`..

See also: `run_testsuite`.

### Variable: testsuite_files

`testsuite_files` is the set of tests to be run by
`run_005ftestsuite`.  It is a list of names of the files containing
the tests to run.  If some of the tests in a file are known to fail,
then instead of listing the name of the file, a list containing the
file name and the test numbers that fail is used.


For example, this is a part of the default set of tests:



```maxima
["rtest13s", ["rtest14", 57, 63]]
```


This specifies the testsuite consists of the files "rtest13s" and
"rtest14", but "rtest14" contains two tests that are known to fail: 57
and 63.

See also: `run_testsuite`.

