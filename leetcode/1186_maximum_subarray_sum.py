"""
    1186. Maximum subarray sum with one deletion
"""

from typing import List

def maximum_sum(arr: List[int]) -> int:
    """
        1186. Maximum subarray sum with one deletion
    """
    if len(arr) == 0:
        return 0

    max_sum = -float('inf')
    max_zero = -float('inf')
    max_one = -float('inf')

    for elem in arr:
        max_one = max(elem + max_one, max_zero)
        max_zero = max(elem + max_zero, elem)

        max_sum = max(max_sum, max_one, max_zero)

    return max_sum
