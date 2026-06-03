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


# def remove_dupes(items):
#     record = set()
    
#     for i, item in enumerate(items):
#         if item in record:
#             itmes.
#     return len(items)
