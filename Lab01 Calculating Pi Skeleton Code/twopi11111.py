def GregoryLeibniz(n):
    result = 0
    for i in range(n):
        result += 4 / (2*(i+1) - 1) * (-1)**i
    return result

def Nilakantha(n):
    result = 3
    for i in range(n):
        result += 4 / ((2*(i+2))*((2*(i+2))-1)*((2*(i+2))-2)*(-1)**i)
    return result

n = 100
for i in range(n):
    print(i+1, GregoryLeibniz(i+1), Nilakantha(i+1))

pi = 3.1415927
accuracy = 0.001
i=0
diff = 1
result = 0
while diff > accuracy:
    result = GregoryLeibniz(i + 1)
    diff = abs(result - pi)
    i += 1
print("GregoryLeibniz", i, result)

i=0
diff = 1
result = 0
while diff > accuracy:
    result = Nilakantha(i + 1)
    diff = abs(result - pi)
    i += 1
print("Nilakantha", i, result)



