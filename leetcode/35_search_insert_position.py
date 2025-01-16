"""
    35. Search Insert Position
"""

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """
    Find the target in a sorted array. 
    If the target is not in the array returns the position where it would be inserted
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
