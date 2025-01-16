"""
    Find all anagrams in a string
"""

from typing import List

class Solution:
    """
        Find all anagrams in a strings
    """
    def find_anagrams(self, s: str, p: str) -> List[int]:
        """
            Find all anagrams in a strings
        """
        if len(p) > len(s):
            return []

        p_counts = [0] * (ord('z') - ord('a') + 1)

        for c in p:
            p_counts[ord('z') - ord(c)] += 1

        counts = [0] * (ord('z') - ord('a') + 1)

        for i in range(len(p) - 1):
            counts[ord('z') - ord(s[i])] += 1

        indices = []

        for i in range(len(p) - 1, len(s)):
            c = s[i]
            counts[ord('z') - ord(c)] += 1

            if counts == p_counts:
                indices.append(i - len(p) + 1)

            last_c = s[i - len(p) + 1]
            counts[ord('z') - ord(last_c)] -= 1

        return indices
