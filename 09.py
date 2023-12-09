d = [[int(y) for y in x.split(' ')] for x in open('09.txt').read().split('\n') if x]

def extrapolate(h, forward):
    t, a = h, [h]

    while not all([x == 0 for x in t]):
        t = [t[i + 1] - t[i] for i in range(len(t) - 1)]
        a.append(t)

    for x in a: x.insert(len(x) if forward else 0, 0)

    for i in range(len(a) - 2, -1, -1):
        if forward: a[i][-1] = a[i][-2] + a[i+1][-1]
        else: a[i][0] = a[i][1] - a[i+1][0]

    return a[0][-1] if forward else a[0][0]

print(*[sum(extrapolate(x, forward) for x in d) for forward in [True, False]], sep='\n')