def verify(b,n):
    l = []
    flag = 0
    for i in range(n):
        if b[i]=='(':
            l.append(b[i])
        elif b[i]==')' and len(l)!=0:
            l.pop()
        else:
            flag = 1
            break
    if flag==0 and len(l)==0:
        return True
    else:
        return False


        
b = input()
n = len(b)
b = list(b)
i = 0
c = 0
while i<n:
    if verify(b,n):
        c += 1
    x = b.pop(0)
    b.append(x)
    i += 1

print(c)

    
