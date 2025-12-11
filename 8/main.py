
filename = "input.txt"
num_connections = 1000

# get input
boxes = [tuple((int(x) for x in line.strip().split(","))) for line in open(filename)]

# compute distances (note: this actually uses euclidian distance squared to keep integers)
def get_distance(point1, point2):
    result = 0
    for i in range(3):
        result += (point1[i] - point2[i]) ** 2
    return result

# given a list of sets, returns indices of sets elements b1 and b2 are in (or -1 if not in any)
def get_group_ids(groups, b1, b2):
    g1, g2 = -1, -1
    for i, group in enumerate(groups):
        if b1 in group:
            g1 = i
        if b2 in group:
            g2 = i
    return g1, g2

# updates the list of sets according to a connection between box1 and box2
def update_groups(groups, b1, b2):
    g1, g2 = get_group_ids(groups, b1, b2)
    if g1 == -1 and g2 == -1:
        groups.append(set([b1, b2]))
    elif g2 == -1:
        groups[g1].add(b2)
    elif g1 == -1:
        groups[g2].add(b1)
    elif g1 != g2:
        groups[g1].update(list(groups[g2]))
        del groups[g2]

# compute distances
distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distances.append((get_distance(boxes[i], boxes[j]), i, j))
distances.sort()

# part 1
groups = []
for i in range(num_connections):
    _, b1, b2 = distances[i]
    update_groups(groups, b1, b2)
lengths = sorted([len(x) for x in groups], key=lambda x: -x)
result1 = 1
for length in lengths[:3]:
    result1 *= length
print(f"part 1: {result1}")

# part 2 (continues from part 1)
result2 = 0
for i in range(num_connections, len(distances)):
    _, b1, b2 = distances[i]
    update_groups(groups, b1, b2)
    if len(groups) == 1 and len(groups[0]) == len(boxes):
        result2 = boxes[b1][0] * boxes[b2][0]
        break
print(f"part 2: {result2}")
