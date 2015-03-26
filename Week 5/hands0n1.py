""" 03/25/15 Python 101 """
# Subject :
# 	Dictionaries
# 	Tuples
# Going advance on them 

dic = dict()

print(dic)
print(type(dic))

# This is how you can add key-value pairs
dic['one'] = 'uno'
print(dic)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

# This is how you indexing with dictionaries
print(eng2sp['one']) 

print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)


def histogram(s):
	d = dict() # or d = {}
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1 # d = d + 1 
	return d

string = "Watermelon"
h = histogram(string)
print(h)

def print_hist(h):
	for c in h:
		print c, h[c]
print_hist(h)


""" Tuples """

t = 'a', 'b', 'c', 'd', 'e'
print(t)
print(type(t))

t1 = ("a", "b", "c", "d", "e")
print(t)


t2  = tuple("String")
print(t2)

print(t2[0])

# Tuples are not mutable
#t2[0] = 'A' 

t2 = ("A",) + t2[1:]
print(t2)

a = 1
b = 2
temp = a
a = b
b = temp 

a, b = b, a 
print a, b



