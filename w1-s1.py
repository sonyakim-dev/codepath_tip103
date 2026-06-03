def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# print(linear_search(items, target))

# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# print(linear_search(items, target))


def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ['bouncy','flouncy']:
            tigger += 1
        elif op in ['trouncy', 'pouncy']:
            tigger -= 1
    return tigger

# operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

# operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))


def tiggerfy(word):
    result = ''
    i = 0
    while i < len(word):
        if word[i].lower() in ['t', 'i']:
            i += 1
        elif i < len(word) - 1 and word[i:i+2].lower() in ['gg', 'er']:
            i += 2
        else:
            result += word[i].lower()
            i += 1
    return result

# word = "Trigger"
# print(tiggerfy(word))

# word = "eggplant"
# print(tiggerfy(word))

# word = "Choir"
# print(tiggerfy(word))


def non_decreasing(nums):
    flag = False
    
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            if flag: return False
            flag = True

    return True

# nums = [4, 2, 3]
# print(non_decreasing(nums))

# nums = [4, 2, 1]
# print(non_decreasing(nums))


def find_missing_clues(clues, lower, upper):
    result = []
    bound = lower
    
    for c in clues:
        if c > bound:
            result.append([bound, c - 1])
            bound = c + 1
        else:
            bound = c + 1
    
    if clues[-1] < upper:
        result.append([bound, upper])
    return result

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print(find_missing_clues(clues, lower, upper))

# clues = [-1]
# lower = -1
# upper = -1
# print(find_missing_clues(clues, lower, upper))


def harvest(vegetable_patch):
    carrots = 0
    for r in range(len(vegetable_patch)):
        for c in range(len(vegetable_patch[0])):
            if vegetable_patch[r][c] == 'c':
                carrots += 1
    
    return carrots

# vegetable_patch = [
# 	['x', 'c', 'x'],
# 	['x', 'x', 'x'],
# 	['x', 'c', 'c'],
# 	['c', 'c', 'c']
# ]
# print(harvest(vegetable_patch))


def good_pairs(pile1, pile2, k):
    good = 0
    for p1 in pile1:
        for p2 in pile2:
            if p1 % (p2 * k) == 0:
                good += 1
    return good

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# print(good_pairs(pile1, pile2, k))

# pile1 = [1, 2, 4, 12]
# pile2 = [2, 4]
# k = 3
# print(good_pairs(pile1, pile2, k))


def local_maximums(grid):
    result = []
    n = len(grid)
    
    for r in range(n - 2):
        row = []
        for c in range(n - 2):
            row.append(max(grid[i][j] for i in range(r, r + 3) for j in range(c, c + 3)))
        result.append(row)

    return result

# grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
# ]
# print(local_maximums(grid)) # [[9, 9], [8, 6]]

# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# print(local_maximums(grid)) # [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
