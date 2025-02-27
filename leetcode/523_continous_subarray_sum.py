"523. Check subarray Sum"

from typing import List

def check_subarray_sum(nums: List[int], k: int) -> bool:
    "Check subarray Sum"
    remainder_cache = {0:-1}
    remainder = 0
    for i, num in enumerate(nums):
        remainder += num
        remainder %=k
        if remainder not in remainder_cache:
            remainder_cache[remainder] = i
        elif i - remainder_cache[remainder] >=2:
            return True
    return False
