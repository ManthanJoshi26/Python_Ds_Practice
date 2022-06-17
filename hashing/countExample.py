l = list(map(int,input().split()))
sum = 10
d = {}
x = enumerate(l)

for ind,val in enumerate(l):
    print(f"index value : {ind}")
    f"value of val : {val}"
    temp = sum - val
    print(f"temp val : {temp}")
    if temp in d:
        print("True")
    elif temp not in d:
        d[val] = ind

print("False")