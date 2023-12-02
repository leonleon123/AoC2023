from math import prod

bag = {'red': 12, 'green': 13, 'blue': 14}
games = [[{k:int(v) for v,k in [y.split(' ') for y in p.split(', ')]} for p in l.split(': ')[1].split('; ')] for l in open('02.txt').read().split('\n')]

print(sum(i + 1 for i, valid in enumerate(all(all(pull.get(k, 0) <= bag[k] for k in bag) for pull in g) for g in games) if valid))
print(sum(prod(max(g, key=lambda x: x.get(k, 0))[k] for k in bag) for g in games))