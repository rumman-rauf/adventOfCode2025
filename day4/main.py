with open("input.txt") as f:
    rows = f.readlines()
graph = [[
    0 if char=='@' else -1 for char in row.strip()
] for row in rows]

height = len(graph)
width = len(graph[0])

def mark_adjacent_cels(row, col):
    directions = (-1,0,1)
    for di in directions:
        for dj in directions:
            i = row + di
            j = col + dj
            if 0 <= i < height and 0 <= j < width and (row, col) != (i, j):
                if graph[i][j] >= 0:
                    graph[i][j] += 1

def part_one():
    for i in range(height):
        for j in range(width):
            if graph[i][j] >= 0:
                mark_adjacent_cels(i, j)
    result = 0
    for row in graph:
        for cell in row:
            if 0 <= cell < 4:
                result += 1
                # print("XXX", end=" ")
            else:
                pass
                # print(str(cell).rjust(3), end=" ")
        # print()
    return result

print("part one:", part_one())