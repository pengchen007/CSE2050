from fractions import Fraction
import itertools
ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

class ListStack:
    def __init__(self):
        self._L = []
        
    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self._L) == 0

def evaluate(s):
    stack = ListStack()
    for i in s:
        if i in d:
            stack.push(d[i])
        elif i == ops[0]:
            a = stack.pop()
            b = stack.pop()
            result = a+b
            stack.push(result)
        elif i == ops[2]:
            a = stack.pop()
            b = stack.pop()
            result = a*b
            stack.push(result)
        elif i == ops[1]:
            a = stack.pop()
            b = stack.pop()
            result = b-a
            stack.push(result)
        else:
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return 0
            else:
                result = Fraction(b,a)
                stack.push(result)
    return stack.pop()

def evaluate_all_ops(s):
    results = set()
    for i in ops:
        for j in ops:
            for k in ops:
                form1 = s[:2]+[i]+s[2:]+[j]+[k]
                form2 = s+[i,j,k]
                form3 = s[:3]+[i]+s[3:]+[j,k]
                form4 = s[:2]+[i]+[s[2]]+[j]+s[3:]+[k]
                form5 = s[:3]+[i,j]+s[3:]+[k]
                allform = [form1, form2, form3, form4, form5]
                for f in allform:
                    if evaluate(f) == 24:
                        results.add(str(f))
    return results


##    # add your code here
##
### The code below is for testing purposes only; do not modify anything.
##print('Input the cards:')
print('Input the cards:')
s = list(input())
print(s)
s1 = [0, 1, 2, 3]
results_set = set()
# itertools is a Python module that allows us to create all possible permutations of four numbers of length 4.
# For each permutation, loop over the permutation and copy the values of the elements into a new list, s1.
# This creates all possible orderings of the 4 cards.
# For each ordering, evaluate_all_ops() is called to determine all possible orderings of the three operations with the given card ordering.
for L in list(itertools.permutations([0, 1, 2, 3], 4)):
    for i in range(4):
        s1[i] = s[L[i]]
    results_set = results_set | evaluate_all_ops(s1)

# Print each possible solution for a 4-card combination:
for item in results_set:
    print(item)
print(len(results_set), ' solutions.')
