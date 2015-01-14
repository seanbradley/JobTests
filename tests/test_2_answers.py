#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Given a list of filenames in Apache Common Log format, return a mapping
of the total number of responses of different types, and the total size of
all responses of that type. You can find documentation on the format:
http://httpd.apache.org/docs/1.3/logs.html#common
>>> total_size([...])
{'200': 7362899, '404': 28710, ...}
'''
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
    
    
    
    
'''

# returns a set of unique response codes from the list of pairs
reduced_responses = list(set(resp for resp, size in reduced_filenames))
#print reduced_responses

selected_response = list(reduced_responses.pop(1))

for each_pair in reduced_filenames:
    if (selected_response for resp, size in reduced_filenames):
        #tot_size = sum(size)
        print resp
        
    reduce(f, reduced_filenames)
    #if isinstance of a particular response in reduced_responses
        append its size to a list_of_sizes
    
for size in resp, size of reduced_filenames:
    sum(size) if reducedtot_size = lambda  
r = map(append(size of resp, size in , reduced_filenames)

# sums all message sizes for a given response code
i = 0
while i <= len(reduced_filenames) is true:
    response_summed = reduced_responses.pop(i+1))

for pair in reduced_filenames:
    if resp isinstance :
        tot_size_for_response.append(size)
    print sum(tot_size_for_response)
'''
#for t in 
#    if isinstance reduced_types in tagged_tuples:
#        agg_sizes_for_type.append(s)
    
#tot_size_for_types = sum(size for rct., size in tagged_tuples)
#print tot_size_for_types
#code_type = reduced_code_types.pop()
#for code_type in tagged_tuples:
#    print sum(size for code, size in tagged_tuples)
    
#print set(codes)



'''
    keys = []
    vals = []
    for key in range(2, 101):
        val = key**2.5
        keys.append(key)
        vals.append(val)
    dictionary = dict(zip(keys, vals))
    return dictionary
    
    
#buf = StringIO.StringIO(filenames)
#line = buf.readline()    
    
filenames = [
64.242.88.10 - - [07/Mar/2004:16:23:12 -0800] "GET /twiki/bin/oops/TWiki/AppendixFileSystem?template=oopsmore¶m1=1.12¶m2=1.12 HTTP/1.1" 200 11382, 
64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/pic.png HTTP/1.1" 401 12846,
64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523, 64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291, 
64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] "GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1" 200 7352, 
64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] "GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1" 200 5253, 
64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924, 
64.242.88.10 - - [07/Mar/2004:16:29:16 -0800] "GET /twiki/bin/edit/Main/Header_checks?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851, 
64.242.88.10 - - [07/Mar/2004:16:30:29 -0800] "GET /twiki/bin/attach/Main/OfficeLocations HTTP/1.1" 401 12851, 
64.242.88.10 - - [07/Mar/2004:16:31:48 -0800] "GET /twiki/bin/view/TWiki/WebTopicEditTemplate HTTP/1.1" 200 3732, 
64.242.88.10 - - [07/Mar/2004:16:32:50 -0800] "GET /twiki/bin/view/Main/WebChanges HTTP/1.1" 200 40520, 
64.242.88.10 - - [07/Mar/2004:16:33:53 -0800] "GET /twiki/bin/edit/Main/Smtpd_etrn_restrictions?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851,
64.242.88.10 - - [07/Mar/2004:16:35:19 -0800] "GET /mailman/listinfo/business HTTP/1.1" 200 6379,
64.242.88.10 - - [07/Mar/2004:16:36:22 -0800] "GET /twiki/bin/rdiff/Main/WebIndex?rev1=1.2&rev2=1.1 HTTP/1.1" 200 46373,
64.242.88.10 - - [07/Mar/2004:16:37:27 -0800] "GET /twiki/bin/view/TWiki/DontNotify HTTP/1.1" 200 4140,
64.242.88.10 - - [07/Mar/2004:16:39:24 -0800] "GET /twiki/bin/view/Main/TokyoOffice HTTP/1.1" 200 3853,
64.242.88.10 - - [07/Mar/2004:16:43:54 -0800] "GET /twiki/bin/view/Main/MikeMannix HTTP/1.1" 200 3686,
64.242.88.10 - - [07/Mar/2004:16:45:56 -0800] "GET /twiki/bin/attach/Main/PostfixCommands HTTP/1.1" 401 12846
]

