# Exercise #2 ~ Iteration
---

### Note for Success:
> If you want to learn the concepts clearly, put comments around your code. Examine my GitHub account the see how comment using makes the difference. Try to examine the exercises above, they are very similar to each other. Please note their differences and see why they differ. This approach will help you to understand the concepts more...

## Part 1 
Find the correct results for following questions. If no result printed write __blank__. If an error appear just write an __error__. If result won't stop evaluating write __infinite__.

1. 
```Python
total = 0
while sum < 5:
    print(sum)
    total = total + 1
```
2.
```Python
sum = 0 
current = 1
n = eval(input())
while current <= n:
    sum = sum + current
    current = current + 1
```
3. 
```Python
sum = 0 
current = 1
n = eval(input())
while current <= n:
    sum = sum + current
    current = current + 1
print(sum)
```
4. 
```Python
sum = 0 
current = 1
n = eval(input())
while current <= n:
    sum = sum + current
    current = current + 1
    print(sum)
```
5.
```Python
while True:
    print("Looooooping....")
```
6. 
```Python
n = 10
sum = 0
current = 1
while current <= n:
    sum = sum + current
    n = n - 1
print(sum)
```
7. 
```Python
n = 10
sum = 0
current = 1
while current <= n:
    sum = sum + current  
print(sum)
```
---

## Part 2

1. Write a code which has the following attributes:

  - Takes two random single digit integer; number1 and number2
  - Ask user to put the answer of subtraction of number1 and number2
  - Use looping concept to repeatedly ask if user puts wrong answer

__Sample output:__
What is 4 - 3? _4_
Wrong answer. Try again. What is 4 - 3? _5_
Wrong answer. Try again. What is 4 - 3? _1_
You got it!

2. Write a Guessing Number code, here are the instructions:

  - Get a random number
  - Ask a guess of a number until user finds the random number: "Enter a guess: "
  - use some hints:
    - If guess is higher then the number: "Your guess is too high!"
    - If guess is lower then the number: "Your guess is too low!"
    - If user find the number: "You have found it!"

---

## Part 3
Find the correct results for following questions. If no result printed write __blank__. If an error appear just write an __error__. If result won't stop evaluating write __infinite__.

1.
```Python
LetterNum = 1
for Letter in "Howdy!":
    if Letter == "w":
        continue
        print("Encountered w, not processed.")
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
```

2. 
```Python
Value = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
    if LetterNum > 6:
        print("The string is too long!")
        break
```

3.
```Python
LetterNum = 1
for Letter in "Howdy!":
    if Letter == "w":
        pass
        print("Encountered w, not processed.")
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
```

4.
```Python
Value = input("Type less than 6 characters: ")
LetterNum = 1

for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum+=1
else:
  print("The string is blank.")
```

5.
```Python
number = 0
sum = 0
for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number
print("sum is", sum)
print("count is", count)
```

6.
```Python
sum = 0
for i in range(1001):
    sum = sum + i
```

7. 
```Python
school = 'North American University'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
```
---

## Part 4

1. Convert the following into code that uses a for loop.

  print 2
  print 4
  print 6
  print 8
  print 10
  print Goodbye!

2. Convert the following into code that uses a for loop.

  print Hello!
  print 10
  print 8
  print 6
  print 4
  print 2

3. Write a multiplication table using for loop, 9x9 (Force your imagination...)
    Output:
      Multiplication Table
    1  2  3  4  5  6  7  8  9
------------------------------
1 | 1  2  3  4  5  6  7  8  9
2 | 2  4  6  8 10 12 14 16 18
3 | 3  6  9 12 15 18 21 24 27
4 | 4  8 12 16 20 24 28 32 36
5 | 5 10 15 20 25 30 35 40 45
6 | 6 12 18 24 30 36 42 48 54
7 | 7 14 21 28 35 42 49 56 63
8 | 8 16 24 32 40 48 56 64 72
9 | 9 18 27 36 45 54 63 72 81