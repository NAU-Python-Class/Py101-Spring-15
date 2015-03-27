# Python 101 03/26/15

# Subject Dictionaries...

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

print stuff['height']

stuff['city'] = "San Francisco"

del stuff['city']

# Creating 5 element dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = { }
cities = dict()
# adding more elements
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


state = states.get('Texas')
print state

if not state:
    print "Sorry, no Texas."

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

print histogram("alibaba")



def print_hist(h):
	for c in h:
		print c, h[c]

h = histogram('parrot')
print_hist(h)


t = 'a', 'b', 'c', 'd', 'e'
print type(t)
print t
t = ('a', 'b', 'c', 'd', 'e')

t = tuple("alibaba")
print t

l = list("alibaba")

print t[0]

a = 1
b = 3

temp = a
a = b
b = temp

a,b = b,a 


def min_max(t):
	return min(t), max(t)

t = (1,2,3,4,5,6,7,8,9,0)
print min_max(t)


















