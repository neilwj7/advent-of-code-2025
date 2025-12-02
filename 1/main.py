filename = "input.txt"
instructions = []

with open(filename, "r") as file:
    for line in file:
        direction = line[0]
        magnitude = int(line[1:])
        instructions.append((direction, magnitude))

# part 1
result1 = 0
pointer1 = 50
for dir, mag in instructions:
    if dir == "R":
        pointer1 = (pointer1 + mag) % 100
    else:
        pointer1 = (pointer1 - mag) % 100
    result1 += 1 if not pointer1 else 0
print(f"result to part 1: {result1}")

# part 2
result2 = 0
pointer2 = 50
for dir, mag in instructions:
    if dir == "R":
        result2 += (pointer2 + mag) // 100
        pointer2 = (pointer2 + mag) % 100
    else:
        if not pointer2 and mag:    # needed if we start on 0 and are going left
            result2 -= 1
        result2 += abs((pointer2 - mag) // 100)
        pointer2 = (pointer2 - mag) % 100
        result2 += 1 if not pointer2 else 0
print(f"result to part 2: {result2}")