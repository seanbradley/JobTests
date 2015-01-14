# Write a function that returns the sum of its arguments.
def sum(x,y):
   return x + y
   
   
# Write a function that returns the sum of any number of arguments.
def all_arg(*args):
    return sum(args)
    
    
# Write a function that returns the sum of any number of arguments and
# do not use a built-in function like "sum".
def all_args(*args):
    total = 0
    for i in args:
        total += i
    return total
    

# Write a recursive function that returns the sum of any number of arguments.
all_args = lambda x: i + all_args(x) # incorrect; does not terminate


# Write a "recursive" function (i.e., a function that calls itself) that returns 
# the product of any number of arguments.
product_of_all(x):
     x = x * product_of_all(x); 
     return x # incorrect; does not terminate
                 

# Write a function that returns the product of all elements in a list or array.
def product(list):
    x = 1
    for i in list:
        x *= i
    return x
    

# Write a recursive function that returns the product of any number of arguments.
# Second attempt...
def product_x(x):
        return x * product_x(x-1) # incorrect; does not terminate
    

# Write a function that takes any operator function and returns the
# result of that function on all elements of a list or array.
# First attempt...
def any_operater(operator, list):
    i == len(list):
    for i in list and i >= 0:
        x = operator(list.pop(i), list.pop(i-1))
    return x


# Write a function that takes any operator function and returns the
# result of that function on all elements of a list or array.
# Second attempt...
def product(operator, list):
    x = 1 
    for i in list:
        x = operator(x, i)
    return x # semi-correct; presumes x is initialized as 1

