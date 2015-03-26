# Programming Concepts - Week 5

> This file is all about practice. Writing all practices by yourself will improve your understanding in Python. Also I will put here more detailed, and somehow advanced examples, so you can challenge yourself practicing on them.

---

## Dictionaries
Dictionaries are one of the most flexible built-in data types in Python.You can think of dictionaries as unordered collections; the chief distinction is that in dictionaries, items are stored and fetched by key, instead of by positional offset. 

Dictionaries can replace many of the searching algorithms and data structures you might have to implement manually in lower-level languages—as a highly optimized built-in type, indexing a dictionary is a very fast search operation. There are some features of dictionaries:

- Accessed by key, not offset position(index):
	-  They are sometimes called associative arrays or hashes. They associate a set of values with keys, so you can fetch an item out of a dictionary using the key under which you originally stored it.
- Unordered collections of arbitrary objects
	- Unlike in a list, items stored in a dictionary aren’t kept in any particular order; in fact, Python pseudo-randomizes their left-to-right order to provide quick lookup.
- Variable-length, heterogeneous, and arbitrarily nestable
	- Like lists, dictionaries can grow and shrink in place (without new copies being made), they can contain objects of any type, and they support nesting to any depth (they can contain lists, other dictionaries, and so on). Each key can have just one associated value, but that value can be a collection of multiple objects if needed, and a given value can be stored under any number of keys.
- Mutable mapping
	- You can change dictionaries in place by assigning to indexes (they are mutable), but they don’t support the sequence operations that work on strings and lists.
- Hash Tables
	- If lists are arrays of object references that support access by position, dictionaries are unordered tables of object references that support access by key. Internally, dictionaries are implemented as hash tables

### Basic Dictionary Operations

```Python 
D = {'spam': 2, 'ham': 1, 'eggs': 3} # Makes a dictionary
D['spam']
# 2
D  # Showing order is not important
# {'eggs': 3, 'spam': 2, 'ham': 1}

# Number of entries
len(D) 
# 3

# testing by key
'ham' in D
# True

# Creates a new list of D's keys
list(D.keys())
# ['eggs', 'spam', 'ham']

```

### Changing Dictionaries in Place
```Python
D
# {'eggs': 3, 'spam': 2, 'ham': 1}

# Changing entry (value = list)
D['ham'] = ['grill', 'bake', 'fry']
D
# {'eggs': 3, 'spam': 2, 'ham': ['grill', 'bake', 'fry']}

# Delete entry
del D['eggs']
D
# {'spam': 2, 'ham': ['grill', 'bake', 'fry']}

# Adds new entry
D['brunch'] = 'Bacon'
D
# {'brunch': 'Bacon', 'spam': 2, 'ham': ['grill', 'bake', 'fry']}
```

### More Dictionary Methods

```Python
D = {'spam': 2, 'ham': 1, 'eggs': 3}
list(D.values())
# [3, 2, 1]
list(D.items())
# [('eggs', 3), ('spam', 2), ('ham', 1)]


# A key that is there
D.get('spam')
# 2

# A key that is missing
print(D.get('toast'))
# None

# Assings 'toast' to 88 get the result
D.get('toast', 88)
# 88

D
# {'eggs': 3, 'spam': 2, 'ham': 1}
D2 = {'toast':4, 'muffin':5} # Lots of delicious scrambled order here

# Updates D with items in D2
D.update(D2)
D
# {'eggs': 3, 'muffin': 5, 'toast': 4, 'spam': 2, 'ham': 1}

# pop a dictionary by key
D
# {'eggs': 3, 'muffin': 5, 'toast': 4, 'spam': 2, 'ham': 1}
D.pop('muffin')
# 5
D.pop('toast') # Delete and return from a key
# 4
D
# {'eggs': 3, 'spam': 2, 'ham': 1}

# pop a list by position
L = ['aa', 'bb', 'cc', 'dd']
L.pop() # Delete and return from the end
# 'dd'

L
# ['aa', 'bb', 'cc']
L.pop(1) # Delete from a specific position
# 'bb'
L
# ['aa', 'cc']
```


## Tuples

Tuples construct simple groups of objects. They work exactly like lists, except that tuples can’t be changed in place (they’re immutable) and are usually written as a series of items in parentheses, not square brackets. Although they don’t support as many methods, tuples share most of their properties with lists. Here are the features of tuples:

- Ordered collections of arbitrary objects
	- Like strings and lists, tuples are positionally ordered collections of objects (i.e., they maintain a left-to-right order among their contents); like lists, they can embed any kind of object.
- Accessed by offset
	- Like strings and lists, items in a tuple are accessed by offset (not by key); they support all the offset-based access operations, such as indexing and slicing.
- Of the category “immutable sequence”
	- Like strings and lists, tuples are sequences; they support many of the same operations. However, like strings, tuples are immutable; they don’t support any of the in-place change operations applied to lists.
- Fixed-length, heterogeneous, and arbitrarily nestable
	- Because tuples are immutable, you cannot change the size of a tuple without making a copy. On the other hand, tuples can hold any type of object, including other compound objects (e.g., lists, dictionaries, other tuples), and so support arbitrary nesting.
- Arrays of object references
	- Like lists, tuples are best thought of as object reference arrays; tuples store access points to other objects (references), and indexing a tuple is relatively quick.


### Tuples usage
```Python

```















