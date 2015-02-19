Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> True
True
>>> False
False
>>> if something == 0:
	print(" ")

	
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    if something == 0:
NameError: name 'something' is not defined
>>> something = 10
>>> if something == 0:
	print(" ")

	
>>> False or True
True
>>> 78 < 90
True
>>> 78 > 90
False
>>> "NAU" == "nau"
False
>>> "NAU" != "nau"
True
>>> not True
False
>>> not False
True
>>> "NAU" > "nau"
False
>>> int("n")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int("n")
ValueError: invalid literal for int() with base 10: 'n'
>>> 67.0 == 67
True
>>> 67.2 == 67
False
>>> ord("N")
78
>>> ord("n")
110
>>> # if-elif-else
>>> x = 10
>>> if x > 1:
	print("Bigger than 1")

	
Bigger than 1
>>> if x > 11:
	print("Bigger than 11")
else:
	print("Smaller than 11")

	
Smaller than 11
>>>  x = -1
 
SyntaxError: unexpected indent
>>> x = -1
>>> if x > 0:
	print("Positive number")
elif:
	
SyntaxError: invalid syntax
>>> if x > 0:
	print("Positive number")
elif x == 0:
	print("Zero")
else:
	print("Negative number")

	
Negative number
>>> if x > 0:
	print("Positive number")
elif x < 0:
	print("Negative Number")
else:
	print("Zero")

	
Negative Number
>>> x = 0
>>> if x > 0:
	print("Positive number")
elif x < 0:
	print("Negative Number")
else:
	print("Zero")

	
