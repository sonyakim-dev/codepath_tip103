def transpose(matrix):
    """_summary_
    (0,0) -> (0,0)
    (0,1) -> (1,0)
    (0,2) -> (2,0)
    (1,0) -> (0,1)
    """
    result = []
    for c in range(len(matrix[0])):
        row = []
        for r in range(len(matrix)):
            row.append(matrix[r][c])
        result.append(row)
    return result

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(transpose(matrix))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(transpose(matrix))


def reverse_list(lst):
    # return lst[::-1]
    l, r = 0, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1
    return lst

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# print(reverse_list(lst))


def remove_dupes(items):
    record = set()
    l, r = 0, len(items) - 1
    
    while l <= r:
        if items[l] in record:
            items[l] = items[r]
            r -= 1
        record.add(items[l])
        l += 1
        
    return r + 1

# items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# print(remove_dupes(items))

# items = ["extract of malt", "haycorns", "honey", "thistle"]
# print(remove_dupes(items))


def sort_by_parity(nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] % 2 == 1:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1
    return nums

# nums = [3, 1, 2, 4]
# print(sort_by_parity(nums))

# nums = [0]
# print(sort_by_parity(nums))

def most_honey(heights):
    water = 0
    l, r = 0, len(heights) - 1
    
    while l < r:
        water = max(water, (r - l) * min(heights[l], heights[r]))
        if l < r:
            l += 1
        else:
            r -= 1
    
    return water

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(most_honey(height))

# height = [1, 1]
# print(most_honey(height))


def merge_intervals(intervals):
    result = []
    curr_s, curr_e = intervals[0]
    
    for s, e in intervals:
        if curr_e < s:
            result.append([curr_s, curr_e])
            curr_s, curr_e = s, e
        else:
            curr_s, curr_e = min(curr_s, s), max(curr_e, e)
            
    result.append([curr_s, curr_e])
    return result

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(merge_intervals(intervals))

# intervals = [[1, 4], [4, 5]]
# print(merge_intervals(intervals))
