## Study Drills

1. How much of `find` did you implement?

   Only managed to implement the directory, `name` , `type`, `exec` arguments

2. What are the libraries you have found to improve this implementation?

   I found that the `pathlib` module useful.

   For instance, I can construct a Path object which can take a relative
   path and search for wildcard file extensions within it.

   Normally, that could only be done using combination of 2 or more modules,
   such as with `os` and `glob`

 ## References:

 * (pathlib documentation)[https://docs.python.org/3/library/pathlib.html]

 * (subprocess documentation)[https://docs.python.org/3/library/subprocess.html#subprocess.check_output]

 * (subprocess examples)[http://queirozf.com/entries/python-3-subprocess-examples#run-command-and-capture-output]