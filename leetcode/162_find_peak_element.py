"162. Find Peak Element"

from typing import List

def find_peak_element(nums: List[int]) -> int:
    "162. Find Peak Element"
    lo = 0
    hi = len(nums) - 1
    ret = None
    while lo <= hi:
        mid = (lo + hi) // 2

        if mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
            lo = mid + 1
        elif 0 <= mid - 1 and nums[mid - 1] > nums[mid]:
            hi = mid - 1
        else:
            ret = mid
            break

    return ret
