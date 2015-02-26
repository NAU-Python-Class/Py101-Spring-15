# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 04:16:01 2015

@author: Enes Kemal Ergin

Functions by Practical Programming
"""
def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 /9

# Test 
print(convert_to_celcius(80))

# Quadratic equation solver in a*x^2+b*x+c
def quadratic(a,b,c,x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

# Tests
print(quadratic(2,3,4,0.5))
print(quadratic(2,3,4,1.5))
