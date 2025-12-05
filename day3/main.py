def joltage(line: str, batteries_needed: int) -> int:
    line = line.strip()

    largest_digits = [-1] * batteries_needed
    for i in range(len(line)):
        digit = int(line[i])
        found_larger_preceding_digit = False

        x = 0
        if len(line) <= i + batteries_needed:
            x = i + batteries_needed - len(line)
        for j in range(x, len(largest_digits)):
            if (not found_larger_preceding_digit) and digit > largest_digits[j]:
                largest_digits[j] = digit
                found_larger_preceding_digit = True
            elif found_larger_preceding_digit:
                largest_digits[j] = -1

    return int(''.join((str(digit) for digit in largest_digits)))

def part_one(lines: list[str]):
    return sum((joltage(line, 2) for line in lines))

def part_two(lines: list[str]):
    return sum((joltage(line, 12) for line in lines))

with open("input.txt") as f:
    lines = f.readlines()
print("part 1:", part_one(lines))
print("part 2:", part_two(lines))