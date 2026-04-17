## operatingsystem

<!-- category: Other -->
<!-- keywords: chdir -->
<!-- signatures: chdir(dir) -->
### Function: chdir (dir)

Change to directory *dir*

<!-- category: Other -->
<!-- keywords: getcurrentdirectory -->
<!-- signatures: getcurrentdirectory() -->
### Function: getcurrentdirectory ()

returns the current working directory.


See also `directory`.

See also: `directory`.

<!-- category: Other -->
<!-- keywords: getenv -->
<!-- signatures: getenv(env) -->
### Function: getenv (env)

Get the value of the environment variable *env*


Example:



```maxima
(%i1) load("operatingsystem")$
(%i2) getenv("PATH");
(%o2) /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

<!-- category: Other -->
<!-- keywords: mkdir -->
<!-- signatures: mkdir(dir) -->
### Function: mkdir (dir)

Create directory *dir*

<!-- category: Other -->
<!-- keywords: rmdir -->
<!-- signatures: rmdir(dir) -->
### Function: rmdir (dir)

remove directory *dir*

