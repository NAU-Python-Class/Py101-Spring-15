# Programming Concepts - Week 4 

> This file is all about practice. Writing all practices by yourself will improve your understanding in Python. Also I will put here more detailed, and somehow advanced examples, so you can challenge yourself practicing on them.

---

## List Basics
Concept of a list inside the Python is pretty similar to list in real life.We read off (access) items on our to-do list, add items, cross off (delete) items, and so forth. list is a linear data structure , meaning that its elements have a linear ordering.
 
 * Each item in the list is identifi ed by its index value .
 * It is customary in programming languages to begin numbering sequences of items with an index value of 0 rather than 1. (Except R language)
 
```Python 
## Following examples are all types of creating lists
list1 = list() # Creates an empty list
list2 = list([2,3,4]) # Creates a list with elements 2,3,4
list3 = list(["red", "green", "blue"]) # Creates a list with strings
list4 = list(range(3,6)) # Creates a list with elements 3,4,5
list5 = list("abcs") # Creats a list with characters a,b,c,d

## These are also creates lists
## I prefer to use this versions...
list1 = []
list2 = [2,3,4]
list3 = ["red", "green"]

## Lists can have different types of object in one list.

list4 = [2, "three", True]
```

> Here is the list of Common operations of list.

Operation     |  Description
----------    |  --------------
x in s        |           True if element x is in sequence s.
x not in s    |        True if element x is not in sequence s.
s1 + s2       |       Concatenates two sequences s1 and s2.
s * n, n * s n|      copies of sequence s concatenated.
s[i]          |     ith element in sequence s.
s[i : j]      |    Slice of sequence s from index i to j - 1.
len(s)        |   Length of sequence s, i.e., the number of elements in s.
min(s)        |       Smallest element in sequence s.
max(s)        |      Largest element in sequence s.
sum(s)        |     Sum of all numbers in sequence s.
for loop      |    Traverses elements from left to right in a for loop.
<, <=, >, >=, =, != |  Compares two sequences.

--- 

### Functions for Lists
There are some functions which are very useful when you are dealing with lists.You can use the __len__ function to return the number of elements in the list, the __max/min__ functions to return the elements with the greatest and lowest values in the list, and the __sum__ function to return the sum of all elements in the list. You can also use the __shuffle__ function in the _random_ module to shuffle the elements randomly in the list.

```Python
list1 = [2, 3, 4, 1, 32]
len(list) # Returns the size/length of the list
# 5

max(list1) # Returns the max element in the list
# 32

min(list1) # Returns the min element in the list
# 1

sum(list) # Takes the summation of all elements in the list.
# 42

import random # We will need this lib to use shuffle()
random.shuffle(list1) # Shuffle the elements in list
list1
# [4,1, 2, 32, 3]
```

### Index Operator []
An element in a list can be accessed through the index operator, using the syntax: myList[index]. myList[index] can be used as variable and for variables can be added together: ```myList[2] = myList[0] + myList[1]``` 

Using For loop reach every element in the list easily
```Python
for i in range(len(myList) - 1): # Don't forget to put - 1 because of indexation and scope of the loop rules...
    myList[i] = i 

## OR Same for While
i = 0 
while i < len(myList):
    print(myList[i])
    i += 1
```

Python Also uses negative numbers as a indexes to reference positions relative to the end of the list.

```Python 
list1 = [2, 3, 5, 2, 33, 21]
list1[-1]
# 21

list1[-3]
# 2
```
list[-1] is actually same as list1[-1 + len(list1)], which give s the last element in the list.

### List Slicing [start: end]
The slicing operator returns a slice of the list using the syntax list[start : end]. The slice is a sublist from index start to index end - 1. Here are some examples:

```Python
list1 = [2, 3, 5, 7, 9, 1]
list1[2 : 4]
# [5, 7]

list1 = [2, 3, 5, 2, 33, 21]
list1[ : 2]
# [2, 3]

list1[3 : ]
# [2, 33, 21]

list1 = [2, 3, 5, 2, 33, 21]
list1[1 : -3]
# [3, 5]

list1[-4 : -2]
# [3, 5]
```
> If start >= end, list[start : end] returns an empty list. If end specifies a position beyond the end of the list, Python will use the length of the list for end instead.

