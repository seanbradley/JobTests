import pickle
list_one = ['aa','bb','cc']
peck = pickle.dumps(list_one)
list_two = pickle.loads(peck)
print list_two
