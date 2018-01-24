k = ['1', '2', '3', '4'] 
ops = ['+', '-', '*', '/']

def hhh(s):
    a = []
    for i in ops:
        for j in ops:
            for k in ops:
                form = s[:2]+[i]+s[2:]+[j]+[k]
                print(form)
                a.append(form)
    return a

hhh(k)


