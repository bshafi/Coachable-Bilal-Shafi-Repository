"Simplify unix path"

def simplify_path(path: str) -> str:
    "Simplify unix path"
    stack = []
    for elem in path.split('/'):
        if elem in ('', '.'):
            continue
        if elem == '..':
            if stack:
                stack.pop()
        else:
            stack.append(elem)

    return '/' + '/'.join(stack)
