from collections import defaultdict

filename = "input.txt"

# get input
targets = []
buttons = []
joltages = []
with open(filename) as file:
    for line in file:
        data = line.strip().split()
        pattern = data[0][1:len(data[0]) - 1]
        target = []
        for c in pattern:
            if c == "#":
                target.append(True)
            else:
                target.append(False)
        targets.append(target)
        joltage = data[-1][1:len(data[-1]) - 1]
        joltages.append([int(x) for x in joltage.split(",")])
        curr_buttons = []
        for b in data[1:len(data) - 1]:
            b = b[1:len(b) - 1]
            curr_buttons.append([int(x) for x in b.split(",")])
        buttons.append(curr_buttons)

def match(target, buttonset):
    target = tuple(target)
    result = len(buttonset)
    curr_pattern = [False] * len(target)
    curr_score = 0
    def dfs(i):
        nonlocal result, curr_pattern, curr_score
        if i >= len(buttonset):
            if tuple(curr_pattern) == target:
                result = min(curr_score, result)
            return
        dfs(i + 1)
        if curr_score < result:
            curr_score += 1
            for b in buttonset[i]:
                curr_pattern[b] = not curr_pattern[b]
            dfs(i + 1)
            for b in buttonset[i]:
                curr_pattern[b] = not curr_pattern[b]
            curr_score -= 1
        return result
    dfs(0)
    return result

# part 1
result1 = 0
for target, buttonset in zip(targets, buttons):
    result1 += match(target, buttonset)
print(f"part 1: {result1}")

def match_joltages(target_joltages, buttonset):
    parity_builders = defaultdict(list)
    curr_buttons = []
    def build_parity_combinations(i):
        nonlocal curr_buttons
        if i >= len(buttonset):
            parity = [False] * len(target_joltages)
            for b in curr_buttons:
                button = buttonset[b]
                for j in button:
                    parity[j] = not parity[j]
            parity_builders[tuple(parity)].append(curr_buttons[:])
            return
        build_parity_combinations(i + 1)
        curr_buttons.append(i)
        build_parity_combinations(i + 1)
        curr_buttons.pop()
    build_parity_combinations(0)
    cache = {}
    def solve(pattern):
        nonlocal cache, parity_builders
        if min(pattern) < 0:
            return float("inf")
        if max(pattern) == 0:
            return 0
        if tuple(pattern) in cache:
            return cache[tuple(pattern)]
        parity = []
        for p in pattern:
            if p % 2 == 0:
                parity.append(False)
            else:
                parity.append(True)
        builders = parity_builders[tuple(parity)]
        result = float('inf')
        for builder in builders:
            pattern_copy = pattern[:]
            for b in builder:
                button = buttonset[b]
                for j in button:
                    pattern[j] -= 1
            for i, p in enumerate(pattern):
                if p > 0:
                    pattern[i] = p // 2
            result = min(result, 2 * solve(pattern) + len(builder))
            pattern[:] = pattern_copy
        cache[tuple(pattern)] = result
        return result
    return solve(target_joltages)

# part 2
result2 = 0
for target_joltage, buttonset in zip(joltages, buttons):
    num_to_add = match_joltages(target_joltage, buttonset)
    result2 += num_to_add
print(f"part 2: {result2}")
