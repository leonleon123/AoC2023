from functools import cmp_to_key
from itertools import product

d, chars = [x.split(' ') for x in open('07.txt').read().split('\n') if x], 'AKQJT98765432'[::-1]

def get_power(hand):
    power_functions = [
        lambda h: len(set(h)) == 1,
        lambda h: len(set(h)) == 2 and tuple(sorted(h.count(x) for x in set(h))) == (1, 4),
        lambda h: len(set(h)) == 2 and tuple(sorted(h.count(x) for x in set(h))) == (2, 3),
        lambda h: len(set(h)) == 3 and tuple(sorted(h.count(x) for x in set(h))) == (1, 1, 3),
        lambda h: len(set(h)) == 3 and tuple(sorted(h.count(x) for x in set(h))) == (1, 2, 2),
        lambda h: len(set(h)) == 4,
        lambda h: len(set(h)) == 5
    ]
    return len(power_functions) - [fn(hand) for fn in power_functions].index(True)

def create_compare(chars):
    def compare(a, b):
        if a[0] != b[0]: return a[0] - b[0]
        else:
            for ac, bc in zip(a[1], b[1]):
                if ac != bc: return chars.index(ac) - chars.index(bc)
    return compare

get_max_power = lambda h: max(get_power(h.replace('J', '{}').format(*repl)) for repl in product(chars.replace('J', ''), repeat=h.count('J')))
get_score = lambda f, c: sum(x[2]*(i+1) for i, x in enumerate(sorted([(f(h), h, int(b)) for h, b in d], key=cmp_to_key(create_compare(c)))))

print(*[get_score(f,c) for f, c in [(get_power, chars), (get_max_power, 'J'+chars.replace('J', ''))]], sep='\n')
