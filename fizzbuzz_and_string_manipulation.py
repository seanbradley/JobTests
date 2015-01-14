
prompt = "Please provide the highest integer to which you'd like to calculate fizzbuzz: "

highest_int = int(raw_input(prompt))

for i in range(1, highest_int+1):
    if i % 15 == 0:
        print ("fizzbuzz")
    elif i % 3 == 0:
        print ("fizz")
    elif i % 5 == 0:
        print ("buzz")
    else:
        print (i)


#next problems...in order of increasing difficulty:

#Reverse a string
s = 'Sean Bradley'
s = s[::-1]
print s

#Reverse a sentence ("bob likes dogs" -> "dogs likes bob")
sentence = "The quick brown fox jumped over the lazy dog."
words = sentence.split()
sentence_rev = " ".join(reversed(words)) #include space between quotes
print sentence_rev