Zero
>>> x = 1.9
>>> if type(x) == int:
	if x > 0 :
		print("Positive Number:)'
		      
SyntaxError: EOL while scanning string literal
>>> if type(x) == int:
	if x > 0 :
		print("Positive Number:)
		      
SyntaxError: EOL while scanning string literal
>>> if type(x) == int:
	if x > 0 :
		print("Positive Number"):
			
SyntaxError: invalid syntax
>>> if type(x) == int:
	if x > 0 :
		print("Positive Number")
	elif x == 0:
		print("Zero")
	else:
		print("Negative Number")

	
>>> if type(x) == int:
	if x > 0 :
		print("Positive Number")
	elif x == 0:
		print("Zero")
	else:
		print("Negative Number")
else:
	print("Not integer number")

	
Not integer number
>>> x = 0
>>> # increment variable
>>> x = x + 1
>>> x += 1
>>> x
2
>>> x = x - 1
>>> x
1
>>> x -= 1
>>> x = x * 2
>>> x
0
>>> x = 10
>>> x = x *2
>>> x
20
>>> x *= 2
>>> x
40
>>> x /= 2
>>> n = 5
>>> while n > 0:
	print(n)
	n -= 1

	
5
4
3
2
1
>>> n = 10
>>> while True:
	print(n, end = " ")
	n -= 1

	
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 
-5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36 -37 -38 -39 -40 -41 -42 -43 -44 -45 -46 -47 -48 -49 -50 -51 -52 -53 -54 -55 -56 -57 -58 -59 -60 -61 -62 -63 -64 -65 -66 -67 -68 -69 -70 -71 -72 -73 -74 -75 -76 -77 -78 -79 -80 -81 -82 -83 -84 -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95 -96 -97 -98 -99 -100 -101 -102 -103 -104 -105 -106 -107 -108 -109 -110 -111 -112 -113 -114 -115 -116 -117 -118 -119 -120 -121 -122 -123 -124 -125 -126 -127 -128 -129 -130 -131 -132 -133 -134 -135 -136 -137 -138 -139 -140 -141 -142 -143 -144 -145 -146 -147 -148 -149 -150 -151 -152 -153 -154 -155 -156 -157 -158 -159 -160 -161 -162 -163 -164 -165 -166 -167 -168 -169 -170 -171 -172 -173 -174 -175 -176 -177 -178 -179 -180 -181 -182 -183 -184 -185 -186 -187 -188 -189 -190 -191 -192 -193 -194 -195 -196 -197 -198 -199 -200 -201 -202 -203 -204 -205 -206 -207 -208 -209 -210 -211 -212 -213 -214 -215 -216 -217 -218 -219 -220 -221 -222 -223 -224 -225 -226 -227 -228 -229 -230 -231 -232 -233 -234 -235 -236 -237 -238 -239 -240 -241 -242 -243 -244 -245 -246 -247 -248 -249 -250 -251 -252 -253 -254 -255 -256 -257 -258 -259 -260 -261 -262 -263 -264 -265 -266 -267 -268 -269 -270 -271 -272 -273 -274 -275 -276 -277 -278 -279 -280 -281 -282 -283 -284 -285 -286 -287 -288 -289 -290 -291 -292 -293 -294 -295 -296 -297 -298 -299 -300 -301 -302 -303 -304 -305 -306 -307 -308 -309 -310 -311 -312 -313 -314 -315 -316 -317 -318 -319 -320 -321 -322 -323 -324 -325 -326 -327 -328 -329 -330 -331 -332 -333 -334 -335 -336 -337 -338 -339 -340 -341 -342 -343 -344 -345 -346 -347 -348 -349 -350 -351 -352 -353 -354 -355 -356 -357 -358 -359 -360 -361 -362 -363 -364 -365 -366 -367 -368 -369 -370 -371 -372 -373 -374 -375 -376 -377 -378 -379 -380 -381 -382 -383 -384 -385 -386 -387 -388 -389 -390 -391 -392 -393 -394 -395 -396 -397 -398 -399 -400 -401 -402 -403 -404 -405 -406 -407 -408 -409 -410 -411 -412 -413 -414 -415 -416 -417 -418 -419 -420 -421 -422 -423 -424 -425 -426 -427 -428 -429 -430 -431 -432 -433 -434 -435 -436 -437 -438 -439 -440 -441 -442 -443 -444 -445 -446 -447 -448 -449 -450 -451 -452 -453 -454 -455 -456 -457 -458 -459 -460 -461 -462 -463 -464 -465 -466 -467 -468 -469 -470 -471 -472 -473 -474 -475 -476 -477 -478 -479 -480 -481 -482 -483 -484 -485 -486 -487 -488 -489 -490 -491 -492 -493 -494 -495 -496 -497Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    print(n, end = " ")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line == "done"
	
SyntaxError: invalid syntax
>>> while True:
	line = input(">")
	if line == "done":
	print(line)
	
SyntaxError: expected an indented block
>>> 
>>> while True:
	line = input(">")
	if line == "done":
	print(line)
	
SyntaxError: expected an indented block
>>> while True:
	line = input(">")
	if line == "done":
		break
	print(line)

	
> "Enes "
 "Enes "
>123
123
>akfjh
akfjh
>ksudhf
ksudhf
>sadidl
sadidl
>sdfi
sdfi
>done
>>> while True:
	line = input("Write Something: ")
	if line == "done":
		break
	print(line)

	
Write Something: 123
123
Write Something: 134
134
Write Something: 2135
2135
Write Something: 1
12
Write Something: 35sldkjf
35sldkjf
Write Something: sadlgk4
sadlgk4
Write Something: done
>>> import time
>>> n = 1
>>> while True:
	print("Welcome", n, " times.")
	i += 1
	time.sleep(2)

	
Welcome 1  times.
Traceback (most recent call last):
  File "<pyshell#106>", line 3, in <module>
    i += 1
NameError: name 'i' is not defined
>>> while True:
	print("Welcome", n, " times.")
	n += 1
	time.sleep(2)

	
Welcome 1  times.
Welcome 2  times.
Welcome 3  times.
Welcome 4  times.
Welcome 5  times.
Welcome 6  times.
Welcome 7  times.
Welcome 8  times.
Welcome 9  times.
Welcome 10  times.
Welcome 11  times.
Welcome 12  times.
Welcome 13  times.
Welcome 14  times.
Welcome 15  times.
Welcome 16  times.
Welcome 17  times.
Welcome 18  times.
Welcome 19  times.
Welcome 20  times.
Welcome 21  times.
Welcome 22  times.
Welcome 23  times.
Welcome 24  times.
Welcome 25  times.
Welcome 26  times.
Welcome 27  times.
Welcome 28  times.
Welcome 29  times.
Welcome 30  times.
Welcome 31  times.
Welcome 32  times.
Welcome 33  times.
Welcome 34  times.
Welcome 35  times.
Welcome 36  times.
Traceback (most recent call last):
  File "<pyshell#108>", line 4, in <module>
    time.sleep(2)
KeyboardInterrupt
>>> while True:
	line = input("Write Something")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
Write Something 1234
 1234
Write Something123
123
Write Something# aksdjhjkahsdfasdkgj
Write Somethingdone
>>> for i in "Python":
	print(i)

	
P
y
t
h
o
n
>>> for i in range(10):
	print("*")

	
*
*
*
*
*
*
*
*
*
*
>>> for i in range(10):
	for j in range(5):
		print("*")

		
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> i = 1
>>> for i in range(10):
	print(i)
	i += 1

	
0
1
2
3
4
5
6
7
8
9
>>> for a in range(10):
	print(a)

	
0
1
2
3
4
5
6
7
8
9
>>> list_ = [1,2,3,4,5,6]
>>> for i in list_:
	print(i)

	
1
2
3
4
5
6
>>> for i in list_:
	print(i, end = " ")

	
1 2 3 4 5 6 
>>> for i in list_:
	if list_[i] == 1:
		continue
	print(i)

	
1
2
3
4
5
Traceback (most recent call last):
  File "<pyshell#144>", line 2, in <module>
    if list_[i] == 1:
IndexError: list index out of range
>>> for i in list_:
	if i == 1:
		continue
	print(i)

	
2
3
4
5
6
>>> 
