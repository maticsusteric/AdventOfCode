from helpers import getDailyInputByFolderNoParsing

# TODO: Comment the code if you have a crumb of energy
# Read input data
inputData = getDailyInputByFolderNoParsing().strip().split('\n\n')

#print(inputData)

seeds, *maps = [item.split('\n') for item in inputData]
seeds = [int(s) for s in seeds[0].split()[1:] if s]

seed_range = [
    [seeds[i], seeds[i] + seeds[i + 1] - 1]
    for i in range(0, len(seeds), 2)
]

for map in maps:
    rows = sorted([[int(num) for num in row.split()] for row in map[1:]], key=lambda x: x[1])
    for i, s in enumerate(seeds):
        for start, offset, length in rows:
            if offset <= s < offset + length:
                seeds[i] += start - offset
                break

min_seed = min(seeds)
print(min_seed)

for map in maps:
    rows = sorted([[int(num) for num in row.split()] for row in map[1:]], key=lambda x: x[1])
    updated_seeds = []

    while seed_range:
        seed_start, seed_end = seed_range.pop(0)
        for row in rows:
            if row[1] <= seed_start < row[1] + row[2]:
                end = row[1] + row[2] - 1
                shift = row[0] - row[1]
                updated_seeds.append(
                    [seed_start + shift, min(seed_end, end) + shift]
                )
                if end < seed_end:
                    seed_start = end + 1
                else:
                    break
        else:
            updated_seeds.append([seed_start, seed_end])
    seed_range = updated_seeds

min_start = min(seed[0] for seed in seed_range)
print(min_start)