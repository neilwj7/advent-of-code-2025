
filename = "input.txt"

ranges = []
ingredients = []
with open(filename, "r") as file:
    range_portion = True
    for line in file:
        if not range_portion:
            ingredients.append(int(line.strip()))
        elif line == '\n':
            range_portion = False
        else:
            ranges.append([int(bound) for bound in line.strip().split("-")])

# part 1
result1 = 0
for ing in ingredients:
    for r1, r2 in ranges:
        if r1 <= ing <= r2:
            result1 += 1
            break
print(f"part 1: {result1}")

# part 2
def merge_intervals(intervals):
    intervals.sort()
    result = []
    ps, pe = intervals[0]
    for ns, ne in intervals[1:]:
        if ns <= pe:
            pe = max(ne, pe)
        else:
            result.append([ps, pe])
            ps, pe = ns, ne
    result.append([ps, pe])
    return result
ranges = merge_intervals(ranges)
result2 = 0
for r1, r2 in ranges:
    result2 += r2 - r1 + 1
print(f"part 2: {result2}")