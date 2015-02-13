Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def square(x):
    return x * x

>>> square(5)
25
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
16
36
144
2388530067169
>>> 
>>> variable_name = "Something"
>>> variable_name
'Something'
>>> enes = "Enes Kemal Ergin"
>>> enes
'Enes Kemal Ergin'
>>> %
SyntaxError: invalid syntax
>>> name
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name%enes
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name%enes
NameError: name 'name' is not defined
>>> name$
SyntaxError: invalid syntax
>>> name$ = "Enes"
SyntaxError: invalid syntax
>>> for = 13
SyntaxError: invalid syntax
>>> is = "string"
SyntaxError: invalid syntax
>>> foris = "Enes"
>>> foris
'Enes'
>>> for_
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for_
NameError: name 'for_' is not defined
>>> for_ = 85
>>> {}
{}
>>> if for_ == 85: {}

{}
>>> def square(x):
return x * x
SyntaxError: expected an indented block
>>> def square(x):
	return x * x

>>> square(2)
4
>>> square(10)
100
>>> square(100)
10000
>>> square(1000)
1000000
>>> # commenting
>>> ###############
>>> ================================ RESTART ================================
>>> 
16
36
144
2388530067169
>>> """ askdjbakdbadmnfbasasdmfnn
,amsndbfmasndfasdmfmansdbf
kasdhfa
"""
' askdjbakdbadmnfbasasdmfnn\n,amsndbfmasndfasdmfmansdbf\nkasdhfa\n'
>>> ================================ RESTART ================================
>>> 
16
36
144
2388530067169
>>> name = "Enes" # This is a line comment
>>> name
'Enes'
>>> 45 + 80
125
>>> 45*80
3600
>>> 45/80
0.5625
>>> 45 ** 80
1807178711742921674070014520448341764861809132965859026291312391149387101824891603102409541083128718952366398298181593418121337890625
>>> 45-80
-35
>>> 45//80
0
>>> 45 %80
45
>>> 45 % 80
45
>>> 80 % 45
35
>>> 81 % 5
1
>>> 80//45
1
>>> 80%45
35
>>> # We have 4 numeric types
>>> 11
11
>>> 456789123
456789123
>>> 
>>> 11.0
11.0
>>> type(11.0)
<class 'float'>
>>> type(1+4j)
<class 'complex'>
>>> type(1+4i)
SyntaxError: invalid syntax
>>> type(4j)
<class 'complex'>
>>> 1+10e
SyntaxError: invalid syntax
>>> 10e - 1
SyntaxError: invalid syntax
>>> 14e-10
1.4e-09
>>> import math
>>> math.e
2.718281828459045
>>> pow(2, 10)
1024
>>> 2 ** 10
1024
>>> abs(-10)
10
>>> 14e-1
1.4
>>> round(10.1)
10
>>> round(10.6)
11
>>> int(14.5)
14
>>> int(14.1)
14
>>> int(14.6)
14
>>> float(85)
85.0
>>> int(1+4e)
SyntaxError: invalid syntax
>>> int(1+4j)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(1+4j)
TypeError: can't convert complex to int
>>> # Boolean
>>> True
True
>>> False
False
>>> import math
>>> math.sin(0)
0.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(math.radians(90))
1.0
>>> math.trunc(1.7)
1
>>> math.trunc(1.2)
1
>>> math.ceil(1.2)
2
>>> math.floor(1.8)
1
>>> math.sqrt(14)
3.7416573867739413
>>> "jherkwqjhef"
'jherkwqjhef'
>>> "456"
'456'
>>> '123', "123"
('123', '123')
>>> 'Tom''s toy'
'Toms toy'
>>> 'Tom's toy'
SyntaxError: invalid syntax
>>> "Tom's toy"
"Tom's toy"
>>> 'Tom\'s Toy'
"Tom's Toy"
>>> 
>>> s1 = "Tom's Toy"
>>> len(s1)
9
>>> s1 = "Water"
>>> s2 = "melon"
>>> s1 + s2
'Watermelon'
>>> s3 = s1 + s2
>>> s3
'Watermelon'
>>> "Ha" * 5
'HaHaHaHaHa'
>>> print("--------------------------------------------------------------------------------------")
--------------------------------------------------------------------------------------
>>> print("-" * 100)
----------------------------------------------------------------------------------------------------
>>> s3
'Watermelon'
>>> s3[0]
'W'
>>> s3[-1]
'n'
>>> len(s3)
10
>>> s3[11]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s3[11]
IndexError: string index out of range
>>> s3[-11]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s3[-11]
IndexError: string index out of range
>>> s3[-4]
'e'
>>> s3[-10]
'W'
>>> s3[10]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    s3[10]
IndexError: string index out of range
>>> s3[0:4]
'Wate'
>>> s3[0:5]
'Water'
>>> s3[5:]
'melon'
>>> s3[-1:]
'n'
>>> s3[-6:]
'rmelon'
>>> s3[:-5]
'Water'
>>> s3[::2]
'Wtreo'
>>> s3[::3]
'Ween'
>>> s3[::-1]
'nolemretaW'
>>> s3[:]
'Watermelon'
>>> s3[::1]
'Watermelon'
>>> s3[2:5:-1]
''
>>> s3[5:2:-1]
'mre'
>>> s3[-2: -5:-1]
'ole'
>>> s3 = s3 + " juice"
>>> s3
'Watermelon juice'
>>> s3= s3.replace("e", "*")
>>> s3
'Wat*rm*lon juic*'
>>> s1 = "istanbul"
>>> s1.capitalize()
'Istanbul'
>>> s3.lower()
'wat*rm*lon juic*'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
