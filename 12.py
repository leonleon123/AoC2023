from functools import lru_cache

d =  [(a, tuple(map(int, g.split(',')))) for a, g in [x.split(' ') for x in open('12.txt').read().splitlines(False)]]

@lru_cache
def possibilities(line, groups):
    if len(groups) == 0: return 1 if '#' not in line else 0
    elif len(line) == 0: return 0
    if len(line) < sum(groups) + len(groups) - 1: return 0

    if line[0] == '?': return possibilities(line[1:], groups) + hash(line, groups)
    else: return possibilities(line[1:], groups) if  line[0] == '.' else hash(line, groups)

def hash(line, groups):
    if '.' not in line[:groups[0]] and (line[groups[0]:]+'.')[0] != '#': return possibilities(line[groups[0] + 1:], groups[1:])
    else: return 0

print(sum(possibilities(a, g) for a, g in d), sum(possibilities('?'.join([a for _ in range(5)]), g * 5) for a, g in d), sep='\n')