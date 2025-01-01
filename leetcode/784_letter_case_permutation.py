"""
    Generates all permutations of upper and lowercase english characters.
"""

from typing import List

class Solution:
    """
    Generates all permutations of upper and lowercase english characters.
    """
    def letter_case_permutation(self, s: str) -> List[str]:
        """
        Generates all permutations of upper and lowercase english characters.
        """
        if len(s) == 0:
            return []
        permutations = self.letter_case_permutation(s[1:])
        c = s[0]
        letters = [c]
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
            letters = [c.upper(), c.lower()]
        if len(permutations) == 0:
            return letters
        ret = []
        for letter in letters:
            for permutation in permutations:
                ret.append(letter + permutation)
        return ret
