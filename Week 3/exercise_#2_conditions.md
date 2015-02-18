# Exercise #2 ~ Conditional Statements

## Part 1 
Find the correct results for following questions. If no result printed write __blank__. If an error appear just write an __error__.
> You might want to use python interpreter to see things clearly.

1.  
```Python
if 8 > 7:
   print("Yep")
```
2.
```Python
if 6 > 7:
   print("Yep")
else:
   print("Nope")
```
3.
```Python
var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")
```
4.
```Python
temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")
```
5.
```Python
temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")
```
6.
```Python 
money = 2000
if money > 1000:
    print("I am rich!!")
else:
    print("I'm not rich!!")
      print("But I might be later...")
```
---

## Part 2 ~ Assignments

1. Write a piece of Python code that prints out the string 'hello world' if the value of an integer variable, happy, is strictly greater than 2.

2. Create an if statement that checks whether a number of Twinkies (in the variable twinkies) is less than 100 or greater than 500. Your program should print the message "Too few or too many" if the condition is true.

3. Create an if statement that checks whether the amount of money  contained in the variable money is between 100 and 500 or between     1,000 and 5,000.

4. Create an _if_ statement that prints the string "That's too many"
if the variable _ninjas_ contains a number that's less than 50, prints
"It'll be a struggle, but I can take 'em" if it's less than 30, and
prints "I can fight those ninjas!" if it's less than 10.

5. You want an automatic wildlife camera to switch on if the light level is less than 0.01 lux or if the temperature is above freezing, but not if both conditions are true. (You should assume that function ``` turn_camera_on ``` has already been defined.)
Your first attempt to write this is as follows:
```Python
if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        turn_camera_on()
```
A friend says that this is an exclusive or and that you could write it more simply as follows:
```Python
if (light < 0.01) != (temperature > 0.0):
    turn_camera_on()
```
Is your friend right? If so, explain why. If not, give values for light and temperature that will produce different results for the two fragments of code.

6. Variable _x_ refers to a number. Write an expression that evaluates to _True_ if _x_ and its absolute value are equal and evaluates to _False_ otherwise. Assign the resulting value to a variable named _result_.

7. Assume we want to print a strong warning message if a pH value is below 3.0 and otherwise simply report on the acidity. We try this if statement:
```Python
ph = 2
if ph < 7.0:
    print(ph, "is acidic.")
elif ph < 3.0:
    print(ph, "is VERY acidic! Be careful.")
# 2 is acidic
```
This prints the wrong message when a pH of 2 is entered. What is the
problem, and how can you fix it?

