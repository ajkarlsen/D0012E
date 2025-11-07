from main import Stack, Node
import random
import time


def generateNodes(n):
    stack = Stack()

    for i in range(n):
        rand = random.randint(1,n)
        stack.push(rand)

    return stack

def generateNodes2(n):
    stack = Stack()
    for i in range(n, 0, -1):
        stack.push(i)
    return stack

def sortStack(n):
    # i = 0
    start = time.time()
    sortedStack = Stack()
    unsortedStack = generateNodes(n)


    while not unsortedStack.isEmpty():

        temp = unsortedStack.pop()
        # i +=1
        # n + n(n-1)/2 = (n^2+n)/2

        while not sortedStack.isEmpty():
            peeked_var = sortedStack.pop()
            # i+=1
            # n(n-1)/2 + n(n-1)/2 = n^2-n

            # i += 1

            if peeked_var < temp:
             # n(n-1)/2 + n(n-1)/2 = n^2-n
                unsortedStack.push(peeked_var)
                # i+=1
                # n(n-1)/2
            else:
                sortedStack.push(peeked_var)
                # i+=1
                # n(n-1)/2
                break

        sortedStack.push(temp)
        # i+=1
        # n + n(n-1)/2 = (n^2+n)/2


    end = time.time()
    while not sortedStack.isEmpty():
        print(sortedStack.pop())
    print(f"Total runtime of the program is {end - start} seconds")
    # print("i: ",i)

sortStack(10000)