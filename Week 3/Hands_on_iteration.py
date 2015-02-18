Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # looping with Python
>>> ## While loop
>>> # They are called indefinite loops
>>> x = x + 1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = x + 1
NameError: name 'x' is not defined
>>> x = 1
>>> x +=1
>>> x
2
>>> # We call this an initialization
>>> x += 1 # is same as x = x + 1
>>> x -=1
>>> x-=1
>>> x
1
>>> n = 5
>>> while n >0:
	print(n)
	n -= 1

	
5
4
3
2
1
>>> n = 10
>>> while True: # which makes it always true and always run...
	print(n, end = " ")
	n = n - 1
print("Done!")
SyntaxError: invalid syntax
>>> while True: # which makes it always true and always run...
	print(n, end = " ")
	n = n - 1

	
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36 -37 -38 -39 -40 -41 -42 -43 -44 -45 -46 -47 -48 -49 -50 -51 -52 -53 -54 -55 -56 -57 -58 -59 -60 -61 -62 -63 -64 -65 -66 -67 -68 -69 -70 -71 -72 -73 -74 -75 -76 -77 -78 -79 -80 -81 -82 -83 -84 -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95 -96 -97 -98 -99 -100 -101 -102 -103 -104 -105 -106 -107 -108 -109 -110 -111 -112 -113 -114 -115 -116 -117 -118 -119 -120 -121 -122 -123 -124 -125 -126 -127 -128 -129 -130 -131 -132 -133 -134 -135 -136 -137 -138 -139 -140 -141 -142 -143 -144 -145 -146 -147 -148 -149 -150 -151 -152 -153 -154 -155 -156 -157 -158 -159 -160 -161 -162 -163 -164 -165 -166 -167 -168 -169 -170 -171 -172 -173 -174 -175 -176 -177 -178 -179 -180 -181 -182 -183 -184 -185 -186 -187 -188 -189 -190 -191 -192 -193 -194 -195 -196 -197 -198 -199 -200 -201 -202 -203 -204 -205 -206 -207 -208 -209 -210 -211 -212 -213 -214 -215 -216 -217 -218 -219 -220 -221 -222 -223 -224 -225 -226 -227 -228 -229 -230 -231 -232 -233 -234 -235 -236 -237 -238 -239 -240 -241 -242 -243 -244 -245 -246 -247 -248 -249 -250 -251 -252 -253 -254 -255 -256 -257 -258 -259 -260 -261 -262 -263 -264 -265 -266 -267 -268 -269 -270 -271 -272 -273 -274 -275 -276 -277 -278 -279 -280 -281 -282 -283 -284 -285 -286 -287 -288 -289 -290 -291 -292 -293 -294 -295 -296 -297 -298 -299 -300 -301 -302 -303 -304 -305 -306 -307 -308 -309 -310 -311 -312 -313 -314 -315 -316 -317 -318 -319 -320 -321 -322 -323 -324 -325 -326 -327 -328 -329 -330Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(n, end = " ")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> # Control+C stopts the infinite looping,,,
>>> while True:
	line = input(">")
	if line == "done"
	
SyntaxError: invalid syntax
>>> while True:
	line = input(">")
	if line == "done":
		break
	print(line)

	
>s
s
>s
s
>asd
asd
>asd
asd
>afg
afg
>2 + 2
2 + 2
>done
>>> import time
>>> i = 1
>>> while True:
	print("Welcome", i, " times. To stop press [CTRL+C]")
	i += 1
	time.sleep(2) # It just delays for 2 second

	
Welcome 1  times. To stop press [CTRL+C]
Welcome 2  times. To stop press [CTRL+C]
Welcome 3  times. To stop press [CTRL+C]
Welcome 4  times. To stop press [CTRL+C]
Welcome 5  times. To stop press [CTRL+C]
Traceback (most recent call last):
  File "<pyshell#37>", line 4, in <module>
    time.sleep(2) # It just delays for 2 second
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line[0] == "#":
		continue
	if line == "done":
		break

	
>123
>123
>123
>123
>123
>123
>123
>123
>123
>123
>123
>BEcause I forget to put print() :)
>done
>>> while True:
	line = input(">")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
>123
123
>123
123
>123
123
># Enes Kemal 
>enes kemal
enes kemal
>done
>>> for i in "Python":
	print(i, end = "-")

	
P-y-t-h-o-n-
>>> for i in "Python":
	print(i)

	
P
y
t
h
o
n
>>> 
