from re import findall, match
from math import lcm

d = [x for x in open('08.txt').read().split('\n') if x]
ins, nodes = d[0], {x: (l,r) for x,l,r in[findall('([0-9A-Z]+)', x) for x in d[1:]]}
def get_score(node, e_node_re, i=0, c=0):
    while not match(e_node_re, node): i, c, node = (i + 1) % len(ins), c + 1, nodes[node][ins[i] == 'R']
    return c
print(get_score('AAA', 'ZZZ'), lcm(*[get_score(x, '.*Z') for x in nodes if match('.*A', x)]), sep='\n')
