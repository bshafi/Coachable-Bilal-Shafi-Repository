"""
    Find the longest chain given pairs of integers. 
    A chain can be formed if two pairs (a, b) and (c, d) satisfy b < c.
"""

from typing import List

class Solution:
    """
        Solution to problem
    """
    def find_longest_chain(self, pairs: List[List[int]]) -> int:
        """
            Find the longest chain given pairs of integers. 
            A chain can be formed if two pairs (a, b) and (c, d) satisfy b < c.
        """
        pairs.sort(key=lambda elem: elem[1])
        count = 0
        last_chain = None
        for start, end in pairs:
            if last_chain is None:
                last_chain = end
                count += 1
            elif last_chain < start:
                last_chain = end
                count += 1
        return count
