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

def algorithm2(array, dict):
    if len(array)<=3:
        return False
    hm = dict
    target = array[0]
    i = 0
    while i<len(array):
        if target-array[i] in hm:
            return True
        hm[array[i]] = ""
        i += 1
    return algorithm2(array[1:], hm)



print(algorithm2([1,1,1,1,3,5,2,3], {}))