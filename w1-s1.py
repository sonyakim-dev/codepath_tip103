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

# def find_missing_clues(clues, lower, upper):
#     result = []
#     s, e = lower, 0
#     for i in range(1, len(clues)):
        
        
    
#     return result
