from collections import Counter, defaultdict


def find_balanced_subsequence(art_pieces):
    """
    balance = diff min max == 1
    return: length of balanced subsq
    input: int list , duplicates, not ordered 
    """
    record = Counter(art_pieces)
    result = 0
    for n in art_pieces:
        if n + 1 in record:
            result = max(result, record[n] + record[n+1])
        if n - 1 in record:
            result = max(result, record[n] + record[n-1])
    return result


def is_authentic_collection(art_pieces):
    # sort? n log n
    # find the max
    n = len(art_pieces)
    unique = set()
    


art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
