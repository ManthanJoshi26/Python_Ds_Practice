l = list(map(int,input().split()))
d ={}
count = 0

for i in l:
    if i not in d:
        d[i] = count
        count += 1

print(d)
print("unique elements :" + str(len(d)))