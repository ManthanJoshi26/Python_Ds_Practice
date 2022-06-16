s = input()
s = s.lower()
count = 0
for i in range(97,123):
    if chr(i) in s:
        count += 1
        
if count == 26:
    print("Panagram ")
else:
    print("No Panagram ")