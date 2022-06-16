def validate(s):
    if len(s)<10:
        return 0
    numC = 0
    spC = 0
    smallAlphaC = 0
    capitalAlphaC = 0

    for i in s:
         
        if(ord(i)>= 48 and ord(i)<58):
            numC += 1 
        if(ord(i)>= 65 and ord(i)<91):
            capitalAlphaC += 1 
        if(ord(i)>= 97 and ord(i)<123):
            smallAlphaC += 1 
        if(ord(i) == 35 or ord(i) == 36 or ord(i) == 42 or ord(i) == 64 or ord(i) == 45 ):
            spC += 1

 

    if(numC == 0 or capitalAlphaC == 0 or smallAlphaC == 0 or spC == 0):
        return 0
    else:
        return 1 

s = input()

ans = validate(s)
print(ans)