for filenames in range[0, len(filenames)+1]:
    filenames.pop[0]


# Non-ASCII character '\xc2' in file scratch.py on line 15, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
    
import re

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')


64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/pic.png HTTP/1.1" 401 12846,
64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523, 64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291, 
64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] "GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1" 200 7352, 
64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] "GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1" 200 5253, 
64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924, 
64.242.88.10 - - [07/Mar/2004:16:29:16 -0800] "GET /twiki/bin/edit/Main/Header_checks?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851, 
64.242.88.10 - - [07/Mar/2004:16:30:29 -0800] "GET /twiki/bin/attach/Main/OfficeLocations HTTP/1.1" 401 12851, 
64.242.88.10 - - [07/Mar/2004:16:31:48 -0800] "GET /twiki/bin/view/TWiki/WebTopicEditTemplate HTTP/1.1" 200 3732, 
64.242.88.10 - - [07/Mar/2004:16:32:50 -0800] "GET /twiki/bin/view/Main/WebChanges HTTP/1.1" 200 40520, 
64.242.88.10 - - [07/Mar/2004:16:33:53 -0800] "GET /twiki/bin/edit/Main/Smtpd_etrn_restrictions?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851,
64.242.88.10 - - [07/Mar/2004:16:35:19 -0800] "GET /mailman/listinfo/business HTTP/1.1" 200 6379,
64.242.88.10 - - [07/Mar/2004:16:36:22 -0800] "GET /twiki/bin/rdiff/Main/WebIndex?rev1=1.2&rev2=1.1 HTTP/1.1" 200 46373,
64.242.88.10 - - [07/Mar/2004:16:37:27 -0800] "GET /twiki/bin/view/TWiki/DontNotify HTTP/1.1" 200 4140,
64.242.88.10 - - [07/Mar/2004:16:39:24 -0800] "GET /twiki/bin/view/Main/TokyoOffice HTTP/1.1" 200 3853,
64.242.88.10 - - [07/Mar/2004:16:43:54 -0800] "GET /twiki/bin/view/Main/MikeMannix HTTP/1.1" 200 3686,
64.242.88.10 - - [07/Mar/2004:16:45:56 -0800] "GET /twiki/bin/attach/Main/PostfixCommands HTTP/1.1" 401 12846

m = pattern.match(filenames)
res = m.groupdict()

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
print re.match(regex, filenames).groups()
'''


'''
keys = []
vals = []
for key in range(2, 101):
    val = key**2.5
    keys.append(key)
    vals.append(val)
dictionary = dict(zip(keys, vals))
return dictionary

#D = {key:val for (key,val) in list}

#for key, val in D.iteritems():
#    print key, val

D = []
for key in range(1, 101):
    #D.append(key)
    val = key**2.5
map(val, key)
#print (D.index(val)+1)
#print key, ":", val
#D = {key: value for (key, value) in sequence}

print D

D = []
for key in range(1, 101):
    #D.append(key)
    val = key**2.5
    D.append(val)
#print (D.index(val)+1)
#print key, ":", val
#D = {key: value for (key, value) in sequence}

#print D

def cube(x): return x*x*x

map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    print memo[n]
    
D = defaultdict(int)
for key in range(1, 101):
    value = key**2.5
    D[key].append(value)
for key, value in D.items():
    print key, ":", val
    
reddit.com 72.247.244.88
imgur.com 173.231.140.219
google.com 74.125.157.99
youtube.com 74.125.65.91
yahoo.com 98.137.149.56
hotmail.com 65.55.72.135
bing.com 65.55.175.254
digg.com 64.191.203.30
theonion.com 97.107.137.164
hush.com 65.39.178.43
gamespot.com 216.239.113.172
ign.com 69.10.25.46
cracked.com 98.124.248.77
sidereel.com 144.198.29.112
github.com 207.97.227.239


'''
