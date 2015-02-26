# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:28:35 2015

@author: Enes Kemal Ergin

List Examples from A Byte of Python
"""

shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are: ', end= ' ')

for item in shoplist:
    print(item, end= ' ')
    
print('\n also have to buy rice.')
shoplist.append('rice')
print('My Shopping list is now', shoplist)

print('I want to sort my list')
shoplist.sort()
print('Sorted list: ', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]

del shoplist[0]

print('I bought the', olditem)
print('My shopping list is now', shoplist)