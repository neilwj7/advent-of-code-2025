from bisect import bisect_right

filename = "input.txt"

points = [[int(x) for x in line.strip().split(",")] for line in open(filename)]

# part 1
result1 = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        result1 = max(result1, (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1))
print(f"part 1: {result1}")

# build walls
horizontal_walls = []
vertical_walls = []
hw_rows = []
vw_cols = []
for i in range(1, len(points)):
    p1 = points[i-1]
    p2 = points[i]
    if p1[0] == p2[0]:
        horizontal_walls.append([p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])])
        hw_rows.append(p1[0])
    else:
        vertical_walls.append([p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])])
        vw_cols.append(p1[1])
hw_rows.sort()
vw_cols.sort()

# functions to help validate points
def covered_h(r, c, hw):
    covered_above = covered_below = False
    for wall in hw:
        if not wall[1] <= c <= wall[2]:
            continue
        if r == wall[0]:
            return True
        elif r > wall[0]:
            covered_above = True
        else:
            covered_below = True
        if covered_above and covered_below:
            return True
    return False

def covered_v(r, c, vw):
    covered_right = covered_left = False
    for wall in vw:
        if not wall[1] <= r <= wall[2]:
            continue
        if c == wall[0]:
            return True
        elif c > wall[0]:
            covered_left = True
        else:
            covered_right = True
        if covered_left and covered_right:
            return True
    return False

def covered(r, c, hw, vw):
    return covered_h(r, c, hw) and covered_v(r, c, vw)

def valid(p1, p2, hw, vw):
    if not covered(p1[0], p2[1], hw, vw) or not covered(p2[0], p1[1], hw, vw):
        return False
    top_row = min(p1[0], p2[0])
    bottom_row = max(p1[0], p2[0])
    left_col = min(p1[1], p2[1])
    right_col = max(p1[1], p2[1])
    next_col_idx = bisect_right(vw_cols, left_col)
    while next_col_idx < len(vw_cols) and vw_cols[next_col_idx] < right_col:
        curr_col = vw_cols[next_col_idx]
        if not covered(top_row, curr_col, hw, vw) or not covered(bottom_row, curr_col, hw, vw):
            return False
        next_col_idx += 1
    next_row_idx = bisect_right(hw_rows, top_row)
    while next_row_idx < len(hw_rows) and hw_rows[next_row_idx] < bottom_row:
        curr_row = hw_rows[next_row_idx]
        if not covered(curr_row, left_col, hw, vw) or not covered(curr_row, right_col, hw, vw):
            return False
        next_row_idx += 1
    return True

# part 2
result2 = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        potential_area = max(result2, (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1))
        if potential_area > result2 and valid(points[i], points[j], horizontal_walls, vertical_walls):
            result2 = potential_area
print(f"part 2: {result2}")