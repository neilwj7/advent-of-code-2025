from collections import deque

filename = "input.txt"

# get input
grid = None
with open(filename, "r") as file:
    grid = [list(line.strip()) for line in file]

# get cells next to current
def get_adjacent(i, j):
    return [(i + dx, j + dy)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if not (dx == 0 and dy == 0)]

# helper function for both parts
def get_count(grid, i, j):
    count = 0
    checkset = get_adjacent(i, j)
    for ni, nj in checkset:
        if min(ni, nj) < 0 or ni >= len(grid) or nj >= len(grid[0]):
            continue
        count += 1 if grid[ni][nj] == "@" else 0
    return count

# part 1
result1 = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "@":
            result1 += 1 if get_count(grid, x, y) < 4 else 0
print(f"part 1: {result1}")

# part 2
counts = {}
cutset = deque()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "@":
            count = get_count(grid, x, y)
            if count < 4:
                cutset.append((x, y))
            else:
                counts[(x, y)] = count 
result2 = 0
while cutset:
    result2 += 1
    i, j = cutset.popleft()
    checkset = get_adjacent(i, j)
    for ni, nj in checkset:
        if min(ni, nj) < 0 or ni >= len(grid) or nj >= len(grid[0]) or (ni, nj) not in counts:
            continue
        counts[(ni, nj)] -= 1
        if counts[(ni, nj)] < 4:
            cutset.append((ni, nj))
            del counts[(ni, nj)]
print(f"part 2: {result2}")
