"""
calculate the cumulative sums of the weights

generate a random number withing the max of these weights
use binary search to find the location of the weight
"""

from typing import List
from random import randint

class Solution:
    "Randomly generate a number based of weights"
    def __init__(self, w: List[int]):
        self.cum_sum = [0] * len(w)
        self.cum_sum[0] = w[0]

        for i in range(1, len(w)):
            self.cum_sum[i] = self.cum_sum[i - 1] + w[i]   

    def pick_index(self) -> int:
        "Randomly generate a index based on the weights"
        target = randint(1, self.cum_sum[-1])

        left = 0
        right = len(self.cum_sum)

        while left < right:
            mid = (left + right) // 2

            lower = 1
            if mid > 0:
                lower = self.cum_sum[mid - 1] + 1
            upper = self.cum_sum[mid]

            if lower <= target <= upper:
                return mid
            if target > upper:
                left = mid + 1
            else:
                right = mid
