from collections import defaultdict

s = {'a': 1, 'c': {'d': {'e': 4}}, 'b': {'a': 2, 'b': 3}
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print d.items()