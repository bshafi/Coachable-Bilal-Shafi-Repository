"670. Maximum Swap"


def maximum_swap(num: int) -> int:
    "Find the maximum swap "
    if num == 0:
        return 0


    digits = []

    a = num
    i = 0
    while a != 0:
        digits.append(a % 10)
        a = a // 10
        i += 1


    max_i = 0
    max_val = digits[0]

    best_lo_i = 0
    best_hi_i = 0
    best_change_in_value = 0

    for i, cur in enumerate(digits):
        cur_change_in_value = (
            (-cur * (10 ** i) - digits[max_i] * (10 ** max_i)) +
            (cur * (10 ** max_i) + digits[max_i] * (10 ** i))
        )

        if cur_change_in_value > best_change_in_value:
            best_lo_i = i
            best_hi_i = max_i
            best_change_in_value = cur_change_in_value

        if digits[i] > max_val:
            max_i = i
            max_val = digits[i]

    digits[best_lo_i], digits[best_hi_i] = digits[best_hi_i], digits[best_lo_i]

    res = 0
    while digits:
        res = (10 * res) + digits.pop()

    return res
