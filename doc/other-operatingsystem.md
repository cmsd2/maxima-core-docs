## operatingsystem

### Function: chdir (dir)

Change to directory *dir*

### Function: getcurrentdirectory ()

returns the current working directory.


See also `directory`.

See also: `directory`.

### Function: getenv (env)

Get the value of the environment variable *env*


Example:



```maxima
(%i1) load("operatingsystem")$
(%i2) getenv("PATH");
(%o2) /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### Function: mkdir (dir)

Create directory *dir*

### Function: rmdir (dir)

remove directory *dir*

