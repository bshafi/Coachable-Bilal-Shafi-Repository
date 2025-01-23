"""
    1047. Remove all Adjacent Duplicates in String
"""

def remove_duplicates(s: str) -> str:
    """
        Removes the adjacent duplicates in the string
    """
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
