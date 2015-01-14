#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Prints results of each function...

Didn't create a proper module here...just code I could copy-paste 
into the .py file sent to me.

This .py file actually prints the solutions...albeit in reverse order: 
question #6 to question #1

Commentary about each solution is in the original .py

In lieu of unittests, you can run this file to see if the guts
of each function in the original .py produce reasonable results.
'''


print "#6) A decorator with an argument..."
from functools import wraps

def minimum_x(x):
    def factory(fn):
        @wraps(fn)
        def decorator(arg):
            if arg >= x:
                print arg 
            else: 
                raise ValueError('test(%d) is smaller than @minimum_x(%d).' % (arg, x)) 
        return decorator
    return factory

@minimum_x(6)
def test(arg):
    print "This function has a decorator (or more) with an arg: ", arg

test(6)
print ("\n")



print "#5) Parse Apache log files..."
import re
from collections import defaultdict

# here's a list of ACL entries, each entry including filename, response code, and size...
filenames = [
'64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/pic.png HTTP/1.1" 401 12846',
'64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523','64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291', 
'64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] "GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1" 200 7352',
'64.242.88.10 - - [07/Mar/2004:16:30:29 -0800] "GET /twiki/bin/attach/Main/OfficeLocations HTTP/1.1" 401 12851', 
'64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] "GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1" 200 5253', 
'64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924'
]

# first, I reduce the above list of ACL entries to a list of tuples called 'reduced_filenames'
# each tuple in the list contains a filename's response code string and related message size integer
responses = []
sizes = []
for filename in filenames:
    resp = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', filename)).pop(-2)
    responses.append(str(resp))
    size = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', filename)).pop(-1)
    sizes.append(int(size))
    reduced_filenames = zip(responses, sizes)

# then, using my list of tuples, I generate a dictionary with unique response codes 
# as the keys, and a list of sizes for each key's value
dictionary = defaultdict(list)
for resp, size in reduced_filenames:
    dictionary[resp].append(size)

# sum the sizes associated with each response code in the dictionary
print {resp: sum(sizes) for resp, sizes in dictionary.iteritems()}
print ("\n")


print "#4) Cubes until zero..."
prompt = "Please provide a modulus: "
modulus = int(raw_input(prompt))

list = []

for i in range(1, modulus+1):
    cube = i*i*i
    # here's where I square i instead of cube it due to example...
    if (i*i) < modulus and (i*i) % cube >= 0:
        list.append(cube)
print list
print ("\n")




print "#3) Find IP addresses..."
inp  = "This is a string with some IP addresses: 127.0.0.1, 192.168.1.1, 72.247.244.88, 0123.123.123.1230"
import re
print re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', inp)
print ("\n")



print "#2) Map integers to their 2.5th root...all integers from 2 up to 100..."
keys = []
vals = []
for key in range(2, 101):
    val = key**2.5
    keys.append(key)
    vals.append(val)
dictionary = dict(zip(keys, vals))
print dictionary
print ("\n")


print "#1) List of integers 23 to 100 evenly divisble by 7..."
for i in range(23, 101):
        if (i % 7) == 0:  
            print i



