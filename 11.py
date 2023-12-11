from itertools import combinations
import numpy as np

d = np.array([[['.','#'].index(y) for y in x] for x in open('11.txt').read().split('\n')])
r, c = np.sum(d, axis=1) == 0, np.sum(d, axis=0) == 0
dist = lambda k: sum(
    np.abs(a-b).sum() + r[min(a[0],b[0]):max(a[0],b[0])].sum()*(k-1) + c[min(a[1],b[1]):max(a[1],b[1])].sum()*(k-1)
    for a, b in combinations(np.array(np.where(d > 0)).T, r=2)
)
print(dist(2), dist(1000000), sep='\n')