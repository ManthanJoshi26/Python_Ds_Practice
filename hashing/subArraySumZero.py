l = list(map(int,input().split()))
n = len(l)
t = []
for i in range(n):
    for j in range(i+1,n+1):
        if(sum(l[i:j]) == 0):
            t.append(l[i:j])

print(t)


l = list(map(int,input().split()))
n = len(l)
s = set()
sum = 0
t = []
for i in range(n):
    sum += l[i]
    if sum == 0 or sum in s:
        print("true")
    s.add(sum)

