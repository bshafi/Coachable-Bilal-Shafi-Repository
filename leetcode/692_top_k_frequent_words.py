"""
    Calculate the top k frequent words
"""
from heapq import heapify, heappop
from typing import List


class CountWord:
    """
        Class that implments < for a integer count and a string word
    """
    def __init__(self, count, word):
        self.count = count
        self.word = word
    def __lt__(self, rhs):
        if self.count != rhs.count:
            return self.count < rhs.count
        return self.word < rhs.word
class Solution:
    """
        Solution to leetcode problem
    """
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
            Returns the top k frequent words.
            Words with the same frequency will be in lexographical order.
        """
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1

        arr = [CountWord(-count, word) for (word, count) in counts.items()]
        heapify(arr)
        res = []
        for _i in range(k):
            if len(arr) == 0:
                break
            res.append(heappop(arr).word)
        return res
