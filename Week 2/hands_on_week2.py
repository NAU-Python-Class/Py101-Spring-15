Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Python 101
>>> 100
100
>>> enes = 100
>>> enes
100
>>> enes = 80
>>> enes
80
>>> Python_class = enes
>>> Python_class
80
>>> # right hand side is always the source for copying.
>>> print(enes)
80
>>> print(Python_class)
80
>>> Python_class == enes
True
>>> Python_class != enes
False
>>> # We cannot use @,#,$,%,^
>>> nam$e
SyntaxError: invalid syntax
>>> name^enes
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name^enes
NameError: name 'name' is not defined
>>> # It understand name and enes as a variable name and look for a value
>>> name%enes
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name%enes
NameError: name 'name' is not defined
>>> name = 100
>>> name%enes
20
>>> # We are trying to make a variable not math...
>>> # We cannot use reserved words.
>>> this = 100
>>> this
100
>>> is = 100
SyntaxError: invalid syntax
>>> # this is not reserved so, it wont cause any error
>>> # But is caused trouble for us..
>>> for = 100
SyntaxError: invalid syntax
>>> for_this_is = 100
>>> 
>>> # Indentation is very crucial
>>> if enes == 80:
	# Do something
	pass

>>> if enes == 80:
print(True)
SyntaxError: expected an indented block
>>> # For most of the syntax we use indentation
>>> # IT is line comment
>>> '''
aasdsdkjgl hasgh
skdfjh las
sadfkh sad
askludfh
asdfuhl;sa
'''
'\naasdsdkjgl hasgh\nskdfjh las\nsadfkh sad\naskludfh\nasdfuhl;sa\n'
>>> 10+10
20
>>> 205+12
217
>>> 154-54
100
>>> 1854-47
1807
>>> 12*8
96
>>> 95
95
>>> 95*8
760
>>> 10+54*87-54
4654
>>> (10+54)*(87-54)
2112
>>> 12/4
3.0
>>> 1/2 # version 2.X
0.5
>>> # It is not 0.5
>>> # it is 0
>>> 1.0/2.0
0.5
>>> 1//2
0
>>> 1.0/2.0
0.5
>>> 1.0//2.0
0.0
>>> # Floating point division /
>>> # Integer division //
>>> 21/3
7.0
>>> 45/9
5.0
>>> 45/8
5.625
>>> 45//8
5
>>> 45.0//8.0
5.0
>>> 
>>> 21%3
0
>>> 21 % 5
1
>>> 234 %5
4
>>> (234 // 5) + (234 % 5)
50
>>> 21.0 % 3.0
0.0
>>> print("=" * 45)
=============================================
>>> # Numeric Types
>>> type() # Which shows the type of an input
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    type() # Which shows the type of an input
TypeError: type() takes 1 or 3 arguments
>>> type(3)
<class 'int'>
>>> type(-10)
<class 'int'>
>>> type(10000000000000000000)
<class 'int'>
>>> type(0)
<class 'int'>
>>> 1/2
0.5
>>> type(1/2)
<class 'float'>
>>> import math
>>> type(math.pi)
<class 'float'>
>>> type(1.90123)
<class 'float'>
>>> type(-10000000.90123)
<class 'float'>
>>> type(math.e)
<class 'float'>
>>> # Every calculation includes at least 1 float makes the result float
>>>  (1+ 2.0) * 56 / (15-4)
 
SyntaxError: unexpected indent
>>> (1+ 2.0) * 56 / (15-4)
15.272727272727273
>>> # Every calculation includes at least 1 float makes the result float
>>> (1+ 2.0) * 56 // (15-4)
15.0
>>> # We have only one float
>>> True
True
>>> False
False
>>> 
>>> # ==, >, <, !=
>>> 2 == 2
True
>>> 5 != 5
False
>>> # Built-in functions
>>> pow(3,2) # 3^2
9
>>> abs(-10)
10
>>> round(3.55)
4
>>> round(3.45)
3
>>> int(3.56)
3
>>> int(3.12)
3
>>> # Int function drops the fraction to make it integer.
>>> float(3)
3.0
>>> float(1230)
1230.0
>>> import math
>>> math.sin(0)
0.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90)
0.8939966636005579
>>> # Because of weird rounding in floating-operations
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sqrt(16)
4.0
>>> math.sqrt(12)
3.4641016151377544
>>> math.floor(2.567)
2
>>> math.floor(-2.567)
-3
>>> math.trunc(2.567)
2
>>> math.trunc(-2.567)
-2
>>> # trunc ust drops the decimal digits
>>> 
>>> 
>>> 
>>> 
>>> 
>>> String
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    String
NameError: name 'String' is not defined
>>> # String
>>> 'Enes Kemal'
'Enes Kemal'
>>> "Enes Kemal "
'Enes Kemal '
>>> """ askjdhas
asdldjhf
akkdfhj
kajddhf """
' askjdhas\nasdldjhf\nakkdfhj\nkajddhf '
>>> "Tom's toy"
"Tom's toy"
>>> 'Tom"s toy'
'Tom"s toy'
>>> "Tom's toy"
"Tom's toy"
>>> s = "NAU Python Class"
>>> len(s)
16
>>> "water" + "melon"
'watermelon'
>>> "Ha" * 5
'HaHaHaHaHa'
>>> print("----------------------------------------------------------------------------------")
----------------------------------------------------------------------------------
>>> print("-" * 100)
----------------------------------------------------------------------------------------------------
>>> my_hobby = "hacking"
>>> h in my_hobby
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    h in my_hobby
NameError: name 'h' is not defined
>>> "h" in my_hobby
True
>>> "z" in my_hobby
False
>>> "king" in my_hobby
True
>>> # indexing
>>> s = "NAU Python Clas"
>>> s = "NAU Python Class"
>>> s[0]
'N'
>>> s[-1]
's'
>>> s[3]
' '
>>> # Slicing
>>> # you can extract words
>>> s[:3]
'NAU'
>>> # : colon is from-to operator
>>> # if we have one more it will be skipping
>>> s[1:10: 2]
'A yhn'
>>> s[1:10:1]
'AU Python'
>>> s[1:10:-1]
''
>>> s[:-1]
'NAU Python Clas'
>>> s[::-1]
'ssalC nohtyP UAN'
>>> 
>>> # Strings are immutable
>>> s = s + " Spring 15"
>>> print(s)
NAU Python Class Spring 15
>>> # We kind changed it
>>> s[:4] + "Burger" + s[-1]
'NAU Burger5'
>>> s = s.replace("5", "#1")
>>> print(s)
NAU Python Class Spring 1#1
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
