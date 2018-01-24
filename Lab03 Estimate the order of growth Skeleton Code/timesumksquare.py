import time
import math
import statistics


def selectionsort(L):      
    start = time.time()
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            while L[j] < L[i]:
                L[i],L[j] = L[j],L[i]
    end = time.time()      
    return L, end - start  

def sumksquare(k):
    start = time.time()   
    total = 0
    for i in range(1,k+1):
        total += i**2   
    end = time.time()
    return total, end - start  

def sumksquare2(k):
    start = time.time()
    total = k*(k+1)*(2*k+1)/6
    end = time.time()      
    return total, end - start  

#Calculate the time taken for 20 trials
def timetrials(func, k, trials =20):
    totaltime = 0
    for i in range(trials):
        totaltime += func(k)[1]
    return totaltime/trials

### Call the sumksquare2 function and obtain the total time
T = [timetrials(sumksquare2, 10000, 10000)]
T.append(timetrials(sumksquare2, 100000, 10000))
T.append(timetrials(sumksquare2, 1000000, 10000))
T.append(timetrials(sumksquare2, 10000000, 10000))

###Estimate the order of grwoth for sumksquare2
m = int(statistics.mean([math.log(T[i+1]/T[i], 10) for i in range(len(T)-1)])+ 0.5)
print("The order of growth for running time of sumksquare2 is n^%d" % m)

### Call the sumksquare function and obtain the total time
T = [timetrials(sumksquare, 1000)]
T.append(timetrials(sumksquare, 10000))
T.append(timetrials(sumksquare, 100000))
T.append(timetrials(sumksquare, 1000000))

###Estimate the order of grwoth for sumksquare
m = int(statistics.mean([math.log(T[i+1]/T[i], 10) for i in range(len(T)-1)])+ 0.5)
print("The order of growth for running time of sumksquare is n^%d" % m)

### Call the selectionsort function and obtain the total time
L = list(range(10))
T = [timetrials(selectionsort, L)]
L = list(range(100))
T.append(timetrials(selectionsort, L))
L = list(range(1000))
T.append(timetrials(selectionsort, L))

###Estimate the order of grwoth for selectionsort
m = int(statistics.mean([math.log(T[i+1]/T[i], 10) for i in range(1, len(T)-1)])+ 0.5)
print("The order of growth for running time of selection sort is n^%d" % m)

### A list with values in the descending order
L = list(range(10, 0, -1))

### Call the selectionsort function and obtain the total time
T = [timetrials(selectionsort, L)]
L = list(range(100, 0, -1))
T.append(timetrials(selectionsort, L))
L = list(range(1000, 0, -1))
T.append(timetrials(selectionsort, L))

###Estimate the order of grwoth for selectionsort
m = int(statistics.mean([math.log(T[i+1]/T[i], 10) for i in range(1, len(T)-1)])+ 0.5)
print("The order of growth for running time of selection sort is n^%d" % m)


