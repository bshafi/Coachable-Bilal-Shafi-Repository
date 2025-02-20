"""
    1539. Kth Missing Positive Number
"""

from typing import List

def find_kth_positive(arr: List[int], k: int) -> int:
    """
        Finds the kth missing positive number that is not included in arr
    """
    if len(arr) == 0:
        return k

    expecting = 1
    missing = 0
    for i, num in enumerate(arr):
        diff = num - expecting
        if missing + diff >= k:
            if i == 0:
                return k

            return arr[i - 1] + (k - missing)

        missing += diff
        expecting = num + 1
    return arr[-1] + (k - missing)
