f = open("day1/input.txt")
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]
movements = [int(x[1:]) if x[0] == "R" else -int(x[1:]) for x in lines]

def partOne():
    dialPosition = 50
    count = 0
    for movement in movements:
        dialPosition = dialPosition + movement
        if dialPosition % 100 == 0:
            count += 1
        
    return count

def partTwo():
    dialPosition = 50
    count = 0
    for movement in movements:
        newDialPosition = dialPosition + movement

        count += abs(newDialPosition // 100)
        # ending at 0 counts as a pass
        if newDialPosition % 100 == 0 and newDialPosition <= 0:
            count += 1
        
        # edge case where we move from 0 to negative number, we'll overcount
        if dialPosition == 0 and newDialPosition < 0:
            count -= 1

        dialPosition = newDialPosition % 100
    return count

print("part one: ", partOne())
print("part two: ", partTwo())