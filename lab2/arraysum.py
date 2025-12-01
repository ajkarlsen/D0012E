import random

def genArray(n):
    array = []
    while n>0:
        array.append(random.randint(0, n))
        n = n-1
    return array

def algorithm1(array):
    if len(array)<=3:
        return False
    j = 0
    while j < len(array):
        k = j+1
        while k < len(array):
            if array[0] + array[j] == array[k]:
                return True
            k += 1
        j += 1
    return algorithm1(array[1:])


#def algorithm2(array, exTargets=None):
    if exTargets is None:
        exTargets = {}

    if array==[]:
        return False

    target = array[0]

    for element in exTargets:
        needed = target-element

        if needed in exTargets and needed != element:
            return True

    exTargets[target] = ""
    return algorithm2(array[1:], exTargets)



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

