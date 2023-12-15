d, b = open('15.txt').read().split(','), {}

def get_hash(s, v = 0):
    for c in s: v = ((v + ord(c)) * 17) % 256
    return v

for ins in d:
    if '-' in ins:
        label = ins[:-1]
        v = get_hash(label)
        if v in b: b[v] = [(l, fl) for l, fl in b[v] if l != label]
    elif '=' in ins:
        label, lens = ins.split('=')
        v = get_hash(label)
        if v in b:
            for i in range(len(b[v])):
                if b[v][i][0] == label:
                    b[v][i] = (label, int(lens))
                    break
            else: b[v] = [*b[v], (label, int(lens))]
        else: b[v] = [(label, int(lens))]

print(sum(get_hash(x) for x in d), sum(sum((key + 1) * (i + 1) * fl for i, (l, fl) in enumerate(b[key])) for key in b), sep='\n')