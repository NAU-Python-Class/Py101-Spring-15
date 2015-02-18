# Programming Concepts - Week 3 

> This file is all about practice. Writing all practices by yourself will improve your understanding in Python. Also I will put here more detailed, and somehow advanced examples, so you can challenge yourself practicing on them.

---

## Boolean Operators
There are only three basic Boolean operators: and, or, and not. not operator has the highes precedence, followed by and, followed by or.
not operator works as a negation
```Python
not True
# False

not False
# True
```

It is like logic, all about 1s, and 0s. Trues, Falses.

- and operator

```Python
True and True
# True

False and False
# False

True and False
# False

False and True
# False

```

- or operator

```Python
True or True
# True

False or False 
# False

True or False
# True

False or True
# True
```


Following concept is very deep and if you want to deal with machines for future also important. 

### Building and Exclusive Or Expression
If you want an exclusive or, you need to build a Boolean expression for it. We'll walk through the development of this expression.

Let's say you have two Boolean variables, b1 and b2, and you want an expression that evaluates to True if and only if exactly one of them is True. Evaluation of b1 and not b2 will produce True if b1 is True and b2 is False. Similarly, evaluation of b2 and not b1 will produce True if b2 is True and b1 is False.

It isn't possible for both of these expressions to produce True. Also, if b1 and b2 are both True or both False, both expressions will evaluate to False. We can, therefore, combine the two expressions with an or:

```Python
b1 = False
b2 = False
(b1 and not b2) or (b2 and not b1)
# False

b1 = False
b2 = True
(b1 and not b2) or (b2 and not b1)
# True

b1 = True
b2 = False
(b1 and not b2) or (b2 and not b1)
# True

b1 = True
b2 = True
(b1 and not b2) or (b2 and not b1)
# False
```
---

But usually we don't use boolean operators and boolean expressions as it is. We use them to represent our daily problems solutions.

```Python
cold = True
windy = False
(not cold) and windy
# False

not(cold and windy)
# True
```

## Comparison Operators
Typically, we don't use boolean operators and boolean expressions as it is. Comparison operators and ther usage will result boolean results.
```Python
>       # Greater than
<       # Less than
>=      # Greater than or equal to
<=      # Less than or equal to
==      # Equal to
!=      # Not equal to
```

All relational operators are binary operators: they compare two values and produce True or False as appropriate.

```Python 
45 > 34
# True

45 > 79
# False

45 < 79
# True

45 < 34
# False
```
We can compare integers to floating-point numbers with any of the relational operators. Integers are automatically converted to floating point when we do this,

```Python
23.1 >= 23
# True

23.1 <= 23
# False
```

The same holds for "equal to" and "not equal to":
```Python 
67.3 == 87
# False

67.3 == 67
# False

67.0 == 67
# True

67.2 != 67
# True
```

### Combining Comparisons
There are some rule when we combine them.
* Arithmetic operators have higher precedence than relational operators. For example, + and / are evaluated before < or >.
* Relational operators have higher precedence than Boolean operators. For example, comparisons are evaluated before and, or, and not.
* All relational operators have the same precedence.

```Python 
x = 5
y = 10
z = 20

(x < y) and (y < z)
# True

x = 3
(1 < x) and (x <= 5)
# True

x = 7
(1 < x) and (x <= 5)
# False
```
We can also chain the comparisons:

```Python 
x = 3
1 < x <= 5
# True

3 < 5 != True
# True

3 < 5 != False
# True
```
---

### Comparing Strings
It's possible to compare strings just as you would compare numbers. The characters in strings are represented by integers: a capital A, for example, is represented by 65, while a space is 32, and a lowercase z is 172. This encoding is called ASCII, which stands for "American Standard Code for Information Interchange."

> One of its quirks is that all the uppercase letters
come before all the lowercase letters, so a capital Z is less than a small a.

One of the most common reasons to compare two strings is to decide which one comes first alphabetically. It may be very useful for some problems that you will face during this class...

```Python
'A' < 'a'
# True

'A' > 'z'
# False

'abc' < 'abd'
# True

'abc' < 'abcd'
# True
```

