d = {}
arr = list(map(int,input().split()))        
for i in arr:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
        
count = 0
for k,v in d.items():
    if v == 1:
        count += 1
print(count)