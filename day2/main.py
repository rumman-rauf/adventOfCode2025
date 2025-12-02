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
    pass

print("part one:", partOne())