### The +/* and in/not in operators
We can use concatenation operator (+), and repetition operator (*) for lists.
```Python
list1 = [2, 3]
list2 = [1, 9]
list3 = list1 + list2
list3
# [2, 3, 1, 9]

list4 = 3 * list1
list4
# [2, 3, 2, 3, 2, 3]

list1 = [2, 3, 5, 2, 33, 21]
2 in list1
# True

2 not in list1
# False
```

### range() function
The standard way of using the ```range``` function is to give it a number to stop at, and ```range``` will give a list of values that start at 0 and go through the stop value minus 1. For example, calling ```range(stop)``` yields the following: 
```Pyhon
range(5)
# [0,1,2,3,4]
```
However, we can call ```range``` with some additional, optional parameters - a value to start at, and a step size. You can specify a start value by calling ```range(start, stop)```, like this: 
```Pyhton
range(2, 5)
# [2, 3, 4]
```
To specify a step size, you must specify a start value - the call is ```range(start, stop, stepSize)```, like this: 
```Python
range(2, 10, 2)
# [2, 4, 6, 8]
```

### Traversing Elements in a for loop
The elements in a Python list are iterable. Python supports a convenient for loop, which enables you to traverse the list sequentially without using an index variable.
```Python
## "For each element i in myList, print it."
for i in myList:
    print(i)
```
This version shows the elements at odd numbered positions.
```Python
for i in range(0, len(myList), 2):
    print(myList[i])
```
More examples on range function:
```Python
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
```

### sum() function
The function ```sum``` is a built-in function that takes one list as an argument and returns the sum of that list. The items in the list must be numeric types. Some examples: 
```Python
>>> sum([1, 9, 10])
20
>>> sum([4.5, 7, 0.331])
11.831
>>> sum(['a', 'b', 'c'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### List Comprehensions
List comprehensions provide a concise way to create a sequential list of elements. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The list comprehension produces a list with the results from evaluating the expression.

```Python
list1 = [x for x in range(5)] # Returns a list of 0, 1, 2, 3, 4
list1
# [0, 1, 2, 3, 4]

list2 = [0.5 * x for x in list1]
list2
# [0.0, 0.5, 1.0, 1.5, 2.0]

list3 = [x for x in list2 if x < 1.5]
list3
# [0.0, 0.5, 1.0]
```

### List Methods
Once you have the list created, you can use list class's methods to manipulate the list.The list class contains methods for manipulating a list:

Method Names                        |     Description
---------------------                   -----------------------           
append(x: object): None             | Adds an element x to the end of the list.
count(x: object): int               | Returns the number of times element x appears in the list.
extend(l: list): None               | Appends all the elements in l to the list.
index(x: object): int               | Returns the index of the first occurrence of element x in the list.
insert(index: int, x: object):None  | Inserts an element x at a given index. Note that the first element in the list has index 0.
pop(i): object                      | Removes the element at the given position and returns it. The parameter i is optional. If it is not specified, list.pop() removes and returns the last element in the list.
remove(x: object): None             | Removes the first occurrence of element x from the list.
reverse(): None                     | Reverses the elements in the list.
sort(): None                        | Sorts the elements in the list in ascending order.


Examples of using; append, count, extend, index, and insert methods:
```Python
list1 = [2,3,4,1, 32, 4]
list.append(19)
list1
# [2,3,4,1,32,4,19]

list1.count(4) # Return the count for number 4
# 2

list2 = [99, 54]
list1.extend(list2)
list1
# [2, 3, 4, 1, 32, 4, 19, 99, 54]

list1.index(4) # Return the index of number 4
# 2

list1.insert(1, 25) # Insert 25 at position index 1
list1
# [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
```
Examples of Using; insert, pop, remove, reverse, and sort methods:
```Python
list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
list1.pop(2) # Removes the element in the index 2
3 # Which is this one.

list1
# [2, 25, 4, 1, 32, 4, 19, 99, 54]

