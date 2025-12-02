import random

def genArray(n):
    array = []
    while n>0:
        array.append(random.randint(0, n))
        n = n-1
    return array


def algorithm20(array, index=0, exTargets=None):
    if exTargets is None:
        exTargets = set()

    if index >= len(array):
        return False

    target = array[index]

    for element in exTargets:
        needed = target - element

        if needed in exTargets and needed != element:
            return True

        sum = target + element
        if sum in exTargets and sum != element:
            return True
    exTargets.add(target)

    return algorithm20(array, index + 1, exTargets)

def algorithm2(A, n):

    # Recursive base case, when only 2 elements in array, sort them and return false
    # since 2 elements cant build x + y = z
    if n < 3:

        if A[0] > A[1]:
            temp = A[0]
            A[0] = A[1]
            A[1] = temp
        return False

    if algorithm2(A, n - 1):
        return True

    # Set the last element of the usable length to the target
    target = A[n - 1]

    # Declare 2 pointers, one in the start and one in the end of the list
    # Move pointer 2 down if too big and pointer 1 up if too small
    left = 0
    right = n - 2
    while left < right:
        current_sum = A[left] + A[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1


    # To check if target is a part of x + y = z but is not z, we use absolute value
    # this checks if target is either x or y

    target_diff = target
    if target_diff < 0:
        target_diff = -target_diff

    # We declare 2 new pointers, one at first element and one at second. If this diff is too big, we
    # try with the next pair instead, aka move up both pointers one step
    left = 0
    right = 1

    while right < n - 1:
        diff = A[right] - A[left]

        if diff < target_diff:
            right += 1
        elif diff > target_diff:
            left += 1
            if left == right:
                right += 1
        else:
            return True

    # sort in the element which was being used as target to make sure list is sorted for next
    # recursive run
    j = n - 2
    while j >= 0 and A[j] > target:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = target

    return False


def algorithm1(A, n):

    if n < 3:
        return False

    if algorithm1(A, n - 1):
        return True

    target = A[n - 1]

    i = 0
    while i < n - 1:
        j = i + 1
        while j < n - 1:
            x = A[i]
            y = A[j]


            if x + y == target:
                return True


            if x + target == y:
                return True


            if y + target == x:
                return True

            j += 1
        i += 1

    return False