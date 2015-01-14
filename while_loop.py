# This will print a set like so [4, 6, 8]
# because i is tested before it is incremented
nums = list()
i = 4
while(i < 9):
    nums.append(i)
    i = i+2
print(nums)



# This will print...

# 6
# 8
# 10

# ...because of where the test for i is made (i.e., not in the middle
# of the loop; also, i must be initialized. i will print till 10, because
# the number 8 will pass the test.

i = 0
while(i < 9):
    i = i+2
    print(i)
    

# This will print all numbers, 0 through 8...

littlelist = list()
i = 0
while(i < 9):
    littlelist.append(i) #<--on first pass, i as 0 is inserted into list
    i += 1
print(littlelist)
