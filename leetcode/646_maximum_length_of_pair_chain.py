"""
    Find the longest chain of pairs where the last element of 
    the previous pair is strictly less than the first element of the next pair.
"""

from typing import List

class Solution:
    """
        Find the longest chain of pairs where the last element of 
        the previous pair is strictly less than the first element of the next pair.
    """
    def find_longest_chain(self, pairs: List[List[int]]) -> int:
        """
            Find the longest chain of pairs where the last element of 
            the previous pair is strictly less than the first element of the next pair.
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