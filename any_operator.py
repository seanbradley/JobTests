from operator import add, sub, div, mul

def any_operator(passed_init_val, passed_operator, passed_list):
    for iterator in passed_operator:
        passed_init_val = passed_operator(passed_init_val, iterator)
    passed_init_val = final_return_val
    return final_return_val
    
def execute_operation(x, user_operator, user_list):
    
    if user_operator == "+":
        print "Your operator is a plus sign."
        
        while list != []:
            a = user_list.pop(int(len(user_list)),
            b = user_list.pop(int(len(user_list)),
            x = x + add(a, b)
            
        #find a way to return x
            
    elif user_operator == "-":
        print "Your operator is a minus sign."
        for i in user_list:
            while i <= len(user_list):
                x = sub(x, i)
                i = i+1
            return x
        print(x)
            
    elif user_operator == "/":
        print "Your operator is a division sign."
        for i in user_list:
            while i <= len(user_list):
                x = div(x, i)
                i = i+1
            return x
        print(x)
            
    elif user_operator == "*":
        print "Your operator is a multiplication sign."
        for i in user_list:
            while i <= len(user_list):
                x = mul(x, i)
                i = i+1
            return x
            
            
    else:
        print "Your operator is a function."
        any_operator(initialized_x, user_operator, user_list)
    
print """Please enter an ordered list of integers 
separated by commas. You may enter any integers, like so...
1, 2, 3, 4, 5"""
print "\n"
prompt = ">"
user_list = raw_input(prompt).split(",")
user_list = [int(x) for x in user_list]
x = user_list.pop(0)  #initialized x
print "\n"
print """Please enter the operator you want to use. 
You may enter +, -, *, / ...whatever function
you desire, like my_operator(list)."""
print "\n"
prompt = ">"
user_operator = str(raw_input(prompt))
print "\n"
print x
print user_operator
user_list.insert(0, x) #re-insert x back into user's list
print user_list
execute_operation(x, user_operator, user_list)



