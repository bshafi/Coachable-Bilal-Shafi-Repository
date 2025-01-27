"""
Kth largest element
"""

from typing import List
from random import randint

def partition(nums, lo, hi):
    """
        Three way partition
    """
    pivot_i = randint(lo, hi)
    pivot = nums[pivot_i]

    i = lo
    j = lo
    k = hi

    while j <= k:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > pivot:
            nums[k], nums[j] = nums[j], nums[k]
            k -= 1
        else:
            j += 1

    return (i, j)

def quick_select(nums, target, lo, hi):
    "Quick select"
    i, j = partition(nums, lo, hi)

    if i <= target < j:
        return nums[target]
    if target >= j:
        return quick_select(nums, target, j, hi)
    return quick_select(nums, target, lo, i - 1)

def find_kth_largest(nums: List[int], k: int) -> int:
    "Kth largest"
    return quick_select(nums, len(nums) - k, 0, len(nums) - 1)
