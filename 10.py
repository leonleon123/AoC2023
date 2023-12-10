from matplotlib.path import Path

d = [x for x in open('10.txt').read().split('\n') if x]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pipes = {'|': [1, 0, 1, 0],'-': [0, 1, 0, 1],'L': [1, 1, 0, 0],'J': [1, 0, 0, 1],'7': [0, 0, 1, 1],'F': [0, 1, 1, 0]}
s_pos = [(i,j) for i in range(len(d)) for j in range(len(d[i])) if d[i][j] == 'S'][0]
s_dir = [dd for dd in dirs if (dd[0]*-1,dd[1]*-1) in [dd for val,dd in zip(pipes.get(d[s_pos[0]+dd[0]][s_pos[1]+dd[1]], []), dirs) if val]][0]
pos = (s_pos[0] + s_dir[0], s_pos[1] + s_dir[1])
visited = [s_pos]

while pos not in visited:
    visited.append(pos)
    connecting = [
        x for x in [
            (pos[0]+x[0], pos[1]+x[1]) for x in [dd for val, dd in zip(pipes[d[pos[0]][pos[1]]], dirs) if val] 
            if pos[0]+x[0]>=0 and pos[0]+x[0]<len(d) and pos[1]+x[1]>=0 and pos[1]+x[1]<len(d[0]) 
            and (pos[0]+x[0], pos[1]+x[1]) not in visited and d[pos[0]+x[0]][pos[1]+x[1]] != '.'
        ]
        if not x in visited
    ]
    if len(connecting): pos = connecting[0]
    else: break

print(len(visited) // 2)
print(sum(Path(visited).contains_points([(-1,-1) if (i,j) in visited else (i,j) for i in range(len(d)) for j in range(len(d[i]))])))