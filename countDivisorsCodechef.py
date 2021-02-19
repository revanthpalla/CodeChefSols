l,r,k = [int(i) for i in input().split()]

count = 0
if k>r:
    print(0)
else:
    for i in range(l,r+1):
        if i%k==0:
            count += 1

    print(count)
