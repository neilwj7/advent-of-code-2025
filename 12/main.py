
filename = "input.txt"

queries = []
with open(filename) as file:
    for line in file:
        if "x" in line:
            data = line.strip().split()
            dimensions = data[0][:len(data[0]) - 1].split("x")
            queries.append(([int(x) for x in dimensions], [int(x) for x in data[1:]]))

# part 1
result1 = 0
for query in queries:
    if (query[0][0] // 3) * (query[0][1] // 3) >= sum(query[1]):
        result1 += 1
print(f"part 1: {result1}")

# there is no part 2...