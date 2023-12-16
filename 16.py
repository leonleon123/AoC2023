import numpy as np

dirs = np.array([(-1, 0), (0, 1), (1, 0), (0, -1)])
d = [x for x in open('16.txt').read().split('\n')]

def energize(sp, s_dir_idx):
    m, q, visited = np.zeros((len(d), len(d[0]))).astype(int), [(np.array(sp), s_dir_idx)], set()

    while len(q):
        p, dir_idx = q.pop(0)

        if (tuple(p), dir_idx) in visited: continue
        visited.add((tuple(p), dir_idx))

        if p[0] < 0 or p[1] < 0 or p[0] >= len(d) or p[1] >= len(d[0]): continue

        c = d[p[0]][p[1]]
        dir = dirs[dir_idx]
        left_dir_idx, right_dir_idx = (dir_idx - 1) % len(dirs), (dir_idx + 1) % len(dirs)
        left_dir, right_dir = dirs[left_dir_idx], dirs[right_dir_idx]
        m[p[0]][p[1]] = 1

        if c == '|' and dir[1] != 0 or c == '-' and dir[0] != 0:
            q.append((p + left_dir, left_dir_idx))
            q.append((p + right_dir, right_dir_idx))
        elif c == '/':
            if dir_idx == 0 or dir_idx == 2: q.append((p + right_dir, right_dir_idx))
            elif dir_idx == 1 or dir_idx == 3: q.append((p + left_dir, left_dir_idx))
        elif c == '\\':
            if dir_idx == 0 or dir_idx == 2: q.append((p + left_dir, left_dir_idx))
            elif dir_idx == 1 or dir_idx == 3: q.append((p + right_dir, right_dir_idx))
        else: q.append((p + dir, dir_idx))
    return m.sum()

print(energize((0,0), 1))
print(max([
    *[energize((i, 0), 1) for i in range(len(d))],
    *[energize((0, i), 2) for i in range(len(d[0]))],
    *[energize((i, len(d[0]) - 1), 3) for i in range(len(d))],
    *[energize((len(d) - 1, i), 0) for i in range(len(d[0]))]
]))