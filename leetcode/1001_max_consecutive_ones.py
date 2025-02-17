"1001. Max Consecutive Ones"

from typing import List

def longest_ones(nums: List[int], k: int) -> int:
    "1001. Max Consecutive Ones"
    max_value = 0
    start = 0
    zero_count = 0
    for stop, num in enumerate(nums):
        if num == 0:
            zero_count += 1

        while zero_count > k and start <= stop:
            if nums[start] == 0:
                zero_count -= 1
            start += 1

        max_value = max(max_value, stop - start + 1)
    return max_value