---

## Chosing which statements to Execute
An if statement lets you change how your program behaves based on a condition. The general form of an if statement is as follows:

> if <<condition>>:
     <<block>>

The condition is an expression, such as color != "neon green" or x < y, as we seen before.

* if must be indented!

__Remainder:__ Python uses four spaces to indent.

If the condition is true, the statements in the block are executed; otherwise, they are not. As with functions, the block of statements must be indented to show that it belongs to the if statement. If you don't indent properly, Python might raise an error, or worse, might happily execute the code that you wrote but do something you didn't intend because some statements were not indented properly. We'll briefly explore both problems in this chapter.

Here is a table of solution categories based on pH level:

* 0-4         Strong Acid
* 5-6         Weak Acid
* 7           Neutral
* 8-9         Weak Base
* 10-14       Strong Base

> Before we start to exercise on if-else statements there is one important built-in function to mentioned

---

### Asking input from a user
input() function takes an input from the user. you can use this function in various ways.

```Python
input("Give me a string:")
string
# 'string'
```

input() function does not automatically return to an integer
```Python
input("Give me an integer: ")
1
# '1'
```
As you can see it retured to '1' which is also string. To make the result integer or float we need to use one more function either eval(input()) or int(input()), float(input())
```Python
eval(input("What is the temperature outside in celcius: "))
25
# 25

# To check if it is integer or string...
type(eval(input()))
25
# <class 'int'>

int(input("What is the temperature outside in celcius: "))
25
# 25

## For floats eval() also work or float()
eval(input("What is the temperature outside in fahrenheit: "))
75.2
# 75.2

float(input("What is the temperature outside in fahrenheit: "))
75.2
# 75.2
```

--- 
Now we can come back to our main topic...


We can use an if statement to print a message only when the pH level given by the program's user is acidic:

```Python
ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
if ph < 7.0:
    print(ph, "is acidic.")

# 6.0 is acidic
```

```Python
ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
if ph < 7.0:
    print(ph, "is acidic".)
  
print("You should be careful with that!")
# You should be careful with that!
```

```Python 
ph = float(input('Enter the pH level: '))
Enter the pH level: 8.5
if ph < 7.0:
    print(ph, "is acidic.")
if ph > 7.0:
    print(ph, "is basic.")

# 8.5 is basic
```
---

### Two way selection
Instead of using conditional statements like that we use if-else way. We need to merge the two cases in the example above and make them if- else

```Python
ph = float(input('Enter the pH level: '))
Enter the pH level: 8.5
if ph < 7.0:
    print(ph, "is acidic.")
else:
    print(ph, "is basic.")
    
# 8.5 is basic
```
As you can see example above, we don't have to put a condition in else brach, because it automatically takes all case left from the if brach. 

But there is something missing, we know from chemistry that 7.0 is neutral but in our case, let's see what will print out if we put 7.0
```Pyhthon
ph = float(input('Enter the pH level: '))
Enter the pH level: 7.0
if ph < 7.0:
    print(ph, "is acidic.")
else:
    print(ph, "is basic.")
    
# 7.0 is basic
```
Okay! this is definetly wrong.

### Multi-way selection
We can increase the number of branches by using elif statements.
```Python
ph = float(input('Enter the pH level: '))
Enter the pH level: 7.0
if ph < 7.0:
    print(ph, "is acidic.")
elif ph == 7.0:
    print(ph, "is neutral.")
else:
    print(ph, "is basic.")

# 7.0 is neutral
```
Know we got the wanted result. let's work on something interesting like compound finding...
```Python
compound = input('Enter the compound: ')
Enter the compound: H2SO4
if compound == "H20":
    print("Water")
elif compound == "NH3":
    print("Ammonia")
elif compound == "CH4":
    print("Methane")
elif compound == "H2SO4":
    print("Sulfuric Acid")
else:
    print("Unknown-Compound")

# Sulfuric Acid
```
---

### Nested If statements
An if statement's block can contain any type of Python statement, which implies that it can include other if statements. An if statement inside another is called a nested if statement.

