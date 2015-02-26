# Exercise #3 ~ Functions

## Part 1
Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, write 'error'. If the result is a function,  write 'function'. As always, try to do this problem by hand before turning to your interpreter. Provide a type of result and result itself. __Assume this function already defined.__
```Python
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
```
1.  ```a(False, 2, 3```
2.  ```b(3, 2)```
3.  ```a(3>2, a, b)```
4.  ```b(a, b)```

## Part 2

1. Write a python function, ```square```, that takes in one number and returs the square of that number. This function takes in one number and returns one number. 

2. Write a Python function, ```evalQuadratic(a, b, c, x)```, that returns the value of the quadratic ```a*x^2 + b*x + c```. This function takes in four numbers and returns a single number. 

3. Write a Python function, ```clip(lo, x, hi)``` that returns ```lo``` if ```x``` is less than ```lo```; ```hi``` if ```x``` is greater than ```hi```; and ```x``` otherwise. For this problem, you can assume that ```lo < hi```.  Don't use any conditional statements for this problem. Instead, use the built in Python functions ```min``` and ```max```. You may wish to read the [documentation on min](http://docs.python.org/library/functions.html#min) and the [documentation on max](http://docs.python.org/library/functions.html#max), and play around with these functions a bit in your interpreter, before beginning this problem. This function takes in three numbers and returns a single number. 

4. Write a Python function, ```fourthPower```, that takes in one number and returns that value raised to the fourth power. You should use the ```square``` procedure that you defined in question 1. This function takes in one number and returns one number.

5. Write a Python function, ```odd```, that takes in one number and returns ```True``` when the number is odd and ```False``` otherwise.You should use the ```%```(mod) operator, not ```if```.This function takes in one number and returns a boolean.

6. Define a function ```isVowel(char)``` that returns True if ```char``` is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that ```char``` is a single letter of any case (ie, 'A' and 'a' are both valid). Do not use the keyword ```in```. Your function should take in a single string and return a boolean.

7. Define a function ```isVowel2(char)``` that returns True if ```char``` is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that ```char``` is a single letter of any case (ie, 'A' and 'a' are both valid). This function is similar to the previous problem - but this time, do use the keyword ```in```. Your function should take in a single string and return a boolean.


## Part 3
Provide a type of result and result itself.
1.
```Python
a = 10
def f(x):
    return x + a
a = 3
f(1)
```
2.
```Python
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)
```
3.
```Python
def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

foo(3)
```
4.
```Python
def foo (x):
   def bar (z):
      return z + x
   return bar(3)

foo(2)
```
