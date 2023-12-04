from re import findall, split
from math import floor

d, c = [len(set.intersection(*[set(split('\s+', y)) for y in findall(':\s+(.*?)\s+\|\s+(.*)', x)[0]])) for x in open('04.txt').read().split('\n') if x], {}
for i, w in enumerate(d):
    for j in range(w): c[i+j+1] = c.get(i+j+1, 1) + c.get(i, 1)

print(sum(floor(2 ** (w - 1)) for w in d), sum(c.get(i, 1) for i in range(len(d))), sep='\n')
