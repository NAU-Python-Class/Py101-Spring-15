# Programming Concepts - Week 2

> This file is all about practice. Writing all practices by yourself will improve your understanding in Python. Also I will put here more detailed, and somehow advanced examples, so you can challenge yourself practicing on them.

---

## Get to know Variables

The word variable in programming describes a place to store information such as numbers, text, lists of numbers and text, and so
on. Another way of looking at a variable is that it's like a label for something.

We making a variable using assingment operator "="
We assigned integer value 100 to variable name called thompson: ``` thompson = 100 ```, it will allow us to use it again and again.

```Python 
thompson = 100
print(thompson)

# We can rewrite the variables, they are recyclable
thompson = 200
print(thompson)

# We can copy values inside of the thompson to enes variable
# right-hand side is the source 
# left-hand side is where we assigning tos 
enes = thompson
print(enes)
```

* There are some signs that we cannot use when we are naming our variables such as $,%,@,^,etc.

* Also we cannot use reserved words as they are.

```Python
na$me = "Enes Kemal" # Wrong
nam^e = "Enes Kemal" # Wrong
this = 5 # Wrong
is = 10 # Wrong
this_is = 1 # Correct
for = "string" # Wrong

```

## Why Spacing is important for Python?

Python uses indentation(having spaces to indicate it is inside of some statements.) Controls structures, functions, classes, methods, all need some indentation to be specify the hierarchical order.

In R language you use brackets to specify there is a hierarchy
```R 
square <- function(x){ return(x^2)}
```

But in Python you don't have to specify with brackets
```Python
def square(x):
    return(x**2)
```

Without indentation things will get very complicated, if they did, Python will throw an error at our faces says: ```IndentationError: expected an indented block```

## Comments
Commenting is very important concept in every programming language, it's because it is important for development process.

When you and your group mates are working on a project, and you are the first part of th project, and you forget to put comments about what are the changes that you put. After some time, you will hear a lot of complaints about you and your lazy head...

It is also beneficial for yourself. After a while, when you look at one of your codes you could understand everything or nothing. It all depends usign comments.

```Python 
# This is a line comment 
# Python will ignore everything in line after '#' sign,

''' 
This is multi line comment, which allows you to 
write comment on multiple lines.

'''
```

## Basic Math using Python
As we all now we have 4 basic math operators which are: '+', '-', '*', '/'; addition, substraction, multiplication, and divison. You can do kinds of calculation using these operators in Python interpreter.

```Python
1 + 10
# 10

7 - 9
# -2

3.0 * 4.0
# 12.0

5 ** 2
# 25

21 / 3
# 7.0  // it is bit different

```
Python version 3.X they implemented division with result of fraction in any case. Because in version 2.X there was a problem when we type 1 / 2. The result was 0. If a developer or scientist was not aware of that and use some fraction resulted division in their experiment or software, it resulted as a disaster.

Python solved this issue with using two different operators '/' for float-point division, and '//' is integer division

```Python
# Python 3.4.2

21 / 3
# 7.0

21 // 3
# 7

21.0 // 7.0
# 3.0

21.0 / 4.0
# 5.25

21.0 // 4.0
# 5.0

1/2
# 0.5

```

We also have modulus operator "%" which gives us the remainder of a division :
```Python
21 % 3
# 0

21.0 % 3.0
# 0.0

21 % 4
# 1

21.0 % 4.0
# 1.0
```
## Numeric Types
### Integers
Integer are same as we know in general math. They can be both positive and negative without any fraction points.

They represented as 3, -54, 1239990, and so on.

In mathematical calculations integer with integer always resulted as integer except in fraction division. It will automatically return as a floating-point number.

---

### Floating-point Numbers
They are also same as decimal point numbers in math. They have to be number.number form.
```Python 
13      # integer
13.0    # float
4/5     # float
```
All calculations of floating point to floating-point will result as floating-point.

### Boolean Types
We are seeing them here inside of the numeric types because their value is 1 and 0. What are they? True and False.

They resulted after comparison statements which we will cover detailed way next week.

Comparison operators are:
* ==  is equal
* >   is smaller than
* <   is greater than
* >=  is smaller or equal
* <=  is greater or equal
* !=  is not equal

```Python 
2 == 2
# True

2 > 3
# False

2 < 3
# True

2 >= 2
# True

2 <= 1
# False

2 != 1
# True
```

### Built-in Functions Using in Numbers

pow(), abs(), round(), int(), float(),

