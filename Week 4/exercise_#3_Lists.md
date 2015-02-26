# Exercise #3 ~ Lists and List Comprehension

## Part 1
Find the correct results for following questions. If no result printed write __blank__. If an error appear just write an __error__.
> You might want to use python interpreter to see things clearly.

Find corresponding results of following using this variable ```Python x = [1, 2, [3, 'John', 4], 'Hi'] ```

1.  ``` x[0]```
2.  ``` x[2]```
3.  ``` x[-1]```
4.  ``` x[0:1]```
5.  ``` x[2][2]```
6.  ``` 2 in x```
7.  ``` 3 in x```
8.  
```Python 
x[0] = 8
x
```
## Part 2
Find corresponding results of following using this variable ```Python x = [1, 2, [3, 'John', 4], 'Hi'] ```

1.  ```rrange(3)```
2.  ```range(3,10)```
3.  ```range(3,10,3)```
4.  ```range(3,10.5,0.5)```
5.  ```range(10,3)```
6.  ```range(10,3,-1)```
7.  ```range(len(x))```
8.  ```sum(range(len(x)))```

## Part 3 
For this part careful that ever question link to eachother.

1.
```Python
aList = range(1, 6)
bList = aList
aList[2] = 'hello'
aList == bList
```
2. 
```Python
aList is bList
```
3.
```Python
aList
```
4.
```Python
bList
```
5.
```Python
cList = range(6, 1, -1)
dList = []
for num in cList:
      dList.append(num)
cList == dList
```
6.
```Python
cList is dList
```
7.
```Python
cList[2] = 20
cList
```
8.
```Python
dList
```

## Part 4
Use the following list to guide you through this part.
```Python
>>> listA = [1, 4, 3, 0]
>>> listB = ['x', 'z', 't', 'q']
```
1.  ```listA.sort```
2.  ```listA.sort()```
3.  ```listA```
4.  ```listA.insert(0,100)```
5.  ```listA.remove(3)```
6.  ```listA.append(7)```
7.  ```listA```
8.  ```listA + listB```
9.
```Python
listB.sort()
listB.pop()
```
10. ```listB.count("a")```
11. ```listB.remove("a")```
12. ```listA.extend([4,1,6,3,4])```
13. ```listA.count(4)```
14. ```listA.index(1)```
15. ```listA.pop(4)```
16. ```listA.reverse()```
17. ```listA```

