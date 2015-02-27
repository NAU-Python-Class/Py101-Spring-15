def function_name():
    print("Hello World!")

def function2(i, j):
    return i+j

def average(a,b,c,d):
    return (a+b+c+d)/4

def list_average(list):
    return (sum(list)/len(list))

def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32)*5/9

def covert_to_fahrenheit(celcius):
    return (fahrenheit * 9)/5 + 32

def quadratic(a,b,c,x):
    first = a * x  ** 2
    second = b * x
    third = c
    return first + second + third