```Python 
pow(2,6) # Returns the first numbers second numbers power
# 64

abs(-27) # Returns the positive of the number
# 27

round(3.45)
# 3

round(3.55)
# 4

# We could round decimal points as well
round(3.333333333, 2) # Adding one more will make it more efficient.
# 3.34

int(3.45)
# 3

float(3)
# 3.0

```
We have other built-in numeric tools inside math modules. For now just know, we can call other modules by importing them...
After importing the module we can use math.pi, math.e, math.sin(), math.sqrt(), math.floor(), math.trunc(), math.ceil()

```Python 
import math # Calling the math library/module

math.pi
# 3.141592653589793

math.e
# 2.718281828459045

math.sin(0)
# 0.0

math.sqrt(4)
# 2.0

math.floor(2.567)
# 2

math.floor(-2.567)
# -3

math.trunc(2.567) # It drops the decimal digits
# 2

math.trunc(-2.567) # It drops the decimal digits
# -2

math.ceil(2.567)
# 3

math.ceil(-2.567)
# -2

```

---

### Random library

```Python
import random # Calling the random library/module

random.random() # it will give us random floats between 0 and 1
# 0.050899111154044

random.randint(1, 10)
# 9

random.choice(list)

random.shuffle(list)
```

## Strings
Strings are very powerful data types, because they have a lot of tools along with them.

### string Literals
Strings are fairly easy to use. Perhaps the most complicated thing about them is that there are som many ways to write them in your code:

* Single quotes: 'spam'
* Double quotes: "spam"
* Triple quotes: '''... spam... ''', """... spam..."""
* There are more but complicated...

Single and double quotes are same

```Python
"knight's"

'knight"s'

title = "Introductory " 'Python' #this called implicit concatenation
```
There are some methods, which will make strings powerful

```Python
s = "This is example string"
len(s) # Returns the length of the variable s
# 22

# Concatenation is another powerful tool

'abc' + 'def'
# abcdef

repeat_string = 'Ni!' * 4 # Concatenate 4 times...
repeat_string
# 'Ni!Ni!Ni!Ni!'

# For example if we want to put 80 dashes to make our code stylis
print('-----------....more....-------------') # The hard way
print('-' * 80) # the easy way. You love Python right?

my_job = 'scientist' # Create string variable called my_job

"k" in my_job # is there any k in the string
# False 

"t" in my_job # is there any t in the string
# True

"tist" in my_job # is there any tist in the string
# True
```
---

### String Indexing and Slicing
Because strings are defined as ordered collections of characters, we can access their components by position. In Python, characters in a string are fetched by indexing-providing the numeric offset of the desired component in square brackets after the string. You get back the one-character string at the specified position.

As in the C language, Python offsets start at 0 and end at one less than the length of the string. Unlike C, however, Python also lets you fetch items from sequences such as strings using negative offsets. Technically, a negative offset is added to the length of a
string to derive a positive offset. You can also think of negative offsets as counting backward from the end.

```Pyhton 
s = 'spam'
s[0] # Show the first character in the string
# 's'
s[-2] # Show the character before the last one in the string
# 'a'

s[1:3] # slicing
# 'pa'
s[1:] # Takes every character before second element with second
# 'pam'
s[:-1]  # Takes every element until the las one s[:3]  same
# 'spa'

s2 = 'endoplasmic reticulum'
s2[1:10:2] # it takes the character from 1 to 9 with skipping items
# 'nolsi'

"hello"[::-1] # easy way to reverse the order...
```
---

### Changing strings 1

Strings are immutable sequence, means that you cannot change a string in place. If you do this:
```Python
S = "spam"
s[0] = "x" 
# TypeError: "str" object does not support item assignment

```
it will yell at you with an error.

But we can make a new one with reassigning 
```Python
s = "spam"
s = s + "SPAM!"
s
# "spamSPAM!"

s = s[:4] + "Burger" + s[-1]
s
# "spamBurger!"

s = s.replace("spam", "chicken") 
s
"chickenBurger!"

```
There are other methods for string. You can look at them by typing ```dir(str)```

### Changing Strings 2

```Python
s = 'spammy'
s = s[:3] + 'xx' + s[5:]
s
# "spaxxy"

s = "spammy"
s = s.replace("mm", "xx")
s
# "spaxxy"

'aa$bb$cc$dd'.replace('$', 'SPAM')
# 'aaSPAMbbSPAMccSPAMdd'

line = "The knights who say Ni!\n"
line.rstrip()
'The knights who say Ni!'

line.upper()
# 'THE KNIGHTS WHO SAY NI!\n'

line.isalpha()
# False

line.endswith('Ni!\n')
# True

line.startswith('The')
# True

```

Thank you for your time, have a great learning!
