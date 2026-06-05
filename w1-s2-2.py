def add_matrices(matrix1, matrix2):
    row, col = len(matrix1), len(matrix1[0])
    
    for r in range(row):
        for c in range(col):
            matrix1[r][c] += matrix2[r][c]
    
    return matrix1

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# print(add_matrices(matrix1, matrix2))


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# s = "madam"
# print(is_palindrome(s))

# s = "madamweb"
# print(is_palindrome(s))


def squash_spaces(s):
    result = ""
    for i, c in enumerate(s):
        if c == " " and (i == 0 or i == len(s) - 1 or s[i-1] == " "):
            continue
        result += c
    return result

# s = "   Up,     up,   and  away! "
# print(squash_spaces(s))

# s = "With great power comes great responsibility."
# print(squash_spaces(s))


def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else: # nums[l] + nums[r] == target
            return [l, r]

# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))

# nums = [2, 7, 11, 15]
# target = 18
# print(two_sum(nums, target))


def three_sum(nums):
    nums.sort()
    result = []

    pass
# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))

# nums = [0, 1, 1]
# print(three_sum(nums))

# nums = [0, 0, 0]
# print(three_sum(nums))
