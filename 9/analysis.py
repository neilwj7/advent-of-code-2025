"""
This script performs analysis on my input to ensure my solution works. 
In particular, it checks for two things:
    1. Are there ever three points in a row with the same row or column?
    2. Once the trail leaves a specific row or a column, does it ever come back?
"""

filename = "input.txt"
points = [[int(x) for x in line.strip().split(",")] for line in open(filename)]
common_element = []
for i in range(1, len(points)):
    p1 = points[i - 1]
    p2 = points[i]
    if p1[0] == p2[0]:
        common_element.append(0)
    else:
        common_element.append(1)
for i in range(1, len(common_element)):
    if common_element[i-1] == common_element[i]:
        print("triple found")
rows = set()
cols = set()
for i in range(1, len(points)):
    p1 = points[i-1]
    p2 = points[i]
    if p1[0] == p2[0]:
        if p1[0] in rows:
            print("duplicate row")
        rows.add(p1[0])
    else:
        if p1[1] in cols:
            print("duplicate col")
        cols.add(p1[1])
