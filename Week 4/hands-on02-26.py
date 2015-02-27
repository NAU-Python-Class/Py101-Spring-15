Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list = list("Hello World")
>>> my_list
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
>>> x = []
>>> x
[]
>>> x [1,2,3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x [1,2,3]
TypeError: list indices must be integers, not tuple
>>> x = [1,2,3]
>>> x
[1, 2, 3]
>>> y = ["enes", 12, 12.0, 1+4j, True]
>>> y
['enes', 12, 12.0, (1+4j), True]
>>> x[1] = "string"
>>> x
[1, 'string', 3]
>>> x = [1,2,3,4,5,6]
>>> del x[2]
>>> x
[1, 2, 4, 5, 6]
>>> name = list("Perl")
>>> name
['P', 'e', 'r', 'l']
>>> name[2:] = list("ar")
>>> print(name)
['P', 'e', 'a', 'r']
>>> print(x)
[1, 2, 4, 5, 6]
>>> x.
SyntaxError: invalid syntax
>>> x.append(3)
>>> x
[1, 2, 4, 5, 6, 3]
>>> x.append(3,2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x.append(3,2)
TypeError: append() takes exactly one argument (2 given)
>>> x = [[1,2],1,1,[2,1,[1,2]]]
>>> x
[[1, 2], 1, 1, [2, 1, [1, 2]]]
>>> x.count(1)
2
>>> lst = [123,23456, 987, 234, 2345678890]
>>> len(lst)
5
>>> max(lst)
2345678890
>>> min(lst)
123
>>> sum(lst)
2345703690
>>> sorted(lst)
[123, 234, 987, 23456, 2345678890]
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> print(a+b)
[1, 2, 3, 4, 5, 6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
>>> ================================ RESTART ================================
>>> 
>>> function_name()
Hello World!
>>> ================================ RESTART ================================
>>> 
>>> function2()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    function2()
TypeError: function2() missing 2 required positional arguments: 'i' and 'j'
>>> function2(1,2)
3
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> average(1,2,3,4)
2.5
>>> ================================ RESTART ================================
>>> 
>>> average([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    average([1,2,3,4])
TypeError: average() missing 3 required positional arguments: 'b', 'c', and 'd'
>>> list_average([1,2,3,4])
2.5
>>> ================================ RESTART ================================
>>> 
>>> convert_to_celcius(75)
23.88888888888889
>>> convert_to_celcius(80)
26.666666666666668
>>> ================================ RESTART ================================
>>> 
>>> quadratic(2,3,4,.5)
6.0
>>> quadratic(2,3,4,1)
9
>>> 
