from re import findall
from math import prod

d = open('06.txt').read().split('\n')
r, (t, dst) = [*zip(*[[int(y) for y in findall('\d+', x)] for x in d if x])], [int(''.join(findall('\d+', x))) for x in d]
print(prod(sum((t-tt)*tt > dst for tt in range(t)) for t,dst in r), sum((t-tt)*tt > dst for tt in range(t)), sep='\n')