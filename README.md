# holbertonschool-AirBnB_clone

## AirBnb Console - Project's Intention

Similar to how we created a simple shell using
the C Language, we are creating a command
interpreter that works in similar fashion but is
limited to specific use-cases.

Use-cases our project will be able to manage:

- Create new objects (ex: new User or a new
  Place).
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats,
  etc).
- Update attributes of an object.
- Destroy an object.

## Learning Objectives

| Objective                                                          | Description                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to create a Python package                                     | A Python package is a way of organizing related modules into a directory hierarchy. It involves creating a directory, placing related modules inside it, and adding an `__init__.py` file.                                                                            |
| How to create a command interpreter in Python using the cmd module | The `cmd` module in Python provides a framework for building line-oriented command interpreters. It can be used to build interactive shells and other command interpreters.                                                                                           |
| What is Unit testing and how to implement it in a large project    | Unit testing is a method of software testing that checks whether individual components of the source code are working correctly. It involves writing test cases for each function or method in your code and running them to ensure they produce the expected output. |
| How to serialize and deserialize a Class                           | Serialization is the process of converting a data structure or object state into a format that can be stored or transmitted and reconstructed later. In Python, you can use the `pickle` module for serialization and deserialization.                                |
| How to write and read a JSON file                                  | JSON (JavaScript Object Notation) is a popular data format with diverse uses in data interchange, including that of web applications with servers. In Python, you can use the `json` module to read and write JSON files.                                             |
| How to manage datetime                                             | The `datetime` module in Python is used for dealing with dates and times. It provides classes for manipulating dates and times in a simple and complex way.                                                                                                           |
| What is an UUID                                                    | UUID (Universally Unique Identifier) is a python library which helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).                                              |
| What is \*args and how to use it                                   | `*args` in Python is used to pass a variable number of non-keyworded arguments to a function. It allows you to pass any number of positional arguments to the function.                                                                                               |
| What is \*\*kwargs and how to use it                               | `**kwargs` in Python is used to pass a variable number of keyworded arguments to a function. It allows you to pass any number of keyword arguments to the function.                                                                                                   |
| How to handle named arguments in a function                        | Named arguments, also known as keyword arguments, are used in function calls. They allow the caller to specify the argument name along with its value, making it easier to understand what value is being passed for which function parameter.                        |

## Program's Usage:

## Interactive Mode

Your shell should work like this in interactive mode:

```bash
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

## Non-Interactive Mode

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

## Project Structure

| File/Folder                      | Description                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `AUTHORS`                        | Contains information about the authors of the project.                                |
| `console.py`                     | Contains the main entry point of the command interpreter.                             |
| `file.json`                      | This file is used to store all objects.                                               |
| `__init__.py`                    | Makes the folder a Python module.                                                     |
| `models/`                        | This folder contains all the classes used in this project.                            |
| `README.md`                      | This is the file you are currently reading, contains information about this project.  |
| `test_base_model_dict.py`        | Contains the unit tests for the `BaseModel` class (dictionary representation).        |
| `test_base_model.py`             | Contains the unit tests for the `BaseModel` class.                                    |
| `tests/`                         | This folder contains all the unit tests for the project.                              |
| `test_save_reload_base_model.py` | Contains the unit tests for the `save` and `reload` methods of the `BaseModel` class. |
| `test_save_reload_user.py`       | Contains the unit tests for the `save` and `reload` methods of the `User` class.      |

## Models Structure

| File/Folder     | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| `amenity.py`    | Contains the `Amenity` class.                                                            |
| `base_model.py` | Contains the `BaseModel` class, the parent class for all other classes.                  |
| `city.py`       | Contains the `City` class.                                                               |
| `engine/`       | This folder contains the storage engine for the project.                                 |
| `__init__.py`   | Makes the folder a Python module.                                                        |
| `place.py`      | Contains the `Place` class.                                                              |
| `__pycache__/`  | This folder contains Python3 byte code files that are automatically generated by Python. |
| `review.py`     | Contains the `Review` class.                                                             |
| `state.py`      | Contains the `State` class.                                                              |
| `user.py`       | Contains the `User` class.                                                               |

## Engine Structure

| File/Folder       | Description                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| `file_storage.py` | Contains the `FileStorage` class that serializes instances to a JSON file and deserializes JSON file to instances. |
| `__init__.py`     | Makes the folder a Python module.                                                                                  |
| `__pycache__/`    | This folder contains Python3 byte code files that are automatically generated by Python.                           |

## Tests Structure

| File/Folder    | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| `__init__.py`  | Makes the folder a Python module.                                      |
| `test_models/` | This folder contains all the unit tests for the models in the project. |

## Test Models Structure

| File/Folder            | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| `__init__.py`          | Makes the folder a Python module.                                                        |
| `__pycache__/`         | This folder contains Python3 byte code files that are automatically generated by Python. |
| `test_base_model.py`   | Contains the unit tests for the `BaseModel` class.                                       |
| `test_engine/`         | This folder contains all the unit tests for the engine in the project.                   |
| `test_file_storage.py` | Contains the unit tests for the `FileStorage` class.                                     |

## Test Engine Structure

## Test Engine Structure

| File/Folder            | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `__init__.py`          | Makes the folder a Python module.                    |
| `test_file_storage.py` | Contains the unit tests for the `FileStorage` class. |

```

```
