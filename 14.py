import numpy as np

d, c = np.array([['.#O'.index(y) for y in x] for x in open('14.txt').read().split('\n')]), {}
score = lambda d: np.sum(np.sum(d == 2, axis=1) * np.arange(len(d[0]), 0, -1))

def store_sort_key(stone, dir):
    if dir[0] == -1: return stone[0]
    elif dir[0] == 1: return -stone[0]
    elif dir[1] == -1: return stone[1]
    elif dir[1] == 1: return -stone[1]

def move_stones(dir, d):
    for s in np.array(sorted(np.array(np.where(d == 2)).T, key=lambda s: store_sort_key(s, dir))):
        n = s + dir
        while n[0] >= 0 and n[0] < len(d) and n[1] >= 0 and n[1] < len(d[0]) and d[n[0]][n[1]] == 0:
            n = n + dir
        n = n - dir
        d[s[0]][s[1]] = 0
        d[n[0]][n[1]] = 2

for i in range(1_000_000_000):
    for dir in np.array([[-1,0],[0,-1], [1,0],  [0,1]]):
        move_stones(dir, d)
        if dir[0] == -1 and i == 0:
            print(score(d))
    key = tuple(d.ravel())
    if key in c:
        idx = ((1_000_000_000 - c[key]) % (i - c[key])) + c[key] - 1
        print(score(np.array([key for key, val in c.items() if val == idx][0]).reshape((len(d), len(d[0])))))
        break
    c[key] = i
