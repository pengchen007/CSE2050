import time

def mergesort(L):
    cost_A = 0
    cost_B = 0
    cost_m = 0

    if len(L) < 2:    
        return 1

    mid = len(L)//2

    A = L[:mid]

    B = L[mid:]

    mergesort(A)
    cost_A += mergesort(A)

    mergesort(B)
    cost_B += mergesort(B)
    
    merge(A, B, L)
    cost_m = merge(A, B, L)

    return (cost_A + cost_B + cost_m + 1)

def merge(A, B, L):
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]

            i += 1
        else:
            L[i+j] = B[j]

            j += 1
    L[i+j:] = A[i:] + B[j:]

    return len(L)

def bubblesort(L):
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                keepgoing = True

def selectionsort(L):
    n = len(L)
    for i in range(n-1):
        max_index = 0
        for index in range(n-i):
            if L[index] > L[max_index]:
                max_index = index
        L[n-i-1], L[max_index] = L[max_index], L[n-i-1]


def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n-1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j += 1
    
##def run(fun, k, trials = 400):
##    print(fun)
##    for j in range(k):        
##        start = time.time()
##        for i in range(trials):
##            L = [i for i in range(2**j, 0, -1)]
##            fun(L)
##        end = time.time()
##        if j == 0: old = (end - start)/trials
##        else: print("%7.3f" % ((end - start)/trials/old))
##        old = (end - start)/trials

##run(mergesort, 10)
##run(bubblesort, 10)
##run(selectionsort, 10)
##run(insertionsort, 10)




