Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Let's remember the booleans
>>> TRUE
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    TRUE
NameError: name 'TRUE' is not defined
>>> True
True
>>> False
False
>>> not True
False
>>> not False
True
>>> # We can also use logic to result complicated relations
>>> True and True # I know it is not that complicated
True
>>> False or True
True
>>> (False or True) and (False and False) or (True and False)
False
>>> # Comparison operations result boolean
>>> 78 < 9
False
>>> 12 > 9
True
>>> 12 >= 12
True
>>> 67.0 == 67
True
>>> 67.3 == 67
False
>>> # We can combine more numbers into logical concepts
>>> (123 != 14) and (14 and 15 == 14)
False
>>> # Those comparisons work in strings as well
>>> "NAU" > "nau"
False
>>> # It uses ASCII table to obtain numbers correlated with character
>>> "z" == "Z"
False
>>> # They are not equal
>>> if "a" == "a":
	print("yes they are equal")

	
yes they are equal
>>> x = 10
>>> if x > 0:
	print("It is positive!")

	
It is positive!
>>> if x <= 0:
	print("It is not positive!")

	
>>> # As you can see nothing printed, because condition was not resulted True
>>> # To avoid these answerless situations we uses default case called else
>>> if x > 0:
	print("It is positive!")
else :
	print("It is not positive!")

	
It is positive!
>>> # Lets change x and see the else working
>>> x = -1
>>> if x > 0:
	print("It is positive!")
else :
	print("It is not positive!")

	
It is not positive!
>>> # We can increase the situations using elif
>>> if x > 0:
	print("It is positive!")
elif x == 0:
	print("It is zero!")
else :
	print("It is not positive!")

	
It is not positive!
>>> x = 0
>>> if x > 0:
	print("It is positive!")
elif x == 0:
	print("It is zero!")
else :
	print("It is not positive!")

	
It is zero!
>>> # You can increase the number of elifs inside the conditionals
>>> number = 2
>>> if type(number) == int:
	if number > 0:
		print("It is a positive integer number!")
	elif number == 0:
		print("It is zero")
	else:
		print("It is a negative integer number!")
else:
	print("This number is not an integer!")

	
It is a positive integer number!
>>> number = 2.0
>>> if type(number) == int:
	if number > 0:
		print("It is a positive integer number!")
	elif number == 0:
		print("It is zero")
	else:
		print("It is a negative integer number!")
else:
	print("This number is not an integer!")

	
This number is not an integer!
>>> 
