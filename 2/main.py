
filename = "input.txt"
ranges = []
with open(filename, "r") as file:
    for line in file:
        for r in line.split(","):
            num1, num2 = r.split("-")
            ranges.append((int(num1), int(num2)))

# part 1
def check1(x):
    x = str(x)
    if len(x) % 2:
        return False
    return x[:len(x)//2] == x[len(x)//2:]

result1 = 0
for a, b in ranges:
    for x in range(a, b + 1):
        result1 += x if check1(x) else 0
print(f"part 1: {result1}")

# part 2
def check2(x):
    x = str(x)
    if len(x) > 1 and len(set(list(x))) == 1:
        return True
    roots = []
    for n in range(2, len(x) // 2 + 1):
        if len(x) % n == 0:
            roots.append(([n, len(x) // n]))
    for r1, r2 in roots:
        curr_i = r1
        prev = x[:r1]
        for _ in range(r2 - 1):
            if x[curr_i:curr_i+r1] != prev:
                break
            curr_i += r1
        else:
            return True
        curr_i = r2
        prev = x[:r2]
        for _ in range(r1 - 1):
            if x[curr_i:curr_i+r2] != prev:
                break
            curr_i += r2
        else:
            return True
    return False

result2 = 0
for a, b in ranges:
    for x in range(a, b + 1):
        result2 += x if check2(x) else 0
print(f"part 2: {result2}")