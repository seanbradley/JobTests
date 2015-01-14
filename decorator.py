#this decorator adds one to the result of the function which it decorates
def decorator(random_func):
    def add_one(*args):
        func = random_func()
        func + 1
    return add_one


@decorator
def sum(x, y):
    x + y

s = sum(1,2)
print s


s = decorator(sum1,2)
print s

