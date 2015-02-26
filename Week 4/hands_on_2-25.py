Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mylist = list("Hello World!")
>>> mylist
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
>>> x = [1,2,3]
>>> x
[1, 2, 3]
>>> y = []
>>> type(y)
<class 'list'>
>>> x[1] = 7
>>> print(x)
[1, 7, 3]
>>> names = ["Enes", "Yunus", "Emre", "Bedir", "Behic", "Amy"]
>>> del name[2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del name[2]
NameError: name 'name' is not defined
>>> del names[2]
>>> print(names)
['Enes', 'Yunus', 'Bedir', 'Behic', 'Amy']
>>> name = list("Perl")
>>> print(name)
['P', 'e', 'r', 'l']
>>> name[2:] list("ar")
SyntaxError: invalid syntax
>>> name[2:] = list("ar")
>>> print(name)
['P', 'e', 'a', 'r']
>>> krypton = ["Krypton", "KR", -157.2, 153, True]
>>> krytopn[0]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    krytopn[0]
NameError: name 'krytopn' is not defined
>>> krypton[0]
'Krypton'
>>> krypton[5]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    krypton[5]
IndexError: list index out of range
>>> krypton[2]
-157.2
>>> 
>>> len(krypton)
5
>>> half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
>>> max(half_lives)
373300.0
>>> max(krypton)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    max(krypton)
TypeError: unorderable types: float() > str()
>>> min(half_lives)
14
>>> sum(ha)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(ha)
NameError: name 'ha' is not defined
>>> sum(half_lives)
404864.7
>>> sorted(half_lives)
[14, 887.7, 6563.0, 24100.0, 373300.0]
>>> lst = [1,2,3]
>>> lst.append(4)
>>> lst
[1, 2, 3, 4]
>>> print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
2
>>> count_to = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
>>> print(count_to)
2
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a.extend(b)
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> print(a+b)
[1, 2, 3, 4, 5, 6]
>>> a.append(b)
>>> print(a.append(b))
None
>>> a = a.append(b)
>>> a
>>> print([a])
[None]
>>> knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
>>> knights.index("who")
4
>>> knigths.index("me")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    knigths.index("me")
NameError: name 'knigths' is not defined
>>> knights.index("me")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    knights.index("me")
ValueError: 'me' is not in list
>>> sorted(knigths)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    sorted(knigths)
NameError: name 'knigths' is not defined
>>> sorted(knights)
['We', 'are', 'knights', 'ni', 'say', 'the', 'who']
>>> 
