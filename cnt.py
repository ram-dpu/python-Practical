str=input("enter a number")
cntv=0
cntc=0
vowel="aeiou"
str=str.lower()
for char in str:
    if char in vowel:
        cntv+=1
    else:
        cntc+=1
print("count of vowel in worlds",cntv)      
