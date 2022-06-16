s = input()
s = s.lower()
count = 0
l = ''
for i in range(97,123):
    if chr(i) in s:
        count += 1
    elif chr(i) not in l:
        l += chr(i)
                
if count == 26:
    print("String is already Panagram")
else:
    print("Missing value in Panagram :" + l)