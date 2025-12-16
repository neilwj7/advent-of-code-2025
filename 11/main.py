from collections import defaultdict

filename = "input.txt"

# get input
edges = defaultdict(list)
with open(filename) as file:
    for line in file:
        nodes = line.strip().split()
        edges[nodes[0][:len(nodes[0]) - 1]].extend(nodes[1:])

# part 1
cache = {"out": 1}
def dfs(node):
    if node in cache:
        return cache[node]
    result = 0
    for out_node in edges[node]:
        result += dfs(out_node)
    cache[node] = result
    return result

result1 = dfs("you")
print(f"part 1: {result1}")

# part 2
cache = {"out": (0, 0, 1, 0)} # dac, fft, neither, both
def dfs_part2(node):
    if node in cache:
        return cache[node]
    dac_count, fft_count, neither_count, both_count = 0, 0, 0, 0
    for out_node in edges[node]:
        dc, fc, nc, bc = dfs_part2(out_node)
        dac_count += dc
        fft_count += fc
        neither_count += nc
        both_count += bc
    if node == "dac":
        both_count = fft_count
        dac_count = neither_count
        fft_count = 0
        neither_count = 0
    if node == "fft":
        both_count = dac_count
        fft_count = neither_count
        dac_count = 0
        neither_count = 0
    cache[node] = (dac_count, fft_count, neither_count, both_count)
    return cache[node]

result2 = dfs_part2("svr")[3]
print(f"part 2: {result2}")
