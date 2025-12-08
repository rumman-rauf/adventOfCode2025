ranges = []
ingredients = []
with open("input.txt") as f:
    ingredient_flag = False
    for line in map(lambda l: l.strip(), f.readlines()):
        if line == '':
            ingredient_flag = True
            continue

        if ingredient_flag:
            ingredients.append(int(line))
        else:
            ranges.append(tuple(map(int, line.split('-'))))

# merge intervals
ranges.sort()
curr_l, curr_r = ranges[0]
merged_ranges = []

for l, r in ranges[1:]:
    if l <= curr_r:
        curr_r = max(curr_r, r)
    else:
        merged_ranges.append((curr_l, curr_r))
        curr_l, curr_r = l, r

merged_ranges.append((curr_l, curr_r))

def p1():
    # could binary search but i think linear scan is fast enough
    def find(val: int ) -> bool:
        for l, r in merged_ranges:
            if val >= l and val <= r:
                return True
        return False
        
    ans = 0
    for ingredient in ingredients:
        if find(ingredient):
            ans += 1
    
    return ans

def p2():
    ans = 0
    for l, r in merged_ranges:
        ans += r - l + 1
    return ans

print(p1())
print(p2())