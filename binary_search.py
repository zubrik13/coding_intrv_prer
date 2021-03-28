"""
Here we rely on the assumption that the list is ordered.
The idea is simple:
1. Pick an index, i, that divides the list L roughly in half.
2. Ask if L[i] == e.
3. If not, ask whether L[i] is larger or smaller than e.
4. Depending upon the answer, search either the left or right half of L for e.
"""


def search(L, e):
    """
    Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L and False otherwise
    Time complexity O(log(len(L)))
    """

    def bin_search(L, e, low, high):
        # Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)

L = [1, 3, 5, 9]
print(search(L, 3))