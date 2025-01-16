"""
    953. Verifying an Alien Dictionary
"""

from typing import List

def alien_le(left, right, alien_order):
    """
        Determines if less than or equal to in alien_order
    """
    for i in range(min(len(left), len(right))):
        l = alien_order[left[i]]
        r = alien_order[right[i]]

        if l > r:
            return False
        if l < r:
            return True

    if len(left) > len(right):
        return False
    return True

def is_alien_sorted(words: List[str], order: str) -> bool:
    """
        Determins if words is sorted in alien order 
    """
    if len(words) == 0:
        return True

    alien_order = {}
    for i, c in enumerate(order):
        alien_order[c] = i

    for i in range(1, len(words)):
        prev = words[i - 1]
        cur = words[i]

        if not alien_le(prev, cur, alien_order):
            return False

    return True
