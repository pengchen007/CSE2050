import sys
sys.setrecursionlimit(10000)
### This function uses the Gregory Leibniz series to calculate Pi with n terms, and returns the value of the estimated Pi.
def GregoryLeibniz(n):
    if n == 1:
        return 4.0
    else:
        return 4/((2*n-1)*(-1)**(n+1)) + GregoryLeibniz(n-1)
### This function uses the Nilakantha series to calculate Pi with n terms, and returns the value of the estimated Pi.
def Nilakantha(n):
    if n == 0:
        return 3
    else:
        return 4 / ((2*(n+1))*((2*(n+1))-1)*((2*(n+1))-2)*(-1)**(n+1)) + Nilakantha(n-1)

n = 100
for i in range(n):
    print(i+1, GregoryLeibniz(i+1), Nilakantha(i+1))
### In this piece of code, we print the minimum number of terms required in order to approximate pi within an accuracy of 0.001 by using Gregory Leibniz series, together with the approximated value of pi.
pi = 3.1415927
accuracy = 0.001
i=0
diff = 1
result = 0
while diff > accuracy:
    result = GregoryLeibniz(i+1)
    diff = abs(result-pi)
    i += 1
print("GregoryLeibniz", i, result)
### In this piece of code, we print the minimum number of terms required in order to approximate pi within an accuracy of 0.001 by using Nilakantha series, together with the approximated value of pi.
i=0
diff = 1
result = 0
while diff > accuracy:
    result = Nilakantha(i+1)
    diff = abs(result-pi)
    i += 1
print("Nilakantha", i, result)
