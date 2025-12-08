def p1():
    nums = []
    ops = []
    with open("input.txt") as f:
        for line in f.readlines():
            row = line.split()
            try:
                int(row[0])
                nums.append(list(map(int, row)))
            except ValueError:
                ops = row

    results = []
    for col in range(len(nums[0])):
        op = ops[col]
        results.append(nums[0][col])
        for row in range(1, len(nums)):
            if op == '+':
                results[col] += nums[row][col]
            else:
                results[col] *= nums[row][col]

    return sum(results)

def p2():
    nums = []
    ops = ''
    with open("input.txt") as f:
        for line in f.readlines():
            row = line.split()
            try:
                int(row[0])
                nums.append(line[:-1]) # take out the newline
            except ValueError:
                ops = line

    # use ops as indexes
    cols = []
    prev_idx = 0
    for i in range(1, len(ops)):
        if ops[i] == '+' or ops[i] == '*':
            cols.append([])
            for row in nums:
                cols[-1].append(row[prev_idx:i - 1])
            prev_idx = i
    cols.append([])
    for row in nums:
        cols[-1].append(row[prev_idx:len(ops)])
        
    actual_nums = []
    for col in cols:
        # go backwards
        actual_nums.append([])
        for i in range(len(col[0]) - 1, -1, -1):
            actual_num = ''
            for num in col:
                if num[i] == ' ':
                    continue
                actual_num += num[i]
            actual_nums[-1].append(int(actual_num))

    actual_ops = ops.split()
    results = []
    for i in range(len(actual_nums)):
        op = actual_ops[i]
        actual_row = actual_nums[i]
        results.append(actual_row[0])
        for num in actual_row[1:]:
            if op == '+':
                results[i] += num
            else:
                results[i] *= num

    return sum(results)

print(p1())
print(p2())