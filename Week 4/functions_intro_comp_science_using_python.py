# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 03:32:00 2015

@author: Enes Kemal Ergin

Functions from Introduction to Computer Science Using Python
"""

def average(n1,n2,n3):
    return (n1+n2+n3)/ 3.0

# Tests
average(40,10,25)
average(10,25,40)
average(40,25,10)

def addup(first, last):
    if first > last:
        sum = -1
    else:
        sum = 0
        for i in range(first, last + 1):
            sum = sum + 1
    return sum

# Tests
addup(1,10)
addup(first = 1, last = 10)
addup(last = 10, first = 1)


def addup2(first, last, incr = 1):
    if first > last:
        sum = -1
    else:
        sum = 0
        for i in range(first, last + 1, incr):
            sum = sum + 1
    return sum

# Tests
addup(1,10)
addup(1,10,2)
addup(first = 1, last = 10)
addup(incr = 2, first = 1, last = 10)
