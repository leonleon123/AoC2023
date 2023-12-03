from math import prod
from re import finditer, match

d = open('03.txt').read().split('\n')
n = [[*finditer('([0-9]+)', x)] for x in d]
neighbour_indices = lambda i, j: [(k,l) for k in range(i-1,i+2) for l in range(j-1,j+2) if k>=0 and l>=0 and k<len(d) and l<len(d[k]) and not (k==i and l==j)]
neighbours_valid = lambda i, s, e: not all(not any(not match('[0-9\.]', d[k][l]) for k,l in neighbour_indices(i,j)) for j in range(s, e))
neighbour_numbers = lambda i, j: [int(m[0]) for k in range(i-1,i+2) for m in n[k] if k>=0 and k<len(n) and set((k,l) for l in range(m.start(),m.end())) & set(neighbour_indices(i,j))]
print(sum(int(m[0]) for i, numbers in enumerate(n) for m in numbers if neighbours_valid(i, m.start(), m.end())))
print(sum(prod(x) for x in [neighbour_numbers(i, j) for i, x in enumerate(d) for j, y in enumerate(x) if y == '*'] if len(x) == 2))
