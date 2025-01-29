"""
    767. Reorganize String
"""
def find_max_char(counts, k):
    "Find max count excluding index k"
    max_i = None
    max_counts = 0
    for i, count in enumerate(counts):
        if i != k and count > max_counts:
            max_i = i
            max_counts = count

    return max_i

def reorganize_string(s: str) -> str:
    """
    767. Reorganize String
    """
    counts = [0] * (ord('z') - ord('a') + 1)
    for c in s:
        counts[ord(c) - ord('a')] += 1

    j = find_max_char(counts, None)
    if j is None:
        return ""
    res = [chr(j + ord('a'))]
    counts[j] -= 1

    for _i in range(1, len(s)):
        j = find_max_char(counts, j)
        if j is None:
            return ""

        res.append(chr(j + ord('a')))
        counts[j] -= 1

    return "".join(res)