list1.pop()
# 54
list1
# [2, 25, 4, 1, 32, 4, 19, 99]

list.remove(32) # Remove number 32
list1
# [2, 25, 4, 1, 4, 19, 99]

list1.reverse() # Reverse the list
list1
# [99, 19, 4, 1, 4, 25, 2]

list1.sort() # Sort the list
list1
# [1, 2, 4, 4, 19, 25, 99]
```

### Splitting a String into a List
This is an intermediate topic but also the essential one for text handling operations. The str class contains the split method, which is useful for splitting items in a string into a list. For example, the following statement: ``` items = "Jane John Peter Susan".split()``` splits the string Jane John Peter Susan into the list ['Jane', 'John', 'Peter', 'Susan'].

* In the case above the items are delimited by spaces in the string. 
* You can use a nonspace delimeter ``` items = "02/08/15".split("/")``` splits the string 02/08/15 into the list ["02", "08", "15"]

### Inputting Lists
You may often need code that reads data from the console into a list. You can enter one data item per line and append it to a list in a loop. For example, the following code reads ten numbers one per line into a list.
```Python
lst = [] # Creates an empty list
print("Enter 10 numbers: ")
for i in range(10):
    lst.append(eval(input()))
```
Sometimes it is more convenient to enter the data in one line separated by spaces. You can use the string's split method to extract data from a line of input. For example, the following code reads ten numbers separated by spaces from one line into a list.
```Python
# Reads numbers as a string from the console
s = input("Enter 10 numbers separated by spaces from one line: ")
items = s.split() # Extracts items from the string
lst = [eval(x) for x in items] # Converts items to numbers
```

---

## Functions
Functions can be used to define reusable code and organize and simplify code.Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. If you create a program to add these three sets of numbers, your code might look like this:

```Python
sum = 0
for i in range(1, 11):
    sum += i
print("Sum from 1 to 10 is", sum)

sum = 0
for i in range(20, 38):
    sum += i
print("Sum from 20 to 37 is", sum)

sum = 0
for i in range(35, 50):
    sum += i
print("Sum from 35 to 49 is", sum)
```
It is pretty devastating, and think about it for more than 3. Let's try to write it in more usable way, using functions...
```Python
# Defining a sum function
def sum(n1, n2):
    result = 0 
    for i in range(n1, n2 + 1):
        result += i
    return result

# Defining main function invoke sum.
def main():
    print("Sum from 1 to 10 is", sum(1, 10))
    print("Sum from 20 to 37 is", sum(20, 37))
    print("Sum from 35 to 49 is", sum(35, 49))

main() # Calls the main function...
```
A function is a collection of statements grouped together that performs an operation.

### Defining a Function
Function syntax is made of function's name, parameters, and body. The syntax fo defining a function is as follows:
```Python
def functionName(list of parameters):
    # Function Body
```
Let's look at the function for finding max number:
```Python
def max(num1, num2): # Function headers with 2 formal parameters.
    # Function body Starts from here
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result     # Return Value...
    
# Invoke a function
z = max(x, y) # X and Y are actual parameters(arguments)

```

---

### Function with/without Return Values
There can be some functions without return values, we call them void functions, but they have some side effects on the code...
```Python
def printGrade(score):
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", end = " ")
    printGrade(score)

main() # Call the main function
```
 The code above does not have a return value, but we used it to call it into another function... What if we would like to have it with returns...
```Python
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'

def main():
    score = eval(input("Enter a score: "))
    print("The grade is", getGrade(score))
    
main()
```
The getGrade function returns a character, and it can be invoked and used just like a character. The printGrade function does not return a value, and it must be invoked as a statement.

> Technically, every function in Python returns a value whether you use return or not. If a function does not return a value, by default, it returns a special value None. For this reason, a function that does not return a value is also called a None function. The None value can be assigned to a variable to indicate that the variable does not reference any object. For example, if you run the following program:
```Python
def sum(number1, number2):
    total = number1 + number2
print(sum(1,2))
```
you will see the output is None, because the sum function does not have a return statement. By default, it returns None.

---

Thank you for your time, have a great learning!
 

