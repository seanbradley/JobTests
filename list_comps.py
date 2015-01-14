#!/usr/bin/env python

'''
TODO:

Calculate a remainder (given a numerator and denominator)
Return distinct values from a list including duplicates (i.e. "1 3 5 3 7 3 1 1 5" -> "1 3 5 7")
Return distinct values and their counts (i.e. the list above becomes "1(3) 3(3) 5(2) 7(1)")
Given a string of expressions (only variables, +, and -) and a set of variable/value pairs (i.e. a=1, b=7, c=3, d=14) return the result of the expression ("a + b+c -d" would be -3)
See also: project euler
'''

y = [1, 4, 32, 16, 27]
m = max(y) # simplest function to find max
print m

n = min(y) # simplest function to find min
print n

p = y.index(m) # tells you what position in the list; index starts at 0
print p

y = [1, 4, 32, 16, 27]
y.sort()
print y

m = y[-1:] # prints last element in list as a list; result keeps brackets
print m

n = y.pop(0) # removes first element in list; result has no brackets
print n

s = sum(y) # list is now [4, 16, 27, 32]
print s

# calc product of all elements in list
def product(list):
    x = 1
    for i in list:
        x *= i
    return x

list = [5, 4, 3]
p = product(list)
print p


import operator
p = reduce(operator.mul, (y[0], y[-1]), 1) # multiply first and last elements of list
print p


a = ["foo", "bar", "baz"]
for i in reversed(a):
    print i


'''
Lists implement the standard sequence interface; len(L) returns the number of items in the list, L[i] returns the item at index i (the first item has index 0), and L[i:j] returns a new list, containing the objects between i and j.

    n = len(L)

    item = L[index]

    seq = L[start:stop]
If you pass in a negative index, Python adds the length of the list to the index. L[-1] can be used to access the last item in a list.

For normal indexing, if the resulting index is outside the list, Python raises an IndexError exception. Slices are treated as boundaries instead, and the result will simply contain all items between the boundaries.

Lists also support slice steps:

    seq = L[start:stop:step]

    seq = L[::2] # get every other item, starting with the first
    seq = L[1::2] # get every other item, starting with the s
'''