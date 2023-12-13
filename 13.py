import numpy as np

d = [np.array([['.#'.index(z) for z in y] for y in x.split('\n')]) for x in open('13.txt').read().split('\n\n')]

def offset(p, repair):
    for i in range(1, len(p)):
        top, bottom = p[:i], np.flip(p[i:], axis=0)
        m = min(len(top) , len(bottom))
        if (np.all(top[-m:] == bottom[-m:]) and not repair) or (np.sum(top[-m:] != bottom[-m:]) == 1 and repair):
            return i
    return 0

print(*[sum(offset(p, r) * 100 + offset(p.T, r) for p in d) for r in [False, True]], sep='\n')
