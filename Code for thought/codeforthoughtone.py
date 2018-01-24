### Run the code below and understand the error messages
### Fix the code to sum integers from 1 up to k
### 

def f(k):
    while k > 0:
        return f(k-1)+k
    return 0

print(f(10))
