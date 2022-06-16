s = input()

l = ['a','e','i','o','u']
count = 0
for i in s:
    if i in l:
        count += 1
        
print(count)