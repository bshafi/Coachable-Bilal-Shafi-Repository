"636. Exclusive Time of Functions"

from typing import List

def parse_log(log):
    "Parse logs"
    sections = log.split(':')
    return (int(sections[0]), sections[1], int(sections[2]))

def exclusive_times(n: int, logs: List[str]) -> List[int]:
    "636. Exclusive Time of Functions"
    times = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        log_id, action, time = parse_log(log)

        if "start" == action:
            if stack:
                diff = time - prev_time
                times[stack[-1]] += diff

            stack.append(log_id)
            prev_time = time
        else:
            stack.pop()

            times[log_id] += time - prev_time + 1

            prev_time = time + 1

    return times
