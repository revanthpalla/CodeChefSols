n = int(input())

val = [int(i) for i in input().split()][0:n]
val.append(999999999)

out = []
flag = 1
for i in range(n):
    for j in range(i+1,n):
        if val[i]>=val[j]:
            flag = 1
            continue
        else:
            flag = 0
            break
    if flag == 1:
        out.append(val[i])
    flag = 1

for i in range(len(out)):
    print(out[i],end=' ')

