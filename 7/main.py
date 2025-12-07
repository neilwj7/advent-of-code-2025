
filename = "input.txt"

# get input
grid = [list(line.strip()) for line in open(filename)]

# find original beam
original_beam = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            original_beam = c
            break
    if original_beam is not None:
        break

# part 1
result1 = 0
beams = [original_beam]
for row in range(1, len(grid)):
    new_beams = []
    for beam in beams:
        if grid[row][beam] == "^":
            result1 += 1
            if not new_beams or new_beams[-1] != beam - 1:
                new_beams.append(beam - 1)
            new_beams.append(beam + 1)
        elif not new_beams or new_beams[-1] != beam:
            new_beams.append(beam)
    beams = new_beams
print(f"part 1: {result1}")

# part 2
beams_counts = [[original_beam, 1]]
for row in range(1, len(grid)):
    new_beams_counts = []
    for beam, count in beams_counts:
        if grid[row][beam] == "^":
            if not new_beams_counts or new_beams_counts[-1][0] != beam - 1:
                new_beams_counts.append([beam - 1, count])
            else:
                new_beams_counts[-1][1] += count
            new_beams_counts.append([beam + 1, count])
        elif not new_beams_counts or new_beams_counts[-1][0] != beam:
            new_beams_counts.append([beam, count])
        else:
            new_beams_counts[-1][1] += count
    beams_counts = new_beams_counts
result2 = sum((count for _, count in beams_counts))
print(f"part 2: {result2}")