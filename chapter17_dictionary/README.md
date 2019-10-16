## Data Structure - Dictionary

Exercise from chapter 17 of `Learn You more Python`

To run the tests:
```
python -m unittest -v test_dict
```

## Analysis of data structure

The Dictionary comprises of a single double linked list which contains other double linked lists to hold the data.

Each node in the dictionary map points to a dobule linked list where the key-value pairs are stored.

Each key value pair is stored in a node within a map's list as a tuple
```
node.value = (key, value)
```

For a new entry, it is appended to the end of the `bucket` as a new node.

If a key exists, it returns the existing node as a `slot` within the `bucket`(list)
and replaces the value in the existing node.

The core logic to get/set values are dependent on `get_bucket` function which creates
a hash of the key with the length of the map to return the given list/bucket within the map.

The function `get_slot` traverses the nodes in a given list from the `get_bucket` function and returns both the bucket and node if they exist.

The function `hash_key` returns an index into the map to retrive the list. It uses the built-in `hash()` function to generate a unique value based on the key. The `hash()` function is used to provide quick dictionary lookup for getting/setting values.