
filename = "input.txt"

# get input for part 1
nums_lists = []
ops = []
with open(filename) as file:
    for line in file:
        if line[0] in "*+":
            ops = line.strip().split()
        else:
            nums_lists.append([int(c) for c in line.strip().split()])
nums_lists = list(map(list, zip(*nums_lists)))

def multiply(nums):
    result = 1
    for num in nums:
        result = num * result
    return result

# computation for part 1
result1 = 0
for op, nums_list in zip(ops, nums_lists):
    if op == "+":
        result1 += sum(nums_list)
    else:
        result1 += multiply(nums_list)
print(f"part 1: {result1}")

# get input for part 2 
char_grid = [line for line in open(filename)]
char_grid = char_grid[:len(char_grid) - 1] # remove ops (we have from part 1)
for i, line in enumerate(char_grid):
    char_grid[i] = line[:len(line) - 1] # remove trailing '\n' on each line

# build nums_lists one column at a time
nums_lists = [[]]
for curr_col_idx in range(len(char_grid[0])):
    curr_col = "".join([char_grid[r][curr_col_idx] for r in range(len(char_grid))])
    num = curr_col.strip()
    if not num:
        nums_lists.append([])
    else:
        nums_lists[-1].append(int(num))
    curr_col_idx += 1

# computation for part 2
result2 = 0
for op, nums_list in zip(ops, nums_lists):
    if op == "+":
        result2 += sum(nums_list)
    else:
        result2 += multiply(nums_list)
print(f"part 2: {result2}")