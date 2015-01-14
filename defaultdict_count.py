from collections import defaultdict

wordlist = [one_word, two_word, three_word, whateva]

frequencies = defaultdict(int)
for word in wordlist:
    frequencies[word] += 1
return wordlist
