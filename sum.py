n=int(input("enter a number"))
sum=0
while(n!=0):
  last=n%10
  sum+=last
  n//=10
print("sum of digit",sum)
