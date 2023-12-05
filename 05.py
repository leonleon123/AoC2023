from functools import reduce

seeds_line, *map_lines = [x for x in open('05.txt').read().split('\n\n')]
maps = [[(range(s,s+l), d) for d,s,l in m] for m in [[map(int, y.split(' ')) for y in x.split('\n')[1:]] for x in map_lines]]
seeds = [int(x) for x in seeds_line[7:].split(' ')]
seed_ranges = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

def transform_seed(seed, m):
    for r, d in m:
        if seed in r:
            return d + (seed - r.start)
    return seed

def transform_seed_range(seed_range, m):
    for r, d in m:
        if seed_range.start <= r.start and seed_range.stop <= r.stop and seed_range.stop >= r.start:
            return [range(seed_range.start, r.start), range(d, d + (seed_range.stop - r.start))]
        elif seed_range.start >= r.start and seed_range.stop >= r.stop and seed_range.start <= r.stop:
            return [range(r.stop, seed_range.stop), range(d + (seed_range.start - r.start), d + (r.stop - r.start))]
        elif seed_range.start >= r.start and seed_range.stop <= r.stop:
            return [range(d + (seed_range.start - r.start), d + (seed_range.stop - r.start))]
        elif seed_range.start <= r.start and seed_range.stop >= r.stop:
            return [range(seed_range.start, r.start), range(d, d + (r.stop - r.start)), range(r.stop, seed_range.stop)]
    return [seed_range]

for m in maps:
    seeds = [transform_seed(x, m) for x in seeds]
    seed_ranges = reduce(lambda a, b: a+b, [transform_seed_range(x, m) for x in seed_ranges])

print(min(seeds), min([r for r in seed_ranges if r.start > 0], key=lambda r: r.start).start, sep='\n')
