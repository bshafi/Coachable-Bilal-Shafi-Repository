"207. Course Schedule"

from typing import List
from collections import defaultdict, deque

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    "207. Course Schedule"
    prereq_counts = [0] * num_courses

    graph = defaultdict(list)

    for course, prereq in prerequisites:
        prereq_counts[course] += 1
        graph[prereq].append(course)

    queue = deque([i for i, count in enumerate(prereq_counts) if count == 0])

    visited = set()

    course_count = 0

    while queue:
        course = queue.popleft()

        if course in visited:
            continue

        visited.add(course)
        course_count += 1

        if course_count >= num_courses:
            return True

        for post_req in graph[course]:
            prereq_counts[post_req] -= 1

            if prereq_counts[post_req] == 0 and post_req not in visited:
                queue.append(post_req)

    return False
