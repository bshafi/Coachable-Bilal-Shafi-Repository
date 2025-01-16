"""
    283. Move Zeroes
"""

from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 0
    for i, c in enumerate(nums):
        if c != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
