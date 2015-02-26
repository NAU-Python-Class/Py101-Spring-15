# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:33:41 2015

@author: Enes Kemal Ergin

List Examples from Beginning Python from novice to Professional
"""

mylist = list("Hello World")
print(mylist)

# Overwriting an element on list.
x = [1,2,3]
x[1]= 7 # Lists are mutable
print(x)

# Deleting Elements
names = ['Alice', 'Beth', "Cecil", "Dee-Dee", "Earl"]
del names[2]
print(names)

# Assigning to Slices
name = list("Perl")
print(name)
name[2:] = list("ar")
print(name)

lst = [1,2,3]
lst.append(4)
print(lst)


print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
x.count(1)

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# It does the same thing as:

a = [1,2,3]
b = [4,5,6]

print(a + b) # concatenate doesnot overwrite the compounds.

print(a)


knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
knights.index('who')

knights.index('herring') # Will throw and error because herring is not in the list

knights[4]

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
numbers


x = [1,2,3]
x.pop()
print(x)

x.append(x.pop()) # Appends the removed one, so it won't change anything.

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)

x.remove('bee') # It will throw and error.

x = [1, 2, 3]
x.reverse()
print(x)

x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
