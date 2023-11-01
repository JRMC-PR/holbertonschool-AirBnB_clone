# holbertonschool-AirBnB_clone

## AirBnb Console - Project's Intention

Similar to how we created a simple shell using
the C Language, we are creating a command
interpreter that works in similar fashion but is
limited to specific use-cases.

Use-cases our project will be able to manage:

* Create new objects (ex: new User or a new
Place).
* Retrieve an object from a file, a database, etc.
* Do operations on objects (count, compute stats,
etc).
* Update attributes of an object.
* Destroy an object.

## Program's Usage:

To bring some context to the table, the file that
allows us to manage cases is named **console.py**.

*ALSO*, similar to our previous shell, there are two ways of execution to our program:

**INTERACTIVE MODE**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```


**NON-INTERACTIVE**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

