
def leftmostfiling(L):
    M = [x for x in range(20)]
    count = 0
    for l in L:
        i = M.index(l)
        M.remove(l)
        M.insert(0,l)
        count += i
    return count
def rightmostfiling(L):
    M = [x for x in range(20)]
    count = 0
    for l in L:
        i = M.index(l)
        M.remove(l)
        M.append(l)
        count += i
    return count

def fixedfiling(L):
    M = [x for x in range(20)]
    count = 0
    for l in L:
        count += M.index(l)
        M.insert(M.index(l), l)
        M.remove(l)
        count += M.index(l)
    return count



### Do not modify anything below, for testing purposes only.
# Random requests
print("Random request")
L = [int(line) for line in open('data.txt')]

print("Cost for leftmost filing:", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Always request first item
print("Always request first item")
L = [0]*100000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Always request last item
print("Always request last item")
L = [19]*100000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Repeated requests

print("Repeated requests #1")
L = [x for x in range(20)]*5000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

print("Repeated requests #2")
L = [x for x in range(10)]*10000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

print("Repeated requests #3")
L = [x + 10 for x in range(10)]*10000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))
