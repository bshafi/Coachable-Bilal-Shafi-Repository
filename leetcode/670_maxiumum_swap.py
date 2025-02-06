"670. Maximum Swap"


def maximum_swap(num: int) -> int:
    "Find the maximum swap "
    if num == 0:
        return 0


    digits = []

    a = num
    i = 0
    while a != 0:
        digits.append((i, a % 10))
        a = a // 10
        i += 1

    sorted_digits = sorted(digits, key=lambda x: x[1])

    for i in range(len(digits) - 1, -1, -1):
        if sorted_digits[i][1] != digits[i][1]:
            a = sorted_digits[i][0]
            b = digits[i][0]

            min_sorted_digits = sorted_digits[i]
            for j in range(0, len(digits)):
                if (sorted_digits[j][1] == min_sorted_digits[1] and
                sorted_digits[j][0] < min_sorted_digits[0]):
                    a = sorted_digits[j][0]
                    min_sorted_digits = sorted_digits[j]

            digits[a], digits[b] = digits[b], digits[a]
            break

    res = 0
    while digits:
        res = (10 * res) + digits.pop()[1]

    return res
