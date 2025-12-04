
data = []
filename = "input.txt"

with open(filename, "r") as file:
    for line in file:
        data.append(list(line.strip()))

# helper function for both parts (different n values)
def find_max_ndigits(row, n):
    digits = []
    prev_digit_position = -1
    for curr_digit in range(1, n + 1):
        curr_max = 0
        max_position = 0
        for i in range(prev_digit_position + 1, len(row) - (n - curr_digit)):
            if int(row[i]) > curr_max:
                curr_max = int(row[i])
                max_position = i
        digits.append(curr_max)
        prev_digit_position = max_position
    return int("".join([str(x) for x in digits]))

# part 1
result1 = 0
for line in data:
    result1 += find_max_ndigits(line, 2)
print(f"part 1: {result1}")

# part 2
result2 = 0
for line in data:
    result2 += find_max_ndigits(line, 12)
print(f"part 2: {result2}")
