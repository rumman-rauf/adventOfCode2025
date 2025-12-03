with open("input.txt") as f:
    lines = f.readlines()

def joltage(line: str) -> int:
    line = line.strip()

    largest = -1
    second_largest = -1
    for digit in line[:-1]:
        digit = int(digit)
        if digit > largest:
            largest = digit
            second_largest = -1
        elif digit > second_largest:
            second_largest = digit

    if int(line[-1]) > second_largest:
        second_largest = int(line[-1])

    return largest * 10 + second_largest

def partOne():
    total = sum((joltage(line) for line in lines))
    print(total)

partOne()