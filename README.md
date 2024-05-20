### ALX AirBnB Clone Project

#### Description

This project serves as the launchpad for your very own Airbnb clone! We'll begin by constructing a robust console application, the backbone of your lodging management system.

#### How to use

Run the console -> ./console.py <br />
Quit the console -> (hbnb) quit <br />
Display the help for a command -> (hbnb) help <command> <br />
Create an object (prints its id) -> (hbnb) create <class> <br />
Show an object -> (hbnb) show <class> <id> or (hbnb) <class>.show(<id>) <br />
Destroy an object -> (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>) <br />
Show all objects, or all instances of a class -> (hbnb) all or (hbnb) all <class> <br />
Update an attribute of an object -> (hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") <br />

#### Interactive Mode Example

$ ./console.py
(hbnb) help

# Documented commands (type help <topic>):

EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$

#### Non-Interactive Mode Example

$ echo "help" | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help quit
(hbnb)
$

#### Tests

$ python3 unittest -m discover tests -> for all test files

$ python3 unittest -m tests/test_console.py -> for specific test file

#### Authors

AbdisaDev -> <abdisaDev@gmail.com>
