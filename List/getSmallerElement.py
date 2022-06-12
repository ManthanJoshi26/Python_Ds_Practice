l = list(map(int,input().split()))

x = int(input())

ans = []

for i in l:
    if i<x:
        ans.append(i)

print(ans)


print(l[0:10:2])