def maxSubarraySum2(arr, start, end):

    if  start == end:
        return arr[0], arr[0], arr[0], arr[0]

    middle = (start + end)/2

    left_max, left_prefix, left_suffix, left_total = maxSubarraySum2(arr, start, middle)
    right_max, right_prefix, right_suffix, right_total = maxSubarraySum2(arr, middle, end)

    total = left_total + right_total

    prefix = left_prefix
    if left_total + right_prefix > left_prefix:
        prefix = left_total + right_prefix

    suffix = right_suffix
    if right_total + left_suffix > right_suffix:
        suffix = right_total + left_suffix

    middle_sum = left_suffix + right_prefix

    max = left_max
    if right_max > max:
        max = right_max
    if middle_sum > max:
        max = middle_sum

    return max, prefix, suffix, total


