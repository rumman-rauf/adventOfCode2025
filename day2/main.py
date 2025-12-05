with open('input.txt') as f:
    pairs = [tuple(map(int,pair.split('-'))) for pair in f.read().strip().split(",")]

def partOne():    
    r = 0
    for pair in pairs:
        for n in range(pair[0], pair[1] + 1):
            x = str(n)
            if len(x) % 2 != 0:
                continue
            if x[:len(x) // 2] == x[len(x) // 2:]:
                r += n
    return r

def partTwo():
    r = 0
    for pair in pairs:
        left, right = pair
        r += helper(left, right)

    return r

digits = {
    2: [1],
    3: [1],
    4: [1, 2],
    5: [1],
    6: [1,2,3],
    7: [1],
    8: [1,2,4],
    9: [1,3],
    10: [1,2,5]
}

def helper(a: int, b : int):
    # 52500467
    res = 0
    for n in range(a, b + 1):
        num_digits = len(str(n))
        n_str = str(n)
        if num_digits not in digits:
            continue
        for digit in digits[num_digits]:
            first_str = n_str[:digit]
            matched = True
            for i in range(0, num_digits // digit):
                if first_str != n_str[i*digit : i*digit + digit]:
                    matched = False
                    break
            if matched:
                res += n
                break

    return res


print("part one:", partOne())
print("part two:", partTwo())