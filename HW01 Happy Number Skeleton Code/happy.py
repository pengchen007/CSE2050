def happy(number):
    s = list()
    while True:
        new_n = 0
        l = str(number)
        for i in range(len(l)):
            new_n += (int(l[i])**2)
        if new_n == 1:
            return True
        elif new_n in s:
            return False
        s.append(new_n)
        number = new_n

        
n = 0
for i in range(1000):
    s = str(i+1)
    if happy(s):
        n += 1;
        print(n, ':', s)

    
        





