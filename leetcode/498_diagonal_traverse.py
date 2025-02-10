"498. Diagonal Traverse"


from typing import List

def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    "498. Diagonal Traverse"
    elems = []

    rows = len(mat)
    cols = len(mat[0])

    x = 0
    y = 0

    going_backwards = False

    while 0 <= x < rows and 0 <= y < cols:
        elems.append(mat[x][y])


        next_x = x - 1
        next_y = y + 1
        if going_backwards:
            next_x = x + 1
            next_y = y - 1

        if 0 <= next_x < rows and 0 <= next_y < cols:
            x = next_x
            y = next_y
            continue

        if next_x < 0 and next_y == cols:
            x += 1

        elif next_x == rows and next_y < 0:
            y += 1
        elif next_x < 0:
            # top edge
            y += 1
        elif next_y < 0:
            # left edge
            x += 1
        elif next_x == rows:
            # bottom edge
            y += 1
        elif next_y == cols:
            # right edge
            x += 1

        going_backwards = not going_backwards

    return elems
