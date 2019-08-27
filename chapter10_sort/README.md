## Sort program

Implementation of `sort` util in python.

Exercise from chapter 10 of 'Learn You More Python The Hard Way'

To run:
```
python sort.py [input file] [options]
``` 

To input from stdin:
```
ls | python sort.py [options]
```

To do numeric sort:
```
echo -e "1\n10\n11\n2\n3" | python sort.py -g
```

Options:
```
-r => Reverse sort

-f => Ignore case sort

-g => Numeric sort
```


## References
* (Python docs on sorting)[https://docs.python.org/3.6/howto/sorting.html]