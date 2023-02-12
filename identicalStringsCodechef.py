t = int(input())

while t:
    s1,s2 = [i for i in input().split()]
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    print(l1)
    print(l2)
    flag = 0
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            flag = 1
            break
    if(flag==1):
        print('NO')
    else:
        print('YES')
    t -= 1