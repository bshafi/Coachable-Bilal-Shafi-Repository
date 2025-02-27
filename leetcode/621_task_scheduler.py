"621. Task Scheduler"

from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List

def least_interval(tasks: List[str], n: int) -> int:
    "621. Task Scheduler"
    counts = defaultdict(int)

    for task in tasks:
        counts[task] += 1

    heap = [(-count, task) for (task, count) in counts.items()]
    heapify(heap)

    latest_occurence = {}
    schedule_size = 0
    while heap:
        top_np1 = [heappop(heap) for _ in range(min(len(heap), n + 1))]

        for top_count, top_task in top_np1:

            prev_occurence = latest_occurence.get(top_task, None)
            if prev_occurence is not None and schedule_size - prev_occurence <= n:
                offset = n + 1 - (schedule_size - prev_occurence)
                schedule_size += offset

            latest_occurence[top_task] = schedule_size
            schedule_size += 1

            if top_count + 1 != 0:
                heappush(heap, (top_count + 1, top_task))

    return schedule_size