```Python
value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0: 
        print(ph, "is acidic.")
    elif ph > 7.0:
        print(ph, "is basic.")
    else:
        print(ph, "is neutral.")
else:
    print("No pH value was given!")
```
In the case above, we ask the user to provide a pH value, which we'll initially receive as __a string.__ The first, or outer, _if_ statement checks whether the user typed something, which determines whether we examine the value of _pH_ with the __inner__ _if_ statement. (If the user didn't enter a number, then function call _float(value)_ will produce a _ValueError._)

--- 

## Executing Statements Repeatedly

### While Statement
Python's while statement is the most general iteration construct in the language. In simple terms, it repeatedly executes a block of (normally indented) statements as long as a test at the top keeps evaluating to a true value. It is called a "loop" because control keeps looping back to the start of the statement until the test becomes false. When the test becomes false, control passes to to another statement which follows the while loop.

>   while test: # Loop test
        statements # Loop body
    else: # Optional else
        statements # Run if didn't exit loop with break
We don't usually use else for while loop, but I would like to put it the definition to make everything clear about while.

Let's write a little program to count number from value x to y...
```Python
x = 0
y = 10
while x < y : # it does not count y, <= counts y
    print(a, end = " ")
    a = a + 1
```
end argument in print function just adds them in one line, other wise they will be printed in different line each time.

This is an example of an infinite loop, it goes to infinity unless you interrupt. Ctrl-C key combination to forcibly terminate one
```Python
while True:
    print("Ctrl-C to stop infinite loop!")
# This example will looping until you stop the loop with ctrl-c
```
---
There are some statements which have purpose in only loop structure.

#### break 
It jumps out of the closes enclosing loop(it passes the entire loop statement). The break statement causes an immediate exit from a loop. Because the code that follows it in the loop is not executed if the break is reached, you can also sometimes avoid nesting by including a break.

This piece of code actually count up to 10 with using infinite loop and break statement
```Python
count = 1
while True:
    print(count)
    count = count + 1
    if count == 10: 
        break
```
This one is keep asking name and age until we put stop to name
```Python
while True:
    name = input('Enter name:') 
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)
```

---

#### continue
The continue statement causes an immediate jump to the top of a loop.

This example uses continue to skip odd numbers. This code prints all even numbers less than 10 and greater than or equal to 0.
```Python
x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue ## If number is odd skip printing.
    print(x, end = " ")
```
---

#### pass
the pass statement is a no-operation placeholder that is used when the syntax requires a statement, but you have nothing useful to say. It is often used to code an empty body for a compound statement.

```Python 
while True:
    pass      ## It does nothing but it also keep program inside the loop
              ## To interrupt remember Ctrl-C
```
---

#### loop else
When combined with the loop else clause, the break statement can often eliminate the need for the search status flags

For instance, the following piece of code determines whether a positive integer y is prime by searching for factors greater than 1:
```Python
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x = x - 1
else:
    print(y , 'is prime')
```
Because the loop else clause is unique to Python, it tends to perplex some newcomers In general terms, the loop else simply provides explicit syntax for a common coding scenario-it is a coding structure that lets us catch the "other" way out of a loop, without setting and checking flags or conditions.

---

### for loops
The for loop is a generic iterator in Python: it can step through the items in any ordered sequence or other iterable object.

>   for target in object:         # Assign object items to target
        statements                # Repeated loop body: use target
    else:                         # Optional else part
        statements                # If we didn't hit a 'break'
        
Note that for loop has great usage in lists but since we did not mentioned list yet, we will work on list iteration later on when we see lists.

```Python
s = "lumberjack"
for i in S:
    print(i, end = " ")     # Iteration over a string.
# l u m b e r j a c k
```
i represents just a name of a variable, which will be assigned objects each iteration. You can name it x, y, z, k ...

Don't worry, if you did not understand the concept totally, because for now we did not cover everything about iteration. To finish it completely we need to finish other built-in data types as well. Study the exercises well you will get used to python's syntax.

Thank you for your time, have a great learning!
