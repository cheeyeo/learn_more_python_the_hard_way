## Chapter 11 - uniq command

Python rewriting of the `uniq` linux command.

Example usage:
```
history | sed -e "s/^[ 0-9]*//g" | cut -d ' ' -f 1 | sort | python uniq.py
```

`uniq.py` only accepts stdin input since it relies on the output of previous commands to find unique entries. e.g. a pipe command like above example

Options:
```
-c => Show number of occurences of each unique entry
```

## Study Drills

1. In order to fully implement a solution using other programs written previously, the two projects need further modification: `sed` and `cut` 

Need to add command line options to `sed` and to remove required command option from cut


