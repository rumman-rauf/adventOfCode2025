dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def p1():
    with open('input.txt') as f:
        rolls = []
        for line in f.readlines():
            rolls.append(line.strip())
        
        res = 0
        for row in range(len(rolls)):
            for col in range(len(rolls[row])):
                num_adj = 0
                if rolls[row][col] != '@':
                    continue

                for i in range(8):
                    d_row = dy[i]
                    d_col = dx[i]
                    if row + d_row < 0 or row + d_row >= len(rolls):
                        continue
                    if col + d_col < 0 or col + d_col >= len(rolls[row]):
                        continue
                    if rolls[row+d_row][col+d_col] == '@':
                        num_adj += 1

                if num_adj < 4:
                    res += 1
        
        return res
    
def p2():
    with open('input.txt') as f:
        rolls = []
        for line in f.readlines():
            rolls.append(line.strip())
        
        num_adj_map = [[0 for _ in range(len(rolls[0]))] for _ in range(len(rolls))]
        remove_queue = []
        for row in range(len(rolls)):
            for col in range(len(rolls[row])):
                num_adj = 0
                if rolls[row][col] != '@':
                    continue

                for i in range(8):
                    d_row = dy[i]
                    d_col = dx[i]
                    if row + d_row < 0 or row + d_row >= len(rolls):
                        continue
                    if col + d_col < 0 or col + d_col >= len(rolls[row]):
                        continue
                    if rolls[row+d_row][col+d_col] == '@':
                        num_adj += 1

                num_adj_map[row][col] = num_adj
                if num_adj < 4:
                    remove_queue.append((row, col))

        res = 0
        visited = [[False for _ in range(len(rolls[0]))] for _ in range(len(rolls))]

        while (len(remove_queue) > 0):
            row, col = remove_queue.pop()
            if visited[row][col]:
                continue

            visited[row][col] = True
            res += 1

            for i in range(8):
                d_row = dy[i]
                d_col = dx[i]
                new_row = row + d_row
                new_col = col + d_col
                if new_row < 0 or new_row >= len(rolls):
                    continue
                if new_col < 0 or new_col >= len(rolls[row]):
                    continue
                
                
                if rolls[new_row][new_col] == '@':
                    num_adj_map[new_row][new_col] -= 1

                    if num_adj_map[new_row][new_col] < 4:
                        remove_queue.append((new_row, new_col))
            
        return res


print(p1())
print(p2())