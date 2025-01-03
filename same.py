n=int(input("enter a number"))
a,b=0,1
print("fibonaci series")
for _ in range(n):
   print(a,end=" ")
   a,b=b,a+b
   
