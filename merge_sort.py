"""
Merge sort is a prototypical divide-and-conquer algorithm.
It was invented in 1945, by John von Neumann, and is still widely used.
Like many divide-and-conquer algorithms it is most easily described recursively:
1. If the list is of length 0 or 1, it is already sorted.
2. If the list has more than one element, split the list into two
lists, and use merge sort to sort each of them.
3. Merge the results.
The key observation made by von Neumann is that two sorted lists can be efficiently merged into a single sorted list.
The idea is to look at the first element of each list and move the smaller of the two to the end of the result list.
When one of the lists is empty, all that remains is to copy the remaining items from the other list.
"""


def merge(left, right, compare):
    """
    Assumes left and right are sorted lists and compare defines an ordering of the elements
    Returns a new sorted (by compare) list containing the same elements as
    (left + right) would contain.
    Time complexity O(len(L))
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L, compare=lambda x, y: x < y):
    """
    Assumes L is a list, compare defines an ordering on elements of L
    Returns a  new sorted list with same elements as L
    Time complexity O(n*log(n)), where n is len(L)
    Space complexity O(len(L))
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


L = [2, 1, 4, 5, 3]

print(merge_sort(L))
print(merge_sort(L), merge_sort(L, lambda x, y: x > y))