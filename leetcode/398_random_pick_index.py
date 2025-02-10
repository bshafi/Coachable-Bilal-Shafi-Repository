"398. Random Pick Index"

from collections import defaultdict
from typing import List
from random import randint

class Solution:
    "398. Random Pick Index"

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)

        for i, num in enumerate(nums):
            self.nums[num].append(i)

    def pick(self, target: int) -> int:
        "398. Random Pick Index"
        res = self.nums[target]

        return res[randint(0, len(res) - 1)]
