"""
Heap

Calculate the magnitude and heapify them O(n)
Pop the top k elements from the min heap O(k log(n))


Add the points to a max heap O(n log(k))
if the the size exceeds the capcity pop the max heap

return max heap
"""

from typing import List
from heapq import heappush, heappop

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    "Returns k closest points to origin"
    heap = []

    for point in points:
        mag = (point[0] ** 2) + (point[1] ** 2)
        heappush(heap, (-mag, point))
        if len(heap) > k:
            heappop(heap)

    return [point for mag, point in heap]
