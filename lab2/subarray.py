def maxSubarraySum(arr, res = 0, maxEnding = 0):
    # Stores the result (maximum sum found so far)
    res = res

    # Maximum sum of subarray ending at current position
    maxEnding = maxEnding

    for i in range(1, len(arr)):
        # Either extend the previous subarray or start
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])

        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)

    return res

def maxSubarraySum2(arr):
    if len(arr) == 1:
        return arr[0], arr[0], arr[0], arr[0]

    middle = len(arr) // 2

    left_max, left_prefix, left_suffix, left_total = maxSubarraySum2(arr[:middle])
    right_max, right_prefix, right_suffix, right_total = maxSubarraySum2(arr[middle:])

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


print(maxSubarraySum2([-5, -2, -9, -1, -8]))
