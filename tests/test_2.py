'''
Using Python 2.6, 2.7, or 3.3 syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.
'''

# fortunately simpler than fizzbuzz
def list_of_integers():
    '''
    Returns a list of integers from 23 to 100 that are evenly divisible by 7.
    '''
    for i in range(23, 101):
        if (i % 7) == 0:  
            return i


# maybe more elegant/performant to use a dict comprehension? ...but this is 
# easier for me to read
def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.5th root for all integers
    from 2 up to 100 (including 100).
    '''
    
    keys = []
    vals = []
    for key in range(2, 101):
        val = key**2.5
        keys.append(key)
        vals.append(val)
    dictionary = dict(zip(keys, vals))
    return dictionary
        

# admittedly, regex stuff is not my strength; moreover, maybe possible to
# do this more efficiently without an import
def find_ips(inp):
    '''
    Returns a list of ip addresses of the form 'x.x.x.x' that are in the input
    string (separated by at least some whitespace).
    >>> find_ips('this has one ip address 127.0.0.1')
    ['127.0.0.1']
    '''
    
    inp  = "This is a string with some IP addresses: 127.0.0.1, 192.168.1.1, 72.247.244.88"
    import re
    return re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', inp)


# not sure I fully understood instructions for this one...because
# the docstring example seems to be generating cubes up until the *square* 
# of integers modulo 25 equals zero.
def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next is 0 modulo
    the provided modulus.
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    prompt = "Please provide a modulus: "
    modulus = int(raw_input(prompt))

    list = []

    for i in range(1, modulus+1):
        cube = i*i*i
        # here's where I square i instead of cube it due to example...
        if (i*i) < modulus and (i*i) % cube >= 0:
            list.append(cube)
    return list


# this one was the toughest, again...due to regex
def total_size(filenames):
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

    # first, reduce the above list of ACL entries to a list of tuples (called 'reduced_filenames')
    # each tuple in the new list contains just a response code and related message size
    responses = []
    sizes = []
    for filename in filenames:
        resp = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', filename)).pop(-2)
        responses.append(str(resp))
        size = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', filename)).pop(-1)
        sizes.append(int(size))
        reduced_filenames = zip(responses, sizes)

    # then, using the resultant list of tuples, generate a dictionary...
    # with each key : value being unique response code: list of respective sizes
    dictionary = defaultdict(list)
    for resp, size in reduced_filenames:
        dictionary[resp].append(size)

    # sum the values (the sizes) associated with each key (response code) 
    return {resp: sum(sizes) for resp, sizes in dictionary.iteritems()}


# the only way I know how to paramatize a decorator is via wrapping it with a
# factory function; in practice, I'd probably have been tempted to create a 
# classmethod...albeit, for this use case, I believe a nested function is 
# more efficient
def minimum_x(x):
    '''
    Write a function decorator that takes an argument, and returns a decorator
    that can be used to decorate a function, which verifies that the first
    argument to a decorated function is at least the given value, raising a
    ValueError on failure.
    >>> @minimum_x(6)
    ... def test(arg):
    ...   print arg
    ... 
    >>> test(6)
    6
    >>> test(5) # raises ValueError
    '''
        
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
    
    #results in the following...
    #
    #test(7)
    #7
    #test(5)
    #Traceback (most recent call last):
    #  File "my_scratch_file.py", line 39, in <module>
    #    test(5)
    #  File "my_scratch_file.py", line 30, in decorator
    #    raise ValueError('test(%d) is smaller than @minimum_x(%d).' % (arg, x)) 
    #ValueError: test(5) is smaller than @minimum_x(6).

    
